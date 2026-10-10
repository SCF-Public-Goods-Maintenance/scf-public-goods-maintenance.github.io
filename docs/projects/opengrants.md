---
title: "OpenGrants"
canonical_id: daoip-5:scf:project:opengrants
parent: Public Good Projects
proposal_issue: 78
proposer: sam-mccarthy07
category: "Other"
budget: "$20,000"
---

# OpenGrants

<!-- markdownlint-disable MD036 -->

_OpenGrants is open data infrastructure for Web3 grants that maintains the largest cross-ecosystem
funding data set, including all completed SCF rounds._

<!-- markdownlint-enable MD036 -->

|                      |                                                  |
| -------------------- | ------------------------------------------------ |
| **Category**         | Other                                            |
| **Website**          | <https://opengrants.daostar.org/>                |
| **Repository**       | <https://github.com/metagov/opengrants-platform> |
| **Gateway-API**      | <https://github.com/metagov/Grants-Gateway-API>  |
| **First Released**   | September 2025                                   |
| **Intake**           | soft-launch                                      |
| **Budget Requested** | $20,000                                          |

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

Q3 was planned as a return to active development. In practice the quarter went to keeping OpenGrants
running and its SCF data current, so of the planned work only maintenance, PG Atlas support and the
sensor repair were completed within the quarter. As agreed with SCF, the remaining deliverables and
their budget ($10,000) move to Q4. Most of them have since been built; they will be reported for
payment there.

This generated the following impact for the Stellar ecosystem:

- SCF funding data stayed current as rounds closed: SCF #42–#45 were ingested into DAOIP-5
  (141 Build awards, $14.15M), alongside the full history (933 applications, $70.2M).
- The automated SCF ingestion was repaired. The Airtable change sensor was failing on two of its
  three tables, so new SCF data did not trigger the pipeline; it was fixed in August.
- API users can renew and revoke their keys. A user-reported bug blocked key renewal; it was fixed
  and the flow extended with revocation and selectable expiry.
- PG Atlas can read OpenGrants' dependencies: both repositories run the PG Atlas SBOM action.

<!-- markdownlint-enable MD034 -->

---

## Past Deliverables

<!-- markdownlint-disable MD034 -->

### 2026 Q3

| Budget allocation | Reserved | Actual  |
| ----------------- | -------- | ------- |
| Maintenance       |          | $10,000 |
| Other             |          | $0      |

All of the work completed in Q3 was maintenance: hosting and data updates (D5, $5,000), PG Atlas and
dependency support (D6, $2,000), and the sensor repair, a bug fix (D2, $3,000). Reserved stays empty
because the Q3 proposal predates the reserve.

**Carried to Q4: $10,000.** As agreed with SCF, the budget for the deliverables not completed in Q3
is deducted from the second half of the Q3 award ($10,000) and added to the Q4 request, so the two
quarters are accounted for separately:

| Carried deliverable                                 | Amount  |
| --------------------------------------------------- | ------- |
| D1: SCF Intelligence Report                         | $2,000  |
| D2 (remainder): edit detection, failed-run alerting | $1,500  |
| D3: MCP server                                      | $2,500  |
| D4a: Stellar project view                           | $2,000  |
| D4b: About page                                     | $500    |
| D7: PG Award data integration                       | $1,500  |
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
- **Moved to Q4:** re-running the pipeline when existing Airtable records are edited, and alerting
  on failed runs. Edit detection has since been merged
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
- Uptime: OpenGrants and the Gateway API stayed available throughout the quarter, with no outages
  or service complaints from users or downstream projects, including PG Atlas. Uptime records are
  available on request.
- DAOIP-5 compliance: 100% of finished SCF rounds, through SCF #44, are indexed and available in
  DAOIP-5, the same metric as our October 2025 and March 2026 reports. SCF #45 is not counted yet
  because it is still in its notification and award-distribution phase. Its latest data is already
  indexed (last sync on 2026-10-10), and the round will be assessed once distribution is complete.
  Field level: all 14 required fields are backed by source data, with no fabricated values (the
  March `createdAt` issue is fixed):
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

For the next three months, OpenGrants will remain the reliable, up-to-date source of structured
Stellar funding data while making targeted improvements to legibility, automation, and downstream
usability. Alongside zero-downtime hosting and continued 100% DAOIP-5 compliance, Q3 focuses on
reducing manual overhead in data ingestion, improving how Stellar-specific funding data is surfaced,
and exposing OpenGrants data programmatically so agents and downstream tools can consume it directly.

1. **Data-driven SCF governance.** Recurring, per-round Intelligence Reports give delegates and the
   community consistent funding and milestone analytics at decision time, building directly on the
   SCF 41 report that informed community voting.

2. **Lower-friction, more reliable data infrastructure.** Polishing the SCF ingestion pipeline toward
   full automation reduces manual steps and the risk of data gaps, keeping Stellar funding data
   accurate and current using AI agents for automation.

3. **Programmatic access for downstream tooling.** An MCP server exposes the OpenGrants dataset so
   agents, researchers, and dependent projects (including PG Atlas) can query funding data directly,
   strengthening OpenGrants as shared ecosystem infrastructure.

4. **Improved legibility of Stellar funding data.** A dedicated Stellar project view and an About
   page make OpenGrants easier to understand and navigate for community members, delegates, and
   reviewers, directly supporting clearer user signal during evaluation.

5. **Ongoing hosting, maintenance, and continued support for dependent projects.** Ongoing
   operational support for PG Atlas and any new dependencies that build on OpenGrants data.

6. **A source of truth for the Public Goods Award.** Consolidating fragmented PG Award data which is
   currently scattered across SDF Airtables, community-maintained mappings, and Tansu on-chain
   proposals into OpenGrants gives the community its first reliable, comparable record of award
   history, ready to ingest binding on-chain funding decisions once they exist.

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

1. **SCF Intelligence Report.** OpenGrants generates and publishes a funding Intelligence Report to
   the SCF community for the next round (`SCF #45`), which includes the following data: funding
   distribution, category breakdowns, milestone and tranche completion trends, and comparison against
   prior rounds. Builds on the `SCF #41` Intelligence Report that delegates used during community
   voting, turning a one-off contribution into a repeatable governance input.
   - _Ecosystem value: consistent, data-driven context for delegates and the community during the
     decision-making and voting process of every SCF round._

2. **Data integration automation.** Polish and harden the ingestion pipeline toward fully automated
   data ingestion, reducing manual steps (per PG Atlas team feedback).
   - _Ecosystem value: more reliable, always-current Stellar funding data with less operational
     overhead. Setting this base infra enables us to build towards more intelligent data points._

3. **MCP server for OpenGrants.** Ship an MCP server exposing the OpenGrants dataset so agents and
   downstream tools can query funding data directly.
   - _Ecosystem value: makes OpenGrants data programmatically consumable by agents, researchers, and
     dependent projects._

4. **More legible data with greater signal**

   4.a. **Stellar project view.** A dedicated, improved view surfacing SCF funded project's funding
   data for easier navigation. For example: View OpenGrants and its funding history by SCF.
   - _Ecosystem value: clearer, SCF-specific legibility for community members and reviewers._

     4.b. **About page for OpenGrants.** An About page documenting what OpenGrants is, its data
     sources, and how to use the infrastructure.

   - _Ecosystem value: lowers the barrier to understanding and adopting OpenGrants._

5. **Ongoing hosting and maintenance.** Zero-downtime operation of OpenGrants infrastructure and
   continuous SCF funding data updates, maintaining Stellar's 100% DAOIP-5 compliance rate.

   _Ecosystem value: uninterrupted community access to structured funding data that eliminates data
   loss and fragmentation._

6. **PG Atlas and dependency support.** Continued operational support for the PG Atlas team and any
   other new dependencies. _Ecosystem value: sustains downstream projects building on OpenGrants
   data._

7. **PG Award data integration.** Reconstruct and integrate a complete, comparable dataset for the
   SCF Public Goods Award into OpenGrants, consolidating sources that are currently fragmented across
   SDF Airtables, the community-maintained round mappings, and Tansu on-chain proposals. Delivers the
   historical and current rounds as a best-effort dataset, with the pipeline structured to ingest
   binding on-chain funding decisions once they exist (expected 2027).

Ecosystem value: establishes the first reliable source of truth for the Public Goods Award, making
award history legible and comparable alongside SCF grant data.

<!-- markdownlint-enable MD034 -->

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aopengrants&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aopengrants)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aopengrants&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aopengrants)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aopengrants&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aopengrants)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aopengrants&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aopengrants)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
