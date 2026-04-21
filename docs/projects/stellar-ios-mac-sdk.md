---
title: "stellar-ios-mac-sdk"
parent: Public Good Projects
proposal_issue: 41
proposer: christian-rogobete
category: "SDKs"
budget: "18000"
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
| **Budget Requested** | 18000                                           |

## Project Description

The iOS Stellar SDK is a native Swift library for building Stellar applications on iOS and macOS. It
provides transaction building, account management, Horizon API access, Soroban RPC support,
high-level Soroban smart contract support, and implements 18 Stellar Ecosystem Proposals (SEPs). The
SDK is listed on the official Stellar developer documentation and is used by wallets and applications
including LOBSTR, Unstoppable Wallet, and others.

## Team & Experience

My name is Christian (GitHub: christian-rogobete, Discord: soneso, LinkedIn:
https://www.linkedin.com/in/rogobete/) and I am the main developer and maintainer of the iOS Stellar
SDK. I have a master's degree in computer science and a master's degree in logistics and have been
working in the IT field since the mid-1990s as a developer, software architect, project manager, and
in other roles.

I began contributing to the Stellar network in 2017, specializing primarily in the development and
maintenance of Stellar SDKs. The first Stellar SDK I developed was the iOS Stellar SDK, which won the
Stellar Build Challenge in 2018 and has since been expanded and maintained by me with the help of the
SDF Infrastructure Grant and the SCF Public Goods Award. Other SDKs I have developed include the
Flutter Stellar SDK, the PHP Stellar SDK, and the Kotlin Multiplatform Stellar SDK.

I currently work full-time on my Stellar SDK projects.

Previous SCF participation: Multiple SCF Build Awards (Flutter Wallet SDK, Swift Wallet SDK, KMP
Stellar SDK, and others), SCF Public Goods Award since Q3 2025 (Batch 1) for iOS, Flutter, and PHP
SDKs. Member of the SCF Public Goods Maintenance working group.

## Retroactive Impact

In Q1 2026, the iOS SDK shipped 5 releases (3.4.2 through 3.4.6). The SDK is used by wallets and
applications including LOBSTR, Unstoppable Wallet, and others. Stats (as of April 10, 2026): 129
stars, 56 forks, 140 releases, 0 open issues at end of quarter. Median time to close: 21.1h, 100%
response rate.

Unit test coverage was extended and tracking was set up, currently at 88.78%, with a new CI pipeline
and Codecov integration (80% project, 70% patch thresholds). Security hardening was applied across
all SDK modules. Bugs found during testing and maintenance were fixed. All public types now conform
to Swift 6 Sendable for thread safety. Protocol 25 support was added.

SEP-53 message signing was implemented, cross-SDK compatible with the Java, Python, Flutter, and PHP
SDKs. A new XDR code generator replaces hand-written types with machine-generated code from Stellar's
canonical .x files, adding new types and round-trip tests. A daily upstream XDR change detection
workflow auto-creates issues when the spec changes.

An AI coding agent skill was published for AI-assisted development tools. The SDK documentation was
fully rewritten with tested code examples.

SBOM submission to PG Atlas was added and runs on every push. A new daily statistics collection has
been implemented and runs via https://github.com/Soneso/soneso-sdk-stats (live dashboard:
https://soneso.github.io/soneso-sdk-stats/).

## Past Deliverables

### 1. Continuous Maintenance and Improvement

Description from last quarter: Regular SDK updates addressing horizon, rpc, protocol updates (e.g.
p25), bug fixes, feature requests, code modernization, unit test coverage improvement, and
documentation enhancements to ensure long-term sustainability. This includes a new documentation for
AI Coding Agents, a so called "skill", providing token efficient documentation and best practices
when using the SDK. Furthermore it includes setting up a configuration for unit test coverage
tracking and adding to CI/CD pipeline.

Proof of completion:

- Release 3.4.2: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.4.2
- Release 3.4.3: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.4.3
- Release 3.4.4: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.4.4
- Release 3.4.5: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.4.5
- Release 3.4.6: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.4.6

Protocol support: Added Protocol 25 RPC response fields (v3.4.2). Updated XDR definitions to latest
upstream (v3.4.5, v3.4.6).

Test coverage and CI/CD: Unit test coverage was extended and tracking was set up, currently at
88.78%. Added GitHub Actions CI with Codecov integration.

- PR #183: https://github.com/Soneso/stellar-ios-mac-sdk/pull/183

Security hardening: Replaced force-cast crash paths with proper error handling, validated memo text
by UTF-8 byte count, rejected negative/overflowing amounts in toXDRAmount, percent-encoded all
user-supplied URL values, guarded XDR array decoding against memory exhaustion, enforced HTTPS on
SEP-7 callbacks. Pinned all CI actions to commit SHAs with least-privilege permissions. Dependabot
configured for monthly updates.

- PR #196: https://github.com/Soneso/stellar-ios-mac-sdk/pull/196

Bug fixes: Bugs found during the test coverage extension and security hardening have been fixed.

Thread safety improvements: All public types now conform to Swift 6 Sendable.

- PR #189: https://github.com/Soneso/stellar-ios-mac-sdk/pull/189

Documentation: Full documentation rewrite with tested code examples that are validated by the test
suite.

- PR #192: https://github.com/Soneso/stellar-ios-mac-sdk/pull/192

AI Coding Agent documentation: Agent Skill following the agentskills.io open standard, compatible
with Claude Code, Codex CLI, Cursor, Gemini CLI, and others. Also available via the Claude Code
marketplace.

- PR #190: https://github.com/Soneso/stellar-ios-mac-sdk/pull/190

Compatibility matrices: Updated for Horizon, RPC, and all SEPs with automated generators
(tools/matrix-generator/).

- Horizon:
  https://github.com/Soneso/stellar-ios-mac-sdk/blob/master/compatibility/horizon/HORIZON_COMPATIBILITY_MATRIX.md
- RPC:
  https://github.com/Soneso/stellar-ios-mac-sdk/blob/master/compatibility/rpc/RPC_COMPATIBILITY_MATRIX.md
- SEPs: https://github.com/Soneso/stellar-ios-mac-sdk/tree/master/compatibility/sep

SBOM submission: Added PG Atlas SBOM workflow that triggers on every push to master.

- https://github.com/Soneso/stellar-ios-mac-sdk/blob/master/.github/workflows/sbom.yml

Statistics and monitoring: A new repository https://github.com/Soneso/soneso-sdk-stats was created to
collect daily statistics for the iOS SDK. Data collected: GitHub clones (daily counts and unique
cloners), meta data (stars, forks, watchers), activity (52-week commit history and full release
list), and issue/PR response times with closure stats. Metrics (as of April 10, 2026): 129 stars, 56
forks, 140 releases, 0 open issues, median time to close 21.1h, 100% response rate. Live dashboard:
https://soneso.github.io/soneso-sdk-stats/

### 2. SEP-53 Support

Description from last quarter: SEP-53 standardizes message signing functionality across Stellar
wallets, libraries, and services, preventing ecosystem fragmentation and ensuring interoperability.
SEP-53 support is also implemented in the Java and Python SDKs.

Proof of completion:

- Release 3.4.3: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.4.3
- PR #187: https://github.com/Soneso/stellar-ios-mac-sdk/pull/187
- SEP-53 compatibility matrix:
  https://github.com/Soneso/stellar-ios-mac-sdk/blob/master/compatibility/sep/SEP-0053_COMPATIBILITY_MATRIX.md
- Documentation: https://github.com/Soneso/stellar-ios-mac-sdk/blob/master/docs/sep/sep-53.md

Adds signMessage() and verifyMessage() on KeyPair with String and [UInt8] overloads. Unit tests cover
all spec test vectors (ASCII, Japanese, binary), encoding round-trips, failure cases, and edge cases.
Cross-SDK compatible with the Java, Python, Flutter, and PHP SDKs.

### 3. XDR Classes Generator

Description from last quarter: Currently the SDK has hundreds of manually written XDR
classes/structs/enums used to encode and decode XDR objects. Extensions or updates in the XDR
structure need to be implemented manually at this time, which makes the SDK difficult to maintain.
The new XDR class generator will improve the maintainability and also add missing XDR classes so that
they can immediately be used as new features require them.

Proof of completion:

- Release 3.4.5: https://github.com/Soneso/stellar-ios-mac-sdk/releases/tag/3.4.5
- PR #191: https://github.com/Soneso/stellar-ios-mac-sdk/pull/191
- Generator: https://github.com/Soneso/stellar-ios-mac-sdk/tree/master/tools/xdr-generator
- XDR definitions: https://github.com/Soneso/stellar-ios-mac-sdk/tree/master/xdr
- CI workflow:
  https://github.com/Soneso/stellar-ios-mac-sdk/blob/master/.github/workflows/xdr-generator.yml

Ruby-based code generator reads Stellar's canonical .x XDR definition files (from
https://github.com/stellar/stellar-xdr). Replaces hand-written XDR type definitions with
auto-generated Swift code and adds new types not previously in the SDK. Round-trip encode/decode unit
tests cover 95% of generated types. CI snapshot tests verify generated code stays in sync with XDR
definitions. High-level SDK APIs unchanged. The ledger close metadata XDR mentioned in the
deliverable description can now be decoded. Daily upstream XDR change detection workflow auto-creates
GitHub issues when the spec changes.

## Proposed Impact

Keep the SDK compatible with Horizon, Soroban RPC, and protocol updates including Protocol 26 when it
ships. Maintain existing SEP implementations and update as needed. Fix bugs and respond to issues and
feature requests.

Add support for OpenZeppelin Smart Accounts (C-address wallets) on Soroban, enabling passkey-based
wallet authentication, multi-signer authorization, and policy-based access control. This follows the
SCF RFP for C-Address Tooling and matches the implementation already shipped in the KMP Stellar SDK
(v1.4.0). A TypeScript reference exists in kalepail/smart-account-kit.

Smart account support on iOS and macOS will allow native app developers to build Stellar wallets with
OpenZeppelin smart accounts using passkeys and biometric authentication.

Rewrite the SEP-11 TxRep implementation to delegate to code-generated methods, replacing the
monolithic hand-written serialization. This improves maintainability and reduces the risk of encoding
errors when the XDR spec changes. The same rewrite was already completed in the Flutter SDK (Q1 2026)
and is planned for the PHP SDK (Q2 2026).

## Proposed Deliverables

### 1. Continuous Maintenance and Improvement

Regular SDK updates addressing Horizon, Soroban RPC, and protocol updates (including Protocol 26),
bug fixes, feature requests, and documentation updates. Maintain existing SEP implementations and
update as needed. Keep compatibility matrices, CI pipelines, statistics dashboard, and SBOM workflow
up to date.

Proof: Release notes on GitHub, updated compatibility matrices, soneso-sdk-stats dashboard.

### 2. SEP-11 TxRep Rewrite

Replace the monolithic hand-written TxRep implementation with generated toTxRep()/fromTxRep() methods
on XDR types, reducing TxRep.swift to a thin facade. This mirrors the approach already completed in
the Flutter and PHP SDKs.

Proof: Release on GitHub, PR with implementation, updated test suite.

### 3. OpenZeppelin Smart Account Support

Implement support for the OpenZeppelin smart account contracts on Soroban, covering:

- Wallet lifecycle: create, deploy, and connect smart account wallets with WebAuthn passkey
  registration
- Context rules and policies: create, edit, and remove authorization rules with configurable signers
  and policies
- Token operations and contract calls with automatic auth entry signing
- Multi-signer authorization: passkey signers, delegated Stellar account signers, and Ed25519 key
  signers
- Fee sponsoring via relayer proxy for gasless transactions
- Credential discovery via indexer integration
- Platform-native WebAuthn via ASAuthorization for iOS and macOS with secure storage adapters
- Demo application for iOS and macOS
- Documentation: API reference and onboarding guide

Proof: Release on GitHub, PR with implementation, demo app, documentation, test suite.

## Budget justification

The budget increase from $15,000 to $18,000 reflects the addition of OpenZeppelin Smart Account
support, which is a major new feature involving platform-native WebAuthn integration, a demo
application, documentation, and manual testing across platforms (passkeys require physical device
testing).

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
