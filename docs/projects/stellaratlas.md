---
title: "StellarAtlas"
parent: Public Good Projects
proposal_issue: 202
proposer: silence48
category: "Infrastructure Monitoring"
budget: "$38,000"
health_endpoint: "https://api.stellaratlas.io/v1/public-goods/health"
metrics_endpoint: "https://api.stellaratlas.io/v1/public-goods/metrics"
---

# StellarAtlas

<!-- markdownlint-disable MD036 -->

_StellarAtlas provides free, open-source network monitoring, archive verification and repair tooling,
an explorer, and historical data APIs for Stellar operators, developers and researchers._
<!-- markdownlint-enable MD036 -->

|                         |                                                                                                                                                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Category**            | Infrastructure Monitoring                                                                                                                                                                    |
| **Website**             | <https://stellaratlas.io>                                                                                                                                                                    |
| **Repository**          | <https://github.com/Stellar-Atlas/StellarAtlas>                                                                                                                                              |
| **Backend and APIs**    | [Source](https://github.com/Stellar-Atlas/StellarAtlas/tree/main/apps/backend)                                                                                                               |
| **Frontend**            | [Source](https://github.com/Stellar-Atlas/StellarAtlas/tree/main/apps/frontend-v4)                                                                                                           |
| **Documentation**       | [Source](https://github.com/Stellar-Atlas/StellarAtlas/tree/main/docs)                                                                                                                       |
| **Archive scanner**     | [Source](https://github.com/Stellar-Atlas/StellarAtlas/tree/main/apps/history-scanner)                                                                                                       |
| **Data processing**     | [Ledger history](https://github.com/Stellar-Atlas/StellarAtlas/tree/main/apps/full-history-etl) · [Parsed datasets](https://github.com/Stellar-Atlas/StellarAtlas/tree/main/apps/hubble-etl) |
| **First Released**      | April 2025                                                                                                                                                                                   |
| **Intake**              | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/159>                                                                                          |
| **Budget Requested**    | $38,000                                                                                                                                                                                      |
| **Maintenance Reserve** | 20000                                                                                                                                                                                        |
| **Other**               | 18000                                                                                                                                                                                        |

## Project Description

<!-- markdownlint-disable MD034 -->

Forked from Stellarbeat, StellarAtlas combines network monitoring, archive verification, historical
datasets and developer tools in a free, open-source service. Operators can investigate failures and
inconsistent observations, while developers and researchers explore transactions, contract events and
ledger data through our explorer and public APIs.

We prioritize reliable uptime, better parsed datasets and accessible documentation. Our ledger-state
proof research explores how independent watchtowers could publish verifiable observations, helping
applications detect misleading RPC responses and verify private-payment state, including spent
nullifiers and accepted pool roots. A completed prover remains a longer-term goal.

StellarAtlas will remain open source under its existing MIT license, and public data access will
remain free.
<!-- markdownlint-enable MD034 -->

## Team & Experience

<!-- markdownlint-disable MD034 -->

Our experience spans enterprise software development, information security, infrastructure operations
(DevSecOps), user experience and web3 tooling (including Stellar), and business consulting. Previous
stellar focused work includes Stellar Turrets, Hoops Finance, Script3, Transfuse/Ionize, PayShare,
network visualization, and consulting with various teams within the Stellar ecosystem.

| Team member   | GitHub                                        | LinkedIn                                            | Discord      |
| ------------- | --------------------------------------------- | --------------------------------------------------- | ------------ |
| Timothy Baker | [silence48](https://github.com/silence48)     | [Profile](https://www.linkedin.com/in/tim4802/)     | silence4802  |
| Hunter Sides  | [HunterSides](https://github.com/HunterSides) | [Profile](https://www.linkedin.com/in/huntersides/) | hunterionize |

<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->

This is our first full Public Goods Award proposal. Q3 work strengthened archive processing, data
verification, developer documentation and public explorer tools.

### Current public services

| Service                                                                                                | What it provides                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Network and quorum monitoring](https://stellaratlas.io/)                                              | Network graphs, quorum relationships, blocking and splitting sets, observed SCP activity and a [network overview](https://stellaratlas.io/overview). |
| [Validators](https://stellaratlas.io/nodes) and [organizations](https://stellaratlas.io/organizations) | Connectivity, validation observations, software versions, organization details and archive evidence.                                                 |
| [Archive verification and repair](https://stellaratlas.io/archives)                                    | Root inventories, scanned versus verified coverage, file-level findings, checkpoint evidence and checked replacement availability.                   |
| [Explorer](https://stellaratlas.io/explorer)                                                           | Linked account, asset, transaction, ledger, operation, transfer, contract, trade, offer and liquidity-pool records.                                  |
| [Soroban events](https://stellaratlas.io/explorer/contract-events)                                     | Decoded topics and payloads, original records, transaction context and outcomes, distinguishing contract and diagnostic events.                      |
| [Historical REST and GraphQL APIs](https://stellaratlas.io/docs/datasets)                              | Parsed datasets, schemas, filtered queries, aggregations and available coverage intervals.                                                           |
| [Data-lake downloads](https://stellaratlas.io/docs/api/listHistoryDataBatches)                         | Typed Parquet and compressed ledger-close XDR batches, with schemas, record counts and checksums.                                                    |
| [Horizon and Stellar RPC access](https://stellaratlas.io/docs/services)                                | Documented Horizon and RPC compatible API access, with history distinct from the parsed datasets.                                                    |
| [Developer tools](https://stellaratlas.io/docs)                                                        | Searchable references, guides, examples, endpoint testers and an interactive [GraphQL workspace](https://stellaratlas.io/docs/graphql).              |
| [Legacy tools](https://stellaratlas.io/legacy/) and [service status](https://stellaratlas.io/status)   | Historical network snapshots, quorum export, node simulation, network analysis and application-level health reporting.                               |

For a working example, inspect findings and repair availability in the
[archive inventory](https://stellaratlas.io/archives), or follow decoded events to transactions in
this
[contract view](https://stellaratlas.io/explorer/contracts/CA526Y2NQWGWVVQ7RFFPGAZMU66PSYJ3UC2MTVAV4ZU7OM5BOPHDXUSG?min_ledger=64877635&max_ledger=64877698).

StellarAtlas brings network monitoring, archive verification, historical datasets and developer tools
together in a free, open-source public service. Operators can investigate archive failures and
inconsistent observations, while developers can explore transactions, contract events and historical
records through documented APIs. By making both the data and its supporting evidence accessible, we
reduce the work required to investigate network problems and build applications on Stellar. Our
continued focus on uptime, clearer coverage reporting and easier data access strengthens that
foundation for operators, researchers and developers.

Our ongoing ledger-state proof research could extend this value to private payments and applications
that need independently verifiable information. Wallets could check spent-nullifier status, accepted
pool roots and transaction outcomes against authenticated ledger checkpoints, helping detect
fabricated or stale RPC responses while keeping private payment secrets on the user’s device.
Independently operated watchtowers could publish verifiable observations, and anyone with the
required underlying data could generate proofs for others to check. This creates a path toward
verifiable data services, stronger private-payment verification and less dependence on individual
infrastructure providers. Completing the prover remains a longer-term goal; the current work focuses
on investigation, prototypes and validating these capabilities.

### Recorded usage

| Measurement                 |     Recorded activity | Reporting period             |
| --------------------------- | --------------------: | ---------------------------- |
| Requests                    | Approximately 205,700 | September 3–October 11, 2026 |
| Data transferred            | Approximately 1.78 TB | September 3–October 11, 2026 |
| Public API requests         |  Approximately 82,000 | September 3–October 11, 2026 |
| Node-inventory API requests |  Approximately 44,400 | September 3–October 11, 2026 |
| Unique visitor IPs          |   Approximately 5,180 | September 3–October 2, 2026  |

These approximate Cloudflare figures run through October 11. We plan to implement better analytics
tooling this quarter. Unique IPs are the closest analog for unique users. We recently implemented
stronger bot filtering tools such as Turnstile and bot scores on certain requests to attempt to limit
inorganic traffic.
<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

| Date         | Completed work                                                                                                            | Evidence                                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| September 5  | Preserved archive findings through failed refreshes and frontend releases; added unavailable states and regression tests. | [Archive interface recovery](https://github.com/Stellar-Atlas/StellarAtlas/commit/5973adc989f9916ad71a86647bc3fd9e1bd5a448)        |
| September 7  | Updated dependencies and checked affected parser and sandbox behavior.                                                    | [Dependency maintenance](https://github.com/Stellar-Atlas/StellarAtlas/commit/f23145b77512addbe659bb1c0350aea8695189e6)            |
| September 7  | Added known-transaction comparisons across REST and GraphQL.                                                              | [Transaction verification](https://github.com/Stellar-Atlas/StellarAtlas/commit/c14910592b37284d8e04f9678085463d44d534aa)          |
| September 23 | Integrated additional documentation and API example.                                                                      | [Documentation and validator views](https://github.com/Stellar-Atlas/StellarAtlas/commit/b17c559c722202a809bb62518d4cf051b6aa27bb) |
| September 25 | Added the historical contract-event workspace and querying guide WIP.                                                     | [Event workspace](https://github.com/Stellar-Atlas/StellarAtlas/commit/f8dade5bd63816764daf9922e1a6b85dda691570)                   |
| September 25 | Corrected stalled archive scheduling and added processing-state checks and tests for self healing in future.              | [Archive scheduling](https://github.com/Stellar-Atlas/StellarAtlas/commit/c0fda7d3472058a0728aa13468979cfb1a41ac8f)                |

Our internal development priorities have established a new modern interface, historical query
services, archive repair tools, and a plethora of other expanded features. Work still ahead includes
additional independent reporting, frontend continuity, easier dataset reuse, and proof of ledger
state publication and verifier (using ZK proofs). Broader proof work including bls12-381 proofs of
ledger state, graph products, community-scanner, expanded Testnet coverage and full application
failover remain longer-term priorities.
<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

- Provide more development tools such as additional features on transaction finder, clearer explorer
  views and historical reports using our datasets.
- Give operators timely archive alerts and independent reporting on availability, usage, data
  freshness and network observations via email.
- Create a public x.com account for maintenance alerts and public facing comms which should be
  accessible to a broader user-base than just discord users.
- Make our public data easier to reuse through providing more APIs and GraphQL examples, produce
  additional documentation and outline architecture for a builders SDK.
- Improve service uptime and keep the frontend accessible through server restarts.
- Provide a hosted uptime and site status tracker, living in a large cloud service provider (either
  AWS or GCP)
- Continue investigation and development of independently verifiable ledger-state proofs, enabling
  others to generate proofs from the underlying data and verify StellarAtlas’s published
  attestations.

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

Service uptime is our first priority. We will maintain existing services while delivering the
following improvements.

### Frontend caching and continuity

We will use the new nextjs frontend to build the dynamic frontend routes at build time and use ISR to
keep up to date. We will then provide caching rules to ensure the public frontend remains available
through Cloudflare even if a backend service is updating or unavailable by retaining a fallback copy.
The initial release will keep the interface and saved network overview and archive inventory readable
during server restarts, including when the edge cache is empty.

- Each snapshot will show its original observation time and caution about any information that has
  not been retained. New inbound queries will show an unavailable state until the service recovers.
- Service-health checks will run separately from cached page delivery, so a readable frontend cannot
  conceal a failed data service.

### Cloud monitoring, analytics and public status notices

Both reporting pages will be hosted on a cloud service such as AWS or GCP, separately from the main
application, so an application outage does not also take down its reporting pages.

- **Analytics page:** we will self-host Plausible and report browser actions and API events, starting
  with documentation use, archive inspection and successful event queries.
- **Status and uptime page:** we will monitor public services from outside the application, including
  a small query with a known result. We will publish each check's purpose, interval and freshness
  threshold, with response validity, data timestamps, availability history and monitoring gaps shown
  separately. We will maintain historical records as well.
- **Public automated Twitter/X account:** we will connect cloud monitoring to notices for confirmed
  StellarAtlas outages and recoveries, with timestamps and status-page links. We will create official
  socials and publish alerts on x.com as well.
- **Operational anomaly notices:** we will begin with sustained data-freshness or ledger-progression
  delays against published thresholds, testing the rules before enabling automatic posts.
- Analytics collection will run separately from API response handling and will exclude request
  payloads and wallet addresses.

### Parsed Datasets, datalake and explorer

We will continue building upon our parsed ClickHouse datasets to provide practical tools for
exploring Stellar activity.

- **Transaction finder:** provide account and asset searches that open related transactions and
  ledgers, offers, swaps, contracts and other data, preserving filters, ledger ranges and the results
  page when users return (share links).
- **Explorer views:** improve the links between existing wallet/account, asset, transaction and
  ledger pages. Add additional dynamic routes to provide better link sharing and data access.
- **Soroban events:** add additional Mainnet topic filtering, with examples covering pagination and
  event classification.
- **Contract Source Verification:** Provide tooling for builders to verify their contract source
  code, and expose this information on the frontend.
- **GraphQL examples:** publish reusable queries for account and asset investigations.
- **Data-lake access:** maintain the catalogue, batch listings and downloads, and better document
  availability.

### Builders SDK plan

We want developers to build with our data without having to assemble every GraphQL request and
pagination loop themselves. In Q4, we will publish an SDK design and implementation plan, with
TypeScript, rust, and go as the proposed first targets. The plan will cover:

- Typed query interfaces for account, asset and transaction workflows, using the examples above.
- Pagination, coverage and freshness, large identifiers and amount precision, errors/retries and
  schema-version compatibility.
- An API sketch, initial test cases and implementation milestones for the SDK.
- Documented data requirements and validation criteria for future multihop swap pathfinding,
  including current offers and pool state, asset identities, fees and precision. We will distinguish
  native Stellar markets from Soroban exchanges and assess how Atlas data could complement existing
  path-discovery services.

We will complete the design, examples and development plan this quarter. A released SDK are
longer-term goals, targeting H1 27.

### Ledger-state proof research

We will continue investigating and developing a BLS12-381-based ledger-state prover, building on our
existing state-import integrity checks and canonical archive evidence. The goal is to support
independently operated watchtowers and verifiable access to Stellar ledger state.

- **Independent proof generation:** explore how anyone with the required underlying data can
  construct proofs of specific ledger-state claims, bound to authenticated Stellar checkpoints, that
  others can independently verify.
- **StellarAtlas attestations:** investigate authenticated publication of our proofs, identifying
  StellarAtlas as the publisher and linking each result to its ledger, checkpoint and supporting
  evidence.
- **On-chain verification:** prototype verification approaches and assess their execution costs and
  practical limits, including potential use in private-payment state checks.
- **Proof-generation performance:** investigate whether selected proofs can be produced within five
  seconds of ledger close, accounting for data availability, witness preparation and proving time.
  Record performance, resource requirements and remaining challenges.

This is ongoing research and development. The five-second window is a performance target to evaluate;
a completed prover and operational watchtower system remain longer-term goals.

### Reporting page for comparing our results to Radar

We will publish a comparison page covering:

- Any discrepancy and how our system investigated such and what if any actions were required.
- Shared node and network observations supported by both sources.
- The source and observation time of each result.

### Archive-root email subscriptions

We will extend the existing subscription and archive-notification code for validator operators.

- Operators will be able to opt in to alerts for their archive roots.
- Notifications will identify the affected root and link to the supporting evidence.
- Repeated notices for an unchanged failure will be suppressed, and each email will include an
  unsubscribe link.
- We will test the complete flow with a controlled failure example before enabling subscriptions.

### Power protection, storage and recovery

Power outages are common and can interrupt public access, data processing and archive verification.
Our infrastructure is self hosted in two locations however, reliable battery backup helps keep
services available through short interruptions and allows an orderly shutdown during longer outages,
reducing abrupt stops and the recovery work that follows.

- **Replacement power protection:** replace two UPS units, targeting at least 30 minutes of continued
  operation plus time for switchover to standby generators, or an orderly shutdown for longer
  outages. We will validate the runtime under representative load.
- **Storage:** add two additional 4 TB NVMe disks to support the public data services, specifically
  faster indexing and access to certain faceted search tools.

### Delivery period and reporting

We aim to complete these Q4 deliverables by December 31 while maintaining our existing services
throughout the quarter. We will launch external monitoring first to begin collecting observations,
followed by frontend continuity and the transaction and asset-analysis workflows. Analytics, Radar
comparisons and operator subscriptions will build on our existing reporting and notification tools.
We will also publish the builders SDK plan through our github.

Each release will include a working example and relevant checks. Updates will link completed work and
identify remaining issues; the quarter-end report will summarize results and next priorities. Uptime
reporting will be included.

### Quarterly budget

| Award category      | Amount (USD) |
| ------------------- | -----------: |
| Maintenance Reserve |      $20,000 |
| Other               |      $18,000 |
| **Total**           |  **$38,000** |

**Maintenance Reserve — $20,000:** funds engineering and operational capacity for existing public
services: protocol and dependency updates, security and correctness fixes, incidents, recovery,
releases, testing, documentation and developer support. This includes operational costs, and
unscheduled maintenance throughout Q4.

**Other — $18,000:** funds the additions described above and their service costs.

| Item                                                                                                                                                               | Quantity | Estimated unit amount |  Allocation |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------: | --------------------: | ----------: |
| Parsed-data and explorer additions, frontend continuity, SDK planning, analytics and reporting integrations, including testing, documentation and Q4 service costs |       Q4 |                     — |     $10,000 |
| Replacement UPS units for the 30-minute continuity target                                                                                                          |        2 |                $3,000 |      $6,000 |
| Additional 4 TB NVMe disks                                                                                                                                         |        2 |                 $1000 |      $2,000 |
| **Other total**                                                                                                                                                    |          |                       | **$18,000** |

<!-- markdownlint-enable MD034 -->

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellaratlas&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellaratlas)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellaratlas&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellaratlas)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellaratlas&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellaratlas)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellaratlas&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellaratlas)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
