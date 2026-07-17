# PROGRAM-0001 — AISET Program Charter

**Identifier:** PROGRAM-0001

**Title:** AISET Program Charter

**Version:** 0.5 Draft

**Status:** Draft

**Date:** 16 July 2026

**Author:** Arkadiy Lazarev

**Program Originator:** Arkadiy Lazarev

**Lead Editor:** Arkadiy Lazarev

**Publisher:** AISET Program

**Previous Version:** PROGRAM-0001 v0.4 Draft

**Revision Basis:** PROGRAM-0001-REVIEW-003

**License:** Creative Commons Attribution 4.0 International

---

## Document Status

This document is a revised Draft of the AISET Program Charter.

It was prepared in response to:

`PROGRAM-0001-REVIEW-002 — Normative Terminology Review`

That review determined that `PROGRAM-0001 v0.3 Review` was architecturally coherent but required targeted normative terminology revision before progression to Candidate Publication.

This Draft therefore returns the Charter from Review to Draft for the limited purpose of:

- establishing one authoritative normative keyword policy;
- converting binding requirements to uppercase normative keywords;
- distinguishing normative permission from factual possibility;
- clarifying the normative scope of individual clauses;
- removing `Cognitive Contracts` from the foundational entity list;
- replacing `Cognitive Composition` with `Cognitive Transformation Composition`;
- introducing canonical terminology and capitalization rules.

This document has not been approved as the governing Charter of the AISET Program or as an AISET Reference Publication.

### Normative Keyword Policy

Only clauses using the uppercase keywords **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, or **MAY** are normative requirements of this Charter.

The keywords have the following meanings:

- **MUST** indicates an absolute requirement.
- **MUST NOT** indicates an absolute prohibition.
- **SHOULD** indicates a recommended requirement that can be departed from only for a documented and justified reason.
- **SHOULD NOT** indicates a discouraged action that can be taken only for a documented and justified reason.
- **MAY** indicates normative permission.

Lowercase words such as `must`, `should`, and `may` do not carry normative force in this document unless they appear inside a quotation.

Descriptive background, examples, historical statements, forecasts, and implementation guidance are informative unless they contain an explicit uppercase normative keyword.

While this document remains in Draft status, all provisions remain reviewable and non-binding.

---

## 1. Purpose

This Charter establishes the foundational identity, mission, scope, principles, structure, authority, governance direction, publication model, and continuity requirements of the AISET Program.

The Charter defines the institutional and engineering framework within which AISET publications, specifications, schemas, registries, reference implementations, governance records, and related artifacts are developed and maintained.

Upon approval, program activities covered by this Charter **MUST** conform to its normative clauses.

---

## 2. Program Identity

The name of the program is:

> **AISET Program**

AISET is an open, technology-independent engineering program for standardizing the architecture of cognitive context transformations.

AISET does not standardize intelligence.

AISET standardizes the architectural conditions under which cognitive state can be represented, transformed, validated, trusted, measured, shared, composed, and evolved across heterogeneous technologies, implementations, people, and organizations.

The program identity **MUST NOT** be represented as dependent on a specific model, vendor, runtime, or implementation framework.

---

## 3. Mission

The mission of the AISET Program is:

> **Standardizing the Architecture of Cognitive Context Transformations.**

The AISET Program develops vendor-neutral architectural knowledge, specifications, schemas, registries, governance mechanisms, evaluation methods, and reference implementations for reliable cognitive context processing and shared cognitive evolution.

Material program decisions **SHOULD** remain consistent with this mission.

A decision that materially changes the mission **MUST** be treated as a major Charter revision.

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

This section is informative.

---

## 5. Program Scope

The AISET Program includes the development and governance of:

- AISET publications;
- Architecture Reference documents;
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

Program work represented as normative AISET architecture **MUST** fall within the declared scope or be introduced through an approved Charter amendment.

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

Technology-specific implementations **MAY** be developed.

Technology-specific material **MUST** remain distinguishable from normative AISET architecture.

A normative AISET requirement **MUST NOT** depend on a specific vendor, model, language, runtime, or implementation framework unless the dependency is explicitly confined to a technology-specific profile.

---

## 7. Foundational Principles

The AISET Program is governed by the following foundational principles.

### 7.1 Technology Independence

A normative AISET entity **MUST NOT** depend on a specific technology, model, executor, programming language, runtime, vendor, or implementation framework.

Technology-specific profiles **MAY** define constrained dependencies when those dependencies are explicit and do not redefine the technology-independent architecture.

### 7.2 Context First

Cognitive Transformations operate on Cognitive Context Objects.

A normative transformation **MUST** address context rather than a particular executor.

An implementation **MUST NOT** redefine a transformation solely by reference to the identity of the executor.

### 7.3 Shared Context

Collaboration is represented through coordinated evolution of shared cognitive context rather than direct dependency between executors.

Interoperable implementations **SHOULD** coordinate through governed changes to shared Cognitive Context Objects.

### 7.4 Cognitive Compatibility

Different implementations can be considered compatible when they produce valid Cognitive Context Objects under the same applicable specification.

A compatibility claim **MUST** identify the applicable specification and version.

### 7.5 Cognitive Interoperability

Independent implementations can interoperate when they jointly participate in the governed transformation and evolution of shared cognitive context.

An interoperability claim **MUST** identify the shared context, applicable specifications, and tested scope.

### 7.6 Cognitive Portability

An implementation can be replaced without changing the applicable Cognitive Transformation Specification.

A portability claim **MUST** identify the replaced implementation, replacement implementation, applicable specification, and validation evidence.

### 7.7 Explicit Trust and Provenance

Cognitive state changes **SHOULD** preserve traceable information about origin, transformation, authority, evidence, and responsibility.

A specification that omits required provenance information **SHOULD** document the reason and resulting limitations.

### 7.8 Independent Measurement

Evaluation criteria **SHOULD** remain separable from the technology or implementation being evaluated.

A conformance metric **MUST NOT** depend exclusively on vendor-controlled evidence when independent validation is required by the applicable specification.

### 7.9 Governed Context Evolution

Changes to shared cognitive context **SHOULD** be versioned, traceable, reviewable, and subject to explicit invariants and governance rules.

A normative shared-context process **MUST** define how invalid or unauthorized state transitions are detected or handled.

### 7.10 Transparent Publication

AISET publications and specifications **MUST** have explicit authorship, status, versioning, licensing, and publication history.

Approved and released publications **MUST** preserve applicable review and decision records.

---

## 8. Core Architectural Entities

The AISET Program currently recognizes the following foundational architectural terms:

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
- Cognitive Portability;
- Cognitive Transformation Composition.

These terms represent different conceptual classes, including objects, transformations, specifications, properties, models, graphs, frameworks, and capabilities.

The formal conceptual class and definition of each term **MUST** be established in an Architecture Reference, Cognitive Dictionary, or normative specification before a conformance claim depends on that term.

`Cognitive Contracts` is not recognized as a foundational normative term in this version.

The former term `Cognitive Composition` is replaced by `Cognitive Transformation Composition`.

### 8.1 Terminology Status

A capitalized architectural term denotes a formally recognized AISET concept or a concept intended for formal definition.

A lowercase use of the same word retains its ordinary-language meaning.

A term that has not yet received a formal definition **MUST** be treated as provisional for conformance purposes.

A provisional term **MUST NOT** be used as the sole basis for a conformance claim.

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

Each area has a distinct role.

Normative architecture, governance, metadata, and implementation-specific material **MUST** remain distinguishable.

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

Where two approved documents at the same level conflict, the conflict **MUST** be evaluated in the following order:

1. the document with the more specific scope;
2. the document with the later approved version;
3. the document explicitly designated as superseding the other.

Informative publications, examples, implementations, and repository documentation **MUST NOT** redefine normative program requirements.

### 9.2 Conflict Resolution

A conflict between approved AISET documents **MUST** be recorded.

The conflict **MAY** be resolved through:

- an interpretation record;
- a correction notice;
- an amendment;
- a new document version;
- a superseding publication;
- a registry status update.

Until resolution, the higher-level approved document **MUST** remain authoritative.

---

## 10. Publication Classes

AISET documents can include:

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

Each publication class **SHOULD** have defined review, approval, metadata, and release requirements before its first approved use.

A publication **MUST** identify its class.

---

## 11. Publication Lifecycle

AISET publications can pass through the following statuses:

1. Draft;
2. Review;
3. Candidate Publication;
4. Approved Publication;
5. Reference Publication;
6. Superseded;
7. Withdrawn.

A lifecycle transition **MUST** identify:

- the previous status;
- the new status;
- the applicable version;
- the decision authority;
- the effective date;
- supporting records.

A released publication **MUST NOT** be silently modified.

A material change **MUST** use a new version, amendment, correction record, or superseding publication.

The distinction between Approved Publication and Reference Publication **MUST** be defined before `PROGRAM-0001` reaches final approval.

---

## 12. Program Roles

### 12.1 Program Originator

The Program Originator establishes the foundational mission, identity, architectural intent, and initial direction of the AISET Program.

Program origination is a historical and provenance role.

Program origin attribution **MUST** remain preserved in the program record.

### 12.2 Author

An Author creates substantive content for an AISET publication, specification, governance document, schema, or other artifact.

Authorship applies to the identified contribution or publication.

Authorship **MUST NOT** automatically grant approval, publishing, registry, or maintenance authority.

### 12.3 Lead Editor

The Lead Editor maintains terminology, structure, editorial consistency, publication quality, and coherence across AISET documents.

Editorial authority **MUST NOT** by itself authorize final publication.

### 12.4 Reviewer

A Reviewer evaluates a contribution against its stated purpose, architectural principles, normative requirements, publication criteria, and assigned review scope.

A Reviewer **MUST** disclose material conflicts of interest.

Review participation **MUST NOT** automatically establish authorship or publication authority.

### 12.5 Publisher

The Publisher authorizes and records an official AISET release after applicable requirements have been satisfied.

The Publisher **MUST** preserve the approved text, metadata, release artifacts, review records, decision records, and publication history.

### 12.6 Registry Authority

A Registry Authority manages registered identifiers, status records, canonical references, version relationships, and machine-readable metadata within assigned authority.

Registry administration **MUST NOT** alter the meaning of an approved publication.

### 12.7 Maintainer

A Maintainer manages repository content, issue processing, pull request review, release operations, and technical continuity within assigned authority.

A Maintainer **MUST NOT** automatically be treated as holding authorship, approval, publishing, or registry authority.

### 12.8 Contributor

A Contributor submits material, analysis, review findings, specifications, schemas, implementations, tests, or other improvements to the AISET Program.

A contribution **MUST** comply with applicable contribution and licensing requirements.

### 12.9 Separation of Authorities

The AISET Program distinguishes:

- authorship authority;
- editorial authority;
- review authority;
- approval authority;
- publication authority;
- registry authority;
- repository maintenance authority.

One person **MAY** perform multiple roles during the initial foundation stage.

Each action **MUST** remain attributable to the applicable role.

As the program matures, a material normative publication **SHOULD** receive review or approval from a person or body other than the principal Author where practical.

No role **MAY** erase valid authorship, provenance, approval history, or program origin records.

---

## 13. Current Program Authority

During the initial foundation stage:

**Program Originator:** Arkadiy Lazarev

**Author and Lead Editor of PROGRAM-0001:** Arkadiy Lazarev

**Publisher:** AISET Program

**Repository Maintainer:** Arkadiy Lazarev

**Interim Registry Authority:** AISET Program, administered by Arkadiy Lazarev

The initial authority model exists to establish the program foundation.

Future governance documents **MAY**:

- delegate authority;
- create review bodies;
- establish working groups;
- create a registry authority;
- establish a publication council;
- define succession procedures.

A delegation **MUST** identify its scope, effective date, responsible authority, and revocation or succession conditions.

A delegation **MUST NOT** erase valid authorship, provenance, publication history, or the recorded origin of the AISET Program.

Delegation of operational authority **MUST NOT** transfer historical authorship or program origination.

---

## 14. Contributions

AISET can accept contributions involving:

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

A contribution **MUST** follow the repository contribution guidelines, licensing rules, and applicable review procedures.

A contribution **MUST NOT** automatically establish publication authority, authorship of the complete publication, or governance authority.

A contribution record **SHOULD** preserve attribution and provenance appropriate to its scope.

---

## 15. Review

AISET review can include:

- editorial review;
- architectural review;
- normative review;
- technical review;
- security review;
- privacy review;
- implementation review;
- governance review;
- publisher review.

A material review finding **MUST** be traceable, specific, and associated with the relevant document, version, or artifact.

### 15.1 Review Outcomes

A review **MUST** record one of the following outcomes:

- approved;
- approved with non-blocking recommendations;
- revision required;
- rejected;
- deferred pending additional evidence;
- referred to another review scope.

A blocking finding **MUST** identify the affected requirement, risk, inconsistency, or publication criterion.

### 15.2 Conflicts of Interest

A Reviewer or decision-maker **MUST** disclose a material conflict of interest when the person:

- has a direct financial interest in the outcome;
- represents an affected implementation vendor;
- reviews a disputed claim concerning their own work;
- cannot reasonably provide independent judgment.

A disclosed conflict does not necessarily require exclusion.

The conflict and its treatment **MUST** be recorded.

### 15.3 Disagreement and Lack of Consensus

Where reviewers disagree:

1. the disagreement **MUST** be documented;
2. the competing positions and supporting reasons **MUST** be recorded;
3. an attempt **SHOULD** be made to resolve the conflict through evidence, clarification, or revision;
4. unresolved disagreement **MUST** be referred to the applicable approval authority.

Consensus is preferred but is not required during the initial foundation stage.

A decision made without consensus **MUST** record:

- the decision-maker;
- the unresolved objections;
- the reason for proceeding;
- any conditions or future review requirements.

### 15.4 Appeals

A material review or approval decision **MAY** be reconsidered when:

- relevant evidence was unavailable;
- a procedural requirement was not followed;
- a conflict of interest was not disclosed;
- the decision conflicts with a higher-level AISET document;
- a significant technical or governance error is demonstrated.

An appeal **MUST NOT** automatically suspend an approved release.

The Publisher or applicable governance authority **MAY** suspend the release when the appeal identifies a material integrity, legal, security, or governance risk.

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

Each condition above **MUST** be satisfied unless an approved publication-class rule explicitly provides an alternative.

Repository commits alone **MUST NOT** establish an approved AISET publication.

### 16.1 Decision Record

A publication approval **MUST** identify:

- the publication identifier;
- the approved version;
- the approval date;
- the approving authority;
- completed reviews;
- unresolved non-blocking findings;
- publication conditions, if any.

### 16.2 Urgent Corrections

An urgent correction **MAY** be authorized when an approved artifact contains:

- a security risk;
- a material legal or licensing defect;
- a broken canonical reference;
- an integrity or checksum defect;
- a critical publication metadata error;
- a defect likely to cause harmful implementation behavior.

An urgent correction **MUST NOT** silently replace the released artifact.

It **MUST** use an explicit correction notice, new artifact, new version, or superseding release.

### 16.3 Withdrawal and Suspension

A publication **MAY** be suspended or withdrawn when:

- its integrity cannot be verified;
- it contains a material legal or licensing defect;
- it creates a substantial security or safety risk;
- its approval record is invalid;
- it materially misrepresents authorship or provenance;
- it has been superseded and continued use creates significant risk.

A withdrawal **MUST** preserve the historical record.

A withdrawal record **MUST** state the reason, authority, date, and replacement publication where applicable.

---

## 17. Versioning and Immutability

Every released AISET publication **MUST** have an explicit version.

Published versions, Git tags, release manifests, checksums, and release artifacts **MUST** be treated as immutable records.

AISET publications **SHOULD** use semantic versioning principles in the form:

```text
MAJOR.MINOR.PATCH
```

### 17.1 Major Version

A major version change **MUST** be used when a change:

- alters the mission or fundamental scope of the program;
- changes a foundational architectural principle;
- changes the document hierarchy;
- materially changes approval or governance authority;
- removes or reverses a normative guarantee;
- creates broad incompatibility with the previous version.

### 17.2 Minor Version

A minor version change **SHOULD** be used when a change:

- adds a new compatible program rule;
- adds a role, process, publication class, or governance mechanism;
- materially clarifies an existing requirement without reversing it;
- expands scope consistently with the current major version;
- introduces a compatible amendment.

### 17.3 Patch Version

A patch version change **SHOULD** be used when a change:

- corrects grammar, formatting, links, citations, or metadata;
- resolves an unambiguous editorial defect;
- clarifies wording without changing normative meaning;
- corrects a non-substantive publication error.

A patch version **MUST NOT** conceal a normative change.

### 17.4 Pre-release Versions

Draft, Review, and Candidate Publication versions **MAY** use pre-release identifiers such as:

```text
0.4-draft
1.0-rc.1
```

A pre-release version **MUST NOT** be represented as an approved Reference Publication unless an approved governance rule explicitly permits that designation.

### 17.5 Immutable Releases

A released artifact **MUST NOT** be silently edited, overwritten, or replaced.

A correction or substantive change **MUST** use:

- a new version;
- a correction notice;
- an amendment;
- or a superseding publication.

Historical versions **MUST** remain discoverable.

### 17.6 Version Classification

Where the appropriate version level is disputed, the change **MUST** be classified according to its normative effect rather than its textual size.

A small textual change **MAY** require a major or minor version when it changes normative meaning.

---

## 18. Registries and Identifiers

AISET identifiers **MUST** be:

- unique;
- stable;
- version-aware;
- traceable to canonical artifacts;
- suitable for human and machine use.

A registry record **SHOULD** preserve:

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

A registry record **MUST NOT** alter the meaning of the registered object.

A material registry status change **MUST** be traceable to an authorized decision or lifecycle record.

---

## 19. Normative and Informative Material

A clause using **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, or **MAY** is normative.

A clause without an uppercase normative keyword is informative unless another approved rule explicitly assigns normative status.

Normative material defines requirements, prohibitions, recommendations, permissions, constraints, interfaces, invariants, validation rules, or conformance conditions.

Informative material provides explanation, examples, context, history, guidance, or interpretation.

A publication **SHOULD** identify sections or clauses as Normative, Informative, Provisional, or Historical where the distinction is not obvious.

Normative keywords **MUST** be used deliberately and consistently.

---

## 20. Conformance

A system or implementation **MAY** claim conformance only to an identified AISET specification and version.

A conformance claim **MUST** state:

- the applicable specification;
- the implemented scope;
- the implementation profile;
- validation evidence;
- known limitations;
- deviations;
- test results where applicable.

A conformance claim **MUST NOT** imply security, correctness, suitability, portability, compatibility, or interoperability beyond its stated and validated scope.

A conformance claim based on a provisional term **MUST NOT** be accepted unless an applicable specification supplies a formal definition.

---

## 21. Licensing

Unless explicitly stated otherwise, AISET publications, specifications, governance documents, registry records, schemas, and other non-software materials are licensed under the Creative Commons Attribution 4.0 International License.

Software components are licensed separately.

Each software component **MUST** identify its applicable software license before public release.

A publication **MUST** identify its applicable license.

A contribution **MUST** comply with the licensing requirements applicable to the target artifact.

---

## 22. Intellectual Responsibility

Authors, editors, reviewers, publishers, maintainers, and contributors remain responsible for the material they submit, approve, or publish within their assigned roles.

Use of software tools or artificial intelligence systems **MUST NOT** remove human responsibility for:

- accuracy;
- provenance;
- licensing;
- review;
- security;
- publication decisions;
- normative meaning.

A publication decision **MUST** identify the accountable human or authorized governance body.

---

## 23. Security and Privacy

AISET publications and specifications **SHOULD** identify relevant:

- trust boundaries;
- threat assumptions;
- provenance requirements;
- integrity requirements;
- confidentiality considerations;
- privacy implications;
- failure modes;
- abuse cases;
- implementation risks.

A normative specification **MUST** identify security or privacy assumptions that materially affect conformance.

AISET conformance **MUST NOT** be presented as an unconditional guarantee of security or privacy.

---

## 24. Amendments

This Charter **MAY** be amended through a documented program process.

An amendment **MUST** identify:

- the affected version;
- the proposed change;
- the reason for the change;
- architectural and governance impact;
- review findings;
- approval authority;
- effective date.

A material amendment **MUST** create a new Charter version.

A released Charter version **MUST** remain historically accessible.

An amendment **MUST NOT** silently alter a previously released Charter version.

---

## 25. Continuity and Succession

The AISET Program **SHOULD** preserve continuity of:

- publications;
- identifiers;
- registries;
- authorship;
- provenance;
- release history;
- licenses;
- governance records;
- canonical artifacts.

A succession procedure **MUST** preserve valid authorship, provenance, program origin, publication history, and licensing records.

A succession procedure **MUST NOT** authorize silent alteration, appropriation, or misrepresentation of the program’s historical record.

Critical canonical artifacts **SHOULD** have documented continuity and recovery arrangements.

---

## 26. Program Evolution

The AISET Program can evolve through:

- new publications;
- new normative specifications;
- amended governance;
- new registry classes;
- new schemas;
- independent implementations;
- broader review participation;
- delegated roles;
- formal councils or working groups.

Program evolution **MUST** remain consistent with the foundational mission and approved principles recorded in this Charter.

A material change inconsistent with the current mission or principles **MUST** use a major Charter revision.

---

## 27. Relationship to DISCOVERY-0001

`DISCOVERY-0001 — AISET Discovery` records why AISET emerged and how the foundational architecture developed from an engineering necessity.

This Charter establishes the program framework through which that architectural direction is governed, specified, published, implemented, and evolved.

`DISCOVERY-0001` is historical and informative.

It **MUST NOT** override an approved normative Charter clause.

---

## 28. Current Status

The AISET Program is in its initial foundation stage.

This document is a targeted Draft revision of the proposed AISET Program Charter.

The transition from `PROGRAM-0001 v0.3 Review` to `PROGRAM-0001 v0.4 Draft` is based on:

`PROGRAM-0001-REVIEW-002 — Normative Terminology Review`

That review identified five findings blocking direct progression to Candidate Publication:

1. inconsistent uppercase and lowercase mandatory language;
2. incomplete classification of obligation, recommendation, and permission language;
3. ambiguity of `Cognitive Contracts`;
4. insufficient classification of `Cognitive Composition`;
5. lack of a precise clause-level normative rule.

This version addresses those findings by:

- defining one normative keyword policy;
- assigning normative force only to uppercase keywords;
- converting intended obligations to **MUST** or **MUST NOT**;
- converting intended recommendations to **SHOULD** or **SHOULD NOT**;
- converting normative permissions to **MAY**;
- replacing factual possibility with non-normative language;
- removing `Cognitive Contracts` from the foundational list;
- replacing `Cognitive Composition` with `Cognitive Transformation Composition`;
- adding canonical terminology and capitalization rules.

This Draft is not yet an approved publication, governing Charter, Candidate Publication, or AISET Reference Publication.

The next intended action is normative terminology re-review.

Progression beyond Draft **MUST** be supported by review, registry, and Publisher records appropriate to the next lifecycle state.

---

## 29. Canonical Repository

The canonical public repository is:

`https://github.com/setem4405-collab/aiset`

The canonical website is:

`https://aisetcfs.com`

An official lifecycle or publication record **MUST** identify the canonical repository path of the applicable artifact.

---

## 30. Attribution

**Author:** Arkadiy Lazarev

**Program Originator:** Arkadiy Lazarev

**Lead Editor:** Arkadiy Lazarev

**Publisher:** AISET Program

Authorship, editorial responsibility, program origination, and publication authority **MUST** remain distinguishable in program records.

---

## 31. License

Copyright © 2026 AISET Program.

This document is licensed under the Creative Commons Attribution 4.0 International License.

See:

- `LICENSE`
- `LICENSES/CC-BY-4.0.txt`