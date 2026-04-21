---
title: "Stellar Hardware Wallet Support"
parent: Public Good Projects
proposal_issue: 51
proposer: overcat
category: "Wallet Support"
budget: "12000"
---

# Stellar Hardware Wallet Support

_Hardware wallet integration for Stellar, enabling secure transaction signing on Ledger and Trezor
devices._

|                      |                                                                    |
| -------------------- | ------------------------------------------------------------------ |
| **Category**         | Wallet Support                                                     |
| **Website**          | <https://gist.github.com/overcat/ca6e3da0d3602a928c2eef6e054f853a> |
| **Repository**       | <https://gist.github.com/overcat/ca6e3da0d3602a928c2eef6e054f853a> |
| **First Released**   | July 2021                                                          |
| **Intake**           | soft-launch                                                        |
| **Budget Requested** | 12000                                                              |

## Project Description

This project maintains and advances Stellar support across the two most widely used hardware wallet
ecosystems: Ledger and Trezor. The project covers upstream work on the Stellar Ledger app, Ledger
Live integration points and related libraries, as well as Stellar support in Trezor firmware and
Trezor Suite. This includes protocol upgrades, asset support, transaction-signing improvements, bug
fixes, and compatibility work needed to keep Stellar usable on secure hardware devices as the network
evolves.

Hardware wallet support requires continuous upstream maintenance to remain useful as Stellar evolves.
Protocol upgrades, new assets, SDK changes, and new signing flows can otherwise leave users and
integrators behind. This project keeps that support current across Ledger and Trezor, reducing
breakage risk and helping ensure Stellar remains accessible to security-conscious users and
organizations.

## Team & Experience

overcat (GitHub: [overcat](https://github.com/overcat), Discord: @overcat.me) has been active in the
Stellar community since 2018 and has rich experience in Stellar-related development, maintaining a
series of Stellar infrastructure software. Currently maintained Stellar-related projects are listed
at https://lightsail.network. For hardware wallet support specifically, overcat has maintained the
Stellar Ledger app across all device generations since Protocol 13, collaborating closely with the
Ledger team on the app, Ledger Live, and related libraries, and handling community-reported issues
and bug fixes throughout. On the Trezor side, overcat introduced Stellar support to Trezor Suite and
has maintained ongoing bug fixes and updates in collaboration with the Trezor team over the years.

## Retroactive Impact

In Q1 2026, all planned deliverables were completed and additional work was delivered beyond the
original scope. The Stellar Ledger App binary size was reduced by approximately 15% through
optimization work now staged on the next-release branch, pending bundling with a future update to
avoid a standalone security audit cycle. Full Stellar token support was shipped in Trezor Suite
Mobile v26.2.2, completing mobile feature parity for Trezor users. Working with the Trezor team, a
Figma design for Soroban transaction support on Trezor was completed, laying the groundwork for
future smart contract signing. Two minor Ledger app releases (v6.0.2, v6.0.3) kept the app current
with the latest SDK versions and added community-requested token support.

## Past Deliverables

### 1. Ledger App Optimization and Size Reduction

Description from last quarter:

> Over the next quarter, I will optimize the Stellar Ledger App with a focus on reducing its binary
> size (currently ~150 KB). This will improve performance, reliability, and leave more room for
> future protocol upgrades, ensuring the long-term sustainability of Stellar's hardware wallet
> support.

Proof of completion:

- next-release branch: https://github.com/lightsail-network/app-stellar/tree/next-release

The Stellar Ledger App binary size was reduced by approximately 15% through targeted optimization
passes developed in coordination with the Ledger team. The changes are staged on the next-release
branch and will be bundled with the next production update, combined with a security audit to avoid
the cost of a standalone audit cycle.

### 2. Full Stellar Token Support in Trezor Suite Mobile

Description from last quarter:

> I will extend full Stellar token support to Trezor Suite Mobile, enabling mobile users to securely
> send, receive, and manage non-XLM assets. This significantly improves everyday usability for
> mobile-first users and expands Stellar's reach across platforms.

Proof of completion:

- Trezor Suite Mobile v26.2.2: https://github.com/trezor/trezor-suite/releases/tag/v26.2.2%40mobile —
  full Stellar token support shipped on mobile

Full Stellar token support was shipped in Trezor Suite Mobile v26.2.2 in collaboration with the
Trezor team, enabling mobile users to securely send, receive, and manage non-XLM Stellar assets
directly from their Trezor devices. This completes feature parity between Trezor Suite Desktop and
Mobile for Stellar users.

### 3. Soroban Support Design for Trezor

Description from last quarter:

> This work was not explicitly planned but was completed as additional contribution during the
> quarter.

Proof of completion:

- Internal Trezor Figma (not publicly available) — Soroban smart contract interaction design for
  Trezor wallet

Collaborated with the Trezor team to complete a Figma design for Soroban smart contract support in
Trezor wallet. This design work lays the foundation for future Soroban transaction signing on Trezor
devices and represents the first step toward hardware-secured Soroban interactions.

### 4. Ongoing Ledger App Maintenance

Description from last quarter:

> Ongoing maintenance ensures the Ledger app remains compatible with the latest SDK versions and
> continues to support community-requested Stellar assets.

Proof of completion:

- PR #101: https://github.com/LedgerHQ/app-stellar/pull/101 — Add support for SolvBTC and xSolvBTC
  tokens
- PR #110: https://github.com/LedgerHQ/app-stellar/pull/110 — Refactor deprecated SDK debug macros

Two minor releases shipped in coordination with the Ledger team. v6.0.2 added support for the SolvBTC
and xSolvBTC tokens following a community request. v6.0.3 modernized the codebase by replacing
deprecated Ledger SDK debug macros, ensuring forward compatibility with upcoming SDK versions.

## Proposed Impact

The primary goals for Q2 2026 are: ongoing maintenance of the Ledger and Trezor integrations; add
WalletConnect support for Stellar in Trezor Suite; and implement Soroban transaction signing support
for Trezor in collaboration with the Trezor team. The Soroban PR may not be merged within the quarter
due to current firmware team priorities, but the implementation will be submitted and metrics
observed to inform next steps.

## Proposed Deliverables

### 1. Ongoing Maintenance

Regular upkeep of the Stellar Ledger app and Trezor integrations in coordination with the Ledger and
Trezor teams: responding to community issues and pull requests, keeping SDK and firmware dependencies
current, and ensuring Stellar assets and protocol features remain fully supported.

Proof: Release tags on GitHub, updated changelogs, etc.

### 2. Stellar WalletConnect Support in Trezor Suite

Add WalletConnect support for Stellar in Trezor Suite, enabling users to connect their Trezor
hardware wallets to Stellar dApps directly from the suite. This brings hardware-level signing
security to WalletConnect-based Stellar applications and improves interoperability across the
ecosystem.

Proof: Release changelog.

### 3. Soroban Support for Trezor

Implement Soroban transaction signing support for Trezor in collaboration with the Trezor team. This
work follows prior design and discussion with the Trezor team. Due to current firmware team
priorities, PR merge is not guaranteed within the quarter, but the implementation will be submitted
and metrics (review feedback, CI results, community interest) will be tracked to guide future work.

Proof: PR(s) submitted to trezor-firmware.

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
