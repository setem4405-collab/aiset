# AISET Implementations

This directory contains reference implementations, implementation profiles, adapters, validation tools, test harnesses, and other software artifacts developed within the AISET Program.

AISET implementations are intended to demonstrate, test, and validate published AISET specifications without making any specific implementation technology normative.

## Purpose

The implementation layer exists to:

- demonstrate how AISET specifications may be implemented;
- validate architectural assumptions;
- test conformance requirements;
- compare independent implementations;
- support interoperability testing;
- provide examples for developers and organizations;
- identify gaps in specifications;
- produce reusable implementation guidance.

## Separation from Normative Specifications

AISET specifications define normative requirements.

AISET implementations are non-normative unless a publication explicitly states otherwise.

An implementation must not redefine the meaning of a normative AISET specification.

Where implementation behavior differs from a published specification, the specification takes precedence.

## Planned Implementation Categories

The AISET implementation framework may include:

- AISET Architecture Reference Implementation;
- Cognitive Context Object libraries;
- Cognitive Transformation runtimes;
- schema validators;
- registry validation tools;
- provenance and trust tooling;
- metric evaluation tools;
- compatibility test suites;
- interoperability test suites;
- conformance test harnesses;
- implementation adapters;
- command-line utilities;
- example applications.

## Reference Implementations

A reference implementation is intended to provide a transparent and testable example of how one or more AISET specifications may be implemented.

A reference implementation should:

- identify the specifications and versions it implements;
- document known limitations;
- include reproducible installation instructions;
- include validation and test procedures;
- avoid undocumented normative behavior;
- expose implementation-specific assumptions;
- include security considerations;
- identify its software license.

Reference implementations do not create exclusive or preferred implementation status.

Independent implementations may use different technologies while remaining compatible and conformant.

## Implementation Profiles

An implementation profile may define a technology-specific binding or deployment pattern for one or more AISET specifications.

Profiles may address:

- programming languages;
- serialization formats;
- APIs;
- databases;
- runtimes;
- orchestration systems;
- operating systems;
- hardware environments;
- deployment models.

A profile must clearly distinguish technology-specific choices from normative AISET requirements.

## Conformance Evidence

An implementation claiming conformance should provide, where applicable:

- the implemented specification identifier;
- the implemented specification version;
- the supported profile;
- validation results;
- test reports;
- known deviations;
- security considerations;
- interoperability evidence;
- release metadata;
- software license information.

## Testability

AISET implementations should be designed for independent testing.

Testable behavior may include:

- schema validation;
- invariant preservation;
- transformation input and output validation;
- provenance generation;
- metric calculation;
- compatibility checks;
- interoperability scenarios;
- failure handling;
- reproducibility.

## Current Implementation Status

No normative AISET reference implementation has yet been released.

The first planned implementation publication is:

- `ARI-0001` — AISET Architecture Reference Implementation.

Its software license will be selected before the first public code release.

## Relationship to Other Directories

- [Specifications](../specifications/README.md)
- [Schemas](../schemas/README.md)
- [Registry](../registry/README.md)
- [Governance](../governance/README.md)
- [Publications](../publications/README.md)

## Licensing

Software source code, executable implementations, libraries, validators, and related software artifacts are licensed separately from AISET publications and documentation.

Each software component must identify its applicable software license.

Until an explicit software license is assigned, a software component must not be treated as open-source software.

See:

- [Repository Licensing Notice](../LICENSE)
- [Software Licensing Notice](../LICENSES/SOFTWARE-LICENSE-NOTICE.md)

## Program

**AISET Program**

Program Originator and Lead Editor: **Arkadiy Lazarev**