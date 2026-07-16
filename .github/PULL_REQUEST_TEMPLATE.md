# Pull Request

## Summary

Provide a concise description of the proposed change.

## Change Type

Select all that apply:

- [ ] Editorial documentation change
- [ ] Architectural change
- [ ] Normative specification change
- [ ] Governance change
- [ ] Registry change
- [ ] Schema change
- [ ] Implementation change
- [ ] Test or validation change
- [ ] Licensing change
- [ ] Release or publication change
- [ ] Other

## Affected Areas

Identify the affected files, directories, publications, specifications, schemas, registry records, or implementations.

## Purpose

Explain the problem being addressed and why this change is needed.

## Normative Impact

Does this pull request change normative meaning?

- [ ] No, editorial or informative only
- [ ] Yes
- [ ] Uncertain; normative review required

If yes or uncertain, describe the affected requirements, constraints, invariants, interfaces, validation rules, or conformance conditions.

## Technology Independence

Confirm that the change does not introduce unnecessary dependence on a specific:

- vendor;
- model;
- programming language;
- runtime;
- database;
- orchestration framework;
- operating system;
- hardware platform;
- implementation technology.

Describe any technology-specific elements and explain why they are placed in an implementation profile, binding, adapter, example, or reference implementation.

## Compatibility Impact

Describe any backward compatibility, version compatibility, migration, or deprecation implications.

## Interoperability Impact

Describe how the change affects interoperability between independent implementations.

## Security and Privacy

Describe any relevant:

- security implications;
- privacy implications;
- trust assumptions;
- provenance requirements;
- abuse cases;
- failure modes.

Use the private reporting process described in [SECURITY.md](../SECURITY.md) for exploitable vulnerabilities.

## Authorship and Provenance

Identify the author or authors of the substantive contribution.

Describe any source material, prior work, automated assistance, generated content, or external dependencies used in preparing the change.

The submitter remains responsible for accuracy, provenance, licensing, and compliance.

## Licensing

Confirm that:

- [ ] I have the right to submit this contribution.
- [ ] Non-software material is compatible with the repository documentation license.
- [ ] Software material identifies an applicable software license.
- [ ] Third-party material and dependencies are properly identified.
- [ ] No confidential, proprietary, or unlawfully copied material is included.

## Validation

Describe how the change was reviewed, tested, measured, or validated.

Include relevant commands, results, checksums, test reports, or review records.

## Required Checks

Before submission:

- [ ] I reviewed the changed files.
- [ ] I ran `git diff --check`.
- [ ] I ran `git diff --cached --check` before committing.
- [ ] Markdown links and relative paths were checked.
- [ ] Released artifacts were not silently modified.
- [ ] Version, status, and checksum records were updated where required.
- [ ] Normative and informative material are clearly distinguished.
- [ ] The change is focused and does not include unrelated modifications.

## Publication and Release Impact

Does this pull request affect a released publication or release artifact?

- [ ] No
- [ ] Yes

If yes, identify the required:

- new version;
- correction notice;
- amendment;
- updated release manifest;
- updated checksum;
- updated review record;
- new Git tag;
- new GitHub Release.

Published tags and release artifacts must not be silently replaced.

## Related Material

Reference related issues, proposals, publications, specifications, registry records, reviews, or pull requests.

Examples:

```text
Closes #123
Related to DISCOVERY-0001
Implements AAR-0001 section X
```

## Reviewer Notes

Highlight areas requiring particular editorial, architectural, normative, security, licensing, or implementation review.