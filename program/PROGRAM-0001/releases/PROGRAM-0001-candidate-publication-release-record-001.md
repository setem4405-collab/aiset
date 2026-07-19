# PROGRAM-0001 Candidate Publication Release Record 001

**Record Identifier:** PROGRAM-0001-RELEASE-001

**Record Type:** Non-normative Release Documentation Record

**Documentation Status:** Current

**Governance Status:** Non-normative and provisional

**Record Date:** 19 July 2026

**Documented Version:** PROGRAM-0001 v1.0 Candidate Publication

**Documented Lifecycle Tier:** Candidate Publication as recorded by PROGRAM-0001-REGISTRY-007

**Canonical File:** `program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md`

**File Size:** 65839 bytes

**Hash Algorithm:** SHA-256

**Checksum Value:** `426ab2347cd2591313065ac0c05474fd4bc81f71eb4b57ebfd97bb8cb1b49b6a`

**Documented Git Tag:** `PROGRAM-0001-v1.0-candidate-publication`

**Annotated Tag Object:** `0b554792d585965f4f4f8e28dddc32a7b2f3d9d4`

**Tagged Commit:** `fe1e22f8fb10eebce6b158bb048c3244cfc3c5d2`

**Prepared By:** Arkadiy Lazarev

**AI Assistance:** Claude Code (Anthropic)

**Program Originator:** Arkadiy Lazarev

**Responsible Program:** AISET Program

**Classification:** Public

**License:** Creative Commons Attribution 4.0 International

---

## 1. Purpose

This record provides a single, non-normative reference consolidating:

- the canonical Candidate Publication artifact;
- the pre-existing Git tag and tagged commit that mark it;
- a separately recomputed checksum and file size, compared against the authoritative integrity record;
- the review, decision, integrity, registry, and Publisher records that already govern this artifact.

It creates, authorizes, and supersedes nothing.

---

## 2. Non-Final-Status Disclaimer

This is Candidate Publication documentation. Candidate Publication is not Approved Publication and not Reference Publication.

Per `program/PROGRAM-0001/publisher/README.md` §5, Candidate Publication is not final approval. This record does not represent, and is not to be read as representing: Approved Publication; final governing Charter status; AISET Reference Publication; independent external validation; accredited standards approval; legal, security, or privacy certification.

---

## 3. Scope and Limitations

This record:

- was created after the tagged release, documents the existing Git tag, and is not part of the tagged commit;
- creates no integrity, registry, Publisher, decision, operational specification, or Git tag record;
- does not create, modify, or supersede `PROGRAM-0001-INTEGRITY-003`, `PROGRAM-0001-REGISTRY-007`, or `PROGRAM-0001-PUBLISHER-ACK-007`;
- does not create, modify, or supersede any decision record;
- does not create, modify, or delete any Git tag;
- is not defined by any current AISET specification, including `PROGRAM-0001-OPSPEC-001`;
- does not alter the lifecycle status of `PROGRAM-0001 v1.0 Candidate Publication`.

---

## 4. Documented Git Tag

**Tag Type:** Annotated

**Tagger:** Arkadiy Lazarev

**Tag Message:** `PROGRAM-0001 v1.0 Candidate Publication`

**Commit Subject:** `Update PROGRAM-0001 operations index`

This record was written after the tag and its tagged commit already existed. It documents that pre-existing tag rather than creating one; it is not part of the tagged commit and did not exist at the time the tag was created.

**Verification commands used:**

```bash
git rev-parse PROGRAM-0001-v1.0-candidate-publication
git rev-parse PROGRAM-0001-v1.0-candidate-publication^{}
```

The first command resolves the annotated tag object; the second resolves the tagged commit.

---

## 5. Checksum Cross-check

This record's checksum and file size were separately recomputed and compared against `PROGRAM-0001-INTEGRITY-003`.

**Verification commands used:**

```bash
sha256sum program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md
wc -c < program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md
```

| Field | Separately Recomputed | PROGRAM-0001-INTEGRITY-003 |
|---|---|---|
| SHA-256 | `426ab2347cd2591313065ac0c05474fd4bc81f71eb4b57ebfd97bb8cb1b49b6a` | `426ab2347cd2591313065ac0c05474fd4bc81f71eb4b57ebfd97bb8cb1b49b6a` |
| File Size | 65839 bytes | 65839 bytes |

**Comparison Result:** Match. No mismatch detected.

`PROGRAM-0001-INTEGRITY-003` remains authoritative for this artifact's integrity evidence. This cross-check does not supersede, replace, or create integrity evidence.

---

## 6. Related Lifecycle Records

- **Readiness Review** — `PROGRAM-0001-REVIEW-011`: `program/PROGRAM-0001/reviews/PROGRAM-0001-candidate-publication-readiness-review-011.md`
- **Second-party Review** — `PROGRAM-0001-REVIEW-012`: `program/PROGRAM-0001/reviews/PROGRAM-0001-independent-second-party-review-012.md` (not to be read as independent external review)
- **Transition Decision** — `PROGRAM-0001-DECISION-001`: `program/PROGRAM-0001/decisions/PROGRAM-0001-candidate-publication-transition-decision-001.md`
- **Package Reconciliation Decision** — `PROGRAM-0001-DECISION-002`: `program/PROGRAM-0001/decisions/PROGRAM-0001-candidate-package-reconciliation-decision-002.md`
- **Identifier Correction Decision** — `PROGRAM-0001-DECISION-003`: `program/PROGRAM-0001/decisions/PROGRAM-0001-review-identifier-reconciliation-decision-003.md`
- **Integrity Record** — `PROGRAM-0001-INTEGRITY-003`: `program/PROGRAM-0001/integrity/PROGRAM-0001-candidate-publication-integrity-record-003.md` (authoritative)
- **Registry Record** — `PROGRAM-0001-REGISTRY-007`: `program/PROGRAM-0001/registry/PROGRAM-0001-candidate-publication-registry-record-007.md`
- **Publisher Acknowledgment** — `PROGRAM-0001-PUBLISHER-ACK-007`: `program/PROGRAM-0001/publisher/PROGRAM-0001-candidate-publication-publisher-acknowledgment-007.md`

---

## 7. Governance Status of This Record

This document type is not defined by any current AISET specification, including `PROGRAM-0001-OPSPEC-001`. Whether to formally define it in a future subordinate specification remains open for review.

---

## 8. Retention

As a non-normative administrative expectation, this record is expected to be preserved permanently and not silently rewritten. A correction, if needed, would use a superseding documentation file rather than an in-place edit.

---

## 9. Attribution

Attribution for this record is recorded in the header fields above.

---

## 10. License

Copyright © 2026 AISET Program.

This record is licensed under the Creative Commons Attribution 4.0 International License.

See:

- `LICENSE`
- `LICENSES/CC-BY-4.0.txt`
