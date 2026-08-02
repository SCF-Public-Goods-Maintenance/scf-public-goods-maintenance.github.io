---
title: "stellar-php-sdk"
parent: Public Good Projects
proposal_issue: 45
proposer: christian-rogobete
category: "SDKs"
budget: "15000"
---

# stellar-php-sdk

_The Stellar SDK for PHP, providing transaction building, Horizon and Soroban RPC access, high-level
Soroban smart contract support, and implements 19 Stellar Ecosystem Proposals (SEPs)._

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
support, high-level Soroban smart contract support, and implements 19 Stellar Ecosystem Proposals
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

In Q2 2026 the PHP SDK shipped four releases — 1.9.6, 1.9.7, 1.9.8, and 1.10.0. The SDK is used by
projects including StellarChain.io, the cNGN Stablecoin, and the PHP Anchor SDK. At the close of the
quarter: 41 stars, 20 forks, 84 total releases, 0 open issues, Packagist downloads of approximately
54,300 total and 2,211/month (up from 1,495/month at Q1 close), 32 dependent repositories and 2
dependent packages, a median first-response time of 3.5 hours, a median time-to-close of 20.8 hours,
and a 100% response rate.

Protocol 26 was tracked by updating the Horizon and RPC compatibility matrices to v26.0.0. Unit test
coverage moved from 85.9% to 92.74%, exceeding the committed "toward 90%" goal. CI was hardened with
PHPStan static analysis and a composer audit dependency gate, GitHub Actions stay pinned to commit
SHAs with least-privilege permissions, and the third-party crypto shim was removed in favor of native
ext-sodium.

The SDK delivered SEP-51 (XDR-JSON) bi-directional conversion, and added Protocol 27 (CAP-0071)
support. That work also fixed prior silent data loss in credential round-tripping, fixed an
auth-callback signature-expiration bug, bounded decode recursion against a maliciously nested
delegate tree, and shipped an end-to-end delegated-auth test.

The SEP-11 TxRep rewrite was shipped in 1.9.6 and reduced TxRep.php from 3,515 lines to a 505-line
facade, with serialization generated onto 144 XDR classes.

Targeted SEP hardening landed across the quarter: SEP-7 URI signature verification, SEP-10 challenge
validation plus error-path tests, federation, SEP-31, and stellar.toml error-path tests, and an
injectable Soroban RPC server for SEP-45 contract-account web auth. Documentation for SEP-51 and
Protocol 27 was added, and the per-SEP compatibility matrices were regenerated with current
timestamps and target versions.

The SBOM workflow to PG Atlas continues to run on every push to main, and the
[soneso-sdk-stats][statsdash] dashboard continues daily collection of Packagist downloads,
dependents, clones, stars, and responsiveness metrics for the SDK.

## Past Deliverables

### 1. Continuous Maintenance and Improvement

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

### 2. SEP-11 TxRep Rewrite

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

### 3. SEP-51 (XDR-JSON) Support

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

[codecov]: https://github.com/Soneso/stellar-php-sdk/blob/main/codecov.yml
[pr77]: https://github.com/Soneso/stellar-php-sdk/pull/77
[pr85]: https://github.com/Soneso/stellar-php-sdk/pull/85
[pr90]: https://github.com/Soneso/stellar-php-sdk/pull/90
[pr92]: https://github.com/Soneso/stellar-php-sdk/pull/92
[pr94]: https://github.com/Soneso/stellar-php-sdk/pull/94
[statsdash]: https://soneso.github.io/soneso-sdk-stats/
