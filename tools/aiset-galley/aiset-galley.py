#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Аркадий Лазарев
# SPDX-License-Identifier: Apache-2.0
"""AISET Galley Operator.

A small, dependency-free command-line tool that enforces the safety
invariants required of an AISET Galley task executor:

- exactly-once execution per (task_id, attempt) with a durable lock;
- explicit approval consumption (an approval token is used once and only
  once);
- power-loss classification for a lock that was left in a non-terminal
  phase by a prior, interrupted run;
- SHA-256 evidence checksums for every changed path;
- protected-source checks (a changed path must never touch a forbidden
  path such as ``.git``, ``.github``, ``src``, ``infrastructure``,
  ``sandbox``);
- mandatory enforcement of the *complete* changed-path set (staged,
  unstaged, and untracked) against a task's ``allowed_paths`` allowlist,
  failing closed the moment any changed path is not explicitly allowed;
- a hard guard that blocks the Operator itself from ever invoking
  ``git commit`` or ``git push``;
- refusal to leave Python bytecode artifacts (``__pycache__``, ``*.pyc``,
  ``*.pyo``) behind in the governed worktree.

Run ``python -B aiset-galley.py selftest`` to execute the embedded,
dependency-free test suite (see ``run_selftest`` below). The selftest
never modifies the real repository: every scenario, including the
negative "unauthorized path" case, is built inside an isolated temporary
git repository that is deleted when the test finishes.

This tool is operational tooling for the AISET Galley control plane. It
is not a normative AISET specification artifact; see
``docs/operations/AISET-GALLEY-OPERATOR.md`` for the operational
contract and ``README.md`` in this directory for usage and licensing
status.
"""

from __future__ import annotations

import sys

# Bytecode-artifact prevention (see docs/operations/AISET-GALLEY-OPERATOR.md
# and README.md, "Bytecode policy"). This must be set before any further
# imports so that no ``__pycache__``/``*.pyc`` is written for this process,
# regardless of whether the caller also used ``-B`` or
# ``PYTHONDONTWRITEBYTECODE=1``.
sys.dont_write_bytecode = True

import argparse  # noqa: E402
import enum  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402
import tempfile  # noqa: E402
import unittest  # noqa: E402
from dataclasses import dataclass, field  # noqa: E402
from datetime import datetime, timezone  # noqa: E402
from pathlib import Path  # noqa: E402
from typing import Iterable, Mapping, Optional, Sequence  # noqa: E402

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

SCRIPT_VERSION = "1.0.0"


# ---------------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------------


class GalleyOperatorError(Exception):
    """Base class for every fail-closed Operator error."""


class UnauthorizedPathError(GalleyOperatorError):
    """A changed path fell outside the task's ``allowed_paths`` allowlist."""


class ProtectedSourceError(GalleyOperatorError):
    """A changed path touched a protected/forbidden source path."""


class AlreadyExecutedError(GalleyOperatorError):
    """Exactly-once execution was violated: this task already completed."""


class ApprovalError(GalleyOperatorError):
    """The approval token is missing, not granted, or already consumed."""


class CommitPushBlockedError(GalleyOperatorError):
    """The Operator's own commit/push guard rejected a git subcommand."""


class BytecodeArtifactError(GalleyOperatorError):
    """A Python bytecode artifact was found in the governed worktree."""


class PowerLossDetectedError(GalleyOperatorError):
    """A prior run's lock was left in a non-terminal phase.

    The caller must explicitly pass ``--resume`` (to continue the same
    attempt) or ``--force-reset`` (to discard the stale lock after manual
    review) — the Operator never silently guesses which is safe.
    """

    def __init__(self, classification: "PowerLossClassification", state: Mapping[str, object]):
        self.classification = classification
        self.state = dict(state)
        super().__init__(
            "prior run for task_id={task_id!r} attempt_id={attempt_id!r} did not "
            "complete (classified as {classification}); rerun with --resume to "
            "continue that attempt or --force-reset to discard the stale lock "
            "after manual review".format(
                task_id=self.state.get("task_id"),
                attempt_id=self.state.get("attempt_id"),
                classification=classification.value,
            )
        )


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------


def _iso_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


_SAFE_NAME_RE = re.compile(r"[^A-Za-z0-9_.-]+")


def _safe_name(value: str) -> str:
    return _SAFE_NAME_RE.sub("_", value)


def _repo_root(start: Optional[Path] = None) -> Path:
    """Resolve the git worktree root, failing closed if it cannot be found."""

    start = start or Path(__file__).resolve().parent
    result = subprocess.run(
        ["git", "-C", str(start), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise GalleyOperatorError(
            f"could not resolve git worktree root from {start}: {result.stderr.strip()}"
        )
    return Path(result.stdout.strip())


# ---------------------------------------------------------------------------
# Changed-path-set enforcement (mandatory, fail-closed)
# ---------------------------------------------------------------------------


def compute_changed_paths(repo_root: Path) -> set:
    """Return the *complete* changed-path set: staged + unstaged + untracked.

    Fails closed (raises) if ``repo_root`` is not a readable git worktree or
    if ``git status`` cannot be executed — an enforcement function must
    never silently treat "git failed" as "nothing changed".
    """

    result = subprocess.run(
        [
            "git",
            "-C",
            str(repo_root),
            "status",
            "--porcelain=v1",
            "--untracked-files=all",
            "--no-renames",
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise GalleyOperatorError(
            f"'git status' failed in {repo_root}: {result.stderr.strip()}"
        )

    changed = set()
    for line in result.stdout.splitlines():
        if not line:
            continue
        # Porcelain v1 lines are "XY <path>" (XY = two status characters).
        path = line[3:]
        if len(path) >= 2 and path[0] == '"' and path[-1] == '"':
            # git quotes paths containing special/non-ASCII characters.
            path = path[1:-1].encode("utf-8").decode("unicode_escape")
        changed.add(path.replace("\\", "/"))
    return changed


def _is_authorized(path: str, allowed_paths: Sequence[str]) -> bool:
    for allowed in allowed_paths:
        allowed_norm = allowed.replace("\\", "/")
        if path == allowed_norm:
            return True
        if allowed_norm.endswith("/") and path.startswith(allowed_norm):
            return True
        # Directory-prefix match for allowlist entries that name a directory.
        if path.startswith(allowed_norm.rstrip("/") + "/"):
            return True
    return False


def enforce_allowed_paths(changed_paths: Iterable[str], allowed_paths: Sequence[str]) -> None:
    """Fail closed if any changed path is outside ``allowed_paths``.

    This is the mandatory full changed-path-set enforcement required by the
    Operator: every entry in ``changed_paths`` (which must already be the
    *complete* set from :func:`compute_changed_paths`, i.e. staged +
    unstaged + untracked) is checked; the function raises on the first
    violation rather than only checking a subset of the working tree.
    """

    unauthorized = sorted(
        p for p in changed_paths if not _is_authorized(p, allowed_paths)
    )
    if unauthorized:
        raise UnauthorizedPathError(
            "unauthorized changed path(s) outside allowed_paths: "
            + ", ".join(unauthorized)
        )


def check_protected_paths(changed_paths: Iterable[str], protected_paths: Sequence[str]) -> None:
    """Fail closed if any changed path touches a protected/forbidden path."""

    for path in changed_paths:
        for protected in protected_paths:
            protected_norm = protected.replace("\\", "/").rstrip("/")
            if path == protected_norm or path.startswith(protected_norm + "/"):
                raise ProtectedSourceError(
                    f"changed path '{path}' touches protected source '{protected}'"
                )


# ---------------------------------------------------------------------------
# Bytecode-artifact rejection
# ---------------------------------------------------------------------------


def find_bytecode_artifacts(root: Path) -> list:
    """Return every ``__pycache__`` dir / ``*.pyc`` / ``*.pyo`` under ``root``.

    ``.git`` is excluded from the walk (its internal contents are not
    Operator-governed worktree files).
    """

    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        if "__pycache__" in dirnames:
            found.append(str(Path(dirpath) / "__pycache__"))
        for name in filenames:
            if name.endswith(".pyc") or name.endswith(".pyo"):
                found.append(str(Path(dirpath) / name))
    return sorted(found)


def reject_bytecode_artifacts(root: Path) -> None:
    artifacts = find_bytecode_artifacts(root)
    if artifacts:
        raise BytecodeArtifactError(
            "Python bytecode artifacts are forbidden in the governed worktree: "
            + ", ".join(artifacts)
        )


# ---------------------------------------------------------------------------
# Commit/push blocking guard
# ---------------------------------------------------------------------------


_BLOCKED_GIT_SUBCOMMANDS = {"commit", "push", "reset", "rebase", "tag", "branch"}


def run_git(args: Sequence[str], cwd: Path) -> subprocess.CompletedProcess:
    """Run a git subcommand, hard-blocking commit/push (and other
    history-mutating subcommands) before they ever reach ``subprocess``.

    This is the only place in the Operator that is allowed to shell out to
    git; every other function in this module goes through it (directly or
    indirectly) so the guard cannot be bypassed by a future code path.
    """

    if not args:
        raise GalleyOperatorError("run_git() called with an empty argument list")
    subcommand = args[0]
    if subcommand in _BLOCKED_GIT_SUBCOMMANDS:
        raise CommitPushBlockedError(
            f"git subcommand '{subcommand}' is blocked by the Operator's "
            "commit/push guard and must be performed by a human, never by "
            "the Operator itself"
        )
    result = subprocess.run(
        ["git", "-C", str(cwd), *args], capture_output=True, text=True
    )
    if result.returncode != 0:
        raise GalleyOperatorError(
            f"git {' '.join(args)} failed in {cwd}: {result.stderr.strip()}"
        )
    return result


# ---------------------------------------------------------------------------
# Exactly-once execution + power-loss classification
# ---------------------------------------------------------------------------


class RunPhase(str, enum.Enum):
    STARTED = "started"
    APPROVAL_CONSUMED = "approval_consumed"
    CHANGES_VERIFIED = "changes_verified"
    EVIDENCE_RECORDED = "evidence_recorded"
    COMPLETED = "completed"


class PowerLossClassification(str, enum.Enum):
    NONE = "none"
    INTERRUPTED_BEFORE_APPROVAL = "interrupted_before_approval"
    INTERRUPTED_AFTER_APPROVAL_BEFORE_CHANGES = "interrupted_after_approval_before_changes"
    INTERRUPTED_AFTER_CHANGES_BEFORE_EVIDENCE = "interrupted_after_changes_before_evidence"
    INTERRUPTED_AFTER_EVIDENCE_BEFORE_COMPLETE = "interrupted_after_evidence_before_complete"


_PHASE_TO_CLASSIFICATION = {
    RunPhase.STARTED.value: PowerLossClassification.INTERRUPTED_BEFORE_APPROVAL,
    RunPhase.APPROVAL_CONSUMED.value: PowerLossClassification.INTERRUPTED_AFTER_APPROVAL_BEFORE_CHANGES,
    RunPhase.CHANGES_VERIFIED.value: PowerLossClassification.INTERRUPTED_AFTER_CHANGES_BEFORE_EVIDENCE,
    RunPhase.EVIDENCE_RECORDED.value: PowerLossClassification.INTERRUPTED_AFTER_EVIDENCE_BEFORE_COMPLETE,
}


def classify_power_loss(state: Mapping[str, object]) -> PowerLossClassification:
    phase = state.get("phase")
    if phase == RunPhase.COMPLETED.value:
        return PowerLossClassification.NONE
    return _PHASE_TO_CLASSIFICATION.get(
        str(phase), PowerLossClassification.INTERRUPTED_BEFORE_APPROVAL
    )


class ExecutionLock:
    """A durable, exactly-once execution lock for one ``task_id``.

    The lock file is written atomically (write to a temp file, then
    ``os.replace``) so an interrupted write never leaves a half-written,
    unparseable lock behind.
    """

    def __init__(self, state_dir: Path, task_id: str):
        self.state_dir = Path(state_dir)
        self.task_id = task_id
        self.path = self.state_dir / f"{_safe_name(task_id)}.lock.json"

    def _read(self) -> Optional[dict]:
        if not self.path.exists():
            return None
        return json.loads(self.path.read_text(encoding="utf-8"))

    def _write(self, state: Mapping[str, object]) -> None:
        self.state_dir.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
        os.replace(tmp, self.path)

    def acquire(self, attempt_id: str, *, resume: bool = False, force_reset: bool = False) -> dict:
        existing = self._read()
        if existing is not None and not force_reset:
            classification = classify_power_loss(existing)
            if classification is PowerLossClassification.NONE:
                raise AlreadyExecutedError(
                    f"task_id={self.task_id!r} already completed at "
                    f"{existing.get('completed_at')}; exactly-once execution "
                    "forbids rerunning it"
                )
            if not resume:
                raise PowerLossDetectedError(classification, existing)
            if existing.get("attempt_id") != attempt_id:
                raise GalleyOperatorError(
                    "cannot resume: the existing lock belongs to a different "
                    f"attempt_id ({existing.get('attempt_id')!r} != {attempt_id!r})"
                )
            return existing

        state = {
            "task_id": self.task_id,
            "attempt_id": attempt_id,
            "phase": RunPhase.STARTED.value,
            "started_at": _iso_now(),
        }
        self._write(state)
        return state

    def advance(self, state: Mapping[str, object], phase: RunPhase) -> dict:
        new_state = dict(state)
        new_state["phase"] = phase.value
        new_state[f"{phase.value}_at"] = _iso_now()
        if phase is RunPhase.COMPLETED:
            new_state["completed_at"] = _iso_now()
        self._write(new_state)
        return new_state

    def current(self) -> Optional[dict]:
        return self._read()


# ---------------------------------------------------------------------------
# Approval consumption
# ---------------------------------------------------------------------------


def consume_approval(approval_path: Path, task_id: str) -> dict:
    """Consume a one-time approval token, failing closed on any anomaly."""

    if not approval_path.exists():
        raise ApprovalError(f"approval file not found: {approval_path}")
    data = json.loads(approval_path.read_text(encoding="utf-8"))
    if data.get("task_id") != task_id:
        raise ApprovalError(
            f"approval task_id {data.get('task_id')!r} does not match {task_id!r}"
        )
    if not data.get("approved"):
        raise ApprovalError(f"approval for task_id={task_id!r} was not granted")
    if data.get("consumed"):
        raise ApprovalError(f"approval for task_id={task_id!r} was already consumed")
    data["consumed"] = True
    data["consumed_at"] = _iso_now()
    approval_path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    return data


# ---------------------------------------------------------------------------
# Evidence checksums
# ---------------------------------------------------------------------------


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def compute_evidence_checksums(repo_root: Path, changed_paths: Iterable[str]) -> dict:
    """SHA-256 (lowercase, 64-hex, per the repository's checksum policy) for
    every changed path. A path that no longer exists (e.g. deleted) is
    recorded explicitly as ``None`` rather than silently omitted.
    """

    checksums = {}
    for rel in sorted(changed_paths):
        full = repo_root / rel
        checksums[rel] = sha256_file(full) if full.is_file() else None
    return checksums


def write_evidence_manifest(
    evidence_dir: Path, task_id: str, attempt_id: str, checksums: Mapping[str, Optional[str]]
) -> Path:
    evidence_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = (
        evidence_dir / f"{_safe_name(task_id)}-{_safe_name(attempt_id)}-evidence.json"
    )
    payload = {
        "task_id": task_id,
        "attempt_id": attempt_id,
        "generated_at": _iso_now(),
        "checksum_algorithm": "sha256",
        "files": dict(checksums),
    }
    manifest_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    return manifest_path


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------


@dataclass
class OperatorConfig:
    task_id: str
    allowed_paths: list = field(default_factory=list)
    forbidden_paths: list = field(default_factory=list)
    protected_source_paths: list = field(default_factory=list)
    state_dir: str = ""
    evidence_dir: str = ""
    approval_file: str = ""

    @classmethod
    def load(cls, path: Path) -> "OperatorConfig":
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
        default_state = str(Path(tempfile.gettempdir()) / "aiset-galley" / "state")
        default_evidence = str(Path(tempfile.gettempdir()) / "aiset-galley" / "evidence")
        default_approval = str(
            Path(tempfile.gettempdir()) / "aiset-galley" / "approval.json"
        )
        protected = raw.get("protected_source_paths", raw.get("forbidden_paths", []))
        return cls(
            task_id=raw["task_id"],
            allowed_paths=list(raw.get("allowed_paths", [])),
            forbidden_paths=list(raw.get("forbidden_paths", [])),
            protected_source_paths=list(protected),
            state_dir=raw.get("state_dir") or default_state,
            evidence_dir=raw.get("evidence_dir") or default_evidence,
            approval_file=raw.get("approval_file") or default_approval,
        )


# ---------------------------------------------------------------------------
# CLI commands
# ---------------------------------------------------------------------------


def cmd_run(args: argparse.Namespace) -> int:
    config = OperatorConfig.load(args.config)
    repo_root = Path(args.repo_root).resolve() if args.repo_root else _repo_root()

    lock = ExecutionLock(Path(config.state_dir), config.task_id)
    try:
        state = lock.acquire(
            args.attempt_id, resume=args.resume, force_reset=args.force_reset
        )

        if state["phase"] == RunPhase.STARTED.value:
            consume_approval(Path(config.approval_file), config.task_id)
            state = lock.advance(state, RunPhase.APPROVAL_CONSUMED)

        if state["phase"] == RunPhase.APPROVAL_CONSUMED.value:
            changed = compute_changed_paths(repo_root)
            check_protected_paths(changed, config.protected_source_paths)
            enforce_allowed_paths(changed, config.allowed_paths)
            state = lock.advance(state, RunPhase.CHANGES_VERIFIED)
        else:
            changed = compute_changed_paths(repo_root)

        if state["phase"] == RunPhase.CHANGES_VERIFIED.value:
            checksums = compute_evidence_checksums(repo_root, changed)
            write_evidence_manifest(
                Path(config.evidence_dir), config.task_id, args.attempt_id, checksums
            )
            state = lock.advance(state, RunPhase.EVIDENCE_RECORDED)

        reject_bytecode_artifacts(repo_root)

        state = lock.advance(state, RunPhase.COMPLETED)
        print(json.dumps(state, indent=2, sort_keys=True))
        return 0
    except GalleyOperatorError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


def cmd_status(args: argparse.Namespace) -> int:
    config = OperatorConfig.load(args.config)
    lock = ExecutionLock(Path(config.state_dir), config.task_id)
    state = lock.current()
    if state is None:
        print(json.dumps({"task_id": config.task_id, "phase": None}, indent=2))
        return 0
    print(json.dumps(state, indent=2, sort_keys=True))
    return 0


# ---------------------------------------------------------------------------
# Embedded selftest suite
# ---------------------------------------------------------------------------


class _TempGitRepo:
    """An isolated, throwaway git repository used only by the selftest.

    No selftest scenario is ever built inside the real AISET worktree —
    every fixture, including the negative "unauthorized path" case, lives
    entirely inside this temporary repository and is deleted on exit.
    """

    def __enter__(self) -> Path:
        self._tmp = tempfile.mkdtemp(prefix="aiset-galley-selftest-")
        root = Path(self._tmp)
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        subprocess.run(
            ["git", "-C", str(root), "config", "user.email", "selftest@example.invalid"],
            check=True,
        )
        subprocess.run(
            ["git", "-C", str(root), "config", "user.name", "aiset-galley-selftest"],
            check=True,
        )
        (root / ".gitkeep").write_text("", encoding="utf-8")
        subprocess.run(["git", "-C", str(root), "add", "-A"], check=True)
        subprocess.run(
            ["git", "-C", str(root), "commit", "-q", "-m", "selftest baseline"],
            check=True,
        )
        return root

    def __exit__(self, *exc_info) -> None:
        shutil.rmtree(self._tmp, ignore_errors=True)


class ChangedPathEnforcementTests(unittest.TestCase):
    def test_only_allowed_paths_passes(self):
        with _TempGitRepo() as repo:
            target = repo / "tools" / "aiset-galley" / "aiset-galley.py"
            target.parent.mkdir(parents=True)
            target.write_text("# authorized change\n", encoding="utf-8")
            changed = compute_changed_paths(repo)
            self.assertEqual(changed, {"tools/aiset-galley/aiset-galley.py"})
            enforce_allowed_paths(changed, ["tools/aiset-galley/aiset-galley.py"])

    def test_unauthorized_path_is_rejected(self):
        """Negative test (required by AC2/AC4): an unauthorized changed path
        must be detected in the complete changed-path set and rejected.
        The fixture lives only inside the temporary repo, never the real one.
        """

        with _TempGitRepo() as repo:
            target = repo / "tools" / "aiset-galley" / "aiset-galley.py"
            target.parent.mkdir(parents=True)
            target.write_text("# authorized change\n", encoding="utf-8")
            unauthorized = repo / "src" / "unauthorized.txt"
            unauthorized.parent.mkdir(parents=True)
            unauthorized.write_text("this path is not on the allowlist\n", encoding="utf-8")

            changed = compute_changed_paths(repo)
            self.assertIn("src/unauthorized.txt", changed)
            with self.assertRaises(UnauthorizedPathError) as ctx:
                enforce_allowed_paths(changed, ["tools/aiset-galley/aiset-galley.py"])
            self.assertIn("src/unauthorized.txt", str(ctx.exception))

    def test_untracked_files_are_included(self):
        with _TempGitRepo() as repo:
            (repo / "untracked.txt").write_text("never added or committed\n", encoding="utf-8")
            changed = compute_changed_paths(repo)
            self.assertIn("untracked.txt", changed)

    def test_modified_tracked_file_is_included(self):
        with _TempGitRepo() as repo:
            (repo / ".gitkeep").write_text("modified\n", encoding="utf-8")
            changed = compute_changed_paths(repo)
            self.assertIn(".gitkeep", changed)

    def test_staged_file_is_included(self):
        with _TempGitRepo() as repo:
            (repo / "staged.txt").write_text("staged\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(repo), "add", "staged.txt"], check=True)
            changed = compute_changed_paths(repo)
            self.assertIn("staged.txt", changed)

    def test_non_git_directory_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(GalleyOperatorError):
                compute_changed_paths(Path(tmp))


class ProtectedSourceTests(unittest.TestCase):
    PROTECTED = [".git", ".github", "src", "infrastructure", "sandbox"]

    def test_protected_path_is_rejected(self):
        with self.assertRaises(ProtectedSourceError):
            check_protected_paths({"src/core.py"}, self.PROTECTED)

    def test_protected_path_exact_match_is_rejected(self):
        with self.assertRaises(ProtectedSourceError):
            check_protected_paths({"sandbox"}, self.PROTECTED)

    def test_unrelated_path_is_not_rejected(self):
        check_protected_paths({"docs/operations/AISET-GALLEY-OPERATOR.md"}, self.PROTECTED)

    def test_similar_prefix_is_not_falsely_rejected(self):
        # "srcish/" must not be treated as inside protected "src".
        check_protected_paths({"srcish/file.txt"}, self.PROTECTED)


class BytecodeArtifactTests(unittest.TestCase):
    def test_dont_write_bytecode_is_enabled(self):
        self.assertTrue(sys.dont_write_bytecode)

    def test_clean_directory_has_no_artifacts(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(find_bytecode_artifacts(Path(tmp)), [])

    def test_pycache_directory_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "__pycache__").mkdir()
            (root / "__pycache__" / "mod.cpython-311.pyc").write_text("", encoding="utf-8")
            artifacts = find_bytecode_artifacts(root)
            self.assertTrue(any("__pycache__" in a for a in artifacts))
            with self.assertRaises(BytecodeArtifactError):
                reject_bytecode_artifacts(root)

    def test_stray_pyc_file_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "stray.pyc").write_text("", encoding="utf-8")
            with self.assertRaises(BytecodeArtifactError):
                reject_bytecode_artifacts(root)

    def test_git_internal_pycache_is_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".git" / "hooks" / "__pycache__").mkdir(parents=True)
            self.assertEqual(find_bytecode_artifacts(root), [])


class CommitPushBlockingTests(unittest.TestCase):
    def test_commit_is_blocked(self):
        with _TempGitRepo() as repo:
            with self.assertRaises(CommitPushBlockedError):
                run_git(["commit", "-m", "should never happen"], repo)

    def test_push_is_blocked(self):
        with _TempGitRepo() as repo:
            with self.assertRaises(CommitPushBlockedError):
                run_git(["push"], repo)

    def test_force_push_is_blocked(self):
        with _TempGitRepo() as repo:
            with self.assertRaises(CommitPushBlockedError):
                run_git(["push", "--force"], repo)

    def test_reset_is_blocked(self):
        with _TempGitRepo() as repo:
            with self.assertRaises(CommitPushBlockedError):
                run_git(["reset", "--hard"], repo)

    def test_status_is_allowed(self):
        with _TempGitRepo() as repo:
            result = run_git(["status", "--porcelain"], repo)
            self.assertEqual(result.returncode, 0)


class ApprovalConsumptionTests(unittest.TestCase):
    def test_missing_approval_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ApprovalError):
                consume_approval(Path(tmp) / "missing.json", "TASK-1")

    def test_task_id_mismatch_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            approval_path = Path(tmp) / "approval.json"
            approval_path.write_text(
                json.dumps({"task_id": "OTHER-TASK", "approved": True}), encoding="utf-8"
            )
            with self.assertRaises(ApprovalError):
                consume_approval(approval_path, "TASK-1")

    def test_not_approved_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            approval_path = Path(tmp) / "approval.json"
            approval_path.write_text(
                json.dumps({"task_id": "TASK-1", "approved": False}), encoding="utf-8"
            )
            with self.assertRaises(ApprovalError):
                consume_approval(approval_path, "TASK-1")

    def test_valid_approval_is_consumed_exactly_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            approval_path = Path(tmp) / "approval.json"
            approval_path.write_text(
                json.dumps({"task_id": "TASK-1", "approved": True}), encoding="utf-8"
            )
            consume_approval(approval_path, "TASK-1")
            with self.assertRaises(ApprovalError):
                consume_approval(approval_path, "TASK-1")


class ExecutionLockTests(unittest.TestCase):
    def test_exactly_once_execution(self):
        with tempfile.TemporaryDirectory() as tmp:
            lock = ExecutionLock(Path(tmp), "TASK-1")
            state = lock.acquire("attempt-1")
            for phase in (
                RunPhase.APPROVAL_CONSUMED,
                RunPhase.CHANGES_VERIFIED,
                RunPhase.EVIDENCE_RECORDED,
                RunPhase.COMPLETED,
            ):
                state = lock.advance(state, phase)
            with self.assertRaises(AlreadyExecutedError):
                lock.acquire("attempt-2")

    def test_power_loss_is_classified_and_blocks_by_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            lock = ExecutionLock(Path(tmp), "TASK-1")
            state = lock.acquire("attempt-1")
            state = lock.advance(state, RunPhase.APPROVAL_CONSUMED)
            with self.assertRaises(PowerLossDetectedError) as ctx:
                lock.acquire("attempt-2")
            self.assertEqual(
                ctx.exception.classification,
                PowerLossClassification.INTERRUPTED_AFTER_APPROVAL_BEFORE_CHANGES,
            )

    def test_resume_continues_the_same_attempt(self):
        with tempfile.TemporaryDirectory() as tmp:
            lock = ExecutionLock(Path(tmp), "TASK-1")
            state = lock.acquire("attempt-1")
            state = lock.advance(state, RunPhase.APPROVAL_CONSUMED)
            resumed = lock.acquire("attempt-1", resume=True)
            self.assertEqual(resumed["phase"], RunPhase.APPROVAL_CONSUMED.value)

    def test_resume_rejects_a_different_attempt_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            lock = ExecutionLock(Path(tmp), "TASK-1")
            state = lock.acquire("attempt-1")
            lock.advance(state, RunPhase.APPROVAL_CONSUMED)
            with self.assertRaises(GalleyOperatorError):
                lock.acquire("attempt-2", resume=True)

    def test_force_reset_discards_a_stale_lock(self):
        with tempfile.TemporaryDirectory() as tmp:
            lock = ExecutionLock(Path(tmp), "TASK-1")
            state = lock.acquire("attempt-1")
            lock.advance(state, RunPhase.APPROVAL_CONSUMED)
            fresh = lock.acquire("attempt-2", force_reset=True)
            self.assertEqual(fresh["phase"], RunPhase.STARTED.value)
            self.assertEqual(fresh["attempt_id"], "attempt-2")

    def test_classification_none_when_completed(self):
        self.assertEqual(
            classify_power_loss({"phase": RunPhase.COMPLETED.value}),
            PowerLossClassification.NONE,
        )

    def test_classification_before_approval(self):
        self.assertEqual(
            classify_power_loss({"phase": RunPhase.STARTED.value}),
            PowerLossClassification.INTERRUPTED_BEFORE_APPROVAL,
        )

    def test_classification_after_evidence(self):
        self.assertEqual(
            classify_power_loss({"phase": RunPhase.EVIDENCE_RECORDED.value}),
            PowerLossClassification.INTERRUPTED_AFTER_EVIDENCE_BEFORE_COMPLETE,
        )


class EvidenceChecksumTests(unittest.TestCase):
    def test_known_sha256_vector(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "file.txt"
            path.write_bytes(b"abc")
            self.assertEqual(
                sha256_file(path),
                "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
            )

    def test_checksums_are_lowercase_64_hex(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "a.txt").write_text("hello\n", encoding="utf-8")
            checksums = compute_evidence_checksums(root, ["a.txt"])
            digest = checksums["a.txt"]
            self.assertEqual(len(digest), 64)
            self.assertEqual(digest, digest.lower())
            self.assertTrue(all(c in "0123456789abcdef" for c in digest))

    def test_missing_path_is_recorded_as_none(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            checksums = compute_evidence_checksums(root, ["does-not-exist.txt"])
            self.assertIsNone(checksums["does-not-exist.txt"])

    def test_manifest_round_trips(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "a.txt").write_text("hello\n", encoding="utf-8")
            checksums = compute_evidence_checksums(root, ["a.txt"])
            manifest_path = write_evidence_manifest(root / "evidence", "TASK-1", "attempt-1", checksums)
            payload = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["checksum_algorithm"], "sha256")
            self.assertEqual(payload["files"], checksums)


def run_selftest() -> int:
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Post-condition required by AC3: the selftest itself must not have left
    # bytecode artifacts behind in this tool's own directory.
    own_dir = Path(__file__).resolve().parent
    artifacts = find_bytecode_artifacts(own_dir)
    if artifacts:
        print(
            "FAIL: bytecode artifacts present after selftest: " + ", ".join(artifacts),
            file=sys.stderr,
        )
        return 1

    return 0 if result.wasSuccessful() else 1


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="aiset-galley", description="AISET Galley Operator (safety-control CLI)"
    )
    parser.add_argument(
        "--version", action="version", version=f"aiset-galley {SCRIPT_VERSION}"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    run_p = sub.add_parser("run", help="Execute one Operator pass for a task attempt")
    run_p.add_argument("--config", required=True, type=Path)
    run_p.add_argument("--attempt-id", required=True)
    run_p.add_argument("--repo-root", type=Path, default=None)
    run_p.add_argument(
        "--resume", action="store_true", help="Acknowledge a classified power-loss and continue"
    )
    run_p.add_argument(
        "--force-reset",
        action="store_true",
        help="Discard a stale lock after manual review and start a fresh attempt",
    )

    sub.add_parser("selftest", help="Run the embedded Operator selftest suite")

    status_p = sub.add_parser("status", help="Print the exactly-once lock state for a task_id")
    status_p.add_argument("--config", required=True, type=Path)

    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_arg_parser().parse_args(argv)
    if args.command == "selftest":
        return run_selftest()
    if args.command == "run":
        return cmd_run(args)
    if args.command == "status":
        return cmd_status(args)
    return 2  # pragma: no cover - argparse enforces a valid subcommand


if __name__ == "__main__":
    sys.exit(main())
