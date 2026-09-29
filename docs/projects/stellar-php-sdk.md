---
title: "stellar-php-sdk"
canonical_id: daoip-5:scf:project:stellar_php_sdk
parent: Public Good Projects
proposal_issue: 45
proposer: christian-rogobete
category: "SDKs"
budget: "15000"
---

# stellar-php-sdk

_The Stellar SDK for PHP, providing transaction building, Horizon and Soroban RPC access, high-level
Soroban smart contract support, and implements 23 Stellar Ecosystem Proposals (SEPs)._

|                      |                                             |
| -------------------- | ------------------------------------------- |
| **Category**         | SDKs                                        |
| **Website**          | <https://github.com/Soneso/stellar-php-sdk> |
| **Repository**       | <https://github.com/Soneso/stellar-php-sdk> |
| **First Released**   | May 2022                                    |
| **Intake**           | soft-launch                                 |
| **Budget Requested** | 15000                                       |

## Project Description

The Stellar PHP SDK is a PHP library for building Stellar applications on web servers and backend
systems. It provides transaction building, account management, Horizon API access, Soroban RPC
support, high-level Soroban smart contract support, and implements 23 Stellar Ecosystem Proposals
(SEPs). The SDK is listed on the official Stellar developer documentation and is used by projects
including StellarChain.io, cNGN Stablecoin, PHP Anchor SDK, and others.

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

In Q3 2026 the SDK shipped five releases, 1.11.0 through 1.15.0. Users include StellarChain.io and
Montelibero. At the close of the quarter: 42 stars, 21 forks, 89 releases, 0 open issues, 0 open pull
requests, and 62,623 Packagist installs in total, 2,705 in the last 30 days. Over the last 90 days
every community issue and pull request received a first maintainer response within 48 hours. Unit
test coverage is tracked on Codecov and enforced in CI with a 90% project target, currently at
93.19%.

Native ScVal Conversion shipped in 1.14.0. When an app calls a smart contract, the answer comes back
in Stellar's binary format, which developers had to take apart by hand. The new helper turns such a
value into a plain PHP value with one call, so apps can use the results of contract calls and
simulations directly, with less code. Bence ([ngybnc][ngybnc]), a Soneso team member who has worked
on the PHP SDK since 2022, authored this deliverable.

The Contract Bindings Update keeps the PHP output of the community code generator, which the Stellar
CLI points developers to, in step with the SDK. Developers can generate ready-to-use PHP code for
talking to any smart contract with one command, and the generated code runs on the current SDK,
including contracts that use external-reference executables (Protocol 28).

SEP-35 (Operation IDs) shipped in 1.13.0. Every operation on Stellar has an ID that encodes where it
sits in the ledger history, and Horizon uses the same numbers as bookmarks for paging through long
result lists. Backend developers can now compute and read these IDs in their own code without a
network call, for example to start reading history right after a given ledger. Bence authored this
deliverable as well.

The SDK supported every network upgrade of the quarter ahead of time. Protocol 27, the upgrade the
proposal named, was tracked through its mainnet activation on 2026-07-08, and the SDK now uses the
new authorization format it introduced (CAP-71) by default. Support for Protocol 28 followed in
1.13.0 on 2026-08-24, 23 days before the network switched on 2026-09-16. App developers had that time
to prepare for its main new feature, contracts that share code through external references (CAP-85).

Maintenance made the SDK safer for users. The existing memo-required check (SEP-29) now runs by
default inside the SDK's submit methods. A payment without a memo to an account that requires one,
such as an exchange, is stopped before it is sent. Addresses and Stellar's binary data are checked
more strictly, so a mistyped address or damaged data is caught early with a clear error.

Documentation kept pace: the [SEP guides][sepguides] index now covers all 23 implemented SEPs, and
the Soroban guide gained sections on converting contract values and on external references. The
compatibility matrices show full coverage of Horizon and Soroban RPC through v28.0.1, and every SEP
matrix is at 100%. CI was hardened with stricter static code analysis, Dependabot updates, and a
daily check that flags upstream XDR changes. SBOM submission to PG Atlas continues on every push to
the default branch, and daily statistics collection continues through [soneso-sdk-stats][statsdash],
which tracks maintenance and usage of the SDK.

## Past Deliverables

### 2026 Q3

#### 1. Continuous Maintenance and Improvement (2026 Q3)

Description from last quarter:

> Regular SDK updates addressing Horizon, Soroban RPC, and protocol updates (tracking Protocol 27
> through its mainnet activation), bug fixes, feature requests, and documentation updates. Maintain
> existing SEP implementations and update as needed, keep the SEP compatibility matrices current.
> Hold line coverage at 90% or above (currently 92.74%) under the blocking Codecov thresholds. Keep
> compatibility matrices, CI pipelines, statistics dashboard, and SBOM workflow up to date.

Proof of completion:

- Release notes: [1.11.0][rel1110], [1.12.0][rel1120], [1.13.0][rel1130], [1.14.0][rel1140],
  [1.15.0][rel1150]
- Protocol 27 tracked through its mainnet activation: CAP-71 `useUpgradedAuth` simulation flag and
  RPC v27.1 fields (1.11.0), ADDRESS_V2 credentials as the default (1.13.0): [PR #100][pr100],
  [commit b9abda5][cb9abda5], [PR #122][pr122]
- Support for Protocol 28 ahead of its mainnet activation: CAP-85 external-reference executables in
  XDR (1.12.0), external-reference resolution, deployment from an external reference, and contract id
  derivation (1.13.0): [PR #106][pr106], [PR #117][pr117], [PR #118][pr118], [PR #119][pr119],
  [protocol delivery ledger][protoledger]
- Feature requests, both answered in about 1.5 hours: the CAP-71 simulation flag, available since
  1.11.0, and Protocol 28 compatibility, shipped in 1.13.0: [issue #112][is112], [issue #120][is120]
- Horizon and XDR updates: signer effects parsed with the type codes Horizon uses, claimable balance
  ids in the form Horizon serves (1.13.0), XDR definitions at the current upstream stellar-xdr
  (1.14.0): [PR #121][pr121], [PR #114][pr114], [PR #129][pr129]
- Soroban client: contract address conversion from contract values (1.11.0), transaction status
  handling and deployment spec loading (1.12.0): [PR #99][pr99], [commit 0db4af8][c0db4af8]
- Stricter input validation: muxed ids, signed-payload addresses, wasm hashes, amounts, and addresses
  stored in canonical form (1.13.0): [PR #121][pr121], [PR #122][pr122], [PR #114][pr114]
- XDR decoding hardened: union arms, array counts, extension points, and presence words checked,
  undecodable fee-bump and allow-trust XDR reported with a clear error (1.15.0): [PR #135][pr135],
  [PR #137][pr137], [PR #138][pr138]
- SEP-51 output aligned with the reference implementation, unknown and duplicate keys rejected
  (1.12.0), SEP-23 strkey checks hardened to the js-stellar-sdk v17 level (1.12.0, 1.13.0):
  [PR #111][pr111], [commit eebca70][ceebca70], [PR #114][pr114]
- SEP-6, SEP-9, SEP-10, SEP-12, and SEP-24 zero values and amount precision, SEP-11 TxRep id forms
  (1.13.0): [PR #121][pr121], [PR #122][pr122]
- SEP-29 memo-required check inside the submit methods by default, with a SEP-29 compatibility matrix
  and a rewritten guide, authored by Bence ([ngybnc][ngybnc]), with follow-up corrections to the
  guide (1.15.0): [PR #133][pr133], [PR #134][pr134], [PR #136][pr136]
- Documentation: Soroban guide sections on external references and contract id derivation, claimable
  balance id forms, a community documentation contribution, agent skill and API reference regenerated
  every release: [Soroban guide][sorobanguide], [PR #130][pr130], [PR #132][pr132],
  [agent skill][agentskill]
- Compatibility matrices regenerated every release, Horizon and RPC at 100% through v28.0.1 and every
  SEP matrix at 100% (1.15.0): [Horizon][q3horizon], [RPC][q3rpc], [SEP][q3sep]
- Codecov coverage report: line coverage stayed above 92.5% in every Codecov report of the quarter,
  93.19% at 1.15.0, project gate raised from 80% to 90% in 1.15.0 and made a required check:
  [Codecov][codecovapp], [codecov.yml][codecovyml]
- CI, SBOM, and dashboard: static analysis on the hand-written XDR classes, XDR generator on a
  patched xdrgen fork with the fix proposed upstream, SBOM submitted to PG Atlas on every push to the
  default branch, statistics dashboard rebuilt with the SDK's maintenance profile: [PR #138][pr138],
  [commit 34ead58][c34ead58], [stellar/xdrgen PR #231][xdrgen231], [SBOM runs][sbomruns],
  [dashboard][statsdash]

Five releases shipped this quarter. Protocol 27 was tracked through its mainnet activation, and
support for Protocol 28 followed in 1.13.0 on 2026-08-24, 23 days before the network switched on
2026-09-16. Compatibility matrices were regenerated for every release: Horizon and RPC report 100%
through v28.0.1, and every SEP matrix reports 100%.

#### 2. Native ScVal Conversion

Description from last quarter:

> Add a helper that converts a smart-contract value (XdrSCVal) to a native PHP value, so contract
> invocation and simulation results can be consumed directly instead of parsing the raw XDR union by
> hand. This matches the JS and Python SDKs.

Delivered in 1.14.0 (2026-09-15).

Proof of completion:

- GitHub release: [1.14.0][rel1140]
- PR with implementation and tests (1.14.0): [PR #124][pr124]
- Documentation: [PR #125][pr125], [guide section][guidesection]

`XdrSCVal::toNative()` turns contract values into plain PHP values with one call and never throws.
Values without a PHP counterpart come back unchanged. The helper is documented in the Soroban guide
and the agent skill reference.

#### 3. Contract Bindings Update

Description from last quarter:

> Update the PHP contract-bindings implementation that Soneso contributed to the community
> stellar-contract-bindings generator (linked from the Stellar CLI) so its generated PHP code is
> compatible with the current SDK.

Delivered in stellar-contract-bindings 0.6.0b0 (2026-09-02). The generator PR merged on 2026-07-21.

Proof of completion:

- Pull request to stellar-contract-bindings, PHP output updated for the current SDK: [PR #22][scb22],
  [PHP commit][scb22php]
- Follow-up, spec-text escaping for multi-line contract docs: [PR #36][scb36]
- Follow-up, CAP-85 external-reference resolution in the generator: [PR #37][scb37]
- Generator release: [0.6.0b][scbrel]
- Generated PHP clients tested against testnet in the SDK repository, regenerated with the released
  generator (1.14.0): [generated clients][generatedclients], [PR #127][pr127]
- The Stellar CLI command `stellar contract bindings php` points to this generator: [php.rs][clibind]

Six generated clients run as testnet integration tests in the SDK repository, two of them added this
quarter. The generator's PHP output requires SDK 1.11.0 or later and covers contracts that share code
through external references.

#### 4. SEP-35 (Operation IDs)

Description from last quarter:

> Implement SEP-35: a TOID utility that packs and unpacks a ledger sequence, transaction order, and
> operation index into the total-order ID used for operation IDs and Horizon paging cursors, with
> unit tests and documentation.

Delivered in 1.13.0 (2026-08-24).

Proof of completion:

- GitHub release: [1.13.0][rel1130]
- PR with implementation and tests (1.13.0): [PR #113][pr113]
- SEP-35 compatibility matrix, 7 of 7 fields: [SEP-35 matrix][sep35matrix]
- Documentation: [SEP-35 guide][sep35doc]

The `TOID` class packs and unpacks operation IDs and computes the ID bounds of a ledger range for
paging. The guide and the agent skill reference document it.

### 2026 Q2

#### 1. Continuous Maintenance and Improvement

Description from last quarter:

> Regular SDK updates addressing Horizon, Soroban RPC, and protocol updates (including Protocol 26
> when released), bug fixes, feature requests, and documentation updates. Maintain existing SEP
> implementations and update as needed. Keep compatibility matrices, CI pipelines, statistics
> dashboard, and SBOM workflow up to date. Improve unit test coverage toward 90%.

Proof of completion:

- Release 1.9.6: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.9.6
- Release 1.9.7: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.9.7
- Release 1.9.8: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.9.8
- Release 1.10.0: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.10.0
- Protocol 26 tracked: Horizon/RPC matrices updated to v26.0.0 (release 1.9.7)
- Protocol 27 / CAP-0071 support (v1.10.0): [PR #94][pr94]
- CI and security hardening ([PR #92][pr92]):
  - PHPStan
  - composer audit gate
- Native ext-sodium migration: [PR #77][pr77]
- SEP hardening ([PR #92][pr92]):
  - SEP-7
  - SEP-10
  - federation/SEP-31/stellar.toml error paths
- SEP-45 injectable RPC server: release 1.9.8
- Correctness fixes ([PR #92][pr92]):
  - full unsigned 64-bit Memo ids
  - corrected Asset pool-share type constant
  - CAP-40 signed-payload hint for short payloads
  - 32-byte KeyPair key validation
- Soroban contract client ([PR #92][pr92]):
  - injectable SorobanServer on ClientOptions/InstallRequest/DeployRequest
  - immediate transaction-status polling with exponential backoff
- Coverage improved from 85.9% to 92.74% (main), exceeding the toward-90% goal, under blocking
  Codecov thresholds (project 80%, patch 70%); the unit suite now runs fully offline (SorobanClient
  unit-tested with mocked RPC, live SEP-10 moved to integration). Config: [codecov.yml][codecov]
- Stats dashboard: https://soneso.github.io/soneso-sdk-stats/
- [Horizon compatibility matrix](https://github.com/Soneso/stellar-php-sdk/blob/main/compatibility/horizon/COMPATIBILITY_MATRIX.md)
- [RPC compatibility matrix](https://github.com/Soneso/stellar-php-sdk/blob/main/compatibility/rpc/RPC_COMPATIBILITY_MATRIX.md)
- [SEP compatibility matrices](https://github.com/Soneso/stellar-php-sdk/tree/main/compatibility/sep)
- AI-agent skill bundle updated alongside each release

Four releases shipped this quarter. Protocol 26 was tracked and Protocol 27 (CAP-0071) delegated
Soroban authorization was delivered beyond the committed scope. Line coverage rose from 85.9% to
92.74% under blocking Codecov gates. A security pass added PHPStan static analysis, a composer audit
gate, and native ext-sodium, and error-path hardening landed across SEP-7, SEP-10, SEP-31, SEP-45,
and federation/stellar.toml loading. Compatibility matrices, the SBOM workflow, and the stats
dashboard were kept current.

#### 2. SEP-11 TxRep Rewrite

Description from last quarter:

> Replace the monolithic hand-written TxRep implementation with generated toTxRep()/fromTxRep()
> methods on XDR types, reducing TxRep.php to a thin facade. This mirrors the approach already
> completed in the Flutter SDK.

Proof of completion:

- Release 1.9.6: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.9.6
- PR 78: https://github.com/Soneso/stellar-php-sdk/pull/78
- [SEP-11 compatibility matrix](https://github.com/Soneso/stellar-php-sdk/blob/main/compatibility/sep/SEP-0011_COMPATIBILITY_MATRIX.md)

TxRep.php was reduced from 3,515 lines to a 505-line facade ("Thin facade over the generated XDR
toTxRep/fromTxRep methods"), with serialization generated onto 144 XDR classes.

#### 3. SEP-51 (XDR-JSON) Support

Description from last quarter:

> Implement SEP-51 bi-directional conversion between XDR and JSON for all XDR types. Extend the
> existing XDR code generator to produce toJson()/fromJson() methods. Handle Stellar-specific types
> (StrKey encoding for AccountID, ContractID, AssetCode, etc.) per the specification.

Proof of completion:

- Release 1.9.7 (JSON encoding on XDR types): [PR #85][pr85]
- Release 1.9.8 (generator round-trip + negative tests): [PR #90][pr90]
- Generator: https://github.com/Soneso/stellar-php-sdk/tree/main/tools/xdr-generator
- Fixtures: https://github.com/Soneso/stellar-php-sdk/tree/main/tools/sep-51-test-fixtures
- Documentation: https://github.com/Soneso/stellar-php-sdk/blob/main/docs/sep/sep-51.md
- [SEP-51 compatibility matrix](https://github.com/Soneso/stellar-php-sdk/blob/main/compatibility/sep/SEP-0051_COMPATIBILITY_MATRIX.md)
- Tests: Soneso/StellarSDKTests/Unit/Xdr/Sep51/ (15 files: corpus round-trips, canonical spec
  examples, hand-written-vs-generated equivalence, negative inputs, union-arm rejection, and more)

SEP-51 bi-directional XDR/JSON conversion is implemented via the extended code generator, with
Stellar-specific StrKey handling in XdrAccountIDBase.php and XdrAccountID.php. Verification spans
corpus round-trips, canonical spec examples, hand-written-vs-generated equivalence, negative inputs,
and union-arm rejection.

## Proposed Impact

Keep the SDK compatible with Horizon, Soroban RPC, and protocol updates including Protocol 27.
Maintain existing SEP implementations and update as needed. Fix bugs and respond to issues and
feature requests.

Improve the Soroban developer experience by adding a helper that converts a returned smart-contract
value (XdrSCVal) to a native PHP value, so contract invocation and simulation results can be consumed
directly instead of parsing the raw XDR union by hand. The JS and Python SDKs already provide this.

Update the PHP contract-bindings implementation that Soneso contributed to the community
stellar-contract-bindings generator (linked from the Stellar CLI) so it produces code compatible with
the current SDK.

Implement SEP-35 (Operation IDs), the standard for the total-order ID of a ledger, transaction, or
operation, so backend integrators can compute and parse operation IDs and Horizon paging cursors
offline. The Python and Java SDKs already implement this.

## Proposed Deliverables

### Continuous Maintenance and Improvement

Regular SDK updates addressing Horizon, Soroban RPC, and protocol updates (tracking Protocol 27
through its mainnet activation), bug fixes, feature requests, and documentation updates. Maintain
existing SEP implementations and update as needed, keep the SEP compatibility matrices current. Hold
line coverage at 90% or above (currently 92.74%) under the blocking Codecov thresholds. Keep
compatibility matrices, CI pipelines, statistics dashboard, and SBOM workflow up to date.

Proof: Release notes on GitHub, updated compatibility matrices, Codecov coverage report, and the
soneso-sdk-stats dashboard.

### Native ScVal Conversion

Add a helper that converts a smart-contract value (XdrSCVal) to a native PHP value, so contract
invocation and simulation results can be consumed directly instead of parsing the raw XDR union by
hand. This matches the JS and Python SDKs.

Proof: GitHub release, PR with implementation and tests, documentation.

### Contract Bindings Update

Update the PHP contract-bindings implementation that Soneso contributed to the community
stellar-contract-bindings generator (linked from the Stellar CLI) so its generated PHP code is
compatible with the current SDK.

Proof: pull request to the stellar-contract-bindings repository.

### SEP-35 (Operation IDs)

Implement SEP-35: a TOID utility that packs and unpacks a ledger sequence, transaction order, and
operation index into the total-order ID used for operation IDs and Horizon paging cursors, with unit
tests and documentation.

Proof: GitHub release, PR with implementation and tests, SEP-35 compatibility matrix, documentation.

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_php_sdk&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_php_sdk)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_php_sdk&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_php_sdk)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_php_sdk&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_php_sdk)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_php_sdk&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_php_sdk)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

[agentskill]: https://github.com/Soneso/stellar-php-sdk/blob/1.15.0/skills/stellar-php-sdk/SKILL.md
[c0db4af8]: https://github.com/Soneso/stellar-php-sdk/commit/0db4af8
[c34ead58]: https://github.com/Soneso/stellar-php-sdk/commit/34ead58
[cb9abda5]: https://github.com/Soneso/stellar-php-sdk/commit/b9abda5
[ceebca70]: https://github.com/Soneso/stellar-php-sdk/commit/eebca70
[clibind]:
  https://github.com/stellar/stellar-cli/blob/main/cmd/soroban-cli/src/commands/contract/bindings/php.rs
[codecov]: https://github.com/Soneso/stellar-php-sdk/blob/main/codecov.yml
[codecovapp]: https://app.codecov.io/gh/Soneso/stellar-php-sdk
[codecovyml]: https://github.com/Soneso/stellar-php-sdk/blob/1.15.0/codecov.yml
[generatedclients]:
  https://github.com/Soneso/stellar-php-sdk/tree/1.15.0/Soneso/StellarSDKTests/bindings
[guidesection]:
  https://github.com/Soneso/stellar-php-sdk/blob/1.14.0/docs/soroban.md#converting-to-native-php-values
[is112]: https://github.com/Soneso/stellar-php-sdk/issues/112
[is120]: https://github.com/Soneso/stellar-php-sdk/issues/120
[ngybnc]: https://github.com/ngybnc
[pr100]: https://github.com/Soneso/stellar-php-sdk/pull/100
[pr106]: https://github.com/Soneso/stellar-php-sdk/pull/106
[pr111]: https://github.com/Soneso/stellar-php-sdk/pull/111
[pr113]: https://github.com/Soneso/stellar-php-sdk/pull/113
[pr114]: https://github.com/Soneso/stellar-php-sdk/pull/114
[pr117]: https://github.com/Soneso/stellar-php-sdk/pull/117
[pr118]: https://github.com/Soneso/stellar-php-sdk/pull/118
[pr119]: https://github.com/Soneso/stellar-php-sdk/pull/119
[pr121]: https://github.com/Soneso/stellar-php-sdk/pull/121
[pr122]: https://github.com/Soneso/stellar-php-sdk/pull/122
[pr124]: https://github.com/Soneso/stellar-php-sdk/pull/124
[pr125]: https://github.com/Soneso/stellar-php-sdk/pull/125
[pr127]: https://github.com/Soneso/stellar-php-sdk/pull/127
[pr129]: https://github.com/Soneso/stellar-php-sdk/pull/129
[pr130]: https://github.com/Soneso/stellar-php-sdk/pull/130
[pr132]: https://github.com/Soneso/stellar-php-sdk/pull/132
[pr133]: https://github.com/Soneso/stellar-php-sdk/pull/133
[pr134]: https://github.com/Soneso/stellar-php-sdk/pull/134
[pr135]: https://github.com/Soneso/stellar-php-sdk/pull/135
[pr136]: https://github.com/Soneso/stellar-php-sdk/pull/136
[pr137]: https://github.com/Soneso/stellar-php-sdk/pull/137
[pr138]: https://github.com/Soneso/stellar-php-sdk/pull/138
[pr77]: https://github.com/Soneso/stellar-php-sdk/pull/77
[pr85]: https://github.com/Soneso/stellar-php-sdk/pull/85
[pr90]: https://github.com/Soneso/stellar-php-sdk/pull/90
[pr92]: https://github.com/Soneso/stellar-php-sdk/pull/92
[pr94]: https://github.com/Soneso/stellar-php-sdk/pull/94
[pr99]: https://github.com/Soneso/stellar-php-sdk/pull/99
[protoledger]: https://github.com/Soneso/soneso-sdk-stats/blob/main/curated/protocol-delivery.json
[q3horizon]:
  https://github.com/Soneso/stellar-php-sdk/blob/1.15.0/compatibility/horizon/COMPATIBILITY_MATRIX.md
[q3rpc]:
  https://github.com/Soneso/stellar-php-sdk/blob/1.15.0/compatibility/rpc/RPC_COMPATIBILITY_MATRIX.md
[q3sep]: https://github.com/Soneso/stellar-php-sdk/tree/1.15.0/compatibility/sep
[rel1110]: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.11.0
[rel1120]: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.12.0
[rel1130]: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.13.0
[rel1140]: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.14.0
[rel1150]: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.15.0
[sbomruns]: https://github.com/Soneso/stellar-php-sdk/actions/workflows/sbom.yml
[scb22]: https://github.com/lightsail-network/stellar-contract-bindings/pull/22
[scb22php]: https://github.com/lightsail-network/stellar-contract-bindings/commit/cd4f4fed8
[scb36]: https://github.com/lightsail-network/stellar-contract-bindings/pull/36
[scb37]: https://github.com/lightsail-network/stellar-contract-bindings/pull/37
[scbrel]: https://github.com/lightsail-network/stellar-contract-bindings/releases/tag/0.6.0b
[sep35doc]: https://github.com/Soneso/stellar-php-sdk/blob/1.13.0/docs/sep/sep-35.md
[sep35matrix]:
  https://github.com/Soneso/stellar-php-sdk/blob/1.13.0/compatibility/sep/SEP-0035_COMPATIBILITY_MATRIX.md
[sepguides]: https://github.com/Soneso/stellar-php-sdk/blob/main/docs/sep/README.md
[sorobanguide]:
  https://github.com/Soneso/stellar-php-sdk/blob/1.15.0/docs/soroban.md#external-reference-executables-cap-85
[statsdash]: https://soneso.github.io/soneso-sdk-stats/
[xdrgen231]: https://github.com/stellar/xdrgen/pull/231
