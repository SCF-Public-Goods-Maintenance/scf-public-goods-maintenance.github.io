---
title: "kmp-stellar-sdk"
canonical_id: daoip-5:scf:project:kmp_stellar_sdk
parent: Public Good Projects
proposal_issue: 120
proposer: christian-rogobete
category: "SDKs"
budget: "15000"
---

# kmp-stellar-sdk

<!-- markdownlint-disable MD036 -->

_Write your Stellar integration once in Kotlin and run it across Mobile, Web, Desktop, and Server:
transactions, Stellar RPC and Horizon, smart contracts, OpenZeppelin smart accounts, and 20 SEPs._

<!-- markdownlint-enable MD036 -->

|                      |                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| **Category**         | SDKs                                                                                               |
| **Website**          | <https://developers.stellar.org/docs/tools/sdks/client-sdks#kotlin-multiplatform-sdk>              |
| **Repository**       | <https://github.com/Soneso/kmp-stellar-sdk>                                                        |
| **First Released**   | October 2025                                                                                       |
| **Intake**           | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/86> |
| **Budget Requested** | 15000                                                                                              |

## Project Description

<!-- markdownlint-disable MD034 -->

The Kotlin Multiplatform Stellar SDK lets developers write their Stellar integration once in Kotlin
and run it across Mobile (Android and iOS), Web (browser), Desktop (JVM, native macOS), and Server
(JVM, Node.js). It covers XDR encoding and decoding, transaction building and signing, Stellar RPC
and Horizon, low-level and high-level Soroban smart-contract support (deploy, simulate, invoke,
auth-entry signing), OpenZeppelin smart account support (WebAuthn passkeys, multi-signer
authorization, context rules, and policy-based access control), and 20 Stellar Ecosystem Proposals
(SEPs). It ships two cross-platform demo apps (general-purpose and smart-account) and an AI
coding-agent skill. It is open-source (Apache-2.0), published on Maven Central, listed on the
official Stellar developer documentation, built on audited cryptography (BouncyCastle, libsodium),
and tested on CI with 95% unit test coverage tracked on Codecov, with zero open issues.

<!-- markdownlint-enable MD034 -->

## Team & Experience

<!-- markdownlint-disable MD034 -->

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

<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->

In Q3 2026 the SDK shipped six releases, v1.9.0 through v1.14.0. Maven Central artifacts recorded
about 32,000 downloads from roughly 2,100 unique sources over the quarter (Scarf), nearly double the
quarter before, which had about 17,000 downloads from 1,100 sources. At the close of the quarter: 15
stars, 5 forks, 29 releases, 0 open issues, and 0 open pull requests. Unit test coverage is tracked
on Codecov and enforced in CI with a 90% minimum, currently at 95.12%, up from 81% at the proposal.

SEP-51 (XDR-JSON) shipped in v1.11.0. Apps can now convert any Stellar XDR data, the binary format of
transactions and ledger data, to readable JSON and back. The JSON follows the standard form defined
by SEP-51, which the Python and PHP SDKs use as well. Developers can inspect and edit transactions
and contract data as text, which makes debugging easier and lets them exchange data with other tools.

Native ScVal Conversion shipped in v1.13.0. When an app calls a smart contract, the answer comes back
in Stellar's binary format, which the app had to take apart by hand. The new helper turns such a
value into a plain Kotlin value with one call, without the contract's interface description, so apps
can use contract results directly. Bence ([ngybnc][ngybnc]), a Soneso team member on the KMP SDK
since February 2026, authored this deliverable.

Contract Bindings (KMP Target) added Kotlin as a new target of the community code generator, next to
the Dart, Swift, and PHP targets that Soneso contributed, and the Stellar CLI now points developers
to it for Kotlin as well. Developers can generate ready-to-use Kotlin code for talking to any smart
contract with one command, and the generated code runs on the current SDK, including contracts that
use external-reference executables (Protocol 28).

The SDK supported the quarter's network upgrades ahead of time. Protocol 27, the upgrade the proposal
named, was tracked through its mainnet activation on 2026-07-08, and the SDK now uses the new
authorization format it introduced (CAP-71) by default. Support for Protocol 28 followed in v1.12.0
on 2026-08-26, 21 days before the network switched on 2026-09-16. That gave app developers time to
prepare for contracts that share code through external references (CAP-85), which the SDK can load
and deploy.

Maintenance made the SDK safer for users. Addresses and incoming binary data are checked more
strictly on every platform, so a mistyped address or a malformed data packet is caught early. Sign-in
with anchors (SEP-10) and anchor callbacks (SEP-12) are verified more strictly as well.

Smart accounts became easier to build into wallets. A wallet can now install policies, such as a
spending limit, at the moment it creates an account, an addition the proposal did not name. Input
that the smart-account contract would reject, such as an overlong rule name or too many policies on
one rule, is caught before the transaction is sent, so the wallet learns about it without paying a
fee. And every error the OpenZeppelin smart-account contracts can return is translated into a named
error the wallet can explain to its user. In web apps, a lost network connection now arrives as a
specific error the app can handle.

Documentation kept pace: the [SEP guides][sepguides] index now covers all 20 implemented SEPs, a new
guide explains Stellar address types, and a migration guide walks developers through the upgrade to
v1.12.0. The compatibility matrices show full coverage of Horizon and Soroban RPC through v28.0.1,
and every SEP matrix is at 100%. CI stays current through Dependabot, security updates of the build
tooling, and a check that flags upstream XDR changes. SBOM submission to PG Atlas runs on every push
to the default branch. The SDK joined the [soneso-sdk-stats][statsdash] dashboard this quarter, which
tracks maintenance and usage of all four Soneso SDKs.

<!-- markdownlint-enable MD034 -->

## Past Deliverables

### 2026 Q3

#### 1. Continuous Maintenance and Improvement (2026 Q3)

Description from last quarter:

> Regular SDK updates addressing Horizon, Soroban RPC, and protocol updates (tracking Protocol 27
> through its mainnet activation), bug fixes, feature requests, and documentation updates. Maintain
> existing SEP implementations and update as needed, keep the compatibility matrices current. Improve
> unit test coverage toward 85% (currently 81%). Keep CI pipelines and the SBOM workflow up to date,
> and add the KMP SDK to the soneso-sdk-stats dashboard so its statistics are tracked alongside the
> other Soneso SDKs (see: [soneso-sdk-stats dashboard](https://soneso.github.io/soneso-sdk-stats/)).

Proof of completion:

- Release notes: [v1.9.0][rel190], [v1.10.0][rel1100], [v1.11.0][rel1110], [v1.12.0][rel1120],
  [v1.13.0][rel1130], [v1.14.0][rel1140]
- Protocol 27 tracked through its mainnet activation: CAP-71 `useUpgradedAuth` simulation flag and
  RPC v27.1 fields (v1.9.0), ADDRESS_V2 credentials as the default (v1.12.0): [PR #45][pr45],
  [commit 41d0466cc][c41d0466], [PR #62][pr62]
- Support for Protocol 28 ahead of its mainnet activation: CAP-85 external-reference executables in
  XDR (v1.11.0), external-reference resolution, deployment from an external reference, and contract
  id derivation (v1.12.0): [PR #50][pr50], [PR #59][pr59], [PR #60][pr60], [PR #61][pr61],
  [protocol delivery ledger][protoledger]
- Horizon and XDR updates: claimable balance ids in every spelling and nullable balance-change
  accounts (v1.12.0), one client identification on every request path (v1.14.0), XDR definitions at
  the current upstream stellar-xdr (v1.13.0): [PR #58][pr58], [PR #74][pr74], [PR #70][pr70]
- Soroban and network handling: transaction polling reports the last failure and network errors in
  web apps arrive as typed exceptions (v1.10.0), Horizon event streams reconnect reliably, RPC
  decoding errors carry a clear message, and contract deployment reports a refused transaction
  immediately (v1.11.0): [PR #47][pr47], [PR #54][pr54], [commit d1a7d2310][cd1a7d23]
- Stricter input validation: strkeys on all platforms, hex parsing, and amount strings (v1.12.0), XDR
  array counts checked before allocation and WebAuthn length checks (v1.14.0): [PR #58][pr58],
  [commit 713bb5144][c713bb51], [PR #73][pr73], [PR #74][pr74]
- Unit test coverage raised from 81% to 95.12%, past the 85% the proposal targeted, with a
  restructured test suite and a 90% minimum enforced in CI and as a required check (v1.11.0):
  [PR #54][pr54], [Codecov][codecovapp], [codecov.yml][codecovyml]
- SEP-6, SEP-10, and SEP-29 updates: transaction patching per the spec, challenge source account
  verified and token requests never auto-retried, memo-required check fires on submission (v1.11.0):
  [PR #54][pr54], [commit d1a7d2310][cd1a7d23]
- SEP-8, SEP-12, SEP-23, and SEP-45 updates: strict strkey decoding on all platforms, callbacks and
  issuers verified more strictly (v1.12.0), authorization entries checked for array counts (v1.14.0):
  [PR #58][pr58], [PR #73][pr73]
- Smart-account hardening: contract limits, indexer defaults, and error catalog (v1.10.0), relayer
  response parsing and signer input checks (v1.11.0), ADDRESS_V2 defaults with a relayer opt-out and
  demo apps updated for Protocol 28 (v1.12.0): [PR #47][pr47], [PR #54][pr54], [PR #62][pr62],
  [commit 1f15e94b9][c1f15e94]
- Documentation: accuracy pass with every code sample compiled (v1.12.0), migration guide for
  v1.12.0, guide to Stellar address types (v1.13.0), agent skill updated every release:
  [commit f8fbdc67e][cf8fbdc6], [1.12.0 guide][mig1120], [PR #71][pr71], [agent skill][agentskill]
- Compatibility matrices regenerated every release, Horizon and RPC at 100% through v28.0.1 and every
  SEP matrix at 100% (v1.14.0): [Horizon][q3horizon], [RPC][q3rpc], [SEP][q3sep]
- CI and SBOM: Dependabot updates with pinned actions, XDR generator on a patched xdrgen fork with
  the fix proposed upstream (v1.10.0), API reference published from the main branch (v1.14.0), SBOM
  submitted to PG Atlas on every push to the default branch: [PR #64][pr64],
  [commit ef89d7d2f][cef89d7d], [commit 53b7fa495][c53b7fa4], [stellar/xdrgen PR #231][xdrgen231],
  [PR #72][pr72], [SBOM runs][sbomruns]
- KMP SDK added to the soneso-sdk-stats dashboard, with Maven Central download collection and the
  SDK's maintenance profile: [dashboard commit d842da410][statscd842da4], [dashboard][statsdash],
  [KMP profile][profile]

Six releases shipped this quarter. Protocol 27 was tracked through its mainnet activation, and
support for Protocol 28 followed in v1.12.0 on 2026-08-26, 21 days before the network switched on
2026-09-16. Compatibility matrices were regenerated for every release: Horizon and RPC report 100%
through v28.0.1, and every SEP matrix reports 100%.

#### 2. SEP-51 (XDR-JSON)

Description from last quarter:

> Implement bi-directional XDR/JSON conversion via the XDR generator, with round-trip unit tests and
> documentation, for cross-SDK parity with the Python and PHP SDKs.

Delivered in v1.11.0 (2026-08-10).

Proof of completion:

- GitHub release: [v1.11.0][rel1110]
- PR with implementation and round-trip tests (v1.11.0): [PR #57][pr57]
- SEP-51 compatibility matrix, 37 of 37 fields: [SEP-51 matrix][sep51matrix]
- Documentation: [SEP-51 guide][sep51doc]
- Weekly check of the round-trip corpus against the reference implementation:
  [corpus drift workflow][corpusdriftworkflow]

Every generated XDR type converts to and from the SEP-51 JSON form with `toXdrJson()` and
`fromXdrJson()`. Round-trip tests run in CI against a corpus from the reference implementation, and a
test executes every example in the guide.

#### 3. Native ScVal Conversion

Description from last quarter:

> Add a helper that converts a smart-contract value (SCValXdr) to a native Kotlin value without
> requiring the contract spec, so contract invocation and simulation results can be consumed directly
> instead of parsing the raw XDR union by hand. This matches the JS and Python SDKs.

Delivered in v1.13.0 (2026-09-15).

Proof of completion:

- GitHub release: [v1.13.0][rel1130]
- PR with implementation and tests (v1.13.0): [PR #67][pr67]
- Documentation: [PR #68][pr68], [guide section][guidesection]

`SCValXdr.toNative()` turns contract values into plain Kotlin values with one call, without the
contract's interface description, and never throws. Values without a Kotlin counterpart come back
unchanged. The helper is documented in the usage guide and the agent skill reference.

#### 4. Contract Bindings (KMP Target)

Description from last quarter:

> Add a Kotlin Multiplatform target to the community stellar-contract-bindings generator (implemented
> by overcat and linked from the Stellar CLI), generating typed Kotlin contract clients backed by the
> SDK's ContractClient and joining the Dart, Swift, and PHP targets that Soneso contributed. Includes
> the SDK addition the generated clients need (a public raw-SCVal invoke path on ContractClient).
> Once the generator target is merged, add a `stellar contract bindings kmp` subcommand to the
> Stellar CLI, as with the existing subcommands for the other languages.

Delivered in v1.9.0 (2026-07-14) for the SDK addition, stellar-contract-bindings 0.6.0b0 (2026-09-02)
for the generator target, and stellar-cli v28.1.0 (2026-09-26) for the CLI subcommand.

Proof of completion:

- Pull request to stellar-contract-bindings, new Kotlin Multiplatform target: [PR #22][scb22],
  [KMP commit][scb22kmp]
- Follow-up, spec-text escaping for multi-line contract docs: [PR #36][scb36]
- Follow-up, CAP-85 external-reference resolution in the generator: [PR #37][scb37]
- Generator release: [0.6.0b][scbrel]
- Pull request to stellar-cli, the `stellar contract bindings kmp` subcommand that points developers
  to the generator, released in v28.1.0: [PR #2721][cli2721], [v28.1.0][clirel2810]
- SDK release with the client addition, a raw-value invoke path on ContractClient (v1.9.0):
  [v1.9.0][rel190], [PR #44][pr44]
- Generated Kotlin clients tested in unit and testnet integration tests, regenerated with the
  released generator (v1.13.0): [generated clients][generatedclients], [PR #65][pr65]
- Documentation of generated bindings (v1.13.0): [PR #66][pr66]

Six generated clients run as testnet integration tests in the SDK repository. Generated Kotlin code
calls contracts through the SDK's ContractClient and covers contracts that share code through
external references.

#### Beyond the committed scope (2026 Q3)

The following work was not named in the Q3 proposal.

- Constructor-time smart-account policies (v1.10.0): [PR #47][pr47]

<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

Keep the SDK compatible with Horizon, Soroban RPC, and protocol updates including Protocol 27.
Maintain existing SEP implementations and update as needed. Fix bugs and respond to issues and
feature requests.

Implement SEP-51 (XDR-JSON), a standard mapping between Stellar's XDR structures and JSON. This
enables developers to inspect and manipulate XDR data in a human-readable format, improving debugging
and tooling integration. The Python SDK and the PHP SDK already implement this SEP.

Improve the Soroban developer experience by adding a helper that converts a returned smart-contract
value (SCValXdr) to a native Kotlin value without requiring the contract spec, so contract invocation
and simulation results can be consumed directly instead of parsing the raw XDR union by hand. The JS
and Python SDKs already provide this.

Add a Kotlin Multiplatform target to the community stellar-contract-bindings generator (implemented
by overcat and linked from the Stellar CLI), so developers can generate typed Kotlin contract clients
from a deployed contract's spec, joining the Dart, Swift, and PHP targets that Soneso contributed
(see: [stellar-contract-bindings generator][scbindings]).

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

### Continuous Maintenance and Improvement

Regular SDK updates addressing Horizon, Soroban RPC, and protocol updates (tracking Protocol 27
through its mainnet activation), bug fixes, feature requests, and documentation updates. Maintain
existing SEP implementations and update as needed, keep the compatibility matrices current. Improve
unit test coverage toward 85% (currently 81%). Keep CI pipelines and the SBOM workflow up to date,
and add the KMP SDK to the soneso-sdk-stats dashboard so its statistics are tracked alongside the
other Soneso SDKs (see: [soneso-sdk-stats dashboard](https://soneso.github.io/soneso-sdk-stats/)).

Proof: Release notes on GitHub, updated compatibility matrices, Codecov coverage report, and the
soneso-sdk-stats dashboard.

### SEP-51 (XDR-JSON)

Implement bi-directional XDR/JSON conversion via the XDR generator, with round-trip unit tests and
documentation, for cross-SDK parity with the Python and PHP SDKs.

Proof: GitHub release, PR with implementation and tests, SEP-51 compatibility matrix, documentation.

### Native ScVal Conversion

Add a helper that converts a smart-contract value (SCValXdr) to a native Kotlin value without
requiring the contract spec, so contract invocation and simulation results can be consumed directly
instead of parsing the raw XDR union by hand. This matches the JS and Python SDKs.

Proof: GitHub release, PR with implementation and tests, documentation.

### Contract Bindings (KMP Target)

Add a Kotlin Multiplatform target to the community stellar-contract-bindings generator (implemented
by overcat and linked from the Stellar CLI), generating typed Kotlin contract clients backed by the
SDK's ContractClient and joining the Dart, Swift, and PHP targets that Soneso contributed. Includes
the SDK addition the generated clients need (a public raw-SCVal invoke path on ContractClient). Once
the generator target is merged, add a `stellar contract bindings kmp` subcommand to the Stellar CLI,
as with the existing subcommands for the other languages.

Proof: pull requests to the stellar-contract-bindings and stellar-cli repositories, SDK release with
the client addition, generated-code tests.

<!-- markdownlint-enable MD034 -->

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Akmp_stellar_sdk&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Akmp_stellar_sdk)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Akmp_stellar_sdk&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Akmp_stellar_sdk)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Akmp_stellar_sdk&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Akmp_stellar_sdk)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Akmp_stellar_sdk&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Akmp_stellar_sdk)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

[agentskill]: https://github.com/Soneso/kmp-stellar-sdk/tree/v1.14.0/skills
[c1f15e94]: https://github.com/Soneso/kmp-stellar-sdk/commit/1f15e94b9
[c41d0466]: https://github.com/Soneso/kmp-stellar-sdk/commit/41d0466cc
[c53b7fa4]: https://github.com/Soneso/kmp-stellar-sdk/commit/53b7fa495
[c713bb51]: https://github.com/Soneso/kmp-stellar-sdk/commit/713bb5144
[cd1a7d23]: https://github.com/Soneso/kmp-stellar-sdk/commit/d1a7d2310
[cef89d7d]: https://github.com/Soneso/kmp-stellar-sdk/commit/ef89d7d2f
[cf8fbdc6]: https://github.com/Soneso/kmp-stellar-sdk/commit/f8fbdc67e
[cli2721]: https://github.com/stellar/stellar-cli/pull/2721
[clirel2810]: https://github.com/stellar/stellar-cli/releases/tag/v28.1.0
[codecovapp]: https://app.codecov.io/gh/Soneso/kmp-stellar-sdk
[codecovyml]: https://github.com/Soneso/kmp-stellar-sdk/blob/v1.14.0/codecov.yml
[corpusdriftworkflow]:
  https://github.com/Soneso/kmp-stellar-sdk/blob/v1.14.0/.github/workflows/sep-51-corpus-drift.yml
[generatedclients]:
  https://github.com/Soneso/kmp-stellar-sdk/tree/v1.14.0/stellar-sdk/src/commonTest/kotlin/com/soneso/stellar/sdk/contract/bindings
[guidesection]:
  https://github.com/Soneso/kmp-stellar-sdk/blob/v1.13.0/docs/sdk-usage-examples.md#spec-less-conversion-with-tonative
[mig1120]: https://github.com/Soneso/kmp-stellar-sdk/blob/v1.12.0/docs/migration/1.12.0.md
[ngybnc]: https://github.com/ngybnc
[pr44]: https://github.com/Soneso/kmp-stellar-sdk/pull/44
[pr45]: https://github.com/Soneso/kmp-stellar-sdk/pull/45
[pr47]: https://github.com/Soneso/kmp-stellar-sdk/pull/47
[pr50]: https://github.com/Soneso/kmp-stellar-sdk/pull/50
[pr54]: https://github.com/Soneso/kmp-stellar-sdk/pull/54
[pr57]: https://github.com/Soneso/kmp-stellar-sdk/pull/57
[pr58]: https://github.com/Soneso/kmp-stellar-sdk/pull/58
[pr59]: https://github.com/Soneso/kmp-stellar-sdk/pull/59
[pr60]: https://github.com/Soneso/kmp-stellar-sdk/pull/60
[pr61]: https://github.com/Soneso/kmp-stellar-sdk/pull/61
[pr62]: https://github.com/Soneso/kmp-stellar-sdk/pull/62
[pr64]: https://github.com/Soneso/kmp-stellar-sdk/pull/64
[pr65]: https://github.com/Soneso/kmp-stellar-sdk/pull/65
[pr66]: https://github.com/Soneso/kmp-stellar-sdk/pull/66
[pr67]: https://github.com/Soneso/kmp-stellar-sdk/pull/67
[pr68]: https://github.com/Soneso/kmp-stellar-sdk/pull/68
[pr70]: https://github.com/Soneso/kmp-stellar-sdk/pull/70
[pr71]: https://github.com/Soneso/kmp-stellar-sdk/pull/71
[pr72]: https://github.com/Soneso/kmp-stellar-sdk/pull/72
[pr73]: https://github.com/Soneso/kmp-stellar-sdk/pull/73
[pr74]: https://github.com/Soneso/kmp-stellar-sdk/pull/74
[profile]: https://soneso.github.io/soneso-sdk-stats/profiles/kmp-stellar-sdk.json
[protoledger]: https://github.com/Soneso/soneso-sdk-stats/blob/main/curated/protocol-delivery.json
[q3horizon]:
  https://github.com/Soneso/kmp-stellar-sdk/blob/v1.14.0/compatibility/horizon/HORIZON_COMPATIBILITY_MATRIX.md
[q3rpc]:
  https://github.com/Soneso/kmp-stellar-sdk/blob/v1.14.0/compatibility/rpc/RPC_COMPATIBILITY_MATRIX.md
[q3sep]: https://github.com/Soneso/kmp-stellar-sdk/tree/v1.14.0/compatibility/sep
[rel1100]: https://github.com/Soneso/kmp-stellar-sdk/releases/tag/v1.10.0
[rel1110]: https://github.com/Soneso/kmp-stellar-sdk/releases/tag/v1.11.0
[rel1120]: https://github.com/Soneso/kmp-stellar-sdk/releases/tag/v1.12.0
[rel1130]: https://github.com/Soneso/kmp-stellar-sdk/releases/tag/v1.13.0
[rel1140]: https://github.com/Soneso/kmp-stellar-sdk/releases/tag/v1.14.0
[rel190]: https://github.com/Soneso/kmp-stellar-sdk/releases/tag/v1.9.0
[sbomruns]: https://github.com/Soneso/kmp-stellar-sdk/actions/workflows/sbom.yml
[scb22]: https://github.com/lightsail-network/stellar-contract-bindings/pull/22
[scb22kmp]: https://github.com/lightsail-network/stellar-contract-bindings/commit/49885f1ad
[scb36]: https://github.com/lightsail-network/stellar-contract-bindings/pull/36
[scb37]: https://github.com/lightsail-network/stellar-contract-bindings/pull/37
[scbindings]: https://github.com/lightsail-network/stellar-contract-bindings
[scbrel]: https://github.com/lightsail-network/stellar-contract-bindings/releases/tag/0.6.0b
[sep51doc]: https://github.com/Soneso/kmp-stellar-sdk/blob/v1.11.0/docs/sep/sep-51.md
[sep51matrix]:
  https://github.com/Soneso/kmp-stellar-sdk/blob/v1.14.0/compatibility/sep/SEP-0051_COMPATIBILITY_MATRIX.md
[sepguides]: https://github.com/Soneso/kmp-stellar-sdk/blob/main/docs/sep/README.md
[statscd842da4]: https://github.com/Soneso/soneso-sdk-stats/commit/d842da410
[statsdash]: https://soneso.github.io/soneso-sdk-stats/
[xdrgen231]: https://github.com/stellar/xdrgen/pull/231
