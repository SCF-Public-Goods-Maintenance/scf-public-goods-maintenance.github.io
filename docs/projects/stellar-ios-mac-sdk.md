---
title: "stellar-ios-mac-sdk"
parent: Public Good Projects
proposal_issue: 41
proposer: christian-rogobete
category: "SDKs"
budget: "15000"
---

# stellar-ios-mac-sdk

_The Stellar SDK for iOS and macOS, providing transaction building, Horizon and Soroban RPC access,
high-level Soroban smart contract support, and implements 18 Stellar Ecosystem Proposals (SEPs)._

|                      |                                                 |
| -------------------- | ----------------------------------------------- |
| **Category**         | SDKs                                            |
| **Website**          | <https://github.com/Soneso/stellar-ios-mac-sdk> |
| **Repository**       | <https://github.com/Soneso/stellar-ios-mac-sdk> |
| **First Released**   | March 2018                                      |
| **Intake**           | soft-launch                                     |
| **Budget Requested** | 15000                                           |

## Project Description

The iOS Stellar SDK is a native Swift library for building Stellar applications on iOS and macOS. It
provides transaction building, account management, Horizon API access, Soroban RPC support,
high-level Soroban smart contract support, and implements 18 Stellar Ecosystem Proposals (SEPs). The
SDK is listed on the official Stellar developer documentation and is used by wallets and applications
including LOBSTR, Unstoppable Wallet, and others.

## Team & Experience

My name is Christian, also known as Soneso in the Stellar community, and I am the main developer and
maintainer of several Stellar Client SDKs.

- GitHub: [christian-rogobete](https://github.com/christian-rogobete)
- Discord: `soneso`
- LinkedIn: [Christian Rogobete](https://www.linkedin.com/in/rogobete/)

I began contributing to the Stellar network in 2017, specializing primarily in the development and
maintenance of Stellar SDKs. I developed the iOS Stellar SDK, the Flutter Stellar SDK, the PHP
Stellar SDK, and the Kotlin Multiplatform Stellar SDK. I currently work full-time on my Stellar SDK
projects.

Previous SCF participation:

- Multiple SCF Build Awards, including the KMP Stellar SDK OZ smart account support and wallet SDKs
  for Dart and Swift
- SCF Public Goods Award since Q3 2025 (Batch 1) for the iOS, Flutter, and PHP SDKs

## Retroactive Impact

In Q2 2026 the iOS/macOS SDK shipped four releases — 3.4.7, 3.5.0, 3.6.0, and 3.6.1. The SDK is used
by wallets and applications including LOBSTR and Unstoppable Wallet. At the close of the quarter: 130
stars, 57 forks, 144 total releases, 0 open issues, a median first-response time of 2.7 hours, a
median time-to-close of 21.1 hours, and a 100% response rate. Unit test coverage is tracked on
Codecov and enforced in CI, currently at 91%.

The SEP-11 TxRep rewrite shipped in v3.4.7: the monolithic 3,596-line hand-written TxRep.swift was
replaced with generated toTxRep() and fromTxRep() methods on the XDR types, reducing TxRep.swift to a
75-line facade with an unchanged public API. The rewrite also fixed several SEP-11 conformance
issues, including pool-share ChangeTrustAsset encoding, unsigned and zero-operation transactions,
L-address liquidity-pool StrKey decoding, and C-style MEMO_TEXT escaping.

OpenZeppelin smart account support shipped in v3.5.0. It uses a two-layer design: a contract-agnostic
core with an OpenZeppelin layer on top, so third parties can support other smart-account contract
families without rewriting the cryptographic foundations (e.g. WebAuthn COSE public-key extraction,
secp256r1 handling). It covers wallet lifecycle via passkeys, context rules and policies, automatic
auth-entry signing, multi-signer authorization (passkey, delegated G-address, Ed25519),
relayer-sponsored fees, and indexer-based credential discovery, on iOS and macOS with native
ASAuthorization passkeys.

A demo application for iOS and macOS exercises the smart-account features against the released SDK,
including Reown and Freighter wallet-connect via the stellar_signAuthEntry method. Beyond the
committed demo, a full agent-signer flow was delivered: a standalone reference agent, a coordination
server, and an approval inbox — the flow where a user delegates scoped authority to an agent, the
agent acts within scope, over-scope calls are rejected on-chain and surfaced to the user for
approval, and the approved call is re-submitted via the relayer.

Smart account documentation comprises an onboarding guide, an API reference, and per-platform
WebAuthn guides for iOS and macOS.

Protocol 26 was tracked (matrices to Horizon/RPC v26.0.0) and Protocol 27 / CAP-71 was delivered in
v3.6.0, with ADDRESS_V2 and ADDRESS_WITH_DELEGATES authorization support and an end-to-end
ADDRESS_WITH_DELEGATES testnet integration test. The same release bounded XDR decode recursion depth,
preventing a stack overflow from a maliciously nested delegate tree. Release 3.6.1 added a headless
connectToContract path with RPC-visibility polling for smart accounts, hardened SEP-10 by rejecting
challenges without finite time bounds, and fixed a SEP-6/SEP-24 anchor-transaction decode that
crashed on an unrecognized kind/status, and recovered the dropped fee description field.

CI stays hardened — Actions pinned to commit SHAs, least-privilege permissions, Codecov thresholds, a
daily upstream XDR change-detection workflow, and monthly Dependabot updates — and compatibility
matrices were regenerated to Horizon/RPC v27.0.0. SBOM submission to PG Atlas continues on every push
to master, and daily statistics collection continues via soneso-sdk-stats, providing the
responsiveness metrics above (see: [soneso.github.io/soneso-sdk-stats][statsdash]).

## Past Deliverables

### 1. Continuous Maintenance and Improvement Deliverable

Description from last quarter:

> Regular SDK updates addressing Horizon, Soroban RPC, and protocol updates (including Protocol 26),
> bug fixes, feature requests, and documentation updates. Maintain existing SEP implementations and
> update as needed. Keep compatibility matrices, CI pipelines, statistics dashboard, and SBOM
> workflow up to date.

Proof of completion:

- Release 3.4.7: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.4.7
- Release 3.6.0: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.6.0
- Release 3.6.1: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.6.1
- Protocol 26 tracked: Horizon v26.0.0 / RPC v26.0.0 matrices (3.4.7)
- Protocol 27 / CAP-71 support (v3.6.0): [PR #211][pr211]
- Headless connectToContract + RPC-visibility polling for smart accounts (v3.6.1): [PR #213][pr213]
- SEP-10 hardening, reject challenges without finite time bounds (v3.6.1): [PR #214][pr214]
- SEP-6/SEP-24 anchor-transaction crash fix on unrecognized kind/status, and recovered fee
  description field (v3.6.1): [PR #212][pr212]
- Error-handling guide (docs/error-handling.md) with integration tests covering every documented
  scenario (v3.4.7)
- Dependabot bumps (monthly, pinned SHAs)
- Stats dashboard: https://soneso.github.io/soneso-sdk-stats/
- [Horizon compatibility matrix](https://github.com/Soneso/stellar-ios-mac-sdk/blob/master/compatibility/horizon/HORIZON_COMPATIBILITY_MATRIX.md)
- [RPC compatibility matrix](https://github.com/Soneso/stellar-ios-mac-sdk/blob/master/compatibility/rpc/RPC_COMPATIBILITY_MATRIX.md)
- [SEP compatibility matrices](https://github.com/Soneso/stellar-ios-mac-sdk/tree/master/compatibility/sep)

Four releases shipped this quarter. Protocol 26 was tracked and Protocol 27 (CAP-71) was delivered,
including an end-to-end ADDRESS_WITH_DELEGATES testnet integration test. Release 3.6.1 added a
headless connectToContract path with RPC-visibility polling, hardened SEP-10, and improved SEP-6
decoding. CI hardening (Actions pinned to commit SHAs, least-privilege permissions, Codecov
thresholds) and the daily upstream XDR change-detection workflow remain in force, and compatibility
matrices were regenerated to Horizon/RPC v27.0.0.

### 2. SEP-11 TxRep Rewrite

Description from last quarter:

> Replace the monolithic hand-written TxRep implementation with generated toTxRep()/fromTxRep()
> methods on XDR types, reducing TxRep.swift to a thin facade. This mirrors the approach already
> completed in the Flutter and PHP SDKs.

Proof of completion:

- Release 3.4.7: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.4.7
- PR 202: https://github.com/Soneso/stellar-ios-mac-sdk/pull/202

TxRep.swift was reduced from 3,596 lines to a 75-line facade, with toTxRep()/fromTxRep() generated on
the XDR types and the public API unchanged. The rewrite also fixed several SEP-11 conformance issues
(pool-share ChangeTrustAsset encoding, unsigned and zero-operation transactions, L-address
liquidity-pool StrKey decoding, and C-style MEMO_TEXT escaping).

### 3. OpenZeppelin Smart Account Support

Description from last quarter:

> Implement support for the OpenZeppelin smart account contracts on Soroban, covering:
>
> - Wallet lifecycle: create, deploy, and connect smart account wallets with WebAuthn passkey
>   registration
> - Context rules and policies: create, edit, and remove authorization rules with configurable
>   signers and policies
> - Token operations and contract calls with automatic auth entry signing
> - Multi-signer authorization: passkey signers, delegated Stellar account signers, and Ed25519 key
>   signers
> - Fee sponsoring via relayer proxy for gasless transactions
> - Credential discovery via indexer integration
> - Platform-native WebAuthn via ASAuthorization for iOS and macOS with secure storage adapters
> - Demo application for iOS and macOS
> - Documentation: API reference and onboarding guide

Delivered in release [3.5.0][rel350] ([PR #208][pr208]), with the Protocol 27 ADDRESS_WITH_DELEGATES
auth path integrated in 3.6.0. The additional wallet-connect scope committed in the PR-42 response
was also delivered. Delivery by area:

#### SDK implementation

Proof of completion:

- Release 3.5.0: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.5.0
- PR 208: https://github.com/Soneso/stellar-ios-mac-sdk/pull/208

A two-layer design separates a contract-agnostic core (passkey/WebAuthn, secp256r1) from the
OpenZeppelin layer, so other smart-account contract families can be supported without rewriting the
cryptographic core. All committed sub-items - wallet lifecycle, context rules and policies, automatic
auth-entry signing, multi-signer authorization, fee sponsoring via relayer, credential discovery via
indexer, and native ASAuthorization WebAuthn on iOS and macOS - are present and tested.

#### Demo app

Proof of completion:

- Repository: https://github.com/Soneso/ios-oz-smartaccount-demo
- Platforms: iOS and macOS

#### Documentation

Proof of completion:

- [Smart-account documentation set][sadocs]: onboarding guide, API reference, and per-platform
  WebAuthn guides (iOS, macOS)

#### Agent-signer flow in the demo app

Beyond the committed demo, a full agent-signer flow was added to the demo app: a standalone reference
agent, a coordination server, and an approval inbox.

Proof of completion:

- Demo [PR #1][demopr1]
- Agent-flow runbook (demo repo): [documentation/agent-flow.md][agflow]

The user delegates scoped authority to the agent, the agent acts within scope, an over-scope call is
rejected on-chain by the spending-limit policy and surfaced to the user through the coordination
server, the user approves it in the demo app inbox, and the call is re-submitted via the relayer
under the Default rule.

## Proposed Impact

Keep the SDK compatible with Horizon, Soroban RPC, and protocol updates including Protocol 27.
Maintain existing SEP implementations and update as needed. Fix bugs and respond to issues and
feature requests.

Implement SEP-51 (XDR-JSON), a standard mapping between Stellar's XDR structures and JSON. This
enables developers to inspect and manipulate XDR data in a human-readable format, improving debugging
and tooling integration. The Python SDK and the PHP SDK already implement this SEP.

Improve the Soroban developer experience by adding a helper that converts a returned smart-contract
value (SCValXDR) to a native Swift value, so contract invocation and simulation results can be
consumed directly instead of parsing the raw XDR union by hand. The JS and Python SDKs already
provide this.

Update the Swift contract-bindings implementation that Soneso contributed to the community
stellar-contract-bindings generator (linked from the Stellar CLI) so it produces code compatible with
the current SDK.

## Proposed Deliverables

### Continuous Maintenance and Improvement

Regular SDK updates addressing Horizon, Soroban RPC, and protocol updates (tracking Protocol 27
through its mainnet activation), bug fixes, feature requests, and documentation updates. Maintain
existing SEP implementations and update as needed. Harden the smart-account feature as the network
advances. Keep compatibility matrices, CI pipelines, statistics dashboard, and SBOM workflow up to
date.

Proof: Release notes on GitHub, PRs with the fixes, updated compatibility matrices, and the
soneso-sdk-stats dashboard.

### SEP-51 (XDR-JSON)

Implement bi-directional XDR/JSON conversion via the XDR generator, with round-trip unit tests and
documentation, for cross-SDK parity with the Python and PHP SDKs.

Proof: GitHub release, PR with implementation and tests, SEP-51 compatibility matrix, documentation.

### Native ScVal Conversion

Add a helper that converts a smart-contract value (SCValXDR) to a native Swift value, so contract
invocation and simulation results can be consumed directly instead of parsing the raw XDR union by
hand. This matches the JS and Python SDKs.

Proof: GitHub release, PR with implementation and tests, documentation.

### Contract Bindings Update

Update the Swift contract-bindings implementation that Soneso contributed to the community
stellar-contract-bindings generator (linked from the Stellar CLI) so its generated Swift code is
compatible with the current SDK.

Proof: pull request to the stellar-contract-bindings repository.

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_ios_mac_sdk&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_ios_mac_sdk)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_ios_mac_sdk&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_ios_mac_sdk)
[![Criticality](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_ios_mac_sdk&query=%24.criticality_score&label=Criticality&color=E5484D)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_ios_mac_sdk)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_ios_mac_sdk&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_ios_mac_sdk)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_ios_mac_sdk&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_ios_mac_sdk)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

[agflow]: https://github.com/Soneso/ios-oz-smartaccount-demo/blob/main/documentation/agent-flow.md
[demopr1]: https://github.com/Soneso/ios-oz-smartaccount-demo/pull/1
[pr208]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/208
[pr211]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/211
[pr212]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/212
[pr213]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/213
[pr214]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/214
[rel350]: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.5.0
[sadocs]: https://github.com/Soneso/stellar-ios-mac-sdk/tree/master/docs/smart-accounts
[statsdash]: https://soneso.github.io/soneso-sdk-stats/
