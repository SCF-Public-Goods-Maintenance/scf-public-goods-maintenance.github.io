---
title: "stellar-flutter-sdk"
parent: Public Good Projects
proposal_issue: 43
proposer: christian-rogobete
category: "SDKs"
budget: "15000"
---

# stellar-flutter-sdk

_The Stellar SDK for Flutter, providing transaction building, Horizon and Soroban RPC access,
high-level Soroban smart contract support, and implements 18 Stellar Ecosystem Proposals (SEPs)
across iOS, Android, and web._

|                      |                                                 |
| -------------------- | ----------------------------------------------- |
| **Category**         | SDKs                                            |
| **Website**          | <https://github.com/Soneso/stellar_flutter_sdk> |
| **Repository**       | <https://github.com/Soneso/stellar_flutter_sdk> |
| **First Released**   | June 2020                                       |
| **Intake**           | soft-launch                                     |
| **Budget Requested** | 15000                                           |

## Project Description

The Flutter Stellar SDK is a Dart library for building Stellar applications on iOS, Android, and web
using Flutter. It provides transaction building, account management, Horizon API access, Soroban RPC
support, high-level Soroban smart contract support, and implements 18 Stellar Ecosystem Proposals
(SEPs). The SDK is listed on the official Stellar developer documentation and is used by wallets and
applications including Beans App, Stack Wallet, Defindex, Meru, and others.

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

In Q2 2026 the Flutter SDK shipped three releases. The SDK is used by wallets and applications
including Beans App, Stack Wallet, Defindex, and Meru. At the close of the quarter: 85 stars, 36
forks, 110 total releases, pub.dev downloads of 2,013 (30-day, up from 837 at Q1 close) and 15,279
(52-week), 0 open issues, 87 dependent GitHub repositories and 5 dependent packages, a median
first-response time of 1.3 hours, a median time-to-close of 1.3 days, and a 100% response rate. Unit
test coverage is tracked on Codecov with 80% project / 70% patch thresholds enforced, currently at
90%.

The headline delivery is OpenZeppelin smart account support, shipped in v3.1.0 and published to
pub.dev. It uses a two-layer design: a contract-agnostic core layer with an OpenZeppelin layer on
top, so third parties can support other smart-account contract families without rewriting the
cryptographic foundations (e.g. WebAuthn COSE public-key extraction, secp256r1 handling). It covers
wallet lifecycle via passkeys, context rules and policies, automatic auth-entry signing, multi-signer
authorization (passkey, delegated G-address, Ed25519), relayer-sponsored fees, and indexer-based
credential discovery, across iOS, Android, and web. Smart account documentation comprises an
onboarding guide, an API reference, and per-platform WebAuthn guides.

A cross-platform demo builds on iOS, Android, and web exercising the smart-account features: wallet
creation and connection, single- and multi-signer token transfers, on-chain context-rule management
with expiry, signers, policies. The demo repo also includes an agent-signer flow: a reference agent
that runs headlessly against the SDK, a coordination server, and an approval inbox — the complete
flow where a user delegates scoped authority to an agent, the agent acts within scope, over-scope
calls are rejected on-chain and surfaced to the user for approval in the demo app, and the approved
call is re-submitted via the relayer.

Protocol 26 was tracked and Protocol 27 support has been added, with ADDRESS_V2 and
ADDRESS_WITH_DELEGATES authorization support and an end-to-end testnet integration test (v3.2.0).
Release 3.2.1 added a headless connectToContract path for smart accounts and hardened SEP-10 by
rejecting challenges without finite time bounds. A SEP-11 TxRep escaping bug was fixed. CI stays
hardened — Actions pinned to commit SHAs, least-privilege permissions, Codecov thresholds, a daily
upstream XDR change-detection workflow, and monthly Dependabot updates — and compatibility matrices
were regenerated to Horizon/RPC v27.0.0. SBOM submission to PG Atlas continues on every push to
master, and daily statistics collection continues via soneso-sdk-stats, providing the responsiveness
and adoption metrics above (see: [soneso.github.io/soneso-sdk-stats][statsdash]).

## Past Deliverables

### 1. Continuous Maintenance and Improvement

Description from last quarter:

> Regular SDK updates addressing Horizon, Soroban RPC, and protocol updates (including Protocol 26),
> bug fixes, feature requests, and documentation updates. Maintain existing SEP implementations and
> update as needed. Keep compatibility matrices, CI pipelines, statistics dashboard, and SBOM
> workflow up to date.

Proof of completion:

- Release 3.1.0: https://github.com/Soneso/stellar_flutter_sdk/releases/tag/3.1.0
- Release 3.2.0: https://github.com/Soneso/stellar_flutter_sdk/releases/tag/3.2.0
- Release 3.2.1: https://github.com/Soneso/stellar_flutter_sdk/releases/tag/3.2.1
- Protocol 26 tracked: Horizon v26.0.0 / RPC v26.0.0 matrices, XDR upstream 0a56f5b
- Protocol 27 / CAP-71 support (v3.2.0): [PR #150][pr150]
- Headless connectToContract + RPC-visibility polling for smart accounts (v3.2.1): [PR #151][pr151]
- SEP-10 hardening, reject challenges without finite time bounds (v3.2.1): [PR #152][pr152]
- SEP-11 TxRep MEMO_TEXT escaping fix + coverage: [PR #140][pr140]
- Dependabot bumps (monthly, pinned SHAs): PRs 141-146
- Stats dashboard: https://soneso.github.io/soneso-sdk-stats/
- [Horizon compatibility matrix](https://github.com/Soneso/stellar_flutter_sdk/blob/master/compatibility/horizon/HORIZON_COMPATIBILITY_MATRIX.md)
- [RPC compatibility matrix](https://github.com/Soneso/stellar_flutter_sdk/blob/master/compatibility/rpc/RPC_COMPATIBILITY_MATRIX.md)
- [SEP compatibility matrices](https://github.com/Soneso/stellar_flutter_sdk/tree/master/compatibility/sep)

Three releases shipped this quarter. Protocol 26 was tracked and Protocol 27 (CAP-71) support has
been added, including an end-to-end ADDRESS_WITH_DELEGATES testnet integration test. Release 3.2.1
added a headless connectToContract path with RPC-visibility polling and hardened SEP-10. CI hardening
(Actions pinned to commit SHAs, least-privilege permissions, Codecov 80% project / 70% patch
thresholds) and the daily upstream XDR change-detection workflow remain in force, and compatibility
matrices were regenerated to Horizon/RPC v27.0.0.

### 2. OpenZeppelin Smart Account Support

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
> - Platform support: WebAuthn via ASAuthorization (iOS), CredentialManager (Android), and
>   navigator.credentials (web) with secure storage adapters
> - Cross-platform demo application (iOS, Android, web)
> - Documentation: API reference and onboarding guide

Delivered in release [3.1.0][rel310] ([PR #148][pr148]) and published to pub.dev, with the Protocol
27 ADDRESS_WITH_DELEGATES auth path integrated in [3.2.0][rel320].

Delivery by area:

#### SDK implementation

Proof of completion:

- Release 3.1.0: https://github.com/Soneso/stellar_flutter_sdk/releases/tag/3.1.0
- PR 148: https://github.com/Soneso/stellar_flutter_sdk/pull/148

A two-layer design separates a contract-agnostic core from the OpenZeppelin layer, so other
smart-account contract families can be supported without rewriting the cryptographic core. All
committed sub-items - wallet lifecycle, context rules and policies, automatic auth-entry signing,
multi-signer authorization, fee sponsoring via relayer, credential discovery via indexer, and
cross-platform WebAuthn - are present and tested.

#### Cross-platform demo

Proof of completion:

- Repository: https://github.com/Soneso/flutter-oz-smartaccount-demo
- Platforms: ios/ (iOS 16.0+), android/ (API 28+), web/ (modern WebAuthn browser)
- Real deployed relayer proxy (Cloudflare Worker), exercised in the transfer and approval flows
- Indexer integration and Reown (mobile) / Freighter (web) wallet-connect

The demo exercises the smart-account features: wallet creation and connection (passkey, indexer, and
address recovery), single- and multi-signer token transfers, on-chain context-rule management with
signers, policies, and expiry, SEP-41 token allowances, and the agent delegation and approval-inbox
flow.

#### Documentation

Proof of completion:

- [Smart-account documentation set][sadocs]: onboarding guide, API reference, and per-platform
  WebAuthn guides (iOS, Android, web)

#### Agent-signer flow in the demo app

Beyond the committed scope, the [PR-44 response][pr44resp] added a full agent-signer flow to the demo
app.

Proof of completion:

- Demo [PR #1][demopr1]
- Agent-flow runbook (demo repo): [documentation/agent-flow.md][agflow]
- Worked delegation example (demo repo): [agent-delegation-demo.md][deleg]

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
value (XdrSCVal) to a native Dart value, so contract invocation and simulation results can be
consumed directly instead of parsing the raw XDR union by hand. The JS and Python SDKs already
provide this.

Update the Dart contract-bindings implementation that Soneso contributed to the community
stellar-contract-bindings generator (linked from the Stellar CLI) so it produces code compatible with
the current SDK.

## Proposed Deliverables

### Continuous Maintenance and Improvement

Regular SDK updates addressing Horizon, Soroban RPC, and protocol updates (tracking Protocol 27
through its mainnet activation), bug fixes, feature requests, and documentation updates. Maintain
existing SEP implementations and update as needed. Harden the smart-account feature as the network
advances and reduce code duplication in the Horizon request builders and operation builders. Keep
compatibility matrices, CI pipelines, statistics dashboard, and SBOM workflow up to date.

Proof: Release notes on GitHub, PRs with the fixes and refactors, updated compatibility matrices, and
the soneso-sdk-stats dashboard.

### SEP-51 (XDR-JSON)

Implement bi-directional XDR/JSON conversion via the XDR generator, with round-trip unit tests and
documentation, for cross-SDK parity with the Python and PHP SDKs.

Proof: GitHub release, PR with implementation and tests, SEP-51 compatibility matrix, documentation.

### Native ScVal Conversion

Add a helper that converts a smart-contract value (XdrSCVal) to a native Dart value, so contract
invocation and simulation results can be consumed directly instead of parsing the raw XDR union by
hand. This matches the JS and Python SDKs.

Proof: GitHub release, PR with implementation and tests, documentation.

### Contract Bindings Update

Update the Dart contract-bindings implementation that Soneso contributed to the community
stellar-contract-bindings generator (linked from the Stellar CLI) so its generated Dart code is
compatible with the current SDK.

Proof: pull request to the stellar-contract-bindings repository.

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

[agflow]:
  https://github.com/Soneso/flutter-oz-smartaccount-demo/blob/main/documentation/agent-flow.md
[deleg]:
  https://github.com/Soneso/flutter-oz-smartaccount-demo/blob/main/documentation/smart-accounts/agent-delegation-demo.md
[demopr1]: https://github.com/Soneso/flutter-oz-smartaccount-demo/pull/1
[pr140]: https://github.com/Soneso/stellar_flutter_sdk/pull/140
[pr148]: https://github.com/Soneso/stellar_flutter_sdk/pull/148
[pr150]: https://github.com/Soneso/stellar_flutter_sdk/pull/150
[pr151]: https://github.com/Soneso/stellar_flutter_sdk/pull/151
[pr152]: https://github.com/Soneso/stellar_flutter_sdk/pull/152
[pr44resp]:
  https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/pull/44#issuecomment-4274930402
[rel310]: https://github.com/Soneso/stellar_flutter_sdk/releases/tag/3.1.0
[rel320]: https://github.com/Soneso/stellar_flutter_sdk/releases/tag/3.2.0
[sadocs]: https://github.com/Soneso/stellar_flutter_sdk/tree/master/documentation/smart-accounts
[statsdash]: https://soneso.github.io/soneso-sdk-stats/
