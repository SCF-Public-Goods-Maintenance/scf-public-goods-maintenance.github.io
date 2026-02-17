---
title: Graph Scaling
parent: PG Atlas Architecture
nav_order: 10
---

# Graph Scaling

## Native Property Graph DB Options

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

### SurrealDB (embedded or dedicated single-node)

**Overview**: [SurrealDB](https://surrealdb.com/) is a multi-model database (document, graph,
relational) with a SQL-like query language (SurrealQL) that supports graph traversals natively.
Single Rust binary, no JVM, embeddable or client-server.

Introduced by @waldmatias during the v0 storage decision
([issue #2](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/2)).

**Pros**:

- **Unified multi-model**: Graph traversals _and_ tabular data in one system. No NetworkX sidecar, no
  separate tables for pony factor stats — everything in SurrealQL.
- **SQL-like syntax**: Potentially lower learning curve than Gremlin for contributors with SQL
  background. Graph traversals use `<->` and `<-` operators in queries.
- **Single binary deployment**: Aligns perfectly with minimal-DevOps, <$100/month operational
  constraint. No JVM memory overhead.
- **Rust performance**: Low memory footprint, fast concurrent reads, good write throughput.
- **Schema flexibility**: Schemaless by default but supports strict schema definitions. Good for
  rapid iteration.
- **Built-in features**: Change feeds (for real-time updates), full-text search, multiple storage
  backends (memory, file, TiKV).

**Cons**:

- **Zero team experience**: Nobody on the working group has used SurrealDB in production. For a
  system powering funding decisions, this is a meaningful risk.
- **Project maturity**: Post-v1.0 but younger than PostgreSQL (30+ years) or TinkerPop (10+ years).
  Fewer production war stories, smaller community, less StackOverflow coverage.
- **Ecosystem tooling**: Python client exists but is less mature than psycopg3 or SQLAlchemy.
  Integration with FastAPI/Pydantic requires custom work.
- **No TinkerPop compatibility**: If we later migrate to JanusGraph or another TinkerPop backend,
  SurrealQL queries don't port to Gremlin any more easily than SQL + NetworkX (maybe slightly easier
  due to native graph operators).
- **Uncertain scaling path**: While SurrealDB claims horizontal scaling via TiKV backend, production
  evidence at scale is limited compared to Cassandra/Scylla (JanusGraph's proven path).

**When SurrealDB makes sense**:

- If the team is willing to invest learning time upfront.
- If we want to avoid the dual PostgreSQL + NetworkX architecture and prefer native graph traversals
  in storage layer.
- If we're comfortable with a newer tool and can contribute back to the ecosystem (Scientific Python
  ethos).
- As a migration target post-v0 if PostgreSQL + NetworkX hits scaling limits and we want to avoid JVM
  operational overhead.

**Example SurrealQL graph traversal** (for comparison):

```sql
-- Count transitive dependents (criticality)
SELECT count() FROM depends_on<-project<-depends_on<-project
WHERE activity_status = 'live' AND id = $project_id;

-- Active subgraph projection (simplified)
SELECT id, display_name FROM project
WHERE activity_status = 'live'
AND in_degree = 0
RELATE ->depends_on->project;
```

**Decision context**: During the v0 storage discussion, @waldmatias introduced SurrealDB but
recommended Option B (PostgreSQL + NetworkX) for v0, noting that SurrealDB remains an interesting
option to revisit during scaling discussions. The working group agreed this was the pragmatic path:
ship fast with known tools, reevaluate (TinkerPop vs. SurrealDB vs. PostgreSQL extensions) when we
hit actual scaling constraints.

## Recommended Path

Assume **JanusGraph + BerkeleyDB** for detailed implementation:

- Best native graph performance for metrics (transitive counts, active subgraph).
- Per-project updates: Gremlin transactions for edge/vertex changes.
- Batch activity updates: Scripted Gremlin or bulk load for flag flips.
- Pony factor: Materialize on repo vertices but store intermediate git contributor stats as an edge
  type or in a separate data structure.

## Migration & Extensibility

The first 3 options preserve TinkerPop compatibility:

- Start with chosen single-node → add distributed backend later if needed.
- Export path: Gremlin bulk dump or standard serialization. Traversals stay in Gremlin and won't need
  a major port/rewrite later on.

We can investigate adding a TinkerPop-compatible interface to SurrealDB, which would allow us to
write Gremlin in Python without adding a JVM dependency.
