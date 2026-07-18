# PROGRAM-0001 Candidate Publication Integrity Record 001

**Record Identifier:** PROGRAM-0001-INTEGRITY-001

**Record Type:** Artifact Integrity Record

**Title:** PROGRAM-0001 v1.0 Candidate Publication Integrity Record

**Status:** Active

**Classification:** Public

**Creation Date:** 18 July 2026

**Effective Date:** 18 July 2026

**Responsible Authority:** AISET Program

**Author or Recorder:** Arkadiy Lazarev

**Calculating Authority:** Arkadiy Lazarev, Program Originator

**Foundation-Stage Role Overlap:** Disclosed — the Program Originator prepared the Candidate artifact and calculated its checksum during the foundation stage.

**Related Document:** PROGRAM-0001 — AISET Program Charter

**Related Version:** PROGRAM-0001 v1.0 Candidate

**Lifecycle Status:** Candidate Publication

**Related Readiness Decision:** PROGRAM-0001-CANDIDATE-READINESS-REVIEW-001

**Related Independent Review:** PROGRAM-0001-INDEPENDENT-REVIEW-001

**Related Findings Disposition:** PROGRAM-0001-INDEPENDENT-DISPOSITION-001

**Related Registry Record:** Pending

**Related Publisher Acknowledgment:** Pending

**Canonical File:** PROGRAM-0001-v1.0-candidate.md

**Canonical Path:** program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate.md

**File Size:** 64381 bytes

**Encoding:** UTF-8 without byte order mark

**Line Endings:** LF

**Final Newline:** Present

**Trailing Whitespace:** None detected

**Hash Algorithm:** SHA-256

**Checksum Value:** a17f8b099d215db99ef3baebdd6e8838bf7cdeea434e888e26789b477e05ba1c

**Calculation Date:** 18 July 2026

**Calculation Environment:** Windows Git Bash

**Calculation Tool:** GNU-compatible `sha256sum`

**Verification Method:** Repeated local calculation using `sha256sum`, with digest-length validation using `awk`

**Verification Result:** Verified — repeated calculation produced the recorded 64-character lowercase hexadecimal digest

**Second-Party Confirmation:** Not obtained at record creation; not identified as a mandatory precondition by the applicable Charter or readiness decision

**Disposition:** Verified

**Integrity Information:** This record binds the Candidate artifact identifier, lifecycle status, canonical filename, canonical repository path, exact file size, canonical byte conditions, hash algorithm, and checksum value.

**Retention or Review Condition:** Retain permanently with the Candidate Publication lifecycle record set. Review upon any artifact modification, path change, checksum mismatch, correction, supersession, or lifecycle transition.

**License or Access Terms:** Creative Commons Attribution 4.0 International

---

## 1. Purpose

This record provides public, reproducible integrity evidence for:

`PROGRAM-0001 v1.0 Candidate`

It binds the Candidate Publication artifact to its canonical path and exact SHA-256 digest.

---

## 2. Canonical Artifact

**Document Identifier:** PROGRAM-0001

**Version:** 1.0 Candidate

**Lifecycle Status:** Candidate Publication

**Canonical Filename:** `PROGRAM-0001-v1.0-candidate.md`

**Canonical Repository Path:** `program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate.md`

**File Size in Bytes:** `64381`

---

## 3. Canonical Byte Conditions

The checksum was calculated over the exact bytes of the canonical Markdown artifact under these conditions:

- encoding: UTF-8;
- byte order mark: absent;
- line endings: LF;
- final newline: present;
- trailing whitespace: none detected;
- filename: stable;
- canonical repository path: identified;
- artifact content: finalized for the Candidate lifecycle action.

Any byte-level change invalidates the checksum recorded here.

---

## 4. Checksum

**Hash Algorithm:** `SHA-256`

**Digest Representation:** 64 lowercase hexadecimal characters

**Checksum Value:**

```text
a17f8b099d215db99ef3baebdd6e8838bf7cdeea434e888e26789b477e05ba1c
```

**GNU-compatible checksum line:**

```text
a17f8b099d215db99ef3baebdd6e8838bf7cdeea434e888e26789b477e05ba1c  program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate.md
```

---

## 5. Calculation

**Calculation Date:** 18 July 2026

**Calculating Authority:** Arkadiy Lazarev, Program Originator

**Environment:** Windows Git Bash

**Command Used:**

```bash
sha256sum program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate.md
```

The command returned:

```text
a17f8b099d215db99ef3baebdd6e8838bf7cdeea434e888e26789b477e05ba1c
```

The exact file size was recorded using:

```bash
wc -c program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate.md
```

The command returned:

```text
64381
```

---

## 6. Verification

The digest was recalculated and its representation was validated using:

```bash
sha256sum program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate.md | awk '{print length($1), $1}'
```

The verification output confirmed:

- digest length: `64`;
- representation: lowercase hexadecimal;
- recalculated value: identical to the recorded checksum.

**Verification Result:** Verified

**Second-Party Verification:** Not performed at record creation.

The applicable policy recommends second-party confirmation where available. No applicable Charter clause or Candidate readiness decision was identified as making second-party checksum confirmation mandatory for this transition.

---

## 7. Reproducible Verification Method

From the repository root, run:

```bash
printf '%s  %s\n' \
'a17f8b099d215db99ef3baebdd6e8838bf7cdeea434e888e26789b477e05ba1c' \
'program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate.md' \
| sha256sum --check
```

Expected result:

```text
program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate.md: OK
```

A verifier should also confirm the expected size:

```bash
test "$(wc -c < program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate.md)" -eq 64381 && echo "PASS: file size matches"
```

---

## 8. Registry and Publisher Relationships

At record creation:

- Candidate registry record: Pending;
- Candidate Publisher acknowledgment: Pending.

Those records must reference this integrity record and the exact checksum value.

Their later creation does not change the checksum of the Candidate artifact.

---

## 9. Mismatch Procedure

When recalculation does not match the recorded checksum:

1. do not represent the affected file as the registered Candidate Publication;
2. preserve the mismatched artifact and available evidence;
3. verify canonical path, encoding, line endings, final newline, and file size;
4. determine whether the difference is authorized, accidental, or malicious;
5. suspend reliance on this integrity record where the mismatch remains unexplained;
6. restore the verified canonical artifact or create an authorized corrected or superseding artifact;
7. calculate a new checksum when artifact bytes legitimately change;
8. create or update the applicable correction, integrity, registry, and Publisher records;
9. preserve the historical checksum and supersession relationship.

---

## 10. Conformance Checklist

- [x] canonical artifact identified;
- [x] canonical path recorded;
- [x] encoding fixed;
- [x] line endings fixed;
- [x] approved algorithm used;
- [x] full digest recorded;
- [x] lowercase hexadecimal representation used;
- [x] file size recorded;
- [x] calculation date recorded;
- [x] calculating authority recorded;
- [x] calculation environment and tool recorded;
- [x] verification method recorded;
- [x] checksum recalculated and matched;
- [ ] second-party verification obtained;
- [ ] Candidate registry relationship completed;
- [ ] Candidate Publisher relationship completed;
- [x] mismatch handling defined.

Unchecked relationship items are pending lifecycle records, not checksum failures.

---

## 11. Current Decision

The recorded SHA-256 digest matches the finalized local Candidate artifact at the canonical path.

The artifact is integrity-ready for:

- Candidate lifecycle decision;
- Candidate registry binding;
- Candidate Publisher acknowledgment.

Candidate Publication is not complete until the remaining lifecycle records are created and verified.

---

## 12. Final Disposition

**Disposition:** Verified

**Artifact Integrity:** Confirmed for the recorded canonical bytes

**Registry Binding:** Pending

**Publisher Acknowledgment:** Pending

**Final Approval:** Not granted

---

## 13. Attribution

**Prepared By:** Arkadiy Lazarev

**Role:** Program Originator and foundation-stage calculating authority

**Program:** AISET Program

**Date:** 18 July 2026
