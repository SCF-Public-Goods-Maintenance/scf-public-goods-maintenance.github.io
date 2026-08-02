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

In Q2 2026, all three planned deliverables were completed, and protocol work went beyond the plan.
The SDK shipped three stable releases (14.0.0 through 14.1.1). Support for the smart-contract
self-description SEPs (SEP-46, SEP-47, SEP-48) and an AI coding agent skill both landed in 14.1.0.
`stellar_sdk.auth` was redesigned so any account contract can authorize Soroban entries, and the
generated XDR was advanced from the planned Protocol 26 to Protocol 27, with CAP-71 Soroban
authorization support implemented in the 15.0.0-beta0 pre-release. Alongside features, the toolchain
was modernized, migration to ruff, parallelized CI, and network-free test mocks, and dependencies
kept current.

## Past Deliverables

### 1. Continuous Maintenance and Improvement

Description from last quarter:

> Regular SDK updates addressing Horizon, Soroban RPC, and protocol changes (including Protocol 26),
> bug fixes, feature requests, and documentation updates. Keep CI/CD pipelines, SBOM workflow, and
> dependency updates current.

Proof of completion:

- Release 14.0.0: https://github.com/StellarCN/py-stellar-base/releases/tag/14.0.0
- Release 14.1.0: https://github.com/StellarCN/py-stellar-base/releases/tag/14.1.0
- Release 14.1.1: https://github.com/StellarCN/py-stellar-base/releases/tag/14.1.1
- Pre-release 15.0.0-beta0: https://github.com/StellarCN/py-stellar-base/releases/tag/15.0.0-beta0

Some notable PR, not exhaustive:

- PR #1189: https://github.com/StellarCN/py-stellar-base/pull/1189 — feat: add CAP-71 (Protocol 27)
  Soroban authorization support
- PR #1199: https://github.com/StellarCN/py-stellar-base/pull/1199 — test: migrate from aioresponses
  to aiointercept for aiohttp 3.14 support
- PR #1188: https://github.com/StellarCN/py-stellar-base/pull/1188 — feat: add simulateTransaction
  authV2 flag
- PR #1177: https://github.com/StellarCN/py-stellar-base/pull/1177 — Migrate to ruff, PR 2
- PR #1176: https://github.com/StellarCN/py-stellar-base/pull/1176 — Migrate to ruff, PR 1
- PR #1172: https://github.com/StellarCN/py-stellar-base/pull/1172 — test: replace real network
  requests with local httpserver mocks
- PR #1167: https://github.com/StellarCN/py-stellar-base/pull/1167 — test: use local httpbin fixture
  in tests
- PR #1162: https://github.com/StellarCN/py-stellar-base/pull/1162 — feat: improve
  stellar_sdk.contract.AssembledTransaction authorization lifecycle for contract account
  authorization
- PR #1160: https://github.com/StellarCN/py-stellar-base/pull/1160 — feat!: redesign stellar_sdk.auth
  so any account contract can authorize Soroban entries
- View all 37 merged PRs (Q2 2026):
  https://github.com/StellarCN/py-stellar-base/pulls?q=is%3Apr+is%3Amerged+merged%3A2026-04-01..2026-06-30

Three stable releases shipped. The generated XDR was upgraded to Protocol 26 and then to Protocol 27,
exceeding the planned Protocol 26 target. `stellar_sdk.auth` was redesigned so any account contract
(default Stellar account, BLS, WebAuthn, threshold, etc.) can authorize Soroban entries, and CAP-71
Protocol 27 Soroban authorization — including the new address-bound and delegated credential types —
was implemented across the high-level API. This work currently ships in the 15.0.0-beta0 pre-release
rather than a stable release: Protocol 27 is not yet broadly available in real-world test
environments, so the stable 15.0.0 is intentionally held until the implementation can be validated
against a live Protocol 27 network. The toolchain was also modernized with a migration to ruff,
parallelized CI, and network-free test mocks, alongside numerous bug fixes and dependency updates.

### 2. SEP-46, SEP-47, and SEP-48 Support

Description from last quarter:

> Add support for SEP-46 (Contract Meta), SEP-47 (Contract Interface Discovery), and SEP-48 (Contract
> Interface Specification). These three SEPs form the foundation for smart contract self-description:
> SEP-46 defines how contracts embed metadata in Wasm custom sections, SEP-47 lets contracts declare
> which SEPs they implement, and SEP-48 provides a rich interface specification including Soroban
> host types, user-defined types, and event schemas. Together they enable the SDK to parse and expose
> contract metadata, which is essential for tooling, auto-generated contract clients, and off-chain
> systems that need to understand contract interfaces.

Proof of completion:

- Release 14.1.0: https://github.com/StellarCN/py-stellar-base/releases/tag/14.1.0

Introspection APIs for SEP-46 (contract metadata), SEP-47 (contract interface discovery), and SEP-48
(contract interface specification) were added and shipped in 14.1.0, including `ContractMeta`,
`ContractSpec`, `ContractInfo`, and `SorobanServer[Async].get_contract_*` helpers that parse a
Soroban contract's Wasm and expose its self-described metadata. This gives tooling and off-chain
systems a standard way to understand contract interfaces.

### 3. AI Coding Agent Skill

Description from last quarter:

> Publish an AI coding agent skill for py-stellar-base following the agentskills.io open standard,
> compatible with Claude Code, Codex CLI, Cursor, Gemini CLI, and others. The skill provides
> token-efficient documentation and best practices for AI-assisted development with the SDK, lowering
> the barrier for developers using AI tools to build on Stellar.

Proof of completion:

- Skill marketplace listing:
  https://skillsmp.com/creators/stellarcn/py-stellar-base/skills-py-stellar-base — published
  py-stellar-base agent skill

An Agent Skills-compatible `stellar-sdk` skill was published — both in the SDK repository and to the
skill marketplace — with Claude Code plugin marketplace metadata and topic references covering
transactions, Horizon, Soroban, XDR/SCVal, async workflows, SEP integrations, security, and
troubleshooting. It gives AI coding assistants token-efficient, accurate guidance for building on
Stellar with the SDK, lowering the barrier for developers using AI tools.

## Proposed Impact

The primary goal for Q3 2026 is to ship py-stellar-base 15.0.0 as a stable release with full Protocol
27 support, giving the ecosystem's large Python user base a supported path to the new protocol.
CAP-71 Soroban authorization is already implemented in the 15.0.0 beta; the stable release is held
until Protocol 27 is available on live test networks for end-to-end validation (issue #1187). Ongoing
maintenance continues in parallel.

## Proposed Deliverables

### 1. Release py-stellar-base 15.0.0 with Full Protocol 27 Support

Finalize the 15.0.0 beta into a stable release with complete Protocol 27 support, including CAP-71
Soroban authorization (`ADDRESS_V2` and delegated `ADDRESS_WITH_DELEGATES` credentials). The
implementation is already done in beta; the remaining work, validating against a live Protocol 27
network, auth examples and a migration guide for the breaking auth changes, and the stable release to
PyPI.

Proof: Stable 15.0.0 release on GitHub and PyPI, auth examples and migration notes, passing CI on
main.

### 2. Continuous Maintenance and Improvement

Beyond routine upkeep, responding to community issues and pull requests, tracking Horizon and Soroban
RPC changes, and keeping CI/CD, the SBOM workflow, and dependencies current, we want to be candid
about our intent for Q3: rather than adding new features, we plan to slow down and look inward. We
will audit the codebase for accumulated technical debt, refactor rough edges, and optimize code that
has grown organically across many releases, so the SDK stays maintainable and dependable for the long
term.

This is a deliberate decision to consolidate, not to coast. For this SDK, "maintenance" has
consistently produced meaningful improvements well beyond what we formally plan, Q2 is the clearest
example, where full Protocol 27 support, the `stellar_sdk.auth` redesign, and a toolchain
modernization all shipped under this same deliverable. We expect Q3 to be no different: as we dig
into the code, concrete fixes and refinements will follow.

Proof: Release notes on GitHub, updated CHANGELOG, refactoring and optimization PRs, passing CI on
main.

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Apython_stellar_sdk&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Apython_stellar_sdk)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Apython_stellar_sdk&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Apython_stellar_sdk)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Apython_stellar_sdk&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Apython_stellar_sdk)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Apython_stellar_sdk&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Apython_stellar_sdk)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
