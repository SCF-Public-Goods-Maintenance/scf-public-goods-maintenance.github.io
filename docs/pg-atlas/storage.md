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
- `type` (enum: `public-good`, `scf-project`).
- `activity_status` (enum: `live`, `in-dev`, `discontinued`, `non-responsive`).
- `git_org_url` (str: GitHub/GitLab organization URL, for discovery and linking).
- `pony_factor` (int: materialized, aggregated across all project repos).
- `criticality_score` (int: materialized, sum of all project repo criticality scores).
- `adoption_score` (float: materialized, composite of repo-level adoption signals).
- `metadata` (JSONB: anything we want to show but not traverse/query). In Python the attribute is
  `project_metadata` to avoid the SQLAlchemy `metadata` name reservation.
- `updated_at` (timestamp).

#### `Repo`

Represents a single git repository or published package within the ecosystem.

**Columns** (vertex properties):

- `canonical_id` (unique key: `ecosystem:package` or `github:org/repo`).
- `display_name`.
- `project_id` (foreign key → `Project`; enforces 1-to-many).
- `latest_version` (str: git hash/tag or published version; **required**). SBOM ingestion should
  always supply this; it is the canonical version identifier for graph snapshot diffs.
- `latest_commit_date` (timestamp: from git log, used for activity triangulation).
- `repo_url` (str: the ingestion source for git contributor stats).
- `visibility` (enum: `public`, `private`)
- `pony_factor` (int: materialized, computed from this repo's contributor stats).
- `criticality_score` (int: materialized, transitive active dependent count for this repo).
- `releases` (JSONB array: `[{"version": "...", "release_date": "..."}]`).
- `adoption_downloads` (int: registry downloads last 30 days, from npm/crates/PyPI).
- `adoption_stars` (int: GitHub stars).
- `adoption_forks` (int: GitHub forks).
- `metadata` (JSONB, including code license from dependent SBOMs or GitHub API). In Python the
  attribute is `repo_metadata` to avoid the SQLAlchemy `metadata` name reservation.
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
- `latest_version` (str: from registry crawl; **required**).
- `repo_url` (str: future extension point, nice to have).
- `criticality_score` (int: materialized, transitive active dependent count for this repo).
- `releases` (JSONB array: `[{"version": "...", "release_date": "..."}]`).
- `updated_at` (timestamp).

#### `Contributor`

**Columns** (vertex properties):

- `email_hash` (SHA-256 digest of the normalized author email, stored as 32-byte BYTEA / 64-char hex
  string via `HexBinary`; used for reconciliation across repos).
- `name` (commit author).

### Edge Types

#### `depends_on`

- Directed: dependent repo → dependency repo (pointing "toward roots").
- Source vertex: `Repo` or `ExternalRepo` (any `RepoVertex`).
- Target vertex: `Repo` or `ExternalRepo` (any `RepoVertex`).
- Stored in the `depends_on` table with **integer foreign keys** to `repo_vertices.id`, which
  provides full referential integrity while allowing a single FK column to reference either subtype.
- Properties:
  - `version_range` (str).
  - `confidence` (enum: `verified-sbom`, `inferred-shadow`).

#### `contributed_to`

- Directed: `Contributor` → `Repo`.
- Properties:
  - `number_of_commits` (int: from `git shortlog -sne`).
  - `first_commit_date` (timestamptz, UTC; **required**).
  - `last_commit_date` (timestamptz, UTC; **required**).

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

Raw SBOM files are stored outside the relational database to avoid bloating the main schema:

- **Local development**: Written to a configurable filesystem path (`ARTIFACT_STORE_PATH`, default
  `./artifact_store`). Files are written atomically (write-to-temp, rename).
- **Production**: Stored on [Storacha](https://storacha.network/) (w3up), a content-addressed
  IPFS-backed store. The CID returned by Storacha is recorded in `sbom_submissions.artifact_path`.
- **Referencing**: `sbom_submissions.artifact_path` holds the storage-backend-specific path (relative
  filesystem path in dev; `storacha://<cid>` in prod). This is intentionally opaque — the API never
  exposes raw artifact bytes.
- **Content integrity**: `sbom_submissions.sbom_content_hash` stores the SHA-256 of the raw bytes as
  32 BYTEA (mapped to a hex string in Python via the `HexBinary` custom TypeDecorator). This enables
  deduplication and tamper detection independently of the storage backend.

### SBOM Submission Audit Table

Every ingest attempt is recorded in `sbom_submissions`:

| Column              | Type                | Notes                                     |
| ------------------- | ------------------- | ----------------------------------------- |
| `id`                | serial PK           |                                           |
| `repository_claim`  | varchar(256)        | `repository` field from the OIDC JWT      |
| `actor_claim`       | varchar(128)        | `actor` field from the OIDC JWT           |
| `sbom_content_hash` | bytea (hex in code) | SHA-256 of raw SBOM bytes                 |
| `artifact_path`     | varchar(1024)       | Path in artifact store; set on submission |
| `status`            | enum                | `pending` → `processed` or `failed`       |
| `error_detail`      | varchar(4096)       | Error message on failure                  |
| `submitted_at`      | timestamptz         | Server-default `now()`                    |
| `processed_at`      | timestamptz         | Null until processing completes           |

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

**`RepoVertex` Joined Table Inheritance (JTI)**:

Both `Repo` and `ExternalRepo` inherit from a common `RepoVertex` base class backed by the
`repo_vertices` table. This table holds the shared identity columns (`id`, `canonical_id`,
`vertex_type` discriminator). Concrete subtypes store their own columns in `repos` and
`external_repos` tables, joined by primary key.

The motivation: edge tables (`depends_on`) carry a single FK column pointing to `repo_vertices.id`,
which gives full referential integrity — a constraint on `in_vertex_id`/`out_vertex_id` correctly
enforces that both endpoints must be known vertices, regardless of subtype. This is exactly the
property-graph "vertex registry" pattern.

```txt
repo_vertices (id PK, canonical_id, vertex_type)
     │ ← FK
repos (id FK ref repo_vertices.id, display_name, project_id FK, visibility, ...)
external_repos (id FK ref repo_vertices.id, display_name, ...)
depends_on (in_vertex_id FK ref repo_vertices.id, out_vertex_id FK ref repo_vertices.id, ...)
```

**Edge types** (e.g., `depends_on`, `contributed_to`):

- Use **integer FK columns** (`in_vertex_id`, `out_vertex_id`) referencing `repo_vertices.id` rather
  than string identifiers. This provides referential integrity and enables efficient JOINs.
- Additional columns store literal data (edge properties).
- Multi-valued edge properties use JSONB if needed.
- SQLAlchemy association tables or explicit edge models.

**Implementation conventions**:

- All timestamps are `DateTime(timezone=True)` (UTC everywhere — no localized datetimes in the
  schema). Python code uses UTC-aware `datetime.datetime` objects.
- `sbom_submissions.sbom_content_hash` is stored as 32-byte BYTEA via a `HexBinary` `TypeDecorator`
  that transparently converts between 64-char hex strings in Python code and compact binary storage
  in PostgreSQL.

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
   - Mark confidence as `verified-sbom`.
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
3. Mark `depends_on` confidence as `inferred-shadow`.
4. Full graph reload recommended (or use delta if performance becomes an issue).

### NetworkX Integration Points

Code examples are only offered as rough sketches. Where we use raw SQL here, we want to rely on
SQLAlchemy in our implementation.

**Graph construction** (repo-level — the primary analysis graph):

```python
import networkx as nx
import pandas as pd

# Load repo-level edges; JOIN repo_vertices to resolve canonical_id strings
# (in_vertex_id/out_vertex_id are integer FKs to repo_vertices.id)
edges_df = pd.read_sql(
    """
    SELECT
        rv_in.canonical_id  AS in_vertex,
        rv_out.canonical_id AS out_vertex,
        d.version_range,
        d.confidence
    FROM depends_on d
    JOIN repo_vertices rv_in  ON rv_in.id  = d.in_vertex_id
    JOIN repo_vertices rv_out ON rv_out.id = d.out_vertex_id
    """,
    conn,
)
repos_df = pd.read_sql(
    "SELECT rv.canonical_id, r.project_id, r.latest_commit_date, "
    "r.pony_factor, r.adoption_downloads, r.adoption_stars "
    "FROM repos r JOIN repo_vertices rv ON rv.id = r.id",
    conn,
)
external_df = pd.read_sql(
    "SELECT rv.canonical_id, er.display_name "
    "FROM external_repos er JOIN repo_vertices rv ON rv.id = er.id",
    conn,
)

# Build directed graph at repo resolution
G = nx.from_pandas_edgelist(
    edges_df,
    source="in_vertex",
    target="out_vertex",
    edge_attr=["version_range", "confidence"],
    create_using=nx.DiGraph,
)

# Attach node attributes for repos and external repos
nx.set_node_attributes(G, repos_df.set_index("canonical_id").to_dict("index"))
nx.set_node_attributes(G, external_df.set_index("canonical_id").to_dict("index"))
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
  early testing. **PostgreSQL 18+**: role names starting with `pg_` are disallowed for superusers —
  use `atlas` (not `pg_atlas`) as the database user.
- **Docker Compose (local dev)**: Use `postgres:18` image; mount the data volume at
  `/var/lib/postgresql` (not `/var/lib/postgresql/data` — the path convention changed in PG 18).
- **Connection pooling**: Use SQLAlchemy with asyncpg for FastAPI async support.
- **Migrations**: Alembic for schema versioning (`pg_atlas/migrations/`). The initial migration
  (`versions/20260302_1440_d10e2f635f77_initial_schema.py`) creates all 8 tables and 6 PostgreSQL
  enum types. The `downgrade()` function explicitly drops enum types — Alembic does not do this
  automatically when dropping tables.
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
- Production artifact storage: Storacha (w3up) is the target — which CID format do we store in
  `sbom_submissions.artifact_path`, and what client library do we use?
