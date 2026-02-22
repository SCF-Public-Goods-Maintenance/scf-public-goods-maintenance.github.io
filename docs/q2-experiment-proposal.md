# Building the Backbone: Infrastructure for SCF Public Goods

Project URL: <https://scf-public-goods-maintenance.github.io/>

Technical Architecture Document:<https://scf-public-goods-maintenance.github.io/pg-atlas>

GitHub URL: <https://github.com/SCF-Public-Goods-Maintenance/>

Video URL: ???

## Products & Services

Realizing the new Public Goods Award structure requires updates to one existing product and the
development of one new system.

### Tansu — Governance Platform Updates

[Tansu](https://tansu.dev) is an existing decentralized governance and versioning platform built on
Soroban, already deployed on Stellar mainnet. It provides on-chain project registration, DAO-based
proposals and voting (public and anonymous), badge-based membership, and IPFS content storage. The
[full documentation is on tansu.dev](https://tansu.dev/docs/intro).

For the first enhanced decentralization Public Goods Award round (in Q2), Tansu needs targeted
additions to support the PG Award voting workflow:

1. **SCF Governance Space**: Configure and deploy a dedicated SCF Governance organization on Tansu,
   including proposal templates and operational documentation.
1. **NQG Score Integration**: Bridge Tansu’s voting weight system with SCF’s dynamic
   [NQG scores](https://github.com/stellar/stellar-community-fund-contracts), enabling weighted
   voting based on governance reputation.
1. **NQG Soulbound NFT (SEP-50)**: Implement dynamic, soulbound NFTs to represent NQG scores
   on-chain, with [Freighter](https://www.freighter.app/) wallet compatibility and governance
   reputation visualization.

### PG Atlas — Metrics Backbone

[PG Atlas](https://scf-public-goods-maintenance.github.io/pg-atlas/overview) is a new system that
provides the objective, transparent metrics backbone for funding decisions. It does not exist yet.
The full technical architecture is
[documented in the working group repo](https://scf-public-goods-maintenance.github.io/pg-atlas).

The v0 goal is to have PG Atlas operational before the first Q2 voting round, providing metric
context that voters and reviewers can reference. PG Atlas v0 is scoped for a single-machine
deployment. Deliverables include:

1. **Data Ingestion Pipeline**: Build the ingestion layer to populate the dependency graph and
   contributor statistics from
   [SBOM submissions](https://scf-public-goods-maintenance.github.io/pg-atlas/ingestion), registry
   crawling, and git logs.
1. **Storage & Data Model**: Implement a
   [two-level PostgreSQL data model](https://scf-public-goods-maintenance.github.io/pg-atlas/storage)
   with NetworkX for graph analytics, supporting project and repository relationships.
1. **Metric Computation Engine**: Develop algorithms to compute criticality scores, pony factors, and
   adoption signals, materialized for fast API/dashboard reads.
1. **API Layer**: Create a public, read-only REST API to expose PG Atlas metrics for integration with
   dashboards and external tools.
1. **Dashboard**: Build a user-friendly dashboard to visualize metrics, dependency graphs, and
   project-level insights.
1. **Deployment**: Deploy PG Atlas v0 as a single-machine system with <$100/month operational costs,
   ensuring scalability for future iterations.

All of this will be built as free open-source software from the beginning.

## Traction Evidence

This project has been selected as the first concrete initiative in a broader effort to explore
enhanced decentralization for the Stellar Community Fund. The SCF Public Goods Award soft-launched in
June 2025 with intentionally centralized aspects to validate the award structure. After running
several rounds, this structure has proven itself, and we are now ready to take the first step towards
broader community participation.

PG Atlas supports the first Public Goods Award round in Q2 (April) with an updated structure.
Initially, it will be used by eligible public goods maintainers and all SCF Pilots to ensure that
critical ecosystem components can receive sufficient funding. Later in the year, we expect to trial
the first round with delegated community voting, similarly to the existing Build Award (Open track)
process.

## SCF Build Tranche Deliverables

### Tranche 1

30% of budget for first tranche (2 weeks)

#### T1. SCF Governance Space

Create a dedicated SCF Governance organization on Tansu. This is the on-chain space where eligible PG
Award proposals will be submitted, discussed, and voted on. Projects applying for awards don't need
to be registered on Tansu themselves—the governance space is independent.

**Acceptance Criteria**:

1. The SCF Governance space has a Soroban Domain and is visible on Tansu.dev
1. There is a proposal template for PG Award applications
1. It is clearly documented how the SCF Governance space will be used in the award process

**Budget**: $???

#### A1. Repository Scaffolding & CI/CD

Set up the PG Atlas component repositories and continuous integration pipelines under the
[SCF Public Goods Maintenance GitHub organization](https://github.com/SCF-Public-Goods-Maintenance/).
This is the prerequisite for all parallel development work on the backend, ingestion, and dashboard.

**Acceptance Criteria**:

1. Component repositories for the PG Atlas backend (API + ingestion) and dashboard are created and
   publicly accessible under the SCF Public Goods Maintenance org
1. Each repository has a passing CI pipeline (linting and tests) on the main branch
1. Each repository has a README with local development setup instructions
1. Each repository has a FOSS license to ensure code reusability

**Budget**: $???

#### A2. PostgreSQL Schema & Hosting

Provision a hosted PostgreSQL instance and apply the
[two-level data model](https://scf-public-goods-maintenance.github.io/pg-atlas/storage): Projects,
Repos, ExternalRepos, Contributors, `depends_on` edges, and `contributed_to` edges. This is the
storage foundation that all ingestion pipelines write to.

**Acceptance Criteria**:

1. A hosted PostgreSQL instance is running and accessible to the development team
1. The full schema is applied and version-controlled as a migration script
1. The migration script is documented and can be applied from scratch to reproduce the schema

**Budget**: $???

#### A3. FastAPI Application Scaffold & SBOM Webhook

Bootstrap the FastAPI application with a health endpoint and a SBOM webhook receiver. The webhook is
the entry point for project teams submitting SBOMs—it accepts, validates format, and queues
submissions for downstream processing (A8).

**Acceptance Criteria**:

1. The FastAPI application is deployed and reachable at a live URL
1. `GET /health` returns a valid response
1. `POST /ingest/sbom` accepts a CycloneDX SBOM payload, validates its format, and returns 202
   Accepted for valid submissions
1. Submissions with invalid or missing GitHub Action signatures are rejected with an appropriate
   error response

**Budget**: $???

#### A4. SBOM GitHub Action

Publish a [GitHub Action](https://scf-public-goods-maintenance.github.io/pg-atlas/ingestion) that
project teams add to their CI pipelines. The action generates a CycloneDX SBOM and submits it to the
PG Atlas webhook. Early release gives SCF public goods maintainers maximum lead time to onboard
before the Q2 voting round.

**Acceptance Criteria**:

1. The GitHub Action is published and installable from a public repository
1. The action generates a valid CycloneDX SBOM and submits it to the configured PG Atlas endpoint
1. Usage documentation and an example workflow YAML are published
1. The action has been announced to SCF public goods maintainers

**Budget**: $???

#### A5. OpenGrants Project Bootstrapper

Build a script that seeds the Projects table from
[OpenGrants](https://opengrants.daostar.org/system/scf), the DAOIP-5-compatible registry of
SCF-awarded projects. This provides the initial set of known public goods and their dependent SCF
projects as starting nodes for the dependency graph.

**Acceptance Criteria**:

1. The bootstrapper fetches SCF project data from OpenGrants and populates the Projects table
1. The Projects table contains >150 known Stellar/Soroban projects with `display_name`,
   `git_org_url`, and `activity_status` populated
1. The bootstrapper is documented and runnable as both a one-off script and a scheduled job

**Budget**: $???

#### Tranche 1 Completion Date: March 8

### Tranche 2

30% of budget for second tranche (2 weeks)

#### T2. NQG Score Integration

Integrate SCF's existing NQG (Neural Quorum Governance) scores as voting weights in Tansu. Currently,
NQG scores are calculated and stored in the
[stellar-community-fund-contracts](https://github.com/stellar/stellar-community-fund-contracts).
Tansu already supports badge-based weighted voting—the work here is bridging Tansu's weight system to
read from dynamic/changing NQG scores.

Tansu's voting infrastructure supports two integration paths: token-based (locking collateral
proportional to assigned weight) or badge-based (mapping NQG scores to on-chain badges). Both are
feasible with modest contract work. The choice depends on UX and governance preferences—the working
group will finalize this during implementation.

> **Note on anonymous voting:** Tansu already supports anonymous voting using BLS12-381 Pedersen
> commitment schemes. This is available out of the box for the PG Award: the SCF space maintainer can
> inspect votes (comparable to current process), while individual voter choices remain hidden from
> other participants. No additional development is needed for this capability.

**Acceptance Criteria**:

1. Smart contract integration between NQG score source and Tansu voting weights is implemented
1. Frontend updates display NQG-weighted voting power
1. Integration is deployed on testnet and is verified to work

**Budget**: $???

#### A6. Registry Crawlers & Active Subgraph Projection

Build crawlers for npm, crates.io, PyPI, and the Go proxy that populate the dependency graph from
public package registries, starting from curated Stellar/Soroban root packages. Once the graph is
populated, compute the
[active subgraph projection](https://scf-public-goods-maintenance.github.io/pg-atlas/metric-computation)—the
set of repos reachable from at least one active project leaf—which is the prerequisite for
criticality scoring in Tranche 3.

**Acceptance Criteria**:

1. Crawler(s) for npm, crates.io, PyPI, and Go proxy have completed at least one full run
1. The dependency graph contains >100 Repo/ExternalRepo nodes with `depends_on` edges marked
   `inferred_shadow`
1. The active subgraph projection produces a correct, queryable set of active nodes
1. Crawlers are idempotent and safe to re-run without duplicating nodes or edges

**Budget**: $???

#### A7. Git Log Parser & Contributor Statistics

Build the git log ingestion pipeline that parses contributor history for the git repositories in the
Repos table. This populates Contributor vertices and `contributed_to` edges, providing the raw data
for pony factor computation in Tranche 3.

**Acceptance Criteria**:

1. The git log parser runs against all Stellar public goods repos, and on other (SCF project or
   external) repos as desired
1. Contributor vertices and `contributed_to` edges (with commit counts, first/last commit dates) are
   populated in the database
1. `Repo.latest_commit_date` is updated for all processed repos
1. The parser handles repos with no commits or inaccessible URLs gracefully (logged, not fatal)

**Budget**: $???

#### A8. SBOM Processing Pipeline

Implement the downstream processing pipeline for queued SBOM submissions: schema validation,
dependency extraction, repo and edge upserts, and NetworkX graph reload. This closes the loop between
the webhook receiver (A3) and the live graph. SBOMs submitted by early-adopting projects will be
reflected in graph queries once A8 is complete. See the
[Ingestion specification](https://scf-public-goods-maintenance.github.io/pg-atlas/ingestion) for the
full processing logic.

**Acceptance Criteria**:

1. Queued SBOM submissions are validated against the CycloneDX schema; malformed submissions are
   rejected and logged
1. Valid SBOMs are processed end-to-end: the submitting Repo is upserted, declared dependency edges
   are created or updated with `verified_sbom` confidence
1. The NetworkX graph is invalidated or reloaded after each processed SBOM
1. End-to-end verified: a test SBOM submission results in observable Repo and edge changes in the
   database

**Budget**: $???

#### Tranche 2 Completion Date: March 22

### Tranche 3

40% of budget for third tranche (3 weeks)

#### T3. NQG Soulbound NFT (SEP-50)

Build NQG scores as dynamic, soulbound NFTs following the
[SEP-50](https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0050.md) spec for
Freighter wallet compatibility. Each SCF Pilot gets a visible, on-chain representation of their
governance reputation that updates as their NQG score changes.

This has value beyond the PG Award: any Stellar ecosystem project could leverage this trust signal
(e.g., Soroban Security already uses Discord-based Pilot verification for audit report submissions;
an on-chain credential would be a direct improvement).

**Acceptance Criteria**:

1. Smart contract for soulbound dynamic NFT issuance and updates is implemented
1. Art/design for status visualization is completed
1. Freighter integration testing is performed and documented
1. Comprehensive documentation for the NFT system is published

**Budget**: $???

#### A9. Criticality Scores & Pony Factor Materialization

Compute and materialize the two primary impact and risk metrics—criticality scores and pony
factors—at both repo and project level. Criticality (transitive active dependent count) builds on the
active subgraph from A6; pony factor builds on the git contributor data from A7. These are the
headline signals that are displayed on the dashboard and can later be used in the Metric Gate. See
the
[Metric Computation specification](https://scf-public-goods-maintenance.github.io/pg-atlas/metric-computation)
for the full algorithms.

**Acceptance Criteria**:

1. Criticality scores are computed for all repos in the active subgraph and materialized to
   `repos.criticality_score`
1. Project-level criticality is aggregated and materialized to `projects.criticality_score`
1. Pony factors are computed from `contributed_to` edge data and materialized to `repos.pony_factor`
   and `projects.pony_factor`
1. A batch recompute runs on schedule and is triggered by significant graph changes (e.g., new SBOM
   ingestion)

**Budget**: $???

#### A10. Adoption Signals

Fetch and store off-chain adoption data—registry download counts (last 30 days), GitHub stars, and
forks—for all repos in the Projects table. These supplement criticality and pony factor as a third
signal for voters and reviewers.

**Acceptance Criteria**:

1. Download counts are fetched from npm, crates.io, and PyPI for all known packages and stored in
   `repos.adoption_downloads`
1. GitHub stars and forks are fetched and stored in `repos.adoption_stars` and `repos.adoption_forks`
1. Adoption signals are aggregated to project level in `projects.adoption_score`
1. A periodic refresh job keeps adoption signals up to date

**Budget**: $???

#### A11. Public REST API & TypeScript SDK

Build the full public, read-only
[REST API](https://scf-public-goods-maintenance.github.io/pg-atlas/api) that exposes all PG Atlas
data to the dashboard, Tansu voting context, and community tools. Includes an auto-generated
TypeScript SDK for easy consumption by external integrations.

**Acceptance Criteria**:

1. Core endpoints are live and return real data: `/projects`, `/projects/{id}`, `/repos`,
   `/repos/{id}`, `/repos/{id}/dependents`, `/repos/{id}/dependencies`, `/scores`, and graph export
1. OpenAPI spec is auto-generated and can be interactively tested at `/docs`
1. Rate limiting (100 req/min per IP) is enforced
1. A TypeScript SDK is generated from the OpenAPI spec, published, and documented with usage examples

**Budget**: $???

#### A12. Public Dashboard

Build the public, zero-auth
[React-based dashboard](https://scf-public-goods-maintenance.github.io/pg-atlas/dashboard) that makes
PG Atlas data browsable for voters, maintainers, and community observers. The dashboard consumes the
REST API exclusively.

**Acceptance Criteria**:

1. The dashboard is publicly accessible at a live URL with no login required
1. The landing page displays an ecosystem summary: total active projects, top critical PGs, and a
   risk distribution overview
1. The searchable leaderboard shows projects sortable by criticality, pony factor, and adoption, with
   risk flags (e.g., pony factor = 1 highlighted)
1. Project detail pages show score breakdowns, dependent and dependency lists, and contributor
   statistics
1. An interactive dependency (sub-)graph visualization is accessible from project detail pages

**Budget**: $???

#### A13. Deployment & Operations

Put all PG Atlas components into production with automated scheduling, monitoring, and backups, per
the [operations specification](https://scf-public-goods-maintenance.github.io/pg-atlas/operations).

**Acceptance Criteria**:

1. Scheduled jobs are running: registry crawls (weekly), git log refresh (periodic), and metric
   recomputes (scheduled batch + triggered on SBOM ingestion)
1. Health monitoring is configured: the `/health` endpoint is monitored externally with alerting on
   failure
1. Error tracking (Sentry) is active for the API and ingestion services
1. Database backups are automated (daily `pg_dump` to a remote location)

**Budget**: $???

#### A14. Community Feedback Loop

Establish the mechanisms for the community to report graph errors and propose project additions, and
complete an initial data quality pass before the Q2 voting round opens.

**Acceptance Criteria**:

1. Issue templates for reporting graph corrections and proposing new project additions are published
   in the GitHub repo
1. Known Stellar/Soroban public goods are present in the graph with plausible metric values
1. The first correction cycle has been initiated: community feedback is being received, reviewed, and
   reflected in the graph

**Budget**: $???

#### Tranche 3 Completion Date: April 12
