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

#### D1. Soroban Support for Trezor

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

#### D2. Protocol 27 Support for the Ledger App and SDK

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

#### D3. Ongoing Maintenance

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

### 2026 Q2

#### 1. Ongoing Maintenance

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

#### 2. Stellar WalletConnect Support in Trezor Suite

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

#### 3. Soroban Support for Trezor

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

In Q4 2026, we will focus on the Ledger app: adding Protocol 28 support so Ledger users can keep
signing as the network upgrades, and showing any Stellar Asset Contract in a readable form, not just
the tokens on a fixed list. Since the app was audited in September, we won't release these updates on
their own this quarter. They will ship with future updates after the next audit. We will keep
maintaining the Ledger and Trezor integrations in parallel.

Note. Ledger has also changed how the Stellar Ledger app is developed. Development now happens in a
private repository, and Ledger syncs the code to the public repository from time to time. This is
Ledger's decision. As a result, we may not be able to share PR links or release notes for Ledger
work, and changes will only show up in the public repository after each sync.

## Proposed Deliverables

### P1. Protocol 28 Support for the Ledger App

Add Protocol 28 support to the Stellar Ledger app, so it can parse, display, and sign transactions
that use the new protocol features. We will finish this work this quarter, and it will be released
with future updates after the next audit.

Proof: The changes in the public Stellar Ledger app repository once Ledger syncs them, which may be
several months after the work is done. PR links and release notes may not be available.

### P2. Readable Display for Any Stellar Asset Contract on Ledger

Right now, the Ledger app only shows SAC token operations in a readable form for tokens on a fixed
list. We will extend this to any SAC, so every SAC in a contract call is shown in a readable form. We
will also provide a JavaScript library that helps wallets look up the SACs in a transaction. As with
P1, we will finish the Ledger app work this quarter, and it will be released with future updates
after the next audit.

Proof: The JavaScript library repository, and the Ledger app changes in the public repository once
Ledger syncs them, which may be several months after the work is done.

### P3. Ongoing Maintenance

Regular upkeep of the Stellar Ledger app and Trezor integrations in coordination with the Ledger and
Trezor teams: responding to community issues and pull requests, keeping SDK and firmware dependencies
current, and ensuring Stellar assets and protocol features remain fully supported.

Proof: Commits or PRs, or release notes.

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_hardware_wallet_support)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
