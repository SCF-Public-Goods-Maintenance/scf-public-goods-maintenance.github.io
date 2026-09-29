---
title: "py-stellar-base"
canonical_id: daoip-5:scf:project:python_stellar_sdk
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
| **py-stellar-base**           | <https://github.com/StellarCN/py-stellar-base>                   |
| **stellar-contract-bindings** | <https://github.com/lightsail-network/stellar-contract-bindings> |
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

This project also maintains stellar-contract-bindings, a CLI tool built on py-stellar-base that generates typed Python client code for Soroban smart contracts from their SEP-48 interface specifications, so developers can call a contract without writing the encoding by hand.

## Team & Experience

overcat (GitHub: [overcat](https://github.com/overcat), Discord: @overcat.me) has been active in the
Stellar community since 2018 and has rich experience in Stellar-related development, maintaining a
series of Stellar infrastructure software. Currently maintained Stellar-related projects are listed
at https://lightsail.network.

## Retroactive Impact

In Q3 2026, both planned deliverables were completed, and two higher-priority items were added mid-quarter: Protocol 28 support in the SDK and SEP-48-based binding generation in stellar-contract-bindings. These took most of the quarter, so the planned maintenance work was smaller than expected. The SDK shipped three stable releases: 15.0.0 brought Protocol 27 support to a stable release as planned, and 16.0.0 and 16.1.0 added Protocol 28 support, including CAP-85 external executable references. stellar-contract-bindings released 0.6.0b, which generates typed Python bindings for contract events as well as functions.

Maintenance still delivered results. In the SDK, the unit test suite was restructured and a community-reported CAP-71 signing bug was fixed within a week. In stellar-contract-bindings, the tool now reuses the SDK's SEP-48 parser, and the Python generator was simplified.


## Past Deliverables

### 2026 Q3

#### D1. Release py-stellar-base 15.0.0 with Full Protocol 27 Support

Description from last quarter:

> Finalize the 15.0.0 beta into a stable release with complete Protocol 27 support, including CAP-71 Soroban authorization (`ADDRESS_V2` and delegated `ADDRESS_WITH_DELEGATES` credentials). The implementation is already done in beta; the remaining work — validating against a live Protocol 27 network, auth examples and a migration guide for the breaking auth changes, and the stable release to PyPI — is paced by Protocol 27 test-network availability.

Proof of completion:

- Release 15.0.0: https://github.com/StellarCN/py-stellar-base/releases/tag/15.0.0
- https://github.com/StellarCN/py-stellar-base/pull/1198
- Auth example: https://github.com/StellarCN/py-stellar-base/commit/98230946a467ed7481b69573a77e205737fbe036 — docs: add CAP-71 delegated authorization example

15.0.0 brought Protocol 27 support to a stable release. It supports the new CAP-71 authorization credentials (`ADDRESS_V2` and `ADDRESS_WITH_DELEGATES`) in signing, contract clients, and SEP-45.

#### D2. Continuous Maintenance and Improvement

Description from last quarter:

> Beyond routine upkeep — responding to community issues and pull requests, tracking Horizon and Soroban RPC changes, and keeping CI/CD, the SBOM workflow, and dependencies current — we want to be candid about our intent for Q3: rather than adding new features, we plan to slow down and look inward. We will audit the codebase for accumulated technical debt, refactor rough edges, and optimize code that has grown organically across many releases, so the SDK stays maintainable and dependable for the long term.
>
> This is a deliberate decision to consolidate, not to coast. For this SDK, "maintenance" has consistently produced meaningful improvements well beyond what we formally plan — Q2 is the clearest example, where full Protocol 27 support, the `stellar_sdk.auth` redesign, and a toolchain modernization all shipped under this same deliverable. We expect Q3 to be no different: as we dig into the code, concrete fixes and refinements will follow.

Proof of completion:

- https://github.com/StellarCN/py-stellar-base/pull/1207
- https://github.com/StellarCN/py-stellar-base/pull/1218
- https://github.com/StellarCN/py-stellar-base/pull/1206
- Commit 56bffa5: https://github.com/StellarCN/py-stellar-base/commit/56bffa593a03db621344c9089fa0e4ffcf61fe3e — test: merge call_builder sync/async test trees (38 files -> 19)
- Commit cf03fa9: https://github.com/StellarCN/py-stellar-base/commit/cf03fa96897ecc8c131d2dccbaab6e8c900b138b — test: standardize all HTTP mocking on pytest-httpserver
- Commit 54c8705: https://github.com/StellarCN/py-stellar-base/commit/54c8705461058482dd9d91612826625d29057642 — test: restore behavioral coverage lost in the sync/async merges
- View all merged PRs (Q3 2026): https://github.com/StellarCN/py-stellar-base/pulls?q=is%3Apr+is%3Amerged+merged%3A2026-07-01..2026-09-30
- https://github.com/lightsail-network/stellar-contract-bindings/pull/23
- https://github.com/lightsail-network/stellar-contract-bindings/pull/29
- https://github.com/lightsail-network/stellar-contract-bindings/pull/35

Maintenance was smaller than planned, because Protocol 28 support and SEP-48 binding generation (D3 and D4) were added mid-quarter and took up much of the time planned for it. The planned consolidation still produced results.

In the SDK, the unit test suite was restructured: sync and async test trees were merged and HTTP mocking was standardized on one library, removing about 2,900 net lines. A community-reported CAP-71 bug was fixed within a week: signing one part of a delegated entry with a different expiration used to silently invalidate the signatures already on it, and it now raises an error instead. The fix is in the pending release. The federation lookup now uses the HTTP client the caller supplies.

In stellar-contract-bindings, the tool dropped its own Wasm parser and now uses the SDK's SEP-48 parser, so both projects share one implementation. Type mapping and templates in the Python generator were simplified, dead code was removed, and dependencies and CI were updated.

#### D3. Protocol 28 Support

Description from last quarter:

> This work was not explicitly planned but was completed as additional contribution during the quarter.

Proof of completion:

- Release 16.0.0: https://github.com/StellarCN/py-stellar-base/releases/tag/16.0.0
- Release 16.1.0: https://github.com/StellarCN/py-stellar-base/releases/tag/16.1.0
- https://github.com/StellarCN/py-stellar-base/pull/1212
- https://github.com/StellarCN/py-stellar-base/pull/1213
- https://github.com/StellarCN/py-stellar-base/pull/1216

Protocol 28 support was added mid-quarter and shipped in 16.0.0 and 16.1.0, so Python developers can build against the new protocol as soon as it is available. CAP-85 lets a contract follow Wasm code that an owner contract publishes under a tag, so updating the tag upgrades every contract that follows it. The SDK can now create such contracts, look up the code they point to, and read their interface specs.

#### D4. SEP-48 Contract Bindings in stellar-contract-bindings

Description from last quarter:

> This work was not explicitly planned but was completed as additional contribution during the quarter.

Proof of completion:

- Release 0.6.0b: https://github.com/lightsail-network/stellar-contract-bindings/releases/tag/0.6.0b
- https://github.com/lightsail-network/stellar-contract-bindings/pull/24
- https://github.com/lightsail-network/stellar-contract-bindings/pull/26
- https://github.com/lightsail-network/stellar-contract-bindings/pull/30
- https://github.com/lightsail-network/stellar-contract-bindings/pull/25

This work was added mid-quarter and builds on the SEP-48 support added to the SDK in Q2. The Python generator can now produce typed bindings for the events a contract declares in its SEP-48 spec, not only for its functions. Generated Python code no longer executes text taken from a contract spec, keeps the contract's documentation readable, and uses the contract's own names for union cases.

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
