# PROGRAM-0001 — AISET Program Charter

**Identifier:** PROGRAM-0001

**Title:** AISET Program Charter

**Version:** 1.0 Review

**Status:** Review

**Date:** 16 July 2026

**Author:** Arkadiy Lazarev

**Program Originator:** Arkadiy Lazarev

**Lead Editor:** Arkadiy Lazarev

**Publisher:** AISET Program

**Previous Version:** PROGRAM-0001 v0.9 Draft

**Revision Basis:** PROGRAM-0001-REVIEW-008

**License:** Creative Commons Attribution 4.0 International

---

## Document Status

This document is the formal Review version of the AISET Program Charter following completion of the targeted security, privacy, governance, and editorial revision based on:

`PROGRAM-0001-REVIEW-007 — Security and Privacy Review`

The return from `PROGRAM-0001 v0.9 Draft` to `PROGRAM-0001 v1.0 Review` is supported by:

`PROGRAM-0001-REVIEW-008 — Security, Privacy, Governance, and Editorial Re-review`

That re-review determined that:

- both previous blocking findings were resolved;
- no new blocking finding was identified;
- the security and privacy findings were resolved at Charter level;
- `NEW-001` and `NEW-002` were resolved;
- return to formal Review is permitted;
- direct progression to Candidate Publication is not yet permitted.

This Review version preserves:

- the Technology Independence clause;
- the normative keyword policy;
- governance-record classification;
- least-privilege access controls;
- personal-data protections;
- restricted-record handling;
- incident and recovery governance;
- mandatory Candidate Publication checksums;
- registry integrity binding;
- governance-capture safeguards;
- security-sensitive change review;
- non-circular foundation-stage exception authority;
- lifecycle classification alignment.

The following non-blocking matters remain:

- `ED-002 — Normative and Informative Boundaries`;
- `ED-003 — Cross-Reference Precision`;
- `NEW-003 — Operational Record Specifications`;
- `NEW-004 — Checksum Algorithm Policy`;
- `NEW-005 — Independent Review Availability`.

This document has not been approved as:

- the governing Charter of the AISET Program;
- a Candidate Publication;
- an Approved Publication;
- an AISET Reference Publication.

The purpose of this Review version is to enable:

- preparation of operational record specifications or templates;
- definition of checksum algorithm policy;
- independent or second-party review;
- final disposition of remaining non-blocking findings;
- Candidate Publication readiness preparation.

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

Where a section combines normative and informative material, the document **SHOULD** identify the normative rule, rationale, example, or historical note explicitly.

While this document remains in Review status, its provisions remain reviewable and non-binding.
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

Program Originator status **MUST NOT** automatically grant permanent approval, publication, registry, maintenance, or governance authority.

### 12.2 Author

An Author creates substantive content for an AISET publication, specification, governance document, schema, or other artifact.

Authorship applies to the identified contribution or publication.

Authorship **MUST NOT** automatically grant approval, publishing, registry, or maintenance authority.

An Author **MUST** disclose when participating in the review or approval of their own normative change.

### 12.3 Lead Editor

The Lead Editor maintains terminology, structure, editorial consistency, publication quality, and coherence across AISET documents.

Editorial authority **MUST NOT** by itself authorize final publication.

The Lead Editor **MAY** prepare publication-ready text but **MUST NOT** represent editorial preparation as approval.

### 12.4 Reviewer

A Reviewer evaluates a contribution against its stated purpose, architectural principles, normative requirements, publication criteria, and assigned review scope.

A Reviewer **MUST** disclose material conflicts of interest.

Review participation **MUST NOT** automatically establish authorship or publication authority.

A Reviewer **MUST** identify whether the review is internal, independent, external, implementation-specific, security-sensitive, or limited to a defined scope.

### 12.5 Approval Authority

An Approval Authority determines whether an identified publication or lifecycle transition satisfies the applicable approval conditions.

Approval authority **MUST** be explicitly assigned.

Approval authority **MUST NOT** be inferred solely from authorship, editorial control, repository access, registry administration, Publisher representation, or Program Originator status.

### 12.6 Publisher

The Publisher authorizes and records an official AISET release after applicable requirements have been satisfied.

The Publisher **MUST** preserve the approved text, metadata, release artifacts, review records, decision records, and publication history.

Publisher acknowledgment records lifecycle recognition but **MUST NOT** be represented as independent review.

### 12.7 Registry Authority

A Registry Authority manages registered identifiers, status records, canonical references, version relationships, and machine-readable metadata within assigned authority.

Registry administration **MUST NOT** alter the meaning of an approved publication.

Registry administration **MUST NOT** independently grant approval status unless an approved governance rule explicitly assigns that authority.

### 12.8 Maintainer

A Maintainer manages repository content, issue processing, pull request review, release operations, and technical continuity within assigned authority.

A Maintainer **MUST NOT** automatically be treated as holding authorship, approval, publishing, or registry authority.

Repository control **MUST NOT** by itself establish governance authority.

### 12.9 Contributor

A Contributor submits material, analysis, review findings, specifications, schemas, implementations, tests, or other improvements to the AISET Program.

A contribution **MUST** comply with applicable contribution and licensing requirements.

Contribution status **MUST NOT** automatically establish approval or governance authority.

### 12.10 Separation of Authorities

The AISET Program distinguishes authorship, editorial, review, approval, publication, registry, and repository maintenance authority.

Each material lifecycle action **MUST** identify the role under which the action was performed.

One person **MAY** perform multiple roles during the initial foundation stage only when the overlap is explicitly disclosed, each action remains separately attributable, the applicable record identifies the role used, no record misrepresents the action as independent, and any required second-party confirmation is obtained.

### 12.11 Self-approval Restrictions

An Author **MUST NOT** independently grant final approval to their own normative change.

A person acting as principal Author **MAY** prepare, explain, internally review, and record a proposed disposition for the change, and may act as Publisher representative during the foundation stage.

Candidate Publication of a material normative revision **MUST** receive documented confirmation from at least one Reviewer who is not the sole Author of that revision.

Final approval of a material normative publication **MUST** include either confirmation by an Approval Authority distinct from the sole Author, approval by an authorized governance body, or a documented foundation-stage exception approved under a higher-level governance rule.

A foundation-stage exception **MUST** disclose the overlapping roles, why separation was not practicable, the resulting risks, compensating review measures, the authority granting the exception, and its period of application.

### 12.12 Delegation

A delegation of authority **MUST** identify the delegating authority, receiving person or body, delegated role, scope, effective date, duration if limited, constraints, revocation conditions, succession conditions, and canonical decision record.

Delegation **MUST NOT** erase historical authorship, provenance, publication history, or program origination.

Delegated authority **MUST NOT** exceed the authority held by the delegating role.
---

## 13. Current Program Authority

During the initial foundation stage:

**Program Originator:** Arkadiy Lazarev

**Author and Lead Editor of PROGRAM-0001:** Arkadiy Lazarev

**Publisher:** AISET Program

**Publisher Representative:** Arkadiy Lazarev

**Repository Maintainer:** Arkadiy Lazarev

**Interim Registry Authority:** AISET Program, administered by Arkadiy Lazarev

The initial authority model exists to establish the program foundation.

The present overlap of roles is disclosed and is not represented as independent governance.

### 13.1 Foundation-stage Authority Conditions

During the foundation stage, overlapping roles **MAY** perform Draft, internal review, registry, and Publisher acknowledgment actions when each action is separately recorded.

Authorship and review, review and approval, approval and Publisher acknowledgment, approval and registry administration, and registry administration and repository maintenance **MUST NOT** be represented as independent when performed by the same person.

A foundation-stage record **MUST** identify relevant role overlap.

### 13.2 Transition Beyond Foundation-stage Governance

Before the first final approval of `PROGRAM-0001`, the Program **MUST** establish or designate an Approval Authority, an appeal or reconsideration authority, a conflict-of-interest decision process, a registry administration process, a Publisher authorization process, and continuity and succession arrangements.

Candidate Publication **MUST** include at least one reviewer who is not the sole Author of the reviewed normative revision.

### 13.3 Authority Delegation

Future governance documents **MAY** delegate authority, create review bodies, establish working groups, create a registry authority, establish a publication council, define succession procedures, establish independent review panels, or create temporary emergency authorities.

A delegation **MUST** comply with Section 12.12.

Delegation of operational authority **MUST NOT** transfer historical authorship or program origination.

### 13.4 Revocation and Expiration

Delegated authority **MAY** be revoked or allowed to expire.

A revocation or expiration record **MUST** identify the affected delegation, effective date, responsible authority, reason, successor authority if applicable, and pending actions affected by the change.

An expired or revoked authority **MUST NOT** continue to approve new actions.
---

## 14. Contributions

AISET can accept contributions involving editorial improvements, architectural proposals, normative specifications, terminology, schemas, registry records, governance proposals, implementations, conformance tests, and technical or publication reviews.

A contribution **MUST** follow the repository contribution guidelines, licensing rules, and applicable review procedures.

A contribution **MUST NOT** automatically establish publication authority, authorship of the complete publication, or governance authority.

A contribution record **SHOULD** preserve attribution and provenance appropriate to its scope.

### 14.1 Material Proposals

A material proposal **MUST** receive a persistent identifier or other traceable record.

A material proposal record **MUST** identify the proposer, scope, affected publication or program area, submission date, requested action, applicable licensing, and current disposition.

### 14.2 Proposal Disposition

A material proposal **MUST** receive one of the following dispositions: accepted, accepted with revision, rejected, deferred, superseded, withdrawn, or referred to another process.

A rejection **MUST** include a stated reason.

A deferral **MUST** identify the missing evidence, dependency, or future condition where practical.

A disposition **MUST NOT** erase the contribution record.

### 14.3 Contributor Attribution

Material contributions **MUST** preserve appropriate authorship, co-authorship, review, or contributor attribution.

Contribution to one section or artifact **MUST NOT** automatically establish authorship of the complete publication.

Attribution **MUST NOT** be removed solely because a proposal was rejected or superseded.

### 14.4 Resubmission and Reconsideration

A rejected or deferred proposal **MAY** be resubmitted when new evidence is available, the proposal has been materially revised, a dependency has been resolved, or a procedural error affected the prior disposition.

Resubmission **MUST** reference the previous proposal or disposition record.

### 14.5 Participation Restrictions

Participation **MAY** be restricted to protect security, privacy, legal compliance, repository integrity, participants from abuse or harassment, or the integrity of review and publication processes.

A material participation restriction **MUST** identify the restricted action, reason, responsible authority, effective period, and available reconsideration or appeal options.

A participation restriction **MUST NOT** be used to erase valid contribution history or unresolved objections.

### 14.6 Public and Restricted Records

Governance, review, proposal, and disposition records **SHOULD** remain publicly discoverable.

A record **MAY** be temporarily restricted when publication would create a material security, privacy, legal, or safety risk.

A restriction **MUST** be documented and reviewed when the underlying risk changes.
---

## 15. Review

AISET review can include editorial, architectural, normative, technical, security, privacy, implementation, governance, Publisher, independent, or external review.

A material review finding **MUST** be traceable, specific, and associated with the relevant document, version, or artifact.

### 15.1 Review Outcomes

A review **MUST** record one of the following outcomes: approved; approved with non-blocking recommendations; revision required; rejected; deferred pending additional evidence; or referred to another review scope.

A blocking finding **MUST** identify the affected requirement, risk, inconsistency, or publication criterion.

### 15.2 Review Classification

A review record **MUST** identify whether it is internal, independent, external, implementation-specific, security-sensitive, or limited in scope.

An internal review **MUST NOT** be represented as independent review.

A limited-scope review **MUST NOT** be represented as validating matters outside its stated scope.

### 15.3 Conflicts of Interest

A Reviewer or decision-maker **MUST** disclose a material conflict of interest when the person has a direct financial interest, represents an affected vendor, reviews a disputed claim concerning their own work, is the sole Author of the reviewed normative revision, has an affected organizational obligation, has a relationship that could reasonably affect judgment, administers the registry or repository involved in the disputed action, or cannot reasonably provide independent judgment.

A disclosed conflict **MUST** receive a recorded treatment: no restriction with rationale, advisory participation only, exclusion from the decision, mandatory recusal, independent confirmation, or a documented foundation-stage exception.

A person with a direct material conflict **MUST NOT** be the sole decision-maker on the affected matter.

### 15.4 Disagreement and Lack of Consensus

Where reviewers disagree, the disagreement, competing positions, and supporting reasons **MUST** be documented; an attempt **SHOULD** be made to resolve the matter through evidence, clarification, or revision; and unresolved disagreement **MUST** be referred to the applicable Approval Authority.

A decision made without consensus **MUST** record the decision-maker, unresolved objections, reason for proceeding, and any conditions or future review requirements.

### 15.5 Reconsideration and Appeals

A material review, approval, registry, or publication decision **MAY** be reconsidered when relevant evidence was unavailable, a procedural requirement was not followed, a conflict was not disclosed, the decision conflicts with a higher-level document, a significant technical or governance error is demonstrated, the decision record is materially incomplete, or the responsible authority exceeded its scope.

An appeal record **MUST** identify the appeal identifier, challenged decision, requesting party, reason, evidence, reviewing authority, disclosed conflicts, temporary status, final disposition, rationale, effective date, and canonical record location.

An appeal **MUST NOT** automatically suspend an approved release.

The Publisher or applicable governance authority **MAY** suspend the release when the appeal identifies a material integrity, legal, security, privacy, safety, or governance risk.

A person who was the sole decision-maker for the challenged action **MUST NOT** be the sole authority deciding the appeal.

### 15.6 Appeal Outcomes

An appeal **MUST** result in one of the following outcomes: original decision affirmed, modified, reversed, suspended, returned for new review, rejected as out of scope, or deferred pending evidence.

The appeal outcome **MUST** preserve the original decision record.

### 15.7 Review Time and Inactivity

A review or appeal process **SHOULD** identify an expected response period.

An inactive record **MAY** be closed, deferred, or archived only through a documented disposition.

Inactivity **MUST NOT** be represented as approval.
---

## 16. Approval and Publication Authority

An AISET publication becomes official only when its identifier, version, and status are explicit; required review is complete; blocking findings are resolved; major findings are resolved or dispositioned; authorship, editorial, and licensing records are present; release artifacts are prepared; the applicable Approval Authority authorizes progression; the Publisher authorizes release; and a permanent release record is created.

Each condition above **MUST** be satisfied unless an approved publication-class rule explicitly provides an alternative.

Repository commits alone **MUST NOT** establish an approved AISET publication.

### 16.1 Candidate Publication Readiness

Progression to Candidate Publication **MUST** be supported by a Candidate Publication readiness record.

The readiness record **MUST** identify the document identifier, proposed Candidate version, canonical file, normative change summary, completed reviews, resolved blocking findings, disposition of major findings, unresolved non-blocking findings, editorial review status, governance review status, security and privacy review status, terminology consistency status, known dependencies and limitations, role and conflict disclosures, independent or public review status, registry readiness, Publisher readiness, artifact integrity information, and responsible decision authority.

### 16.2 Candidate Publication Blocking Conditions

Progression to Candidate Publication **MUST NOT** occur when a blocking finding remains unresolved; the canonical document is ambiguous or unavailable; version or status is inconsistent; required review records are missing; the sole Author is also the sole approving Reviewer for a material normative revision; a material conflict remains undisposed; licensing information is absent; registry or Publisher readiness is not established; artifact integrity cannot be reasonably verified; or the readiness decision record is incomplete.

### 16.3 Candidate Publication Review Requirement

A material normative revision entering Candidate Publication **MUST** receive documented review from at least one person who is not the sole Author of that revision.

The review **MAY** be internal, independent, or external, but its classification **MUST** be explicit.

Candidate Publication status **MUST NOT** be represented as final approval.

### 16.4 Decision Record

A publication or lifecycle approval **MUST** identify the publication identifier, approved version, lifecycle transition, approval date, approving authority, completed reviews, unresolved non-blocking findings, conflict disclosures, publication conditions, and canonical decision record.

### 16.5 Publisher Authorization

The Publisher **MUST** verify that applicable approval and readiness records exist before authorizing an official release.

Publisher authorization **MUST NOT** silently replace the Approval Authority decision.

Publisher acknowledgment **MUST** identify the lifecycle transition being acknowledged.

### 16.6 Emergency Actions

An emergency action **MAY** be authorized when delay would create a material risk involving security compromise, unauthorized publication, repository takeover, credential compromise, malicious registry modification, incorrect publication status, legal or licensing exposure, safety risk, loss of canonical infrastructure, or compromised Publisher or registry authority.

An emergency action **MAY** suspend publication status, restrict repository changes, revoke or rotate credentials, mark a registry record as disputed, temporarily restrict access, publish a warning or correction notice, or preserve affected artifacts for investigation.

An emergency action record **MUST** identify the emergency, authorizing role, action taken, affected artifacts, evidence, effective time, expected duration, and review or restoration conditions.

Emergency authority **MUST NOT** silently become permanent authority.

An emergency action **MUST** receive retrospective review when the immediate risk has been controlled.

### 16.7 Urgent Corrections

An urgent correction **MAY** be authorized when an approved artifact contains a security risk, material legal or licensing defect, broken canonical reference, integrity or checksum defect, critical publication metadata error, or defect likely to cause harmful implementation behavior.

An urgent correction **MUST NOT** silently replace the released artifact.

It **MUST** use an explicit correction notice, new artifact, new version, or superseding release.

### 16.8 Withdrawal and Suspension

A publication **MAY** be suspended or withdrawn when its integrity cannot be verified; it contains a material legal or licensing defect; it creates a substantial security or safety risk; its approval record is invalid; it materially misrepresents authorship or provenance; continued use after supersession creates significant risk; canonical infrastructure is compromised; or registry status is materially disputed.

A withdrawal or suspension **MUST** preserve the historical record.

A withdrawal or suspension record **MUST** state the reason, authority, effective date, affected version, temporary or permanent status, replacement publication where applicable, and restoration conditions where applicable.
---

## 17. Versioning and Immutability

Every released AISET publication **MUST** have an explicit version.

Published versions, Git tags, release manifests, checksums, and release artifacts **MUST** be treated as immutable records.

AISET publications **SHOULD** use semantic versioning principles in the form:

```text
MAJOR.MINOR.PATCH
```

### 17.1 Major Version

A major version change **MUST** be used when a change alters the mission or fundamental scope, changes a foundational architectural principle or document hierarchy, materially changes approval or governance authority, removes or reverses a normative guarantee, or creates broad incompatibility with the previous version.

### 17.2 Minor Version

A minor version change **SHOULD** be used when a change adds a compatible rule, role, process, publication class, or governance mechanism; materially clarifies a requirement without reversing it; expands scope consistently with the current major version; or introduces a compatible amendment.

### 17.3 Patch Version

A patch version change **SHOULD** be used when a change corrects grammar, formatting, links, citations, or metadata; resolves an unambiguous editorial defect; clarifies wording without changing normative meaning; or corrects a non-substantive publication error.

A patch version **MUST NOT** conceal a normative change.

### 17.4 Pre-release Versions

Draft, Review, and Candidate Publication versions **MAY** use pre-release identifiers such as:

```text
0.8-review
1.0-rc.1
```

A pre-release version **MUST NOT** be represented as an Approved Publication or Reference Publication unless an approved governance rule explicitly permits that designation.

### 17.5 Immutable Releases

A released artifact **MUST NOT** be silently edited, overwritten, or replaced.

A correction or substantive change **MUST** use a new version, correction notice, amendment, or superseding publication.

Historical versions **MUST** remain discoverable.

### 17.6 Version Classification

Where the appropriate version level is disputed, the change **MUST** be classified according to its normative effect rather than its textual size.

A small textual change **MAY** require a major or minor version when it changes normative meaning.

### 17.7 Canonical Lifecycle Terminology

The canonical lifecycle states are Draft, Review, Candidate Publication, and Approved Publication.

Reference Publication is a publication designation and **MUST NOT** be treated as automatically equivalent to Approved Publication unless an approved governance rule defines that relationship.

Document lifecycle status and registry-record status **MUST** remain distinguishable.

Registry-record statuses may include active, historical, superseded, corrected, suspended, withdrawn, and invalidated.

Approval, acknowledgment, registration, publication, supersession, suspension, and withdrawal are distinct actions and **MUST NOT** be represented as interchangeable.
---

## 18. Registries and Identifiers

AISET identifiers **MUST** be unique, stable, version-aware, traceable to canonical artifacts, and suitable for human and machine use.

A registry record **SHOULD** preserve identifier, title, object type, version, lifecycle status, registry-record status, canonical path, release information, authorship, Publisher, license, checksum where applicable, relationships to other objects, and the authorizing lifecycle or decision record.

A registry record **MUST NOT** alter the meaning of the registered object.

A material registry status change **MUST** be traceable to an authorized decision or lifecycle record.

### 18.1 Registry Record Statuses

A registry record **MUST** use an explicit status.

Supported statuses include Active, Historical, Superseded, Corrected, Suspended, Withdrawn, and Invalidated.

### 18.2 Status Transitions

A registry status transition **MUST** identify the affected record, previous status, new status, effective date, authorizing decision, reason, and successor or replacement record where applicable.

A superseded record **MUST** remain discoverable.

Supersession **MUST NOT** erase the validity of the historical state recorded at the time of publication.

### 18.3 Registry Corrections

A material registry error **MUST NOT** be silently edited after publication.

The error **MUST** be addressed through a correction record, superseding registry record, amendment, or invalidation and replacement.

A correction record **MUST** identify the affected text, corrected information, and reason.

### 18.4 Conflicting Registry Claims

When two registry records appear to claim active status for the same object and lifecycle state, the conflict **MUST** be resolved by examining the applicable higher-level governance rule, authorizing decision record, effective date, supersession relationship, Publisher acknowledgment, and repository or release provenance.

The conflict **MUST** be recorded.

Until resolved, the affected status **MAY** be marked disputed or suspended.

### 18.5 Canonical Location Changes

A canonical location change **MUST** preserve the previous location, new location, effective date, redirect or discovery information where practicable, and authorizing record.

A canonical location change **MUST NOT** silently replace the registered object.

### 18.6 Integrity Failure

When a checksum, signature, artifact identity, or canonical file does not match the registry record, the inconsistency **MUST** be recorded, affected publication claims **MAY** be suspended, the responsible authority **MUST** investigate, and restoration or replacement **MUST** be documented.

### 18.7 Registry Precedence

The normative meaning of a registered object is determined by the canonical publication, not by descriptive registry metadata.

A registry record determines registered identity and status within its assigned authority.

When registry metadata conflicts with the canonical publication text, the publication text governs meaning and the registry inconsistency **MUST** be corrected.

When registry status conflicts with an authorized lifecycle decision, the applicable higher-level governance and decision record govern the status, and the registry **MUST** be updated.
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

## 28. Governance Record Security and Privacy

### 28.1 Record Classification

Each governance record **MUST** be assigned one of these classifications:

- **Public**;
- **Internal**;
- **Restricted**;
- **Confidential Security**;
- **Personal Data Restricted**.

A classification decision **MUST** identify the record, classification, responsible authority, basis, effective date, and review or declassification condition.

A record **MUST NOT** be classified solely to conceal misconduct, suppress legitimate criticism, avoid accountability, or misrepresent a governance decision.

### 28.2 Access Control

Access to non-public governance records **MUST** follow least-privilege and need-to-know principles.

Access authority **MUST** be traceable to a role, delegated responsibility, specific review, incident-response function, or documented legal, safety, privacy, or security requirement.

Access to Restricted, Confidential Security, or Personal Data Restricted records **MUST NOT** be inferred solely from repository access, authorship, Publisher status, registry administration, or Program Originator status.

Material access grants, revocations, and exceptional disclosures **MUST** be recorded.

### 28.3 Declassification and Disclosure

A non-public record **SHOULD** include a review date or disclosure condition.

Declassification or expanded disclosure **MUST** be authorized and recorded.

A public metadata record **SHOULD** normally exist for a withheld material governance record and identify its existence, identifier, general category, withholding basis, responsible authority, and review date or disclosure condition.

The metadata record **MUST NOT** disclose protected content.

### 28.4 Personal Data Principles

The Program **MUST** apply purpose limitation, data minimization, accuracy, access limitation, retention limitation, correction, confidentiality, accountability, and transparency with justified exceptions.

Personal data **MUST NOT** be collected or published unless necessary for a documented governance purpose.

Sensitive personal information **SHOULD** be summarized, redacted, pseudonymized, or stored separately where full disclosure is unnecessary.

### 28.5 Public and Restricted Record Separation

Where a matter contains sensitive evidence, the Program **SHOULD** maintain a public decision summary and a separate restricted evidence record.

A public decision summary **SHOULD** preserve the decision identity, authority, outcome, rationale summary, conflict treatment, and effective date.

### 28.6 Retention, Correction, Redaction, and Deletion

The Program **MUST** distinguish between immutable governance conclusions, correctable factual or personal data, removable credentials or secrets, restricted source evidence, historical metadata, and unlawfully or mistakenly published information.

A correction, redaction, or deletion action **MUST** preserve a traceable record of the affected record, action, authority, reason, date, and replacement or sanitized record where applicable.

Credentials, secrets, exploit details, or unlawfully disclosed personal data **MAY** be removed immediately where necessary to prevent harm.

Emergency removal **MUST** be followed by retrospective review.

### 28.7 Confidential Appeals and Conflict Records

Appeal and conflict processes **MUST** support privacy-preserving separation between public outcome, restricted evidence, protected identity, and full confidential disclosure.

A person with access to confidential appeal or conflict information **MUST NOT** disclose it outside the authorized process without recorded authority.

### 28.8 Security Reporter Protection

The Program **SHOULD** provide a confidential channel for good-faith security reports.

A good-faith reporter **MUST NOT** be subjected to retaliation solely for making a report.

Reporter identity **SHOULD** be limited to persons who require it for investigation, response, or legal obligation.

Knowingly false, malicious, coercive, or abusive reports **MAY** be treated as governance misconduct through a documented process.

---

## 29. Security Incident and Recovery Governance

### 29.1 Incident Identification

A material security or privacy incident **MUST** receive a persistent incident identifier.

An incident record **MUST** identify discovery date, severity, affected records or systems, responsible authority, containment actions, evidence handling, recovery status, notification decision, retrospective review, closure decision, and follow-up actions.

### 29.2 Severity and Containment

The Program **MUST** classify incident severity using a documented method.

Containment actions **MAY** include credential revocation, authority suspension, repository restriction, registry suspension, Publisher suspension, canonical-location freeze, temporary publication withdrawal, access revocation, and evidence preservation.

Containment **MUST** be necessary and proportionate.

### 29.3 Credential and Authority Compromise

Where a credential or authority is suspected to be compromised:

- the affected authority **MUST** be suspended or restricted promptly;
- compromised credentials **MUST** be revoked or replaced;
- actions during the compromise window **MUST** be reviewed;
- material authority restoration **MUST** receive independent or second-party confirmation;
- affected records **MUST** be corrected where necessary.

A compromised person or role **MUST NOT** be the sole authority confirming its own recovery.

### 29.4 Incident Notification

Each material incident **MUST** include a documented notification decision considering severity, affected persons, further-harm risk, public-record integrity, investigation needs, legal or contractual obligations, and public-interest implications.

Notification **MAY** be delayed where immediate disclosure would materially increase harm, but the delay and basis **MUST** be recorded.

### 29.5 Continuity and Recovery

The Program **MUST** maintain at least one independent backup of canonical governance and registry records.

Continuity arrangements **MUST** identify recovery ownership, backup class or location, restoration procedure, alternate canonical-location procedure, registry-history preservation, integrity-evidence recovery, and post-recovery verification.

Restoration procedures **SHOULD** be tested periodically.

A major recovery action **MUST** produce a continuity or recovery record.

### 29.6 Third-party Dependencies

A material third-party service used for repository hosting, identity, communications, registry publication, website hosting, backups, signing, or issue tracking **MUST** have a documented dependency record identifying purpose, data handled, authority granted, canonicality implications, backup availability, compromise response, and exit or migration path.

A third-party service **MUST NOT** be the sole source of truth where its loss would prevent reconstruction of canonical status.

---

## 30. Candidate Publication Integrity

### 30.1 Mandatory Checksum

A Candidate Publication artifact **MUST** have a cryptographic checksum recorded before Candidate Publication status is granted.

The integrity record **MUST** identify the document identifier, version, lifecycle status, canonical file path, hash algorithm, checksum value, calculation date, responsible authority, and related registry record.

### 30.2 Registry Binding

The Candidate Publication registry record **MUST** bind the document identifier, version, lifecycle status, canonical location, checksum, hash algorithm, Publisher acknowledgment, and approval or readiness decision.

A registry record **MUST NOT** identify an artifact as canonical where its checksum does not match the registered checksum.

### 30.3 Verification Instructions

The Candidate Publication record set **MUST** provide instructions sufficient to verify the checksum of the canonical artifact.

A mirror or exported copy **MAY** be treated as equivalent only where its checksum matches the registered checksum.

### 30.4 Integrity Failure

A checksum mismatch **MUST** trigger invalidation or suspension of the affected claim, investigation, safe preservation of the mismatched artifact, correction or replacement record, notification where material, and restoration of a verified canonical artifact.

A mismatched artifact **MUST NOT** be represented as the registered Candidate Publication.

### 30.5 Signatures and Transparency Logs

A detached signature, trusted timestamp, or transparency-log entry **SHOULD** be added for Candidate Publication where operationally feasible.

These controls supplement but do not replace the mandatory checksum.

---

## 31. Governance Capture and Security-sensitive Change Control

### 31.1 Governance Capture

The Program **MUST** treat coordinated manipulation of governance as a material governance and security risk.

Indicators may include identity duplication, coordinated proposal flooding, fabricated consensus, concealed vendor control, control of multiple supposedly independent roles, coercion, abusive appeals, deliberate obstruction, or fabricated independent review.

Suspected governance capture **MUST** receive a documented assessment.

### 31.2 Participation Controls

Controls against abuse **MUST** preserve legitimate dissent and good-faith participation.

The Program **MAY** apply rate limits, proportional identity or role verification, duplicate-submission controls, recusal, conflict review, second-party confirmation, and temporary participation restrictions.

A restriction **MUST** identify its basis, scope, duration, authority, and reconsideration path.

### 31.3 Independent Review Representation

A review **MUST NOT** be represented as independent where the reviewer is the sole Author, sole decision-maker, or materially controlled by the same undisclosed interest.

Role overlap **MUST** be disclosed.

### 31.4 Security-sensitive Changes

A change affecting approval authority, emergency authority, registry precedence, access control, confidentiality exceptions, artifact integrity, Publisher authority, credential recovery, or Candidate Publication integrity **MUST** be classified as security-sensitive.

A security-sensitive change **MUST** include a security impact statement, conflict review, second-party review, appropriate verification, and disposition of identified risks.

### 31.5 Foundation-stage Exception Authority

A foundation-stage exception **MUST NOT** be created, approved, and relied upon solely by the same person.

Before Candidate Publication, an exception affecting final approval or authority separation **MUST** receive approval by a distinct temporary Approval Authority, independent or second-party confirmation, or approval through a documented non-circular exception mechanism.

Where no such mechanism exists, the exception **MUST NOT** be used to grant final approval.

### 31.6 Lifecycle Classification Alignment

The canonical lifecycle states are:

- Draft;
- Review;
- Candidate Publication;
- Approved Publication.

Reference Publication, Superseded, Suspended, Withdrawn, Invalidated, Corrected, Historical, and Active are publication or registry designations rather than homogeneous lifecycle states.

A document **MUST NOT** treat those categories as interchangeable.

---

## 32. Current Status

The AISET Program is in its initial foundation stage.

This document is the current formal Review version of the proposed AISET Program Charter.

The transition to `PROGRAM-0001 v1.0 Review` follows:

1. `PROGRAM-0001 v0.8 Review`;
2. `PROGRAM-0001-REVIEW-007 — Security and Privacy Review`;
3. `PROGRAM-0001 v0.9 Draft`;
4. `PROGRAM-0001-REVIEW-008 — Security, Privacy, Governance, and Editorial Re-review`;
5. `PROGRAM-0001 v1.0 Review`.

`PROGRAM-0001-REVIEW-008` determined that:

- `SEC-001` was resolved;
- `SEC-002` was resolved;
- all other security and privacy findings were resolved at Charter level;
- `NEW-001` and `NEW-002` were resolved;
- no new blocking finding was identified;
- return to formal Review is permitted.

The following non-blocking matters remain:

- `ED-002 — Normative and Informative Boundaries`;
- `ED-003 — Cross-Reference Precision`;
- `NEW-003 — Operational Record Specifications`;
- `NEW-004 — Checksum Algorithm Policy`;
- `NEW-005 — Independent Review Availability`.

This Review version includes:

- governance-record classification;
- least-privilege and need-to-know access control;
- personal-data principles;
- public and restricted record separation;
- retention, correction, redaction, and deletion;
- confidential appeal and conflict handling;
- security reporter protection;
- incident lifecycle and notification;
- credential and authority compromise controls;
- continuity and recovery requirements;
- third-party dependency controls;
- mandatory Candidate Publication checksums;
- registry binding and integrity-failure handling;
- governance-capture safeguards;
- security-sensitive change review;
- non-circular foundation-stage exception authority;
- lifecycle classification alignment.

This Review version is not yet:

- a Candidate Publication;
- an Approved Publication;
- the governing Charter of the AISET Program;
- an AISET Reference Publication.

The next intended actions are:

1. register `PROGRAM-0001 v1.0 Review`;
2. publish a Publisher acknowledgment;
3. update lifecycle indexes;
4. prepare operational record specifications or templates;
5. define checksum algorithm policy;
6. obtain independent or second-party review;
7. perform Candidate Publication readiness assessment.

Any transition beyond Review requires applicable review, registry, decision, integrity, and Publisher records.
---

## 33. Canonical Repository

The canonical public repository is:

`https://github.com/setem4405-collab/aiset`

The canonical website is:

`https://aisetcfs.com`

An official lifecycle or publication record **MUST** identify the canonical repository path of the applicable artifact.

---

## 34. Attribution

**Author:** Arkadiy Lazarev

**Program Originator:** Arkadiy Lazarev

**Lead Editor:** Arkadiy Lazarev

**Publisher:** AISET Program

Authorship, editorial responsibility, program origination, and publication authority **MUST** remain distinguishable in program records.

---

## 35. License

Copyright © 2026 AISET Program.

This document is licensed under the Creative Commons Attribution 4.0 International License.

See:

- `LICENSE`
- `LICENSES/CC-BY-4.0.txt`
