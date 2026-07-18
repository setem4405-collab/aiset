# AISET AI-Assisted Development Model

**Document Identifier:** AISET-AI-ASSISTED-DEVELOPMENT-MODEL-001

**Title:** AISET Multi-Model Development, Review, and Commit Authorization Model

**Project:** AISET CFS

**Document Type:** Engineering Governance and Development Process

**Status:** Established

**Version:** 0.1

**Date:** 19 July 2026

**Canonical Path:**

`governance/development/AISET-AI-ASSISTED-DEVELOPMENT-MODEL-001.md`

---

## 1. Purpose

This document establishes the initial AI-assisted development model for AISET.

The model defines:

- the roles of Claude Code, OpenAI Codex, and the human decision authority;
- task classification levels;
- implementation and review workflows;
- architecture-review escalation;
- commit authorization requirements;
- provenance and accountability expectations;
- restrictions on autonomous changes.

The purpose is to obtain the productivity benefits of multiple AI systems without transferring architectural, governance, or publication authority to those systems.

---

## 2. Core Decision

AISET adopts the following default development model:

> **Claude Code is the primary implementation and repository-aware engineering tool. OpenAI Codex is the independent architecture challenger and code reviewer. Arkadiy Lazarev is the human decision authority who approves architecture, reviews the final diff, and authorizes commits.**

For ordinary engineering work:

```text
Claude Code implementation
        ↓
OpenAI Codex independent review
        ↓
Arkadiy Lazarev final diff review and commit authorization
```

For architectural or critical work:

```text
OpenAI Codex independent architecture proposal
        ↓
Claude Code conformance review against AISET architecture
        ↓
Arkadiy Lazarev architecture decision
        ↓
Claude Code implementation
        ↓
OpenAI Codex implementation review
        ↓
Arkadiy Lazarev final diff review and commit authorization
```

---

## 3. Development Environment

The initial reference development environment is:

- Visual Studio Code as the primary IDE;
- Claude Code as the primary implementation tool;
- OpenAI Codex as the independent reviewer and architecture challenger;
- Git as the canonical version-control system;
- GitHub as the initial remote repository and collaboration platform.

GitHub Copilot may be used as an optional convenience layer for autocomplete or GitHub-native assistance.

Cursor may be used for comparative experiments but is not the canonical development environment.

All tools remain replaceable implementations.

---

## 4. Human Authority

AI systems may propose, analyze, implement, test, and review changes.

AI systems must not independently:

- approve architecture;
- authorize a commit;
- merge a protected change;
- alter normative governance;
- approve a publication;
- expand their own permissions;
- redefine task classification;
- suppress material findings;
- represent an AI-generated decision as a human decision.

Arkadiy Lazarev remains responsible for:

- approving the task objective;
- selecting or confirming the task class;
- resolving conflicts between AI recommendations;
- accepting or rejecting architectural proposals;
- reviewing the final diff;
- authorizing commit and push actions;
- escalating governance-sensitive work where required.

---

## 5. AI Tool Roles

### 5.1 Claude Code

Claude Code is the primary repository-aware implementation tool.

Its expected responsibilities include:

- reading relevant repository context;
- preparing implementation plans;
- creating and modifying files;
- performing multi-file refactoring;
- writing tests;
- executing validation commands;
- identifying affected documentation;
- preparing candidate diffs;
- addressing validated review findings;
- maintaining consistency with existing architecture.

Claude Code must treat AAR, CTSpec, CCO definitions, governance rules, security requirements, and repository conventions as constraints.

### 5.2 OpenAI Codex

OpenAI Codex is the independent architecture challenger and implementation reviewer.

Its expected responsibilities include:

- proposing independent architectural alternatives;
- challenging assumptions;
- reviewing diffs;
- detecting defects and omissions;
- identifying security and governance risks;
- checking tests and failure paths;
- evaluating maintainability;
- finding unnecessary vendor coupling;
- suggesting simpler or more portable designs.

Codex review must not be treated as automatic approval.

### 5.3 Human Decision Authority

The human decision authority evaluates evidence from both AI systems.

The human authority decides:

- which proposal is accepted;
- which findings are material;
- whether rework is required;
- whether the final change satisfies its acceptance criteria;
- whether a commit may be created;
- whether a push or merge may occur.

---

## 6. Task Classification

AISET uses three initial task classes.

### 6.1 L1 — Routine Change

Examples:

- spelling and formatting corrections;
- local documentation clarification;
- non-semantic metadata correction;
- isolated test adjustment;
- low-risk configuration cleanup;
- small change with no architectural or governance effect.

Default workflow:

```text
Claude Code or direct human edit
        ↓
Automated validation
        ↓
Arkadiy Lazarev review
        ↓
Commit authorization
```

A second AI review is optional unless risk is discovered.

### 6.2 L2 — Engineering Change

Examples:

- a new software module;
- validator functionality;
- parser or serializer;
- user-interface component;
- BPMN importer;
- CI workflow;
- schema tooling;
- non-trivial refactoring;
- security-relevant implementation without normative architecture change.

Default workflow:

```text
Arkadiy approves task and acceptance criteria
        ↓
Claude Code prepares plan
        ↓
Claude Code implements and tests
        ↓
OpenAI Codex independently reviews the diff
        ↓
Claude Code addresses accepted findings
        ↓
Arkadiy reviews the final diff
        ↓
Commit authorization
```

L2 is the default class for substantive engineering work.

### 6.3 L3 — Architectural or Critical Change

Examples:

- changes to CCO;
- changes to CTSpec;
- changes to Cognitive Contracts or invariants;
- new normative interface;
- governance architecture;
- trust and provenance architecture;
- security architecture;
- executor authority model;
- BPMN-to-CTSpec mapping;
- AISET semantic extension schema;
- lifecycle or approval logic;
- technology selection with long-term architectural consequences.

Default workflow:

```text
Arkadiy defines the problem and constraints
        ↓
OpenAI Codex proposes an independent architecture
        ↓
Claude Code checks conformance with AAR, CTSpec,
Technology Independence, governance, and repository context
        ↓
Claude Code produces a consolidated implementation plan
        ↓
Arkadiy approves, rejects, or revises the architecture
        ↓
Claude Code implements and tests
        ↓
OpenAI Codex independently reviews implementation
        ↓
Claude Code addresses accepted findings
        ↓
Arkadiy reviews the final diff
        ↓
Commit authorization
```

L3 changes may require additional human review, formal lifecycle records, or Approval Authority action where applicable.

---

## 7. Classification Rules

A task must be classified by its highest material risk.

A change is not L1 merely because it modifies only one file.

A change should be classified as L3 when it can materially affect:

- normative semantics;
- interoperability;
- authority;
- trust;
- provenance;
- security boundaries;
- lifecycle progression;
- conformance;
- technology independence;
- irreversible public commitments.

When classification is uncertain, the higher class should be used until the risk is clarified.

---

## 8. Architecture Challenge Principle

For L3 work, the first architecture proposal should preferably come from the AI system that will not be the primary implementer.

This creates separation between:

- proposal;
- conformance analysis;
- implementation;
- review;
- human authorization.

The objective is not to make one AI system authoritative over another.

The objective is to expose assumptions, alternatives, and contradictions before implementation begins.

---

## 9. Independent Review Principle

The reviewing AI must receive:

- the approved task description;
- acceptance criteria;
- relevant architecture constraints;
- the diff or changed files;
- test results;
- known limitations.

The reviewer should not merely confirm that the implementation appears plausible.

It should actively search for:

- incorrect assumptions;
- missing failure cases;
- architectural drift;
- hidden vendor dependency;
- governance bypass;
- insufficient validation;
- missing tests;
- unsafe defaults;
- excessive permissions;
- provenance gaps;
- inconsistencies with normative documents.

---

## 10. Finding Disposition

AI review findings should be classified as:

- Blocking;
- Major;
- Minor;
- Observation;
- Rejected with Reason;
- Deferred with Condition.

A finding is not resolved merely because the implementer disagrees with it.

Material disagreement should be presented to the human decision authority with:

- the finding;
- the implementer's response;
- supporting evidence;
- the remaining risk;
- the proposed disposition.

---

## 11. Commit Authorization

No AI-generated or AI-modified change is authorized for commit solely because:

- tests pass;
- one AI system reports success;
- two AI systems agree;
- the diff is small;
- the change was generated from an approved prompt.

Before commit authorization, the human decision authority should verify:

- the intended files changed;
- no unrelated files changed;
- acceptance criteria are satisfied;
- tests and validation passed;
- material findings are resolved or dispositioned;
- documentation is consistent;
- security and governance constraints are preserved;
- the commit message accurately describes the change.

The human decision authority may require additional review at any time.

---

## 12. Provenance

Development records should preserve, where practical:

- task identifier;
- task class;
- initiating human;
- primary implementation tool;
- independent review tool;
- approved architecture basis;
- relevant prompts or summarized instructions;
- test and validation results;
- review findings and dispositions;
- human commit authorization;
- resulting commit identifier.

Raw private conversations, secrets, credentials, and unnecessary personal data must not be committed.

---

## 13. Tool Independence

The roles in this document are functional roles.

Claude Code and OpenAI Codex are the initial implementations of:

- Primary Implementation Tool;
- Independent Architecture Challenger;
- Independent Implementation Reviewer.

They may be replaced by other conforming tools without changing the governance model.

A replacement must preserve:

- separation of implementation and review;
- repository-aware analysis;
- traceable findings;
- human authorization;
- technology independence.

---

## 14. Security Boundaries

AI development tools must operate under least privilege.

They must not be given unrestricted access to:

- production credentials;
- private keys;
- financial accounts;
- publication authority;
- repository administration;
- protected branches;
- deployment secrets;
- personal correspondence;
- governance evidence not required for the task.

Destructive commands, credential changes, publication actions, and irreversible operations require explicit human authorization.

---

## 15. Relationship to AISET Architecture

This development model supports:

- Technology Independence;
- Cognitive Trust and Provenance;
- Cognitive Contracts;
- governance-aware execution;
- separation of duties;
- human escalation;
- replaceable executors;
- measurement and evaluation;
- controlled Shared Cognitive Evolution.

AI tools are treated as replaceable executors of governed development transformations.

They are not normative authorities.

---

## 16. Initial Operational Rule

The initial operational rule is:

> **L1 uses human-controlled lightweight review. L2 uses Claude Code implementation, Codex independent review, and human commit authorization. L3 adds independent architecture proposal and conformance review before implementation, followed by independent implementation review and human commit authorization.**

This rule may be refined through a future engineering governance specification.

---

## 17. Current Status

**Model Status:** Established

**Primary IDE:** Visual Studio Code

**Primary Implementation Tool:** Claude Code

**Independent Reviewer:** OpenAI Codex

**Human Decision Authority:** Arkadiy Lazarev

**Default Engineering Class:** L2

**Architectural and Critical Class:** L3

**Commit Authorization:** Human Required

---

## 18. Non-Goals

This model does not:

- make AI output authoritative;
- guarantee correctness;
- replace security review;
- replace governance review;
- replace publication approval;
- require two AI systems for every trivial edit;
- prevent use of additional tools;
- bind AISET permanently to Anthropic, OpenAI, Microsoft, or GitHub.

---

## 19. License

This document is licensed under the Creative Commons Attribution 4.0 International License.

See:

- `LICENSE`
- `LICENSES/CC-BY-4.0.txt`
