---
title: Graph Scaling
parent: PG Atlas Architecture
nav_order: 10
---

# Graph Scaling

## Current Architecture

PG Atlas operates with PostgreSQL 18 + NetworkX for graph storage and computation:

- **Storage** — PostgreSQL tables
- **Computation** — NetworkX in-memory graphs for metric calculation projections)
- **Scale** — Fits comfortably in RAM; full metrics recomputation in under a minute

This hybrid approach balances simplicity (single managed database, familiar SQL) with performance
(efficient in-memory graph algorithms).

**Scaling characteristics**:

- **Read scaling** — PostgreSQL read replicas for API query distribution
- **Write scaling** — Single-node PostgreSQL handles current ingestion volume (bootstrap weekly,
  sbom-queue hourly, gitlog every 3 days)
- **Computation scaling** — NetworkX loads active subgraph into memory; O(nodes + edges) for
  traversals

When growth exceeds single-node PostgreSQL capabilities, scaling options include native graph
databases and distributed systems.

## Native Property Graph Databases

### JanusGraph (BerkeleyDB backend, single-node)

**Pros**:

- Native TinkerPop/Gremlin — optimal for traversals (active subgraph upstream propagation) and OLAP
  batch jobs.
- BerkeleyDB is embeddable/file-based — true zero-cluster persistence, low overhead.
- Efficient indexed writes for per-project updates; supports batch transactions.
- Proven for property graphs with versioning/multi-properties.
- Seamless future scaling (swap to Cassandra/Scylla).

**Cons**:

- Java ecosystem — communication between JVM and FastAPI/Procrastinate provides friction.
- Slightly higher memory footprint than pure relational for small graphs.

### Sqlg (over PostgreSQL)

**Pros**:

- Gremlin queries on familiar relational backend — no new infrastructure.
- PostgreSQL excels at mixed workloads: graph edges + tabular audit records in separate schemas.
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
- Scaling path less standardized than JanusGraph.

## SurrealDB

**Overview**: [SurrealDB](https://surrealdb.com/) is a multi-model database (document, graph,
relational) with a SQL-like query language (SurrealQL) that supports graph traversals natively.
Single Rust binary, no JVM, embeddable or client-server.

Introduced by [@waldmatias](https://github.com/waldmatias) during the v0 storage decision
([issue #2](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/2)).

**Pros**:

- **Unified multi-model**: Graph traversals _and_ tabular data in one system. No NetworkX sidecar, no
  separate tables for audit records — everything in SurrealQL.
- **SQL-like syntax**: Potentially lower learning curve than Gremlin for contributors with SQL
  background. Graph traversals use `<->` and `<-` operators in queries.
- **Single binary deployment**: Aligns perfectly with minimal-DevOps constraint. No JVM memory
  overhead.
- **Rust performance**: Low memory footprint, fast concurrent reads, good write throughput.
- **Schema flexibility**: Schemaless by default but supports strict schema definitions. Good for
  rapid iteration.
- **Built-in features**: Change feeds (for real-time updates), full-text search, multiple storage
  backends (memory, file, TiKV).

**Cons**:

- **Zero team experience**: No PG Atlas contributors have used SurrealDB in production. For a system
  that factors into funding decisions, this is a meaningful risk.
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

**Decision context**: During the v0 storage discussion, [@waldmatias](https://github.com/waldmatias)
introduced SurrealDB but recommended Option B (PostgreSQL + NetworkX) for v0, noting that SurrealDB
remains an interesting option to revisit during scaling discussions. The team agreed this was the
pragmatic path: ship fast with known tools, reevaluate (TinkerPop vs. SurrealDB vs. PostgreSQL
extensions) when we hit actual scaling constraints.

## Migration Decision Criteria

Consider migrating from PostgreSQL + NetworkX when:

- **Graph size** — Exceeds 100K nodes or in-memory computation time > 5 minutes
- **Query complexity** — Deep traversals (>5 hops) become performance bottlenecks
- **Real-time requirements** — Need low-latency transitive queries via API (not pre-computed)
- **Distributed needs** — Multi-region deployment or horizontal scaling required

**Current assessment** (after Build Award completion): PostgreSQL + NetworkX meets all performance
requirements. No immediate migration needed.

## Recommended Migration Path

When scaling becomes necessary:

1. **JanusGraph + BerkeleyDB** (single-node) — Migrate to TinkerPop/Gremlin for native graph
   traversals while maintaining single-node simplicity
2. **JanusGraph + Cassandra/Scylla** (distributed) — Scale horizontally when BerkeleyDB limits
   reached
3. **Alternative: SurrealDB** — Consider if multi-model database appeals and team is willing to
   invest in newer ecosystem

The first two options preserve TinkerPop compatibility:

- Start with chosen single-node → add distributed backend later if needed.
- Export path: Gremlin bulk dump or standard serialization.
- Traversals stay in Gremlin — no major rewrite when scaling

We can investigate adding a TinkerPop-compatible interface to SurrealDB, which would allow us to
write Gremlin in Python without adding a JVM dependency.
