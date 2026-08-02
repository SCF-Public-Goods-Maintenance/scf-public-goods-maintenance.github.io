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

In Q2 2026, all three planned deliverables were completed, and protocol work went beyond the plan.
The SDK shipped two stable releases (3.0.0 and 3.1.0). Support for the smart-contract
self-description SEPs (SEP-46, SEP-47, SEP-48) and an AI coding agent skill both landed in 3.1.0. The
generated XDR was advanced from the planned Protocol 26 to Protocol 27, with CAP-71 Soroban
authorization support implemented in the 4.0.0-beta0 pre-release. Alongside features, the toolchain
was modernized, a JDK 21 build toolchain, updated Gradle/Kotlin, and dependency refreshes, and
Horizon request handling was hardened.

## Past Deliverables

### 1. Continuous Maintenance and Improvement

Description from last quarter:

> Regular SDK updates addressing Horizon, Soroban RPC, and protocol changes (including Protocol 26),
> bug fixes, feature requests, and documentation updates. Keep CI/CD pipelines and dependency updates
> current.

Proof of completion:

- Release 3.0.0: https://github.com/lightsail-network/java-stellar-sdk/releases/tag/3.0.0
- Release 3.1.0: https://github.com/lightsail-network/java-stellar-sdk/releases/tag/3.1.0
- Pre-release 4.0.0-beta0:
  https://github.com/lightsail-network/java-stellar-sdk/releases/tag/4.0.0-beta0

Some notable PR, not exhaustive:

- PR #804: https://github.com/lightsail-network/java-stellar-sdk/pull/804 — feat: add CAP-71
  (Protocol 27) Soroban authorization support
- PR #807: https://github.com/lightsail-network/java-stellar-sdk/pull/807 — feat: add
  simulateTransaction useUpgradedAuth flag
- PR #806: https://github.com/lightsail-network/java-stellar-sdk/pull/806 — refactor!: return
  signature SCVal from Auth.Signer for custom account contracts
- PR #800: https://github.com/lightsail-network/java-stellar-sdk/pull/800 — chore: upgrade generated
  XDR definitions to Protocol 27
- PR #784: https://github.com/lightsail-network/java-stellar-sdk/pull/784 — docs: improve xdr
  generator javadocs
- PR #783: https://github.com/lightsail-network/java-stellar-sdk/pull/783 — docs: add missing Javadoc
  comments for various classes and methods

- View all 23 merged PRs (Q2 2026):
  https://github.com/lightsail-network/java-stellar-sdk/pulls?q=is%3Apr+is%3Amerged+merged%3A2026-04-01..2026-06-30

Two stable releases shipped. The generated XDR was upgraded to Protocol 26 and then to Protocol 27,
exceeding the planned Protocol 26 target. CAP-71 Protocol 27 Soroban authorization, including the new
address-bound and delegated credential types, was implemented across the high-level API and shipped
in the 4.0.0-beta0 pre-release, and `Auth.Signer` was further redesigned to natively support custom
account contracts (BLS, WebAuthn, threshold, policy) in the pending release. This Protocol 27 work
currently ships in the 4.0.0-beta0 pre-release rather than a stable release: Protocol 27 is not yet
broadly available in real-world test environments, so the stable 4.0.0 is intentionally held until
the implementation can be validated against a live Protocol 27 network. The toolchain was also
modernized with a JDK 21 build toolchain and updated Gradle/Kotlin/dependencies, and Horizon request
handling was hardened, alongside various bug fixes.

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

- PR #796: https://github.com/lightsail-network/java-stellar-sdk/pull/796 — add SEP-46/47/48 contract
  introspection support
- Release 3.1.0: https://github.com/lightsail-network/java-stellar-sdk/releases/tag/3.1.0

Introspection APIs for SEP-46 (contract metadata), SEP-47 (contract interface discovery), and SEP-48
(contract interface specification) were added and shipped in 3.1.0, including `ContractMeta`,
`ContractSpec`, and `ContractInfo` wrappers under `org.stellar.sdk.contract` and `SorobanServer`
helpers (`getContractWasm`, `getContractMeta`, `getContractSpec`, `getContractInfo`) that parse a
Soroban contract's Wasm and expose its self-described metadata. This gives tooling and off-chain
systems a standard way to understand contract interfaces.

### 3. AI Coding Agent Skill

Description from last quarter:

> Publish an AI coding agent skill for the java-stellar-sdk following the agentskills.io open
> standard, compatible with Claude Code, Codex CLI, Cursor, Gemini CLI, and others. The skill
> provides token-efficient documentation and best practices for AI-assisted development with the SDK,
> lowering the barrier for developers using AI tools to build on Stellar.

Proof of completion:

- PR #797: https://github.com/lightsail-network/java-stellar-sdk/pull/797 — add agent skill for
  java-stellar-sdk
- Release 3.1.0: https://github.com/lightsail-network/java-stellar-sdk/releases/tag/3.1.0

An Agent Skills-compatible skill was published under `skills/`, with Claude Code plugin manifests in
`.claude-plugin/` and Stellar-specific guidance covering transactions, operations, Horizon, Soroban,
XDR/SCVal, and SEP protocols. It gives AI coding assistants token-efficient, accurate guidance for
building on Stellar with the SDK, lowering the barrier for developers using AI tools.

## Proposed Impact

The primary goal for Q3 2026 is to ship java-stellar-sdk 4.0.0 as a stable release with full Protocol
27 support, giving the ecosystem's JVM and Android developer base a supported path to the new
protocol. CAP-71 Soroban authorization is already implemented in the 4.0.0 beta; the stable release
is held until Protocol 27 is available on live test networks for end-to-end validation. Ongoing
maintenance continues in parallel.

## Proposed Deliverables

### 1. Release java-stellar-sdk 4.0.0 with Full Protocol 27 Support

Finalize the 4.0.0 beta into a stable release with complete Protocol 27 support, including CAP-71
Soroban authorization (`ADDRESS_V2` and delegated `ADDRESS_WITH_DELEGATES` credentials) and the
redesigned `Auth.Signer` that natively supports custom account contracts (BLS, WebAuthn, threshold,
policy). The implementation is already done in beta; the remaining work, validating against a live
Protocol 27 network, auth examples and a migration guide for the breaking auth changes, and the
stable release to Maven Central, is paced by Protocol 27 test-network availability.

Proof: Stable 4.0.0 release on GitHub and Maven Central, auth examples and migration notes, passing
CI on master.

### 2. Continuous Maintenance and Improvement

Beyond routine upkeep, responding to community issues and pull requests, tracking Horizon and Soroban
RPC changes, keeping Android compatibility current, and keeping CI/CD and dependencies up to date, we
want to be candid about our intent for Q3: rather than adding new features, we plan to slow down and
look inward. We will audit the codebase for accumulated technical debt, refactor rough edges, and
optimize code that has grown organically across many releases, so the SDK stays maintainable and
dependable for the long term.

This is a deliberate decision to consolidate, not to coast. For this SDK, "maintenance" has
consistently produced meaningful improvements well beyond what we formally plan, Q2 is the clearest
example, where full Protocol 27 support, the `Auth.Signer` redesign, and a JDK 21 toolchain upgrade
all shipped under this same deliverable. We expect Q3 to be no different: as we dig into the code,
concrete fixes and refinements will follow.

Proof: Release notes on GitHub, updated CHANGELOG, refactoring and optimization PRs, passing CI on
master.

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Ajava_stellar_sdk&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Ajava_stellar_sdk)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Ajava_stellar_sdk&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Ajava_stellar_sdk)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Ajava_stellar_sdk&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Ajava_stellar_sdk)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Ajava_stellar_sdk&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Ajava_stellar_sdk)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
