# PROGRAM-0001 Operational Record Specification 001

**Specification Identifier:** PROGRAM-0001-OPSPEC-001

**Title:** PROGRAM-0001 Operational Record Specification

**Version:** 1.0 Review

**Status:** Review

**Date:** 17 July 2026

**Applies To:** PROGRAM-0001 — AISET Program Charter

**Reference Version:** PROGRAM-0001 v1.0 Review

**Revision Basis:** PROGRAM-0001-REVIEW-008

**Review Basis:** PROGRAM-0001-REVIEW-009

**Previous Version:** 1.0 Draft

**Responsible Program:** AISET Program

**Author:** Arkadiy Lazarev

**Publisher:** AISET Program

**License:** Creative Commons Attribution 4.0 International

---

## Document Status

This document defines a consolidated operational record specification for records required or anticipated by:

`PROGRAM-0001 v1.0 Review`

It is intended to address:

`NEW-003 — Operational Record Specifications`

as recorded in:

`PROGRAM-0001-REVIEW-008 — Security, Privacy, Governance, and Editorial Re-review`

This specification provides reusable minimum structures for:

- classification decisions;
- access-control decisions;
- declassification and disclosure decisions;
- incident records;
- notification decisions;
- continuity and recovery records;
- third-party dependency records;
- integrity records;
- correction, redaction, and deletion records;
- governance-capture assessments;
- security-sensitive change records;
- participation-restriction records;
- foundation-stage exception records.

This document is subordinate to `PROGRAM-0001`.

It does not amend the Charter and must not be interpreted as overriding any higher-level normative requirement.

This Review version was authorized for progression by `PROGRAM-0001-REVIEW-009`. It remains subject to registration and Publisher acknowledgment before it is treated as the active subordinate Review document.

---

## 1. Purpose

The purpose of this specification is to ensure that operational governance records are:

- identifiable;
- consistently structured;
- traceable;
- reviewable;
- classifiable;
- integrity-verifiable;
- privacy-aware;
- suitable for registry or Publisher reference where applicable.

The specification establishes common fields and record-specific minimum requirements.

---

## 2. Scope

This specification applies to operational records created under `PROGRAM-0001`.

It covers records concerning:

- governance classification;
- access control;
- restricted disclosure;
- security and privacy incidents;
- credential and authority compromise;
- continuity and recovery;
- external dependencies;
- artifact integrity;
- correction and redaction;
- malicious participation and governance capture;
- security-sensitive changes;
- participation restrictions;
- foundation-stage exceptions.

It does not define:

- the full Charter lifecycle;
- final approval criteria;
- Candidate Publication approval;
- repository implementation details;
- legal compliance obligations;
- infrastructure-specific incident procedures.

---

## 3. Conformance

A record conforms to this specification when it:

- uses an applicable record type;
- contains all mandatory common fields;
- contains all mandatory fields for that record type;
- identifies unavailable information explicitly;
- preserves required relationships;
- follows the classification and integrity rules;
- records responsible authority;
- records status and disposition.

A conforming record may include additional fields.

An implementation must not omit a mandatory field silently.

Where information is unavailable, the field must state:

- `Unknown`;
- `Not Available`;
- `Not Applicable`;
- `Pending`;
- another documented equivalent.

---

## 4. Record Identifier Model

Each operational record must have a persistent identifier.

The recommended format is:

`PROGRAM-0001-<RECORD-TYPE>-<SEQUENCE>`

Examples:

- `PROGRAM-0001-CLASS-001`;
- `PROGRAM-0001-ACCESS-001`;
- `PROGRAM-0001-INCIDENT-001`;
- `PROGRAM-0001-NOTIFY-001`;
- `PROGRAM-0001-RECOVERY-001`;
- `PROGRAM-0001-DEPENDENCY-001`;
- `PROGRAM-0001-INTEGRITY-001`;
- `PROGRAM-0001-CORRECTION-001`;
- `PROGRAM-0001-CAPTURE-001`;
- `PROGRAM-0001-SECCHANGE-001`;
- `PROGRAM-0001-RESTRICTION-001`;
- `PROGRAM-0001-EXCEPTION-001`.

Identifiers must not be reused.

A corrected or superseding record must preserve the original identifier and add a new identifier for the new record.

---

## 5. Common Record Fields

Every operational record must include:

- **Record Identifier**
- **Record Type**
- **Title**
- **Status**
- **Classification**
- **Creation Date**
- **Effective Date**
- **Responsible Authority**
- **Author or Recorder**
- **Related Document**
- **Related Version**
- **Related Review or Decision**
- **Canonical File**
- **Summary**
- **Disposition**
- **Integrity Information**
- **Retention or Review Condition**
- **License or Access Terms**

Where applicable, a record should also include:

- previous record;
- superseding record;
- affected persons;
- affected systems;
- conflict disclosure;
- approval authority;
- reviewer;
- public metadata record;
- restricted evidence record;
- registry relationship;
- Publisher relationship.

---

## 6. Record Statuses

Operational record statuses are:

- **Draft**
- **Active**
- **Historical**
- **Superseded**
- **Corrected**
- **Suspended**
- **Closed**
- **Withdrawn**
- **Invalidated**

A record must identify its current status.

A status transition must identify:

- previous status;
- new status;
- transition date;
- responsible authority;
- reason;
- related decision or record.

A record must not be silently replaced.

---

## 7. Record Classifications

The permitted classifications are:

- **Public**
- **Internal**
- **Restricted**
- **Confidential Security**
- **Personal Data Restricted**

Each record must identify one classification.

A non-public record should have a public metadata record where required by the Charter.

The public metadata record must not disclose protected content.

---

## 8. Canonical File and Location

Each operational record must identify its canonical file.

The recommended directory is:

`program/PROGRAM-0001/operations/`

Subdirectories may be used by record type.

A canonical path change requires:

- a correction record;
- a registry update where applicable;
- preservation of the historical path;
- a traceable migration record.

---

## 9. Integrity Requirements

Each operational record should identify:

- hash algorithm;
- checksum value;
- calculation date;
- calculation authority;
- verification instructions.

Integrity evidence is mandatory where required by the Charter or a later approved policy.

A checksum mismatch must be treated according to the applicable integrity-failure procedure.

---

## 10. Classification Decision Record

### 10.1 Identifier

Recommended type code:

`CLASS`

### 10.2 Mandatory Fields

A classification decision record must include:

- subject record identifier;
- assigned classification;
- classification authority;
- basis;
- effective date;
- permitted audience;
- handling requirements;
- review date;
- declassification or disclosure condition;
- public metadata requirement;
- related restricted record, if any.

### 10.3 Disposition

Permitted dispositions include:

- classification assigned;
- classification changed;
- declassified;
- disclosure expanded;
- classification retained;
- classification invalidated.

---

## 11. Access-Control Decision Record

### 11.1 Identifier

Recommended type code:

`ACCESS`

### 11.2 Mandatory Fields

An access-control decision record must include:

- subject record or system;
- requesting person or role;
- requested access;
- granted access;
- authority;
- purpose;
- basis;
- start date;
- expiry or review date;
- conditions;
- revocation method;
- exceptional disclosure status;
- audit or logging requirement.

### 11.3 Disposition

Permitted dispositions include:

- granted;
- granted with restrictions;
- denied;
- revoked;
- expired;
- suspended;
- corrected.

---

## 12. Declassification and Disclosure Record

### 12.1 Identifier

Recommended type code:

`DISCLOSE`

### 12.2 Mandatory Fields

A declassification or disclosure record must include:

- subject record;
- previous classification;
- new classification or disclosure scope;
- decision authority;
- decision basis;
- effective date;
- redactions;
- affected persons;
- notification decision;
- public metadata update;
- review or reversal condition.

### 12.3 Disposition

Permitted dispositions include:

- declassified;
- partially disclosed;
- disclosure denied;
- disclosure deferred;
- classification retained;
- corrected.

---

## 13. Security and Privacy Incident Record

### 13.1 Identifier

Recommended type code:

`INCIDENT`

### 13.2 Mandatory Fields

An incident record must include:

- incident identifier;
- discovery date and time;
- reported date and time;
- severity;
- incident category;
- affected systems;
- affected records;
- affected authorities;
- affected persons;
- incident authority;
- containment actions;
- evidence-preservation actions;
- compromise window;
- recovery status;
- notification decision;
- retrospective-review status;
- closure criteria;
- follow-up actions.

### 13.3 Severity

Recommended severity levels are:

- Low;
- Moderate;
- High;
- Critical.

A severity method should define:

- confidentiality impact;
- integrity impact;
- availability impact;
- governance impact;
- personal-data impact;
- publication-status impact.

### 13.4 Disposition

Permitted dispositions include:

- open;
- contained;
- recovering;
- monitoring;
- closed;
- reopened;
- invalidated.

---

## 14. Notification Decision Record

### 14.1 Identifier

Recommended type code:

`NOTIFY`

### 14.2 Mandatory Fields

A notification decision record must include:

- related incident or governance event;
- affected audience;
- notification authority;
- decision;
- decision date;
- severity assessment;
- further-harm assessment;
- legal or contractual consideration;
- public-interest consideration;
- notification channel;
- notification deadline;
- delay basis, if any;
- completion evidence.

### 14.3 Disposition

Permitted dispositions include:

- notification required;
- notification not required;
- notification delayed;
- partial notification;
- completed;
- corrected.

---

## 15. Continuity and Recovery Record

### 15.1 Identifier

Recommended type code:

`RECOVERY`

### 15.2 Mandatory Fields

A continuity or recovery record must include:

- triggering event;
- affected canonical resources;
- recovery authority;
- backup source;
- backup verification;
- restoration procedure;
- restoration start;
- restoration completion;
- alternate canonical location;
- registry-history verification;
- integrity-evidence verification;
- post-recovery validation;
- unresolved risks;
- closure decision.

### 15.3 Disposition

Permitted dispositions include:

- recovery initiated;
- partial recovery;
- full recovery;
- alternate operation;
- recovery failed;
- closed;
- superseded.

---

## 16. Third-party Dependency Record

### 16.1 Identifier

Recommended type code:

`DEPENDENCY`

### 16.2 Mandatory Fields

A dependency record must include:

- provider or service;
- dependency purpose;
- service category;
- data handled;
- authority granted;
- access granted;
- canonicality implications;
- availability implications;
- privacy implications;
- security implications;
- backup availability;
- compromise response;
- exit or migration path;
- review date;
- responsible owner.

### 16.3 Disposition

Permitted dispositions include:

- approved for use;
- approved with conditions;
- under review;
- migration required;
- suspended;
- retired;
- replaced.

---

## 17. Artifact Integrity Record

### 17.1 Identifier

Recommended type code:

`INTEGRITY`

### 17.2 Mandatory Fields

An integrity record must include:

- document identifier;
- version;
- lifecycle status;
- canonical file;
- hash algorithm;
- checksum value;
- calculation date;
- calculating authority;
- verification command or method;
- related registry record;
- related Publisher acknowledgment;
- related approval or readiness decision;
- mismatch procedure;
- status.

### 17.3 Disposition

Permitted dispositions include:

- verified;
- verification pending;
- mismatch detected;
- suspended;
- corrected;
- superseded;
- invalidated.

---

## 18. Correction, Redaction, and Deletion Record

### 18.1 Identifier

Recommended type code:

`CORRECTION`

### 18.2 Mandatory Fields

A correction, redaction, or deletion record must include:

- affected record;
- action type;
- authority;
- reason;
- affected fields or content;
- effective date;
- emergency status;
- replacement record;
- sanitized historical record;
- notification decision;
- integrity update;
- registry update, if applicable.

### 18.3 Action Types

Action types include:

- factual correction;
- personal-data correction;
- redaction;
- secret removal;
- credential removal;
- unlawful-content removal;
- duplicate removal;
- deletion;
- sanitized replacement.

### 18.4 Disposition

Permitted dispositions include:

- completed;
- partially completed;
- denied;
- deferred;
- reversed;
- superseded.

---

## 19. Governance-capture Assessment Record

### 19.1 Identifier

Recommended type code:

`CAPTURE`

### 19.2 Mandatory Fields

A governance-capture assessment must include:

- triggering indicator;
- affected process;
- affected roles;
- suspected coordination;
- conflict information;
- evidence classification;
- assessment authority;
- protective controls;
- legitimate-dissent safeguards;
- second-party confirmation;
- outcome;
- follow-up review.

### 19.3 Disposition

Permitted dispositions include:

- no capture identified;
- concern substantiated;
- concern partially substantiated;
- monitoring required;
- participation controls imposed;
- authority suspended;
- external review required.

---

## 20. Security-sensitive Change Record

### 20.1 Identifier

Recommended type code:

`SECCHANGE`

### 20.2 Mandatory Fields

A security-sensitive change record must include:

- change identifier;
- affected provision;
- change summary;
- security impact statement;
- privacy impact statement;
- affected authorities;
- conflict review;
- second-party reviewer;
- verification method;
- identified risks;
- risk dispositions;
- approval authority;
- implementation status;
- rollback or correction plan.

### 20.3 Disposition

Permitted dispositions include:

- approved;
- approved with conditions;
- revision required;
- rejected;
- deferred;
- withdrawn;
- superseded.

---

## 21. Participation-restriction Record

### 21.1 Identifier

Recommended type code:

`RESTRICTION`

### 21.2 Mandatory Fields

A participation-restriction record must include:

- affected participant or role;
- restriction basis;
- restriction scope;
- effective date;
- duration;
- authority;
- evidence classification;
- public summary;
- reconsideration path;
- appeal path;
- review date;
- removal condition.

### 21.3 Disposition

Permitted dispositions include:

- active;
- modified;
- suspended;
- expired;
- removed;
- overturned;
- superseded.

---

## 22. Foundation-stage Exception Record

### 22.1 Identifier

Recommended type code:

`EXCEPTION`

### 22.2 Mandatory Fields

A foundation-stage exception record must include:

- affected rule;
- requested exception;
- requesting authority;
- decision authority;
- non-circularity mechanism;
- independent or second-party confirmation;
- conflict disclosure;
- scope;
- duration;
- effective date;
- expiry;
- review condition;
- revocation method;
- final disposition.

### 22.3 Prohibited Condition

The same person must not be the sole requester, sole approver, sole confirmer, and sole beneficiary of the exception.

### 22.4 Disposition

Permitted dispositions include:

- approved;
- approved with conditions;
- denied;
- expired;
- revoked;
- superseded;
- invalidated.

---

## 23. Public Metadata Record

Where a material record is non-public, a public metadata record should include:

- protected record identifier;
- record type;
- existence statement;
- general category;
- classification;
- withholding basis;
- responsible authority;
- creation date;
- review date;
- disclosure condition;
- public disposition.

The public metadata record must not expose restricted content.

---

## 24. Relationship Fields

Operational records should use explicit relationship fields such as:

- `Related Record`;
- `Previous Record`;
- `Supersedes`;
- `Superseded By`;
- `Corrects`;
- `Corrected By`;
- `Related Review`;
- `Related Registry Record`;
- `Related Publisher Acknowledgment`;
- `Related Incident`;
- `Related Decision`;
- `Related Integrity Record`.

Relationships must be reciprocal where practical.

---

## 25. Record Naming

Recommended filenames are:

`PROGRAM-0001-<record-type-lowercase>-<sequence>.md`

Examples:

- `PROGRAM-0001-incident-001.md`;
- `PROGRAM-0001-integrity-001.md`;
- `PROGRAM-0001-dependency-001.md`;
- `PROGRAM-0001-secchange-001.md`.

A filename should remain stable after publication.

---

## 26. Record Templates

A conforming template should include:

1. metadata;
2. purpose;
3. scope;
4. facts or evidence;
5. decision authority;
6. analysis;
7. disposition;
8. relationships;
9. integrity;
10. attribution;
11. license or access terms.

Record-specific fields may be added as dedicated sections.

---

## 27. Privacy and Security Handling

A record author must avoid including unnecessary:

- personal identifiers;
- contact information;
- credentials;
- secrets;
- exploit details;
- private relationship details;
- financial information;
- location information;
- allegations not required for the decision.

Sensitive evidence should be separated from public summaries.

---

## 28. Review and Approval

A material operational record should receive review proportionate to its impact.

Records concerning the following require second-party review:

- Candidate Publication integrity;
- material authority restoration;
- foundation-stage exceptions affecting final approval;
- security-sensitive changes;
- governance-capture findings;
- critical incidents;
- final participation restrictions with material effect.

The reviewer must disclose conflicts and role overlap.

---

## 29. Retention

Each record must identify a retention or review condition.

Possible conditions include:

- permanent historical preservation;
- preservation until superseded;
- review after a defined period;
- deletion after a defined period;
- retention while a dependency remains active;
- retention while legal, security, or governance obligations remain.

Secrets and credentials must not be retained merely for historical completeness.

---

## 30. Correction and Supersession

A published operational record must not be silently modified.

A material correction requires:

- a new correction record;
- a corrected replacement;
- preserved historical relationship;
- updated integrity evidence;
- registry or Publisher update where applicable.

A superseded record remains discoverable unless restricted for security, privacy, legal, or safety reasons.

---

## 31. Minimum Repository Structure

The recommended structure is:

```text
program/PROGRAM-0001/
├── operations/
│   ├── README.md
│   ├── classification/
│   ├── access/
│   ├── incidents/
│   ├── notifications/
│   ├── recovery/
│   ├── dependencies/
│   ├── integrity/
│   ├── corrections/
│   ├── capture/
│   ├── security-changes/
│   ├── restrictions/
│   └── exceptions/
```

Subdirectories may remain uncreated until the first record of that type exists.

---

## 32. Current Adoption Status

This specification is currently:

**Status:** Review

It has been approved by `PROGRAM-0001-REVIEW-009` for subordinate Review status. It has not yet been registered or acknowledged by the Publisher as the active subordinate Review specification.

The next intended actions are:

1. register this Review version;
2. create the applicable Publisher acknowledgment;
3. index the active subordinate Review document;
4. use it as the governing Review specification for future operational records;
5. conduct later revision when implementation experience requires it.

---

## 33. Relationship to NEW-003

This specification is intended to satisfy the requirement identified as:

`NEW-003 — Operational Record Specifications`

`PROGRAM-0001-REVIEW-009` determined that:

- the required operational record types are covered;
- mandatory fields are sufficient;
- classifications are aligned;
- record relationships are traceable;
- privacy and integrity requirements are preserved.

**Disposition:** `NEW-003 — Resolved`

---

## 34. Attribution

**Author:** Arkadiy Lazarev

**Program Originator:** Arkadiy Lazarev

**Lead Editor:** Arkadiy Lazarev

**Publisher:** AISET Program

**Registry Authority:** AISET Program

---

## 35. License

Copyright © 2026 AISET Program.

This specification is licensed under the Creative Commons Attribution 4.0 International License.

See:

- `LICENSE`
- `LICENSES/CC-BY-4.0.txt`
