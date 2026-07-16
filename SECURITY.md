# AISET Security Policy

## Purpose

The AISET Program is committed to responsible security practices across its publications, specifications, schemas, registries, reference implementations, tooling, and supporting infrastructure.

This policy establishes the baseline process for reporting potential security issues.

## Scope

Security reports may relate to:

- source code;
- reference implementations;
- validation tools;
- schemas;
- registry tooling;
- automation workflows;
- build and release processes;
- dependency vulnerabilities;
- credential exposure;
- provenance failures;
- integrity issues;
- unsafe implementation guidance;
- security-relevant specification defects.

Documentation-only editorial issues should normally be reported through the standard contribution process rather than this security policy.

## Supported Versions

The AISET Program is currently in its initial foundation stage.

No production software implementation has yet been released.

Security support will be defined for each future software component and release.

Published documentation and release artifacts remain available for historical traceability, but only explicitly supported versions should be assumed to receive security updates.

## Reporting a Vulnerability

Do not publicly disclose a potential vulnerability before the AISET Program has had a reasonable opportunity to investigate and respond.

A security report should include, where practical:

- the affected file, component, or version;
- a clear description of the issue;
- steps to reproduce;
- expected and actual behavior;
- potential impact;
- proof-of-concept information;
- suggested mitigation;
- whether the issue has already been disclosed elsewhere.

Do not include passwords, private keys, access tokens, personal data, or other sensitive information unless strictly necessary.

## Current Reporting Channel

A dedicated private security reporting channel has not yet been established.

Until a private reporting channel is published, avoid posting exploit details in public issues.

A reporter may initially provide a minimal public notice stating that a potential security issue exists and request a private contact method, without disclosing technical details.

The repository will adopt a dedicated private reporting process before public production software is released.

## Responsible Disclosure

Reporters are expected to:

- act in good faith;
- avoid privacy violations;
- avoid destruction or alteration of data;
- avoid service disruption;
- avoid accessing more information than necessary;
- allow reasonable time for investigation and remediation;
- avoid public disclosure before coordination.

The AISET Program will make reasonable efforts to:

- acknowledge valid reports;
- investigate reported issues;
- assess severity and impact;
- communicate remediation status;
- credit reporters where appropriate and permitted;
- publish correction or advisory information when necessary.

## Out of Scope

The following are generally out of scope unless they demonstrate a concrete security impact:

- unsupported software or obsolete versions;
- purely theoretical issues without a practical impact;
- social engineering against contributors;
- denial-of-service testing that disrupts services;
- automated scans without meaningful validation;
- missing security headers on non-production informational pages;
- typographical or editorial errors;
- reports requiring access to stolen credentials;
- third-party services not controlled by the AISET Program.

## Security in Specifications

Security-relevant specification contributions should identify:

- assets being protected;
- threat assumptions;
- trust boundaries;
- authentication and authorization considerations;
- integrity requirements;
- confidentiality requirements;
- provenance requirements;
- failure modes;
- abuse cases;
- implementation risks.

A specification must not imply that conformance alone guarantees security.

## Security in Implementations

Software components should document, where applicable:

- supported versions;
- dependencies;
- secure configuration;
- secrets handling;
- update procedures;
- logging and audit behavior;
- input validation;
- failure handling;
- known limitations;
- vulnerability reporting instructions.

Each implementation may provide a more specific security policy that takes precedence for that component.

## Release Integrity

AISET releases should use verifiable publication and release practices, including where applicable:

- immutable Git tags;
- release manifests;
- cryptographic checksums;
- authorship and provenance records;
- review records;
- explicit versioning;
- documented correction procedures.

Released artifacts must not be silently replaced.

## Security Advisories and Corrections

A confirmed issue may require one or more of the following:

- a security advisory;
- a corrected release;
- a new version;
- a checksum update for a new artifact;
- a correction notice;
- a superseding publication;
- an implementation patch;
- a registry status update.

Historical records should remain traceable.

## Safe Harbor

Good-faith security research conducted consistently with this policy should not be treated as malicious activity by the AISET Program.

This statement does not authorize violations of applicable law, access to third-party systems, privacy violations, data destruction, or service disruption.

## Current Status

This document establishes the initial AISET security reporting baseline.

A dedicated private reporting address, severity model, response targets, and advisory process will be introduced before the first public production software release.

## Licensing

This Security Policy is an AISET non-software document and is licensed under the Creative Commons Attribution 4.0 International License unless explicitly stated otherwise.

See:

- [Repository Licensing Notice](LICENSE)
- [CC BY 4.0 License Text](LICENSES/CC-BY-4.0.txt)

## Program

**AISET Program**

Program Originator and Lead Editor: **Arkadiy Lazarev**