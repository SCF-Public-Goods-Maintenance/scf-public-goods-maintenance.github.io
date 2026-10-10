---
title: "PG Atlas"
parent: Public Good Projects
proposal_issue: 197
proposer: aolieman
category: "Ecosystem Visibility"
budget: "$37,000"
health_endpoint: https://api.pgatlas.xyz/health
metrics_endpoint: https://api.pgatlas.xyz/analytics/task-queue
---

# PG Atlas

<!-- markdownlint-disable MD036 -->

_An open data platform for the Stellar software ecosystem that provides transparency into ecosystem
health, project criticality, adoption signals, and contributor activity — helping voters,
maintainers, and builders make data-driven decisions._

<!-- markdownlint-enable MD036 -->

|                         |                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------- |
| **Category**            | Ecosystem Visibility                                                                                |
| **Website**             | <https://pgatlas.xyz>                                                                               |
| **Repository**          | <https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-backend>                                  |
| **SBOM Action**         | <https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-sbom-action>                              |
| **TS Data SDK**         | <https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-ts-sdk>                                   |
| **Frontend**            | <https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-frontend>                                 |
| **First Released**      | April 2026                                                                                          |
| **Intake**              | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/140> |
| **Budget Requested**    | $37,000                                                                                             |
| **Maintenance Reserve** | $16,000                                                                                             |
| **Other**               | $21,000                                                                                             |

## Project Description

PG Atlas is an open data platform and metrics service for understanding the Stellar software
ecosystem. Our primary aim is to show how Stellar-specific public goods are embedded in the broader
ecosystem, consisting of projects, people, and the software that they build.

It combines verified Software Bill of Materials (SBOM) submissions, public package-registry and
OpenGrants data, and Git contributor history into a dependency graph. The system computes transparent
signals for transitive criticality, contributor concentration risk (pony factor), and off-chain
adoption, then publishes them through a public REST API and dashboard. Maintainers and community
members can inspect project details, dependencies, contributors, score breakdowns, and interactive
subgraphs. The data also provides structured context for SCF Public Goods Award review and
Tansu-based governance.

A high-level explanation of how it works is in our [architecture documentation][architecture].

[architecture]: https://scf-public-goods-maintenance.github.io/pg-atlas/

## Team & Experience

**Alex Olieman**, based in the Netherlands

- Role: Project maintainer
- GitHub: @aolieman
- Discord: convergence
- LinkedIn: <https://www.linkedin.com/in/alexolieman/>

Academically trained as a data scientist. I've worked as an NLP researcher at the University of
Amsterdam and as an R&D engineer at a SaaS company. During that time I contributed to numerous
open-source tools, maintained a tiny language model, and supported the DBpedia ecosystem. My
participation in SCF goes back to when it was still a competition. I've launched Stellarcarbon and PG
Atlas with the help of Build awards, and made small contributions to other ecosystem projects.

**Lawal Babatunde**, based in Nigeria

- Role: Co-maintainer of the frontend, SDK, and API
- GitHub: @Utilitycoder
- Discord: utility6151
- LinkedIn: <https://www.linkedin.com/in/lawalbabatunde/>

Lawal is comfortable working in several blockchain ecosystems. His SCF journey started as an engineer
on the Give Credit project, and he stuck around as an active community member. Lawal cofounded
Fundable Finance which also received a Build Award. Proud survivor of a Drips Wave with a height of
hundreds of commits.

**Jay Gutierrez**, PhD, is a computational systems scientist who contributed large parts of the
metrics engine. He will be brought on as needed, for the work where his expertise makes a difference.

**Christian Rogobete** (Soneso) has contributed several big features to PG Atlas. He has done so
voluntarily and without compensation. We'll refer to Christian's work in our deliverables.

## Retroactive Impact

PG Atlas is operational and has supported the SCF Public Goods Award process since Q2. In the Q3
round, we added headline metrics to all proposals as dynamic badges. The criticality score is missing
from the row of badges, because of systematic coverage gaps that we address in this proposal. More
than 50 repositories upload their SBOMs, of which more than 5 are private. GitHub's [dependency
graph][sbom-gh-dependents] gives an impression of who are contributing their data.

Merged changes are continuously deployed to our backend. We improved the accuracy of PG project pages
on Atlas by incorporating data from live and previous quarter PG proposals, which is not yet
available elsewhere. Our Q3 included several bug fixes, one performance improvement, and a GitHub
dependents crawler authored by Christian. We released API and SDK [v0.7.0][release-v070] in
September. In the frontend, we fixed a user-reported bug and updated the PG Award round pages.

Tansu and the Public Goods Award program itself are continuing their integrations with PG Atlas.

[sbom-gh-dependents]:
  https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-sbom-action/network/dependents
[release-v070]: https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-backend/releases/tag/v0.7.0

## Past Deliverables

N/A

## Proposed Impact

Over the next three months, our goal is to make PG Atlas a more complete, accurate, and operationally
reliable source of evidence about public goods in the Stellar ecosystem.

Current dependency coverage is not yet representative of ecosystem use. Among the 18 public goods
funded in the [2026 Q3 round][round-2026-q3], multiple projects across categories received zero
criticality scores, despite the Pilots' assessment of their broad ecosystem value. This reflects a
structural gap: registry crawls resolve package dependencies to the repositories that publish them,
but miss many applications and other leaf projects that consume public goods without publishing
packages. More than 50 repositories submitting SBOMs, including private repositories, is a useful
start but not a representative sample; we need submissions from hundreds of repositories at minimum.
This also matters for proprietary codebases: SCF Build statistics show that almost half of awarded
projects maintain one or more, and their dependents are not visible in GitHub's public dependency
graph. The authenticated SBOM submission path can make those private dependencies visible to PG
Atlas.

Our proposed work targets those limits: improve dependency coverage and graph quality, reconcile
GitHub dependent observations with submitted SBOM evidence, and make repository maintenance signals
available for review. Queue monitoring and hosted-service health pages will make ingestion operations
and service availability more visible. Together, these improvements will give Stellar builders,
maintainers, and reviewers better context on project reach, critical dependencies, maintenance
activity, and service reliability, supporting more informed quarterly Award discussions and future
(TBD) maintenance-retainer and SLO checkpoints. PG Atlas metrics remain evidence for human review,
not automatic funding decisions, and this quarter's work is a step toward the program's longer-term
goals.

[round-2026-q3]: https://www.pgatlas.xyz/rounds/2026Q3

## Proposed Deliverables

### Maintenance: focused on data quality improvements

Much of our maintenance capacity is reserved to remove data quality issues as they are discovered.

Our starting point is a filled backlog due to limited capacity from May until September.

Data quality backlog:

- Treatment of forks ([#53][issue-53]). Impact: reduces clutter on contributor pages and inflated
  dependent counts on repos.
- Prevent "loose vertices" ([#83 comment][issue-83-comment]). Impact: improves criticality score
  accuracy and declutters sub-graphs.
- Link `pkg:githubactions/` dependencies to projects via repos ([#41][issue-41]). Impact: improves
  criticality score accuracy.
- Merge projects that have been fragmented across multiple canonical IDs (see [OpenGrants comment on
  PGM#143][pgm-143-opengrants-comment]).
- improve within-ecosystem detection for projects without an explicit repo list
- Remove previously linked repos from projects. Impact: reduces clutter on project pages and improves
  the accuracy of project metrics.

Responding to Public Goods Award program changes:

- Refactor `scripts/draft_pg_proposal_overrides.py` based on stable `canonical_id` identifiers (see
  [PGM#143 comment][pgm-143-comment]). Impact: reduces the need for manual corrections.
- UI component to look up projects by GitHub URL. Impact: makes it easier to assign stable project
  IDs to intakes (see [PGM#143][pgm-143]).

Other backlog items:

- Set up an OpenTelemetry backend for API observability.
- Add privacy-preserving frontend analytics.
- The refactoring that is necessary for the deliverables.
- Give our [architecture documentation][architecture] an end-of-year refresh.

We cannot commit to clearing our backlog, only to use the reserved capacity to work on these issues.
Priority will be given to issues that affect the evolution of the Public Goods Award program, such as
the green-lane renewals for stable projects (hinted at in [PGM#142][pgm-142]).

[issue-53]: https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-backend/issues/53
[issue-83-comment]:
  https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-backend/issues/83#issuecomment-6040134368
[issue-41]: https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-backend/issues/41
[pgm-143-opengrants-comment]:
  https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/143#issuecomment-6026588277
[pgm-143-comment]:
  https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/143#issuecomment-5834959986
[pgm-143]:
  https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/143
[pgm-142]:
  https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/pull/142

### D1: Expand support for the SBOM Action

Budget: $4,000

Expand the [PG Atlas SBOM Action][sbom-action] README and related documentation with an ecosystem
support guide based on the practical findings in [Discussion #10][discussion-10]. Explain which
ecosystems need additional repository configuration or a precursor dependency-submission Action
before their dependencies are included in the GitHub Dependency Graph and SBOM available to PG Atlas.

Provide copyable workflow files that builders can add to their own repositories. This resolves
systematic blind spots with Gradle and Swift Package Manager.

Test the workflows end to end using per-ecosystem repositories or a combined monorepo. We'll set up
each demo with dependencies chosen to produce known outcomes, then verify that the expected
dependency data is visible in PG Atlas. The results are your proof.

[sbom-action]: https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-sbom-action
[discussion-10]: https://github.com/orgs/SCF-Public-Goods-Maintenance/discussions/10

### D2: Integrate the GitHub dependents observations

Budget: $3,000

Incorporate the data gathered with Christian's GitHub dependents crawler [#76][pr-76] into the
dependency graph and the criticality metric. GitHub dependents have known issues, such as staying
visible for long after a dependency has been removed. This deliverable includes the work needed to
let negative observations from submitted SBOMs override any GitHub-observed dependents.

Proof: a merged PR, and `/repos/{canonical_id}/has-dependents` feeding into
`/repos/{canonical_id}/github-dependents` API responses.

[pr-76]: https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-backend/pull/76

### D3: Validate maintenance signals

Budget: $4,000

Usage signals look different for public goods that are shipped as packaged code, and those that run
services or publish data. The common ground for all Public Goods Award recipients — that they commit
to actively maintaining their project's code — leaves traces in code forges and issue trackers.
Christian has written a proposal ([#80][issue-80]) and built a first implementation ([#85][pr-85])
that collects maintenance signals and publishes them as repo maintenance profiles.

We will fix adjacent code and review the implementation before starting a gradual rollout.
Maintenance profiles will first be shared with PG maintainers for self-review, to flag inaccuracies
and to gather whether they'd be happy to make commitments based on these signals. The validation
against the Q4 Award round is qualitative: if any proposal discussions call into question if the
maintainers were active enough, this should be consistent with the profiles.

No conclusions can be drawn from the signals by themselves: this is an enabler for each maintainer to
decide if they want to set any service level objectives in 2027.

[issue-80]: https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-backend/issues/80
[pr-85]: https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-backend/pull/85

### D4: Read declared maintainers

Budget: $3,000

The maintenance signals configuration includes a per-repository list of team members, who open their
own issues and PRs, and who respond to those opened by their users and external contributors.

- Derive this list from [`stellar-membership`][stellar-membership] tokens, cross-referenced against
  PG project pages.
- Add declared maintainers to project metadata, and expose them via the API.
- Display GitHub handles on Atlas project pages to show what the configuration reads.

Stretch goal: join declaired maintainers with git-derived contributors on their email address hashes
and show membership token metadata on contributor pages.

[stellar-membership]:
  https://radicle.network/nodes/radicle.consulting-manao.com/rad%3Az4KRDyBiL6kP6n5FWP6kJWga6BXJV

### D5: Task queue monitoring

Budget: $2,000

All ingestion is handled by Procrastinate on GitHub-hosted runners. To expose how much has happened
and what is still scheduled in the task queues, we will:

- Take snapshots of grouped task counts and application table row counts.
- Do this every minute while at least one worker is running, on start, and on exit.
- Periodically trim Procrastinate tables, preserving 12 weeks of full job and event history.
- Backfill grouped task counts to March 2026.
- Add a queue-metrics API endpoint that gives the latest counts, or the deltas over a user-selected
  window.
- A frontend page that shows metrics and current queue sizes.

### D6: Basic uptime monitoring of PG services

Budget: $5,000

Use each PG project's configured `health_endpoint` to monitor hosted services. Add a cancellable
asyncio polling task to the FastAPI lifespan that checks endpoints once per minute, polling projects
concurrently with request timeouts. This will run within the existing API process and use the current
database and deployment setup.

Store one row per project per UTC day, accumulating observed up and down seconds. Begin uptime
accounting with the first successful (2xx) response; derive unclassified time from the eligible
monitoring period rather than storing it separately. Retain the latest observation state and time so
missed polls can be reported as PG Atlas API (collector) gaps.

Add a separate service-status page for each monitored project, linked from that project's detail
page. Extend the API to return the monitored health endpoint URL, latest observation state and time,
90 daily uptime records, and historical outages. Display the daily records as uptime bars and list
outages on the status page.

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
