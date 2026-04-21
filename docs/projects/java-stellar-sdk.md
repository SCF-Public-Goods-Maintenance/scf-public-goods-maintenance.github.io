---
title: "java-stellar-sdk"
parent: Public Good Projects
proposal_issue: 53
proposer: overcat
category: "SDKs"
budget: "15000"
---

# java-stellar-sdk

_The Java Stellar SDK provides APIs to build transactions, query Horizon, and interact with Soroban
RPC, with Android support and implementations of several Stellar Ecosystem Proposals._

|                      |                                                         |
| -------------------- | ------------------------------------------------------- |
| **Category**         | SDKs                                                    |
| **Website**          | <https://github.com/lightsail-network/java-stellar-sdk> |
| **Repository**       | <https://github.com/lightsail-network/java-stellar-sdk> |
| **First Released**   | November 2015                                           |
| **Intake**           | soft-launch                                             |
| **Budget Requested** | 15000                                                   |

## Project Description

The Java Stellar SDK is a Java library for building Stellar applications on server-side JVM runtimes
and Android. It provides transaction building, Horizon API access, Soroban RPC support, high-level
Soroban smart contract support, and implements several Stellar Ecosystem Proposals. The SDK is listed
on the official Stellar developer documentation and is used by projects including Lobstr Vault,
[Stellar Anchor Platform](https://github.com/stellar/anchor-platform), and others.

## Team & Experience

overcat (GitHub: [overcat](https://github.com/overcat), Discord: @overcat.me) has been active in the
Stellar community since 2018 and has rich experience in Stellar-related development, maintaining a
series of Stellar infrastructure software. Currently maintained Stellar-related projects are listed
at https://lightsail.network.

## Retroactive Impact

In Q1 2026, all planned deliverables were completed. The SDK shipped 3 releases (2.2.1 through
2.2.3), including a dedicated security hardening release (2.2.2) addressing XDR decoding
vulnerabilities and Federation client DoS vectors. The XDR code generator was migrated from `xdrgen`
into the SDK and substantially refactored. SEP-51 (XDR-JSON) support was implemented and validated
against the Rust Stellar CLI. `ScMap` key ordering was fixed to automatically follow Soroban runtime
rules.

## Past Deliverables

### 1. Ongoing SDK Maintenance

Description from last quarter:

> This deliverable covers all necessary improvements to ensure the SDK's long-term viability. It
> includes resolving defects, implementing new features, refining code quality, and increasing test
> coverage to guarantee the SDK remains a robust and dependable tool for developers.

Proof of completion:

- Release 2.2.1: https://github.com/lightsail-network/java-stellar-sdk/releases/tag/2.2.1
- Release 2.2.2: https://github.com/lightsail-network/java-stellar-sdk/releases/tag/2.2.2
- Release 2.2.3: https://github.com/lightsail-network/java-stellar-sdk/releases/tag/2.2.3

Three releases shipped. Release 2.2.2 was a dedicated security hardening release: a comprehensive
audit was applied across the codebase, fixing XDR decoding vulnerabilities, Federation client DoS
vectors, and multiple input validation and thread-safety issues.

### 2. Add Support for SEP-51

Description from last quarter:

> Add support for
> [SEP-51](https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0051.md), enabling
> developers to serialize XDR data into JSON. This simplifies integration with web services and
> tooling, improves developer experience, and promotes consistent behavior across applications in the
> Stellar ecosystem.

Proof of completion:

- PR #774: https://github.com/lightsail-network/java-stellar-sdk/pull/774 — SEP-51 support added to
  XDR generator
- PR #777: https://github.com/lightsail-network/java-stellar-sdk/pull/777 — Test verifying XDR-JSON
  output against Rust Stellar CLI
- PR #778: https://github.com/lightsail-network/java-stellar-sdk/pull/778 — Unit tests for SEP-51

SEP-51 support was added to the XDR generator, so all generated XDR types automatically gain
`toJson()` / `fromJson()` methods. Output was cross-validated against the Rust Stellar CLI as a
reference implementation.

### 3. xdrgen Migration and Refactoring

Description from last quarter:

> Migrate xdrgen into a dedicated repository and perform necessary refactoring to improve
> maintainability and long-term sustainability of the SDK's tooling. This will strengthen the build
> pipeline and make future protocol upgrades easier to support. ref:
> https://github.com/orgs/stellar/discussions/1738

Proof of completion:

- PR #762: https://github.com/lightsail-network/java-stellar-sdk/pull/762 — Migrate XDR generator
  from xdrgen into the SDK
- PR #767: https://github.com/lightsail-network/java-stellar-sdk/pull/767 — XDR generator snapshot
  tests

The XDR code generator was migrated from the external `xdrgen` tool into the SDK repository and
substantially refactored, giving full control over the generated Java code. Snapshot tests were added
to CI so any unintended output changes are caught automatically on future regeneration runs. During
the refactoring, several latent security issues in the generated XDR encoding/decoding code were
identified and fixed.

### 4. Improve the scval Build Feature

Description from last quarter:

> Currently, when building a map, we require users to manually sort the keys. Enhance the scval build
> functionality to automatically sort the keys of the map, thereby simplifying the developer
> experience and reducing potential sources of errors.

Proof of completion:

- PR #766: https://github.com/lightsail-network/java-stellar-sdk/pull/766 — Sort ScMap entries by key
  in Scv.toMap per Soroban runtime ordering rules

`Scv.toMap` now automatically sorts map entries by key, matching the Soroban runtime's requirement
that `ScMap` keys be in ascending order. The previous `toMap(LinkedHashMap<SCVal, SCVal>)` overload
is deprecated. This eliminates a class of transaction failures that occurred when users provided
unsorted maps.

## Proposed Impact

The primary goals for Q2 2026 are: achieve full Protocol 26 compatibility; implement SEP-46, SEP-47,
and SEP-48 to improve Soroban smart contract tooling interoperability; and publish an AI coding agent
skill to help developers build on Stellar more effectively. Ongoing maintenance will continue:
responding to community issues and pull requests, keeping dependencies and CI/CD pipelines current.

## Proposed Deliverables

### 1. Continuous Maintenance and Improvement

Regular SDK updates addressing Horizon, Soroban RPC, and protocol changes (including Protocol 26),
bug fixes, feature requests, and documentation updates. Keep CI/CD pipelines and dependency updates
current.

Proof: Release notes on GitHub, updated CHANGELOG, passing CI on master.

### 2. SEP-46, SEP-47, and SEP-48 Support

Add support for SEP-46 (Contract Meta), SEP-47 (Contract Interface Discovery), and SEP-48 (Contract
Interface Specification). These three SEPs form the foundation for smart contract self-description:
SEP-46 defines how contracts embed metadata in Wasm custom sections, SEP-47 lets contracts declare
which SEPs they implement, and SEP-48 provides a rich interface specification including Soroban host
types, user-defined types, and event schemas. Together they enable the SDK to parse and expose
contract metadata, which is essential for tooling, auto-generated contract clients, and off-chain
systems that need to understand contract interfaces.

Proof: Release on GitHub, PRs with implementation and tests, documentation.

### 3. AI Coding Agent Skill

Publish an AI coding agent skill for the java-stellar-sdk following the agentskills.io open standard,
compatible with Claude Code, Codex CLI, Cursor, Gemini CLI, and others. The skill provides
token-efficient documentation and best practices for AI-assisted development with the SDK, lowering
the barrier for developers using AI tools to build on Stellar.

Proof: Skill available in the SDK repository, compatible with Claude Code, Codex CLI, Cursor, Gemini
CLI, and others.

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
