---
title: Ingestion
parent: PG Atlas Architecture
nav_order: 2
---

# Ingestion

## Overview

The ingestion layer is responsible for collecting and normalizing data that feeds the dependency
graph and contributor statistics. For v0, ingestion focuses on three primary streams:

1. **SBOM submissions** – explicit dependency declarations from SCF-funded projects (verification
   layer).
2. **Reference graph bootstrapping** – automated crawling of public package registries to build an
   initial graph from known Stellar/Soroban PG roots.
3. **Git contributor logs** – for pony factor calculation (separate but parallel ingestion).

The goal is rapid bootstrapping of a meaningful graph while encouraging accurate, ongoing SBOM
contributions. All ingestion pipelines must be idempotent, validate inputs, and handle incremental
updates without full reprocessing.

## SBOM Ingestion

**Source**: GitHub Action workflow run by project teams on PR/merge to main (or tagged releases).

**Workflow**:

- Teams add a lightweight GitHub Action that generates a CycloneDX or SPDX SBOM (JSON format
  preferred for parsing ease).
- Action posts the SBOM to a designated endpoint directly from the GitHub hosted runner. (only
  accepts allow-listed callers)
- Optional: allow non-GitHub SBOM submissions which are signed with a project key for provenance
  (deferred for v0).

**Processing**:

- Validate format and schema.
- Extract dependencies (package name + version range).
- Map to canonical ecosystem nodes (normalize ecosystem-specific names, e.g., `soroban-sdk` across
  crates/npm).
- Create/update "depends-on" edges from the submitting project (leaf) to declared PGs (roots).
- Flag conflicts with reference graph (e.g., missing declared deps) for manual review.

**Incentives & Enforcement (v0)**:

- Soft: Bonus points in PG scoring for early/complete submissions.
- Planned: Tie to SCF Build testnet tranche release (preferred over mainnet to capture dependencies
  early).

<!-- FUTURE SELF: Add example GitHub Action YAML snippet here once finalized. Link to template repo.
-->

**Open Questions**:

- Mandatory vs. optional for v0? (Risk: low uptake → sparse graph; mitigation: strong reference graph
  bootstrapping).
- Which SBOM format to standardize on (CycloneDX JSON recommended for tool support)?

## Reference Graph Bootstrapping

**Purpose**: Address low initial SBOM uptake by proactively building a "reference graph" from public
metadata, starting from curated root nodes.

**Sources**:

- [OpenGrants](https://opengrants.daostar.org/system/scf)
- npm registry API
- crates.io API
- PyPI JSON API
- Go proxy API
- Optional: deps.dev for cross-ecosystem metadata

<!-- FUTURE SELF: research Open Source Observer architecture and features -->

**Process**:

1. Populate the (unconnected) within-ecosystem nodes from OpenGrants SCF Awarded projects.
1. Maintain a curated seed list of known Stellar/Soroban public goods (e.g., `soroban-sdk`,
   `stellar-js-sdk`, `stellar-sdk` on PyPI, common Soroban contracts/libs).
1. Crawl reverse dependencies (who imports these roots) up to 2–3 hops (configurable depth to bound
   scope).
1. Normalize package names and create nodes/edges.
1. Mark reference-derived nodes as "possibly outside of ecosystem" until verified by SBOM.
1. Run periodically (weekly for v0) or on triggers (new SCF project approval).

**Boundaries**:

- Only include projects with clear Stellar/Soroban relevance.
- Respect registry rate limits; cache aggressively.

<!-- FUTURE SELF: Document seed list maintenance process (PR-based curation in repo). -->

## Git Contributor Logs

**Source**: Direct git clone of target repositories (triggered on SBOM ingestion or manual curation).

**Process**:

- Parse `git log --format='%aN' | sort | uniq -c | sort -nr` (or equivalent) over the last 12–24
  months.
- Reuse patterns from
  [Scientific Python devstats](https://devstats.scientific-python.org/_generated/scipy/).
- Store raw contributor counts and computed pony factor (number of contributors responsible for ≥50%
  of lines of code).
- Update on triggers (new release tag, quarterly refresh).

**Open Questions**:

- Time window for pony factor (12 months vs. all history)?
- Weight recent commits higher?

## Validation & Reconciliation

- On SBOM ingest: Compare declared deps against reference graph → flag discrepancies for review.
- Deduplication: Canonical node IDs (e.g., `ecosystem:package-name`).
- Error handling: Queue failed ingests for manual triage; notify team (via GitHub issue or Sentry?).

## Implementation Notes (v0)

- Use FastAPI endpoint for webhook ingestion.
- Background tasks (Celery or similar) for crawling and git parsing.
- Store raw ingested artifacts (SBOM files, crawl snapshots) in repo or S3/IPFS for auditability.

<!-- QUESTION FOR LEAD: Do we want a diagram here (Mermaid of ingestion flows: SBOM → API →
Validation → Graph Update vs. Reference Crawl → Periodic Job)? -->
