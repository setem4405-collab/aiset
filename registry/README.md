# AISET Registry

This directory contains registries of approved AISET publications, specifications, identifiers, schemas, transformation definitions, and other governed normative objects.

The AISET Registry provides stable identifiers, publication metadata, version references, status information, and links to canonical artifacts.

## Purpose

The registry exists to support:

- stable identification;
- version traceability;
- publication discovery;
- compatibility assessment;
- interoperability;
- provenance verification;
- conformance claims;
- lifecycle management;
- supersession and withdrawal records.

## Registry Principles

AISET registries are governed by the following principles:

1. Every registered object has a unique identifier.
2. Every registered version is explicit.
3. Published records are traceable to canonical artifacts.
4. Status changes are recorded.
5. Released versions are not silently modified.
6. Superseded and withdrawn records remain historically discoverable.
7. Registry records are technology-independent.
8. Machine-readable and human-readable representations should remain consistent.

## Registry Scope

The AISET Registry may contain records for:

- publications;
- architecture reference documents;
- Cognitive Transformation Specifications;
- Cognitive Context Object schemas;
- Cognitive Interface Specifications;
- Cognitive Invariant definitions;
- Cognitive Metrics;
- trust and provenance profiles;
- compatibility profiles;
- interoperability profiles;
- implementation profiles;
- reference implementations;
- governance documents;
- conformance records.

## Identifier Structure

AISET identifiers should be:

- unique;
- stable;
- human-readable where practical;
- independent of implementation technology;
- suitable for use in filenames, registries, citations, and machine-readable metadata.

Current identifier examples include:

- `DISCOVERY-0001`;
- `PROGRAM-0001`;
- `AAR-0001`;
- `ARI-0001`.

Future specification identifiers may use dedicated prefixes defined by the AISET governance process.

## Registry Record Requirements

A registry record should include, where applicable:

- identifier;
- title;
- object type;
- version;
- status;
- publication date;
- canonical path;
- release tag;
- authorship;
- publisher;
- licensing information;
- checksum;
- supersedes;
- superseded by;
- related objects;
- machine-readable metadata location.

## Current Registered Publications

| Identifier | Title | Version | Status | Canonical Record |
|---|---|---:|---|---|
| `DISCOVERY-0001` | AISET Discovery | 1.0 | Reference Publication | [Registry record](../publications/DISCOVERY-0001/registry/DISCOVERY-0001.yaml) |

## Machine-Readable Records

Machine-readable registry records should use open, documented formats such as YAML or JSON.

The current machine-readable record is:

- [DISCOVERY-0001.yaml](../publications/DISCOVERY-0001/registry/DISCOVERY-0001.yaml)

Schemas for registry validation will be introduced as the AISET schema framework develops.

## Lifecycle

Registry records may use the following statuses:

1. Draft;
2. Review;
3. Candidate;
4. Approved;
5. Reference;
6. Superseded;
7. Withdrawn.

Status terminology may be specialized for particular object types.

## Immutability and Corrections

A published registry record must not be silently rewritten in a way that changes the meaning of a released version.

Corrections should be handled through:

- a new version;
- an amendment record;
- a correction notice;
- a superseding record;
- an explicitly documented metadata correction.

## Relationship to Other Directories

- [Publications](../publications/README.md)
- [Specifications](../specifications/README.md)
- [Governance](../governance/README.md)
- [Repository Licensing Notice](../LICENSE)

## Licensing

Unless explicitly stated otherwise, AISET registry records and related non-software materials are licensed under the Creative Commons Attribution 4.0 International License.

See:

- [Repository Licensing Notice](../LICENSE)
- [CC BY 4.0 License Text](../LICENSES/CC-BY-4.0.txt)

## Program

**AISET Program**

Program Originator and Lead Editor: **Arkadiy Lazarev**