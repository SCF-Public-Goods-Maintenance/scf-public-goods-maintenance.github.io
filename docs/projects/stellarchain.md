---
title: "StellarChain"
parent: Public Good Projects
proposal_issue: 60
proposer: devfed1
category: "Infrastructure Monitoring"
budget: "50000"
---

# StellarChain

_Explore the Stellar blockchain - transactions, accounts, contracts, ledgers, and operations._

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
coordination, prioritization, and execution tracking. **Fedot Sereoja, Fullstack Developer:**
responsible for architecture and implementation across frontend and backend, including explorer UX,
API integrations, network data pipelines, and Soroban-related features.

Team experience in the Stellar ecosystem: We have hands-on experience building and operating a public
Stellar explorer that integrates core ecosystem services such as Horizon and Soroban RPC, supports
multiple Stellar networks (mainnet, testnet, futurenet), and delivers
contract/account/asset/transaction transparency features. Our work includes continuous iteration on
usability, mobile-first access, performance, metadata enrichment (including TOML-based asset
context), and reliable public data presentation for independent verification.

## Retroactive Impact

Over the last three months (January-March 2026), Stellarchain delivered a full v4 upgrade that
materially improved public access to Stellar data. We redesigned core explorer experiences (accounts,
transactions, assets, ledgers, markets, contracts), shipped mobile-first interfaces plus PWA support,
and improved accessibility with clearer navigation, search guidance, progressive disclosure, and
better loading/error states. We also expanded ecosystem coverage by integrating Horizon, Soroban RPC,
TOML metadata, CoinGecko and on-chain XLM price, and multi-network support (mainnet, testnet,
futurenet), including deeper Soroban contract visibility (events, storage, transactions, balances,
verification metadata). On the infrastructure side, we improved reliability and usability through
caching, pagination, debounced search, parallel data loading, and cross-network fallback flows that
reduce dead-ends.

## Past Deliverables

1. UX/UI redesign aligned with current Stellar features — Completed We shipped the v4 refresh across
   core explorer surfaces (accounts, transactions, assets, network activity), with broad rollout
   coverage and production releases (including v4.7.0, v4.7.1, v4.7.2 on February 27, 2026 and March
   1, 2026). We have a changelog box in the footer.

2. Mobile-first experience — Completed We implemented dedicated mobile views, touch-first navigation
   patterns, responsive page behavior across major surfaces, plus installable PWA support (manifest +
   service worker).

3. Improved accessibility/usability for non-technical users — Completed We added clearer
   navigation/search guidance, progressive disclosure patterns, skip-to-content, improved
   loading/error states, and clearer labeling/account context flows.

4. Performance and usability improvements — Completed We delivered debounced search, parallelized
   data loading, improved cross-network navigation behavior, pagination enhancements, and backend
   caching/query improvements.

5. Support for current Stellar ecosystem features (including Soroban) — Completed We added Soroban
   RPC integration and delivered contract views/features for transactions, events, storage, balances,
   and verification-oriented metadata handling.

6. Expanded ecosystem integrations — Completed We integrated Horizon, Soroban RPC, Stellarchain API
   v1, TOML metadata enrichment, CoinGecko snapshots, and multi-network support
   (mainnet/testnet/futurenet).

## Proposed Impact

1. **Scam-Flow Investigation and User Safety Context** Improve users’ ability to identify and
   investigate suspicious fund flows, based on recurring feedback from users affected by scams and
   misdirected payments. We aim to deliver clearer risk signals, safer context around destination
   addresses, and practical educational guidance at key decision points.

2. **Enhanced Soroban Contract Transparency** Increase contract-level transparency by improving
   event/log decoding, storage/state visibility, and invocation context. We will strengthen
   verification and provenance signals so users can independently assess contract behavior with
   higher confidence.

3. **Historical Statistics and Charts for Chain Observability** Expand historical visibility through
   richer time-series metrics and chart pages across network activity, usage, assets, contracts, and
   markets. This will support better trend analysis and more data-driven decisions for builders,
   researchers, and ecosystem participants.

4. **Improved Accessibility and Clarity for Non-Technical Users** Reduce usability barriers by
   refining content hierarchy and UX across high-traffic pages, adding more plain-language
   explanations, contextual tooltips, and progressive disclosure to make blockchain data easier to
   understand for non-technical users.

## Proposed Deliverables

1. **Transaction / Payment / Operation Tracing & Safety Layer** Deliverables: trace APIs
   (`/v1/trace/address/{id}`, `/v1/trace/tx/{hash}`) with hop-depth and op-type filters (`payment`,
   `path_payment`, `create_account`, `account_merge`, Soroban transfer-like changes); graph and table
   trace views with aggregated edges (`count`, `amount`, `firstSeen`, `lastSeen`); risk annotations
   based on known labels and behavioral heuristics (informational, not fraud determinations);
   JSON/CSV export. Ecosystem value: faster scam-flow investigation and clearer user safety context.

2. **Enhanced Soroban Contract Transparency Layer** Deliverables: contract endpoints
   (`/v1/contracts/{id}/events`, `/v1/contracts/{id}/transactions`, `/v1/contracts/{id}/storage`,
   `/v1/contracts/{id}/activity`) with ledger-range filters and cursor pagination; improved event/log
   decoding with raw fallback; contract timeline linked to transaction/effects/storage deltas;
   verification metadata (`wasmHash`, `source`, `verificationStatus`, `lastIndexedLedger`). Ecosystem
   value: easier independent verification of contract behavior.

3. **Historical Network Observability (Chart Pages, not Dashboard)** Deliverables: dedicated chart
   pages under `/chart/{slug}` (e.g. `/chart/price`, `/chart/top-payers`, `/chart/transactions`,
   `/chart/contracts`, `/chart/dex-vol-xlm`) backed by
   `GET /v1/network-metrics?metricKey={key}&bucketMinutes={n}&network={mainnet|testnet|futurenet}`.
   Existing metric keys: `price-usd`, `rank`, `market-cap`, `volume-24h`, `circulating-supply`,
   `market-cap-dominance`, `trades`, `dex-vol`, `dex-vol-xlm`, `xlm-total-pay`, `ledgers`, `tps`,
   `ops`, `tx-ledger`, `tx-success`, `tx-failed`, `ops-ledger`, `transactions`, `operations`,
   `avg-ledger-sec`, `accounts`, `assets`, `output-value`, `top-accounts`, `invocations`,
   `contracts`, `fee-charged`, `max-fee`, `active-addresses`, `inactive-addresses`,
   `accounts-created`, `accounts-merged`. Keys to add: `top-payers`, `top-receivers`,
   `top-contract-callers`. Slug alias: `price -> price-usd`. Ecosystem value: gives builders,
   researchers, and public users clear historical visibility without a heavy dashboard surface.

4. **Accessibility and Clarity Improvements** Deliverables: plain-language summaries on core pages,
   contextual tooltips/glossary, improved progressive disclosure, and keyboard/screen-reader QA on
   top user flows. Ecosystem value: lower barrier for non-technical users.

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
