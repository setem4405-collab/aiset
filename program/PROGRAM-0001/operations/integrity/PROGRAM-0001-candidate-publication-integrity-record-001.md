# PROGRAM-0001 Candidate Publication Integrity Record 001

**Record Identifier:** PROGRAM-0001-INTEGRITY-001

**Title:** Integrity Record for PROGRAM-0001 v1.0 Candidate Publication

**Status:** Active

**Record Date:** 19 July 2026

**Document Identifier:** PROGRAM-0001

**Document Version:** 1.0 Candidate Publication

**Lifecycle Status:** Candidate Publication

**Canonical File:** program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md

**File Size:** 65638 bytes

**Hash Algorithm:** SHA-256

**Checksum Value:** 4f100b3e9d37ba549792ea33e57d9b4da9d5d30f3be946f00e9bb723ca2d82d5

**Readiness Basis:** PROGRAM-0001-REVIEW-011

**Second-party Review Basis:** PROGRAM-0001-REVIEW-010

**Operational Specification:** PROGRAM-0001-OPSPEC-001 v1.0 Review

**Checksum Policy:** PROGRAM-0001-CHECKSUM-POLICY-001 v1.0 Review

**Calculating Authority:** Arkadiy Lazarev

**Responsible Program:** AISET Program

**Publisher:** AISET Program

**License:** Creative Commons Attribution 4.0 International

---

## Record Status

This record binds the exact staged bytes of:

`PROGRAM-0001 v1.0 Candidate Publication`

to the SHA-256 checksum recorded below.

The checksum was calculated from the Git index representation of the Candidate artifact before commit.

This record is intended to support:

- Candidate Publication transition decision;
- Candidate registry binding;
- Publisher acknowledgment;
- later verification;
- recovery and correction procedures.

This record does not itself authorize Candidate Publication.

---

## 1. Purpose

The purpose of this record is to provide reproducible integrity evidence for the exact Candidate Publication artifact.

---

## 2. Artifact Identity

**Document Identifier:** PROGRAM-0001

**Version:** 1.0 Candidate Publication

**Lifecycle Status:** Candidate Publication

**Canonical Path:**

`program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md`

---

## 3. Integrity Value

**Algorithm:** SHA-256

**Digest:**

`4f100b3e9d37ba549792ea33e57d9b4da9d5d30f3be946f00e9bb723ca2d82d5`

**Digest Length:** 64 lowercase hexadecimal characters

**File Size:** 65638 bytes

---

## 4. Calculation Source

The checksum was calculated from the Git index representation using:

```bash
git show :program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md | sha256sum
```

The file size was calculated using:

```bash
git show :program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md | wc -c
```

---

## 5. Canonical Byte Conditions

The staged Candidate artifact was verified as:

- UTF-8 compatible text;
- no UTF-8 byte order mark;
- LF line endings in the staged representation;
- final newline present;
- no trailing whitespace detected;
- exact staged size: 65638 bytes.

The first three staged bytes were:

```text
23 20 50
```

These are not the UTF-8 BOM sequence:

```text
ef bb bf
```

The final staged byte was:

```text
10
```

which represents LF.

---

## 6. Policy Conformance

This integrity action conforms to:

`PROGRAM-0001-CHECKSUM-POLICY-001 v1.0 Review`

The following policy requirements are satisfied:

- approved default algorithm used;
- algorithm explicitly identified;
- full digest recorded;
- lowercase hexadecimal representation used;
- canonical path recorded;
- file size recorded;
- calculation method recorded;
- final LF verified;
- BOM absence verified;
- mismatch procedure defined.

---

## 7. Operational Record Conformance

This record conforms to:

`PROGRAM-0001-OPSPEC-001 v1.0 Review`

It includes:

- persistent identifier;
- record type;
- title;
- status;
- classification;
- creation date;
- responsible authority;
- related document;
- related version;
- canonical file;
- summary;
- disposition;
- integrity information;
- retention condition;
- license terms.

---

## 8. Classification

**Classification:** Public

No personal contact details, credentials, secrets, or restricted evidence are included.

---

## 9. Verification Method

A verifier may reproduce the checksum from the canonical staged or committed artifact using:

```bash
sha256sum program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md
```

For verification against the Git index before commit:

```bash
git show :program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md | sha256sum
```

The expected result is:

```text
4f100b3e9d37ba549792ea33e57d9b4da9d5d30f3be946f00e9bb723ca2d82d5
```

---

## 10. Verification Status

**Initial Calculation:** Completed

**Initial Verification:** Completed

**Expected Digest Match:** Yes

**Mismatch Detected:** No

---

## 11. Mismatch Procedure

If a future verification result differs, the responsible authority must:

1. stop relying on the affected artifact;
2. preserve the mismatching artifact;
3. verify canonical path and version;
4. recalculate SHA-256;
5. inspect encoding, line endings, truncation, corruption, and unauthorized modification;
6. create or update an integrity or incident record;
7. suspend Candidate Publication reliance where appropriate;
8. create correction, recovery, or supersession records as needed.

---

## 12. Lifecycle Relationships

**Previous Version:** PROGRAM-0001 v1.0 Review

**Readiness Review:** PROGRAM-0001-REVIEW-011

**Second-party Review:** PROGRAM-0001-REVIEW-010

**Current Review Registry Record:** PROGRAM-0001-REGISTRY-004

**Current Review Publisher Acknowledgment:** PROGRAM-0001-PUBLISHER-ACK-004

**Candidate Transition Decision:** Pending

**Candidate Registry Record:** Pending

**Candidate Publisher Acknowledgment:** Pending

---

## 13. Repository Relationship

The checksum verifies the exact artifact bytes.

A repository commit identifier may later be added as supporting provenance but does not replace this checksum.

The artifact checksum, commit identifier, registry record, and Publisher acknowledgment serve different functions.

---

## 14. Retention

This integrity record must be retained permanently as part of the Candidate Publication lifecycle history.

It must remain discoverable if superseded or corrected.

---

## 15. Correction and Supersession

This record must not be silently modified after publication.

Any material change to the Candidate artifact requires:

- a new checksum;
- a new or corrected integrity record;
- preserved historical relationship;
- updated registry and Publisher records where applicable.

---

## 16. Integrity Decision

The calculating authority records:

**Artifact:** PROGRAM-0001 v1.0 Candidate Publication

**Canonical File:** program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md

**SHA-256:** 4f100b3e9d37ba549792ea33e57d9b4da9d5d30f3be946f00e9bb723ca2d82d5

**File Size:** 65638 bytes

**Integrity Status:** Verified

**Candidate Transition Decision:** Pending

---

## 17. Attribution

**Calculating Authority:** Arkadiy Lazarev

**Program Originator:** Arkadiy Lazarev

**Registry Administrator:** Arkadiy Lazarev

**Publisher Representative:** Arkadiy Lazarev

Role overlap is disclosed.

---

## 18. License

Copyright © 2026 AISET Program.

This integrity record is licensed under the Creative Commons Attribution 4.0 International License.

See:

- `LICENSE`
- `LICENSES/CC-BY-4.0.txt`
