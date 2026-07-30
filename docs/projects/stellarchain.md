---
title: "StellarChain"
parent: Public Good Projects
proposal_issue: 60
proposer: devfed1
category: "Infrastructure Monitoring"
budget: "50000"
---

# StellarChain

_Explore the Stellar blockchain - transactions, accounts, contracts, ledgers, assets, markets, and
operations._

|                      |                                      |
| -------------------- | ------------------------------------ |
| **Category**         | Infrastructure Monitoring            |
| **Website**          | <https://stellarchain.io>            |
| **Repository**       | <https://github.com/stellarchain/v4> |
| **First Released**   | March 2024                           |
| **Intake**           | soft-launch                          |
| **Budget Requested** | 50000                                |

## Project Description

Stellarchain.io is a non-commercial, public blockchain explorer for the Stellar ecosystem that helps
users independently verify on-chain activity across mainnet, testnet, and futurenet. The platform
provides clear, mobile-first views for accounts, transactions, assets, ledgers, markets, and Soroban
contracts, with integrated data from Horizon, Soroban RPC, TOML metadata, and market feeds. It is
designed for both newcomers and advanced users through plain-language UX, progressive disclosure of
technical details, and fast search/navigation flows. By combining transparency, accessibility, and
reliable infrastructure, Stellarchain supports developers, integrators, auditors, and everyday users
who need trustworthy Stellar network insights.

## Team & Experience

Our team is led by:

**Florin Mangu, Project Manager**: responsible for product direction, delivery planning, stakeholder
coordination, prioritization, and execution tracking.

**Fedot Sereoja, Fullstack Developer:** responsible for architecture and implementation across
frontend and backend, including explorer UX, API integrations, network data pipelines, and
Soroban-related features.

Team experience in the Stellar ecosystem: We have hands-on experience building and operating a public
Stellar explorer that integrates core ecosystem services such as Horizon and Soroban RPC, supports
multiple Stellar networks (mainnet, testnet, futurenet), and delivers
contract/account/asset/transaction transparency features. Our work includes continuous iteration on
usability, mobile-first access, performance, metadata enrichment (including TOML-based asset
context), and reliable public data presentation for independent verification.

## Retroactive Impact

Over the last three months (April-June 2026), StellarChain continued improving public access to
Stellar network data and prepared the foundation for deeper Q3 transparency work. We expanded the v4
explorer with stronger contract views, improved API response consistency, better pagination, clearer
frontend states, and richer backend indexing paths for Soroban contracts, events, storage,
transactions, balances, and verification metadata.

We also worked on historical statistics infrastructure and large-scale data ingestion so that the
explorer can move beyond recent API windows and provide longer-term visibility into Stellar activity.
This included continued work around statistics storage, chart-ready metrics, and contract data
collection from ledger/RPC sources. These improvements help users and builders answer more practical
questions: what happened, when it happened, which accounts or contracts were involved, whether a
contract is a Stellar Asset Contract, and how indexed Soroban balances compare with classic asset
market data.

On the product side, we continued refining high-traffic explorer pages with clearer layouts, faster
loading behavior, improved contract detail pages, and more consistent mobile/desktop experiences. The
work reduces dead ends for users who search by transaction, account, contract, asset, or ledger, and
it prepares StellarChain for investigation, reporting, and sustainability features in the upcoming
quarter.

## Past Deliverables

1. **Expanded Soroban contract explorer surfaces - Completed** We improved contract detail pages with
   clearer History, Events, Storage, verification, source, SAC, and token-related fields. Contract
   pages now better separate normal contracts, token contracts, and Stellar Asset Contracts, while
   keeping links back to transactions and accounts.

2. **Contract indexing and balance infrastructure - Completed / ongoing backfill** We built and
   improved backend paths for collecting contract transactions, events, storage entries, holder
   balances, SAC metadata, executable metadata, and derived indexes. This gives the explorer a
   stronger base for contract analytics and future decompiler/verification work.

3. **Historical statistics foundation - Completed / expanded** We continued building chart-ready
   statistics storage and aggregation workflows so StellarChain can support historical network,
   market, payment, account, and contract metrics without relying only on short-lived API windows.

4. **API consistency and pagination improvements - Completed** We improved API response shapes,
   metadata handling, and pagination behavior for contract-related endpoints. This makes the public
   API easier to consume and reduces incorrect totals or incomplete frontend pagination states.

5. **Mobile and desktop UX refinements - Completed** We refined contract, market, statistics, and
   explorer page behavior across desktop and mobile, including loading states, empty states, table
   behavior, labels, and clearer data hierarchy.

6. **Data reliability and network operations - Completed / ongoing** We continued operating the
   infrastructure needed for StellarChain, including database-backed statistics, contract data
   ingestion, RPC/Horizon compatibility paths, and backend commands for rescanning, refreshing
   metadata, and rebuilding derived indexes.

## Proposed Impact

1. **Transaction Investigation and Safety Context** Give users, support teams, and ecosystem
   participants a practical way to trace suspicious or confusing account activity. The goal is not to
   make fraud determinations, but to provide clear evidence, graph context, known labels, timeline
   views, and exportable reports that help users understand fund movement.

2. **Sustainable Explorer Operations** Add a transparent, non-invasive affiliate and partner
   discovery layer so StellarChain can remain free to use while exploring long-term sustainability.
   This should be clearly disclosed, separated from explorer data, and implemented without paywalls
   or misleading rankings.

3. **Enhanced Soroban Contract Intelligence** Improve public transparency for Soroban contracts by
   indexing more contract data, separating SAC from custom Wasm contracts, improving token holder
   visibility, exposing source/provenance signals, and preparing a repeatable decompiler and
   verification workflow.

4. **Reliable Historical Data and Public APIs** Strengthen historical observability by expanding
   chart-ready metrics, data lake/backfill support, API pagination, exports, and developer-friendly
   endpoints. This helps builders, analysts, researchers, and users inspect Stellar activity over
   longer time ranges.

## Proposed Deliverables

1. **StellarChain Investigator: Transaction, Account, and Payment Tracing Tool**

   Deliverables:
   - Investigation workspace with search by account, transaction hash, asset, or contract.
   - Trace graph for account-to-account and account-to-contract flows.
   - Table view with grouped edges, amounts, operation counts, first seen, last seen, and direction.
   - Filters for operation type, asset, date range, hop depth, dust hiding, and grouped/expanded
     view.
   - Triage panel with case queue, watchlist, timeline, evidence list, and report export.
   - Read-only investigation mode suitable for support, education, and public safety workflows.
   - Backend trace endpoints such as `/v1/trace/address/{id}` and `/v1/trace/tx/{hash}` with
     pagination and depth controls.
   - JSON/CSV export for reports and reusable evidence.

   Ecosystem value: users affected by scams, mistaken transfers, or confusing account activity get a
   clearer way to investigate what happened. Developers and ecosystem support teams get a public,
   shareable investigation surface instead of relying only on raw transaction pages.

2. **Affiliate and Partner Discovery Layer for Sustainable Operations**

   Deliverables:
   - Dedicated partner/affiliate pages for relevant Stellar ecosystem services, wallets, exchanges,
     on/off ramps, infrastructure providers, and developer tools.
   - Clear disclosure labels for affiliate links and sponsored placements.
   - Admin/config layer for managing partner entries, categories, tracking URLs, status, ordering,
     and region/network notes.
   - Non-invasive placements on appropriate pages, such as asset pages, account onboarding context,
     wallet-related flows, and educational sections.
   - Basic click analytics that do not interfere with explorer privacy or core public data access.
   - UI rules that keep explorer data neutral and avoid presenting paid placements as verification,
     risk assessment, or endorsement.

   Ecosystem value: helps StellarChain explore a sustainable operating model while keeping explorer
   access free. Users can discover relevant services in context, and the explorer can reduce
   long-term dependence on grants without compromising data neutrality.

3. **Contract Intelligence, SAC Balances, and Verification Pipeline**

   Deliverables:
   - Complete the Soroban contract indexer workflow for transactions, events, storage entries,
     argument usages, holder balances, SAC metadata, and executable metadata.
   - Separate token holder views from contract token holdings on contract pages.
   - Add SAC reconciliation between indexed Soroban balances and classic asset market supply.
   - Expose clearer contract labels: SAC, custom Wasm contract, source available, legacy source
     verified, SEP-55 provenance attested, and SEP-58 reproducible build verification when available.
   - Add backend commands for periodic metadata refresh, derived index rebuilds, decompiler runs, and
     verification refreshes.
   - Store enough Wasm/source metadata to support future decompiler upgrades and repeated
     reprocessing.
   - Improve event decoding and raw fallback display for contracts with partially decoded data.

   Ecosystem value: contract users get more transparent, inspectable contract pages. Builders get a
   clearer view of contract usage, token balances, source/provenance signals, and indexed activity.
   This reduces confusion around SACs, custom contracts, and verification labels.

4. **Historical Data, Chart Pages, and Public API Reliability**

   Deliverables:
   - Expand historical chart pages under `/chart/{slug}` for network, market, payment, account,
     contract, and asset metrics.
   - Continue using chart-ready endpoints such as
     `/v1/network-metrics?metricKey={key}&bucketMinutes={n}&network={network}`.
   - Add or improve metrics such as `top-payers`, `top-receivers`, `top-contract-callers`,
     `contracts`, `invocations`, `dex-vol-xlm`, `active-addresses`, `accounts-created`,
     `accounts-merged`, `fee-charged`, and `tx-success`.
   - Add export options for selected chart/table datasets.
   - Improve API pagination metadata, exact totals where feasible, and cursor pagination for large
     datasets.
   - Use data lake/backfill workflows where needed to cover history beyond short RPC windows.
   - Add operational scripts for rebuilding derived indexes and refreshing metric buckets safely.

   Ecosystem value: builders and researchers get better long-term visibility into Stellar activity.
   Public users can inspect trends without needing to run their own infrastructure, and developers
   can rely on cleaner API responses for external tools.

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellarchain.io&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellarchain.io)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellarchain.io&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellarchain.io)
[![Criticality](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellarchain.io&query=%24.criticality_score&label=Criticality&color=E5484D)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellarchain.io)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellarchain.io&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellarchain.io)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellarchain.io&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellarchain.io)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
