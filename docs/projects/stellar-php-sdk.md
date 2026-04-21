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

My name is Christian (GitHub: christian-rogobete, Discord: soneso, LinkedIn:
https://www.linkedin.com/in/rogobete/) and I am the main developer and maintainer of the Stellar PHP
SDK. I have a master's degree in computer science and a master's degree in logistics and have been
working in the IT field since the mid-1990s as a developer, software architect, project manager, and
in other roles.

I began contributing to the Stellar network in 2017, specializing primarily in the development and
maintenance of Stellar SDKs. I developed the iOS Stellar SDK (which won the Stellar Build Challenge
in 2018), the Flutter Stellar SDK, the PHP Stellar SDK, and the Kotlin Multiplatform Stellar SDK.

I currently work full-time on my Stellar SDK projects.

Previous SCF participation: Multiple SCF Build Awards (Flutter Wallet SDK, Swift Wallet SDK, KMP
Stellar SDK, and others), SCF Public Goods Award since Q3 2025 (Batch 1) for iOS, Flutter, and PHP
SDKs. Member of the SCF Public Goods Maintenance working group.

## Retroactive Impact

In Q1 2026, the PHP SDK shipped 5 releases (1.9.1 through 1.9.5). The SDK is used by projects
including StellarChain.io, cNGN Stablecoin, PHP Anchor SDK, and others. Stats (as of April 10, 2026):
41 stars, 20 forks, 80 releases, Packagist 48,733 total downloads (1,495/month), 32 dependent GitHub
repos, 0 open issues at end of quarter. Median time to close: 10.6h, 100% response rate.

Unit test coverage was extended and tracking was set up, currently at 85.9%, with a new CI pipeline
and Codecov integration (80% project, 70% patch thresholds). Security hardening was applied across
all SDK modules. Bugs found during testing and maintenance were fixed. Protocol 25 support was added.

SEP-53 message signing was implemented, cross-SDK compatible with the Java, Python, iOS, and Flutter
SDKs. A new XDR code generator replaces hand-written types with machine-generated code from Stellar's
canonical .x files, adding new types and round-trip tests. The generator also discovered and fixed
pre-existing encoding bugs in the hand-written code. A daily upstream XDR change detection workflow
auto-creates issues when the spec changes.

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

- Release 1.9.1: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.9.1
- Release 1.9.2: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.9.2
- Release 1.9.3: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.9.3
- Release 1.9.4: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.9.4
- Release 1.9.5: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.9.5

Protocol support: Added Protocol 25 RPC response fields (v1.9.1). Updated XDR definitions to latest
upstream (v1.9.5).

Test coverage and CI/CD: Unit test coverage was extended and tracking was set up, currently at 85.9%.
Added GitHub Actions CI with Codecov integration.

- PR #60: https://github.com/Soneso/stellar-php-sdk/pull/60
- PR #61: https://github.com/Soneso/stellar-php-sdk/pull/61

Security hardening: Security audit across all source files covering cryptographic hardening, HTTPS
enforcement, input validation, and PSR-3 logging.

- PR #71: https://github.com/Soneso/stellar-php-sdk/pull/71

Bug fixes: Bugs found during the test coverage extension and security hardening have been fixed.

Documentation: Full documentation rewrite with tested code examples that are validated by the test
suite. Old URLs preserved as redirect stubs for backward compatibility.

- PR #64: https://github.com/Soneso/stellar-php-sdk/pull/64

AI Coding Agent documentation: Agent Skill following the agentskills.io open standard, compatible
with Claude Code, Codex CLI, Cursor, Gemini CLI, and others. Also available via the Claude Code
marketplace.

- PR #70: https://github.com/Soneso/stellar-php-sdk/pull/70

Platform compatibility: Made ext-pcntl optional for Windows.

- PR #68: https://github.com/Soneso/stellar-php-sdk/pull/68

CI/CD hardening: Pinned all GitHub Actions to commit SHAs. Added daily upstream XDR change detection
workflow. Added Dependabot config for monthly updates. Added least-privilege permissions to tests
workflow.

Compatibility matrices: Updated for Horizon, RPC, and all SEPs with automated generators
(tools/matrix-generator/).

- Horizon:
  https://github.com/Soneso/stellar-php-sdk/blob/main/compatibility/horizon/COMPATIBILITY_MATRIX.md
- RPC:
  https://github.com/Soneso/stellar-php-sdk/blob/main/compatibility/rpc/RPC_COMPATIBILITY_MATRIX.md
- SEPs: https://github.com/Soneso/stellar-php-sdk/tree/main/compatibility/sep

SBOM submission: Added PG Atlas SBOM workflow that triggers on every push to main.

- https://github.com/Soneso/stellar-php-sdk/blob/main/.github/workflows/sbom.yml

Statistics and monitoring: A new repository https://github.com/Soneso/soneso-sdk-stats was created to
collect daily statistics for the PHP SDK. Data collected: GitHub clones (daily counts and unique
cloners), meta data (stars, forks, watchers), activity (52-week commit history and full release
list), issue/PR response times with closure stats, Packagist downloads (total, monthly, daily), and
GitHub dependents (repos and packages). Metrics (as of April 10, 2026): 41 stars, 20 forks, 80
releases, 0 open issues, median first response 5.9h, median time to close 10.6h, 100% response rate,
Packagist 48,733 total downloads (1,495/month), 32 dependent repos. Live dashboard:
https://soneso.github.io/soneso-sdk-stats/

### 2. SEP-53 Support

Description from last quarter: SEP-53 standardizes message signing functionality across Stellar
wallets, libraries, and services, preventing ecosystem fragmentation and ensuring interoperability.
SEP-53 support is also implemented in the Java and Python SDKs.

Proof of completion:

- Release 1.9.2: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.9.2
- PR #63: https://github.com/Soneso/stellar-php-sdk/pull/63
- SEP-53 compatibility matrix:
  https://github.com/Soneso/stellar-php-sdk/blob/main/compatibility/sep/SEP-0053_COMPATIBILITY_MATRIX.md
- Documentation: https://github.com/Soneso/stellar-php-sdk/blob/main/docs/sep/sep-53.md

Adds signMessage() and verifyMessage() on KeyPair. Unit tests cover all spec test vectors (ASCII,
Japanese, binary), encoding round-trips, failure cases, and edge cases. Cross-SDK compatible with the
Java, Python, iOS, and Flutter SDKs.

### 3. XDR Classes Generator

Description from last quarter: Currently the SDK has hundreds of manually written XDR classes used to
encode and decode XDR objects. Extensions or updates in the XDR structure need to be implemented
manually at this time, which makes the SDK difficult to maintain. The new XDR class generator will
improve the maintainability and also add missing XDR classes so that they can immediately be used as
new features require them.

Proof of completion:

- Release 1.9.5: https://github.com/Soneso/stellar-php-sdk/releases/tag/1.9.5
- PR #72: https://github.com/Soneso/stellar-php-sdk/pull/72
- Generator: https://github.com/Soneso/stellar-php-sdk/tree/main/tools/xdr-generator
- XDR definitions: https://github.com/Soneso/stellar-php-sdk/tree/main/xdr
- CI workflow:
  https://github.com/Soneso/stellar-php-sdk/blob/main/.github/workflows/xdr-generator.yml

Ruby-based code generator reads Stellar's canonical .x XDR definition files (from
https://github.com/stellar/stellar-xdr). Replaces hand-written XDR type definitions with
auto-generated PHP code and adds new types not previously in the SDK. Round-trip encode/decode unit
tests cover all generated types. CI snapshot tests verify generated code stays in sync with XDR
definitions. High-level SDK APIs unchanged. The generator discovered and fixed pre-existing encoding
bugs in hand-written XDR code. Daily upstream XDR change detection workflow auto-creates GitHub
issues when the spec changes.

## Proposed Impact

Keep the SDK compatible with Horizon, Soroban RPC, and protocol updates including Protocol 26.
Maintain existing SEP implementations and update as needed. Fix bugs and respond to issues and
feature requests.

Implement SEP-51 (XDR-JSON), a standard mapping between Stellar's XDR structures and JSON. This
enables developers to inspect and manipulate XDR data in a human-readable format, improving debugging
and tooling integration. The Python SDK already implements this SEP.

Rewrite the SEP-11 TxRep implementation to delegate to code-generated methods, replacing the
monolithic hand-written serialization. This improves maintainability and reduces the risk of encoding
errors when the XDR spec changes.

## Proposed Deliverables

### 1. Continuous Maintenance and Improvement

Regular SDK updates addressing Horizon, Soroban RPC, and protocol updates (including Protocol 26 when
released), bug fixes, feature requests, and documentation updates. Maintain existing SEP
implementations and update as needed. Keep compatibility matrices, CI pipelines, statistics
dashboard, and SBOM workflow up to date. Improve unit test coverage toward 90%.

Proof: Release notes on GitHub, updated compatibility matrices, soneso-sdk-stats dashboard, Codecov
coverage.

### 2. SEP-11 TxRep Rewrite

Replace the monolithic hand-written TxRep implementation with generated toTxRep()/fromTxRep() methods
on XDR types, reducing TxRep.php to a thin facade. This mirrors the approach already completed in the
Flutter SDK.

Proof: Release on GitHub, PR with implementation, updated test suite.

### 3. SEP-51 (XDR-JSON) Support

Implement SEP-51 bi-directional conversion between XDR and JSON for all XDR types. Extend the
existing XDR code generator to produce toJson()/fromJson() methods. Handle Stellar-specific types
(StrKey encoding for AccountID, ContractID, AssetCode, etc.) per the specification.

Proof: Release on GitHub, PR with implementation, documentation, round-trip test suite.

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
