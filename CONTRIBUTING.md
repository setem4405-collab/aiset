# Contributing to AISET

Thank you for your interest in contributing to the AISET Program.

AISET is an open, technology-independent engineering program focused on standardizing the architecture of cognitive context transformations.

Contributions may include:

- publications;
- architectural proposals;
- specifications;
- schemas;
- registry records;
- governance documents;
- reference implementations;
- conformance tests;
- reviews;
- terminology improvements;
- editorial corrections.

## Contribution Principles

Contributions should follow these principles:

1. Technology independence;
2. Clear separation between normative and informative material;
3. Explicit authorship and provenance;
4. Reviewable change history;
5. Compatibility and interoperability awareness;
6. Clear licensing;
7. Reproducibility where applicable;
8. Security and privacy awareness;
9. Respectful and evidence-based discussion.

## Before Contributing

Before preparing a contribution:

- review the repository structure;
- read the relevant publication or specification;
- identify whether the change is editorial, architectural, normative, or implementation-specific;
- verify that the proposal does not introduce unnecessary vendor or technology dependence;
- determine whether a new identifier, version, schema, or registry record is required.

## Types of Contributions

### Editorial Contribution

An editorial contribution improves clarity, grammar, formatting, links, citations, or structure without changing normative meaning.

### Architectural Contribution

An architectural contribution introduces or changes concepts, relationships, principles, processing models, or system boundaries.

### Normative Contribution

A normative contribution adds or modifies requirements, constraints, invariants, conformance rules, interfaces, or validation conditions.

### Implementation Contribution

An implementation contribution adds software, tools, adapters, validators, tests, or reference implementation material.

### Review Contribution

A review contribution evaluates a document, specification, schema, implementation, or registry record and provides traceable findings.

## Contribution Workflow

The recommended workflow is:

1. Identify the relevant directory and document.
2. Create a focused change.
3. Review the change locally.
4. Run formatting and validation checks.
5. Create a descriptive commit.
6. Submit the change for review.
7. Address review findings.
8. Record approval or publication status where applicable.

## Branches and Commits

Contributions should use focused branches where practical.

Commit messages should be concise and describe the purpose of the change.

Examples:

```text
docs: clarify CCO terminology
spec: add transformation invariant requirements
schema: add registry record validation
governance: define candidate publication status
impl: add CCO validation prototype
test: add interoperability test case
```

Avoid combining unrelated changes in a single commit.

## Markdown Checks

Before committing Markdown changes, run:

```bash
git diff --check
```

For staged changes, run:

```bash
git diff --cached --check
```

These commands should produce no output.

## Normative Language

Normative AISET documents may use:

- **MUST**
- **MUST NOT**
- **SHOULD**
- **SHOULD NOT**
- **MAY**

Normative terms should only be used when the statement is intended to affect implementation, validation, compatibility, interoperability, or conformance.

## Publication Changes

Released publications must not be silently modified.

Changes to a released publication require one or more of the following:

- a correction notice;
- a new version;
- an amendment;
- a superseding publication;
- an updated release manifest;
- updated checksums;
- updated review records.

Published tags and release artifacts are treated as immutable records.

## Specification Changes

A specification contribution should identify:

- the specification identifier;
- the affected version;
- the change type;
- normative impact;
- compatibility impact;
- interoperability impact;
- migration requirements;
- security considerations;
- validation requirements.

Breaking changes require an explicit new version.

## Schema Changes

Schema contributions should indicate whether the change is:

- backward-compatible;
- conditionally compatible;
- breaking;
- editorial or non-semantic.

Schema changes should include validation examples where practical.

## Registry Changes

Registry contributions should preserve:

- identifier uniqueness;
- explicit versioning;
- canonical artifact references;
- status traceability;
- checksum integrity;
- historical discoverability.

Published registry records must not be silently rewritten in a way that changes their meaning.

## Implementation Contributions

Software contributions must identify:

- the applicable specification and version;
- implementation scope;
- known limitations;
- test procedures;
- security considerations;
- software license;
- third-party dependencies.

Implementation-specific behavior must not be presented as a normative AISET requirement.

## Licensing

By contributing non-software material, the contributor agrees that the contribution may be distributed under the Creative Commons Attribution 4.0 International License unless explicitly stated otherwise.

Software contributions require an explicitly identified software license before acceptance.

See:

- [Repository Licensing Notice](LICENSE)
- [CC BY 4.0 License Text](LICENSES/CC-BY-4.0.txt)
- [Software Licensing Notice](LICENSES/SOFTWARE-LICENSE-NOTICE.md)

Contributors must have the right to submit their contribution.

## Authorship and Attribution

Material contributions should preserve clear authorship and provenance.

Authorship, editorial responsibility, review participation, and publication authority should be recorded separately where applicable.

A Git commit alone does not automatically establish publication authorship or editorial authority.

## Review

Review may include:

- editorial review;
- architectural review;
- technical review;
- normative review;
- security review;
- privacy review;
- implementation review;
- publication review.

Review findings should be specific, traceable, and linked to the affected material.

## Conduct

Contributors are expected to communicate respectfully, evaluate ideas on their technical and architectural merits, and avoid personal attacks, harassment, discrimination, or disruptive behavior.

A dedicated Code of Conduct may be introduced as the contributor community develops.

## Current Contribution Status

The AISET Program is currently in its initial foundation stage.

External contribution procedures, issue templates, pull request templates, and formal review processes will be introduced progressively.

## Program

**AISET Program**

Program Originator and Lead Editor: **Arkadiy Lazarev**