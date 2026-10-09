---
title: "Soroban Scan"
parent: Public Good Projects
proposal_issue: 194
proposer: kowalski
category: "Data Support"
budget: "$4,000"
---

# Soroban Scan

<!-- markdownlint-disable MD036 -->

_Soroban Scan is an open-source, Soroban-first Stellar block explorer that decodes smart contract
calls, CAP-67 events, and swaps into human-readable transaction views, on mainnet and testnet._
<!-- markdownlint-enable MD036 -->

|                         |                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------- |
| **Category**            | Data Support                                                                                        |
| **Website**             | <https://sorobanscan.rumblefish.dev/>                                                               |
| **Repository**          | <https://github.com/rumblefishdev/soroban-block-explorer>                                           |
| **First Released**      | 17 July 2026, interest form sent 03 September 2026                                                  |
| **Intake**              | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/132> |
| **Budget Requested**    | $4,000                                                                                              |
| **Maintenance Reserve** | $[2000] in XLM                                                                                      |
| **Other**               | $[2000] in XLM                                                                                      |

## Project Description

<!-- markdownlint-disable MD034 -->

Soroban Scan is an open-source, Soroban-first block explorer for Stellar, independent of
stellar.expert and StellarChain. It decodes invoke-host-function calls, CAP-67 contract events and
SEP-41 token transfers into readable views instead of raw XDR, including the nested execution trace
of each call. It covers ledgers, transactions, accounts, assets, Soroban contracts (with an
experimental decompiled Code tab built with Inferara's soroban-ret), NFTs, and liquidity pools on
classic and Soroban AMMs.

It ingests LedgerCloseMeta directly (its own Galexie on mainnet, SDF's public data lake on testnet)
into its own ClickHouse schema, with no dependency on Horizon. Indexer, API, frontend and
infrastructure-as-code are public on GitHub.

Mainnet: https://sorobanscan.rumblefish.dev Testnet: https://testnet.sorobanscan.rumblefish.dev

Built under SCF RFP-4; this award keeps it running and maintained.
<!-- markdownlint-enable MD034 -->

## Team & Experience

<!-- markdownlint-disable MD034 -->

Soroban Scan is built and maintained by [Rumble Fish](https://www.rumblefish.dev/), a Web3
engineering agency, which received the SDF Build Award grant for the project (RFP: Soroban-first
Block Explorer). Active maintainers on GitHub: [@karolko9](https://github.com/karolko9),
[@stkrolikiewicz](https://github.com/stkrolikiewicz), [@Efem67](https://github.com/Efem67),
[@fikoayee](https://github.com/fikoayee), [@karolkow435345](https://github.com/karolkow435345),
[@kowalski](https://github.com/kowalski).
<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->

Window: 8 July – 8 October 2026. In this period Soroban Scan went from a pre-launch build behind
basic auth to a public explorer on two networks.

Network compatibility:

- Protocol 27: stellar-xdr 26→27 so P27 ledgers decode (#325). Galexie pinned durably, and the
  ingestion-lag alarm reworked so it fires on a full stop (#323).
- Protocol 28: Galexie 28.0.1 and stellar-xdr 27→28 shipped before the 16 Sept pubnet vote (#456).
- Protocol 29: Galexie bumped to 29.0.0 (#590). We then added a protocol watch that alerts us when a
  Galexie with a newer captive core is released and ours is not on it (#605).

Testnet: launched 5–6 October 2026 at testnet.sorobanscan.rumblefish.dev. It runs the same binaries,
reads from SDF's public data lake, and has its own database and alarms. The Mainnet/Testnet switcher
is in the UI.

Ecosystem integrations:

- Inferara's soroban-ret decompiler is integrated as the experimental Code tab on contract pages.
- the Stellar Prices API uses the explorer's ClickHouse index (soroban_events / soroban_contracts)
  for its pool-coverage sweep. Say this only if the team is comfortable describing it as an
  integration.

Feedback loop: a "Report a bug" link in the navigation opens a GitHub issue (#353). Feature requests,
including some from SCF Pilots, were triaged and shipped within the quarter.

Engineering throughput (develop branch, 8 Jul – 8 Oct): 2,472 commits, 282 merged PRs, 167 tracked
tasks closed, 18 tagged production deploys.
<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

Protocol upgrades & ingestion reliability

- Protocol 27 decode: https://github.com/rumblefishdev/soroban-block-explorer/pull/325 · Galexie
  pin + full-stop alarm: …/pull/323
- Protocol 28 readiness: …/pull/456 · Protocol 29 Galexie: …/pull/590 · Galexie protocol watch:
  …/pull/605
- Seconds-based ingestion-lag metric: …/pull/345 · Observability sweep: …/pull/424

Testnet environment

- …/pull/553, /558, /559, /562, /566, /567, /600, /603, /611, /636 (and others; full list in task
  0553). Live: https://testnet.sorobanscan.rumblefish.dev

Soroban decoding

- Token-flow decode from Soroban events: …/pull/332
- Execution trace (nested call tree from diagnostic events): …/pull/375
- Events identified the way stellar-rpc identifies them: …/pull/465, /473, /475, /579, /580
- soroban-ret decompiled Code tab (with Inferara): …/pull/384, /385, /388

Value, assets, accounts, pools

- Net-settled transaction value: …/pull/355 · lossless value-flow index: …/pull/451
- LP analytics (TVL, volume, fee revenue): …/pull/380 · Soroswap adapter: …/pull/447 · Soroban-AMM
  completeness: …/pull/518, /598
- SEP-2 federated addresses: …/pull/444 · SAC → classic asset: …/pull/387 · trustlines + signers:
  …/pull/426, /432

Security, privacy, performance

- ClickHouse least-privilege grants: …/pull/531 · GTM custom-script blocklist: …/pull/537
- Privacy policy: …/pull/486 · analytics wait for consent: …/pull/529
- Read-path performance after load test: …/pull/348 · fewer DB round trips: …/pull/393

(Use full URLs in the form. … = https://github.com/rumblefishdev/soroban-block-explorer.)
<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

Stay available and current with the network. We target ≥ 99.5% service availability, measured by the
PG program polling our public health endpoint, on mainnet and testnet, and decoding support for any
protocol upgrade before its pubnet vote, as we did for protocol 28.
<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

Maintenance reserve (capacity, not itemised). Expected work:

- Galexie and stellar-xdr bumps for any protocol upgrade, ahead of the pubnet vote, on mainnet and
  testnet.
- Keeping both networks ingesting and the alarms honest. Dependency, toolchain and security updates.
- Bug triage and fixes from GitHub issues. Known items include deployer attribution on fee-bump
  transactions and NFT completeness gaps. Reported next quarter as Reserved vs Actual.

<!-- markdownlint-enable MD034 -->

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
