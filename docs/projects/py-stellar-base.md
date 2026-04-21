---
title: "py-stellar-base"
parent: Public Good Projects
proposal_issue: 55
proposer: overcat
category: "SDKs"
budget: "15000"
---

# py-stellar-base

_The Python Stellar SDK provides APIs to build transactions, query Horizon, and interact with Soroban
RPC, with implementations of several Stellar Ecosystem Proposals._

|                      |                                                |
| -------------------- | ---------------------------------------------- |
| **Category**         | SDKs                                           |
| **Website**          | <https://stellar-sdk.readthedocs.io>           |
| **Repository**       | <https://github.com/StellarCN/py-stellar-base> |
| **First Released**   | October 2016                                   |
| **Intake**           | soft-launch                                    |
| **Budget Requested** | 15000                                          |

## Project Description

py-stellar-base is a Python library for building Stellar applications. It provides transaction
building, Horizon API access, Soroban RPC support, high-level Soroban smart contract support, and
implements several Stellar Ecosystem Proposals. The SDK is distributed via PyPI (`stellar-sdk`) and
listed on the official Stellar developer documentation.

py-stellar-base is one of the most popular SDKs in the Stellar ecosystem, used by organizations
including SDF, Lobstr, and Trezor. Its accessibility makes it a common first choice for developers
new to Stellar, lowering the barrier to entry for the broader ecosystem.

## Team & Experience

overcat (GitHub: [overcat](https://github.com/overcat), Discord: @overcat.me) has been active in the
Stellar community since 2018 and has rich experience in Stellar-related development, maintaining a
series of Stellar infrastructure software. Currently maintained Stellar-related projects are listed
at https://lightsail.network.

## Retroactive Impact

In Q1 2026, all planned deliverables were completed. The SDK shipped 1 release (13.2.1) fixing a
community-reported bug in cursor-based pagination. A dedicated security hardening pass addressed
multiple XDR decoding vulnerabilities and response-size-based DoS vectors. The XDR code generator was
migrated from `xdrgen` into the SDK and substantially refactored. SEP-51 (XDR-JSON) support was
implemented and validated against the Rust Stellar CLI. `to_map` was updated to automatically sort
`ScMap` keys per Soroban runtime rules.

## Past Deliverables

### 1. Ongoing SDK Maintenance

Description from last quarter:

> This deliverable covers all necessary improvements to ensure the SDK's long-term viability. It
> includes resolving defects, implementing new features, refining code quality, and increasing test
> coverage to guarantee the SDK remains a robust and dependable tool for developers.

Proof of completion:

- Release 13.2.1: https://github.com/StellarCN/py-stellar-base/releases/tag/13.2.1
- Pending Release: https://github.com/StellarCN/py-stellar-base/blob/main/CHANGELOG.md#pending

One release shipped alongside a dedicated security hardening pass: a comprehensive audit was applied
across the codebase, fixing response-size-based DoS vectors in federation and TOML fetching, XDR
decoding stack overflow vulnerabilities, and multiple input validation issues. Further XDR generator
security fixes are included in the pending release.

### 2. Add Support for SEP-51

Description from last quarter:

> Add support for
> [SEP-51](https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0051.md), enabling
> developers to serialize XDR data into JSON. This simplifies integration with web services and
> tooling, improves developer experience, and promotes consistent behavior across applications in the
> Stellar ecosystem.

Proof of completion:

- PR #1134: https://github.com/StellarCN/py-stellar-base/pull/1134 — SEP-51 XDR-JSON support added to
  XDR generator
- PR #1139: https://github.com/StellarCN/py-stellar-base/pull/1139 — XDR JSON unit tests
- PR #1140: https://github.com/StellarCN/py-stellar-base/pull/1140 — Test verifying Python XDR-JSON
  output against Rust Stellar CLI

SEP-51 support was added to the XDR generator, so all generated XDR types automatically gain
`to_xdr_json()` / `from_xdr_json()` methods. Output was cross-validated against the Rust Stellar CLI
as a reference implementation.

### 3. xdrgen Migration and Refactoring

Description from last quarter:

> Migrate xdrgen into a dedicated repository and perform necessary refactoring to improve
> maintainability and long-term sustainability of the SDK's tooling. This will strengthen the build
> pipeline and make future protocol upgrades easier to support. ref:
> https://github.com/orgs/stellar/discussions/1738

Proof of completion:

- PR #1113: https://github.com/StellarCN/py-stellar-base/pull/1113 — Migrate Python XDR generator
  from xdrgen into the SDK
- PR #1123: https://github.com/StellarCN/py-stellar-base/pull/1123 — XDR generator refactoring
- PR #1125: https://github.com/StellarCN/py-stellar-base/pull/1125 — XDR generator optimizations
- PR #1129: https://github.com/StellarCN/py-stellar-base/pull/1129 — XDR generator fixes

The XDR code generator was migrated from the external `xdrgen` tool into the SDK repository and
substantially refactored, giving full control over the generated Python code. Snapshot tests were
added to CI so any unintended output changes are caught automatically on future regeneration runs.
During the refactoring, several latent security issues in the generated XDR encoding/decoding code
were identified and fixed.

### 4. Improve the scval Build Feature

Description from last quarter:

> Currently, when building a map, we require users to manually sort the keys. Enhance the scval build
> functionality to automatically sort the keys of the map, thereby simplifying the developer
> experience and reducing potential sources of errors.

Proof of completion:

- PR #1141: https://github.com/StellarCN/py-stellar-base/pull/1141 — Sort ScMap entries by key in
  `to_map` per Soroban runtime ordering rules

`to_map` now automatically sorts entries by key, matching the Soroban runtime's requirement that
`ScMap` keys be in ascending order. This eliminates a class of transaction failures that occurred
when users provided unsorted maps.

## Proposed Impact

The primary goals for Q2 2026 are: achieve full Protocol 26 compatibility; implement SEP-46, SEP-47,
and SEP-48 to improve Soroban smart contract tooling interoperability; and publish an AI coding agent
skill to help developers build on Stellar more effectively. Ongoing maintenance will continue:
responding to community issues and pull requests, keeping dependencies and CI/CD pipelines current.

## Proposed Deliverables

### 1. Continuous Maintenance and Improvement

Regular SDK updates addressing Horizon, Soroban RPC, and protocol changes (including Protocol 26),
bug fixes, feature requests, and documentation updates. Keep CI/CD pipelines, SBOM workflow, and
dependency updates current.

Proof: Release notes on GitHub, updated CHANGELOG, passing CI on main.

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

Publish an AI coding agent skill for py-stellar-base following the agentskills.io open standard,
compatible with Claude Code, Codex CLI, Cursor, Gemini CLI, and others. The skill provides
token-efficient documentation and best practices for AI-assisted development with the SDK, lowering
the barrier for developers using AI tools to build on Stellar.

Proof: Skill available in the SDK repository, compatible with Claude Code, Codex CLI, Cursor, Gemini
CLI, and others.

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
