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

The current integrity record sequence is:

1. `PROGRAM-0001-INTEGRITY-001`

---

## 3. PROGRAM-0001-INTEGRITY-001

**Title:** PROGRAM-0001 v1.0 Candidate Publication Integrity Record

**Related Version:** PROGRAM-0001 v1.0 Candidate

**Lifecycle Status:** Candidate Publication

**Status:** Active

**Disposition:** Verified

**Canonical Artifact:**

`program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate.md`

**Hash Algorithm:** SHA-256

**Checksum Value:**

```text
a17f8b099d215db99ef3baebdd6e8838bf7cdeea434e888e26789b477e05ba1c
```

**File Size:** 64381 bytes

**File:**

`PROGRAM-0001-candidate-integrity-record-001.md`

---

## 4. Current Integrity State

The current Candidate artifact has verified integrity evidence.

The integrity record is linked to:

- `PROGRAM-0001-CANDIDATE-DECISION-001`;
- `PROGRAM-0001-REGISTRY-005`;
- `PROGRAM-0001-PUBLISHER-ACK-005`.

Any byte-level change to the Candidate artifact invalidates the recorded checksum for the changed bytes and requires updated integrity, registry, and Publisher records.

---

## 5. Verification

From the repository root:

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
