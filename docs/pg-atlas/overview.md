---
title: Overview & Goals
parent: PG Atlas Architecture
nav_order: 1
---

# Overview & Goals

## Purpose

PG Atlas is the objective, transparent metrics backbone for the SCF Public Goods Maintenance program.
Its primary role is to shift public goods funding decisions from noisy, subjective signals to
verifiable, data-driven insights by quantifying **adoption**, **criticality**, **reliability**,
**security/quality**, and **decentralization** (risk) across open-source tools, libraries, explorers,
RPC infrastructure, SDKs, and other foundational components in the Stellar/Soroban ecosystem.

By providing a live dependency graph, transitive impact scoring, pony factor analysis, and an active
subgraph projection, PG Atlas directly powers the **Metric Gate** in the proposed funding decision
stack (target ~50% weight in allocation formulas) and supplies off-chain context for NQG-weighted
community voting in the Tansu-based Public Goods DAO pilot.

## Why PG Atlas Matters

- **Reduces systemic risk**: Early detection of pony factor issues, low-usage tools, or concentration
  risks prevents cascading failures (e.g., Okashi/Mercury-style breakdowns).
- **Improves funding efficiency**: Replaces "expectation everyone gets funded" inertia with
  merit-based baselines, minimizing over-funding of low-impact tools while rewarding proven,
  widely-used infrastructure.
- **Enhances legitimacy & decentralization**: Public, reproducible metrics build voter/expert trust,
  attract serious maintainers, and position Stellar's PG program as best-in-class among mid-tier L1s
  (more transparent than Gitcoin QF, more predictable than Polkadot treasury referenda, as
  impact-aligned as Optimism RetroPGF but with NQG sybil resistance).
- **Accelerates ecosystem growth**: Clear visibility into dependencies encourages reuse over
  duplication, lowers developer friction, and signals priorities for new tooling.

If under-delivered: We remain stuck with quarterly manual reviews, noisy signals, and persistent pony
factor risks — stalling the 2026 outcomes (coverage/reliability, risk reduction, signal quality).

## v0 Success Criteria

Target: Usable by April 12, 2026

1. **Bootstrap a meaningful graph**: ≥100 Project nodes (with their child Repos) and basic
   `depends_on` edges from shadow registry crawling + initial SBOM submissions.
2. **Core metrics live**: Transitive active dependent count (criticality proxy), pony factor scoring,
   basic adoption signals (downloads/stars) — computed at repo level, aggregated to project level.
3. **Public dashboard operational**: Readable dependency visualization, searchable PG leaderboards,
   risk flags (e.g., pony factor = 1 highlighted).
4. **API functional**: At least read-only endpoints for projects, repos, criticality scores, and
   graph exports to support first Tansu round context.
5. **Community feedback loop**: Initial data displayed publicly, with clear issue templates for
   corrections/additions.

## Scope Boundaries (v0)

**In scope**:

- Shadow graph bootstrapping from public registries (npm, crates.io, PyPI, Go proxy via APIs or Open
  Source Observer).
- SBOM ingestion via GitHub Action (verification layer).
- **Two-level data model**: `Project` (funding/scoring unit, DAOIP-5 URIs) → `Repo` (1-to-many,
  ingestion unit). Separate `ExternalRepo` table for out-of-ecosystem dependencies. All ingestion
  writes at repo level; project-level metrics derived by aggregation. See
  [Storage](/pg-atlas/storage.md) for schema details.
- Directed `depends_on` graph at repo resolution, with project-level view derived by collapsing repo
  edges.
- **Activity status**: 4-value enum (`live`, `in-dev`, `discontinued`, `non-responsive`) on `Project`
  — sourced from SCF Impact Survey (yearly baseline) with higher-resolution triangulation from
  OpenGrants completion % and repo `latest_commit_date`. See
  [Activity Status Update Logic](/pg-atlas/storage.md#activity-status-update-logic).
- Active subgraph projection via upstream propagation from active leaves.
- Core metrics: transitive dependent count, pony factor (git log parsing), basic off-chain adoption —
  all computed at repo level, aggregated to project level. PG Score composite formula deferred.
- Decoupled backend: PostgreSQL + NetworkX (decided in
  [issue #2](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/2)).
- FastAPI layer with OpenAPI docs (TypeScript SDK generated from spec).
- Public dashboard (technology under discussion in
  [issue #3](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/3)).

**Out of scope for v0** (explicitly deferred):

- On-chain telemetry (Soroban contract/RPC call volume) — no unified activity metrics yet.
- Versioned package modeling (blast radius per release).
- Native property graph DB deployment — PostgreSQL + NetworkX is the v0 choice; graph DB options
  documented in [Graph Scaling](/pg-atlas/graph-scaling.md) for future evaluation.
- Automated on-chain Metric Gate integration with Tansu.
- Advanced Sybil-resistant usage signals.
- PG Score composite weighting formula (deferred until experience from first rounds).

<!-- FUTURE SELF: Revisit out-of-scope list post-v0 launch; prioritize on-chain usage once Soroban
tooling matures -->

## Open Questions

- How aggressively should we mandate SBOM submission (e.g., testnet tranche gate vs. soft incentive)?
- Should criticality scoring include weighted dependents (e.g., production apps > samples) in v0.1?

<!-- QUESTION FOR LEAD: Do we want to include a high-level diagram here (Mermaid flowchart of data
pipeline)? If yes, provide description and I'll add in next iteration. -->

## Assumptions & Risks

- Ecosystem scale remains small enough for in-memory NetworkX OLAP through 2026.
- SBOM uptake can be bootstrapped sufficiently via shadow graph + early incentives.
- Project → Repo mapping can be established from OpenGrants + GitHub org URLs with reasonable
  completeness.
- Risk: Low initial data quality
  - mitigate with transparent flagging ("incomplete graph" warnings) and manual curation path.
