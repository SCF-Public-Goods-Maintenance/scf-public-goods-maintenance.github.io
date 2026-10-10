---
title: "OpenGrants"
canonical_id: daoip-5:scf:project:opengrants
parent: Public Good Projects
proposal_issue: 78
proposer: sam-mccarthy07
category: "Other"
budget: "$15,000"
---

# OpenGrants

<!-- markdownlint-disable MD036 -->

_OpenGrants is open data infrastructure for Web3 grants that maintains the largest cross-ecosystem
funding data set, including all completed SCF rounds._

<!-- markdownlint-enable MD036 -->

|                         |                                                  |
| ----------------------- | ------------------------------------------------ |
| **Category**            | Other                                            |
| **Website**             | <https://opengrants.daostar.org/>                |
| **Repository**          | <https://github.com/metagov/opengrants-platform> |
| **Gateway-API**         | <https://github.com/metagov/Grants-Gateway-API>  |
| **First Released**      | September 2025                                   |
| **Intake**              | soft-launch                                      |
| **Budget Requested**    | $15,000                                          |
| **Maintenance Reserve** | $5,000                                           |
| **Other**               | $10,000                                          |

## Project Description

<!-- markdownlint-disable MD034 -->

Even though billions in Web3 grant capital have been distributed, many ecosystems still struggle to
measure performance and prevent waste. We’ve built OpenGrants as the best publicly-available data
source for Web3 grants to allow projects to learn from each other, create a more vibrant space for
builders, and promote ecosystem-wide growth.

We believe the development of standards and benchmarks, and promotion of data-driven decision-making,
is necessary to support the maturation and growth of Web3 grants and DAO resource allocation
mechanisms. Through OpenGrants, we seek to address problems with data collection, quality, and
analysis, community transparency and engagement, as well as the efficiency and interoperability of
grant systems. Ultimately, OpenGrants will help promote the continuous improvement of Web3 grant
programs and the evolution of the Stellar ecosystem.

<!-- markdownlint-enable MD034 -->

## Team & Experience

<!-- markdownlint-disable MD034 -->

Sam McCarthy (Ecosystem Growth Lead, DAOstar) - discord: samccarthy27, twitter: @samccarthy27,
linkedin: https://www.linkedin.com/in/sam-mccarthy-45488372/

Rashmi (Technical Lead, DAOstar) - github: https://github.com/Rashmi-278, discord: torchablazed,
twitter: @rashmivabbigeri, linkedin: https://www.linkedin.com/in/rashmi-v-abbigeri/

We've worked with the Stellar ecosystem since before the inception of OpenGrants, collaborating on
the underlying infrastructure and data standard, DAOIP-5. We have previously received three public
goods awards from Stellar, taking the DAOIP-5 standard and transforming it into open data
infrastructure featuring a gateway API, ecosystem funding dashboard, and SCF grant reporting.

<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->

During Q3, OpenGrants kept its infrastructure live and its SCF data current, repaired the automated
ingestion, and supported PG Atlas. The remaining build work was completed in early October and, as
agreed with SCF, is carried into Q4 with its budget.

This generated the following impact for the Stellar ecosystem:

- `SCF #42`–`SCF #45` were ingested into DAOIP-5 as the rounds closed, keeping all 933 SCF
  applications ($70.2M) current.
- The SCF Airtable sensor was repaired in August, so new SCF data triggers the pipeline again.
- API users can renew and revoke their keys after a user-reported bug was fixed.
- PG Atlas can read OpenGrants' dependencies through the SBOM action in both repositories.

<!-- markdownlint-enable MD034 -->

---

## Past Deliverables

<!-- markdownlint-disable MD034 -->

### 2026 Q3

| Budget allocation | Reserved |  Actual |
| ----------------- | -------- | ------: |
| Maintenance       |          | $10,000 |
| Other             |          |      $0 |

All of the work completed in Q3 was maintenance: hosting and data updates (D5, $5,000), PG Atlas and
dependency support (D6, $2,000), and the sensor repair, a bug fix (D2, $3,000). Reserved stays empty
because the Q3 proposal predates the reserve.

**Carried to Q4: $10,000.** As agreed with SCF, the budget for the deliverables not completed in Q3
is deducted from the second half of the Q3 award ($10,000) and added to the Q4 request, so the two
quarters are accounted for separately:

| Carried deliverable                                 |  Amount |
| --------------------------------------------------- | ------: |
| D1: SCF Intelligence Report                         |  $2,000 |
| D2 (remainder): edit detection, failed-run alerting |  $1,500 |
| D3: MCP server                                      |  $2,500 |
| D4a: Stellar project view                           |  $2,000 |
| D4b: About page                                     |    $500 |
| D7: PG Award data integration                       |  $1,500 |
| **Total**                                           | $10,000 |

#### ⏭️ D1: SCF Intelligence Report — not completed in Q3, moved to Q4 ($2,000)

Committed: an Intelligence Report for `SCF #45` covering funding distribution, category breakdowns,
milestone and tranche completion trends, and comparison against prior rounds.

Not completed within Q3. It has since been completed (2026-10-09), covering all four rounds since the
`SCF #41` report (#42–#45), and will be reported in Q4:
https://github.com/metagov/opengrants-platform/blob/master/docs/reports/scf_42-45_intelligence_report.md

#### 🟡 D2: Data integration automation — partially completed; remainder moved to Q4 ($1,500)

Committed: polish and harden the ingestion pipeline toward fully automated ingestion, reducing manual
steps.

- **Completed in Q3:** the SCF Airtable sensor requested a field that does not exist on two of the
  three tables, so Airtable rejected the request and the sensor never fired. Fixed with per-table
  fields, plus regression tests (2026-08-06):
  https://github.com/metagov/opengrants-platform/commit/cf1927c05cc096611ba75186f6530e67f077aba3
- **Moved to Q4:** re-running the pipeline when existing Airtable records are edited, and alerting on
  failed runs. Edit detection has since been merged
  (https://github.com/metagov/opengrants-platform/pull/3); alerting is not started.

#### ⏭️ D3: MCP server for OpenGrants — not completed in Q3, moved to Q4 ($2,500)

Committed: an MCP server exposing the OpenGrants dataset so agents and downstream tools can query
funding data directly.

Not completed within Q3. It has since been built (generated from an OpenAPI spec of the Gateway API,
merged 2026-10-10: https://github.com/metagov/Grants-Gateway-API/pull/6) and will be reported in Q4
once its hosted endpoint is live.

#### ⏭️ D4a: Stellar project view — not completed in Q3, moved to Q4 ($2,000)

Committed: a dedicated view surfacing each SCF-funded project's funding data, e.g. a project and its
funding history by SCF.

Not completed within Q3. It has since been built (merged 2026-10-10:
https://github.com/metagov/opengrants-platform/pull/3) and will be reported in Q4. PG Maintenance has
asked for these pages as link targets for PG intakes and proposals (#143).

#### ⏭️ D4b: About page — not completed in Q3, moved to Q4 ($500)

Committed: an About page documenting what OpenGrants is, its data sources, and how to use the
infrastructure.

Not completed within Q3. It has since been built (merged 2026-10-10:
https://github.com/metagov/opengrants-platform/pull/3) and will be reported in Q4.

#### ✅ D5: Ongoing hosting and maintenance — completed ($5,000)

Committed: zero-downtime operation and continuous SCF funding data updates, maintaining Stellar's
100% DAOIP-5 compliance rate.

- SCF data kept current: #42–#45 ingested as rounds closed. The datalake holds 933 SCF applications
  ($70.2M), with silver and gold reconciling (report, Data quality section).
- API key renewal fixed for a user who could not renew, plus revocation and selectable expiry (issue
  https://github.com/metagov/Grants-Gateway-API/issues/3, fixed in
  https://github.com/metagov/Grants-Gateway-API/pull/4, merged 2026-08-05).
- SCF sensor repair (see D2).
- Uptime: OpenGrants and the Gateway API stayed available throughout the quarter, with no outages or
  service complaints from users or downstream projects, including PG Atlas. Uptime records are
  available on request.
- DAOIP-5 compliance: 100% of finished SCF rounds, through SCF #44, are indexed and available in
  DAOIP-5, the same metric as our October 2025 and March 2026 reports. SCF #45 is not counted yet
  because it is still in its notification and award-distribution phase. Its latest data is already
  indexed (last sync on 2026-10-10), and the round will be assessed once distribution is complete.
  Field level: all 14 required fields are backed by source data, with no fabricated values (the March
  `createdAt` issue is fixed):
  https://github.com/metagov/opengrants-platform/blob/master/docs/compliance/daoip5_scf_compliance_report_2026-10-10.md

#### ✅ D6: PG Atlas and dependency support — completed ($2,000)

Committed: continued operational support for PG Atlas and any new dependencies.

- Added the PG Atlas SBOM action to both repositories so PG Atlas can read OpenGrants' dependency
  graph (2026-07-22): https://github.com/metagov/opengrants-platform/pull/2,
  https://github.com/metagov/Grants-Gateway-API/pull/5
- Raised the DAOIP-5 ID stability issue affecting PG Atlas, the project pages and OpenGrants on #143,
  and investigated it (after the quarter):
  https://github.com/metagov/opengrants-platform/blob/master/docs/data-quality/scf_canonical_id_data_loss_report_2026-10-09.md

#### ⏭️ D7: PG Award data integration — not started, moved to Q4 ($1,500)

Not started in Q3; the scoping issue promised in the Q3 review was not opened. It depends on stable
DAOIP-5 IDs (#143), which come first in Q4.

#### Data quality notes

**Paid vs awarded (checked 2026-10-10).** OpenGrants mirrors SDF's Airtable, and a check of
production against the Airtable export found identical figures. Of the 933 SCF applications, some
record more paid than awarded:

- **XLM exchange-rate allowance.** SCF pays in XLM, and each payout's USD value is fixed on the
  payment date, so USD paid can land slightly above the USD award. OpenGrants ignores gaps of up to
  2.5% for this reason. 8 awards fall in this range ($11,301 in total) and are not flagged.
- **Award amount not recorded.** 26 legacy awards (SCF #2–#9) have payments but no award amount in
  the source ($872,887 paid). They are shown as "award amount not recorded" rather than as
  overpayments.
- **Flagged for SDF review.** 11 awards record more paid than awarded beyond the allowance ($445,103
  over), 6 of which look like a payment recorded twice. Their project pages show "Paid exceeds award
  in source data", and we have asked SDF to check the payment records.

The allowance and the "award amount not recorded" label were added on 2026-10-10
(https://github.com/metagov/opengrants-platform/pull/3). Full list:
https://github.com/metagov/opengrants-platform/blob/master/docs/data-quality/scf_paid_over_award_2026-10-10.md

### 2026 Q2

1. **Ongoing hosting and maintenance — Completed.** Maintained OpenGrants infrastructure with zero
   downtime and ingested `SCF #43` funding data during the Q2 period, keeping Stellar in full DAOIP-5
   compliance. The real-time SCF integration and Airtable pipeline shipped prior to the Q2 grant and
   were maintained, not newly built, during this period.

1. **Operational support for PG Atlas — Completed.** OpenGrants remained available and responsive as
   PG Atlas's upstream data source throughout the period. No new integration work was requested
   during the Q2 window.

<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

Q4 is a maintenance quarter. OpenGrants keeps Stellar's funding data reliable and current, supports
PG Atlas through the next SCF Build round, and completes the Q3 deliverables carried into this
quarter.

1. **Reliable SCF data.** PG Atlas relies on OpenGrants for newly awarded SCF projects and status
   changes, and another SCF Build round is expected this quarter.

2. **Stable DAOIP-5 IDs.** Avoiding duplicate DAOIP-5 URIs keeps the links used by SCF project pages,
   PG Atlas and API users working (#143).

3. **The Q3 work, delivered.** The Intelligence Report, MCP server, Stellar project view, About page
   and failed-run alerting.

4. **PG Award data in OpenGrants.** Coordinated with the PG Maintenance team.

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

### Maintenance reserve ($5,000)

1. **Hosting and data updates.** Keep OpenGrants and the Gateway API running, ingest the next SCF
   Build round, and keep SCF at 100% DAOIP-5 compliance.

2. **PG Atlas and dependency support.** Newly awarded projects, status changes, and data requests.

3. **DAOIP-5 ID stability.** Follow up the duplicate DAOIP-5 URI thread (#143).

### Other ($10,000, carried over from Q3)

Already completed:

1. **SCF Intelligence Report.** Report for `SCF #42`–`SCF #45`.
2. **MCP server.** MCP server for OpenGrants data.
3. **Stellar project view.** A page per SCF-funded project with its funding history.
4. **About page.** What OpenGrants is, its data sources, and how to use it.

To complete in Q4:

1. **Failed-run alerting.** Alerts when an SCF pipeline run fails.
2. **PG Award data integration.** Bring PG Award data into OpenGrants, coordinated with the PG
   Maintenance team.

<!-- markdownlint-enable MD034 -->

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aopengrants&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aopengrants)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aopengrants&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aopengrants)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aopengrants&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aopengrants)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aopengrants&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aopengrants)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
