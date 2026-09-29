---
title: "java-stellar-sdk"
canonical_id: daoip-5:scf:project:java_stellar_sdk
parent: Public Good Projects
proposal_issue: 53
proposer: overcat
category: "SDKs"
budget: "15000"
---

# java-stellar-sdk

_The Java Stellar SDK provides APIs to build transactions, query Horizon, and interact with Soroban
RPC, with Android support and implementations of several Stellar Ecosystem Proposals._

|                               |                                                                  |
| ----------------------------- | ---------------------------------------------------------------- |
| **Category**                  | SDKs                                                             |
| **Website**                   | <https://github.com/lightsail-network/java-stellar-sdk>          |
| **java-stellar-sdk**          | <https://github.com/lightsail-network/java-stellar-sdk>          |
| **stellar-contract-bindings** | <https://github.com/lightsail-network/stellar-contract-bindings> |
| **First Released**            | November 2015                                                    |
| **Intake**                    | soft-launch                                                      |
| **Budget Requested**          | 15000                                                            |

## Project Description

The Java Stellar SDK is a Java library for building Stellar applications on server-side JVM runtimes
and Android. It provides transaction building, Horizon API access, Soroban RPC support, high-level
Soroban smart contract support, and implements several Stellar Ecosystem Proposals. The SDK is listed
on the official Stellar developer documentation and is used by projects including Lobstr Vault,
[Stellar Anchor Platform](https://github.com/stellar/anchor-platform), and others.

This project also maintains the Java generator in stellar-contract-bindings, a CLI tool that
generates typed Java client code for Soroban smart contracts from their SEP-48 interface
specifications, so developers can call a contract without writing the encoding by hand.

## Team & Experience

overcat (GitHub: [overcat](https://github.com/overcat), Discord: @overcat.me) has been active in the
Stellar community since 2018 and has rich experience in Stellar-related development, maintaining a
series of Stellar infrastructure software. Currently maintained Stellar-related projects are listed
at https://lightsail.network.

## Retroactive Impact

In Q3 2026, both planned deliverables were completed, and two higher-priority items were added
mid-quarter: Protocol 28 support in the SDK and SEP-48-based Java binding generation in
stellar-contract-bindings. These took most of the quarter, so the planned maintenance work was
smaller than expected. The SDK shipped three stable releases: 4.0.0 brought Protocol 27 support to a
stable release as planned, 4.0.1 fixed a parsing bug, and 5.0.0 added Protocol 28 support, including
CAP-85 external executable references. In stellar-contract-bindings, the Java generator was rewritten
and now generates typed bindings for contract events as well as functions.

Maintenance still delivered results. In the SDK, a community-reported parsing bug was fixed and
released the next day, the SDK no longer polls the RPC server continuously while waiting for a
transaction, and text is now always encoded as UTF-8. In stellar-contract-bindings, the Java
generator was simplified.

## Past Deliverables

### 2026 Q3

#### D1. Release java-stellar-sdk 4.0.0 with Full Protocol 27 Support

Description from last quarter:

> Finalize the 4.0.0 beta into a stable release with complete Protocol 27 support, including CAP-71
> Soroban authorization (`ADDRESS_V2` and delegated `ADDRESS_WITH_DELEGATES` credentials) and the
> redesigned `Auth.Signer` that natively supports custom account contracts (BLS, WebAuthn, threshold,
> policy). The implementation is already done in beta; the remaining work — validating against a live
> Protocol 27 network, auth examples and a migration guide for the breaking auth changes, and the
> stable release to Maven Central — is paced by Protocol 27 test-network availability.

Proof of completion:

- Release 4.0.0: https://github.com/lightsail-network/java-stellar-sdk/releases/tag/4.0.0

4.0.0 brought Protocol 27 support to a stable release. It supports the new CAP-71 authorization
credentials (`ADDRESS_V2` and `ADDRESS_WITH_DELEGATES`), and the redesigned signing interface
(`Auth.Signer`) supports custom account contracts such as BLS, WebAuthn, threshold, and policy
contracts. The release notes include a migration guide for the breaking `Auth.Signer` change.

#### D2. Continuous Maintenance and Improvement

Description from last quarter:

> Beyond routine upkeep — responding to community issues and pull requests, tracking Horizon and
> Soroban RPC changes, keeping Android compatibility current, and keeping CI/CD and dependencies up
> to date — we want to be candid about our intent for Q3: rather than adding new features, we plan to
> slow down and look inward. We will audit the codebase for accumulated technical debt, refactor
> rough edges, and optimize code that has grown organically across many releases, so the SDK stays
> maintainable and dependable for the long term.
>
> This is a deliberate decision to consolidate, not to coast. For this SDK, "maintenance" has
> consistently produced meaningful improvements well beyond what we formally plan — Q2 is the
> clearest example, where full Protocol 27 support, the `Auth.Signer` redesign, and a JDK 21
> toolchain upgrade all shipped under this same deliverable. We expect Q3 to be no different: as we
> dig into the code, concrete fixes and refinements will follow.

Proof of completion:

- Release 4.0.1: https://github.com/lightsail-network/java-stellar-sdk/releases/tag/4.0.1
- https://github.com/lightsail-network/java-stellar-sdk/pull/811
- https://github.com/lightsail-network/java-stellar-sdk/pull/819
- https://github.com/lightsail-network/java-stellar-sdk/pull/820
- View all merged PRs (Q3 2026):
  https://github.com/lightsail-network/java-stellar-sdk/pulls?q=is%3Apr+is%3Amerged+merged%3A2026-07-01..2026-09-30
- https://github.com/lightsail-network/stellar-contract-bindings/pull/29
- https://github.com/lightsail-network/stellar-contract-bindings/pull/33

Maintenance was smaller than planned, because Protocol 28 support and SEP-48 binding generation (D3
and D4) were added mid-quarter and took up much of the time planned for it.

In the SDK, a community user reported that a valid testnet transaction could not be parsed (an
`ExtendFootprintTTLOperation` with `extendTo` set to 0). The fix shipped in 4.0.1 the next day. After
submitting a contract transaction, the SDK now waits between status checks instead of polling the RPC
server continuously. Text is now always encoded as UTF-8, so non-ASCII text produces the same bytes
on every JVM. These two fixes are in the pending release.

In stellar-contract-bindings, type mapping and templates in the Java generator were simplified, and
generated Java no longer depends on the javatuples library.

#### D3. Protocol 28 Support

Description from last quarter:

> This work was not explicitly planned but was completed as additional contribution during the
> quarter.

Proof of completion:

- Release 5.0.0: https://github.com/lightsail-network/java-stellar-sdk/releases/tag/5.0.0
- https://github.com/lightsail-network/java-stellar-sdk/pull/817
- https://github.com/lightsail-network/java-stellar-sdk/pull/815

Protocol 28 support was added mid-quarter and shipped in 5.0.0, so Java and Android developers can
build against the new protocol as soon as it is available. CAP-85 lets a contract follow Wasm code
that an owner contract publishes under a tag, so updating the tag upgrades every contract that
follows it. The SDK can now create such contracts, look up the code they point to, and read their
interface specs.

#### D4. SEP-48 Contract Bindings in stellar-contract-bindings

Description from last quarter:

> This work was not explicitly planned but was completed as additional contribution during the
> quarter.

Proof of completion:

- Release 0.6.0b: https://github.com/lightsail-network/stellar-contract-bindings/releases/tag/0.6.0b
- https://github.com/lightsail-network/stellar-contract-bindings/pull/40
- https://github.com/lightsail-network/stellar-contract-bindings/pull/31
- https://github.com/lightsail-network/stellar-contract-bindings/pull/32
- https://github.com/lightsail-network/stellar-contract-bindings/pull/27

This work was added mid-quarter and builds on the SEP-48 support added to the SDK in Q2. 0.6.0b fixed
the Java generator so that its output compiles, and CI now checks this on every change. The generator
was then rewritten and merged for the next release: it generates typed bindings for contract events,
structs, unions, and contract errors, with a simpler API for callers.

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
