---
title: "Stellar Hardware Wallet Support"
canonical_id: daoip-5:scf:project:stellar_hardware_wallet_support
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

In Q3 2026, Soroban support shipped on Trezor. Working with the Trezor firmware team, we released
Soroban transaction and authorization entry signing in Trezor firmware v2.12.4, so Trezor users can
approve smart contract transactions on their device. v2.12.5 shows SEP-41 token transfers and
approvals as token operations instead of raw contract calls. Protocol 27 delegated authentication
(CAP-71) and contract creation are merged and will ship in the next firmware release.

On Ledger, Protocol 27 (CAP-71) support shipped in Stellar Ledger app v6.1.0, available in Ledger
Wallet. The release passed a security audit with SDF's support. It displays every authorization a
smart contract transaction requests, skips redundant review screens, and adds validation to XDR
parsing and APDU handling. Maintenance work added USDT0 support and reduced the app's size.

## Past Deliverables

### 2026 Q3

#### 1. Soroban Support for Trezor

Description from last quarter:

> Advance Soroban transaction signing on Trezor in collaboration with the Trezor firmware team,
> building on the `StellarInvokeHostFunctionOp` implementation already submitted upstream. With
> Soroban now on the Trezor team's roadmap, the quarter's focus is integration: iterating on review
> feedback, aligning the on-device confirmation UX, passing CI, and driving the work toward merge.
> This brings hardware-secured Soroban smart contract interactions to Trezor users — a first for the
> ecosystem. Because firmware team priorities can shift, merge within the quarter is not guaranteed,
> but the implementation will be actively driven and review/CI/community-interest metrics tracked to
> guide next steps.

Proof of completion:

- Trezor firmware v2.12.4:
  https://github.com/trezor/trezor-firmware/blob/main/core/CHANGELOG.T3T1.md#2124-19th-august-2026 —
  Soroban smart contract transaction signing (`StellarInvokeHostFunctionOp`) and Soroban
  authorization entry signing
- Trezor firmware v2.12.5:
  https://github.com/trezor/trezor-firmware/blob/main/core/CHANGELOG.T3T1.md#2125-16th-september-2026
  — SEP-41 `transfer`/`approve` invocations of Stellar Asset Contracts and trusted token contracts
  shown as token operations
- All commits this quarter:
  https://github.com/trezor/trezor-firmware/commits/main/?author=overcat&since=2026-07-01&until=2026-09-30

Soroban support was merged upstream with the Trezor team and shipped this quarter. Firmware v2.12.4
supports signing Soroban smart contract transactions and authorization entries, and v2.12.5 displays
SEP-41 token transfers and approvals as token operations instead of raw contract calls. Protocol 27
delegated authentication (CAP-71) and contract creation are merged for the next release. This is a
major milestone: Trezor users now have fairly complete Soroban support. 🎉

#### 2. Protocol 27 Support for the Ledger App and SDK

Description from last quarter:

> Add Protocol 27 support to the Stellar Ledger app and its associated SDK/integration libraries,
> ensuring transactions built under the upcoming protocol upgrade continue to parse, display, and
> sign correctly on Ledger devices. Keeping hardware signing current with each protocol upgrade
> prevents breakage for security-conscious users and integrators when the network transitions.

Proof of completion:

- https://github.com/LedgerHQ/app-stellar/commit/88f590f2504619641037a1a355ccb4e2a5fed836 — add
  Protocol 27 (CAP-71) Soroban authorization support
- All commits this quarter:
  https://github.com/LedgerHQ/app-stellar/commits/develop?author=overcat&since=2026-07-01&until=2026-09-30

Protocol 27 support shipped in Stellar Ledger app v6.1.0, available in Ledger Wallet. The release
passed a security audit with SDF's support. The app parses and signs the new authorization
credentials and signing payloads introduced by Protocol 27 (CAP-71). It also displays every Soroban
authorization entry and skips redundant ones, shortening the review for about two thirds of Soroban
transactions.

#### 3. Ongoing Maintenance

Description from last quarter:

> Regular upkeep of the Stellar Ledger app and Trezor integrations in coordination with the Ledger
> and Trezor teams: responding to community issues and pull requests, keeping SDK and firmware
> dependencies current, and ensuring Stellar assets and protocol features remain fully supported.

Proof of completion (a representative selection; all commits are linked in the two deliverables
above):

- https://github.com/LedgerHQ/app-stellar/commit/f6b0003665987420004eccae5a2981b7cf1d9e16 — Ledger:
  reject signing payloads with unreviewed trailing bytes
- https://github.com/LedgerHQ/app-stellar/commit/5bd0e89a96584281521ee68ed8a3232ebadb3a9a — Ledger:
  reject flag values the protocol does not define
- https://github.com/LedgerHQ/app-stellar/commit/7344d58c584d2a46a86352d479b3d241d583a8ec — Ledger:
  harden XDR parser allocations against untrusted length prefixes
- https://github.com/LedgerHQ/app-stellar/commit/988688afedc12111f88ba90fa4ac194d4bc30a45 — Ledger:
  enforce bounded type invariants at construction
- https://github.com/LedgerHQ/app-stellar/commit/9129fe4292f714d14253c9333e59c025ed664ba5 — Ledger:
  reject empty ED25519 signed-payload signers at parse time
- https://github.com/LedgerHQ/app-stellar/commit/6da196dcef42ec5ebf863810a38c6530e69d1949 — Ledger:
  bind APDU chunks to the active signing instruction
- https://github.com/LedgerHQ/app-stellar/commit/3c773c52b729bd975077bd817b8d2720768b5d65 — Ledger:
  display full asset issuer addresses during review
- https://github.com/LedgerHQ/app-stellar/commit/98d9bbb979acb2f0ce57b8dae9798fd9c3f8691d — Ledger:
  remove the app's only `f64`, cutting flex `.text` by 6.9%
- https://github.com/LedgerHQ/app-stellar/commit/66f9e24836760aa16d90b1be75095ef3b6952c13 — Ledger:
  add support for the USDT0 token
- https://github.com/trezor/trezor-firmware/commit/d8b61fd6e0acbdaf2d598d8ae13b459cc5dfff54 — Trezor:
  modernize Stellar Python type hints and drop dead code

Outside Protocol 27, the Ledger app's XDR parsing and APDU handling now reject malformed or
unexpected transaction data, so the data a user reviews matches the data they sign. The app now
displays full asset issuer addresses, which helps users tell apart assets with similar codes. The app
is also smaller and supports the USDT0 stablecoin.

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
