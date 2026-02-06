---
title: Storage
parent: PG Atlas Architecture
nav_order: 3
---

# Storage

## Overview

The storage layer persists the dependency graph, node/edge metadata, versioning information,
contributor statistics, and raw ingested artifacts. For v0, we require a single-machine deployment
with minimal DevOps overhead, supporting efficient per-project incremental updates (e.g., new SBOM
ingestion triggering edge/node changes) and occasional batch updates (e.g., SCF Impact Survey or
milestone status changes flipping many activity flags).

**Primary goals**:

- Incremental updates from ingestion (fast writes for single-project SBOMs).
- Batch efficiency for activity flag recalculations.
- Version labeling: full versioning for published packages (PG roots/upstream), latest git hash/tag
  for leaf projects.
- Visibility into outside-ecosystem dependencies of within-ecosystem PGs.
- Separate pony factor data (git contributor logs).
- Auditability via retained raw SBOMs/crawl snapshots.

**Scale target**: 5–10k nodes, 50–100k edges — comfortably single-machine.

**Decision status**: Final backend deferred until the second full architecture iteration.
Requirements and trade-offs will become clearer as our picture of storage use-cases matures. Current
shortlist: JanusGraph (BerkeleyDB), Sqlg (PostgreSQL), HugeGraph (RocksDB). All are FOSS, single-node
capable, and TinkerPop-compatible.

## Data Model

The schema is designed to map naturally to TinkerPop property graphs, enabling any shortlisted
backend. This schema is minimal and likely incomplete; it'll be expanded based on downstream
use-cases, and eventually performance-oriented benchmark experiments.

**Vertices** (nodes):

- `canonical_id` (unique key: `ecosystem:package` or `github:org/repo`).
- `display_name`.
- `type` (label or property: `pg_root`, `scf_project`, `external_upstream`).
- `active` (boolean property).
- `latest_version` (property: git hash/tag or published version).
- `repo_url` (for pony factor).
- `metadata` (map/JSON property for anything we want to show but not traverse/query).

**Versioned Releases** (for PG roots/upstream):

- Separate vertices per version, or multi-properties on main vertex (v0 simplicity favors
  multi-properties).

**Edges** (dependencies):

- Directed: dependent → dependency ("depends-on" toward roots).
- Properties: `version_range`, `confidence` (`verified_sbom`, `inferred_shadow`).

**Pony Factor**:

- Separate vertex property or side table/collection (JSON map of contributor counts + computed
  pony_factor).

**Activity Flag (v0)**:

- Binary `active` property.
- Derived from: git log recency, SCF Impact Survey score, milestone status.
- Updated via batch job on survey release or per-project on SBOM/git triggers.

**Raw Artifacts**:

- File storage (separate git repo or lightweight bucket/IPFS) with vertex references.

<!-- QUESTION FOR LEAD: Add diagram of property graph schema, through gdotv.com or Hackolade after
implementation? Mermaid ERD before implementation? -->

## Backend Options

### JanusGraph (BerkeleyDB backend, single-node)

**Pros**:

- Native TinkerPop/Gremlin — optimal for traversals (active subgraph upstream propagation) and OLAP
  batch jobs.
- BerkeleyDB is embeddable/file-based — true zero-cluster persistence, low overhead.
- Efficient indexed writes for per-project updates; supports batch transactions.
- Proven for property graphs with versioning/multi-properties.
- Seamless future scaling (swap to Cassandra/Scylla).

**Cons**:

- Java ecosystem (vs. Python-native tooling).
- Slightly higher memory footprint than pure relational for small graphs.
- Git log/pony factor data needs separate storage or JSON properties.

### Sqlg (over PostgreSQL)

**Pros**:

- Gremlin queries on familiar relational backend — no new infrastructure.
- PostgreSQL excels at mixed workloads: graph edges + tabular pony factor/git logs in separate
  schemas.
- Excellent batch update performance (SQL SET for activity flags across thousands of rows).
- Fast incremental writes via standard ORM.
- Easy audit/export with SQL tools.

**Cons**:

- Graph traversals less optimized than native graph DBs (recursive CTEs slower for deep queries).
- Potential impedance mismatch for complex OLAP (still relies on NetworkX load for heavy metrics).
- Migration to full distributed graph later requires data export.

### HugeGraph (RocksDB backend — single-node)

**Pros**:

- Native Gremlin with strong OLTP/OLAP support.
- RocksDB embeddable and high-performance for writes.
- Built-in schema flexibility for versioning.
- Good batch transaction support.

**Cons**:

- Less mature community/maintenance than JanusGraph.
- Configuration overhead higher than BerkeleyDB embed.
- Pony factor/git logs require separate handling or JSON blobs.
- Scaling path less standardized than JanusGraph.

## Recommended Path

Assume **JanusGraph + BerkeleyDB** for detailed implementation:

- Best native graph performance for v0 metrics (transitive counts, active subgraph).
- Per-project updates: Gremlin transactions for edge/vertex changes.
- Batch activity updates: Scripted Gremlin or bulk load for flag flips.
- Pony factor: Materialize on repo vertices but store intermediate git contributor stats as an edge
  type or in a separate data structure.

## Migration & Extensibility

All options preserve TinkerPop compatibility:

- Start with chosen single-node → add distributed backend later if needed.
- Export path: Gremlin bulk dump or standard serialization. Traversals stay in Gremlin and won't need
  a major port/rewrite later on.

## Open Questions

- Final backend selection criteria (e.g., benchmark per-project vs. batch update times)?
- Pony factor storage location (materialized on vertex and/or separate collection / edge type)?
- Activity flag recalculation frequency/triggers post-v0?
