# PROGRAM-0001 v0.4 — Normative Terminology Re-review 003

**Review Identifier:** PROGRAM-0001-REVIEW-003

**Reviewed Document:** PROGRAM-0001 — AISET Program Charter

**Reviewed Version:** 0.4 Draft

**Review Type:** Normative Terminology Re-review

**Review Status:** Completed

**Review Date:** 16 July 2026

**Reviewer:** Arkadiy Lazarev

**Reviewer Role:** Program Originator and Lead Editor

**Publisher:** AISET Program

**Previous Review:** PROGRAM-0001-REVIEW-002

**License:** Creative Commons Attribution 4.0 International

---

## 1. Review Purpose

This review evaluates whether `PROGRAM-0001 v0.4 Draft` resolves the blocking normative terminology findings recorded in:

`PROGRAM-0001-REVIEW-002 — Normative Terminology Review`

The review determines whether the document is ready to return from Draft to formal Review status.

---

## 2. Review Scope

The re-review covers:

- normative keyword policy;
- uppercase and lowercase requirement language;
- normative obligation;
- normative prohibition;
- normative recommendation;
- normative permission;
- factual possibility;
- clause-level normative scope;
- `Cognitive Contracts`;
- `Cognitive Composition`;
- `Cognitive Transformation Composition`;
- terminology capitalization;
- provisional terminology;
- consistency of the revised Charter with `PROGRAM-0001-REVIEW-002`.

The re-review does not constitute:

- independent external review;
- legal review;
- final governance approval;
- final Publisher approval;
- Candidate Publication approval;
- Reference Publication approval.

---

## 3. Previous Blocking Findings

`PROGRAM-0001-REVIEW-002` identified five findings blocking progression to Candidate Publication:

1. inconsistent uppercase and lowercase mandatory language;
2. incomplete classification of obligation, recommendation, and permission language;
3. ambiguity of `Cognitive Contracts`;
4. insufficient classification of `Cognitive Composition`;
5. lack of a precise clause-level normative rule.

The recommended corrective version was `PROGRAM-0001 v0.4 Draft`.

---

## 4. Normative Keyword Policy

`PROGRAM-0001 v0.4 Draft` establishes one authoritative keyword policy.

The document defines:

- **MUST** as an absolute requirement;
- **MUST NOT** as an absolute prohibition;
- **SHOULD** as a normative recommendation;
- **SHOULD NOT** as a normative discouragement;
- **MAY** as normative permission.

The document also states that lowercase `must`, `should`, and `may` do not carry normative force unless they appear inside a quotation.

### Finding

The normative keyword policy is explicit and operational.

### Outcome

**Resolved.**

---

## 5. Clause-Level Normative Scope

The revised Charter states:

> Only clauses using the uppercase keywords MUST, MUST NOT, SHOULD, SHOULD NOT, or MAY are normative requirements of this Charter.

It further distinguishes descriptive, historical, explanatory, and implementation-guidance material as informative unless an uppercase normative keyword is present.

### Finding

The Charter now defines normative force at clause level rather than only at section or subject level.

### Outcome

**Resolved.**

---

## 6. Lowercase Requirement Language

The revised Charter removes ordinary lowercase mandatory and recommendation language from substantive normative clauses.

Lowercase forms remain only where they are:

- named as literal words in the normative keyword policy;
- used inside quotations;
- used as ordinary non-normative language.

### Finding

The ambiguity between uppercase normative keywords and lowercase ordinary-language verbs has been substantially removed.

### Outcome

**Resolved.**

---

## 7. Obligation, Recommendation, and Permission

The revised Charter distinguishes:

- binding obligation through **MUST**;
- binding prohibition through **MUST NOT**;
- recommended action through **SHOULD**;
- discouraged action through **SHOULD NOT**;
- normative permission through **MAY**;
- factual possibility through terms such as `can`.

### Finding

The revised language separates normative permission from factual possibility.

### Outcome

**Resolved.**

---

## 8. Cognitive Contracts

`Cognitive Contracts` has been removed from the foundational architectural term list.

The revised Charter explicitly states:

> `Cognitive Contracts` is not recognized as a foundational normative term in this version.

### Finding

The ambiguity and potential redundancy of `Cognitive Contracts` has been removed from the Charter’s foundational architecture.

### Outcome

**Resolved.**

---

## 9. Cognitive Transformation Composition

The former term `Cognitive Composition` has been replaced with:

> `Cognitive Transformation Composition`

The revised term more clearly identifies composition as a property or capability involving Cognitive Transformations.

### Finding

The revised term is more precise and better aligned with transformation-centric architecture.

### Outcome

**Resolved.**

### Future Requirement

The Architecture Reference should later define:

- sequential composition;
- parallel composition;
- conditional composition;
- graph composition;
- composition validity;
- invariant preservation;
- provenance across composed transformations.

---

## 10. Terminology Capitalization

The revised Charter establishes that:

- capitalized architectural terms denote formally recognized AISET concepts or concepts intended for formal definition;
- lowercase words retain ordinary-language meaning;
- undefined formal terms are provisional for conformance purposes.

### Finding

A usable capitalization and formal-term policy is now present.

### Outcome

**Resolved.**

---

## 11. Provisional Terminology

The revised Charter states that a term without a formal definition:

- is provisional for conformance purposes;
- must not serve as the sole basis of a conformance claim.

### Finding

This rule prevents undefined architectural terminology from being treated as sufficient for conformance.

### Outcome

**Resolved.**

---

## 12. Technology Independence Clause

Section `7.1 Technology Independence` currently states:

> No normative AISET entity **MUST** depend on a specific technology, model, executor, programming language, runtime, vendor, or implementation framework.

Under the normative keyword policy, **MUST** expresses an absolute requirement.

The grammatical structure `No entity MUST depend` is logically and normatively ambiguous.

It can be interpreted as stating that no entity is required to depend on a specific technology, rather than prohibiting such dependency.

The intended architectural rule is a prohibition.

The clause should state:

> A normative AISET entity **MUST NOT** depend on a specific technology, model, executor, programming language, runtime, vendor, or implementation framework.

### Finding

The clause uses the wrong normative operator for its intended meaning.

### Severity

**Blocking for progression to Review.**

### Required Action

Replace:

```markdown
No normative AISET entity **MUST** depend on a specific technology, model, executor, programming language, runtime, vendor, or implementation framework.
```

with:

```markdown
A normative AISET entity **MUST NOT** depend on a specific technology, model, executor, programming language, runtime, vendor, or implementation framework.
```

---

## 13. Technology-Specific Profiles

The revised Charter permits technology-specific profiles while preserving the technology-independent architecture.

It states that technology-specific dependencies can be defined only where they are explicit and do not redefine the underlying architecture.

### Finding

The relationship between technology independence and technology-specific profiles is coherent.

### Outcome

**Accepted.**

---

## 14. Normative Entity List

The revised Charter changes the heading concept from foundational architectural entities to foundational architectural terms.

This is an improvement because the list contains several conceptual classes:

- objects;
- transformations;
- specifications;
- properties;
- models;
- graphs;
- frameworks;
- capabilities.

The document also requires formal classification before a conformance claim depends on a term.

### Finding

The entity-class ambiguity identified in `PROGRAM-0001-REVIEW-002` has been reduced sufficiently for the Charter stage.

### Outcome

**Accepted for further Review.**

---

## 15. Conformance Terminology

The revised Charter requires a conformance claim to identify:

- the applicable specification;
- implemented scope;
- implementation profile;
- validation evidence;
- known limitations;
- deviations;
- applicable test results.

It also prohibits claims based solely on provisional terminology.

### Finding

Conformance terminology is materially clearer and more controlled.

### Outcome

**Accepted.**

---

## 16. Lifecycle Terminology

The revised Charter requires lifecycle transitions to identify:

- previous status;
- new status;
- applicable version;
- decision authority;
- effective date;
- supporting records.

The document also preserves the requirement to define the distinction between Approved Publication and Reference Publication before final approval.

### Finding

Lifecycle terminology is sufficiently precise for the current Draft stage.

### Outcome

**Accepted.**

---

## 17. Review of Blocking Findings

The disposition of the five findings from `PROGRAM-0001-REVIEW-002` is:

| Finding | Disposition |
| --- | --- |
| Uppercase and lowercase mandatory language | Resolved |
| Obligation, recommendation, and permission classification | Resolved |
| `Cognitive Contracts` ambiguity | Resolved |
| `Cognitive Composition` classification | Resolved |
| Clause-level normative rule | Resolved |

One new blocking defect was found in the application of the revised keyword policy:

| New Finding | Disposition |
| --- | --- |
| Incorrect **MUST** operator in Technology Independence clause | Revision required |

---

## 18. Residual Non-Blocking Matters

The following matters remain appropriate for future Architecture Reference, Cognitive Dictionary, governance, or lifecycle documents:

- formal definitions of foundational architectural terms;
- conceptual classification of every architectural term;
- detailed Cognitive Transformation Composition semantics;
- distinction between Approved Publication and Reference Publication;
- formal publication-class requirements;
- machine-readable normative clause metadata;
- conformance test methodology;
- external or independent review.

These matters do not prevent correction of the identified clause and return to Review.

---

## 19. Required Correction

The Lead Editor should create a corrected version containing the following change.

### Existing Text

```markdown
No normative AISET entity **MUST** depend on a specific technology, model, executor, programming language, runtime, vendor, or implementation framework.
```

### Corrected Text

```markdown
A normative AISET entity **MUST NOT** depend on a specific technology, model, executor, programming language, runtime, vendor, or implementation framework.
```

No other normative terminology change is required by this re-review.

---

## 20. Recommended Next Version

Because the correction changes the normative operator from **MUST** to **MUST NOT**, it changes the literal normative meaning of the clause.

The correction should therefore be preserved in a new version rather than silently modifying `v0.4 Draft`.

The recommended next version is:

> **PROGRAM-0001 v0.5 Draft**

The new version should:

- preserve `v0.4 Draft`;
- contain the corrected Technology Independence clause;
- reference `PROGRAM-0001-REVIEW-003`;
- retain the Draft lifecycle status until verification is complete.

---

## 21. Review Decision

`PROGRAM-0001 v0.4 Draft` is assessed as:

> **Substantially resolving PROGRAM-0001-REVIEW-002, with one blocking normative operator correction required.**

The revised normative terminology model is accepted.

The document is not yet approved to return to formal Review status because the Technology Independence clause does not express the intended prohibition unambiguously.

---

## 22. Recommended Lifecycle Action

**Current version:** PROGRAM-0001 v0.4 Draft

**Current status:** Draft

**Recommended next version:** PROGRAM-0001 v0.5 Draft

**Recommended action:** Apply one targeted normative correction

**Return to Review permitted immediately:** No

**Return to Review permitted after correction and verification:** Yes

---

## 23. Review Outcome

**Outcome:** Revision required

**Previous blocking findings resolved:** Five

**New blocking findings:** One

**Architectural inconsistency:** None beyond the affected normative clause

**Direct progression to Candidate Publication permitted:** No

**Return to Review after targeted correction:** Recommended

**Independent review before final approval:** Recommended

---

## 24. Review Limitations

This review was performed by the Program Originator and Lead Editor.

The Reviewer also holds authorship, repository maintenance, registry administration, and Publisher representation roles during the foundation stage.

This overlap is disclosed.

The review must not be represented as:

- independent review;
- external standards validation;
- third-party certification;
- legal advice.

---

## 25. Attribution

**Reviewer:** Arkadiy Lazarev

**Program Originator:** Arkadiy Lazarev

**Lead Editor:** Arkadiy Lazarev

**Publisher:** AISET Program

---

## 26. License

Copyright © 2026 AISET Program.

This review record is licensed under the Creative Commons Attribution 4.0 International License.

See:

- `LICENSE`
- `LICENSES/CC-BY-4.0.txt`