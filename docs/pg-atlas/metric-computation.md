---
title: Metric Computation
parent: PG Atlas Architecture
nav_order: 4
---

# Metric Computation

## Overview

The metric computation layer derives objective scores from the stored graph and contributor data to
power the Metric Gate and public dashboards. Computations run on triggers (per-repo SBOM ingestion,
git log refresh) and scheduled batch jobs (yearly on survey release, plus higher-frequency
triangulation from OpenGrants and git activity).

**v0 focus**:

- Criticality via transitive active dependent count (computed at repo level, aggregated to project).
- Pony factor as primary decentralization/risk metric (per-repo, aggregated to project).
- Basic adoption signals (off-chain: downloads/stars via registry APIs, per-repo).
- Active subgraph projection as foundational step for all graph metrics.

All heavy computations occur offline (batch or incremental), with results materialized back to
storage (e.g., cached scores on repo and project rows) for fast API/dashboard queries.

**Implementation approach**:

- Load full graph into memory (NetworkX DiGraph) for batch runs. The graph operates at **repo
  resolution** — all `depends_on` edges connect repos (or external repos).
- Incremental updates where possible (e.g., delta propagation on new edges).
- Project-level metrics are derived by aggregating repo-level results.
- Backend-agnostic Gremlin preferred long-term; v0 uses NetworkX for speed.

## Active Subgraph Projection

**Purpose**: Identify the "live" portion of the ecosystem — repo nodes that support at least one
active leaf project. This filters out dead branches and ensures criticality reflects current health.

**Logic** (upstream propagation):

- Start from all **repo** vertices where `project.activity_status IN ('live', 'in-dev')` and
  `in-degree == 0` in the repo-level dependency graph (true leaves: repos with no dependents).
- Traverse upstream along "depends-on" edges (outgoing from dependents to dependencies).
- Mark all reached ancestors as part of the active ecosystem.
- Result: Subgraph containing only repo nodes with paths from active leaves.

Repo-level activity status is derived from the parent project's status (see
[Activity Status Update Logic](storage.md#activity-status-update-logic) in Storage). Both `live` and
`in-dev` repos are treated as active for subgraph projection.

**Preferred v0 implementation**:

- In-memory NetworkX: BFS/DFS from active leaves on reversed graph view (O(V + E)).

```python
import networkx as nx

def project_active_subgraph(G: nx.DiGraph) -> set:
    """Return set of repo node IDs reachable from active leaves."""
    # Active leaves: active repos with no dependents (in-degree == 0 in depends-on direction)
    active_leaves = {
        n for n, d in G.nodes(data=True)
        if d.get('activity_status') in ('live', 'in-dev')
        and G.in_degree(n) == 0
    }

    # Traverse upstream (reverse direction) to find all dependencies of active repos
    reversed_G = G.reverse()
    active_nodes = set()
    for leaf in active_leaves:
        active_nodes.update(nx.descendants(reversed_G, leaf))
    active_nodes.update(active_leaves)
    return active_nodes
```

**Efficiency**: O(V + E) per full run — acceptable at projected scale; cache active set between runs.

<!-- FUTURE SELF: Materialize active_subgraph membership as vertex property for faster filtering in
repeated queries. -->

## Core Metrics (v0)

### Criticality Score

**Definition**: Count of active repo nodes that have a directed path to this repo node (i.e.,
transitive dependents in active subgraph). Computed at the **repo level**.

**Calculation**:

1. Project active subgraph (repo-level graph).
2. For each target repo node, count ancestors in the reversed active subgraph (repos depending on it,
   transitively).
3. Materialize as `criticality_score` on repo row.
4. **Project-level aggregation**: `Project.criticality_score = SUM(repo.criticality_score)` across
   all repos belonging to the project. This reflects total ecosystem dependency pressure on the
   project.

**Incremental potential**: On new active leaf/edge, propagate delta upward through the repo graph.

### Pony Factor

**Definition**: Minimum number of contributors responsible for ≥50% of commits (lower = higher risk).

**Calculation** (from git logs, per-repo):

- Parse author counts over 12–24 month window (from `contributed_to` edges).
- Sort descending, cumulative sum until ≥50%.
- Store computed value on `Repo.pony_factor`.

**Project-level aggregation**: Compute pony factor across all repos' contributors (unique
contributors, deduplicated by `Contributor.email_hash`). This avoids double-counting a contributor
who works across multiple repos in the same project. The aggregation method (union of contributors
across repos, then standard pony factor calculation) may need tuning — see Open Questions.

**Extended stats**:

Desirable, comparable to Scientific Python devstats:

- Total contributors.
- Commit distribution (top 10 authors %).
- First/last commit dates (from `contributed_to.first_commit_date`/`last_commit_date`).
- Author experience (tenure).

**v0 scope**: Basic pony factor only.

<!-- INGESTION/STORAGE CHANGE NEEDED: Store richer git log snapshots (full author timeline or
aggregated buckets) to enable extended stats without re-cloning repos each run. -->

<!-- FUTURE EXTENSION: GH API for issue/PR stats (open/closed rates, reviewer diversity) —
requires new ingestion pipeline, possible synergy with SBOM upload action. -->

### Adoption Signals

**Sources** (off-chain, per-repo):

- `adoption_downloads`: Registry package downloads (npm/crates/PyPI last 30 days). Stored on `Repo`.
- `adoption_stars`: GitHub stars. Stored on `Repo`.
- `adoption_forks`: GitHub forks. Stored on `Repo`.

**Calculation**:

- Normalize each signal across all repos (e.g., percentile rank or log-scale normalization).
- Smooth over time if historical snapshots are available.
- Aggregate into composite `adoption_score` per repo, then to project level.

**Project-level aggregation**: `Project.adoption_score` is a composite of its repos' adoption
signals. Aggregation method TBD (sum, max, or weighted average depending on signal type — downloads
may sum well, stars may use max).

<!-- INGESTION CHANGE NEEDED: Periodic registry API crawl job to populate adoption fields —
possibly separate from SBOM/shadow, but research synergies. -->

## Deferred Metrics (Post-v0)

- Reliability (uptime/SLO — requires monitoring integration).
- On-chain usage, e.g.:
  - Soroban invocations and cross-contract calls
  - created/sponsored accounts
  - number of user-initiated transactions
  - transaction volume in USD
- Security/Quality (audit status, CVE response).
- Advanced decentralization (reviewer diversity, open governance signals).

## Materialization & Caching

- Computed scores stored on `Repo` rows (criticality_score, pony_factor, adoption signals).
- Project-level aggregates stored on `Project` rows (criticality_score, pony_factor, adoption_score).
- Timestamp last computation (`updated_at`).
- Dashboard/API read from materialized values; trigger recompute on significant graph changes.

## Open Questions

- Full vs. incremental recompute frequency (yearly full on survey + per-SBOM delta + periodic git
  refresh)?
- Weighting formula for composite PG Score in Metric Gate: the working group has proposed
  (criticality 50%, pony/adoption 25% each) as a starting point, but this is not yet decided. We
  won't operationalize the Metric Gate in v0 — the PG Score formula will be refined based on
  experience from the first rounds.
- Thresholds for risk flags (e.g., `pony_factor == 1` → red)?
- Project-level pony factor aggregation: union of unique contributors across all repos (then standard
  pony factor calculation), or some other method?
- Project-level adoption score aggregation: sum vs. max vs. weighted average per signal type?

<!-- QUESTION FOR LEAD: Include Mermaid flowchart for active subgraph and criticality calculation?
-->

<!-- FUTURE SELF: Benchmark full recompute time post-bootstrap; if >10min, prioritize incremental
logic. -->
