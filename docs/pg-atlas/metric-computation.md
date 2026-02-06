---
title: Metric Computation
parent: PG Atlas Architecture
nav_order: 4
---

# Metric Computation

## Overview

The metric computation layer derives objective scores from the stored graph and contributor data to
power the Metric Gate and public dashboards. Computations run on triggers (per-project SBOM
ingestion) and scheduled batch jobs (quarterly or on survey release).

**v0 focus**:

- Criticality via transitive active dependent count.
- Pony factor as primary decentralization/risk metric.
- Basic adoption signals (off-chain: downloads/stars via registry APIs).
- Active subgraph projection as foundational step for all graph metrics.

All heavy computations occur offline (batch or incremental), with results materialized back to
storage (e.g., cached scores on vertices) for fast API/dashboard queries.

**Implementation approach**:

- Load full graph into memory (NetworkX DiGraph or native TinkerPop traversal) for batch runs.
- Incremental updates where possible (e.g., delta propagation on new edges).
- Backend-agnostic Gremlin preferred long-term; v0 accepts NetworkX for speed.

## Active Subgraph Projection

**Purpose**: Identify the "live" portion of the ecosystem — nodes that support at least one active
leaf project. This filters out dead branches and ensures criticality reflects current health.

**Logic** (upstream propagation):

- Start from all vertices where `active == true` and `in-degree == 0` (true leaves) or all active
  leaves.
- Traverse upstream along "depends-on" edges (outgoing from dependents to dependencies).
- Mark all reached ancestors as part of the active ecosystem.
- Result: Subgraph containing only nodes with paths from active leaves.

**Preferred v0 implementation**:

- In-memory NetworkX: BFS/DFS from active leaves on reversed graph view (O(V + E)).
- Alternative (if JanusGraph selected): Gremlin `repeat(out())` from active leaves.

```groovy
// Identify all nodes that are roots of or ancestors to an ACTIVE leaf
g.V().has('active', true)
 .filter(inE().count().is(0)) // Start at active leaf nodes
 .repeat(outE().subgraph('active-ecosystem').inV())
 .emit()
 .cap('active-ecosystem')
```

**Efficiency**: O(V + E) per full run — acceptable at projected scale; cache active set between runs.

<!-- FUTURE SELF: Materialize active_subgraph membership as vertex property for faster filtering in
repeated queries. -->

## Core Metrics (v0)

### Criticality Score

**Definition**: Count of active nodes that have a directed path to this node (i.e., transitive
dependents in active subgraph).

**Calculation**:

1. Project active subgraph.
2. For each target node, count ancestors in the reversed active subgraph (nodes reaching it).
3. Materialize as `criticality_score` property.

**Incremental potential**: On new active leaf/edge, propagate delta upward.

<!-- NOTE: Requires reversed graph index/view for efficient ancestor counts — add if backend
supports (JanusGraph does natively). -->

### Pony Factor

**Definition**: Minimum number of contributors responsible for ≥50% of commits (lower = higher risk).

**Calculation** (from git logs):

- Parse author counts over 12–24 month window.
- Sort descending, cumulative sum until ≥50%.
- Store computed value + raw stats.

**Extended stats**:

Desirable, comparable to Scientific Python devstats.

- Total contributors.
- Commit distribution (top 10 authors %).
- First/last commit dates.
- Author experience (tenure).

**v0 scope**: Basic pony factor only.

<!-- INGESTION/STORAGE CHANGE NEEDED: Store richer git log snapshots (full author timeline or
aggregated buckets) to enable extended stats without re-cloning repos each run. -->

<!-- FUTURE EXTENSION: GH API for issue/PR stats (open/closed rates, reviewer diversity) —
requires new ingestion pipeline, possible synergy with SBOM upload action. -->

### Adoption Signals

**Sources** (off-chain):

- Registry downloads (npm/crates/PyPI last month).
- GitHub stars/forks/clones (via API).

**Calculation**:

- Normalized, smoothed scores per node.
- Aggregate into composite adoption metric.

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

- Computed scores stored as vertex properties.
- Timestamp last computation.
- Dashboard/API read from cache; trigger recompute on significant graph changes.

## Open Questions

- Full vs. incremental recompute frequency (quarterly full + per-SBOM delta)?
- Weighting formula for composite PG Score in Metric Gate (start with criticality 50%, pony/adoption
  25% each)?
- Thresholds for risk flags (e.g., `pony_factor == 1` → red)?

<!-- QUESTION FOR LEAD: Include Mermaid flowchart for active subgraph and criticality calculation?
-->

<!-- FUTURE SELF: Benchmark full recompute time post-bootstrap; if >10min, prioritize incremental
logic. -->
