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
to NetworkX, and enabling [future scaling](graph-scaling.md) to a native graph DB. This schema is
minimal and likely incomplete; it'll be expanded based on downstream use-cases, and eventually
performance-oriented benchmark experiments.

### Core Modeling Decision: Project vs. Repo

A common assumption is 1 project = 1 repo/package. In practice, many projects span multiple
repositories (e.g., an SDK with separate client, server, and CLI repos). All ingestion (SBOMs, git
logs, registry crawls) happens at the **repo** resolution, but funding decisions and public goods
scoring happen at the **project** level.

We model this as two separate vertex types with a **one-to-many** relationship: one `Project` has
many `Repo` vertices. In PostgreSQL, this is enforced via a foreign key on the `repos` table pointing
to `projects`, rather than a separate association table — enforcing the 1-to-many constraint at the
schema level.

**External upstream repos** (dependencies outside the Stellar ecosystem that we track for blast
radius analysis) are stored in a separate `ExternalRepo` table. We don't maintain project-level data
for these — they exist only as dependency targets for graph analysis.

The dependency graph operates at two levels:

- **Repo-level `depends_on` edges**: The raw truth from SBOMs and registry crawls. All ingestion
  writes here.
- **Project-level dependencies**: Derived by aggregating repo-level edges. In the dashboard, we show
  project-to-project dependencies by default, with the option to drill down to repo-level detail.

### Vertex Types

#### `Project`

Represents a funded project or recognized public good in the Stellar/Soroban ecosystem. Sourced
primarily from OpenGrants.

**Columns** (vertex properties):

- `canonical_id` (unique key: DAOIP-5 URI, e.g. `daoip-5:stellar:project:stellarcarbon`).
- `display_name`.
- `type` (enum: `pg_root`, `scf_project`).
- `activity_status` (enum: `live`, `in-dev`, `discontinued`, `non-responsive`).
- `git_org_url` (str: GitHub/GitLab organization URL, for discovery and linking).
- `pony_factor` (int: materialized, aggregated across all project repos).
- `criticality_score` (int: materialized, sum of all project repo criticality scores).
- `adoption_score` (float: materialized, composite of repo-level adoption signals).
- `metadata` (JSONB: anything we want to show but not traverse/query).
- `updated_at` (timestamp).

#### `Repo`

Represents a single git repository or published package within the ecosystem.

**Columns** (vertex properties):

- `canonical_id` (unique key: `ecosystem:package` or `github:org/repo`).
- `display_name`.
- `project_id` (foreign key → `Project`; enforces 1-to-many).
- `latest_version` (str: git hash/tag or published version).
- `latest_commit_date` (timestamp: from git log, used for activity triangulation).
- `repo_url` (str: the ingestion source for git contributor stats).
- `visibility` (enum: `public`, `private`)
- `pony_factor` (int: materialized, computed from this repo's contributor stats).
- `criticality_score` (int: materialized, transitive active dependent count for this repo).
- `releases` (JSONB array: `[{"version": "...", "release_date": "..."}]`).
- `adoption_downloads` (int: registry downloads last 30 days, from npm/crates/PyPI).
- `adoption_stars` (int: GitHub stars).
- `adoption_forks` (int: GitHub forks).
- `metadata` (JSONB, including code license from dependent SBOMs or GitHub API).
- `updated_at` (timestamp).

#### `ExternalRepo`

Represents an upstream dependency outside the Stellar/Soroban ecosystem. Tracked for blast radius
analysis only — no project-level data maintained. We don't need to model dependencies between
external repos. SBOM ingestion from Project repos will give us either direct or transitive
dependencies, depending on the manifest format. Within-ecosystem criticality is tracked to show
interesting targets for blast radius analysis.

**Columns**:

- `canonical_id` (unique key: `ecosystem:package`, e.g. `npm:express`).
- `display_name`.
- `latest_version` (str: from registry crawl).
- `repo_url` (str: future extension point, nice to have).
- `criticality_score` (int: materialized, transitive active dependent count for this repo).
- `releases` (JSONB array: `[{"version": "...", "release_date": "..."}]`).
- `updated_at` (timestamp).

#### `Contributor`

**Columns** (vertex properties):

- `email_hash` (for reconciliation across repos).
- `name` (commit author).

### Edge Types

#### `depends_on`

- Directed: dependent repo → dependency repo (pointing "toward roots").
- Source vertex: `Repo`.
- Target vertex: `Repo` or `ExternalRepo`.
- Properties:
  - `version_range` (str).
  - `confidence` (enum: `verified_sbom`, `inferred_shadow`).

#### `contributed_to`

- Directed: `Contributor` → `Repo`.
- Properties:
  - `number_of_commits` (int: from `git shortlog -sne`).
  - `current_lines` (int: from `git blame`; undecided for v0).
  - `first_commit_date` (timestamp).
  - `last_commit_date` (timestamp).

### Activity Status Update Logic

The `activity_status` of projects follows a defined update cascade with multiple data sources at
different temporal resolutions:

**Primary source**: SCF Impact Survey (yearly). Provides baseline classification:

- Survey response → `live`, `in-dev`, or `discontinued`.
- No response for a project loaded from OpenGrants → `non-responsive`.

**Higher-resolution updates** (from OpenGrants completion % and repo `latest_commit_date`):

- `in-dev` → `live`: When OpenGrants completion percentage reaches 100%.
- `discontinued` → `live`: Upon new git commits detected in any associated repo.
- `discontinued` → `in-dev`: New commit, when OpenGrants completion percentage < 100.
- `non-responsive` → `live`: Upon new git commits detected in any associated repo.
- `non-responsive` → `in-dev`: New commit, when OpenGrants completion percentage < 100.

**Intentionally not automated**: We **do not** mark `live` or `in-dev` projects as `discontinued`
based on a lack of git activity. Stable, mature tools may have long periods without commits. We wait
for the next survey cycle to re-classify downward.

The precise status update logic is not yet finalized — we want to test it once we can load data from
all sources (survey, OpenGrants, git logs).

### Raw Artifacts

- File storage (separate git repo or lightweight bucket/IPFS) with vertex references.

<!-- TODO: Add Mermaid ERD or gdotv.com diagram of property graph schema. -->

## PostgreSQL Backend

We enforce data modeling discipline to ensure clean handoff between PostgreSQL storage and NetworkX
analysis. The key principle: **model everything as a property graph in tables**, avoiding patterns
that work in SQL but create awkward graph structures.

### Schema Design Patterns

**Vertex types** (e.g., `Project`, `Repo`, `ExternalRepo`, `Contributor`):

- Columns contain mostly literal data.
- The `Repo.project_id` foreign key enforces the 1-to-many Project→Repo relationship. During graph
  construction, this is either joined to attach project metadata to repo nodes, or used to build a
  `part_of` edge in the NetworkX graph.
- `ExternalRepo` is a separate table — these nodes participate in `depends_on` edges but carry no
  project-level data.
- Use SQLAlchemy models with clear vertex semantics.

**Edge types** (e.g., `depends_on`, `contributed_to`):

- Start with `in_vertex` and `out_vertex` columns (many-to-many relationship).
- Additional columns store literal data (edge properties).
- Avoid foreign keys to/from other tables; prefer JSONB for multi-valued edge properties if needed.
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
2. **Upsert repo vertex**: Insert `Repo` if new, update `latest_version`/`updated_at` if existing. If
   the repo's parent `Project` doesn't exist, create it or flag for manual triage.
3. **Upsert dependency targets**: For each dependency in the SBOM, upsert into `Repo` or
   `ExternalRepo` depending on whether it's within-ecosystem.
4. **Bulk operation on edges**:
   - Delete old `depends_on` edges from this repo (if re-ingesting).
   - Insert new `depends_on` edges from SBOM dep list.
   - Mark confidence as `verified_sbom`.
5. **Graph invalidation**: Either reload full graph into NetworkX (cheap at this scale) or implement
   incremental graph update (add/remove edges in existing NetworkX instance).
6. **Async recomputation**: Trigger background job to recompute criticality scores for affected repos
   (this repo's upstream ancestors), then aggregate to project level.

**Batch activity status updates** (yearly on SCF Impact Survey release, plus higher-frequency
triangulation):

1. Load survey results → set `activity_status` on `Project` rows.
2. Load all projects from OpenGrants → mark `non-responsive` where no survey response exists.
3. Load OpenGrants completion percentages → apply status upgrade rules (see Activity Status Update
   Logic above).
4. Propagate project status to child repos.
5. **Graph reload**: Reload entire graph into NetworkX.
6. **Recompute active subgraph projection**: Re-run BFS from all active leaves.
7. **Materialize**: Write updated criticality scores to `repos.criticality_score`, then aggregate to
   `projects.criticality_score`.

**Git log refresh** (periodic, per-repo):

1. Clone (or pull repo if we want to LRU cache), parse `git log` for contributor stats.
2. Update `Repo.latest_commit_date`.
3. Check activity status upgrade rules (e.g., `discontinued` → `live` on new commits).
4. Upsert `Contributor` vertices and `contributed_to` edges.
5. Recompute `Repo.pony_factor`, then aggregate to `Project.pony_factor`.

**Reference graph sync** (weekly cron job):

1. Fetch updated metadata from npm, crates.io, PyPI, etc.
2. **Bulk upsert**: Insert new discovered repos into `Repo` (if within-ecosystem) or `ExternalRepo`.
3. Mark `depends_on` confidence as `inferred_shadow`.
4. Full graph reload recommended (or use delta if performance becomes an issue).

### NetworkX Integration Points

Code examples are only offered as rough sketches. Where we use raw SQL here, we want to rely on
SQLAlchemy in our implementation.

**Graph construction** (repo-level — the primary analysis graph):

```python
import networkx as nx
import pandas as pd

# Load repo-level edges (includes edges to ExternalRepo targets)
edges_df = pd.read_sql(
    "SELECT in_vertex, out_vertex, version_range, confidence FROM depends_on", conn
)
repos_df = pd.read_sql(
    "SELECT canonical_id, project_id, activity_status, latest_commit_date, "
    "pony_factor, adoption_downloads, adoption_stars FROM repos", conn
)
external_df = pd.read_sql(
    "SELECT canonical_id, display_name FROM external_repos", conn
)

# Build directed graph at repo resolution
G = nx.from_pandas_edgelist(
    edges_df,
    source='in_vertex',
    target='out_vertex',
    edge_attr=['version_range', 'confidence'],
    create_using=nx.DiGraph
)

# Attach node attributes for repos and external repos
nx.set_node_attributes(G, repos_df.set_index('canonical_id').to_dict('index'))
nx.set_node_attributes(G, external_df.set_index('canonical_id').to_dict('index'))
```

**Project-level graph** (derived, for dashboard visualization):

```python
# Build project-level dependency graph by collapsing repo edges
project_edges = set()
for u, v in G.edges():
    u_proj = G.nodes[u].get('project_id')
    v_proj = G.nodes[v].get('project_id')
    if u_proj and v_proj and u_proj != v_proj:
        project_edges.add((u_proj, v_proj))

P = nx.DiGraph()
P.add_edges_from(project_edges)
# Attach project-level attributes from projects table
```

**Active subgraph projection** (see [Metric Computation](metric-computation.md)):

- Filter to `project.activity_status IN ('live', 'in-dev')` repo leaves (in-degree == 0 in dependency
  direction).
- BFS/DFS to mark all reachable ancestors.
- Result is boolean mask or subgraph for criticality scoring.

**Persistence after computation**:

```python
# Write computed metrics back to repos table
for node_id, data in G.nodes(data=True):
    if 'criticality_score' in data:
        conn.execute(
            "UPDATE repos SET criticality_score = %s WHERE canonical_id = %s",
            (data['criticality_score'], node_id)
        )

# Aggregate to project level
conn.execute("""
    UPDATE projects p SET
        criticality_score = (SELECT SUM(r.criticality_score) FROM repos r WHERE r.project_id = p.id),
        pony_factor = ...  -- aggregation TBD, see metric-computation.md
    WHERE p.id IN (SELECT DISTINCT project_id FROM repos WHERE criticality_score IS NOT NULL)
""")
```

### Deployment Considerations

- **Hosted PostgreSQL**: DigitalOcean Managed Database, AWS RDS, or various free tier options for
  early testing.
- **Connection pooling**: Use SQLAlchemy with asyncpg for FastAPI async support.
- **Migrations**: Alembic for schema versioning.
- **Backups**: Daily automated snapshots via provider, plus periodic `pg_dump` to git repo or S3 for
  auditability.

## Open Questions

- How much historical data do we want to store for time-axis charts? (snapshot tables? temporal
  columns?)
- Should `ExternalRepo` gain adoption signals (downloads/stars) for richer blast radius context?
- Project-level pony factor aggregation method: sum of unique contributors across all repos, or
  weighted by repo criticality?
- Do we need a `part_of` edge in NetworkX, or is the `project_id` foreign key sufficient for all
  analysis needs?
- For Repo `canonical_id`, should we use SBOM-style (SPDX-format) identifiers `.name` and
  `.packages[].externalRefs[].referenceLocator`, where applicable?
