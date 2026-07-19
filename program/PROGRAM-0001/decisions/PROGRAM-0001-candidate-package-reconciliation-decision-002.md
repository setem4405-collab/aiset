# PROGRAM-0001 Candidate Package Reconciliation Decision 002

**Decision Identifier:** PROGRAM-0001-DECISION-002

**Title:** Reconciliation of Parallel PROGRAM-0001 Candidate Publication Packages

**Status:** Approved

**Decision Date:** 19 July 2026

**Document Identifier:** PROGRAM-0001

**Decision Authority:** Arkadiy Lazarev

**Authority Role:** Program Originator and Foundation-stage Transition Authority

**Responsible Program:** AISET Program

**Classification:** Public

**License:** Creative Commons Attribution 4.0 International

---

## Decision Status

This record resolves the existence of two parallel Candidate Publication artifact and record lines for PROGRAM-0001.

It preserves all historical files, identifies the current canonical Candidate artifact, records identifier collisions, and authorizes corrected lifecycle records.

No file is deleted or silently rewritten by this decision.

---

## 1. Purpose

The purpose of this decision is to reconcile the 18 July 2026 and 19 July 2026 Candidate Publication packages, preserve lifecycle history, determine the current canonical Candidate artifact, resolve duplicate persistent identifiers, and authorize corrected records and index updates.

---

## 2. Earlier Candidate Package

The earlier package is dated 18 July 2026 and includes:

- `program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate.md`;
- `PROGRAM-0001-INTEGRITY-001`;
- `PROGRAM-0001-CANDIDATE-DECISION-001`;
- `PROGRAM-0001-REGISTRY-005`;
- `PROGRAM-0001-PUBLISHER-ACK-005`.

**SHA-256:** `a17f8b099d215db99ef3baebdd6e8838bf7cdeea434e888e26789b477e05ba1c`

**File Size:** 64381 bytes

This was the first completed Candidate Publication lifecycle package.

---

## 3. Later Candidate Package

The later package is dated 19 July 2026 and includes:

- `program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md`;
- a second record using `PROGRAM-0001-INTEGRITY-001`;
- `PROGRAM-0001-DECISION-001`;
- a second record using `PROGRAM-0001-REGISTRY-005`;
- a second record using `PROGRAM-0001-PUBLISHER-ACK-005`.

**SHA-256:** `4f100b3e9d37ba549792ea33e57d9b4da9d5d30f3be946f00e9bb723ca2d82d5`

**File Size:** 65638 bytes

The later artifact incorporates `PROGRAM-0001-REVIEW-010` and `PROGRAM-0001-REVIEW-011`.

---

## 4. Comparison Finding

The two Candidate artifacts are not byte-identical and differ in filename, version label, date, length, checksum, review basis, and lifecycle narrative.

They must not be treated as interchangeable representations of one exact artifact.

---

## 5. Historical Validity Finding

The earlier package was created and published before the later package.

It must remain preserved as historical lifecycle evidence and must not be deleted, overwritten, or represented as never having existed.

---

## 6. Current Canonical Artifact Decision

The current canonical Candidate Publication artifact is:

`program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md`

This designation is based on its later date, incorporation of REVIEW-010 and REVIEW-011, explicit second-party review classification, final disposition of ED-002, ED-003, and NEW-005, and stronger readiness traceability.

---

## 7. Earlier Artifact Status

`program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate.md`

is classified as:

`Superseded Historical Candidate Publication Artifact`

It remains available for provenance and audit purposes.

---

## 8. Identifier Collision Finding

The later package reused identifiers already assigned in the earlier package:

- `PROGRAM-0001-INTEGRITY-001`;
- `PROGRAM-0001-REGISTRY-005`;
- `PROGRAM-0001-PUBLISHER-ACK-005`.

This is an administrative persistent-identifier collision.

---

## 9. Decision Identifier Finding

The decision identifiers do not collide:

- earlier: `PROGRAM-0001-CANDIDATE-DECISION-001`;
- later: `PROGRAM-0001-DECISION-001`.

Both remain preserved.

---

## 10. Corrected Integrity Identifier

The integrity record for the later artifact must be reissued as:

`PROGRAM-0001-INTEGRITY-002`

The later file carrying duplicated identifier `PROGRAM-0001-INTEGRITY-001` must be marked superseded after the corrected record is published.

---

## 11. Corrected Registry Identifier

The registry record for the later artifact must be reissued as:

`PROGRAM-0001-REGISTRY-006`

The later file carrying duplicated identifier `PROGRAM-0001-REGISTRY-005` must be marked superseded after the corrected record is published.

---

## 12. Corrected Publisher Identifier

The Publisher acknowledgment for the later artifact must be reissued as:

`PROGRAM-0001-PUBLISHER-ACK-006`

The later file carrying duplicated identifier `PROGRAM-0001-PUBLISHER-ACK-005` must be marked superseded after the corrected acknowledgment is published.

---

## 13. Duplicate Record Treatment

The three later records with duplicated identifiers are not deleted.

They must be treated as:

`Superseded due to Administrative Identifier Collision`

Any amendment must cite this decision.

---

## 14. Canonical Lifecycle Package

After correction, the current Candidate Publication lifecycle package will consist of:

1. `PROGRAM-0001 v1.0 Candidate Publication`;
2. `PROGRAM-0001-REVIEW-010`;
3. `PROGRAM-0001-REVIEW-011`;
4. `PROGRAM-0001-DECISION-001`;
5. `PROGRAM-0001-INTEGRITY-002`;
6. `PROGRAM-0001-REGISTRY-006`;
7. `PROGRAM-0001-PUBLISHER-ACK-006`;
8. `PROGRAM-0001-DECISION-002`.

---

## 15. Earlier Package Preservation

The earlier package remains a historical package consisting of:

1. `PROGRAM-0001 v1.0 Candidate`;
2. `PROGRAM-0001-INTEGRITY-001`;
3. `PROGRAM-0001-CANDIDATE-DECISION-001`;
4. `PROGRAM-0001-REGISTRY-005`;
5. `PROGRAM-0001-PUBLISHER-ACK-005`.

Its current operational effect is superseded, not erased.

---

## 16. Index Update Rule

README and lifecycle indexes must not be updated to the later package until corrected records 002, 006, and 006 are published and duplicate later records are marked superseded.

---

## 17. Approved Publication Limitation

Neither Candidate package grants Approved Publication, final governing Charter status, Reference Publication, or independent external certification.

---

## 18. Public Representation Rule

> PROGRAM-0001 has a preserved earlier Candidate Publication package dated 18 July 2026 and a later canonical Candidate Publication artifact dated 19 July 2026. The later package incorporates additional second-party review and readiness disposition. Administrative identifier collisions in three later records are being corrected without deleting lifecycle history.

---

## 19. Required Actions

1. publish this reconciliation decision;
2. issue `PROGRAM-0001-INTEGRITY-002`;
3. issue `PROGRAM-0001-REGISTRY-006`;
4. issue `PROGRAM-0001-PUBLISHER-ACK-006`;
5. mark the three later duplicate-ID records as superseded;
6. update README and lifecycle indexes;
7. verify repository consistency.

---

## 20. Decision Outcome

**Earlier Candidate Package:** Preserved as historical and superseded

**Current Canonical Candidate Artifact:** PROGRAM-0001 v1.0 Candidate Publication

**Current Canonical Artifact Path:** program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md

**Current Canonical SHA-256:** 4f100b3e9d37ba549792ea33e57d9b4da9d5d30f3be946f00e9bb723ca2d82d5

**Administrative Identifier Collision:** Confirmed

**Corrected Integrity Identifier:** PROGRAM-0001-INTEGRITY-002

**Corrected Registry Identifier:** PROGRAM-0001-REGISTRY-006

**Corrected Publisher Identifier:** PROGRAM-0001-PUBLISHER-ACK-006

**Deletion Authorized:** No

**Index Update Authorized Now:** No

---

## 21. Effective Date

This decision is effective on `19 July 2026`.

---

## 22. Attribution

**Decision Authority:** Arkadiy Lazarev

**Program Originator:** Arkadiy Lazarev

**Registry Administrator:** Arkadiy Lazarev

**Publisher Representative:** Arkadiy Lazarev

Role overlap is disclosed.

---

## 23. License

Copyright © 2026 AISET Program.

This decision record is licensed under the Creative Commons Attribution 4.0 International License.

See:

- `LICENSE`
- `LICENSES/CC-BY-4.0.txt`
