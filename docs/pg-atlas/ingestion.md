---
title: Ingestion
parent: PG Atlas Architecture
nav_order: 2
---

# Ingestion

## Overview

The ingestion layer is responsible for collecting and normalizing data that feeds the dependency
graph and contributor statistics. For v0, ingestion focuses on three primary streams:

1. **SBOM submissions** – explicit dependency declarations from project repos (verification layer).
2. **Reference graph bootstrapping** – automated crawling of public package registries and OpenGrants
   to build an initial graph from known Stellar/Soroban PG roots.
3. **Git contributor logs** – for pony factor calculation (separate but parallel ingestion).

All ingestion writes at **repo resolution**. `Project` vertices are primarily sourced from
OpenGrants; `Repo` vertices are created/updated by SBOM ingestion and registry crawls. Dependencies
outside the Stellar ecosystem are stored as `ExternalRepo` vertices — tracked for blast radius
analysis only, with no project-level data maintained.

The goal is rapid bootstrapping of a meaningful graph while encouraging accurate, ongoing SBOM
contributions. All ingestion pipelines must be idempotent, validate inputs, and handle incremental
updates without full reprocessing.

## SBOM Ingestion

**Source**: GitHub Action workflow run by project teams on PR/merge to main (or tagged releases).
Each SBOM submission is associated with a specific **Repo**, not a project directly.

**Workflow**:

- Teams add a
  [lightweight GitHub Action](https://github.com/SCF-Public-Goods-Maintenance/pg-atlas-sbom-action)
  to their workflows. The action fetches the repo's SPDX 2.3 dependency graph from the
  [GitHub Dependency Graph API](https://docs.github.com/en/rest/dependency-graph/sboms) and submits
  it to the PG Atlas ingestion endpoint, authenticated via a GitHub OIDC token. Supports both public
  and private repos.
- Optional: allow non-GitHub SBOM submissions which are signed with a project key for provenance
  (deferred for v0).

**Authentication**:

The action requests a short-lived GitHub OIDC token (RS256-signed JWT issued by GitHub's OIDC
provider) with the PG Atlas API URL as the audience, and sends it in the `Authorization: Bearer`
header of the submission request. No secrets need to be configured in the calling repository — the
only caller-side requirement is `id-token: write` in the workflow's `permissions` block.

The API verifies the token by:

1. Fetching GitHub's public JWKS from `https://token.actions.githubusercontent.com/.well-known/jwks`.
2. Verifying the RS256 signature and standard claims (`iss`, `exp`, `aud`).
3. Extracting the `repository` claim (`owner/repo`) to establish which repo submitted the SBOM, and
   recording the `actor` (triggering user) for audit purposes.

Both GitHub-hosted and self-hosted runners are supported. The OIDC token in both cases is signed by
GitHub's OIDC provider and contains a `runner_environment` claim (`github-hosted` or `self-hosted`).

**Trust model**: The OIDC token cryptographically proves the _identity_ of the submitting repo — it
guarantees that the submission originated from a workflow running in the context of `owner/repo`,
authorized by a GitHub user with write access. It does **not** independently verify the _content_ of
the submitted SBOM: a workflow author controls the workflow YAML and could in principle modify the
payload before submission. The principal mitigations are: (1) the reference graph cross-check (A8)
flags declared dependencies that diverge from the inferred graph; (2) all submissions are logged with
the `repository` and `actor` claims, making falsification an attributable act; (3) community review
and the public leaderboard create social accountability.

**Processing**:

- Validate SPDX 2.3 format and schema.
- Extract dependencies (package name + version range).
- Map each dependency to a `Repo` (if within-ecosystem) or `ExternalRepo` (if external). Normalize
  ecosystem-specific names (e.g., `soroban-sdk` across crates/npm) to match `canonical_id` format
  (`ecosystem:package`).
- Upsert the submitting `Repo` vertex. If its parent `Project` doesn't exist, create it or flag for
  manual triage.
- Create/update `depends_on` edges **from the submitting repo** to each dependency (`Repo` or
  `ExternalRepo`). Mark confidence as `verified_sbom`.
- Flag conflicts with reference graph (e.g., missing declared deps) for manual review.

**Incentives & Enforcement (v0)**:

- Soft: Bonus points in PG scoring for early/complete submissions.
- Planned: Tie to SCF Build testnet tranche release (preferred over mainnet to capture dependencies
  early).

**Example workflow**:

```yaml
jobs:
  sbom:
    runs-on: ubuntu-latest
    permissions:
      contents: read # for GitHub Dependency Graph API
      id-token: write # for OIDC authentication to PG Atlas
    steps:
      - uses: SCF-Public-Goods-Maintenance/pg-atlas-sbom-action@<full-commit-hash>
```

The `api-url` input defaults to the production PG Atlas endpoint and does not need to be set. The
calling repo must have the GitHub dependency graph enabled.

**Open Questions**:

- Mandatory vs. optional for v0? (Risk: low uptake → sparse graph; mitigation: strong reference graph
  bootstrapping).

## Reference Graph Bootstrapping

**Purpose**: Address low initial SBOM uptake by proactively building a "reference graph" from public
metadata, starting from curated root nodes.

**Sources**:

- [OpenGrants](https://opengrants.daostar.org/system/scf) — primary source for `Project` vertices and
  their metadata (name, status, organization URL).
- npm registry API
- crates.io API
- PyPI JSON API
- Go proxy API
- Optional: deps.dev for cross-ecosystem metadata

<!-- FUTURE SELF: research Open Source Observer architecture and features -->

**Process**:

1. **Bootstrap Project vertices from OpenGrants**: Load SCF-awarded projects as `Project` rows.
   Populate `activity_status` from SCF Impact Survey data when available; default to `non-responsive`
   for projects with no survey response (see
   [Activity Status Update Logic](storage.md#activity-status-update-logic)).
1. **Discover Repos**: From each project's `git_org_url`, enumerate repositories and create `Repo`
   vertices linked to the parent `Project` via `project_id` foreign key.
1. Maintain a curated seed list of known Stellar/Soroban public goods (e.g., `soroban-sdk`,
   `stellar-js-sdk`, `stellar-sdk` on PyPI, common Soroban contracts/libs).
1. Crawl reverse dependencies from registries (who imports these roots) up to 2–3 hops (for
   within-ecosystem only).
1. For each discovered package: create a `Repo` vertex (if within-ecosystem) or `ExternalRepo` vertex
   (if external). Normalize package names to `canonical_id` format (`ecosystem:package`).
1. Create `depends_on` edges. Mark confidence as `inferred_shadow`.
1. Run periodically (weekly for v0) or on triggers (new SCF project approval).

**Boundaries**:

- Only include projects with clear Stellar/Soroban relevance.
- Respect registry rate limits; cache aggressively.

<!-- FUTURE SELF: Document seed list maintenance process (PR-based curation in repo). -->

## Git Contributor Logs

**Source**: Direct git clone of target repositories (triggered on SBOM ingestion or manual curation).
Cloned repos may be LRU-cached to avoid re-cloning on every refresh.

**Process**:

- Parse `git log --format='%aN' | sort | uniq -c | sort -nr` (or equivalent) over the last 12–24
  months.
- Reuse patterns from
  [Scientific Python devstats](https://devstats.scientific-python.org/_generated/scipy/).
- Create/update `Contributor` vertices and `contributed_to` edges pointing to the **Repo** (not
  Project). Edge properties include `number_of_commits`, `first_commit_date`, `last_commit_date`.
- Store computed pony factor on `Repo.pony_factor` (number of contributors responsible for ≥50% of
  commits). Aggregate to `Project.pony_factor` by computing pony factor over the union of unique
  contributors across all project repos (deduplicated by `Contributor.email_hash`).
- Update `Repo.latest_commit_date` from git log — feeds into activity status triangulation (see
  [Activity Status Update Logic](storage.md#activity-status-update-logic)).
- Update on triggers (new release tag, quarterly refresh).

**Open Questions**:

- Time window for pony factor (12 months vs. all history)?
- Weight recent commits higher?

## Validation & Reconciliation

- On SBOM ingest: Compare declared deps against reference graph → flag discrepancies for review.
- Deduplication: Canonical node IDs (`ecosystem:package` for repos, DAOIP-5 URIs for projects).
- Ecosystem boundary: Determine whether each dependency is within-ecosystem (`Repo`) or external
  (`ExternalRepo`). Criteria TBD — initial heuristic: presence in curated seed list or OpenGrants.
- Error handling: Queue failed ingests for manual triage; notify team (via GitHub issue or Sentry?).

## Implementation Notes (v0)

- Use FastAPI endpoint for webhook ingestion.
- Background tasks (Celery or similar) for crawling and git parsing.
- Store raw ingested artifacts (SBOM files, crawl snapshots) in repo or S3/IPFS for auditability.
- All writes target `Repo`, `ExternalRepo`, `Contributor`, and edge tables. `Project` vertices are
  bootstrapped from OpenGrants and updated via survey/OpenGrants pipelines (see
  [Incremental Updates](storage.md#incremental-updates) in Storage).

<!-- QUESTION FOR LEAD: Do we want a diagram here (Mermaid of ingestion flows: SBOM → API →
Validation → Graph Update vs. Reference Crawl → Periodic Job)? -->
