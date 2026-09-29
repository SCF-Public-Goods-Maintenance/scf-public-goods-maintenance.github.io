---
title: "stellar-ios-mac-sdk"
canonical_id: daoip-5:scf:project:stellar_ios_mac_sdk
parent: Public Good Projects
proposal_issue: 41
proposer: christian-rogobete
category: "SDKs"
budget: "15000"
---

# stellar-ios-mac-sdk

_The Stellar SDK for iOS and macOS, providing transaction building, Horizon and Soroban RPC access,
high-level Soroban smart contract support, and implements 21 Stellar Ecosystem Proposals (SEPs)._

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
high-level Soroban smart contract support, and implements 21 Stellar Ecosystem Proposals (SEPs). The
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

In Q3 2026 the SDK shipped seven releases, 3.7.0 through 3.12.0. Users include LOBSTR and Unstoppable
Wallet. At the close of the quarter: 132 stars, 55 forks, 151 releases, 0 open issues, and 0 open
pull requests. Over the last 90 days every community issue and pull request got a first maintainer
response within 48 hours. Unit test coverage is tracked on Codecov and enforced in CI with a 90%
project target, currently at 92.97%.

SEP-51 (XDR-JSON) shipped in 3.9.0. Apps can now convert any Stellar XDR data, the binary format of
transactions and ledger data, to readable JSON and back, in the standard form defined by SEP-51 that
the Python and PHP SDKs use as well. That makes transactions and contract data easy to inspect, log,
and exchange with other tools.

Native ScVal Conversion shipped in 3.11.0. When an app calls a smart contract, the answer comes back
in Stellar's binary format, which the app had to take apart by hand. The new helper turns any such
value into a plain Swift value with one call, so apps can use contract results directly and with less
code. Bence ([ngybnc][ngybnc]), a Soneso team member, joined the iOS SDK work this quarter and
authored this deliverable.

The Contract Bindings Update keeps the Swift output of the community code generator, which the
Stellar CLI points developers to, in step with the SDK. Developers can generate ready-to-use Swift
code for talking to any smart contract with one command, and the generated code builds and runs on
the current SDK, including contracts that use external-reference executables (Protocol 28).

The SDK supported every network upgrade of the quarter ahead of time. Protocol 27, the upgrade the
proposal named, was tracked through its mainnet activation on 2026-07-08, and the SDK now uses the
new authorization format it introduced (CAP-71) by default. Support for Protocol 28 followed in
3.10.0 on 2026-08-25, 22 days before the network switched on 2026-09-16, so app developers had time
to update for its main new feature, contracts that share code through external references (CAP-85),
before it went live.

Maintenance made the SDK safer for users. Addresses and binary data are validated more strictly
before use, so a mistyped address or a malformed data packet is caught early, and the memo-required
check (SEP-29) now also covers fee-bump transactions, so a payment to an exchange that requires a
memo is stopped before it goes out.

Smart accounts became easier to build into wallets. A wallet can now install policies, such as a
spending limit, at the moment it creates an account, an addition the proposal did not name. Input
that the smart-account contract would reject, such as an overlong rule name or too many policies on
one rule, is caught before the transaction is sent, so the wallet learns about it without paying a
fee. And every error the OpenZeppelin smart-account contracts can return is translated into a named
error the wallet can explain to its user.

Documentation kept pace: the README and 17 SEP guides were improved, the [SEP guides][sepguides]
index now covers all 21 implemented SEPs, and migration guides walk developers through the two
releases with breaking changes, 3.10.0 and 3.12.0. The compatibility matrices show full coverage of
Horizon and Soroban RPC through v28.0.1, and every SEP matrix is at 100%. CI stays hardened with
pinned Actions, Dependabot updates, and a daily check that flags upstream XDR changes the day they
land. SBOM submission to PG Atlas continues on every push to the default branch, and daily statistics
collection continues through [soneso-sdk-stats][statsdash], which tracks maintenance and usage of the
SDK.

## Past Deliverables

### 2026 Q3

#### 1. Continuous Maintenance and Improvement (2026 Q3)

Description from last quarter:

> Regular SDK updates addressing Horizon, Soroban RPC, and protocol updates (tracking Protocol 27
> through its mainnet activation), bug fixes, feature requests, and documentation updates. Maintain
> existing SEP implementations and update as needed. Harden the smart-account feature as the network
> advances. Keep compatibility matrices, CI pipelines, statistics dashboard, and SBOM workflow up to
> date.

Proof of completion:

- Release notes: [3.7.0][rel370], [3.8.0][rel380], [3.8.1][rel381], [3.9.0][rel390],
  [3.10.0][rel3100], [3.11.0][rel3110], [3.12.0][rel3120]
- Protocol 27 tracked through its mainnet activation: CAP-71 `useUpgradedAuth` simulation flag and
  RPC v27.1 fields (3.7.0), ADDRESS_V2 credentials as the default (3.10.0): [PR #218][pr218],
  [commit 76ee91184][c76ee911], [PR #237][pr237]
- Support for Protocol 28 ahead of its mainnet activation: CAP-85 external-reference executables in
  XDR and TxRep (3.8.1), external-reference resolution, deployment from an external reference, and
  contract id derivation (3.10.0): [PR #225][pr225], [PR #233][pr233], [PR #234][pr234],
  [protocol delivery ledger][protoledger]
- Feature requests, both answered in about 1.5 hours: the CAP-71 simulation flag, available since
  3.7.0, and Protocol 28 compatibility, shipped in 3.10.0: [issue #231][is231], [issue #235][is235]
- Horizon and XDR updates: claimable balance ids resolved in every spelling (3.10.0), XDR definitions
  kept at upstream stellar-xdr (3.8.0 to 3.11.0): [PR #232][pr232], [PR #244][pr244]
- Soroban submission: pending and duplicate results polled to an outcome, the last per-attempt
  failure reported (3.8.0, 3.9.0): [commit 2a1fcae70][c2a1fcae], [commit 2f1258157][c2f12581]
- Stricter input validation: wide-integer parsing, hex id lengths, binary reads, and XDR decode
  limits (3.9.0 to 3.12.0): [PR #230][pr230], [PR #232][pr232], [PR #249][pr249], [PR #250][pr250]
- Community bug fix, mnemonic creation checks the random-bytes result (3.8.1): [PR #229][pr229]
- SEP-23 strkey checks hardened to the js-stellar-sdk v17 level (3.10.0): [PR #232][pr232]
- SEP-6 and SEP-24 fee amounts as plain decimals, SEP-9 numeric fields as decimal text, SEP-11
  fixed-width fields (3.10.0): [PR #236][pr236], [commit 2e934b80e][c2e934b]
- SEP-29 memo-required check on fee-bump submissions (3.12.0): [PR #247][pr247]
- Smart-account hardening: contract limits and error catalog (3.8.0), external-reference guard
  (3.8.1), ADDRESS_V2 defaults (3.10.0), signer public key helper (3.12.0), demo app updated through
  3.12.0: [PR #220][pr220], [PR #225][pr225], [PR #237][pr237], [PR #250][pr250],
  [demo app commits][sademo]
- Documentation: CAP-85 and ADDRESS_V2 guide sections, corrections across the README and 17 SEP
  guides, migration guides for 3.10.0 and 3.12.0, API reference regenerated every release:
  [PR #238][pr238], [commit 5ec592b78][c5ec592b], [3.10.0 guide][mig3100], [3.12.0 guide][mig3120],
  [API reference][iosapi]
- Compatibility matrices regenerated every release, Horizon and RPC at 100% through v28.0.1 and every
  SEP matrix at 100% (3.12.0): [Horizon][q3horizon], [RPC][q3rpc], [SEP][q3sep]
- CI, SBOM, and dashboard: Codecov 90% project target as a required check, XDR generator on a patched
  xdrgen fork with the fix proposed upstream, SBOM submitted to PG Atlas on every push to the default
  branch, statistics dashboard rebuilt with the SDK's maintenance profile:
  [commit f70517734][cf705177], [commit 98867cd00][c98867cd], [stellar/xdrgen PR #231][xdrgen231],
  [SBOM runs][sbomruns], [dashboard][statsdash]

Seven releases shipped this quarter. Protocol 27 was tracked through its mainnet activation, and
support for Protocol 28 followed in 3.10.0 on 2026-08-25, 22 days before the network switched on
2026-09-16. Compatibility matrices were regenerated for every release: Horizon and RPC report 100%
through v28.0.1, and every SEP matrix reports 100%.

#### 2. SEP-51 (XDR-JSON)

Description from last quarter:

> Implement bi-directional XDR/JSON conversion via the XDR generator, with round-trip unit tests and
> documentation, for cross-SDK parity with the Python and PHP SDKs.

Delivered in 3.9.0 (2026-08-11).

Proof of completion:

- GitHub release: [3.9.0][rel390]
- PR with implementation and round-trip tests (3.9.0): [PR #230][pr230], [test suite][sep51tests]
- SEP-51 compatibility matrix, 47 of 47 fields: [SEP-51 matrix][sep51matrix]
- Documentation: [SEP-51 guide][sep51doc]
- Weekly check of the JSON field names against the reference implementation:
  [reference watch][sep51watch]

Generated XDR types convert to and from the SEP-51 JSON form with `toXdrJson()` and
`fromXdrJson(String)`. Round-trip tests run in CI, and the guide's examples run as doc tests.

#### 3. Native ScVal Conversion

Description from last quarter:

> Add a helper that converts a smart-contract value (SCValXDR) to a native Swift value, so contract
> invocation and simulation results can be consumed directly instead of parsing the raw XDR union by
> hand. This matches the JS and Python SDKs.

Delivered in 3.11.0 (2026-09-15).

Proof of completion:

- GitHub release: [3.11.0][rel3110]
- PR with implementation and tests (3.11.0): [PR #240][pr240]
- Documentation: [PR #241][pr241], [guide section][scvaldoc]

`SCValXDR.toNative()` turns contract values into plain Swift values with one call and never throws.
Values without a Swift counterpart come back unchanged. `SCAddressXDR.toStrKey()` encodes all five
address kinds. Both are documented in the Soroban guide and the agent skill reference.

#### 4. Contract Bindings Update

Description from last quarter:

> Update the Swift contract-bindings implementation that Soneso contributed to the community
> stellar-contract-bindings generator (linked from the Stellar CLI) so its generated Swift code is
> compatible with the current SDK.

Delivered in stellar-contract-bindings 0.6.0b0 (2026-09-02). The generator PR merged on 2026-07-21.

Proof of completion:

- Pull request to stellar-contract-bindings, Swift output updated for the current SDK:
  [PR #22][scb22], [Swift commit][scb22swift]
- Follow-up, spec-text escaping for multi-line contract docs: [PR #36][scb36]
- Follow-up, CAP-85 external-reference resolution in the generator: [PR #37][scb37]
- Generator release: [0.6.0b][scbrel]
- Generated Swift clients tested against testnet in the SDK repository, regenerated with the released
  generator (3.11.0): [generated clients][bindfix], [PR #242][pr242]
- The Stellar CLI command `stellar contract bindings swift` points to this generator:
  [swift.rs][clibind]

Six generated clients run as testnet integration tests in the SDK repository, two of them added this
quarter. The generator's Swift output compiles against the current SDK and covers contracts that
share code through external references.

#### Beyond the committed scope (2026 Q3)

The following work was not named in the Q3 proposal.

- Smart-account constructor-time policies, `defaultPolicies` and per-call `policies` (3.8.0):
  [PR #220][pr220]

### 2026 Q2

#### 1. Continuous Maintenance and Improvement Deliverable

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

#### 2. SEP-11 TxRep Rewrite

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

#### 3. OpenZeppelin Smart Account Support

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

##### SDK implementation

Proof of completion:

- Release 3.5.0: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.5.0
- PR 208: https://github.com/Soneso/stellar-ios-mac-sdk/pull/208

A two-layer design separates a contract-agnostic core (passkey/WebAuthn, secp256r1) from the
OpenZeppelin layer, so other smart-account contract families can be supported without rewriting the
cryptographic core. All committed sub-items - wallet lifecycle, context rules and policies, automatic
auth-entry signing, multi-signer authorization, fee sponsoring via relayer, credential discovery via
indexer, and native ASAuthorization WebAuthn on iOS and macOS - are present and tested.

##### Demo app

Proof of completion:

- Repository: https://github.com/Soneso/ios-oz-smartaccount-demo
- Platforms: iOS and macOS

##### Documentation

Proof of completion:

- [Smart-account documentation set][sadocs]: onboarding guide, API reference, and per-platform
  WebAuthn guides (iOS, macOS)

##### Agent-signer flow in the demo app

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
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_ios_mac_sdk&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_ios_mac_sdk)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_ios_mac_sdk&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_ios_mac_sdk)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

[agflow]: https://github.com/Soneso/ios-oz-smartaccount-demo/blob/main/documentation/agent-flow.md
[bindfix]:
  https://github.com/Soneso/stellar-ios-mac-sdk/tree/3.12.0/stellarsdk/stellarsdkIntegrationTests/soroban/bindings
[c2a1fcae]: https://github.com/Soneso/stellar-ios-mac-sdk/commit/2a1fcae70
[c2e934b]: https://github.com/Soneso/stellar-ios-mac-sdk/commit/2e934b80e
[c2f12581]: https://github.com/Soneso/stellar-ios-mac-sdk/commit/2f1258157
[c5ec592b]: https://github.com/Soneso/stellar-ios-mac-sdk/commit/5ec592b78
[c76ee911]: https://github.com/Soneso/stellar-ios-mac-sdk/commit/76ee91184
[c98867cd]: https://github.com/Soneso/stellar-ios-mac-sdk/commit/98867cd00
[cf705177]: https://github.com/Soneso/stellar-ios-mac-sdk/commit/f70517734
[clibind]:
  https://github.com/stellar/stellar-cli/blob/main/cmd/soroban-cli/src/commands/contract/bindings/swift.rs
[demopr1]: https://github.com/Soneso/ios-oz-smartaccount-demo/pull/1
[iosapi]: https://soneso.github.io/stellar-ios-mac-sdk/
[is231]: https://github.com/Soneso/stellar-ios-mac-sdk/issues/231
[is235]: https://github.com/Soneso/stellar-ios-mac-sdk/issues/235
[mig3100]: https://github.com/Soneso/stellar-ios-mac-sdk/blob/3.12.0/docs/migration/3.10.0.md
[mig3120]: https://github.com/Soneso/stellar-ios-mac-sdk/blob/3.12.0/docs/migration/3.12.0.md
[ngybnc]: https://github.com/ngybnc
[pr208]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/208
[pr211]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/211
[pr212]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/212
[pr213]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/213
[pr214]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/214
[pr218]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/218
[pr220]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/220
[pr225]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/225
[pr229]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/229
[pr230]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/230
[pr232]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/232
[pr233]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/233
[pr234]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/234
[pr236]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/236
[pr237]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/237
[pr238]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/238
[pr240]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/240
[pr241]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/241
[pr242]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/242
[pr244]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/244
[pr247]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/247
[pr249]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/249
[pr250]: https://github.com/Soneso/stellar-ios-mac-sdk/pull/250
[protoledger]: https://github.com/Soneso/soneso-sdk-stats/blob/main/curated/protocol-delivery.json
[q3horizon]:
  https://github.com/Soneso/stellar-ios-mac-sdk/blob/3.12.0/compatibility/horizon/HORIZON_COMPATIBILITY_MATRIX.md
[q3rpc]:
  https://github.com/Soneso/stellar-ios-mac-sdk/blob/3.12.0/compatibility/rpc/RPC_COMPATIBILITY_MATRIX.md
[q3sep]: https://github.com/Soneso/stellar-ios-mac-sdk/tree/3.12.0/compatibility/sep
[rel3100]: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.10.0
[rel3110]: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.11.0
[rel3120]: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.12.0
[rel350]: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.5.0
[rel370]: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.7.0
[rel380]: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.8.0
[rel381]: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.8.1
[rel390]: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.9.0
[sademo]: https://github.com/Soneso/ios-oz-smartaccount-demo/commits/main
[sadocs]: https://github.com/Soneso/stellar-ios-mac-sdk/tree/master/docs/smart-accounts
[sbomruns]: https://github.com/Soneso/stellar-ios-mac-sdk/actions/workflows/sbom.yml
[scb22]: https://github.com/lightsail-network/stellar-contract-bindings/pull/22
[scb22swift]: https://github.com/lightsail-network/stellar-contract-bindings/commit/d91990b8d
[scb36]: https://github.com/lightsail-network/stellar-contract-bindings/pull/36
[scb37]: https://github.com/lightsail-network/stellar-contract-bindings/pull/37
[scbrel]: https://github.com/lightsail-network/stellar-contract-bindings/releases/tag/0.6.0b
[scvaldoc]:
  https://github.com/Soneso/stellar-ios-mac-sdk/blob/3.11.0/docs/soroban.md#converting-to-native-swift-values
[sep51doc]: https://github.com/Soneso/stellar-ios-mac-sdk/blob/3.9.0/docs/sep/sep-51.md
[sep51matrix]:
  https://github.com/Soneso/stellar-ios-mac-sdk/blob/3.9.0/compatibility/sep/SEP-0051_COMPATIBILITY_MATRIX.md
[sep51tests]:
  https://github.com/Soneso/stellar-ios-mac-sdk/tree/3.9.0/stellarsdk/stellarsdkUnitTests/sep/xdr_json
[sep51watch]:
  https://github.com/Soneso/stellar-ios-mac-sdk/blob/3.9.0/.github/workflows/sep-51-reference-watch.yml
[sepguides]: https://github.com/Soneso/stellar-ios-mac-sdk/blob/master/docs/sep/README.md
[statsdash]: https://soneso.github.io/soneso-sdk-stats/
[xdrgen231]: https://github.com/stellar/xdrgen/pull/231
