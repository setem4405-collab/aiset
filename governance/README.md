# AISET Governance

This directory contains governance documents for the AISET Program.

AISET governance defines how publications, specifications, architectural records, registries, and reference implementations are proposed, reviewed, approved, published, revised, superseded, or withdrawn.

## Governance Scope

AISET governance applies to:

- reference publications;
- architecture reference documents;
- transformation specifications;
- registries and schemas;
- governance records;
- review records;
- reference implementations;
- publication metadata;
- versioning and release procedures.

## Governance Principles

AISET governance is based on the following principles:

1. Technology independence;
2. Transparent authorship and editorial responsibility;
3. Explicit publication status;
4. Reviewable change history;
5. Versioned and immutable releases;
6. Traceable approval records;
7. Clear licensing;
8. Publicly verifiable publication artifacts;
9. Separation between normative and informative material.

## Publication Lifecycle

AISET publications may pass through the following statuses:

1. **Draft**

   A work in active development.

2. **Review**

   A publication under editorial, architectural, technical, or public review.

3. **Candidate Publication**

   A stable document proposed for approval.

4. **Approved Publication**

   A publication formally approved for release.

5. **Reference Publication**

   An approved publication designated as a stable reference for the AISET Program.

6. **Superseded**

   A publication replaced by a newer approved version or publication.

7. **Withdrawn**

   A publication removed from active use while remaining available for historical traceability.

## Publication Requirements

An approved AISET publication should include, where applicable:

- a unique publication identifier;
- a title;
- a version;
- a publication status;
- a publication date;
- authorship and editorial records;
- publisher identification;
- licensing information;
- citation information;
- a release manifest;
- review records;
- a cryptographic checksum;
- a permanent release tag.

## Versioning

AISET publications use explicit version identifiers.

A versioned publication must not be silently modified after release.

Corrections or substantive changes require one of the following:

- a new patch version;
- a new minor version;
- a new major version;
- a formally documented replacement publication.

Published Git tags and release artifacts are treated as immutable records.

## Roles

### Program Originator

Defines the foundational direction, mission, and architectural intent of the AISET Program.

### Author

Creates the substantive content of a publication.

### Lead Editor

Maintains editorial consistency, structure, terminology, and publication quality.

### Reviewer

Evaluates a publication against its stated purpose, architectural requirements, and publication criteria.

### Publisher

Authorizes and records the official release of an AISET publication.

A single person may initially perform more than one role. Role separation may increase as the AISET Program develops.

## Normative and Informative Material

AISET documents should distinguish between:

- **Normative material**, which defines requirements, constraints, specifications, or conformance conditions;
- **Informative material**, which provides explanation, examples, context, interpretation, or implementation guidance.

Normative language should be used deliberately and consistently.

## Change Control

Changes to AISET governance documents must be:

- recorded in Git history;
- associated with a clear commit message;
- reviewed before publication where material;
- released under an explicit version when designated as normative.

## Current Governance Status

The AISET governance model is currently in its initial program formation stage.

This document establishes the baseline governance direction. More specific governance documents may later define:

- proposal procedures;
- review procedures;
- approval authority;
- voting or consensus mechanisms;
- publication identifiers;
- conformance rules;
- registry management;
- amendment procedures;
- dispute resolution;
- deprecation and withdrawal procedures.

## Licensing

Unless explicitly stated otherwise, AISET governance documents are licensed under the Creative Commons Attribution 4.0 International License.

See:

- [Repository Licensing Notice](../LICENSE)
- [CC BY 4.0 License Text](../LICENSES/CC-BY-4.0.txt)

## Program

**AISET Program**

Program Originator and Lead Editor: **Arkadiy Lazarev**