---
title: "Stellar Hardware Wallet Support"
parent: Public Good Projects
proposal_issue: 51
proposer: overcat
category: "Wallet Support"
budget: "15000"
---

# Stellar Hardware Wallet Support

_Hardware wallet integration for Stellar, enabling secure transaction signing on Ledger and Trezor
devices._

|                        |                                                  |
| ---------------------- | ------------------------------------------------ |
| **Category**           | Wallet Support                                   |
| **Website**            | <https://lightsail.network>                      |
| **Ledger Stellar App** | <https://github.com/LedgerHQ/app-stellar>        |
| **Ledger Live**        | <https://github.com/ledgerhq/ledger-live>        |
| **Trezor Firmware**    | <https://github.com/trezor/trezor-firmware>      |
| **Trezor Suite**       | <https://github.com/trezor/trezor-suite>         |
| **strledger**          | <https://github.com/lightsail-network/strledger> |
| **First Released**     | July 2021                                        |
| **Intake**             | soft-launch                                      |
| **Budget Requested**   | 15000                                            |

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

In Q2 2026, the planned Stellar WalletConnect deliverable shipped to users in Trezor Suite Mobile
v26.4.2, letting Trezor owners connect to Stellar dApps and sign with hardware-level security. The
Stellar transaction confirmation and signing flow on Trezor was improved and released in Trezor
firmware v2.12.1, alongside several additional Stellar maintenance fixes across Trezor Suite. On the
Soroban front, the upstream firmware implementation was submitted, and in the final week of the
quarter the Trezor team added Soroban support to their TODO, putting it on their roadmap for the
first time. This makes Soroban the highest-priority workstream heading into Q3.

## Past Deliverables

### 1. Ongoing Maintenance

Description from last quarter:

> Regular upkeep of the Stellar Ledger app and Trezor integrations in coordination with the Ledger
> and Trezor teams: responding to community issues and pull requests, keeping SDK and firmware
> dependencies current, and ensuring Stellar assets and protocol features remain fully supported.

Proof of completion:

- Trezor firmware v2.12.1:
  https://github.com/trezor/trezor-firmware/blob/main/core/CHANGELOG.T3W1.md#fixed — improved Stellar
  transaction confirmation/signing flow
- Trezor Suite Stellar fixes:
  https://github.com/trezor/trezor-suite/pulls?q=is%3Apr+author%3Aovercat+is%3Aclosed — merged
  Stellar maintenance work across Trezor Suite

The Stellar transaction confirmation and signing flow was refined and shipped in Trezor firmware
v2.12.1, making on-device review clearer for signers. Alongside it, several Stellar maintenance fixes
landed in Trezor Suite in coordination with the Trezor team, including Soroban contract token
resolution, Soroban URL prioritization in fiat services, and improved token icon resolution.

### 2. Stellar WalletConnect Support in Trezor Suite

Description from last quarter:

> Add WalletConnect support for Stellar in Trezor Suite, enabling users to connect their Trezor
> hardware wallets to Stellar dApps directly from the suite. This brings hardware-level signing
> security to WalletConnect-based Stellar applications and improves interoperability across the
> ecosystem.

Proof of completion:

- Trezor Suite Mobile v26.4.2: https://github.com/trezor/trezor-suite/releases/tag/v26.4.2%40mobile —
  Stellar WalletConnect support shipped

Stellar WalletConnect support was implemented and released to users in Trezor Suite (Mobile) v26.4.2.
Trezor owners can now connect their devices to WalletConnect-based Stellar dApps and approve
transactions with hardware-level security, extending Stellar's reach into the growing WalletConnect
ecosystem.

### 3. Soroban Support for Trezor

Description from last quarter:

> Implement Soroban transaction signing support for Trezor in collaboration with the Trezor team.
> This work follows prior design and discussion with the Trezor team. Due to current firmware team
> priorities, PR merge is not guaranteed within the quarter, but the implementation will be submitted
> and metrics (review feedback, CI results, community interest) will be tracked to guide future work.

Proof of completion:

- Development branch: https://github.com/overcat/trezor-firmware/pull/3 — Soroban
  `StellarInvokeHostFunctionOp` implementation

The Soroban signing implementation (`StellarInvokeHostFunctionOp`) was submitted upstream to
trezor-firmware. As anticipated in the Q2 plan, it did not merge within the quarter, but in the final
week of the quarter a key milestone was reached: the Trezor team added Soroban support to their TODO,
putting it on their roadmap for the first time. Development continues on a dedicated branch, and this
shift from design discussion to a planned firmware task makes Soroban the top priority for Q3.

## Proposed Impact

The primary goal for Q3 2026 is Soroban. Now that the Trezor team has added Soroban support to their
roadmap, delivering Soroban transaction signing on Trezor is the highest-priority workstream, working
alongside the Trezor firmware team to drive the integration forward. In parallel, we will add
Protocol 27 support to the Stellar Ledger app and its associated SDK/libraries, and continue ongoing
maintenance of both the Ledger and Trezor integrations. Together these keep Stellar first-class on
the two most widely used secure-hardware ecosystems as the network evolves.

## Proposed Deliverables

### 1. Soroban Support for Trezor

Advance Soroban transaction signing on Trezor in collaboration with the Trezor firmware team,
building on the `StellarInvokeHostFunctionOp` implementation already submitted upstream. With Soroban
now on the Trezor team's roadmap, the quarter's focus is integration: iterating on review feedback,
aligning the on-device confirmation UX, passing CI, and driving the work toward merge. This brings
hardware-secured Soroban smart contract interactions to Trezor users, a first for the ecosystem.
Because firmware team priorities can shift, merge within the quarter is not guaranteed, but the
implementation will be actively driven and review/CI/community-interest metrics tracked to guide next
steps.

Proof: Development activity and review progress on the Soroban firmware implementation, tracked via
the development branch and CI results.

### 2. Protocol 27 Support for the Ledger App and SDK

Add Protocol 27 support to the Stellar Ledger app and its associated SDK/integration libraries,
ensuring transactions built under the upcoming protocol upgrade continue to parse, display, and sign
correctly on Ledger devices. Keeping hardware signing current with each protocol upgrade prevents
breakage for security-conscious users and integrators when the network transitions.

Proof: Release/changelog for the Stellar Ledger app and SDK covering Protocol 27 support.

### 3. Ongoing Maintenance

Regular upkeep of the Stellar Ledger app and Trezor integrations in coordination with the Ledger and
Trezor teams: responding to community issues and pull requests, keeping SDK and firmware dependencies
current, and ensuring Stellar assets and protocol features remain fully supported.

Proof: Release tags and updated changelogs on GitHub.

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
