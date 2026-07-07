---
title: "kmp-stellar-sdk"
parent: Public Good Projects
proposal_issue: 120
proposer: christian-rogobete
category: "SDKs"
budget: "15000"
---

# kmp-stellar-sdk

<!-- markdownlint-disable MD036 -->

_Write your Stellar integration once in Kotlin and run it across Mobile, Web, Desktop, and Server:
transactions, Stellar RPC and Horizon, smart contracts, OpenZeppelin smart accounts, and 17 SEPs._
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
and run it across Mobile (Android, iOS), Web (browser), Desktop (JVM, native macOS), and Server (JVM,
Node.js). It covers XDR encoding and decoding, transaction building and signing, Stellar RPC and
Horizon, low-level and high-level Soroban smart-contract support (deploy, simulate, invoke,
auth-entry signing), OpenZeppelin smart account support (WebAuthn passkeys, multi-signer
authorization, context rules, and policy-based access control), and 17 Stellar Ecosystem Proposals
(SEPs). It ships two cross-platform demo apps (general-purpose and smart-account) and an AI
coding-agent skill. It is open-source (Apache-2.0), published on Maven Central, listed on the
official Stellar developer documentation, built on audited cryptography (BouncyCastle, libsodium),
and tested on CI with 81% unit test coverage tracked on Codecov, with zero open issues.
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

In Q2 2026 the KMP Stellar SDK shipped multiple releases — v1.3.1 through v1.8.1. At the close of the
quarter: 0 open issues, a 100% issue response rate, with a median time-to-close of 16.6 hours. The
Maven Central artifacts recorded about 17,000 downloads from roughly 1,100 unique sources over the
last three months (Scarf). Unit test coverage is tracked on Codecov, currently at 81%.

The headline delivery is OpenZeppelin smart account support, shipped in v1.4.0: WebAuthn passkey
authentication on all platforms, multi-signer authorization, context rules and policies,
relayer-sponsored fees, and indexer-based credential discovery, together with a Compose Multiplatform
smart account demo app (Android, iOS, macOS, web). The feature grew across the quarter: cross-device
passkey authentication via WebAuthn hybrid transport (v1.5.0), a hardened wallet-connect cascade
(v1.5.1), Ed25519 external signers (v1.6.1), and token-decimals support with stricter amount
validation (v1.7.1). The smart-account feature was funded by an SCF Build Award (RFP Track); all
other work this quarter, and the SDK's ongoing maintenance, was self-funded.

SEP-31 (Cross-Border Payments, sending side, requested by a community member on Discord) landed in
v1.6.0 together with a shared callback-signature verifier for SEP-12 and SEP-31, bringing the SDK to
17 implemented SEPs. Protocol 27 (CAP-71) Soroban authorization shipped in v1.8.0, with the
compatibility matrices regenerated against Horizon and Soroban RPC v27.0.0.

Release v1.8.1 added a headless connectToContract path with RPC-visibility polling and an
agent-signer flow in the smart account demo: a standalone Kotlin reference agent, a Ktor coordination
server, and an approval inbox — the flow where a user delegates scoped authority to an agent,
over-scope calls are rejected on-chain and surfaced for approval, and the approved call is
re-submitted via the relayer.

The XDR code generator gained upstream source pinning, snapshot tests, and daily upstream-drift
monitoring, and a generator bug collapsing multi-case discriminants was fixed. CI runs on every push
with Codecov coverage tracking and monthly Dependabot updates, the AI-agent skill is updated
alongside each release, and SBOM submission to PG Atlas runs on every push to main.
<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

N/A
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
from a deployed contract's spec, joining the Dart, Swift, and PHP targets that Soneso contributed.
See:
[stellar-contract-bindings generator](https://github.com/lightsail-network/stellar-contract-bindings)
<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

**Continuous Maintenance and Improvement**

Regular SDK updates addressing Horizon, Soroban RPC, and protocol updates (tracking Protocol 27
through its mainnet activation), bug fixes, feature requests, and documentation updates. Maintain
existing SEP implementations and update as needed, keep the compatibility matrices current. Improve
unit test coverage toward 85% (currently 81%). Keep CI pipelines and the SBOM workflow up to date,
and add the KMP SDK to the soneso-sdk-stats dashboard so its statistics are tracked alongside the
other Soneso SDKs (see: [soneso-sdk-stats dashboard](https://soneso.github.io/soneso-sdk-stats/)).

Proof: Release notes on GitHub, updated compatibility matrices, Codecov coverage report, and the
soneso-sdk-stats dashboard.

**SEP-51 (XDR-JSON)**

Implement bi-directional XDR/JSON conversion via the XDR generator, with round-trip unit tests and
documentation, for cross-SDK parity with the Python and PHP SDKs.

Proof: GitHub release, PR with implementation and tests, SEP-51 compatibility matrix, documentation.

**Native ScVal Conversion**

Add a helper that converts a smart-contract value (SCValXdr) to a native Kotlin value without
requiring the contract spec, so contract invocation and simulation results can be consumed directly
instead of parsing the raw XDR union by hand. This matches the JS and Python SDKs.

Proof: GitHub release, PR with implementation and tests, documentation.

**Contract Bindings (KMP Target)**

Add a Kotlin Multiplatform target to the community stellar-contract-bindings generator (implemented
by overcat and linked from the Stellar CLI), generating typed Kotlin contract clients backed by the
SDK's ContractClient and joining the Dart, Swift, and PHP targets that Soneso contributed. Includes
the SDK addition the generated clients need (a public raw-SCVal invoke path on ContractClient). Once
the generator target is merged, add a `stellar contract bindings kmp` subcommand to the Stellar CLI,
as with the existing subcommands for the other languages.

Proof: pull requests to the stellar-contract-bindings and stellar-cli repositories, SDK release with
the client addition, generated-code tests.
<!-- markdownlint-enable MD034 -->

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
