# PROGRAM-0001 Checksum Algorithm Policy 001

**Policy Identifier:** PROGRAM-0001-CHECKSUM-POLICY-001

**Title:** PROGRAM-0001 Checksum Algorithm Policy

**Version:** 1.0 Draft

**Status:** Draft

**Date:** 17 July 2026

**Applies To:** PROGRAM-0001 — AISET Program Charter

**Reference Version:** PROGRAM-0001 v1.0 Review

**Revision Basis:** PROGRAM-0001-REVIEW-008

**Related Specification:** PROGRAM-0001-OPSPEC-001

**Responsible Program:** AISET Program

**Author:** Arkadiy Lazarev

**Publisher:** AISET Program

**License:** Creative Commons Attribution 4.0 International

---

## Document Status

This document defines the checksum algorithm policy for artifacts governed by:

`PROGRAM-0001 v1.0 Review`

It is intended to address:

`NEW-004 — Checksum Algorithm Policy`

as recorded in:

`PROGRAM-0001-REVIEW-008 — Security, Privacy, Governance, and Editorial Re-review`

This policy defines:

- the approved default checksum algorithm;
- canonical byte requirements;
- checksum representation;
- checksum calculation and verification requirements;
- integrity record requirements;
- mismatch handling;
- algorithm deprecation and migration;
- prohibited algorithms;
- lifecycle-specific integrity expectations.

This policy is subordinate to `PROGRAM-0001`.

It does not amend the Charter and must not be interpreted as overriding any higher-level normative requirement.

This Draft requires review before operative adoption.

---

## 1. Purpose

The purpose of this policy is to establish a consistent and verifiable method for demonstrating artifact integrity across the PROGRAM-0001 lifecycle.

The policy is intended to ensure that:

- a checksum refers to an exact artifact;
- the algorithm is explicitly identified;
- the byte representation is stable;
- verification is reproducible;
- mismatches are not ignored;
- weak or ambiguous algorithms are not used;
- future algorithm transitions are controlled and traceable.

---

## 2. Scope

This policy applies to checksums created for:

- PROGRAM-0001 documents;
- review records;
- registry records;
- Publisher acknowledgments;
- operational specifications;
- integrity records;
- Candidate Publication artifacts;
- Approved Publication artifacts;
- Reference Publication artifacts;
- correction or supersession artifacts;
- other records designated by the AISET Program.

This policy governs artifact checksums.

It does not define:

- digital-signature policy;
- identity-verification policy;
- repository authentication;
- transport security;
- encryption policy;
- key-management policy;
- legal admissibility;
- timestamp-authority requirements.

---

## 3. Normative Language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as normative requirements within this policy.

Where this Draft conflicts with an approved higher-level PROGRAM-0001 requirement, the higher-level requirement prevails.

---

## 4. Approved Default Algorithm

The approved default checksum algorithm is:

> **SHA-256**

The normative algorithm identifier is:

`SHA-256`

The expected digest length is:

- 256 bits;
- 32 bytes;
- 64 lowercase hexadecimal characters.

A conforming checksum record MUST identify the algorithm explicitly as `SHA-256`.

The algorithm name MUST NOT be omitted.

---

## 5. Approved Checksum Representation

The normative checksum representation is:

- lowercase hexadecimal;
- exactly 64 characters for SHA-256;
- no `0x` prefix;
- no spaces;
- no line breaks inside the value.

Example format:

```text
sha256:<64-lowercase-hexadecimal-characters>
```

A record MAY store the algorithm and value in separate fields.

Recommended separate-field form:

```text
Hash Algorithm: SHA-256
Checksum Value: <64-lowercase-hexadecimal-characters>
```

---

## 6. Canonical Artifact Principle

A checksum MUST be calculated over the exact bytes of the canonical artifact.

The checksum does not apply merely to:

- visible text;
- rendered appearance;
- conceptual content;
- a filename;
- a repository commit;
- another format of the same document.

Two artifacts with identical visible text but different byte sequences may have different checksums.

---

## 7. Canonical Byte Requirements

Before a checksum is calculated for a text artifact, the canonical artifact MUST have a defined byte representation.

For Markdown and other UTF-8 text artifacts governed by this policy, the canonical representation SHOULD use:

- UTF-8 encoding;
- no byte order mark;
- LF line endings;
- a final newline at end of file;
- no trailing whitespace unless normatively required;
- stable file content;
- stable filename and canonical path.

A checksum record MUST state the actual canonicalization conditions used.

---

## 8. Line-ending Control

Line-ending conversion changes artifact bytes and therefore changes the checksum.

Canonical publication artifacts SHOULD use LF line endings.

Where repository or operating-system settings may convert LF and CRLF, the integrity process MUST verify the bytes of the committed or released canonical artifact rather than relying solely on an editor view.

A checksum MUST NOT be copied from a differently normalized local working copy without verification.

---

## 9. Encoding Control

Canonical text artifacts SHOULD use UTF-8 without a byte order mark.

The integrity record MUST identify the encoding where encoding is relevant.

Re-encoding an artifact creates a different byte representation and requires:

- a new checksum;
- an updated integrity record;
- a documented correction or supersession relationship where applicable.

---

## 10. Filename and Path Binding

An integrity record MUST identify:

- document identifier;
- version;
- lifecycle status;
- canonical filename;
- canonical repository path;
- checksum algorithm;
- checksum value.

The checksum value verifies bytes, not path identity.

Path binding is therefore established by the integrity record, not by the digest alone.

A path change MUST be documented where it affects canonical discovery.

---

## 11. Lifecycle Requirements

### 11.1 Draft

Checksums for Draft artifacts are OPTIONAL unless required by a review, incident, correction, or operational decision.

### 11.2 Review

Checksums for Review artifacts are RECOMMENDED where the exact reviewed artifact must be fixed or independently verified.

### 11.3 Candidate Publication

A Candidate Publication artifact MUST have:

- an integrity record;
- an approved algorithm;
- a recorded checksum;
- a canonical path;
- a reproducible verification method;
- registry binding;
- Publisher acknowledgment or readiness relationship as applicable.

### 11.4 Approved Publication

An Approved Publication artifact MUST retain verifiable checksum evidence.

### 11.5 Reference Publication

An AISET Reference Publication MUST retain publicly discoverable integrity evidence unless restricted by a higher-priority security, legal, or privacy requirement.

---

## 12. Integrity Record Requirements

A checksum used for a lifecycle decision MUST be documented in an integrity record conforming to:

`PROGRAM-0001-OPSPEC-001`

At minimum, the integrity record MUST include:

- record identifier;
- document identifier;
- version;
- lifecycle status;
- canonical file;
- canonical path;
- file size in bytes;
- hash algorithm;
- checksum value;
- calculation date;
- calculating authority;
- calculation environment or tool;
- verification method;
- related registry record;
- related Publisher acknowledgment, where applicable;
- status;
- mismatch procedure.

---

## 13. File-size Recording

An integrity record SHOULD include the exact file size in bytes.

File size is not a cryptographic integrity mechanism.

It is recorded as supporting diagnostic evidence.

A matching file size does not replace checksum verification.

---

## 14. Calculation Authority

The integrity record MUST identify the person, role, or controlled process that calculated the checksum.

Foundation-stage role overlap MUST be disclosed.

The same person MAY author an artifact and calculate its checksum during Draft or Review stages.

For Candidate Publication, second-party confirmation SHOULD be used where available and MUST be used where required by the Charter or an applicable review decision.

---

## 15. Calculation Timing

The checksum MUST be calculated only after:

- the intended artifact content is complete for the stated lifecycle action;
- encoding is fixed;
- line endings are fixed;
- the canonical file is saved;
- the canonical path is identified;
- no further unrecorded edits are expected.

Any byte-level change after calculation invalidates the prior checksum for the changed artifact.

---

## 16. Verification Requirement

A checksum MUST be verified before it is relied upon for:

- Candidate Publication;
- Approved Publication;
- Reference Publication;
- registry binding;
- Publisher recognition;
- recovery validation;
- correction completion;
- incident closure where artifact integrity is material.

Verification MUST compare a newly calculated digest against the recorded expected value.

Visual comparison alone SHOULD NOT be the sole method for high-impact lifecycle actions.

---

## 17. Recommended Verification Commands

### 17.1 Git Bash, Linux, and macOS

```bash
sha256sum <file>
```

Verification using a checksum file:

```bash
sha256sum --check <checksum-file>
```

### 17.2 macOS Alternative

```bash
shasum -a 256 <file>
```

### 17.3 Windows PowerShell

```powershell
Get-FileHash -Algorithm SHA256 <file>
```

### 17.4 OpenSSL

```bash
openssl dgst -sha256 <file>
```

The integrity record SHOULD state the command or method actually used.

---

## 18. Checksum-file Format

Where a standalone checksum file is used, the recommended GNU-compatible format is:

```text
<64-lowercase-hexadecimal-characters>  <filename>
```

Two spaces SHOULD separate the checksum and filename for a binary-mode-compatible representation.

The checksum file SHOULD:

- use UTF-8;
- use LF line endings;
- end with a final newline;
- contain one entry per canonical artifact;
- avoid ambiguous relative paths;
- be stored with the applicable release or integrity record.

---

## 19. Multiple-artifact Sets

Where a lifecycle action covers multiple artifacts, each artifact MUST have its own checksum.

A manifest MAY collect multiple checksum entries.

The manifest MUST identify:

- the set identifier;
- each artifact path;
- each algorithm;
- each checksum;
- calculation date;
- calculating authority;
- manifest status.

A checksum of the manifest MAY be added but does not replace the individual artifact checksums.

---

## 20. Repository Commit Relationship

A repository commit identifier MAY be recorded as supporting provenance.

A commit identifier MUST NOT replace an artifact checksum.

The integrity record SHOULD distinguish:

- artifact checksum;
- repository commit identifier;
- release tag;
- registry record;
- Publisher acknowledgment.

These identifiers serve different purposes.

---

## 21. Mismatch Handling

A checksum mismatch MUST NOT be ignored.

When a mismatch is detected, the responsible authority MUST:

1. stop relying on the affected artifact for the pending lifecycle action;
2. preserve the mismatching artifact and available evidence;
3. recalculate the checksum using a verified method;
4. confirm the expected canonical path and byte representation;
5. investigate line endings, encoding, truncation, corruption, unauthorized modification, and wrong-file selection;
6. classify the event;
7. create or update an integrity or incident record;
8. determine whether suspension, correction, recovery, or replacement is required;
9. record the final disposition.

---

## 22. Integrity Failure Classification

A checksum mismatch SHOULD be classified as one of:

- expected canonicalization difference;
- wrong artifact selected;
- outdated checksum;
- incomplete transfer;
- storage corruption;
- unauthorized modification;
- repository inconsistency;
- tool or process error;
- unknown cause.

An unknown cause MUST remain open until adequately investigated or formally dispositioned.

---

## 23. Suspension on Material Mismatch

A Candidate Publication, Approved Publication, or Reference Publication affected by an unexplained material checksum mismatch MUST be treated as suspended for integrity purposes until:

- the canonical artifact is identified;
- the mismatch is resolved;
- a corrected integrity record is created;
- registry and Publisher records are updated where necessary.

Suspension for integrity purposes does not automatically erase historical status.

---

## 24. Correction and Recalculation

A corrected artifact requires a new checksum.

The previous checksum MUST remain discoverable as historical evidence unless restricted for security, privacy, legal, or safety reasons.

A correction record SHOULD identify:

- old artifact;
- old checksum;
- corrected artifact;
- new checksum;
- correction reason;
- effective date;
- responsible authority;
- related registry and Publisher actions.

---

## 25. Prohibited Algorithms

The following algorithms MUST NOT be used as the sole integrity checksum for artifacts governed by this policy:

- MD5;
- SHA-1;
- CRC32;
- Adler-32;
- non-cryptographic application hashes;
- undocumented proprietary hash functions;
- truncated digests shorter than an approved policy permits.

Such values MAY be retained only as legacy or diagnostic metadata when clearly labeled and accompanied by an approved checksum.

---

## 26. Alternative Algorithms

An alternative cryptographic algorithm MAY be used only when:

- the algorithm is publicly specified;
- the algorithm is suitable for collision-resistant artifact integrity;
- the algorithm identifier is explicit;
- the digest representation is defined;
- the reason is documented;
- approval is recorded;
- compatibility implications are evaluated;
- SHA-256 remains available unless an approved migration policy states otherwise.

Alternative use MUST NOT create ambiguity about which checksum is authoritative.

---

## 27. Algorithm Agility

The AISET Program MUST retain the ability to replace or supplement SHA-256 if:

- material cryptographic weakness is identified;
- ecosystem support becomes inadequate;
- legal or regulatory requirements change;
- a stronger approved algorithm becomes necessary;
- interoperability requirements justify migration.

Algorithm migration MUST be documented through a new or amended policy record.

---

## 28. Algorithm Deprecation

Deprecation of an approved algorithm requires:

- a deprecation decision;
- effective date;
- affected artifact scope;
- replacement algorithm;
- migration procedure;
- compatibility period;
- treatment of historical checksums;
- registry and Publisher implications;
- verification guidance.

Historical SHA-256 checksums MUST NOT be silently deleted merely because a later algorithm is adopted.

---

## 29. Dual-hash Migration

During an algorithm transition, an artifact MAY carry both:

- the existing approved checksum;
- the replacement checksum.

A dual-hash record MUST identify which algorithm is:

- primary;
- transitional;
- historical;
- required for new verification.

The same canonical bytes MUST be used for both calculations.

---

## 30. Truncation Policy

SHA-256 digests governed by this policy MUST NOT be truncated.

The full 64-character lowercase hexadecimal digest is REQUIRED.

Display interfaces MAY visually abbreviate a checksum only when:

- the full value remains available;
- the abbreviation is clearly identified;
- the abbreviated value is not used for authoritative verification.

---

## 31. Copy and Transcription Control

Checksum values SHOULD be generated and transferred mechanically.

Manual transcription SHOULD be avoided.

Where manual transcription occurs, the value MUST be independently rechecked against the calculated output.

Whitespace, capitalization, punctuation, and prefixes MUST NOT be allowed to create ambiguity.

---

## 32. Public Integrity Evidence

Integrity evidence for public Candidate, Approved, or Reference Publications SHOULD be publicly discoverable.

Public integrity evidence SHOULD include:

- artifact identifier;
- version;
- canonical path;
- algorithm;
- checksum;
- calculation date;
- verification method;
- integrity record identifier.

Restricted supporting evidence MAY remain non-public where justified.

---

## 33. Backup and Recovery Verification

A restored artifact MUST be checksum-verified before being accepted as canonical.

Recovery verification SHOULD compare the restored artifact against:

- the recorded checksum;
- the canonical filename and path;
- the recorded file size;
- the registry relationship;
- the applicable release or Publisher record.

A recovery record MUST document unresolved mismatches.

---

## 34. Third-party Distribution

Where an artifact is distributed through a third-party service, the AISET Program SHOULD publish checksum evidence through an independently discoverable canonical channel.

A third-party copy MUST NOT become canonical merely because its checksum matches.

Canonicality and integrity are separate properties.

---

## 35. Tool Independence

This policy does not require a specific software tool.

A conforming implementation MAY use any tool that:

- correctly implements the approved algorithm;
- operates on the exact artifact bytes;
- produces a verifiable digest;
- identifies the algorithm;
- supports reproducible verification.

Tool output SHOULD be normalized into the representation defined by this policy.

---

## 36. Security Considerations

A checksum detects byte differences but does not by itself prove:

- author identity;
- publication authority;
- creation time;
- absence of malicious substitution when both artifact and checksum are replaced;
- confidentiality;
- authenticity of the distribution channel.

Higher assurance may require:

- trusted registry records;
- Publisher records;
- authenticated repository history;
- digital signatures;
- independent publication channels;
- controlled release procedures.

---

## 37. Privacy Considerations

Checksum values normally do not reveal document content directly.

However, checksums of predictable or low-entropy sensitive content may support guessing attacks.

A restricted artifact checksum SHOULD NOT be published automatically without considering whether publication could expose sensitive relationships or confirm possession of protected content.

---

## 38. Conformance Checklist

A conforming checksum action should confirm:

- [ ] the canonical artifact is identified;
- [ ] the canonical path is recorded;
- [ ] encoding is fixed;
- [ ] line endings are fixed;
- [ ] the approved algorithm is used;
- [ ] the full digest is recorded;
- [ ] lowercase hexadecimal representation is used;
- [ ] file size is recorded;
- [ ] calculation date is recorded;
- [ ] calculating authority is recorded;
- [ ] verification method is recorded;
- [ ] the checksum is independently verified where required;
- [ ] registry and Publisher relationships are recorded;
- [ ] mismatch handling is defined.

---

## 39. Current Adoption Status

This policy is currently:

**Status:** Draft

It has not yet been approved as an operative subordinate policy.

The next intended actions are:

1. review this policy;
2. verify alignment with `PROGRAM-0001 v1.0 Review`;
3. verify compatibility with `PROGRAM-0001-OPSPEC-001`;
4. correct any blocking or major findings;
5. approve or register the policy if appropriate;
6. apply it to Candidate Publication integrity records.

---

## 40. Relationship to NEW-004

This policy is intended to satisfy the requirement identified as:

`NEW-004 — Checksum Algorithm Policy`

Closure of `NEW-004` requires a later review or disposition record confirming that:

- an approved default algorithm is defined;
- canonical byte conditions are defined;
- checksum representation is unambiguous;
- lifecycle requirements are defined;
- verification methods are reproducible;
- mismatch handling is defined;
- weak algorithms are prohibited;
- migration and deprecation procedures are defined.

This document alone does not close the finding without review.

---

## 41. Attribution

**Author:** Arkadiy Lazarev

**Program Originator:** Arkadiy Lazarev

**Lead Editor:** Arkadiy Lazarev

**Publisher:** AISET Program

**Registry Authority:** AISET Program

---

## 42. License

Copyright © 2026 AISET Program.

This policy is licensed under the Creative Commons Attribution 4.0 International License.

See:

- `LICENSE`
- `LICENSES/CC-BY-4.0.txt`
