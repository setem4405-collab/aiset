# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

AISET is a documentation and governance repository — not a software project. It publishes an open,
technology-independent engineering program ("AISET": standardizing the architecture of cognitive
context transformations) as Markdown, YAML, and checksum artifacts. There is currently no source
code, no package manager, no build system, no linter, and no test suite anywhere in the repository.
Do not add one unless explicitly asked — do not assume a JS/Python/etc. toolchain exists.

## Commands

There is no build, lint, or test command. The only validation commands used in this repository are:

```bash
# Markdown sanity check before committing (should produce no output)
git diff --check
git diff --cached --check

# Checksum verification (see checksum policy below)
sha256sum <file>                       # Git Bash / Linux / macOS
sha256sum --check <checksum-file>      # verify against a SHA256SUMS-style file
shasum -a 256 <file>                   # macOS alternative
Get-FileHash -Algorithm SHA256 <file>  # Windows PowerShell
openssl dgst -sha256 <file>            # OpenSSL alternative
```

## Repository structure

```text
aiset/
├── program/          program-level charters (PROGRAM-0001, etc.)
├── publications/      approved, released publications (DISCOVERY-0001, etc.)
├── governance/         governance principles, lifecycle rules, publication procedures
├── specifications/     normative and supporting specifications
├── registry/           stable identifiers and machine-readable registry records
├── schemas/            validation schemas for structured artifacts
├── implementations/    reference implementations, adapters, test artifacts (none released yet)
├── architecture/       architecture concept documents
└── LICENSES/           full license texts
```

Each top-level directory has its own `README.md` describing its purpose and current status — read the
relevant one before working in that area.

### Per-publication/charter layout

A document identifier (e.g. `PROGRAM-0001`, `DISCOVERY-0001`) gets its own directory containing
versioned drafts and, once mature, a consistent set of subfolders. `program/PROGRAM-0001/` is the
fullest example:

- versioned documents at the top level, named `<ID>-v<major>.<minor>-<status>.md`
  (e.g. `PROGRAM-0001-v0.9-draft.md`, `PROGRAM-0001-v1.0-candidate-publication.md`)
- `decisions/` — recorded lifecycle/governance decisions
- `governance/` — approval/appeal authority records
- `integrity/` — checksum/integrity records for candidate and approved artifacts
- `operations/` — operational specifications and policies (e.g. checksum algorithm policy)
- `publisher/` — Publisher acknowledgment records
- `registry/` — registry records for each version/status transition
- `reviews/` — review records (architectural, editorial, security/privacy, second-party, etc.)

A released publication (`publications/DISCOVERY-0001/`) instead ships a final set of artifacts:
the reference document, `AUTHORSHIP.md`, `CITATION.md`/`CITATION.bib`, `RELEASE-MANIFEST.md`,
`CHANGELOG.md`, a `.sha256` file and `SHA256SUMS` manifest, plus `registry/` and `reviews/` subfolders.
New publications should follow this same pattern.

## Document identifiers and lifecycle

Identifiers (`DISCOVERY-0001`, `PROGRAM-0001`, planned `AAR-0001`, `ARI-0001`, ...) are unique, stable,
and used as directory/file prefixes. Documents move through statuses: Draft → Review → Candidate
Publication → Approved Publication → Reference Publication → (Superseded | Withdrawn). A released
version is immutable — corrections require a new version, amendment, or superseding publication, never
a silent edit. Registry records mirror this lifecycle in `registry/` (see `registry/README.md`).

Normative documents use RFC-style keywords deliberately: **MUST / MUST NOT / SHOULD / SHOULD NOT /
MAY**. Only use these words when a statement is meant to affect implementation, validation,
compatibility, interoperability, or conformance — not as generic emphasis.

## Checksums

SHA-256 is the only approved checksum algorithm (see the current canonical Review-status policy,
`program/PROGRAM-0001/operations/PROGRAM-0001-checksum-algorithm-policy-001-v1.0-review.md`;
the sibling `PROGRAM-0001-checksum-algorithm-policy-001.md` is the superseded Draft). Canonical text
artifacts use UTF-8, no BOM, LF line endings, and a final newline. Checksums are calculated over exact
artifact bytes, recorded as full lowercase 64-character hex digests (never truncated), and a mismatch
must never be silently ignored or overwritten — it is investigated and dispositioned per that policy.

## Licensing split

Non-software materials (publications, specifications, governance docs, schemas, registry records) are
CC-BY-4.0 by default. Software/code components require a separately and explicitly identified license
before they can be treated as open source (`implementations/README.md`); none has been assigned yet
because no reference implementation has been released.

## How Claude Code should operate here

This repository has a formal AI-assisted development model:
`governance/development/AISET-AI-ASSISTED-DEVELOPMENT-MODEL-001.md`. Key points:

- **Roles**: Claude Code is the primary repository-aware implementation tool. OpenAI Codex is the
  independent architecture challenger/reviewer. Arkadiy Lazarev is the human decision authority.
- **Claude Code must not**, on its own authority: approve architecture, authorize or create a commit,
  push or force-push to any branch, merge protected changes, alter normative governance, approve a
  publication, expand its own permissions, redefine task classification, suppress material findings,
  or represent an AI-generated decision as a human decision. Each of the following requires a separate,
  explicit human instruction naming that exact action before it may be performed: `git add`,
  `git commit`, `git push`, `git push --force`, creating or deleting a tag, `git reset`, `git rebase`,
  amending a commit, any other history-rewriting operation, and deletion of a published lifecycle
  record. Prior review of a diff is necessary but not sufficient authorization for any of these.
- **Task classes** — classify every task by its highest material risk, not by how many files it touches:
  - **L1 (Routine)**: spelling/formatting fixes, isolated clarifications, non-semantic metadata
    corrections — lightweight, human-reviewed.
  - **L2 (Engineering, default)**: substantive changes with no architectural/governance effect —
    implement, then expect independent review before commit.
  - **L3 (Architectural/Critical)**: anything touching core normative concepts (Cognitive Context
    Object, Cognitive Transformation Specification, invariants/contracts), governance architecture,
    trust/provenance, security, or lifecycle/approval logic — requires architecture proposal and
    conformance review *before* implementation. When unsure, use the higher class.
- Treat published/Reference and Approved artifacts as immutable; propose new versions or correction
  records instead of editing them in place.
- Never commit secrets, raw private conversations, or unnecessary personal data.
