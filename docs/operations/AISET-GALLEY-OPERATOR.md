# AISET Galley Operator — Operational Specification

**Component:** `tools/aiset-galley/aiset-galley.py`

**Status:** Operational tooling (non-normative; supports the AISET Galley
control plane, not an AISET specification artifact).

**Related:** [`tools/aiset-galley/README.md`](../../tools/aiset-galley/README.md),
[`governance/development/AISET-AI-ASSISTED-DEVELOPMENT-MODEL-001.md`](../../governance/development/AISET-AI-ASSISTED-DEVELOPMENT-MODEL-001.md)

## Purpose

The AISET Galley Operator is the safety-control layer that governs how an
autonomous or AFK Galley task executor is allowed to act inside a repository
worktree. It exists to make a small number of invariants mechanically
enforced rather than merely documented, so that an executor cannot, through
error or scope drift, exceed the boundaries a task was given.

## Required behavior

An Operator-governed task run **must**:

1. Execute **exactly once** per `task_id`. A task that already reached the
   `completed` phase must never be re-run; the Operator fails closed
   (`AlreadyExecutedError`) if this is attempted.
2. **Consume its approval token exactly once.** An approval that is
   missing, not granted, or already consumed must block the run
   (`ApprovalError`).
3. **Classify power loss.** If a prior run's lock file was left in a
   non-terminal phase (`started`, `approval_consumed`, `changes_verified`,
   or `evidence_recorded`), the Operator must classify which phase the
   interrupted run reached and refuse to silently resume or silently
   restart. Continuation requires an explicit, human-reviewable decision:
   `--resume` (continue that same attempt) or `--force-reset` (discard the
   stale lock after manual review).
4. **Compute and enforce the complete changed-path set.** The changed-path
   set is defined as the union of staged, unstaged, and untracked paths
   reported by `git status` for the governed worktree — never a subset.
   Every path in that set must be checked against the task's
   `allowed_paths` allowlist; if any path is not on the allowlist, the run
   fails closed (`UnauthorizedPathError`) before any further action is
   taken.
5. **Reject protected-source paths.** Any changed path that touches a
   configured protected/forbidden path (for example `.git`, `.github`,
   `src`, `infrastructure`, `sandbox`) must fail closed
   (`ProtectedSourceError`), independent of the `allowed_paths` check.
6. **Never commit or push.** The Operator must not, under any code path,
   invoke `git commit`, `git push`, `git reset`, `git rebase`, `git tag`, or
   `git branch`. Commit and push authority belongs exclusively to the human
   decision authority, per
   `governance/development/AISET-AI-ASSISTED-DEVELOPMENT-MODEL-001.md`
   §4 and §11.
7. **Record evidence checksums.** Every changed path must have a SHA-256
   checksum computed and recorded in a JSON evidence manifest, consistent
   with the repository's checksum policy (lowercase, full 64-character hex
   digest, never truncated or silently overwritten on mismatch).
8. **Leave no Python bytecode artifacts.** Neither a normal run nor the
   selftest may leave a `__pycache__` directory, a `.pyc` file, or a `.pyo`
   file inside the governed worktree. This is enforced independently of the
   caller's own `-B` / `PYTHONDONTWRITEBYTECODE` usage by setting
   `sys.dont_write_bytecode = True` inside the script itself, and by an
   explicit post-run scan that fails closed if an artifact is found.

## Verification

Verification of the Operator implementation itself (as opposed to a task it
governs) is performed by its embedded selftest:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B tools/aiset-galley/aiset-galley.py selftest
```

The selftest is a live, dependency-free `unittest` suite. It must be run,
not merely inspected, before an Operator revision is trusted. It exercises,
at minimum:

- exactly-once execution and the `AlreadyExecutedError` fail-closed path;
- power-loss classification for each non-terminal phase, and both the
  `--resume` and `--force-reset` recovery paths;
- approval consumption, including rejection of a missing, unapproved, or
  already-consumed token;
- the complete changed-path-set computation (staged, unstaged, untracked)
  against a live, temporary git repository;
- **a negative test**: an unauthorized changed path is deliberately
  introduced into an isolated temporary repository and the enforcement
  function is asserted to reject it;
- protected-source rejection;
- the commit/push guard, including `push --force`;
- SHA-256 evidence checksum correctness;
- absence of bytecode artifacts, both as a unit-level check and as a
  post-condition of the selftest run itself.

Every selftest scenario, including the negative unauthorized-path fixture,
is constructed inside a disposable temporary git repository created and
torn down by the test. No selftest scenario is ever built against, or
allowed to modify, the real repository the Operator is protecting.

## Configuration contract

See [`tools/aiset-galley/config.example.json`](../../tools/aiset-galley/config.example.json).
`allowed_paths` and `forbidden_paths` / `protected_source_paths` for a given
task are expected to mirror that task's Galley scope declaration exactly —
the Operator's enforcement is only as strict as the allowlist it is given.

## Relationship to task execution policy

This specification describes the mechanism; it does not itself grant
execution, approval, or commit authority. Human commit and push
authorization requirements defined in
`governance/development/AISET-AI-ASSISTED-DEVELOPMENT-MODEL-001.md` remain
in force regardless of what the Operator enforces mechanically.
