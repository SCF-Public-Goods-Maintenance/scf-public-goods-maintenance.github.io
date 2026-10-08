---
title: "StellarChain"
canonical_id: daoip-5:scf:project:stellarchain.io
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

During Q3 2026 (July-September), with final integration and QA continuing just after the quarter
closed, we took StellarChain beyond the core explorer experience. We added an Account Trust Checker
and a more advanced investigation flow for indexed classic payment activity. Users can search by
account or transaction, follow bounded candidate paths, filter by asset, date, or ledger, review
grouped payments and timelines, keep a local case queue, and export the current page as JSON, CSV, or
HTML. We present this information as evidence, not as a fraud verdict, and we show the coverage
limits whenever the available history may be incomplete.

Statistics also received a major rebuild. The explorer now has dedicated metric pages, selectable
time ranges and bucket sizes, clearer tooltips, keyboard and pointer navigation, older-history
loading, and CSV exports that keep the exact source values. On the backend, we added safer
forwardfill and repair tools, bounded metric windows, pagination metadata, and read models that avoid
scanning the largest statistics tables without limits. Where the available data is not reliable
enough for a metric, we leave it disabled instead of guessing from unrelated aggregates.

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
counted as a completed deliverable. Full-history integration, account-history publication, end-to-end
API validation, and complete Horizon compatibility will continue through Q4 and future funding work.

We also released StellarKey publicly: an open-source, self-custodial Stellar wallet with Merchant
Mode and our own Private Payments implementation. The wallet and merchant tools are available now.
Private Payments Protocol V2 remains an unaudited, Testnet-only preview and must not be used with
real funds. StellarKey is part of the wider ecosystem we are building around StellarChain, not a
replacement for any of the Q3 commitments below.

## Past Deliverables

### 2026 Q3

> **A note on scope:** The list below covers what we formally committed to for Q3, but it is only one
> part of the wider ecosystem we are building. In parallel, we are working on full-history data,
> synchronized APIs, the explorer, contract intelligence, a self-custodial wallet, merchant tools,
> and privacy research. We count work as completed only when it is released and can be checked. The
> larger projects that are still in progress are listed separately and clearly marked.

1. **Investigator for accounts, transactions, and payment activity — Delivered for the data we have
   indexed**

   We shipped two ways to use the Investigator. Basic mode gives newcomers a simpler Account Trust
   Checker, while Advanced mode adds account and transaction search, one-hop evidence, bounded
   two-hop candidate paths, and filters for operation, asset, date, ledger, direction, and small
   amounts. Results can be viewed as grouped flows or individual events, explored on a payment map
   and timeline, saved in a local case queue, paged through, and exported as JSON, CSV, or HTML.

   The API always shows its coverage and any truncation. Asset-first search is still switched off
   until the additional index is installed and populated. We also do not describe contract activity
   as funds flow until caller and transfer provenance can be shown properly.

   Evidence:
   [frontend investigation and reporting](https://github.com/stellarchain/v4/commit/5795502),
   [case queue and chart/investigator integration](https://github.com/stellarchain/v4/commit/45601e3),
   [paginated trace API](https://github.com/stellarchain/v4-api/commit/deb5e02), and
   [bounded depth and asset-side read models](https://github.com/stellarchain/v4-api/commit/f96e7e8).

2. **Affiliate and partner layer — Partially delivered**

   We added one optional Coinzilla native-ad placement on the homepage. It has a visible
   `Advertisement` label, a short explanation, configuration checks, optional-cookie consent, and
   failure isolation. There is also a development preview that never contacts Coinzilla.

   The ad stays away from Account Trust Checker, investigation evidence, rankings, verification, and
   contract provenance. It will not show live ads until Coinzilla approves the site and provides a
   valid zone ID. Partner pages, the partner catalog and admin tools, regional notes, and click
   analytics are still to come.

   Evidence: `src/components/ads/CoinzillaNativeAd.tsx`, `src/lib/ads/coinzilla.ts`, and the
   sponsored placement rules in `UX-CONTRACT.md`.

3. **Contract intelligence, SAC balances, and verification — Delivered for current coverage; deeper
   verification continues**

   We expanded contract indexing and explorer pages for transactions, events, storage, argument
   usage, balances, and holder balances. We also improved SAC event parsing and metadata, added RPC
   fallback, and made SAC supply comparison available alongside separately calculated classic asset
   supply.

   The labels are now more honest about what each signal means: SAC, custom Wasm, source available,
   decompiled source, legacy verification, and SEP-55 provenance are kept separate. Decompiled code
   is not presented as a verified build. SEP-58 reproducible builds, complete contract coverage, and
   reliable contract-caller or token-transfer attribution remain gated until we can prove them.

   Evidence:
   [SAC reconciliation and holder views](https://github.com/stellarchain/v4/commit/39dc828),
   [contract metrics and balance indexing](https://github.com/stellarchain/v4-api/commit/fb9e73a),
   [SEP-55 verification hardening](https://github.com/stellarchain/v4-api/commit/fc2b6da), and
   [contract RPC fallback](https://github.com/stellarchain/v4-api/commit/6b5d66f).

4. **Historical charts and public API reliability — Delivered for supported metrics**

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

5. **Orion full-history infrastructure — In progress and not released yet**

   While building the historical data layer, we reached a point where adding more code to the old
   import paths would have solved the immediate problem but created more duplication and maintenance
   work. We decided to take the stronger long-term route and build Orion instead. We regularly
   reassess the path as we learn from the data, and in this case a larger but more durable solution
   made more sense than finishing something we would soon need to replace.

   Orion is designed to become a fast, storage-efficient, Horizon-compatible service for Stellar's
   full history. It will import historical data, keep up with new ledgers, provide the REST reads
   StellarChain needs. StellarChain will use Orion's compact model instead of keeping unnecessary
   copies of the same data.

   The basic approach is straightforward:
   - XDR stays the authoritative source and is stored separately from processed history.
   - Orion validates the XDR and writes compact Parquet history, while small indexes make it possible
     to locate transactions and account activity without scanning the whole archive.
   - Recent history and current state move forward together through verified publications.
   - Checksums, isolated staging, and retained generations protect readers during updates.
   - Tests compare exact results and resource use with the existing baseline.

   Progress snapshot as of 3 October 2026:
   - The native account-index evidence loader is implemented. All 87 uncached, race-enabled test
     executions passed, but it has not been deployed yet.
   - Live sync and the API reached ledger 64,610,303. The active publication batch was 87.5%
     complete, with roughly 20 minutes remaining at the time of the snapshot.
   - The account forest was 43.75% emitted, with roughly six hours of emission left before
     verification and publication.
   - Overall acceptance remains at 25%: one of four equally weighted stages is complete. The full ETA
     is not confirmed, and gap-account integration is still open.

   Sample measurements show about 52.56% less storage for the processed cluster, but this does not
   prove the same reduction across the full archive. We still need to publish the account-history
   indexes, join the original, intervening, and live ranges correctly, integrate gap accounts, and
   validate the API end to end. Orion is finished only when it is usable and continuously
   synchronized—not simply when an import completes or a sample test passes. It is listed here as
   extra Q3 progress, not as a completed Q3 commitment.

   [https://www.youtube.com/watch?v=yJd3HBujqhg](https://www.youtube.com/watch?v=yJd3HBujqhg)

6. **StellarKey wallet, merchant tools, and Private Payments — Public release; privacy protocol
   remains Testnet-only** [https://stellarkey.io/](https://stellarkey.io/)

   We released StellarKey publicly as an open-source, self-custodial Stellar wallet. Users keep
   control of their keys and encrypted records. The wallet supports sending, receiving, Stellar DEX
   swaps, batch payments, encrypted vaults, and backups. Merchant Mode adds QR checkout, inventory,
   invoices, refunds, reconciliation, and sales reports without making StellarKey a custodial payment
   processor.

   Private Payments is the research-heavy part of the same application. Protocol V2 generates
   zero-knowledge proofs in the browser and is designed to shield the asset, amount, recipient, and
   memo of internal XLM or USDC transfers. Deposits, withdrawals, the submitting account, fee payer,
   timing, proof, commitments, nullifiers, and ciphertext remain public where applicable. Privacy is
   context, not a guarantee, and activity patterns or reuse can weaken it.

   Protocol V2 is unaudited and Testnet-only, so it must not be used with real funds. Mainnet remains
   gated on an independent security review and the required trusted-setup evidence. Dedicated desktop
   and mobile apps and browser extensions are also on the roadmap.

   Evidence: [StellarKey public application](https://stellarkey.io),
   [open-source repository](https://github.com/stellarchain/io.stellarkey),
   [Private Payments whitepaper](https://github.com/stellarchain/io.stellarkey/blob/main/docs/whitepaper/private-payments.pdf),
   and [video demonstration](https://youtu.be/R5xJyHOJ2Uo).

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
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellarchain.io&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellarchain.io)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellarchain.io&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellarchain.io)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
