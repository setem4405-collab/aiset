# AISET Schemas

This directory contains machine-readable schemas used to validate AISET registry records, Cognitive Context Objects, transformation specifications, provenance records, conformance claims, and related structured artifacts.

## Purpose

AISET schemas provide implementation-independent validation rules for structured data used across the AISET Program.

Schemas are intended to support:

- structural validation;
- semantic consistency;
- version compatibility;
- registry integrity;
- provenance verification;
- conformance testing;
- automated tooling;
- interoperability between independent implementations.

## Planned Schema Families

The AISET schema framework is expected to include:

- Cognitive Context Object schemas;
- Cognitive Transformation Specification schemas;
- Cognitive Invariant schemas;
- Cognitive Interface Specification schemas;
- registry record schemas;
- publication metadata schemas;
- provenance and trust record schemas;
- metric definition schemas;
- conformance claim schemas;
- implementation profile schemas;
- compatibility and interoperability profile schemas.

## Schema Formats

AISET schemas may use open and documented formats such as:

- JSON Schema;
- YAML-based schema definitions;
- XML Schema where required;
- protocol-neutral interface definitions;
- other technology-independent validation formats approved by the AISET governance process.

A schema format must not introduce unnecessary dependence on a specific vendor, runtime, programming language, or implementation framework.

## Schema Requirements

An AISET schema should include, where applicable:

- a unique identifier;
- a schema version;
- a status;
- a title and description;
- required fields;
- optional fields;
- type definitions;
- enumerations;
- constraints;
- validation rules;
- extension rules;
- compatibility expectations;
- examples;
- change history;
- licensing information.

## Versioning

Schema versions must be explicit.

A released schema must not be silently modified in a way that changes validation behavior.

Changes should be classified as:

- backward-compatible;
- conditionally compatible;
- breaking;
- editorial or non-semantic.

Breaking changes require a new schema version.

## Compatibility

A newer schema version should preserve compatibility where practical.

Compatibility claims should identify:

- the source schema version;
- the target schema version;
- compatible fields;
- deprecated fields;
- transformed fields;
- incompatible constraints;
- required migration behavior.

## Extensions

AISET schemas may permit controlled extensions.

Extension mechanisms should:

- preserve validation of required normative fields;
- avoid collisions with registered identifiers;
- identify extension ownership;
- distinguish normative and implementation-specific data;
- remain removable without corrupting the canonical AISET object.

## Validation

Schema validation may include:

1. syntactic validation;
2. structural validation;
3. type validation;
4. constraint validation;
5. semantic validation;
6. invariant validation;
7. provenance validation;
8. compatibility validation.

Passing syntactic validation alone does not necessarily establish full AISET conformance.

## Current Schema Status

No normative AISET schema has yet been released.

The current machine-readable publication registry record is:

- [DISCOVERY-0001.yaml](../publications/DISCOVERY-0001/registry/DISCOVERY-0001.yaml)

A formal registry record schema will be introduced in a future AISET specification.

## Relationship to Other Directories

- [Registry](../registry/README.md)
- [Specifications](../specifications/README.md)
- [Publications](../publications/README.md)
- [Governance](../governance/README.md)

## Licensing

Unless explicitly stated otherwise, AISET schemas and related non-software materials are licensed under the Creative Commons Attribution 4.0 International License.

Executable validators, generators, libraries, and schema-processing tools are software components and must use a separately identified software license.

See:

- [Repository Licensing Notice](../LICENSE)
- [CC BY 4.0 License Text](../LICENSES/CC-BY-4.0.txt)
- [Software Licensing Notice](../LICENSES/SOFTWARE-LICENSE-NOTICE.md)

## Program

**AISET Program**

Program Originator and Lead Editor: **Arkadiy Lazarev**