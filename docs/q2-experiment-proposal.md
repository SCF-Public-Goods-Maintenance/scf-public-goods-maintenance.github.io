# Building the Backbone: Infrastructure for SCF Public Goods

Project URL: <https://scf-public-goods-maintenance.github.io/>

Technical Architecture Document:<https://scf-public-goods-maintenance.github.io/pg-atlas>

GitHub URL: <https://github.com/SCF-Public-Goods-Maintenance/>

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

Create a dedicated SCF Governance organization on Tansu. This is the on-chain space where PG Award
proposals will be submitted, discussed, and voted on. Projects applying for awards don't need to be
registered on Tansu themselves—the governance space is independent.

- Scope: Configuration and deployment of an SCF-specific Tansu space; proposal templates for PG Award
  applications; operational documentation.

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

- Scope: Smart contract integration between NQG score source and Tansu voting weights; frontend
  updates to display NQG-weighted voting power; testing on testnet before mainnet deployment.

#### Tranche 2 Completion Date: March 22

### Tranche 3

40% of budget for third tranche (3 weeks)

#### T3. NQG Soulbound NFT (SEP-50)

Build NQG scores as dynamic, soulbound NFTs following the
[SEP-50](https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0050.md) standard for
Freighter wallet compatibility. Each Pilot gets a visible, on-chain representation of their
governance reputation that updates as their NQG score changes.

This has value beyond the PG Award—any Stellar project could leverage this trust signal (e.g.,
Soroban Security already uses Discord-based Pilot verification for audit report submissions; an
on-chain credential would be a direct improvement).

- Scope: Smart contract for soulbound dynamic NFT issuance and updates; art/design for status
  visualization; Freighter integration testing; documentation.

> **Note on anonymous voting:** Tansu already supports anonymous voting using BLS12-381 Pedersen
> commitment schemes. This is available out of the box for the PG Award: the SCF space maintainer can
> inspect votes (comparable to current process), while individual voter choices remain hidden from
> other participants. No additional development is needed for this capability.

#### Tranche 3 Completion Date: April 12

### PG Atlas

<!-- UNTANGLE DELIVERABLES BEFORE ASSIGNING WORK ITEMS TO TRANCHES -->

#### D4. Data Ingestion Pipeline

Build the ingestion layer that populates the dependency graph and contributor statistics from three
sources:

- **SBOM submissions:** A GitHub Action that project teams add to their CI pipelines. It generates a
  CycloneDX SBOM and submits it to PG Atlas. This is the verification layer—explicit,
  project-declared dependencies.
- **Reference graph bootstrapping:** Automated crawling of public package registries (npm, crates.io,
  PyPI, Go proxy) and [OpenGrants](https://opengrants.daostar.org/system/scf) to build an initial
  graph from known Stellar/Soroban roots. This ensures a meaningful graph even before SBOM adoption
  ramps up.
- **Git contributor logs:** Parsing of git history to compute pony factor and contributor statistics
  per repository.

All ingestion writes at the repository level. Project-level data is derived by aggregation. See the
[Ingestion specification](https://scf-public-goods-maintenance.github.io/pg-atlas/ingestion) for
details.

- Scope: GitHub Action for SBOM generation/submission; FastAPI webhook endpoint for ingestion;
  registry crawlers (npm, crates.io, PyPI, Go proxy); git log parser; OpenGrants project
  bootstrapper; validation and deduplication logic.

#### D5. Storage & Data Model

Implement the [two-level data model](https://scf-public-goods-maintenance.github.io/pg-atlas/storage)
(Project → Repo, one-to-many) in PostgreSQL with NetworkX for graph analytics:

- **Vertex types:** Project (funding unit), Repo (ingestion unit), ExternalRepo (out-of-ecosystem
  dependencies), Contributor.
- **Edge types:** `depends_on` (repo → repo/external repo), `contributed_to` (contributor → repo).
- **Activity status tracking:** 4-value enum (live, in-dev, discontinued, non-responsive) sourced
  from SCF Impact Survey with higher-resolution updates from OpenGrants completion data and git
  activity.

The working group chose PostgreSQL + NetworkX over native graph databases for v0 based on team
expertise, speed to ship, scale appropriateness (5–10K nodes, 50–100K edges fits in memory), and
operational simplicity. The architecture preserves a migration path to TinkerPop-compatible graph
databases if needed. The decision rationale is fully documented in the
[Storage specification](https://scf-public-goods-maintenance.github.io/pg-atlas/storage).

- Scope: PostgreSQL schema (SQLAlchemy models); NetworkX graph construction and synchronization;
  incremental update logic for SBOM ingestion, batch updates for activity status, and periodic
  reference graph sync.

#### D6. Metric Computation Engine

Implement the core metrics that power the Metric Gate, computed at repository level and aggregated to
project level:

- **Criticality score:** Transitive active dependent count—how many active projects depend on this
  one, directly or indirectly. Computed via active subgraph projection (BFS from active leaves on
  reversed dependency graph).
- **Pony factor:** Minimum number of contributors responsible for ≥50% of commits. The primary
  risk/decentralization metric.
- **Adoption signals:** Registry downloads, GitHub stars/forks—normalized and aggregated per project.

All computation happens offline (batch or incremental) with results materialized to database rows for
fast API/dashboard reads. The
[Metric Computation specification](https://scf-public-goods-maintenance.github.io/pg-atlas/metric-computation)
documents the algorithms and aggregation methods.

- Scope: Active subgraph projection algorithm; criticality score computation and propagation; pony
  factor calculation from git logs; adoption signal normalization; materialization pipeline;
  trigger-based recomputation on graph changes.

> **Explicitly out of scope for v0:** On-chain telemetry (Soroban invocation metrics—no unified
> source exists yet), composite PG Score formula (deferred until we have experience from first
> rounds), versioned package blast radius modeling, and advanced sybil-resistant usage signals.

#### D7. API Layer

A public, read-only [REST API](https://scf-public-goods-maintenance.github.io/pg-atlas/api) built
with FastAPI that exposes PG Atlas data to the dashboard, Tansu voting context, and community tools:

- Project and repo listings with filtering, pagination, and search.
- Dependency and dependent lookups (direct and transitive).
- Metric scores and leaderboards.
- Bulk exports (CSV/JSON) for offline analysis and community verification.
- Auto-generated OpenAPI spec with Swagger UI, plus a TypeScript SDK generated from the spec.

No authentication required for reads. Rate-limited at 100 requests/minute per IP.

- Scope: FastAPI application; endpoint implementation; OpenAPI documentation; caching layer; rate
  limiting; TypeScript SDK generation.

#### D8. Public Dashboard

A public, zero-auth [dashboard](https://scf-public-goods-maintenance.github.io/pg-atlas/dashboard)
providing visual access to PG Atlas data:

- **Landing page:** Ecosystem summary—total active projects, dependency coverage, risk distribution,
  top critical PGs.
- **Searchable leaderboard:** Filterable table of projects ranked by metrics, with risk flags (e.g.,
  pony factor = 1 highlighted in red).
- **Project detail pages:** Score breakdown, dependent/dependency lists, contributor statistics.
- **Graph explorer:** Interactive dependency graph visualization with active subgraph highlighting.

The technology choice (Panel or React/Next.js) is still
[under discussion](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/3).
The working group is evaluating speed-to-launch vs. long-term flexibility. The dashboard consumes the
API exclusively—no direct database access.

- Scope: Frontend implementation; API integration; graph visualization; responsive design; deployment
  and hosting.

#### D9. Deployment & Operations

Production deployment of PG Atlas targeting <$100/month operational cost:

- Push-to-deploy CI/CD pipeline.
- PostgreSQL hosting (managed or self-hosted).
- Periodic job scheduling for registry crawls, metric recomputes, and activity status updates.
- Health monitoring, error tracking (Sentry), and backup strategy.
- HTTPS enforcement, rate limiting, and ingestion input validation.

Deployment strategy options are
[documented in detail](https://scf-public-goods-maintenance.github.io/pg-atlas/operations). The
working group is evaluating DigitalOcean App Platform, GitHub-maximal (VPS + Actions), and Fly.io.

- Scope: Infrastructure provisioning; CI/CD setup; monitoring and alerting; backup automation;
  operational documentation.
