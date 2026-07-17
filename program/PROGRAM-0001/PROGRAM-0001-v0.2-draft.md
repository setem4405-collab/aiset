# PROGRAM-0001 — AISET Program Charter

**Identifier:** PROGRAM-0001

**Title:** AISET Program Charter

**Version:** 0.2 Draft

**Status:** Draft

**Date:** 16 July 2026

**Author:** Arkadiy Lazarev

**Program Originator:** Arkadiy Lazarev

**Lead Editor:** Arkadiy Lazarev

**Publisher:** AISET Program

**License:** Creative Commons Attribution 4.0 International

---

## Document Status

This document is a draft AISET Program Charter.

It has not yet been approved as an AISET Reference Publication or as the governing Charter of the AISET Program.

The Charter is intended to become a program-level normative document after architectural, governance, editorial, and publisher review.

Once approved, the following provisions are normative for the AISET Program:

- program identity;
- mission;
- program scope and boundaries;
- foundational principles;
- document hierarchy;
- program roles and authorities;
- publication and approval requirements;
- versioning and amendment rules;
- continuity and succession requirements.

Descriptive background, examples, forecasts, and implementation guidance are informative unless explicitly identified as normative.

Where this Charter uses **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, or **MAY**, those terms express normative program requirements.

Until approval, this draft remains non-binding and may be revised during review.

---

## 1. Purpose

This Charter establishes the foundational identity, mission, scope, principles, structure, authority, governance direction, publication model, and continuity requirements of the AISET Program.

The Charter defines the institutional and engineering framework within which AISET publications, specifications, schemas, registries, reference implementations, governance records, and related artifacts are developed and maintained.

---

## 2. Program Identity

The name of the program is:

> **AISET Program**

AISET is an open, technology-independent engineering program for standardizing the architecture of cognitive context transformations.

AISET does not standardize intelligence.

AISET standardizes the architectural conditions under which cognitive state can be represented, transformed, validated, trusted, measured, shared, composed, and evolved across heterogeneous technologies, implementations, people, and organizations.

---

## 3. Mission

The mission of the AISET Program is:

> **Standardizing the Architecture of Cognitive Context Transformations.**

The AISET Program develops vendor-neutral architectural knowledge, specifications, schemas, registries, governance mechanisms, evaluation methods, and reference implementations for reliable cognitive context processing and shared cognitive evolution.

---

## 4. Engineering Problem

Cognitive systems are increasingly implemented through heterogeneous models, services, software platforms, organizations, and human participants.

These systems commonly lack shared architectural standards for:

- representing cognitive state;
- defining transformations of cognitive state;
- preserving and validating invariants;
- recording trust and provenance;
- measuring transformation quality;
- establishing compatibility;
- enabling interoperability;
- composing transformations;
- governing context evolution;
- replacing implementations without redefining the architecture.

The AISET Program exists to address this engineering gap.

---

## 5. Program Scope

The AISET Program includes the development and governance of:

- AISET publications;
- architecture reference documents;
- Cognitive Context Object specifications;
- Cognitive Transformation Specifications;
- Cognitive Invariant specifications;
- Cognitive Processing Cycle specifications;
- Cognitive Interface Specifications;
- trust and provenance frameworks;
- cognitive metrics;
- compatibility and interoperability specifications;
- context evolution models;
- schemas;
- registries;
- implementation profiles;
- conformance requirements;
- reference implementations;
- review and publication records.

---

## 6. Program Boundaries

The AISET Program does not prescribe:

- a specific artificial intelligence model;
- a specific model provider;
- a specific software vendor;
- a specific programming language;
- a specific database;
- a specific runtime;
- a specific orchestration framework;
- a specific operating system;
- a specific hardware platform;
- a specific organizational structure for implementers.

Technology-specific implementations may be developed, but they must remain distinguishable from normative AISET architecture.

---

## 7. Foundational Principles

The AISET Program is governed by the following foundational principles.

### 7.1 Technology Independence

No normative AISET entity depends on a specific technology, model, executor, programming language, runtime, vendor, or implementation framework.

### 7.2 Context First

Cognitive Transformations operate on Cognitive Context Objects.

A normative transformation addresses context rather than a particular executor.

### 7.3 Shared Context

Collaboration is represented through coordinated evolution of shared cognitive context rather than direct dependency between executors.

### 7.4 Cognitive Compatibility

Different implementations may be considered compatible when they produce valid Cognitive Context Objects under the same applicable specification.

### 7.5 Cognitive Interoperability

Independent implementations may interoperate when they can jointly participate in the governed transformation and evolution of shared cognitive context.

### 7.6 Cognitive Portability

An implementation may be replaced without changing the applicable Cognitive Transformation Specification.

### 7.7 Explicit Trust and Provenance

Cognitive state changes should preserve traceable information about origin, transformation, authority, evidence, and responsibility.

### 7.8 Independent Measurement

Evaluation criteria should remain separable from the technology or implementation being evaluated.

### 7.9 Governed Context Evolution

Changes to shared cognitive context should be versioned, traceable, reviewable, and subject to explicit invariants and governance rules.

### 7.10 Transparent Publication

AISET publications and specifications should have explicit authorship, status, versioning, review records, licensing, and publication history.

---

## 8. Core Architectural Entities

The AISET Program currently recognizes the following foundational architectural entities:

- Cognitive Context Object;
- Cognitive Transformation;
- Cognitive Transformation Specification;
- Cognitive Invariant;
- Cognitive Processing Cycle;
- Shared Cognitive Evolution;
- Cognitive Compatibility;
- Cognitive Interoperability;
- Cognitive Trust and Provenance;
- Cognitive Metrics;
- Directed Cognitive Graph;
- Cognitive Context Evolution Model;
- Cognitive Interface Specification;
- Cognitive Contracts;
- Cognitive Portability;
- Cognitive Composition.

These entities will be formally defined in future AISET Architecture Reference and normative specification publications.

---

## 9. Program Structure

The AISET Program is organized into the following areas:

- `program/` — program-level documents and charters;
- `publications/` — approved publications and publication records;
- `governance/` — governance principles and procedures;
- `specifications/` — normative and supporting specifications;
- `registry/` — registered identifiers and governed records;
- `schemas/` — machine-readable validation schemas;
- `implementations/` — reference implementations and implementation profiles.

Each area has a distinct role and must preserve the separation between normative architecture, governance, metadata, and implementation-specific material.

### 9.1 Document Hierarchy

The AISET document hierarchy is:

1. AISET Program Charter;
2. approved Governance Documents;
3. approved Architecture Reference Documents;
4. approved Normative Specifications;
5. registered Schemas and Registry Records;
6. Implementation Profiles and Conformance Profiles;
7. Reference Implementations, tools, examples, and guidance.

A lower-level document **MUST NOT** override a higher-level document.

Where two documents at the same level conflict, the following order applies:

1. the document with the more specific scope;
2. the document with the later approved version;
3. the document explicitly designated as superseding the other.

Informative publications, examples, implementations, and repository documentation **MUST NOT** redefine normative program requirements.

### 9.2 Conflict Resolution

A conflict between approved AISET documents must be recorded and resolved through one or more of the following:

- an interpretation record;
- a correction notice;
- an amendment;
- a new document version;
- a superseding publication;
- a registry status update.

Until resolution, the higher-level approved document remains authoritative.

---

## 10. Publication Classes

AISET documents may include:

- Discovery Publications;
- Program Documents;
- Architecture Reference Documents;
- Normative Specifications;
- Governance Documents;
- Research Papers;
- Implementation Profiles;
- Reference Implementation Publications;
- Registry Records;
- Review Records;
- Conformance Reports.

Each publication class may have specialized review and approval requirements.

---

## 11. Publication Lifecycle

AISET publications may pass through the following statuses:

1. Draft;
2. Review;
3. Candidate Publication;
4. Approved Publication;
5. Reference Publication;
6. Superseded;
7. Withdrawn.

A released publication must not be silently modified.

Material changes require a new version, amendment, correction record, or superseding publication.

---

## 12. Program Roles

### 12.1 Program Originator

The Program Originator establishes the foundational mission, identity, architectural intent, and initial direction of the AISET Program.

Program origination is a historical and provenance role. It is distinct from routine repository administration and must remain attributable in the program record.

### 12.2 Author

An Author creates substantive content for an AISET publication, specification, governance document, schema, or other artifact.

Authorship applies to the identified contribution or publication and does not automatically grant approval, publishing, registry, or maintenance authority.

### 12.3 Lead Editor

The Lead Editor maintains terminology, structure, editorial consistency, publication quality, and coherence across AISET documents.

Editorial authority does not by itself authorize final publication.

### 12.4 Reviewer

A Reviewer evaluates a contribution against its stated purpose, architectural principles, normative requirements, publication criteria, and assigned review scope.

A Reviewer must disclose material conflicts of interest.

Review participation does not automatically establish authorship or publication authority.

### 12.5 Publisher

The Publisher authorizes and records an official AISET release after applicable requirements have been satisfied.

The Publisher must preserve the approved text, metadata, release artifacts, review records, and publication history.

### 12.6 Registry Authority

A Registry Authority manages registered identifiers, status records, canonical references, version relationships, and machine-readable metadata within the authority assigned to that role.

Registry administration must not be used to alter the meaning of an approved publication.

### 12.7 Maintainer

A Maintainer manages repository content, issue processing, pull request review, release operations, and technical continuity within assigned authority.

A Maintainer does not automatically hold authorship, approval, publishing, or registry authority.

### 12.8 Contributor

A Contributor submits material, analysis, review findings, specifications, schemas, implementations, tests, or other improvements to the AISET Program.

### 12.9 Separation of Authorities

The AISET Program distinguishes:

- authorship authority;
- editorial authority;
- review authority;
- approval authority;
- publication authority;
- registry authority;
- repository maintenance authority.

One person may perform multiple roles during the initial foundation stage.

As the program matures, material normative publications should receive review or approval from a person or body other than the principal Author where practical.

No role may erase valid authorship, provenance, approval history, or program origin records.

---

## 13. Current Program Authority

During the initial foundation stage:

**Program Originator:** Arkadiy Lazarev

**Author and Lead Editor of PROGRAM-0001:** Arkadiy Lazarev

**Publisher:** AISET Program

**Repository Maintainer:** Arkadiy Lazarev

**Interim Registry Authority:** AISET Program, administered by Arkadiy Lazarev

The initial authority model exists to establish the program foundation.

The same person may temporarily perform multiple roles, but each action must remain attributable to the applicable role.

Future governance documents may:

- delegate authority;
- create review bodies;
- establish working groups;
- create a registry authority;
- establish a publication council;
- define succession procedures.

Such changes must not erase valid authorship, provenance, publication history, or the recorded origin of the AISET Program.

Delegation of operational authority does not transfer historical authorship or program origination.

---

## 14. Contributions

AISET may accept contributions involving:

- editorial improvements;
- architectural proposals;
- normative specifications;
- terminology;
- schemas;
- registry records;
- governance proposals;
- implementations;
- conformance tests;
- technical and publication reviews.

Contributions must follow the repository contribution guidelines, licensing rules, and applicable review procedures.

A contribution does not automatically establish publication authority, authorship of the complete publication, or governance authority.

---

## 15. Review

AISET review may include:

- editorial review;
- architectural review;
- normative review;
- technical review;
- security review;
- privacy review;
- implementation review;
- governance review;
- publisher review.

Review findings should be traceable, specific, and associated with the relevant document, version, or artifact.

### 15.1 Review Outcomes

A review may produce one of the following outcomes:

- approved;
- approved with non-blocking recommendations;
- revision required;
- rejected;
- deferred pending additional evidence;
- referred to another review scope.

Blocking findings must identify the affected requirement, risk, inconsistency, or publication criterion.

### 15.2 Conflicts of Interest

A Reviewer or decision-maker must disclose a material conflict of interest where the person:

- has a direct financial interest in the outcome;
- represents an affected implementation vendor;
- is reviewing a disputed claim concerning their own work;
- cannot reasonably provide independent judgment.

A disclosed conflict does not always require exclusion, but the conflict and its treatment must be recorded.

### 15.3 Disagreement and Lack of Consensus

Where reviewers disagree:

1. the disagreement must be documented;
2. the competing positions and supporting reasons must be recorded;
3. an attempt should be made to resolve the conflict through evidence, clarification, or revision;
4. unresolved disagreement must be referred to the applicable approval authority.

Consensus is preferred but is not always required during the initial foundation stage.

A decision made without consensus must record:

- the decision-maker;
- the unresolved objections;
- the reason for proceeding;
- any conditions or future review requirements.

### 15.4 Appeals

A material review or approval decision may be reconsidered when:

- relevant evidence was unavailable;
- a procedural requirement was not followed;
- a conflict of interest was not disclosed;
- the decision conflicts with a higher-level AISET document;
- a significant technical or governance error is demonstrated.

An appeal does not automatically suspend an approved release unless the Publisher or applicable governance authority determines that suspension is necessary.

---

## 16. Approval and Publication Authority

An AISET publication becomes official only when:

- its identifier and version are explicit;
- its status is explicit;
- required review has been completed;
- blocking review findings have been resolved or formally accepted;
- authorship and editorial records are present;
- licensing is identified;
- release artifacts are prepared;
- the Publisher authorizes release;
- a permanent release record is created.

Repository commits alone do not establish an approved AISET publication.

### 16.1 Decision Record

A publication approval must identify:

- the publication identifier;
- the approved version;
- the approval date;
- the approving authority;
- completed reviews;
- unresolved non-blocking findings;
- publication conditions, if any.

### 16.2 Urgent Corrections

An urgent correction may be authorized where an approved artifact contains:

- a security risk;
- a material legal or licensing defect;
- a broken canonical reference;
- an integrity or checksum defect;
- a critical publication metadata error;
- a defect likely to cause harmful implementation behavior.

An urgent correction must not silently replace the released artifact.

It must use an explicit correction notice, new artifact, new version, or superseding release.

### 16.3 Withdrawal and Suspension

A publication may be suspended or withdrawn where:

- its integrity cannot be verified;
- it contains a material legal or licensing defect;
- it creates a substantial security or safety risk;
- its approval record is invalid;
- it materially misrepresents authorship or provenance;
- it has been superseded and continued use creates significant risk.

Withdrawal must preserve the historical record and state the reason, authority, date, and replacement publication where applicable.

---

## 17. Versioning and Immutability

Every released AISET publication must have an explicit version.

Published versions, Git tags, release manifests, checksums, and release artifacts are treated as immutable records.

AISET publications should use semantic versioning principles in the form:

```text
MAJOR.MINOR.PATCH
```

### 17.1 Major Version

A major version change is required when a change:

- alters the mission or fundamental scope of the program;
- changes a foundational architectural principle;
- changes the document hierarchy;
- materially changes approval or governance authority;
- removes or reverses a normative guarantee;
- creates broad incompatibility with the previous version.

### 17.2 Minor Version

A minor version change is appropriate when a change:

- adds a new compatible program rule;
- adds a role, process, publication class, or governance mechanism;
- materially clarifies an existing requirement without reversing it;
- expands scope in a way consistent with the current major version;
- introduces a compatible amendment.

### 17.3 Patch Version

A patch version change is appropriate when a change:

- corrects grammar, formatting, links, citations, or metadata;
- resolves an unambiguous editorial defect;
- clarifies wording without changing normative meaning;
- corrects a non-substantive publication error.

A patch version must not be used to conceal a normative change.

### 17.4 Pre-release Versions

Draft, review, and candidate versions may use pre-release identifiers such as:

```text
0.2-draft
1.0-rc.1
```

Pre-release versions are not approved Reference Publications unless explicitly designated otherwise.

### 17.5 Immutable Releases

A released artifact must not be silently edited, overwritten, or replaced.

Corrections or substantive changes require:

- a new version;
- a correction notice;
- an amendment;
- or a superseding publication.

Historical versions must remain discoverable.

### 17.6 Version Classification

Where the appropriate version level is disputed, the change must be classified according to its normative effect rather than its textual size.

A small textual change may require a major or minor version if it changes normative meaning.

---

## 18. Registries and Identifiers

AISET identifiers must be:

- unique;
- stable;
- version-aware;
- traceable to canonical artifacts;
- suitable for human and machine use.

Registry records should preserve:

- identifier;
- title;
- object type;
- version;
- status;
- canonical path;
- release information;
- authorship;
- publisher;
- license;
- checksum;
- relationships to other objects.

---

## 19. Normative and Informative Material

AISET documents should distinguish between:

- **Normative material**, which defines requirements, constraints, interfaces, invariants, validation rules, or conformance conditions;
- **Informative material**, which provides explanation, examples, context, guidance, or interpretation.

Normative terms must be used deliberately.

---

## 20. Conformance

A system or implementation may claim conformance only to an identified AISET specification and version.

A conformance claim should state:

- the applicable specification;
- the implemented scope;
- the implementation profile;
- validation evidence;
- known limitations;
- deviations;
- test results where applicable.

Conformance does not automatically imply security, correctness, suitability, or interoperability beyond the stated scope.

---

## 21. Licensing

Unless explicitly stated otherwise, AISET publications, specifications, governance documents, registry records, schemas, and other non-software materials are licensed under the Creative Commons Attribution 4.0 International License.

Software components are licensed separately.

Each software component must identify its applicable software license before public release.

---

## 22. Intellectual Responsibility

Authors, editors, reviewers, publishers, maintainers, and contributors remain responsible for the material they submit, approve, or publish within their assigned roles.

Use of software tools or artificial intelligence systems does not remove human responsibility for:

- accuracy;
- provenance;
- licensing;
- review;
- security;
- publication decisions;
- normative meaning.

---

## 23. Security and Privacy

AISET publications and specifications should identify relevant:

- trust boundaries;
- threat assumptions;
- provenance requirements;
- integrity requirements;
- confidentiality considerations;
- privacy implications;
- failure modes;
- abuse cases;
- implementation risks.

AISET conformance must not be presented as an unconditional guarantee of security or privacy.

---

## 24. Amendments

This Charter may be amended through a documented program process.

An amendment should identify:

- the affected version;
- the proposed change;
- the reason for the change;
- architectural and governance impact;
- review findings;
- approval authority;
- effective date.

Material amendments require a new Charter version.

Released Charter versions must remain historically accessible.

---

## 25. Continuity and Succession

The AISET Program should preserve continuity of:

- publications;
- identifiers;
- registries;
- authorship;
- provenance;
- release history;
- licenses;
- governance records;
- canonical artifacts.

Future succession procedures should prevent loss, silent alteration, appropriation, or misrepresentation of the program’s historical record.

---

## 26. Program Evolution

The AISET Program may evolve through:

- new publications;
- new normative specifications;
- amended governance;
- new registry classes;
- new schemas;
- independent implementations;
- broader review participation;
- delegated roles;
- formal councils or working groups.

Program evolution must remain consistent with the foundational mission and principles recorded in this Charter.

---

## 27. Relationship to DISCOVERY-0001

`DISCOVERY-0001 — AISET Discovery` records why AISET emerged and how the foundational architecture developed from an engineering necessity.

This Charter establishes the program framework through which that architectural direction will be governed, specified, published, implemented, and evolved.

---

## 28. Current Status

The AISET Program is in its initial foundation stage.

This draft Charter is intended to become the first approved AISET Program Charter following review and publisher approval.

---

## 29. Canonical Repository

The canonical public repository is:

`https://github.com/setem4405-collab/aiset`

The canonical website is:

`https://aisetcfs.com`

---

## 30. Attribution

**Author:** Arkadiy Lazarev

**Program Originator:** Arkadiy Lazarev

**Lead Editor:** Arkadiy Lazarev

**Publisher:** AISET Program

---

## 31. License

Copyright © 2026 AISET Program.

This document is licensed under the Creative Commons Attribution 4.0 International License.

See:

- `LICENSE`
- `LICENSES/CC-BY-4.0.txt`