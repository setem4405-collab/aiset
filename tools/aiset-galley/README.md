# AISET Galley Operator

A small, dependency-free Python 3 command-line tool (`aiset-galley.py`) that
enforces the safety invariants required of an AISET Galley task executor
before, during, and after it runs.

This is operational tooling for the AISET Galley control plane. It is not a
normative AISET specification artifact — see
[`docs/operations/AISET-GALLEY-OPERATOR.md`](../../docs/operations/AISET-GALLEY-OPERATOR.md)
for the operational contract this tool implements.

## What it enforces

- **Exactly-once execution.** A durable, atomically-written lock file keyed
  by `task_id` refuses to let a completed task run again.
- **Approval consumption.** An approval token (`approval_file` in the
  config) is read, validated, and marked consumed; a token that is missing,
  not granted, or already consumed is rejected.
- **Power-loss classification.** If a prior run's lock was left in a
  non-terminal phase (for example, the process was killed mid-run), the
  Operator classifies exactly how far that run got
  (`interrupted_before_approval`, `interrupted_after_approval_before_changes`,
  `interrupted_after_changes_before_evidence`, or
  `interrupted_after_evidence_before_complete`) and refuses to silently
  guess how to proceed — the caller must pass `--resume` (continue the same
  attempt) or `--force-reset` (discard the stale lock after manual review).
- **Mandatory full changed-path-set enforcement.** Every run computes the
  *complete* changed-path set — staged, unstaged, **and untracked** files,
  via `git status --porcelain=v1 --untracked-files=all` — and fails closed
  (raises `UnauthorizedPathError`) the moment any changed path is not on the
  task's `allowed_paths` allowlist. This check is not optional and is not
  limited to a subset of the working tree.
- **Protected-source checks.** Any changed path that touches a
  `protected_source_paths` / `forbidden_paths` entry (for example `.git`,
  `.github`, `src`, `infrastructure`, `sandbox`) is rejected before any
  further action is taken.
- **Commit/push blocking.** All git access funnels through a single
  `run_git()` helper that hard-blocks `commit`, `push`, `reset`, `rebase`,
  `tag`, and `branch` before they ever reach `subprocess`. The Operator can
  never commit or push on its own authority.
- **Evidence checksums.** SHA-256 (lowercase, 64-hex, matching the
  repository's checksum policy) is computed for every changed path and
  recorded in a JSON evidence manifest.
- **No bytecode artifacts.** The script sets `sys.dont_write_bytecode = True`
  before any further imports, and independently verifies — both at the end
  of `run` and at the end of `selftest` — that no `__pycache__`, `*.pyc`, or
  `*.pyo` file exists in the governed worktree, raising
  `BytecodeArtifactError` if one is found.

## Usage

```bash
# Execute one Operator pass for a task attempt.
python -B aiset-galley.py run --config config.json --attempt-id <attempt-id>

# Resume after an acknowledged power-loss classification.
python -B aiset-galley.py run --config config.json --attempt-id <attempt-id> --resume

# Discard a stale lock after manual review and start a fresh attempt.
python -B aiset-galley.py run --config config.json --attempt-id <attempt-id> --force-reset

# Inspect the current exactly-once lock state for a task_id.
python -B aiset-galley.py status --config config.json

# Run the embedded selftest suite (see below).
python -B aiset-galley.py selftest
```

Always invoke the tool with `python -B` (or with `PYTHONDONTWRITEBYTECODE=1`
set in the environment) so no interpreter writes a `.pyc` cache for the
top-level script. The script also sets `sys.dont_write_bytecode = True`
itself as a second, independent layer of the same guard, and both `run` and
`selftest` verify afterward that no bytecode artifact was left behind.

## Configuration

See [`config.example.json`](config.example.json) for the full shape. Key
fields:

| Field | Meaning |
| --- | --- |
| `task_id` | Stable identifier for exactly-once execution and evidence naming. |
| `allowed_paths` | The complete allowlist the changed-path-set enforcement checks against. An entry may be an exact file path, or a directory path (matched as a prefix). |
| `forbidden_paths` / `protected_source_paths` | Paths that must never appear in the changed-path set. |
| `state_dir` | Where the exactly-once lock file is stored. Defaults to a path under the OS temp directory, **outside** the governed repository, so routine Operator runs never pollute `git status` in the worktree they govern. |
| `evidence_dir` | Where the SHA-256 evidence manifest is written. Same out-of-repo default rationale as `state_dir`. |
| `approval_file` | Path to the one-time approval token consumed by `run`. |

## Selftest

```bash
python -B aiset-galley.py selftest
```

The embedded selftest is a `unittest` suite covering every safety control
above, including a **negative test** (`test_unauthorized_path_is_rejected`)
that creates a fixture with one authorized file and one unauthorized file,
computes the complete changed-path set, and asserts that
`enforce_allowed_paths()` raises `UnauthorizedPathError` naming the
unauthorized path.

Every selftest scenario — including that negative fixture — is built inside
an isolated temporary git repository created and destroyed by the test
itself (see `_TempGitRepo`). The selftest never creates files in, or
modifies, the real AISET worktree; it also asserts, as its final
post-condition, that running it left no bytecode artifact behind in this
tool's own directory.

## License

Copyright © 2026 Аркадий Лазарев.

The AISET Galley Operator software component is licensed under the
[Apache License 2.0](LICENSE) (`Apache-2.0`). The component includes
`aiset-galley.py`, `config.example.json`, and this README. In particular,
`config.example.json` is distributed under Apache-2.0 as configuration source
covered by this directory-level license.

The separate operational document
[`docs/operations/AISET-GALLEY-OPERATOR.md`](../../docs/operations/AISET-GALLEY-OPERATOR.md)
remains documentation under the repository's `CC-BY-4.0` default; it is not
relicensed by this directory-level software license.
