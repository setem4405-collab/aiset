# PROGRAM-0001 Candidate Publication Integrity Record 002

**Record Identifier:** PROGRAM-0001-INTEGRITY-003

**Title:** Corrected Integrity Record for PROGRAM-0001 v1.0 Candidate Publication

**Status:** Active

**Record Date:** 19 July 2026

**Document Identifier:** PROGRAM-0001

**Document Version:** 1.0 Candidate Publication

**Lifecycle Status:** Candidate Publication

**Canonical File:** program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md

**File Size:** 65839 bytes

**Hash Algorithm:** SHA-256

**Checksum Value:** 426ab2347cd2591313065ac0c05474fd4bc81f71eb4b57ebfd97bb8cb1b49b6a

**Package Reconciliation Decision:** PROGRAM-0001-DECISION-002

**Identifier Correction Decision:** PROGRAM-0001-DECISION-003

**Transition Decision:** PROGRAM-0001-DECISION-001

**Readiness Basis:** PROGRAM-0001-REVIEW-011

**Second-party Review Basis:** PROGRAM-0001-REVIEW-012

**Identifier Correction Basis:** PROGRAM-0001-DECISION-003

**Previous Integrity Record:** PROGRAM-0001-INTEGRITY-002

**Artifact Commit:** 6d6b7df

**Superseded Duplicate Record:** program/PROGRAM-0001/operations/integrity/PROGRAM-0001-candidate-publication-integrity-record-001.md

**Operational Specification:** PROGRAM-0001-OPSPEC-001 v1.0 Review

**Checksum Policy:** PROGRAM-0001-CHECKSUM-POLICY-001 v1.0 Review

**Calculating Authority:** Arkadiy Lazarev

**Responsible Program:** AISET Program

**Classification:** Public

**License:** Creative Commons Attribution 4.0 International

---

## Record Status

This is the corrected canonical integrity record for `PROGRAM-0001 v1.0 Candidate Publication`.

It replaces the operational effect of the later duplicate record that incorrectly reused `PROGRAM-0001-INTEGRITY-001`.

The earlier valid `PROGRAM-0001-INTEGRITY-001`, associated with the 18 July 2026 Candidate artifact, remains preserved as historical evidence.

---

## 1. Purpose

This record verifies the corrected Candidate artifact bytes created after the review identifier correction authorized by `PROGRAM-0001-DECISION-003`. It supersedes `PROGRAM-0001-INTEGRITY-002` as the current canonical integrity evidence and provides the basis for new Registry and Publisher records.

---

## 2. Artifact Identity

**Document Identifier:** PROGRAM-0001

**Version:** 1.0 Candidate Publication

**Lifecycle Status:** Candidate Publication

**Canonical Path:** `program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md`

---

## 3. Integrity Value

**Algorithm:** SHA-256

**Digest:** `426ab2347cd2591313065ac0c05474fd4bc81f71eb4b57ebfd97bb8cb1b49b6a`

**Digest Length:** 64 lowercase hexadecimal characters

**File Size:** 65839 bytes

---

## 4. Calculation Source

```bash
git show :program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md | sha256sum
git show :program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md | wc -c
```

---

## 5. Canonical Byte Conditions

The artifact was verified as UTF-8-compatible text with no BOM, LF line endings in the staged representation, a final LF, no trailing whitespace, and exact size of 65839 bytes.

The first three bytes were `23 20 50`. The final byte was `10`.

---

## 6. Reconciliation Basis

`PROGRAM-0001-DECISION-002` reconciled the parallel Candidate packages and authorized `PROGRAM-0001-INTEGRITY-002` for the then-current artifact bytes.

`PROGRAM-0001-DECISION-003` subsequently corrected the second-party review identifier. Commit `6d6b7df` applied that correction to the Candidate artifact, changed its bytes, and required the new canonical integrity record `PROGRAM-0001-INTEGRITY-003`.

---

## 7. Identifier Collision Resolution

| Identifier | Artifact | Status |
|---|---|---|
| PROGRAM-0001-INTEGRITY-001 | PROGRAM-0001-v1.0-candidate.md | Historical, valid, superseded operational effect |
| PROGRAM-0001-INTEGRITY-002 | PROGRAM-0001-v1.0-candidate-publication.md | Previous canonical record; superseded after artifact byte correction |
| PROGRAM-0001-INTEGRITY-003 | PROGRAM-0001-v1.0-candidate-publication.md | Current canonical integrity record |

---

## 8. Superseded Duplicate Record

The superseded duplicate file is:

`program/PROGRAM-0001/operations/integrity/PROGRAM-0001-candidate-publication-integrity-record-001.md`

Its evidence remains historical, but its duplicated identifier is not canonical.

`PROGRAM-0001-INTEGRITY-003` directly supersedes `PROGRAM-0001-INTEGRITY-002` because the Candidate artifact bytes changed after the review identifier correction.

---

## 9. Policy Conformance

This action conforms to `PROGRAM-0001-CHECKSUM-POLICY-001 v1.0 Review` and records the algorithm, digest, canonical path, file size, calculation method, byte conditions, mismatch procedure, and reconciliation relationship.

---

## 10. Operational Record Conformance

This record conforms to `PROGRAM-0001-OPSPEC-001 v1.0 Review`.

---

## 11. Verification Method

```bash
sha256sum program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md
```

Expected result:

```text
426ab2347cd2591313065ac0c05474fd4bc81f71eb4b57ebfd97bb8cb1b49b6a
```

---

## 12. Verification Status

**Initial Calculation:** Completed

**Initial Verification:** Completed

**Expected Digest Match:** Yes

**Mismatch Detected:** No

**Identifier Collision:** Resolved by this record

---

## 13. Mismatch Procedure

If verification fails, suspend reliance, preserve available copies, verify canonical identity, recalculate SHA-256, investigate corruption or unauthorized modification, create an integrity or incident record, and update dependent lifecycle records.

---

## 14. Lifecycle Relationships

**Earlier Candidate Artifact:** PROGRAM-0001 v1.0 Candidate

**Current Candidate Artifact:** PROGRAM-0001 v1.0 Candidate Publication

**Transition Decision:** PROGRAM-0001-DECISION-001

**Package Reconciliation Decision:** PROGRAM-0001-DECISION-002

**Identifier Correction Decision:** PROGRAM-0001-DECISION-003

**Readiness Review:** PROGRAM-0001-REVIEW-011

**Second-party Review:** PROGRAM-0001-REVIEW-012

**Successor Registry Record:** PROGRAM-0001-REGISTRY-007 pending

**Successor Publisher Acknowledgment:** PROGRAM-0001-PUBLISHER-ACK-007 pending

---

## 15. Repository Relationship

The checksum verifies exact artifact bytes. Commit identifiers provide supporting provenance but do not replace the checksum.

---

## 16. Retention

This record, `PROGRAM-0001-INTEGRITY-002`, the earlier valid `PROGRAM-0001-INTEGRITY-001`, and the superseded duplicate file must remain permanently discoverable.

---

## 17. Correction and Supersession

Any material artifact change requires a new checksum, integrity record, and updated dependent lifecycle records. Silent modification is prohibited.

---

## 18. Integrity Decision

**Artifact:** PROGRAM-0001 v1.0 Candidate Publication

**Canonical File:** program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md

**SHA-256:** 426ab2347cd2591313065ac0c05474fd4bc81f71eb4b57ebfd97bb8cb1b49b6a

**File Size:** 65839 bytes

**Integrity Status:** Verified

**Canonical Integrity Identifier:** PROGRAM-0001-INTEGRITY-003

**Previous Canonical Integrity Record:** PROGRAM-0001-INTEGRITY-002

**Superseded Duplicate Identifier Use:** PROGRAM-0001-INTEGRITY-001

---

## 19. Attribution

**Calculating Authority:** Arkadiy Lazarev

**Decision Authority:** Arkadiy Lazarev

**Program Originator:** Arkadiy Lazarev

**Registry Administrator:** Arkadiy Lazarev

**Publisher Representative:** Arkadiy Lazarev

Role overlap is disclosed.

---

## 20. License

Copyright © 2026 AISET Program.

This integrity record is licensed under the Creative Commons Attribution 4.0 International License.

See:

- `LICENSE`
- `LICENSES/CC-BY-4.0.txt`
