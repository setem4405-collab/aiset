# PROGRAM-0001 Operations

This directory contains subordinate operational specifications, policies, templates, and operational records associated with:

`PROGRAM-0001 — AISET Program Charter`

The current Charter reference version is:

`PROGRAM-0001 v1.0 Candidate`

---

## 1. Directory Purpose

This directory supports the implementation of PROGRAM-0001 requirements through subordinate operational documents.

It may contain:

- operational record specifications;
- checksum and integrity policies;
- record templates;
- classification records;
- access-control records;
- incident records;
- notification decisions;
- continuity and recovery records;
- dependency records;
- integrity records;
- correction and redaction records;
- governance-capture assessments;
- security-sensitive change records;
- participation-restriction records;
- foundation-stage exception records.

Subordinate operational documents do not amend or override the Charter.

Where a subordinate document conflicts with PROGRAM-0001, the Charter prevails.

---

## 2. Current Subordinate Review Documents

### 2.1 PROGRAM-0001-OPSPEC-001

**Title:** PROGRAM-0001 Operational Record Specification

**Current Version:** 1.0 Review

**Status:** Review

**Review Basis:** PROGRAM-0001-REVIEW-009

**Finding Disposition:** NEW-003 — Resolved

**Current File:**

`PROGRAM-0001-operational-record-specification-001-v1.0-review.md`

**Previous Draft File:**

`PROGRAM-0001-operational-record-specification-001.md`

The Review version defines:

- common operational record fields;
- record identifiers;
- statuses and classifications;
- record-specific mandatory fields;
- integrity and correction requirements;
- privacy and security handling;
- retention and supersession rules;
- repository organization.

---

### 2.2 PROGRAM-0001-CHECKSUM-POLICY-001

**Title:** PROGRAM-0001 Checksum Algorithm Policy

**Current Version:** 1.0 Review

**Status:** Review

**Review Basis:** PROGRAM-0001-REVIEW-009

**Finding Disposition:** NEW-004 — Resolved

**Current File:**

`PROGRAM-0001-checksum-algorithm-policy-001-v1.0-review.md`

**Previous Draft File:**

`PROGRAM-0001-checksum-algorithm-policy-001.md`

The Review version defines:

- SHA-256 as the default checksum algorithm;
- full 64-character lowercase hexadecimal representation;
- canonical byte requirements;
- UTF-8 and LF recommendations;
- calculation and verification requirements;
- mismatch handling;
- prohibited algorithms;
- correction, migration, and deprecation procedures.

---

## 3. Review Basis

Both current subordinate Review documents were evaluated in:

`PROGRAM-0001-REVIEW-009 — Operational Records and Checksum Policy Review`

Canonical review record:

`../reviews/PROGRAM-0001-operational-records-checksum-policy-review-009.md`

The review determined:

- no blocking findings;
- no major findings;
- NEW-003 resolved;
- NEW-004 resolved;
- progression to subordinate Review status permitted;
- Candidate Publication not authorized.

---

## 4. Current Registration State

The subordinate Review documents completed their registration and Publisher acknowledgment sequence through:

- `PROGRAM-0001-OPERATIONS-REGISTRY-001`;
- `PROGRAM-0001-OPERATIONS-PUBLISHER-ACK-001`.

They remain subordinate Review documents.

They must not be described as:

- Approved Publications;
- Candidate Publications;
- independently validated documents;
- externally certified standards.

Their requirements support the current Charter Candidate Publication but do not independently change their own lifecycle status.

---

## 5. Lifecycle Relationships

The current sequence is:

1. `PROGRAM-0001-OPSPEC-001 v1.0 Draft`
2. `PROGRAM-0001-CHECKSUM-POLICY-001 v1.0 Draft`
3. `PROGRAM-0001-REVIEW-009`
4. `PROGRAM-0001-OPSPEC-001 v1.0 Review`
5. `PROGRAM-0001-CHECKSUM-POLICY-001 v1.0 Review`
6. `PROGRAM-0001-OPERATIONS-REGISTRY-001`
7. `PROGRAM-0001-OPERATIONS-PUBLISHER-ACK-001`
8. application of the integrity requirements to `PROGRAM-0001 v1.0 Candidate`
9. creation of `PROGRAM-0001-INTEGRITY-001`

The Draft artifacts remain historical predecessor versions.

They must not be silently deleted or replaced.

---

## 6. Operational Record Types

The recommended future directory structure is:

```text
operations/
├── README.md
├── classification/
├── access/
├── incidents/
├── notifications/
├── recovery/
├── dependencies/
├── integrity/
├── corrections/
├── capture/
├── security-changes/
├── restrictions/
└── exceptions/
```

Subdirectories may remain uncreated until the first record of the corresponding type exists.

---

## 7. Integrity Policy Summary

The current Review checksum policy establishes:

**Default Algorithm:** SHA-256

**Digest Length:** 256 bits

**Representation:** 64 lowercase hexadecimal characters

**Truncation:** Prohibited

**Canonical Text Recommendation:**

- UTF-8;
- no byte order mark;
- LF line endings;
- final newline;
- no trailing whitespace unless required.

Candidate Publication artifacts require formal integrity records and reproducible verification.

---

## 8. Independent Review Status

The Charter-level independent review requirement was satisfied through:

`PROGRAM-0001-INDEPENDENT-REVIEW-001`

The resulting findings were resolved through:

`PROGRAM-0001-INDEPENDENT-DISPOSITION-001`

`NEW-005 — Independent Review Availability` is resolved.

The subordinate operational documents remain internal Review documents and must not be represented as independently certified.

---

## 9. Candidate Publication Application

The checksum policy and operational record specification were applied to the Charter Candidate Publication.

The resulting record set includes:

- `PROGRAM-0001 v1.0 Candidate`;
- `PROGRAM-0001-INTEGRITY-001`;
- `PROGRAM-0001-CANDIDATE-DECISION-001`;
- `PROGRAM-0001-REGISTRY-005`;
- `PROGRAM-0001-PUBLISHER-ACK-005`.

The Candidate artifact uses:

- SHA-256;
- a full 64-character lowercase hexadecimal digest;
- a recorded file size;
- a canonical path;
- reproducible verification instructions.

Candidate Publication remains distinct from Approved Publication.

---

## 10. Record Integrity

Published operational documents must not be silently modified or replaced.

Material changes require, as applicable:

- a new version;
- a correction record;
- a superseding document;
- updated integrity evidence;
- a new review;
- an updated registry record;
- a new Publisher acknowledgment.

Historical versions must remain discoverable unless restriction is justified by security, privacy, legal, or safety requirements.

---

## 11. Related Directories

**PROGRAM-0001 documents:**

`program/PROGRAM-0001/`

**Reviews:**

`program/PROGRAM-0001/reviews/`

**Registry records:**

`program/PROGRAM-0001/registry/`

**Publisher acknowledgments:**

`program/PROGRAM-0001/publisher/`

---

## 12. Authority and Role Disclosure

During the foundation stage, Arkadiy Lazarev may perform multiple roles, including:

- Program Originator;
- Author;
- Lead Editor;
- Internal Reviewer;
- Repository Maintainer;
- Registry Administrator;
- Publisher Representative.

This overlap must be disclosed in applicable operational, registry, and Publisher records.

Internal work must not be represented as independent external validation.

---

## 13. License

Unless otherwise stated in an individual document, files in this directory are licensed under the Creative Commons Attribution 4.0 International License.

See:

- `LICENSE`
- `LICENSES/CC-BY-4.0.txt`
