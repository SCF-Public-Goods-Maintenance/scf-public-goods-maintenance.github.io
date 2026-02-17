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

**Decision status**: We'll build v0 on PostgreSQL, with graph analytics handed off to NetworkX. See
the evaluated choices and our decision process in
[issue #2](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/2).

### Why PostgreSQL + NetworkX?

The working group chose PostgreSQL + NetworkX for v0 based on:

1. **Team expertise**: Everyone knows PostgreSQL. The team has direct connections to NetworkX
   maintainers (Scientific Python ecosystem).
2. **Speed to ship**: FastAPI + SQLAlchemy + PostgreSQL is a well-trodden path. We can have a working
   prototype in days, not weeks — critical for the April 12 deadline.
3. **Scale appropriateness**: At 5–10K nodes and 50–100K edges, the entire graph fits in memory.
   NetworkX loads this in milliseconds and runs BFS/DFS in microseconds. We're at a scale where
   developer velocity matters more than graph DB optimizations.
4. **Operational simplicity**: PostgreSQL is a single process with `pg_dump` backups. No JVM, no
   Gremlin Server, no schema management through separate console. This aligns with our <$100/month
   target and no dedicated DevOps constraint.
5. **Natural home for tabular data**: Pony factor stats, contributor logs, SBOM metadata, audit
   trails, API rate-limit state — all naturally live in PostgreSQL tables.
6. **Migration path preserved**: If we outgrow in-memory NetworkX, we can export to TinkerPop with a
   bulk loader. The data model is designed with TinkerPop compatibility in mind.

**Trade-offs accepted**:

- **Intentional technical debt**: If the long-term answer is TinkerPop (and the architecture suggests
  it might be), PostgreSQL + NetworkX is a temporary scaffold. Every query in SQL + NetworkX may need
  to be rewritten in Gremlin later. We're betting the speed-to-ship benefit justifies this future
  cost.
- **Dual representation**: The graph lives in PostgreSQL (source of truth) and NetworkX
  (computation). At this scale, we can reload on every change or build simple invalidation.
- **Shallow team NetworkX experience**: Collective experience of the core team is measured in months,
  not years. However, we have recruited a NetworkX expert and we also have direct access to NetworkX
  maintainers for guidance.

## Data Model

The schema is designed to map naturally to property graphs, facilitating network analytics hand-off
to NetworkX, and enabling [future scaling](/pg-atlas/graph-scaling.md) to a native graph DB. This
schema is minimal and likely incomplete; it'll be expanded based on downstream use-cases, and
eventually performance-oriented benchmark experiments.

### Vertex Types

#### `Project`

**Columns** (vertex properties):

- `canonical_id` (unique key: `ecosystem:package` or `github:org/repo`).
- `display_name`.
- `type` (enum: `pg_root`, `scf_project`, `external_upstream`).
- `activity_status` (enum: `live`, `in-dev`, `discontinued`, `non-responsive`).
- `latest_version` (str: git hash/tag or published version).
- `repo_url` (the ingestion source for git contributor stats).
- `pony_factor` (int: materialized, see below)
- `criticality_score` (int: materialized)
- `releases`: (JSONB array: see below)
- `metadata` (map/JSON property for anything we want to show but not traverse/query).

**Versioned Releases** (for PG roots/upstream):

- Multi-property (e.g. JSONB array) on project vertex for v0.
- Minimal fields: `version`, `release_date`.
- May evolve into a separate vertex type for versions/releases.

**Pony Factor**:

- Separate vertex property for materialized result.
- Store intermediate git contributor stats as edges from contributor vertices to project vertices.

**Activity Status**:

- Enum property: `live`, `in-dev`, `discontinued`, `non-responsive`.
- Baseline signal from SCF Impact Survey results.
- Triangulated/updated via: last tranche completion from OpenGrants and git log recency (public repos
  only).
- For v0 we assume that every external upstream project is `live`.
- Updated via batch job on survey release or OpenGrants ingestion, and per-project on SBOM upload
  triggers.

#### `Contributor`

**Columns** (vertex properties):

- `email_hash` (for reconciliation)
- `name` (commit author)

### Edge Types

#### `depends_on`

- Directed: dependent → dependency between Project vertices.
- Properties: `version_range`, `confidence` (`verified_sbom`, `inferred_shadow`).

#### `contributed_to`

- Directed: Contributor vertex → Project vertex.
- Properties:
  - `number_of_commits` (int: cheap to obtain through `git shortlog -sne`)
  - `current_lines` (int: trickier, through `git blame`; undecided for v0)

### Raw Artifacts

- File storage (separate git repo or lightweight bucket/IPFS) with vertex references.

<!-- QUESTION FOR LEAD: Add diagram of property graph schema, through gdotv.com or Hackolade after
implementation? Mermaid ERD before implementation? -->

## PostgreSQL Backend

We enforce data modeling discipline to ensure clean handoff between PostgreSQL storage and NetworkX
analysis. The key principle: **model everything as a property graph in tables**, avoiding patterns
that work in SQL but create awkward graph structures.

### Schema Design Patterns

**Vertex types** (e.g., `Project`, `Contributor`):

- Columns contain mostly literal data.
- Foreign keys are allowed but should be either joined or omitted during graph construction.
- Use SQLAlchemy models with clear vertex semantics.

**Edge types** (e.g., `depends_on`, `contributed_to`):

- Start with `in_vertex` and `out_vertex` columns (many-to-many relationship).
- Additional columns store literal data (edge properties).
- Avoid foreign keys to other tables; prefer JSONB for multi-valued edge properties if needed.
- Use SQLAlchemy association tables or explicit edge models.

This approach lets us hand analysis off to NetworkX early, rather than doing traversals in PostgreSQL
to construct the graph. We can use existing glue like `nx.from_pandas_edgelist()` or build minimal
custom loaders.

### Classic Traversal Pitfalls to Avoid

If we do need SQL-based traversals (e.g., during SBOM ingestion validation), we'll use standard
mitigations:

- **Transitive Closure Explosion** (duplicate path processing) → Use `DISTINCT` and/or `UNION` at
  each traversal level.
- **Join Re-evaluations** (when joining edge to vertex tables) → Pre-filter edges, then traverse; or
  complete traversal then join (late materialization).
- **Index Fragmentation on UUIDs** → Use sequential integers as primary keys; UUIDs as secondary
  identifiers if needed.

### Incremental Updates

**Single SBOM ingestion** (the most common write operation):

1. Validate SBOM schema and extract dependencies.
2. **Upsert project vertex**: Insert if new, update `latest_version`/`updated_at` if existing.
3. **Bulk operation on edges**:
   - Delete old `depends_on` edges from this project (if re-ingesting).
   - Insert new `depends_on` edges from SBOM dep list.
   - Mark confidence as `verified_sbom`.
4. **Graph invalidation**: Either reload full graph into NetworkX (cheap at this scale) or implement
   incremental graph update (add/remove edges in existing NetworkX instance).
5. **Async recomputation**: Trigger background job to recompute criticality scores for affected nodes
   (this project's upstream ancestors).

**Batch activity flag updates** (quarterly or on SCF Impact Survey release):

1. Load survey results and OpenGrants completion data.
2. **Bulk UPDATE**: `UPDATE projects SET activity_status = ... WHERE canonical_id IN (...)`
3. **Graph reload**: Reload entire graph into NetworkX (still fast at 10K nodes).
4. **Recompute active subgraph projection**: Re-run BFS from all active leaves.
5. **Materialize**: Write updated criticality scores back to `projects.criticality_score`.

**Reference graph sync** (weekly cron job):

1. Fetch updated metadata from npm, crates.io, PyPI, etc.
2. **Bulk upsert**: Insert new discovered nodes, update existing external nodes.
3. Mark confidence as `inferred_shadow`.
4. Full graph reload recommended (or use delta if performance becomes an issue).

### NetworkX Integration Points

**Graph construction**:

```python
import networkx as nx
import pandas as pd

# Load edges from database
edges_df = pd.read_sql("SELECT in_vertex, out_vertex, version_range, confidence FROM depends_on", conn)
projects_df = pd.read_sql("SELECT canonical_id, type, activity_status, ... FROM projects", conn)

# Build directed graph
G = nx.from_pandas_edgelist(
    edges_df,
    source='in_vertex',
    target='out_vertex',
    edge_attr=['version_range', 'confidence'],
    create_using=nx.DiGraph
)

# Attach node attributes
nx.set_node_attributes(G, projects_df.set_index('canonical_id').to_dict('index'))
```

**Active subgraph projection** (see [Metric Computation](/pg-atlas/metric-computation.md)):

- Filter to `activity_status IN ['live', 'in-dev']` leaves (in-degree == 0 in dependency direction).
- BFS/DFS to mark all reachable ancestors.
- Result is boolean mask or subgraph for criticality scoring.

**Persistence after computation**:

```python
# Write computed metrics back to database
for node_id, data in G.nodes(data=True):
    if 'criticality_score' in data:
        conn.execute(
            "UPDATE projects SET criticality_score = %s WHERE canonical_id = %s",
            (data['criticality_score'], node_id)
        )
```

### Deployment Considerations

- **Hosted PostgreSQL**: DigitalOcean Managed Database, AWS RDS, or various free tier options for
  early testing.
- **Connection pooling**: Use SQLAlchemy with asyncpg for FastAPI async support.
- **Migrations**: Alembic for schema versioning.
- **Backups**: Daily automated snapshots via provider, plus periodic `pg_dump` to git repo or S3 for
  auditability.

## Open Questions

- Activity status recalculation frequency/triggers post-v0?
- Add `updated_at` properties to `Project` and `contributed_to`?
- How much historical data do we want to store for x=time-axis charts?
