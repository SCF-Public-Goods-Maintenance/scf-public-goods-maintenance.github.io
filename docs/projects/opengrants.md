---
title: "OpenGrants"
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
|                      | <https://github.com/metagov/Grants-Gateway-API>  | 
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

During the Q2 grant period, OpenGrants delivered on its maintenance mandate. We kept infrastructure
live with zero downtime and ingested new SCF round data as it landed, maintaining the datasets and
integrations built in prior quarters. This was a maintenance grant, and the work reflects that scope.

This generated the following impact for the Stellar ecosystem:

- OpenGrants infrastructure remained available with zero downtime as the upstream data source PG
  Atlas continues to build its dependency graph on.
- OpenGrants maintained Stellar's 100% DAOIP-5 compliance rate throughout the period, including
  ingestion of SCF #43 data as it became available.
- OpenGrants maintained its expanded ecosystem funding datasets, including the ENS integration
  supporting cross-ecosystem comparative analysis.

<!-- markdownlint-enable MD034 -->

---

## Past Deliverables

<!-- markdownlint-disable MD034 -->

1. **Ongoing hosting and maintenance — Completed.** Maintained OpenGrants infrastructure with zero
   downtime and ingested SCF #43 funding data during the Q2 period, keeping Stellar in full DAOIP-5
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
   the SCF community for the next round (SCF #45), which includes the following data: funding
   distribution, category breakdowns, milestone and tranche completion trends, and comparison against
   prior rounds. Builds on the SCF #41 Intelligence Report that delegates used during community
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

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
