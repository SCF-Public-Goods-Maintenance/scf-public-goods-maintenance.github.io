---
title: "stellar-flutter-sdk"
canonical_id: daoip-5:scf:project:flutter_stellar_sdk
parent: Public Good Projects
proposal_issue: 43
proposer: christian-rogobete
category: "SDKs"
budget: "15000"
---

# stellar-flutter-sdk

_The Stellar SDK for Flutter, providing transaction building, Horizon and Soroban RPC access,
high-level Soroban smart contract support, and implements 21 Stellar Ecosystem Proposals (SEPs)
across iOS, Android, and web._

|                         |                                                 |
| ----------------------- | ----------------------------------------------- |
| **Category**            | SDKs                                            |
| **Website**             | <https://github.com/Soneso/stellar_flutter_sdk> |
| **Repository**          | <https://github.com/Soneso/stellar_flutter_sdk> |
| **First Released**      | June 2020                                       |
| **Intake**              | soft-launch                                     |
| **Budget Requested**    | $15,000                                         |
| **Maintenance Reserve** | $12,500                                         |
| **Other**               | $2,500                                          |

## Project Description

The Flutter Stellar SDK is a Dart library for building Stellar applications on iOS, Android, and web
using Flutter. It provides transaction building, account management, Horizon API access, Soroban RPC
support, high-level Soroban smart contract support, and implements 21 Stellar Ecosystem Proposals
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
Stellar SDK, and the Kotlin Multiplatform Stellar SDK. I work full-time in the Stellar ecosystem; the
SDKs are my main work.

Previous SCF participation:

- Multiple SCF Build Awards, including the KMP Stellar SDK OZ smart account support and wallet SDKs
  for Dart and Swift
- SCF Public Goods Award since Q3 2025 (Batch 1) for the iOS, Flutter, and PHP SDKs, and since Q3
  2026 for the KMP SDK

Bence ([ngybnc][ngybnc]) is a Soneso team member and works with me on the SDK. He first worked on the
Flutter SDK in 2022, returned to it in September 2026, and authored the Native ScVal Conversion
deliverable and the SEP-29 memo-required check of Q3 2026.

## Retroactive Impact

In Q3 2026 the SDK shipped six releases, 3.3.0 through 3.8.0. Users include Stack Wallet, Beans App,
and Meru. At the close of the quarter: 88 stars, 36 forks, 116 releases, 2,326 downloads on pub.dev
in the last 30 days, 0 open issues, and 0 open pull requests. Over the last 90 days every community
issue got a first maintainer response within 48 hours. Unit test coverage is tracked on Codecov and
enforced in CI with a 90% project target, currently at 94.36%.

SEP-51 (XDR-JSON) shipped in 3.5.0. Apps can now convert any Stellar XDR data, the binary format of
transactions and ledger data, to readable JSON and back. The format is the SEP-51 standard, which the
Python and PHP SDKs use as well. Developers can inspect and debug transactions and contract data in
that form and exchange it with other tools.

Native ScVal Conversion shipped in 3.7.0. When an app calls a smart contract, the answer comes back
in Stellar's binary format, which the app had to take apart by hand. The new helper turns such a
value into a plain Dart value with one call, so apps can use contract results directly and with less
code. Bence ([ngybnc][ngybnc]), a Soneso team member, returned to the Flutter SDK work this quarter
and authored this deliverable.

The Contract Bindings Update keeps the Dart output of the community code generator, which the Stellar
CLI points developers to, in step with the SDK. Developers can generate ready-to-use Dart code for
talking to a smart contract with one command. That code builds and runs on the current SDK, including
contracts that use external-reference executables (Protocol 28).

The SDK supported every network upgrade of the quarter ahead of time. Protocol 27, the upgrade the
proposal named, was tracked through its mainnet activation on 2026-07-08, and the SDK now uses the
new authorization format it introduced (CAP-71) by default. Support for Protocol 28 followed in 3.6.0
on 2026-08-24, 23 days before the network switched on 2026-09-16. App developers had time to update
for its main new feature, contracts that share code through external references (CAP-85), before it
went live.

Maintenance made the SDK safer and easier to maintain. By default the SDK now checks before
submitting whether a receiving account requires a memo (SEP-29), a feature the proposal did not name.
A payment to an exchange that needs a memo is stopped before it goes out without one. Keys,
addresses, amounts, and binary data are validated more strictly, so a mistyped address or an
out-of-range amount is caught early. The request and operation builders now share common code, as the
proposal promised, which leaves less duplicated code to maintain.

Smart accounts became easier to build into wallets. A wallet can now install policies, such as a
spending limit, at the moment it creates an account, an addition the proposal did not name. Input the
contract would reject, such as an overlong rule name or too many policies on one rule, is caught
before sending, so the wallet learns of it without paying a fee. And every error the OpenZeppelin
smart-account contracts can return is translated into a named error the wallet can explain to its
user.

Documentation kept pace: the [SEP guides][sepguides] index covers all 21 implemented SEPs, and
migration guides for 3.6.0 and 3.8.0 walk developers through those releases' breaking changes. The
compatibility matrices show full coverage of Horizon and Soroban RPC through v28.0.1, and every SEP
matrix is at 100%. CI stays hardened with pinned Actions, Dependabot updates, and tests on the
minimum, previous, and latest stable Flutter. SBOM submission to PG Atlas continues on every push to
the default branch, and daily statistics collection continues through [soneso-sdk-stats][statsdash],
which tracks maintenance and usage of the SDK.

## Past Deliverables

### 2026 Q3

#### 1. Continuous Maintenance and Improvement (2026 Q3)

Description from last quarter:

> Regular SDK updates addressing Horizon, Soroban RPC, and protocol updates (tracking Protocol 27
> through its mainnet activation), bug fixes, feature requests, and documentation updates. Maintain
> existing SEP implementations and update as needed. Harden the smart-account feature as the network
> advances and reduce code duplication in the Horizon request builders and operation builders. Keep
> compatibility matrices, CI pipelines, statistics dashboard, and SBOM workflow up to date.

Proof of completion:

- Release notes: [3.3.0][rel330], [3.4.0][rel340], [3.5.0][rel350], [3.6.0][rel360], [3.7.0][rel370],
  [3.8.0][rel380]
- Protocol 27 tracked through its mainnet activation: CAP-71 `useUpgradedAuth` simulation flag and
  RPC v27.1 fields (3.3.0), ADDRESS_V2 credentials as the default (3.6.0): [PR #159][pr159],
  [PR #178][pr178]
- Support for Protocol 28 ahead of its mainnet activation: CAP-85 external-reference executables in
  XDR (3.5.0), external-reference resolution, deployment from an external reference, and contract id
  derivation (3.6.0): [PR #167][pr167], [PR #174][pr174], [PR #175][pr175],
  [protocol delivery ledger][protoledger]
- Feature requests, both answered in about 1.5 hours: the CAP-71 simulation flag, available since
  3.3.0, and Protocol 28 compatibility, shipped in 3.6.0: [issue #172][is172], [issue #176][is176]
- Horizon and XDR updates: diagnostic events decoded in simulation responses (3.4.0), ids in the form
  Horizon serves (3.6.0, 3.8.0), XDR definitions at the current upstream stellar-xdr (3.7.0):
  [PR #161][pr161], [PR #173][pr173], [PR #197][pr197], [PR #186][pr186]
- Soroban submission: fee-bump base fee and automatic state restore (3.3.0), pending and duplicate
  results polled to an outcome (3.5.0): [PR #158][pr158], [commit 9776935][c9776935]
- Stricter input validation: ids, key lengths, amounts, and prices, with prices rendered and parsed
  exactly (3.4.0 to 3.8.0): [PR #161][pr161], [PR #173][pr173], [PR #177][pr177], [PR #187][pr187],
  [PR #196][pr196]
- XDR decoding hardened: every read bounded, malformed and unknown XDR rejected (3.8.0):
  [PR #195][pr195], [PR #197][pr197]
- SEP-10 challenge validation: nonce and operation values checked (3.3.0): [PR #158][pr158]
- SEP-6, SEP-7, SEP-11, SEP-23, SEP-24, and SEP-45 updates: strict strkeys, fixed-width TxRep values,
  and fee amounts as plain decimals (3.6.0), entry-count bounds and union checks (3.8.0):
  [PR #173][pr173], [PR #177][pr177], [PR #195][pr195]
- Smart-account hardening: contract limits and error catalog (3.4.0), external-reference guard and
  deployment polling (3.5.0), ADDRESS_V2 defaults (3.6.0), demo app kept on the current SDK:
  [PR #162][pr162], [PR #167][pr167], [commit 9776935][c9776935], [PR #178][pr178],
  [demo app commit][c2c4f1ba]
- Request and operation builders deduplicated: one shared base for 26 operation builders and 17
  request builders, 1,294 net lines removed (3.4.0): [commit 5a41c90][c5a41c90], [PR #161][pr161]
- Documentation: Soroban guide sections for external references and the new credentials, SEP-23 guide
  revised, examples corrected, migration guides for 3.6.0 and 3.8.0: [Soroban guide][sorobanguide],
  [SEP-23 guide][sep23doc], [PR #179][pr179], [PR #194][pr194], [3.6.0 guide][mig360],
  [3.8.0 guide][mig380]
- Compatibility matrices regenerated every release, Horizon and RPC at 100% through v28.0.1 and every
  SEP matrix at 100% (3.8.0): [Horizon][q3horizon], [RPC][q3rpc], [SEP][q3sep]
- CI, SBOM, and dashboard: Codecov 90% project target as a required check, tests on the minimum,
  previous, and latest stable Flutter, XDR generator on a patched xdrgen fork with the fix proposed
  upstream, SBOM submitted to PG Atlas on every push to the default branch, statistics dashboard
  rebuilt with the SDK's maintenance profile: [commit 1235028][c1235028], [commit e6c2c3a][ce6c2c3a],
  [commit 5a976d0][c5a976d0], [stellar/xdrgen PR #231][xdrgen231], [SBOM runs][sbomruns],
  [dashboard][statsdash]

Six releases shipped this quarter. Protocol 27 was tracked through its mainnet activation, and
support for Protocol 28 followed in 3.6.0 on 2026-08-24, 23 days before the network switched on
2026-09-16. Compatibility matrices were regenerated for every release: Horizon and RPC report 100%
through v28.0.1, and every SEP matrix reports 100%.

#### 2. SEP-51 (XDR-JSON)

Description from last quarter:

> Implement bi-directional XDR/JSON conversion via the XDR generator, with round-trip unit tests and
> documentation, for cross-SDK parity with the Python and PHP SDKs.

Delivered in 3.5.0 (2026-08-11).

Proof of completion:

- GitHub release: [3.5.0][rel350]
- PR with implementation and round-trip tests (3.5.0): [PR #171][pr171], [test suite][testsuite]
- SEP-51 compatibility matrix, 39 of 39 fields: [SEP-51 matrix][sep51matrix]
- Documentation: [SEP-51 guide][sep51doc]
- Conformance checked against stored reference data on every pull request that changes the XDR code
  and against the reference implementation weekly: [conformance workflow][conformanceworkflow]

Every XDR type converts to and from the SEP-51 JSON form with `toXdrJson()` and `fromXdrJson()`.
Round-trip tests run in CI, including three browser suites on Chrome.

#### 3. Native ScVal Conversion

Description from last quarter:

> Add a helper that converts a smart-contract value (XdrSCVal) to a native Dart value, so contract
> invocation and simulation results can be consumed directly instead of parsing the raw XDR union by
> hand. This matches the JS and Python SDKs.

Delivered in 3.7.0 (2026-09-15).

Proof of completion:

- GitHub release: [3.7.0][rel370]
- PR with implementation and tests (3.7.0): [PR #180][pr180]
- Documentation: [PR #181][pr181], [guide section][guidesection]

`XdrSCVal.toNative()` turns contract values into plain Dart values with one call and never throws.
64-bit and wider integers come back as `BigInt`, and values without a Dart counterpart, such as
contract errors, come back unchanged. The helper is documented in the Soroban guide and the agent
skill reference.

#### 4. Contract Bindings Update

Description from last quarter:

> Update the Dart contract-bindings implementation that Soneso contributed to the community
> stellar-contract-bindings generator (linked from the Stellar CLI) so its generated Dart code is
> compatible with the current SDK.

Delivered in stellar-contract-bindings 0.6.0b0 (2026-09-02). The generator PR merged on 2026-07-21.

Proof of completion:

- Pull request to stellar-contract-bindings, Dart output updated for the current SDK:
  [PR #22][scb22], [Flutter commit][scb22flutter]
- Follow-up, spec-text escaping for multi-line contract docs: [PR #36][scb36]
- Follow-up, CAP-85 external-reference resolution in the generator: [PR #37][scb37]
- Generator release: [0.6.0b][scbrel]
- Generated Dart clients tested against testnet in the SDK repository, two added in 3.3.0, all
  regenerated with the released generator (3.7.0): [generated clients][generatedclients],
  [PR #157][pr157], [PR #183][pr183]
- The Stellar CLI command `stellar contract bindings flutter` points to this generator:
  [flutter.rs][clibind]

Six generated clients run as testnet integration tests in the SDK repository, two of them added this
quarter. The generator's Dart output requires SDK 3.3.0 or later and covers contracts that share code
through external references.

#### Beyond the committed scope (2026 Q3)

The following work was not named in the Q3 proposal.

- SEP-29 memo-required check on every submission, with a SEP-29 compatibility matrix, authored by
  Bence ([ngybnc][ngybnc]) (3.8.0): [PR #190][pr190], [SEP-29 guide][sep29doc]
- Constructor-time smart-account policies (3.4.0): [PR #162][pr162]

### 2026 Q2

#### 1. Continuous Maintenance and Improvement

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

#### 2. OpenZeppelin Smart Account Support

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

##### SDK implementation

Proof of completion:

- Release 3.1.0: https://github.com/Soneso/stellar_flutter_sdk/releases/tag/3.1.0
- PR 148: https://github.com/Soneso/stellar_flutter_sdk/pull/148

A two-layer design separates a contract-agnostic core from the OpenZeppelin layer, so other
smart-account contract families can be supported without rewriting the cryptographic core. All
committed sub-items - wallet lifecycle, context rules and policies, automatic auth-entry signing,
multi-signer authorization, fee sponsoring via relayer, credential discovery via indexer, and
cross-platform WebAuthn - are present and tested.

##### Cross-platform demo

Proof of completion:

- Repository: https://github.com/Soneso/flutter-oz-smartaccount-demo
- Platforms: ios/ (iOS 16.0+), android/ (API 28+), web/ (modern WebAuthn browser)
- Real deployed relayer proxy (Cloudflare Worker), exercised in the transfer and approval flows
- Indexer integration and Reown (mobile) / Freighter (web) wallet-connect

The demo exercises the smart-account features: wallet creation and connection (passkey, indexer, and
address recovery), single- and multi-signer token transfers, on-chain context-rule management with
signers, policies, and expiry, SEP-41 token allowances, and the agent delegation and approval-inbox
flow.

##### Documentation

Proof of completion:

- [Smart-account documentation set][sadocs]: onboarding guide, API reference, and per-platform
  WebAuthn guides (iOS, Android, web)

##### Agent-signer flow in the demo app

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

Keep the SDK compatible with Horizon, Soroban RPC, and protocol updates, starting with the Horizon
and RPC 29.0.0 releases. Maintain existing SEP implementations and update as needed. Fix bugs and
respond to issues and feature requests.

Make the SDK more reliable for the apps that use it. In addition to the regular maintenance, this
quarter will run a hardening round: an AI-assisted review of the whole SDK has proposed a list of
security hardening measures, bug fixes, and improvements to code, tests, and documentation. The round
will validate each proposal and work through the valid ones as far as the quarter allows.

Make Stellar assets easier to use in apps that work with smart contracts. Add a Stellar Asset
Contract toolkit, so an app can open XLM or any issued asset as a Soroban contract with the same
client it uses for other contracts, look up the asset's contract id, read a balance, and build a
transfer. The JS SDK already provides this.

## Proposed Deliverables

### Continuous Maintenance and Improvement

Regular SDK updates addressing Horizon, Soroban RPC, and protocol updates (the Horizon and RPC 29.0.0
releases, then every following protocol release, each supported before its mainnet activation), bug
fixes, feature requests, and documentation updates. Maintain existing SEP implementations and update
as needed. Keep compatibility matrices, the AI agent skill, CI pipelines, statistics dashboard, and
SBOM workflow up to date.

Hardening round: an AI-assisted review of the whole SDK has proposed a list of security hardening
measures, bug fixes, and improvements to code, tests, and documentation. We will check and validate
each proposal; valid proposals will become issues in the repository, labeled as part of this round,
and will be worked through as far as the quarter allows, security hardening and bug fixes first, then
the improvements.

Dated duties: the SDK's dependency data will keep reaching PG Atlas through GitHub's API change on
2026-11-13. Before GitHub moves its default runners to Ubuntu 26.04 (rollout 2026-10-19 to
2026-11-19), we will verify the Linux CI jobs (tests, documentation, SBOM submission, SEP-51
conformance, XDR generator, XDR update check, AI PR review) on Ubuntu 26.04 and adapt them where they
break.

Commitments for the quarter, each checkable from public data:

1. First maintainer response to every community issue and pull request within 48 hours. Proof:
   responsiveness panel of the [soneso-sdk-stats dashboard][statsdash].
2. Every protocol release supported before its mainnet activation, with the Horizon and RPC matrices
   regenerated at each Horizon and RPC release. Proof: [protocol delivery ledger][protoledger],
   matrix headers.
3. Unit test coverage at or above 90% under the required Codecov check; Horizon, RPC, and every SEP
   matrix at 100% at each release. Proof: Codecov report, matrices in the repository.
4. No release with an open dependency advisory, with Dependabot covering every dependency manifest.
   Proof: release notes, Dependabot configuration.
5. The dated duties done by their dates. Proof: workflow runs.

Proof: Release notes on GitHub, the labeled issues of the hardening round and their PRs, updated
compatibility matrices, workflow runs, the Codecov report, and the soneso-sdk-stats dashboard.

### Stellar Asset Contract Toolkit

Add Stellar Asset Contract (SAC) support to the high-level contract client: a client for an asset's
contract opened from the SAC interface description shipped with the SDK, the contract id derived from
the asset, a balance read, a transfer builder, and read calls that need no funded account, with unit
tests, a testnet integration test, a documentation section, and the agent skill reference.

Proof: GitHub release, PR with implementation and tests, documentation.

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aflutter_stellar_sdk&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aflutter_stellar_sdk)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aflutter_stellar_sdk&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aflutter_stellar_sdk)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aflutter_stellar_sdk&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aflutter_stellar_sdk)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aflutter_stellar_sdk&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aflutter_stellar_sdk)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

[agflow]:
  https://github.com/Soneso/flutter-oz-smartaccount-demo/blob/main/documentation/agent-flow.md
[c1235028]: https://github.com/Soneso/stellar_flutter_sdk/commit/1235028
[c2c4f1ba]: https://github.com/Soneso/flutter-oz-smartaccount-demo/commit/2c4f1ba
[c5a41c90]: https://github.com/Soneso/stellar_flutter_sdk/commit/5a41c90
[c5a976d0]: https://github.com/Soneso/stellar_flutter_sdk/commit/5a976d0
[c9776935]: https://github.com/Soneso/stellar_flutter_sdk/commit/9776935
[ce6c2c3a]: https://github.com/Soneso/stellar_flutter_sdk/commit/e6c2c3a
[clibind]:
  https://github.com/stellar/stellar-cli/blob/main/cmd/soroban-cli/src/commands/contract/bindings/flutter.rs
[conformanceworkflow]:
  https://github.com/Soneso/stellar_flutter_sdk/blob/3.5.0/.github/workflows/sep-51-conformance.yml
[deleg]:
  https://github.com/Soneso/flutter-oz-smartaccount-demo/blob/main/documentation/smart-accounts/agent-delegation-demo.md
[demopr1]: https://github.com/Soneso/flutter-oz-smartaccount-demo/pull/1
[generatedclients]: https://github.com/Soneso/stellar_flutter_sdk/tree/3.8.0/test/contract_bindings
[guidesection]:
  https://github.com/Soneso/stellar_flutter_sdk/blob/3.7.0/documentation/soroban.md#converting-to-native-dart-values
[is172]: https://github.com/Soneso/stellar_flutter_sdk/issues/172
[is176]: https://github.com/Soneso/stellar_flutter_sdk/issues/176
[mig360]: https://github.com/Soneso/stellar_flutter_sdk/blob/3.6.0/documentation/migration/3.6.0.md
[mig380]: https://github.com/Soneso/stellar_flutter_sdk/blob/3.8.0/documentation/migration/3.8.0.md
[ngybnc]: https://github.com/ngybnc
[pr140]: https://github.com/Soneso/stellar_flutter_sdk/pull/140
[pr148]: https://github.com/Soneso/stellar_flutter_sdk/pull/148
[pr150]: https://github.com/Soneso/stellar_flutter_sdk/pull/150
[pr151]: https://github.com/Soneso/stellar_flutter_sdk/pull/151
[pr152]: https://github.com/Soneso/stellar_flutter_sdk/pull/152
[pr157]: https://github.com/Soneso/stellar_flutter_sdk/pull/157
[pr158]: https://github.com/Soneso/stellar_flutter_sdk/pull/158
[pr159]: https://github.com/Soneso/stellar_flutter_sdk/pull/159
[pr161]: https://github.com/Soneso/stellar_flutter_sdk/pull/161
[pr162]: https://github.com/Soneso/stellar_flutter_sdk/pull/162
[pr167]: https://github.com/Soneso/stellar_flutter_sdk/pull/167
[pr171]: https://github.com/Soneso/stellar_flutter_sdk/pull/171
[pr173]: https://github.com/Soneso/stellar_flutter_sdk/pull/173
[pr174]: https://github.com/Soneso/stellar_flutter_sdk/pull/174
[pr175]: https://github.com/Soneso/stellar_flutter_sdk/pull/175
[pr177]: https://github.com/Soneso/stellar_flutter_sdk/pull/177
[pr178]: https://github.com/Soneso/stellar_flutter_sdk/pull/178
[pr179]: https://github.com/Soneso/stellar_flutter_sdk/pull/179
[pr180]: https://github.com/Soneso/stellar_flutter_sdk/pull/180
[pr181]: https://github.com/Soneso/stellar_flutter_sdk/pull/181
[pr183]: https://github.com/Soneso/stellar_flutter_sdk/pull/183
[pr186]: https://github.com/Soneso/stellar_flutter_sdk/pull/186
[pr187]: https://github.com/Soneso/stellar_flutter_sdk/pull/187
[pr190]: https://github.com/Soneso/stellar_flutter_sdk/pull/190
[pr194]: https://github.com/Soneso/stellar_flutter_sdk/pull/194
[pr195]: https://github.com/Soneso/stellar_flutter_sdk/pull/195
[pr196]: https://github.com/Soneso/stellar_flutter_sdk/pull/196
[pr197]: https://github.com/Soneso/stellar_flutter_sdk/pull/197
[pr44resp]:
  https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/pull/44#issuecomment-4274930402
[protoledger]: https://github.com/Soneso/soneso-sdk-stats/blob/main/curated/protocol-delivery.json
[q3horizon]:
  https://github.com/Soneso/stellar_flutter_sdk/blob/3.8.0/compatibility/horizon/HORIZON_COMPATIBILITY_MATRIX.md
[q3rpc]:
  https://github.com/Soneso/stellar_flutter_sdk/blob/3.8.0/compatibility/rpc/RPC_COMPATIBILITY_MATRIX.md
[q3sep]: https://github.com/Soneso/stellar_flutter_sdk/tree/3.8.0/compatibility/sep
[rel310]: https://github.com/Soneso/stellar_flutter_sdk/releases/tag/3.1.0
[rel320]: https://github.com/Soneso/stellar_flutter_sdk/releases/tag/3.2.0
[rel330]: https://github.com/Soneso/stellar_flutter_sdk/releases/tag/3.3.0
[rel340]: https://github.com/Soneso/stellar_flutter_sdk/releases/tag/3.4.0
[rel350]: https://github.com/Soneso/stellar_flutter_sdk/releases/tag/3.5.0
[rel360]: https://github.com/Soneso/stellar_flutter_sdk/releases/tag/3.6.0
[rel370]: https://github.com/Soneso/stellar_flutter_sdk/releases/tag/3.7.0
[rel380]: https://github.com/Soneso/stellar_flutter_sdk/releases/tag/3.8.0
[sadocs]: https://github.com/Soneso/stellar_flutter_sdk/tree/master/documentation/smart-accounts
[sbomruns]: https://github.com/Soneso/stellar_flutter_sdk/actions/workflows/sbom.yml
[scb22]: https://github.com/lightsail-network/stellar-contract-bindings/pull/22
[scb22flutter]: https://github.com/lightsail-network/stellar-contract-bindings/commit/6c987d94e
[scb36]: https://github.com/lightsail-network/stellar-contract-bindings/pull/36
[scb37]: https://github.com/lightsail-network/stellar-contract-bindings/pull/37
[scbrel]: https://github.com/lightsail-network/stellar-contract-bindings/releases/tag/0.6.0b
[sep23doc]: https://github.com/Soneso/stellar_flutter_sdk/blob/3.8.0/documentation/sep/sep-23.md
[sep29doc]: https://github.com/Soneso/stellar_flutter_sdk/blob/3.8.0/documentation/sep/sep-29.md
[sep51doc]: https://github.com/Soneso/stellar_flutter_sdk/blob/3.5.0/documentation/sep/sep-51.md
[sep51matrix]:
  https://github.com/Soneso/stellar_flutter_sdk/blob/3.5.0/compatibility/sep/SEP-0051_COMPATIBILITY_MATRIX.md
[sepguides]: https://github.com/Soneso/stellar_flutter_sdk/blob/master/documentation/sep/README.md
[sorobanguide]: https://github.com/Soneso/stellar_flutter_sdk/blob/3.8.0/documentation/soroban.md
[statsdash]: https://soneso.github.io/soneso-sdk-stats/
[testsuite]: https://github.com/Soneso/stellar_flutter_sdk/tree/3.5.0/test/unit/xdr/json_generated
[xdrgen231]: https://github.com/stellar/xdrgen/pull/231
