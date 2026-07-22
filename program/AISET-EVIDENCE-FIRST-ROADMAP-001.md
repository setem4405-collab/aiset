# AISET Evidence-First Roadmap 001

**Identifier:** AISET-EVIDENCE-FIRST-ROADMAP-001  
**Document Type:** Non-normative program planning record  
**Status:** Draft for human review  
**Baseline Repository:** `setem4405-collab/aiset`  
**Baseline Branch:** `master`  
**Baseline Commit:** `21706588827f4a3a2c2a10ce262dcd30c2a5c880`  
**Prepared Date:** 21 July 2026  
**Responsible Program:** AISET Program  
**Program Originator:** Arkadiy Lazarev

---

## 1. Purpose

This roadmap sequences the next AISET program work so that no maturity, conformance, compatibility, interoperability, approval, or publication claim precedes its evidence.

It translates the repository's declared publication sequence and the scope of `PROGRAM-0001` into gated work packages. It is a planning record only. It does not approve a publication, create a normative requirement, assign authority, change a lifecycle status, or authorize implementation, commit, push, release, deployment, or public representation.

---

## 2. Verified Baseline

At the baseline commit:

- `DISCOVERY-0001` is recorded as AISET's first Reference Publication;
- `PROGRAM-0001 v1.0` is recorded as Candidate Publication, not Approved Publication and not Reference Publication;
- the repository declares the planned sequence `DISCOVERY-0001`, `PROGRAM-0001`, `AAR-0001`, `ARI-0001`, and an AISET Business Reference Model;
- no normative AISET schema has been released;
- no normative AISET reference implementation has been released;
- AISET remains technology-independent, and technology-specific material must remain distinguishable from normative architecture.

This baseline is descriptive. Later work must re-verify it against the then-current canonical repository before relying on it.

---

## 3. Evidence-First Operating Rule

Every work package must follow this order:

1. identify the canonical input artifacts and exact versions;
2. define scope, exclusions, authority, acceptance criteria, and allowed paths;
3. record validation, security, privacy, provenance, and governance requirements;
4. produce the proposed artifact in an isolated and bounded workspace;
5. validate the complete changed-path set and all required checks;
6. perform the required review with its classification stated accurately;
7. resolve or explicitly accept every material finding through the authorized decision process;
8. create checksums and provenance evidence for the exact candidate bytes;
9. obtain a separate human lifecycle or publication decision;
10. publish, register, or release only if that decision explicitly authorizes it.

Passing tests, agreement among AI systems, repository access, authorship, editorial control, or completion of an earlier phase does not substitute for human decision authority.

---

## 4. Universal Stage Gate

A stage may be represented as complete only when one evidence package identifies:

- task and attempt identifiers;
- canonical inputs, versions, paths, and checksums;
- authorized scope and explicit exclusions;
- complete changed-path inventory;
- validation and test results;
- unresolved findings and accepted residual risks;
- security, privacy, licensing, and governance checks applicable to the scope;
- reviewer identities, roles, conflicts, and review classification;
- provenance and tool-assistance records;
- the responsible human decision authority and decision record;
- registry, Publisher, release, and supersession records when applicable;
- independent checksum verification of the bytes proposed for publication.

Missing evidence keeps the stage open. A failed gate must not be relabeled as partial conformance or implied approval.

---

## 5. Sequenced Work Packages

### Phase 0 — Baseline and Control Integrity

**Objective:** preserve a reproducible starting point for all later work.

**Required outputs:**

- canonical repository inventory;
- status and version map for program, publication, governance, specification, schema, registry, and implementation artifacts;
- dependency and cross-reference map;
- open-finding and unresolved-decision register;
- verified AISET Galley operational profile for state-changing work.

**Exit evidence:** exact commit, clean-worktree proof, inventory checksums, validator results, and a reviewed discrepancy report.

### Phase 1 — PROGRAM-0001 Lifecycle Completion Decision

**Objective:** evaluate `PROGRAM-0001 v1.0 Candidate Publication` for its next authorized lifecycle disposition.

**Required work:**

- re-verify the Candidate Publication artifact and its existing review, decision, integrity, registry, Publisher, and release documentation;
- verify that the distinction between Approved Publication and Reference Publication is defined before final approval, as required by the Candidate Publication text;
- collect public, stakeholder, implementation-oriented, and governance feedback applicable to the decision scope;
- classify and resolve findings without representing second-party review as independent external review;
- prepare a human decision package for approval, revision, continued candidacy, withdrawal, or other permitted disposition.

**Exit gate:** an explicit authorized lifecycle decision plus integrity, registry, Publisher, release, and provenance records required for the chosen disposition. This roadmap does not predetermine that decision.

### Phase 2 — AAR-0001 Architecture Reference

**Objective:** formalize the technology-independent AISET Foundation Architecture after the governing program basis is sufficient for the work.

**Minimum scope:**

- Cognitive Context Object;
- Cognitive Transformation and Cognitive Transformation Specification;
- Cognitive Invariants and Cognitive Processing Cycle;
- Shared Cognitive Evolution;
- Cognitive Compatibility, Interoperability, and Portability;
- Cognitive Trust and Provenance;
- Cognitive Metrics;
- Directed Cognitive Graphs and Cognitive Context Evolution;
- Cognitive Interfaces and Cognitive Transformation Composition;
- normative/informative boundaries and the status of provisional terminology.

**Exit evidence:** terminology reconciliation, architecture traceability to approved higher-level documents, technology-independence review, security and privacy review, examples separated from normative requirements, finding disposition, exact checksums, and an authorized publication decision.

### Phase 3 — Foundational Specifications, Schemas, and Registries

**Objective:** turn approved architectural concepts into independently testable contracts.

**Ordered deliverables:**

1. specification framework and identifier rules;
2. Cognitive Context Object specification and schema;
3. Cognitive Transformation Specification and schema;
4. invariant, interface, trust/provenance, and metric definitions required by the first conformance profile;
5. machine-readable registry and publication metadata schemas;
6. compatibility, interoperability, portability, and conformance profiles.

**Exit evidence:** schema validation suites, positive and negative fixtures, semantic and invariant tests, version-compatibility analysis, registry integrity checks, cross-implementation test design, security/privacy threat analysis, and separately authorized lifecycle decisions for each normative artifact.

No implementation behavior may silently become normative.

### Phase 4 — ARI-0001 Architecture Reference Implementation

**Objective:** demonstrate and test published AISET specifications without creating a preferred vendor, model, runtime, language, or executor.

**Required capabilities:**

- parse and validate the selected Cognitive Context Object profile;
- execute declared Cognitive Transformations under explicit specifications and invariants;
- generate trust and provenance records;
- calculate defined metrics;
- expose failure handling and reproducible tests;
- support replacement of at least two heterogeneous executor implementations within the tested scope;
- publish known limitations and implementation-specific assumptions.

**Exit evidence:** reproducible build and installation record, software-license record, test corpus, security review, conformance report, failure-case evidence, executor-replacement evidence, checksum manifest, and independently repeatable results.

ARI-0001 remains non-normative unless an authorized publication explicitly states otherwise.

### Phase 5 — Interoperability and Conformance Demonstration

**Objective:** test AISET's central claim across independent implementations over shared governed context.

**Required demonstration:**

- at least two independently implemented participants;
- one declared shared Cognitive Context Object profile;
- versioned Cognitive Transformations governed by the same applicable specifications;
- invariant validation before and after transformation;
- end-to-end provenance and metric records;
- defined invalid, unauthorized, incompatible, and recovery cases;
- reproducible evidence sufficient for an appropriately scoped claim.

**Exit gate:** the claim identifies the exact specifications, versions, implementations, shared context, test scope, limitations, and evidence. Results outside that scope must not be generalized.

### Phase 6 — AISET Business Reference Model

**Objective:** map governed Cognitive Transformations to organizational and business execution without redefining the architecture.

**Minimum scope:**

- humans, AI systems, software services, and temporary executors as replaceable executors;
- shared business context, Cognitive Contracts, permissions, invariants, resource limits, provenance, trust, metrics, escalation, and lifecycle controls;
- prohibitions on self-expanding authority, silent governance modification, unbounded executor creation, and unrecorded context change;
- traceability between planned processes and actual Cognitive Transformations.

**Entry gate:** the required AAR, specifications, schemas, and tested profiles already exist at versions suitable for the declared scope.

**Exit evidence:** reference scenarios, separation-of-authority review, threat model, audit and recovery evidence, human-escalation tests, executor-replacement tests, and an explicit decision on publication status.

---

## 6. Cross-Cutting Workstreams

The following work continues across all phases and does not bypass their gates:

- Cognitive Dictionary and terminology governance;
- security, privacy, trust, provenance, and zero-trust cognition;
- metrics and independent evaluation;
- contribution, review, appeal, conflict-of-interest, and succession procedures;
- identifier, registry, schema, and version governance;
- conformance and interoperability test infrastructure;
- licensing, attribution, citation, and release reproducibility;
- public documentation and implementation guidance clearly separated from normative text.

---

## 7. Explicit Exclusions

This roadmap does not authorize:

- commit or push to `aiset`;
- creation or modification of any file other than this planning record;
- approval or release of `PROGRAM-0001`, `AAR-0001`, `ARI-0001`, a schema, specification, registry record, or Business Reference Model;
- deployment, production access, secrets access, or protected-branch changes;
- a conformance, compatibility, interoperability, security, privacy, legal, or certification claim;
- dependence of normative AISET architecture on a vendor, model, language, runtime, framework, operating system, hardware platform, or executor type;
- autonomous alteration of governance, authority, permissions, findings, evidence, or lifecycle state;
- reuse of the authorization that created this roadmap for any later work package.

Every later state change requires its own formal task contract, safety preflight, bounded execution, evidence, review, and explicit human authorization.

---

## 8. Source Basis

This roadmap is derived from the following canonical files at the baseline commit:

- `README.md`;
- `program/README.md`;
- `program/PROGRAM-0001/PROGRAM-0001-v1.0-candidate-publication.md`;
- `program/PROGRAM-0001/releases/PROGRAM-0001-candidate-publication-release-record-001.md`;
- `publications/README.md`;
- `governance/README.md`;
- `specifications/README.md`;
- `registry/README.md`;
- `schemas/README.md`;
- `implementations/README.md`.

If a cited source is superseded, later work must use the superseding canonical artifact and record the change in its evidence package.

---

## 9. Next Authorized Decision Point

After human review of this draft, the next decision is whether to accept, revise, or reject it as a planning basis. Acceptance would not authorize Phase 0 or any later state-changing work. Each work package requires a separate authorization.
