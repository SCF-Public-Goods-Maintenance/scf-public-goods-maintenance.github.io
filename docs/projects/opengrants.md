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

- SCF #42–#45 were ingested into DAOIP-5 as the rounds closed, keeping all 933 SCF applications
  ($70.2M) current.
- The SCF Airtable sensor was repaired in August, so new SCF data triggers the pipeline again.
- API users can renew and revoke their keys after a user-reported bug was fixed.
- PG Atlas can read OpenGrants' dependencies through the SBOM action in both repositories.

<!-- markdownlint-enable MD034 -->

---

## Past Deliverables

<!-- markdownlint-disable MD034 -->

### 2026 Q3

$10,000 of the Q3 award covers the deliverables completed in Q3. The other $10,000, for the
deliverables not completed within Q3, is carried into the Q4 request as agreed with SCF.

Completed in Q3:

1. **Ongoing hosting and maintenance.** Kept OpenGrants live with no outages and ingested SCF #42–#45
   as the rounds closed. 100% of finished SCF rounds (through SCF #44) are indexed in DAOIP-5; SCF #45
   is still in its notification and award-distribution phase, and its latest data is indexed (last
   sync 2026-10-10). Fixed API key renewal (https://github.com/metagov/Grants-Gateway-API/pull/4).
2. **PG Atlas and dependency support.** Added the PG Atlas SBOM action to both repositories
   (https://github.com/metagov/opengrants-platform/pull/2,
   https://github.com/metagov/Grants-Gateway-API/pull/5).
3. **Data integration automation (partly).** Repaired the SCF Airtable sensor, which had stopped
   triggering the pipeline
   (https://github.com/metagov/opengrants-platform/commit/cf1927c05cc096611ba75186f6530e67f077aba3).

Completed after Q3, carried into Q4:

1. **SCF Intelligence Report.** Covers SCF #42–#45:
   https://github.com/metagov/opengrants-platform/blob/master/docs/reports/scf_42-45_intelligence_report.md
2. **MCP server.** https://github.com/metagov/Grants-Gateway-API/pull/6
3. **Stellar project view and About page.** https://opengrants.daostar.org/system/scf/projects,
   https://opengrants.daostar.org/about

Not completed, moved to Q4:

1. **Data integration automation:** alerting on failed pipeline runs.
2. **PG Award data integration:** not started.

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

Q4 is a maintenance quarter. OpenGrants keeps Stellar's funding data reliable and current, supports PG
Atlas through the next SCF Build round, and completes the Q3 deliverables carried into this quarter.

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

1. **SCF Intelligence Report.** Report for SCF #42–#45.
2. **MCP server.** MCP server for OpenGrants data.
3. **Stellar project view.** A page per SCF-funded project with its funding history.
4. **About page.** What OpenGrants is, its data sources, and how to use it.

To complete in Q4:

1. **Failed-run alerting.** Alerts when an SCF pipeline run fails.
2. **PG Award data integration.** Bring PG Award data into OpenGrants, coordinated with the
   PG Maintenance team.

<!-- markdownlint-enable MD034 -->

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aopengrants&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aopengrants)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aopengrants&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aopengrants)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aopengrants&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aopengrants)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aopengrants&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aopengrants)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
