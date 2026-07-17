# PROGRAM-0001 v0.3 — Normative Terminology Review 002

**Review Identifier:** PROGRAM-0001-REVIEW-002

**Reviewed Document:** PROGRAM-0001 — AISET Program Charter

**Reviewed Version:** 0.3 Review

**Review Type:** Normative Terminology Review

**Review Status:** Completed

**Review Date:** 16 July 2026

**Reviewer:** Arkadiy Lazarev

**Reviewer Role:** Program Originator and Lead Editor

**Publisher:** AISET Program

**Previous Review:** PROGRAM-0001-REVIEW-001

**License:** Creative Commons Attribution 4.0 International

---

## 1. Review Purpose

This review evaluates the normative terminology of `PROGRAM-0001 v0.3 Review`.

The review examines whether the Charter clearly and consistently distinguishes:

- normative requirements;
- recommendations;
- permissions;
- descriptive statements;
- informative guidance;
- architectural entities that are formally recognized;
- architectural terms that remain provisional or undefined.

The review is intended to identify terminology issues that must be resolved before progression to Candidate Publication.

---

## 2. Review Scope

The review covers:

- normative keywords;
- keyword capitalization;
- normative and informative distinctions;
- strength of obligations;
- consistency of requirement language;
- architectural entity names;
- provisional terminology;
- term plurality and grammatical consistency;
- relationships among program, architecture, governance, and implementation terms;
- terminology readiness for future specifications.

The review does not provide:

- final definitions for every architectural entity;
- a complete AISET Cognitive Dictionary;
- conformance tests;
- legal interpretation;
- external standards-body approval;
- independent third-party validation.

---

## 3. Review Method

The document was evaluated by examining:

1. the normative keyword declaration in `Document Status`;
2. all explicit uses of `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY`;
3. lowercase uses of `must`, `should`, and `may`;
4. statements that impose obligations without a normative keyword;
5. terms listed as foundational architectural entities;
6. terms that are referenced but not yet formally defined;
7. consistency between lifecycle, governance, publication, registry, and architecture terminology.

---

## 4. Normative Keyword Model

`PROGRAM-0001 v0.3 Review` states that the following uppercase terms express intended normative program requirements:

- **MUST**;
- **MUST NOT**;
- **SHOULD**;
- **SHOULD NOT**;
- **MAY**.

This establishes a recognizable normative keyword model.

However, the document also contains many lowercase uses of:

- `must`;
- `must not`;
- `should`;
- `may`.

The distinction between uppercase normative keywords and lowercase ordinary-language verbs is not yet applied consistently throughout the Charter.

### Finding

The declared normative keyword model is valid in principle but incomplete in application.

### Severity

**Blocking for Candidate Publication.**

### Required Action

Before Candidate Publication, the Charter must either:

1. convert intended normative requirements to the declared uppercase keywords; or
2. explicitly state that lowercase forms may also carry normative meaning in identified contexts.

The first approach is recommended because it provides greater precision and machine readability.

---

## 5. Uppercase Keyword Usage

The following clauses use explicit uppercase normative keywords:

- lower-level documents **MUST NOT** override higher-level documents;
- informative material **MUST NOT** redefine normative program requirements.

These clauses are clear and appropriately strong.

### Finding

Existing uppercase normative clauses are understandable and consistent with the declared keyword model.

### Outcome

**Acceptable.**

---

## 6. Lowercase Mandatory Language

The Charter contains multiple lowercase uses of `must` and `must not`, including requirements concerning:

- separation between normative architecture and implementation material;
- preservation of program origination;
- disclosure of conflicts of interest;
- preservation of publication artifacts;
- alteration of registry meaning;
- attribution of actions to applicable roles;
- review findings;
- correction and withdrawal records;
- immutable releases;
- registry identifiers;
- conformance claims;
- licensing;
- publication replacement;
- historical discoverability.

Because `Document Status` assigns normative meaning specifically to uppercase terms, lowercase mandatory language creates ambiguity.

A reader cannot always determine whether lowercase `must` means:

- a binding normative requirement;
- a strong descriptive expectation;
- ordinary explanatory prose.

### Finding

Lowercase mandatory language is not sufficiently differentiated from uppercase normative requirements.

### Severity

**Blocking for Candidate Publication.**

### Required Action

Each lowercase `must` or `must not` must be classified as one of the following:

- normative and converted to **MUST** or **MUST NOT**;
- informative and rewritten without mandatory language;
- deferred to a lower-level governance or specification document.

---

## 7. Lowercase Recommendation Language

The Charter contains numerous lowercase uses of `should`, including statements concerning:

- preservation of traceable trust and provenance;
- independent measurement;
- governed context evolution;
- transparent publication;
- role separation;
- review records;
- historical discoverability;
- registry contents;
- conformance claims;
- security and privacy analysis;
- continuity;
- succession;
- additional reviews.

The current text does not always distinguish whether `should` expresses:

- a normative recommendation;
- a design preference;
- an anticipated future practice;
- informative guidance.

### Finding

Recommendation strength is inconsistent.

### Severity

**Material but non-blocking for Review status. Blocking for Candidate Publication where the recommendation affects governance or conformance.**

### Required Action

Each occurrence should be classified as:

- **SHOULD** for a normative recommendation;
- **MAY** for an optional action;
- informative language such as `is encouraged`, `is expected`, or `is anticipated`;
- a future requirement to be defined in a specialized document.

---

## 8. Permission Language

The Charter uses lowercase `may` in several contexts, including:

- publication classes;
- lifecycle progression;
- role combinations;
- contribution types;
- review types;
- reconsideration and appeals;
- suspension and withdrawal;
- program evolution.

Some uses describe possibility rather than permission.

For example, a document stating that a publication `may pass through` lifecycle statuses describes a possible process, while a statement that an authority `MAY authorize` an action would grant normative permission.

### Finding

Possibility and permission are not always distinguished.

### Severity

**Non-blocking for Review status.**

### Required Action

Before Candidate Publication:

- normative permission should use **MAY**;
- factual possibility should use terms such as `can`, `may occur`, or `is capable of`;
- anticipated future actions should be explicitly identified as informative.

---

## 9. Normative Scope

The `Document Status` section identifies several categories intended to become normative upon approval.

This is useful, but normative status is currently assigned at a broad section or subject level.

Within those categories, individual sentences mix:

- requirements;
- explanations;
- historical statements;
- future expectations;
- implementation guidance.

### Finding

The normative scope is defined broadly but not always at clause level.

### Severity

**Material but non-blocking for Review status.**

### Required Action

The Candidate Publication should state one of the following:

1. all clauses within explicitly identified normative sections are normative unless marked informative; or
2. only clauses using defined uppercase keywords are normative.

The second model is recommended because it minimizes ambiguity.

---

## 10. Informative Material

The Charter states that descriptive background, examples, forecasts, and implementation guidance are informative unless explicitly identified as normative.

This is directionally correct.

However, the document does not mark specific subsections as:

- Normative;
- Informative;
- Historical;
- Provisional.

### Finding

The informative-material rule is present but not operationalized at section level.

### Severity

**Non-blocking.**

### Recommended Action

Future versions should support explicit labels such as:

- `Normative`;
- `Informative`;
- `Provisional`;
- `Historical`.

These labels may be placed beneath section headings or recorded through machine-readable publication metadata.

---

## 11. Foundational Architectural Entity List

Section 8 currently recognizes the following foundational architectural entities:

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

The section correctly states that these entities will be formally defined in future Architecture Reference and normative specification publications.

However, the list currently mixes several different conceptual classes:

- canonical objects;
- transformations;
- specifications;
- processing cycles;
- properties;
- frameworks;
- models;
- graphs;
- interfaces;
- contracts;
- composition concepts.

### Finding

The entity list is useful for architectural orientation but does not yet distinguish entity classes.

### Severity

**Non-blocking for Review status. Material for Architecture Reference development.**

### Required Action

A future version or companion terminology record should classify each term as one of the following:

- normative object;
- normative process;
- normative specification;
- architectural property;
- architectural model;
- framework;
- interface;
- graph;
- lifecycle concept;
- provisional research concept.

---

## 12. Cognitive Context Object

`Cognitive Context Object` is treated as a foundational architectural entity.

The Charter does not yet explicitly state whether it is:

- the canonical representation of cognitive state;
- the only normative unit transformed by a Cognitive Transformation;
- a general conceptual object;
- one possible representation among several.

### Finding

The term is central but under-specified at Charter level.

### Severity

**Non-blocking for the Charter Review, but blocking for any future conformance claim based on the term.**

### Recommended Action

The Architecture Reference should define Cognitive Context Object as the canonical technology-independent representation of cognitive state and clarify its relationship to validity, versioning, invariants, and transformation.

---

## 13. Cognitive Transformation

The term `Cognitive Transformation` is consistently presented as an operation on Cognitive Context Objects.

However, the Charter does not yet distinguish clearly between:

- the abstract transformation;
- its normative specification;
- the executor performing it;
- the runtime event;
- the resulting state transition.

### Finding

The term is conceptually coherent but requires a formal type distinction.

### Severity

**Non-blocking for Charter Review.**

### Recommended Action

Future normative definitions should distinguish:

- Cognitive Transformation;
- Cognitive Transformation Specification;
- transformation execution;
- implementation or executor;
- input Cognitive Context Object;
- output Cognitive Context Object.

---

## 14. Cognitive Transformation Specification

The Charter treats `Cognitive Transformation Specification` as a foundational term and uses it in the portability principle.

This is consistent with the technology-independence objective.

### Finding

The term is suitable for continued use.

### Outcome

**Accepted as a foundational normative term, pending formal definition.**

### Recommended Definition Direction

A Cognitive Transformation Specification should define:

- valid inputs;
- valid outputs;
- preconditions;
- postconditions;
- invariants;
- permitted state changes;
- provenance requirements;
- evaluation requirements;
- failure conditions.

---

## 15. Cognitive Invariant

The Charter refers to both:

- `Cognitive Invariant`;
- `invariants`.

It does not yet specify whether an invariant:

- must always be preserved;
- may be intentionally transformed;
- may apply only within a specific transformation;
- may be structural, semantic, procedural, or governance-based.

### Finding

The singular formal term and plural ordinary-language uses are not yet fully aligned.

### Severity

**Non-blocking for Review status.**

### Recommended Action

The Architecture Reference should distinguish:

- invariant definition;
- invariant scope;
- invariant preservation;
- authorized invariant transformation;
- invariant violation;
- validity consequences.

---

## 16. Cognitive Processing Cycle

The term `Cognitive Processing Cycle` is listed as foundational but is not used extensively elsewhere in the Charter.

### Finding

The term is acceptable but currently has no Charter-level normative role.

### Severity

**Non-blocking.**

### Recommended Action

The Architecture Reference should define whether the Cognitive Processing Cycle is:

- the minimal normative cycle for transforming one valid Cognitive Context Object into another;
- a reference processing sequence;
- a lifecycle model;
- an informative implementation pattern.

---

## 17. Cognitive Compatibility and Interoperability

The Charter distinguishes:

- Cognitive Compatibility;
- Cognitive Interoperability.

The distinction is conceptually useful:

- compatibility concerns production of valid Cognitive Context Objects under the same specification;
- interoperability concerns joint participation in governed transformation and shared context evolution.

### Finding

The distinction is coherent and should be preserved.

### Outcome

**Accepted.**

### Recommended Action

Future definitions should specify:

- compatibility test conditions;
- interoperability test conditions;
- applicable specification versions;
- validation evidence;
- shared-context requirements;
- limits of claims.

---

## 18. Cognitive Portability

The Charter defines portability through replacement of an implementation without changing the applicable Cognitive Transformation Specification.

This formulation is aligned with technology independence.

### Finding

The term is coherent and sufficiently differentiated from compatibility and interoperability.

### Outcome

**Accepted, pending formal specification.**

---

## 19. Cognitive Trust and Provenance

The term `Cognitive Trust and Provenance` may refer to:

- an architectural concern;
- a transversal framework;
- a trust layer;
- a set of metadata requirements;
- an evaluation domain.

The current entity list does not identify which interpretation is intended.

### Finding

The term combines two related but distinct concepts and lacks an explicit conceptual class.

### Severity

**Non-blocking for Review status.**

### Recommended Action

Future terminology should distinguish:

- provenance data;
- provenance verification;
- trust assertions;
- trust evaluation;
- authority;
- evidence;
- responsibility;
- a possible Cognitive Trust and Provenance Framework.

---

## 20. Cognitive Metrics

The term `Cognitive Metrics` is broad and may describe:

- metric definitions;
- measurements;
- evaluation methods;
- result records;
- conformance thresholds.

### Finding

The term is suitable as a domain name but not yet sufficiently precise as a singular architectural entity.

### Severity

**Non-blocking.**

### Recommended Action

Future documentation should distinguish:

- Cognitive Metric;
- metric specification;
- measurement procedure;
- measurement result;
- evaluation criterion;
- conformance threshold.

---

## 21. Directed Cognitive Graph

The term `Directed Cognitive Graph` is recognized but not related explicitly in the Charter to:

- static architecture;
- runtime processing;
- adaptive restructuring;
- Cognitive Processing Cycle;
- Cognitive Context Object evolution.

### Finding

The term remains architecturally plausible but under-classified.

### Severity

**Non-blocking for Charter Review.**

### Recommended Action

The Architecture Reference should determine whether the normative term is:

- Directed Cognitive Graph;
- Cognitive Flow Graph;
- another canonical graph term.

It should also distinguish static, dynamic, and adaptive graph forms where those distinctions remain part of the architecture.

---

## 22. Cognitive Context Evolution Model

The term `Cognitive Context Evolution Model` is consistent with governed context evolution and versioned shared context.

### Finding

The term is suitable but not formally connected to version graphs, lifecycle states, or Shared Cognitive Evolution.

### Severity

**Non-blocking.**

### Recommended Action

Future definitions should establish the relationship among:

- Cognitive Context Evolution Model;
- Cognitive Context Object versions;
- version relationships;
- Shared Cognitive Evolution;
- convergence;
- branching;
- merging;
- provenance.

---

## 23. Cognitive Interface Specification

The Charter includes `Cognitive Interface Specification` as a foundational entity.

This term is consistent with the Context First principle when an interface is defined as an interface to a transformation rather than an interface to an executor.

### Finding

The term is acceptable, but the Context First restriction should become explicit in its formal definition.

### Outcome

**Accepted, pending formal definition.**

---

## 24. Cognitive Contracts

The term `Cognitive Contracts` is listed as a foundational architectural entity but is not defined elsewhere in the Charter.

The term may overlap with:

- Cognitive Transformation Specifications;
- Cognitive Interface Specifications;
- invariants;
- typed transformation requirements;
- trust and provenance requirements.

It is not yet clear whether Cognitive Contract is:

- an independent normative entity;
- a composite of existing specifications;
- an informative design pattern;
- an obsolete earlier term.

### Finding

The term is currently ambiguous and potentially redundant.

### Severity

**Blocking for Candidate Publication unless explicitly classified as provisional.**

### Required Action

Before Candidate Publication, one of the following decisions must be recorded:

1. retain `Cognitive Contract` and define its distinct normative role;
2. classify it as a provisional research term;
3. replace it with existing specification terminology;
4. remove it from the foundational entity list.

The recommended action is to remove it from the foundational normative list unless a distinct role can be demonstrated.

---

## 25. Cognitive Composition

The term `Cognitive Composition` is listed as foundational but is not defined elsewhere in the Charter.

It may refer to:

- sequential composition of transformations;
- parallel composition;
- graph composition;
- specification composition;
- context merge;
- shared evolution.

### Finding

The term names an important architectural capability but not yet a sufficiently defined entity.

### Severity

**Material but non-blocking for Review status. Blocking for Candidate Publication if retained as a formally recognized foundational entity without classification.**

### Required Action

Before Candidate Publication, the term should be:

- formally defined;
- renamed as `Cognitive Transformation Composition`;
- classified as a capability rather than an entity;
- or marked provisional.

The recommended direction is `Cognitive Transformation Composition`.

---

## 26. Shared Cognitive Evolution

The term is aligned with the Shared Context principle and governed evolution of shared Cognitive Context Objects.

However, the Charter does not yet clarify whether Shared Cognitive Evolution concerns:

- one shared Cognitive Context Object;
- multiple related context objects;
- a version graph;
- coordinated transformations by independent implementations.

### Finding

The term is conceptually strong but requires a precise object model.

### Severity

**Non-blocking for Review status.**

### Recommended Action

The Architecture Reference should define Shared Cognitive Evolution as coordinated evolution of shared cognitive context through independently executed but interoperable Cognitive Transformations.

---

## 27. Executor Terminology

The Charter uses the word `executor` only to establish technology independence and the Context First principle.

This is appropriate because the executor is not presented as a normative architectural entity.

### Finding

Executor terminology is correctly subordinate to transformation and context terminology.

### Outcome

**Accepted.**

### Recommendation

The term should remain implementation-neutral and should not be elevated into the foundational normative entity list unless a later specification requires an abstract execution role.

---

## 28. Agent Terminology

The reviewed Charter does not use `Agent` as a foundational architectural entity.

This is consistent with the transformation-centric architecture of the AISET Program.

### Finding

The absence of agent-centric normative terminology improves technology independence and reduces coupling to a specific implementation paradigm.

### Outcome

**Accepted.**

---

## 29. Singular and Plural Forms

Several terms appear both as singular formal names and plural domain labels, including:

- Cognitive Invariant and invariants;
- Cognitive Metric and Cognitive Metrics;
- Cognitive Contract and Cognitive Contracts;
- Cognitive Transformation Specification and specifications.

### Finding

The document does not yet establish canonical singular forms for all registered terms.

### Severity

**Non-blocking.**

### Recommended Action

The AISET Cognitive Dictionary should register:

- canonical singular term;
- accepted plural;
- abbreviation, if any;
- definition;
- conceptual class;
- normative status;
- related terms;
- deprecated aliases.

---

## 30. Capitalization

Formal architectural terms are generally capitalized consistently.

However, the distinction between a formal term and ordinary descriptive language is not always explicit.

For example:

- `Cognitive Transformation` appears as a formal entity;
- `transformation` may appear as ordinary language;
- `Review` may denote a lifecycle status or a review activity;
- `Publisher` may denote a defined role or an organization.

### Finding

Capitalization is generally coherent but requires a formal style rule.

### Severity

**Non-blocking.**

### Recommended Action

A terminology style rule should state:

- capitalized terms denote registered or formally defined AISET concepts;
- lowercase terms retain their ordinary-language meaning;
- lifecycle statuses use canonical capitalization when referring to registered states;
- role names use canonical capitalization when referring to defined AISET roles.

---

## 31. Lifecycle Terminology

The Charter defines the lifecycle statuses:

1. Draft;
2. Review;
3. Candidate Publication;
4. Approved Publication;
5. Reference Publication;
6. Superseded;
7. Withdrawn.

The sequence is understandable, but the relationship between Approved Publication and Reference Publication is not yet fully defined.

### Finding

Lifecycle terminology is coherent but requires transition criteria.

### Severity

**Non-blocking for Review status. Material before final approval.**

### Recommended Action

A future publication lifecycle specification should define:

- entry criteria;
- exit criteria;
- permitted transitions;
- prohibited transitions;
- responsible authority;
- required records;
- immutability point;
- distinction between Approved and Reference Publication.

---

## 32. Program and Publisher Terminology

The Charter identifies:

- `AISET Program` as the program;
- `AISET Program` as Publisher;
- individuals as Publisher representatives or administrators in supporting records.

This is workable during the foundation stage but may create ambiguity between:

- the program as an institutional initiative;
- the Publisher as a defined authority;
- the person exercising Publisher authority.

### Finding

The current terminology is acceptable for the foundation stage but should be formalized before delegated governance.

### Severity

**Non-blocking.**

### Recommended Action

Future governance should distinguish:

- Publisher;
- Publishing Authority;
- Publisher Representative;
- publishing action;
- publication decision record.

---

## 33. Normative Terminology Findings

The review records the following principal findings.

### Blocking Before Candidate Publication

1. inconsistent uppercase and lowercase mandatory language;
2. incomplete classification of `must`, `should`, and `may`;
3. ambiguity of `Cognitive Contracts`;
4. insufficient classification of `Cognitive Composition` if retained as foundational;
5. lack of a precise rule identifying normative clauses.

### Non-Blocking

1. entity-class distinctions remain incomplete;
2. several architectural terms require formal definitions;
3. capitalization rules should be documented;
4. canonical singular and plural forms should be registered;
5. lifecycle transition criteria require a specialized specification;
6. trust, provenance, metrics, graph, and evolution terminology require refinement.

---

## 34. Required Revision Plan

Before progression to Candidate Publication, the Lead Editor should prepare a revised Charter version that:

1. defines one authoritative normative keyword policy;
2. converts binding requirements to uppercase normative keywords;
3. rewrites informative lowercase obligation language;
4. separates normative permission from factual possibility;
5. declares whether only uppercase keyword clauses are normative;
6. removes or classifies `Cognitive Contracts`;
7. defines or reclassifies `Cognitive Composition`;
8. introduces canonical terminology style rules;
9. preserves all accepted architectural distinctions;
10. records the relationship to this review.

The recommended next working version is:

> **PROGRAM-0001 v0.4 Draft**

The recommended lifecycle action is a temporary return from Review to Draft for targeted normative terminology revision.

---

## 35. Review Decision

`PROGRAM-0001 v0.3 Review` is assessed as:

> **Architecturally coherent but requiring normative terminology revision before Candidate Publication.**

The findings do not invalidate the current Review registration.

The findings do prevent progression directly from `v0.3 Review` to Candidate Publication without revision.

---

## 36. Recommended Lifecycle Action

**Current version:** PROGRAM-0001 v0.3 Review

**Current status:** Review

**Recommended next version:** PROGRAM-0001 v0.4 Draft

**Recommended action:** Return to Draft for targeted normative terminology revision

**Reason:** Blocking terminology findings must be resolved before Candidate Publication

After revision, the document should undergo:

- normative terminology re-review;
- editorial review;
- governance consistency review;
- Publisher review;
- registry status update.

---

## 37. Review Outcome

**Outcome:** Revision required

**Architectural blocking findings:** None

**Normative terminology findings blocking Candidate Publication:** Five

**Current Review status invalidated:** No

**Direct progression to Candidate Publication permitted:** No

**Return to Draft recommended:** Yes

**Independent review before final approval:** Recommended

---

## 38. Review Limitations

This review was performed by the Program Originator and Lead Editor.

The Reviewer also holds authorship, editorial, repository maintenance, registry administration, and Publisher representation roles during the foundation stage.

This overlap is disclosed.

The review must not be represented as:

- independent review;
- external standards validation;
- third-party certification;
- legal advice.

---

## 39. Attribution

**Reviewer:** Arkadiy Lazarev

**Program Originator:** Arkadiy Lazarev

**Lead Editor:** Arkadiy Lazarev

**Publisher:** AISET Program

---

## 40. License

Copyright © 2026 AISET Program.

This review record is licensed under the Creative Commons Attribution 4.0 International License.

See:

- `LICENSE`
- `LICENSES/CC-BY-4.0.txt`