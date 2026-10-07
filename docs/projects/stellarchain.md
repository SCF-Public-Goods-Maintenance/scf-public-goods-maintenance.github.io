---
title: "StellarChain"
canonical_id: daoip-5:scf:project:stellarchain.io
parent: Public Good Projects
proposal_issue: 60
proposer: devfed1
category: "Infrastructure Monitoring"
budget: "50000"
health_endpoint: "https://api.stellarchain.io/"
---

# StellarChain

_Explore the Stellar blockchain - transactions, accounts, contracts, ledgers, assets, markets, and
operations._

|                      |                                      |
| -------------------- | ------------------------------------ |
| **Category**         | Infrastructure Monitoring            |
| **Website**          | <https://stellarchain.io>            |
| **Repository**       | <https://github.com/stellarchain/v4> |
| **API Repository**   | <https://github.com/stellarchain/v4-api> |
| **Proposed Quarter** | 2026 Q4 (October-December) |
| **First Released**   | March 2024                           |
| **Intake**           | soft-launch                          |
| **Budget Requested** | $50,000 |
| **Maintenance Reserve** | $5,000 |
| **Other** | $45,000 |

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

During Q3 2026 (July-September), with final integration and QA continuing just after the quarter
closed, we took StellarChain beyond the core explorer experience. We added an Account Trust Checker
and a more advanced investigation flow for indexed classic payment activity. Users can search by
account or transaction, follow bounded candidate paths, filter by asset, date, or ledger, review
grouped payments and timelines, keep a local case queue, and export the current page as JSON, CSV, or
HTML. We present this information as evidence, not as a fraud verdict, and we show the coverage limits
whenever the available history may be incomplete.

Statistics also received a major rebuild. The explorer now has dedicated metric pages, selectable
time ranges and bucket sizes, clearer tooltips, keyboard and pointer navigation, older-history
loading, and CSV exports that keep the exact source values. On the backend, we added safer forwardfill
and repair tools, bounded metric windows, pagination metadata, and read models that avoid scanning the
largest statistics tables without limits. Where the available data is not reliable enough for a
metric, we leave it disabled instead of guessing from unrelated aggregates.

We also made contract pages easier to understand. SACs and custom Wasm contracts are separated more
clearly, holder and holding views are easier to inspect, and contract events, storage, arguments,
balances, RPC fallback, source, and provenance now have more precise labels. SEP-55 attestations,
decompiled source, and legacy verification remain separate signals. We do not show a SEP-58
reproducible-build claim until a rebuild has actually been completed and matched.

For sustainability, we prepared a Coinzilla native-ad placement that only loads after optional-cookie
consent and always carries a visible advertising label. It stays separate from explorer evidence,
rankings, verification, and account trust results. The placement is off by default and cannot show
live ads until Coinzilla approves the site and provides a valid publisher zone. Partner pages,
catalog management, regional metadata, and privacy-reviewed click analytics are still future work.

At the same time, we kept working on Orion, our full-history data service. As the work progressed, we
decided not to keep extending several fragmented import paths just to meet the short-term need. That
would have left us with more duplication and maintenance work later. Instead, we chose the more
ambitious route: a storage-efficient, Horizon-compatible service that can keep Stellar's full history
synchronized with new ledgers. Orion made meaningful progress during Q3, but it is not released or
counted as a completed deliverable. Full-history integration, account-history publication,
end-to-end API validation, and complete Horizon compatibility will continue through Q4 and future
funding work.

We also released StellarKey publicly: an open-source, self-custodial Stellar wallet with Merchant
Mode and our own Private Payments implementation. The wallet and merchant tools are available now.
Private Payments Protocol V2 remains an unaudited, Testnet-only preview and must not be used with real
funds. StellarKey is part of the wider ecosystem we are building around StellarChain, not a
replacement for any of the Q3 commitments below.

## Past Deliverables

### 2026 Q3

> **A note on scope:** The list below covers what we formally committed to for Q3, but it is only one
> part of the wider ecosystem we are building. In parallel, we are working on full-history data,
> synchronized APIs, the explorer, contract intelligence, a self-custodial wallet, merchant tools,
> and privacy research. We count work as completed only when it is released and can be checked. The
> larger projects that are still in progress are listed separately and clearly marked.

#### Investigator for accounts, transactions, and payment activity — Delivered for the data we have indexed

We shipped two ways to use the Investigator. Basic mode gives newcomers a simpler Account Trust
Checker, while Advanced mode adds account and transaction search, one-hop evidence, bounded
two-hop candidate paths, and filters for operation, asset, date, ledger, direction, and small
amounts. Results can be viewed as grouped flows or individual events, explored on a payment map
and timeline, saved in a local case queue, paged through, and exported as JSON, CSV, or HTML.

The API always shows its coverage and any truncation. Asset-first search is still switched off
until the additional index is installed and populated. We also do not describe contract activity
as funds flow until caller and transfer provenance can be shown properly.

Evidence: [frontend investigation and reporting](https://github.com/stellarchain/v4/commit/5795502),
[case queue and chart/investigator integration](https://github.com/stellarchain/v4/commit/45601e3),
[paginated trace API](https://github.com/stellarchain/v4-api/commit/deb5e02), and
[bounded depth and asset-side read models](https://github.com/stellarchain/v4-api/commit/f96e7e8).

#### Affiliate and partner layer — Partially delivered

We added one optional Coinzilla native-ad placement on the homepage. It has a visible
`Advertisement` label, a short explanation, configuration checks, optional-cookie consent, and
failure isolation. There is also a development preview that never contacts Coinzilla.

The ad stays away from Account Trust Checker, investigation evidence, rankings, verification,
and contract provenance. It will not show live ads until Coinzilla approves the site and provides
a valid zone ID. Partner pages, the partner catalog and admin tools, regional notes, and click
analytics are still to come.

Evidence: [Coinzilla native-ad placement](https://github.com/stellarchain/v4/blob/21c663ac42f393d9916198e399e0363dfc52ee9a/src/components/ads/CoinzillaNativeAd.tsx),
[configuration checks](https://github.com/stellarchain/v4/blob/21c663ac42f393d9916198e399e0363dfc52ee9a/src/lib/ads/coinzilla.ts), and
[sponsored placement rules](https://github.com/stellarchain/v4/blob/21c663ac42f393d9916198e399e0363dfc52ee9a/UX-CONTRACT.md).

#### Contract intelligence, SAC balances, and verification — Delivered for current coverage; deeper verification continues

We expanded contract indexing and explorer pages for transactions, events, storage, argument
usage, balances, and holder balances. We also improved SAC event parsing and metadata, added RPC
fallback, and made SAC supply comparison available alongside separately calculated classic asset
supply.

The labels are now more honest about what each signal means: SAC, custom Wasm, source available,
decompiled source, legacy verification, and SEP-55 provenance are kept separate. Decompiled code
is not presented as a verified build. SEP-58 reproducible builds, complete contract coverage, and
reliable contract-caller or token-transfer attribution remain gated until we can prove them.

Evidence: [SAC reconciliation and holder views](https://github.com/stellarchain/v4/commit/39dc828),
[contract metrics and balance indexing](https://github.com/stellarchain/v4-api/commit/fb9e73a),
[SEP-55 verification hardening](https://github.com/stellarchain/v4-api/commit/fc2b6da), and
[contract RPC fallback](https://github.com/stellarchain/v4-api/commit/6b5d66f).

#### Historical charts and public API reliability — Delivered for supported metrics

We redesigned the Statistics overview and added 21 individual `/chart/{slug}` pages. They support
24-hour, 7-day, one-month, and one-year ranges, with five-minute, hourly, or daily buckets where
the source data supports them. Charts now include interactive tooltips, keyboard and pointer
navigation, older-history loading, related-chart links, and CSV exports for the current page.

The public network-metrics API now uses bounded 1–30 day windows, pagination metadata, source
provenance, request cancellation, and clear errors for unsupported bucket sizes. We also added
guarded forwardfill and repair tools without restarting the historical backfill. Metrics such as
asset-level volume and rankings, top payers, top receivers, top contract callers, and a corrected
transaction-fee series remain unpublished until their coverage and read models are ready.

Evidence: [network metrics API](https://github.com/stellarchain/v4-api/commit/71f0670),
[guarded forwardfill and repairs](https://github.com/stellarchain/v4-api/commit/fa5a92e),
[bounded metric reads](https://github.com/stellarchain/v4-api/commit/96c812a), and
[historical chart UX](https://github.com/stellarchain/v4/commit/5795502).

### Additional work during Q3

**Orion full-history infrastructure — In progress and not released**

We continued building Orion as a storage-efficient, Horizon-compatible service for Stellar's history.
XDR remains the authoritative source, with compact Parquet history and indexes for account activity
and transaction lookups. Full-history integration, account-history publication, gap handling, and
end-to-end API validation remain unfinished. Orion has no public repository yet and is not counted
as a completed Q3 commitment. Its release and historical coverage checks are proposed for Q4 below.

**StellarKey wallet and merchant tools — Public release; Private Payments remains Testnet-only**

We also released StellarKey publicly as an open-source, self-custodial Stellar wallet. Users keep
control of their keys and encrypted records. The wallet supports sending, receiving, Stellar DEX
swaps, batch payments, encrypted vaults, and backups. Merchant Mode adds QR checkout, inventory,
invoices, refunds, reconciliation, and sales reports without making StellarKey a custodial payment
processor.

Private Payments remains a Testnet development feature. Mainnet use is blocked pending the required
independent review and redeployment. Deposits, withdrawals, the submitting Stellar account, and
timing remain public; we do not describe this as a released Mainnet privacy protocol.

StellarKey is part of the wider ecosystem we are building around StellarChain. It is additional Q3
work, separate from the four commitments above. The Q4 budget below funds the five proposed Orion
and explorer deliverables.

Public links: [StellarKey](https://stellarkey.io),
[source and current documentation](https://github.com/stellarchain/io.stellarkey), and
[StellarKey is now public! — video demonstration](https://www.youtube.com/watch?v=R5xJyHOJ2Uo).

### 2026 Q2

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

In Q4 2026, we want to bring the work started in Q3 together: release Orion, connect its full-history
service to StellarChain, and make the explorer easier and faster to use. Users should be able to
look up an old transaction, follow an account's activity, or open a ledger through the same explorer
they use for recent activity. The available history and any gaps will stay visible.

We will also rebuild the main explorer views around clearer summaries. Account pages will bring
balances, asset allocation, and an activity calendar together. Ledger and transaction pages will
explain what happened first, with the exact operations, fees, identifiers, and raw data still easy
to inspect. Statistics will move into a searchable workspace with longer time ranges, useful
comparisons, and exports that keep the exact source values.

The goal is practical: give everyday users a clearer way to understand Stellar activity, and give
builders and researchers dependable access to its history without running their own archive. We
will measure performance against the current explorer, keep unsupported metrics clearly marked,
and make live activity and network observations easier to check. Alongside this work, we will keep
capacity available for maintenance, security fixes, protocol changes, and support.

## Proposed Deliverables

### 2026 Q4

We plan to deliver the work below by **31 December 2026**, covering the **October-December 2026**
quarter. As in our Q3 report, we count work as complete only when it is released and can be checked.
A working prototype or a finished import is progress, but it does not replace the public release
and the checks needed for each item.

### Budget Allocation

| Allocation | Amount |
| --- | ---: |
| Maintenance reserve | $5,000 |
| Other: Q4 deliverables | $45,000 |
| **Total requested** | **$50,000** |

We are reserving $5,000 for maintenance that comes up during the quarter, including security fixes,
protocol compatibility, dependency and toolchain updates, incidents, and user support. The other
$45,000 covers the work below. We will report actual spending for maintenance and the other work
separately, without counting the same work twice.

| Deliverable | Budget |
| --- | ---: |
| D1. Orion full-history infrastructure | $20,000 |
| D2. Historical API and explorer integration | $8,000 |
| D3. Clearer and faster explorer pages | $8,000 |
| D4. Historical statistics and analytics | $6,000 |
| D5. Live activity and network health | $3,000 |
| **Other total** | **$45,000** |

#### D1. Orion full-history infrastructure

**Budget: $20,000. Planned delivery: 31 December 2026.**

We kept working on Orion during Q3, but it was not released or counted as a completed commitment.
In Q4, we plan to finish that work and make Orion available as an open-source, storage-efficient
service for Stellar's history. It does not have a public repository yet; publishing the source,
setup instructions, architecture, validation tools, and operating documentation is part of this
deliverable. We will add the repository link to the project page once it is public.

Orion will bring the original archive, intervening ranges, and new ledgers together. We will check
which archive data is available, publish mainnet history from the earliest recoverable ledger to
the synchronized published tip, and finish the account-history indexes and transaction lookups.
These indexes let us find an account or transaction without scanning the whole archive.

XDR will stay the authoritative source. Orion will validate it and publish compact, checksummed
Parquet history. Recent history and current state will move forward together through verified
publications, so readers do not receive a mixture of old and partially published data. We will
also finish gap detection, restart recovery, rollback, and synchronization monitoring. The legacy
importer will be replaced only after the history comparison and recovery checks pass.

We will count Orion as delivered when the complete target interval is published without unresolved
internal gaps, the restart and publication checks pass, and we have recorded at least seven
consecutive days of live synchronization with its lag and recovery behavior. The public coverage
record will show the first and last ledger, source checksums, publication generation, gaps, and
latest synchronized ledger. Missing archive intervals keep the work partial. Testnet and futurenet
will have separate coverage notes, including their resets.

Evidence will include the public repository and release, coverage record, validation and recovery
results, and storage/query measurements with the dataset size, hardware, and workload stated.
Sample storage savings will remain labeled as samples until the whole archive is measured. This
gives StellarChain and other builders a durable history service with less duplicated ingestion
and a clear way to check what is actually available.

Video reference: [StellarChain Full History](https://www.youtube.com/watch?v=yJd3HBujqhg).
This demonstration accompanies the proposal; delivery will be checked against the public release,
coverage record, and validation results described above.

#### D2. Historical API and explorer integration

**Budget: $8,000. Planned delivery: 31 December 2026.**

We will connect Orion to the account, transaction, and ledger pages so users can move through old
history as naturally as recent activity. These pages already exist; the new work is the historical
API and the integration behind them.

The API will provide ledger lookup and its transactions, transaction lookup and its operations and
effects, account state, and account transaction/operation history. We will document the supported
Horizon-compatible reads, any intentional differences, pagination, ordering, errors, XDR access,
and source/coverage information. Account and transaction requests will use Orion's indexes and
stay bounded even when the archive grows.

Recent and archived history will keep the same identifiers and ordering, without duplicate rows
where published ranges meet. Exact amounts, fees, operation results, and XDR will remain available.
If an effect or balance change cannot be reconstructed, we will say so. A page of activity will not
be presented as an account's complete lifetime history.

Before release, we will compare exact chain fields with independent fixtures from at least three
separate historical periods and check the boundaries between publications. We will also check
pagination, busy-account reads, cancellation, timeouts, and fallback/rollback during migration.
Every endpoint in the documented scope must pass these checks, and old transaction lookup, account
history, and ledger navigation must work through the public explorer over Orion's published range.
Incomplete endpoint coverage or recent-only integration remains partial.

Evidence will include public API documentation and example queries, implementation links,
compatibility and pagination results, and repeatable p50/p95 query measurements. Users and external
builders will have one dependable way to read historical data and trace it back to the chain.

#### D3. Clearer and faster explorer pages

**Budget: $8,000. Planned delivery: 31 December 2026.**

We will rebuild the main explorer views around the information people need first. The overview will
bring global identifier search, the selected network, recent ledgers and transactions, and links
into accounts and historical data together in a more compact layout.

Account pages will show balances, asset allocation, trustline and reserve context, and an activity
calendar. Users will be able to move between payments, trading, contract activity, and account
configuration, and inspect balances, issued assets, offers, claimable balances, pools, and account
data where the read sources support them. Portfolio values will say when an asset is excluded
because its price is unavailable, and activity summaries will show their indexed range.

Ledger pages will show close time, transaction and operation counts, successful and failed
transactions, fees, and previous/next navigation. Totals will remain marked as incomplete until
the full requested ledger has been read. Transaction pages will give a clearer summary of success
or failure, fee-bump and fee-source context, memo, operations, exact amounts, and effects or balance
changes where available. JSON, XDR, and full identifiers will stay easy to inspect.

We will reduce unnecessary requests and repeated rendering, load secondary panels when needed,
keep long lists bounded, and cancel outdated reads. The pages will share the existing controls and
work on mobile and desktop, with keyboard navigation, light and dark themes, and stable loading,
empty, partial-data, and error states. An unavailable source will not be shown as zero activity.

We will check the overview, account, ledger, and transaction flows at 390px and 1440px widths, in both
themes and with keyboard-only navigation. For performance, we will compare at least 30 runs per
route against the current explorer using the same browser/device profile, network conditions, and
representative data. Median time to usable primary content must improve for the overview, account,
and transaction pages, while p95 must not get worse. The report will include loading and interaction
timings, request counts, and rendering/long-task observations.

Evidence will include the public pages, implementation links, desktop/mobile recordings, and the
before/after measurements. The result should help newcomers understand what happened faster while
letting experienced users inspect the same exact evidence. A visual refresh alone will not count
as the historical integration or the performance improvement.

#### D4. Historical statistics and analytics

**Budget: $6,000. Planned delivery: 31 December 2026.**

Q3 brought dedicated chart pages for supported metrics. In Q4, we will bring them into a searchable
analytics workspace and extend the verified history behind them. Metrics will be grouped into
network activity, accounts and retention, payments, assets and stablecoins, DEX and liquidity,
market data, fees, and Soroban contracts.

Users will be able to choose recent, one-year, multi-year, or all-history views where the data
supports them, with suitable hourly, daily, weekly, and monthly buckets. Charts will have period
comparisons, interactive tooltips, line or bar views, exact bucket values, related metrics,
shareable URLs, and CSV exports of the selected dataset. Each metric will have a public description
of its source, definition, units, available range, aggregation, and freshness.

The committed historical series are ledgers, transactions, operations, failed transactions, new
accounts, and ledger close time. The archive-derived series will cover their complete validated
Orion source interval, and comparisons will use matching complete windows. We will also add exact
daily, weekly, and monthly active-account counts from account identities, with the source and
direction defined. We will not derive a monthly distinct count by adding or averaging shorter
periods.

Retention cohorts and the asset, DEX, and Soroban series shown in the prototype will be added only
when their data and calculations have been validated. They are additional work, not replacements
for the six core series and three active-account series above. We will not extend a metric into a
period before its source or protocol support existed.

We will count this as delivered when the workspace, metric catalog, and all nine committed series
are public with checked definitions and clear coverage. Core values will be compared with
independent source samples from at least three separate historical periods, and the identity-based
account counts will be checked separately. Exports must match the selected data exactly.

Evidence will include public chart and catalog links, implementation links, definition and coverage
checks, export comparisons, and query measurements for recent and long-range windows. This gives
builders and researchers a useful way to explore Stellar's long-term activity without guessing
what a chart includes. A long-range selector by itself does not prove that the history is complete.

#### D5. Live activity and network health

**Budget: $3,000. Planned delivery: 31 December 2026.**

We will add a clearer view of live activity and the data service behind the explorer. Recent
ledgers, transactions, and operations will come from the synchronized indexed tip, with pause,
reconnect, stale, unavailable, and recovery states. The health view will show Orion's indexed and
published ledger, synchronization lag, verified historical range, active generation, verification
state, and last observation time.

We will also add a searchable validator and organization view with public identifiers, observed
status, software version, host/country information where available from a named source, and
availability history. Daily and 30-day percentages will be shown only when the observation window
supports them. Missing intervals and metadata will stay visible, and any external tier classification
will carry its source and timestamp. Observed reachability will remain separate from evidence of
consensus participation.

Before release, we will check that the public live and health views recover from a controlled
connection interruption without silently dropping activity. Synchronization fields must reflect
real data, and validator status/history must have a named source, timestamps, and a defined
observation window. Mainnet monitoring and other network coverage will be described separately.
We will document the existing public API health endpoint while keeping service availability separate
from historical completeness and chain-current synchronization.

Evidence will include the public live, health, and validator pages, implementation links, source
and measurement documentation, and recovery/freshness checks. Users and operators will have a
clearer way to spot stale data and understand observed network availability without treating it
as a security endorsement.

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellarchain.io&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellarchain.io)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellarchain.io&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellarchain.io)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellarchain.io&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellarchain.io)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellarchain.io&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellarchain.io)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
