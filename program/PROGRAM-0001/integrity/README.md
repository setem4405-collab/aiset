# PROGRAM-0001 Integrity Records

This directory contains artifact integrity records associated with:

`PROGRAM-0001 — AISET Program Charter`

---

## 1. Directory Purpose

Integrity records bind lifecycle artifacts to:

- document identifier;
- version;
- lifecycle status;
- canonical filename and repository path;
- file size;
- canonical byte conditions;
- hash algorithm;
- checksum value;
- calculation and verification method;
- registry and Publisher relationships;
- mismatch handling.

An integrity record verifies artifact bytes. It does not independently grant lifecycle approval.

---

## 2. Integrity Record Sequence

The integrity record sequence is:

1. `PROGRAM-0001-INTEGRITY-001`
2. `PROGRAM-0001-INTEGRITY-002`
3. `PROGRAM-0001-INTEGRITY-003`

`PROGRAM-0001-INTEGRITY-003` is the current canonical integrity record.

Earlier records remain discoverable as historical integrity evidence.

---

## 3. Integrity Records

### 3.1 PROGRAM-0001-INTEGRITY-001

**Related Version:** PROGRAM-0001 v1.0 Candidate

**Record Status:** Historical

**Artifact:**

`program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate.md`

**SHA-256:** `a17f8b099d215db99ef3baebdd6e8838bf7cdeea434e888e26789b477e05ba1c`

**File Size:** 64381 bytes

**File:** `PROGRAM-0001-candidate-integrity-record-001.md`

---

### 3.2 PROGRAM-0001-INTEGRITY-002

**Related Version:** PROGRAM-0001 v1.0 Candidate Publication

**Record Status:** Superseded

**SHA-256:** `4f100b3e9d37ba549792ea33e57d9b4da9d5d30f3be946f00e9bb723ca2d82d5`

**File Size:** 65638 bytes

**File:** `PROGRAM-0001-candidate-publication-integrity-record-002.md`

This was the previous canonical integrity record.

---

### 3.3 PROGRAM-0001-INTEGRITY-003

**Related Version:** PROGRAM-0001 v1.0 Candidate Publication

**Record Status:** Active

**Disposition:** Verified

**Canonical Artifact:**

`program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md`

**SHA-256:** `426ab2347cd2591313065ac0c05474fd4bc81f71eb4b57ebfd97bb8cb1b49b6a`

**File Size:** 65839 bytes

**Second-party Review:** PROGRAM-0001-REVIEW-012

**Package Reconciliation Decision:** PROGRAM-0001-DECISION-002

**Identifier Correction Decision:** PROGRAM-0001-DECISION-003

**File:** `PROGRAM-0001-candidate-publication-integrity-record-003.md`

---

## 4. Current Integrity State

The current canonical integrity record is:

`PROGRAM-0001-INTEGRITY-003`

It is linked to:

- `PROGRAM-0001-REVIEW-012`;
- `PROGRAM-0001-REVIEW-011`;
- `PROGRAM-0001-DECISION-001`;
- `PROGRAM-0001-DECISION-002`;
- `PROGRAM-0001-DECISION-003`;
- `PROGRAM-0001-REGISTRY-007`;
- `PROGRAM-0001-PUBLISHER-ACK-007`.

`PROGRAM-0001-INTEGRITY-002` remains preserved as the previous canonical record.

`PROGRAM-0001-INTEGRITY-001` remains valid for the historical Candidate artifact.

Any later byte-level change requires a new integrity record and updated dependent lifecycle records.

---

## 5. Verification

From the repository root:

```bash
printf '%s  %s\n' \
'426ab2347cd2591313065ac0c05474fd4bc81f71eb4b57ebfd97bb8cb1b49b6a' \
'program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md' \
| sha256sum --check
```

Expected result:

```text
program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md: OK
```

---

## 6. Related Directories

**Program documents:**

`program/PROGRAM-0001/`

**Reviews and lifecycle decisions:**

`program/PROGRAM-0001/reviews/`

**Registry records:**

`program/PROGRAM-0001/registry/`

**Publisher acknowledgments:**

`program/PROGRAM-0001/publisher/`

**Operational integrity policy:**

`program/PROGRAM-0001/operations/`

---

## 7. License

Unless otherwise stated in an individual record, documents in this directory are licensed under the Creative Commons Attribution 4.0 International License.

See:

- `LICENSE`
- `LICENSES/CC-BY-4.0.txt`
