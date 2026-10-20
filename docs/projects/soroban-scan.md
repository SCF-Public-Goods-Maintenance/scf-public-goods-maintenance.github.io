---
title: "Soroban Scan"
canonical_id: daoip-5:scf:project:rumble_fish_software_development_-_rfp
parent: Public Good Projects
proposal_issue: 194
proposer: kowalski
category: "Data Support"
budget: "$6,600"
health_endpoint: "https://api-sorobanscan.rumblefishdev.com/health"
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
| **Budget Requested**    | $6,600                                                                                              |
| **Maintenance Reserve** | $4000 in XLM                                                                                        |
| **Other**               | $2600 in XLM                                                                                        |

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

- Protocol 27: stellar-xdr 26→27 so P27 ledgers decode
  ([PR#325](https://github.com/rumblefishdev/soroban-block-explorer/pull/325)). Galexie pinned
  durably, and the ingestion-lag alarm reworked so it fires on a full stop
  ([PR#323](https://github.com/rumblefishdev/soroban-block-explorer/pull/323)).
- Protocol 28: Galexie 28.0.1 and stellar-xdr 27→28 shipped before the 16 Sept pubnet vote
  ([PR#456](https://github.com/rumblefishdev/soroban-block-explorer/pull/456)).
- Protocol 29: Galexie bumped to 29.0.0
  ([PR#590](https://github.com/rumblefishdev/soroban-block-explorer/pull/590)). We then added a
  protocol watch that alerts us when a Galexie with a newer captive core is released and ours is not
  on it ([PR#605](https://github.com/rumblefishdev/soroban-block-explorer/pull/605)).

Testnet: launched 5–6 October 2026 at testnet.sorobanscan.rumblefish.dev. It runs the same binaries,
reads from SDF's public data lake, and has its own database and alarms. The Mainnet/Testnet switcher
is in the UI.

Ecosystem integrations:

- Inferara's soroban-ret decompiler is integrated as the experimental Code tab on contract pages.
- the Stellar Prices API uses the explorer's ClickHouse index (soroban_events / soroban_contracts)
  for its pool-coverage sweep.

Feedback loop: a "Report a bug" link in the navigation opens a GitHub issue
([PR#353](https://github.com/rumblefishdev/soroban-block-explorer/pull/353)). Feature requests,
including some from SCF Pilots, were triaged and shipped within the quarter.

Engineering throughput (develop branch, 8 Jul – 8 Oct): 2,472 commits, 282 merged PRs, 167 tracked
tasks closed, 18 tagged production deploys.
<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

### 2026 Q3

Protocol upgrades & ingestion reliability

- Protocol 27 decode: [PR#325](https://github.com/rumblefishdev/soroban-block-explorer/pull/325) ·
  Galexie pin + full-stop alarm:
  [PR#323](https://github.com/rumblefishdev/soroban-block-explorer/pull/323)
- Protocol 28 readiness: [PR#456](https://github.com/rumblefishdev/soroban-block-explorer/pull/456) ·
  Protocol 29 Galexie: [PR#590](https://github.com/rumblefishdev/soroban-block-explorer/pull/590) ·
  Galexie protocol watch: [PR#605](https://github.com/rumblefishdev/soroban-block-explorer/pull/605)
- Seconds-based ingestion-lag metric:
  [PR#345](https://github.com/rumblefishdev/soroban-block-explorer/pull/345) · Observability sweep:
  [PR#424](https://github.com/rumblefishdev/soroban-block-explorer/pull/424)

Testnet environment

- [PR#553](https://github.com/rumblefishdev/soroban-block-explorer/pull/553),
  [PR#558](https://github.com/rumblefishdev/soroban-block-explorer/pull/558),
  [PR#559](https://github.com/rumblefishdev/soroban-block-explorer/pull/559),
  [PR#562](https://github.com/rumblefishdev/soroban-block-explorer/pull/562),
  [PR#566](https://github.com/rumblefishdev/soroban-block-explorer/pull/566),
  [PR#567](https://github.com/rumblefishdev/soroban-block-explorer/pull/567),
  [PR#600](https://github.com/rumblefishdev/soroban-block-explorer/pull/600),
  [PR#603](https://github.com/rumblefishdev/soroban-block-explorer/pull/603),
  [PR#611](https://github.com/rumblefishdev/soroban-block-explorer/pull/611),
  [PR#636](https://github.com/rumblefishdev/soroban-block-explorer/pull/636) (and others). Live:
  https://testnet.sorobanscan.rumblefish.dev

Soroban decoding

- Token-flow decode from Soroban events:
  [PR#332](https://github.com/rumblefishdev/soroban-block-explorer/pull/332)
- Execution trace (nested call tree from diagnostic events):
  [PR#375](https://github.com/rumblefishdev/soroban-block-explorer/pull/375)
- Events identified the way stellar-rpc identifies them:
  [PR#465](https://github.com/rumblefishdev/soroban-block-explorer/pull/465),
  [PR#473](https://github.com/rumblefishdev/soroban-block-explorer/pull/473),
  [PR#475](https://github.com/rumblefishdev/soroban-block-explorer/pull/475),
  [PR#579](https://github.com/rumblefishdev/soroban-block-explorer/pull/579),
  [PR#580](https://github.com/rumblefishdev/soroban-block-explorer/pull/580)
- soroban-ret decompiled Code tab (with Inferara):
  [PR#384](https://github.com/rumblefishdev/soroban-block-explorer/pull/384),
  [PR#385](https://github.com/rumblefishdev/soroban-block-explorer/pull/385),
  [PR#388](https://github.com/rumblefishdev/soroban-block-explorer/pull/388)

Value, assets, accounts, pools

- Net-settled transaction value:
  [PR#355](https://github.com/rumblefishdev/soroban-block-explorer/pull/355) · lossless value-flow
  index: [PR#451](https://github.com/rumblefishdev/soroban-block-explorer/pull/451)
- LP analytics (TVL, volume, fee revenue):
  [PR#380](https://github.com/rumblefishdev/soroban-block-explorer/pull/380) · Soroswap adapter:
  [PR#447](https://github.com/rumblefishdev/soroban-block-explorer/pull/447) · Soroban-AMM
  completeness: [PR#518](https://github.com/rumblefishdev/soroban-block-explorer/pull/518),
  [PR#598](https://github.com/rumblefishdev/soroban-block-explorer/pull/598)
- SEP-2 federated addresses:
  [PR#444](https://github.com/rumblefishdev/soroban-block-explorer/pull/444) · SAC → classic asset:
  [PR#387](https://github.com/rumblefishdev/soroban-block-explorer/pull/387) · trustlines + signers:
  [PR#426](https://github.com/rumblefishdev/soroban-block-explorer/pull/426),
  [PR#432](https://github.com/rumblefishdev/soroban-block-explorer/pull/432)

Security, privacy, performance

- ClickHouse least-privilege grants:
  [PR#531](https://github.com/rumblefishdev/soroban-block-explorer/pull/531) · GTM custom-script
  blocklist: [PR#537](https://github.com/rumblefishdev/soroban-block-explorer/pull/537)
- Privacy policy: [PR#486](https://github.com/rumblefishdev/soroban-block-explorer/pull/486) ·
  analytics wait for consent:
  [PR#529](https://github.com/rumblefishdev/soroban-block-explorer/pull/529)
- Read-path performance after load test:
  [PR#348](https://github.com/rumblefishdev/soroban-block-explorer/pull/348) · fewer DB round trips:
  [PR#393](https://github.com/rumblefishdev/soroban-block-explorer/pull/393)

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

Other: move to a dedicated domain, `sorobanscan.com` ($2,600 in XLM)

Soroban Scan currently runs on Rumble Fish company domains. We will move it to its own domain so
links to the explorer and its APIs no longer depend on our agency's hostnames. Work involved:

- Explorer frontends: mainnet to `sorobanscan.com` and testnet to `testnet.sorobanscan.com`.
- Explorer APIs: mainnet and testnet APIs moved to `sorobanscan.com` subdomains, with CORS, Turnstile
  widget hostnames and Cloudflare edge rules (WAF, bot settings, caching) reconfigured for each one.
- Stellar Prices API: it is served from a Soroban Scan subdomain
  (`prices-api.sorobanscan.rumblefish.dev`), so it moves to a `sorobanscan.com` subdomain as well.
- DNS, TLS certificates and the public infrastructure-as-code updated for all of the above.
- Redirect infrastructure: permanent, path-preserving redirects from every old URL (frontends, APIs
  and Prices API), so existing links, bookmarks and integrations keep working.
- Google Analytics and consent configuration updated for the new domain.
- Monitoring: uptime checks and alarms moved to the new hostnames, and the `health_endpoint` on this
  page updated.
- Docs, OpenAPI spec and in-app links updated.
- Communicating the change to the Stellar community, with migration notes for API and Prices API
  users.

Done when both networks and the Prices API are served from `sorobanscan.com`, old URLs redirect, and
the change has been announced.

<!-- markdownlint-enable MD034 -->

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Arumble_fish_software_development_-_rfp&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Arumble_fish_software_development_-_rfp)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Arumble_fish_software_development_-_rfp&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Arumble_fish_software_development_-_rfp)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Arumble_fish_software_development_-_rfp&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Arumble_fish_software_development_-_rfp)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Arumble_fish_software_development_-_rfp&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Arumble_fish_software_development_-_rfp)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
