---
title: Operations & Deployment
parent: PG Atlas Architecture
nav_order: 7
---

# Operations & Deployment

## Requirements

PG Atlas operations must balance simplicity, reliability, and low ongoing maintenance for a
community-driven project:

- **Push-to-deploy simplicity**: Git push to main should trigger builds/deploys without manual
  intervention.
- **Minimal DevOps overhead**: Prefer managed services over raw VMs; avoid complex orchestration
  (Kubernetes) for v0.
- **Single-machine capable**: Backend (graph DB + API) fits on one modest instance.
- **Reliable periodic jobs**: Shadow crawls, metric recomputes, adoption signal pulls, activity flag
  batch updates — scheduled (various frequencies) with logging and alerts.
- **Cost control**: Target <$100/month total; free tiers where possible.
- **GitHub-centric where feasible**: Repo already unavoidable for code/SBOM ingestion — leverage
  Actions for jobs.
- **Resilience & monitoring**: Basic health checks, logs, uptime; easy rollback.
- **Community accessibility**: Public endpoints, no heavy vendor lock-in.
- **Frontend hosting**: Static-friendly, fast CDN; at least one Stellar-native or decentralized
  option.

Security: HTTPS enforced, rate limiting, no public writes.

## Deployment Options

### Option 1: DigitalOcean Hybrid (Droplet + App Platform)

**Description**:

- Graph DB (JanusGraph/BerkeleyDB or chosen backend) on a basic Droplet (e.g., $20–40/month
  CPU-optimized).
- FastAPI container on DigitalOcean App Platform (managed PaaS, auto-deploys from GitHub).
- Periodic workers: App Platform background workers or scheduled Droplet cron + supervisor.
- Dashboard: Static build (Next.js or Streamlit exported) on App Platform static site or separate.

**Pros**:

- App Platform excels at push-to-deploy with zero-config scaling/health checks.
- Droplet gives full control for single-node graph DB persistence.
- Unified billing/dashboard.
- Good logging (Papertrail add-on) and monitoring.

**Cons**:

- Two components to manage (Droplet + Apps).
- Workers less elegant (cron vs. managed queues).
- Not GitHub-native for all parts.

### Option 2: GitHub-Maximal

**Description**:

- API + DB in container self-hosted on low-cost + low-carbon VPS (Hetzner/Linode).
- Periodic jobs exclusively in GitHub Actions Workflows (scheduled cron syntax).
- Dashboard: Static site on GitHub Pages (if Streamlit export or Next.js SSG feasible).
- Ingestion webhooks via GitHub App or Actions dispatch.

**Pros**:

- Maximizes GitHub dependency (already required) — unified auth, secrets, logs.
- Actions schedules reliable and free for public repos.
- Pages free/fast for static frontend.
- Zero additional vendors for core ops.

**Cons**:

- Limited runtime for long jobs (Actions timeouts).
- Less managed scaling for API.

### Option 3: Mixed with Stellar-Native Frontend (xlm.sh)

**Description**:

- Backend/API/DB on DigitalOcean App Platform + Droplet (as Option 1) or Fly.io (global edge).
- Periodic jobs via provider schedulers or GitHub Actions.
- Dashboard frontend: Static build hosted on xlm.sh (Stellar-native decentralized/static hosting via
  Soroban or IPFS gateway).

**Pros**:

- XLM.sh!
- Combines managed backend reliability with Stellar-native visibility.

**Cons**:

- xlm.sh limitations unknown.
- Potential latency vs. traditional CDNs.
- Split hosting increases complexity slightly.

### Option 4: Fly.io Full-Stack

**Description**:

- Entire backend (API + DB container) on Fly.io machines (single region or multi for redundancy).
- Workers via Fly's background tasks or cron-like.
- Dashboard on Fly static or integrated.

**Pros**:

- Global low-latency deployment.
- Push-to-deploy simple.
- Free tier generous; scales vertically easily.

**Cons**:

- Less familiar in Stellar community vs. DigitalOcean.
- DB persistence requires volume attachments.

## Auxiliary Services

Auxiliary services support reliable background processing, error monitoring, and operational
visibility. For v0, we prioritize managed or lightweight options to minimize DevOps burden while
ensuring periodic jobs (shadow crawls, metric recomputes, adoption pulls) and error handling work
seamlessly.

### Task Queue & Workers

**Purpose**: Offload long-running tasks (SBOM processing, shadow crawls, full metric recomputes,
activity flag batch updates) from the FastAPI request cycle.

**Components**:

- Celery as task queue/worker framework.
- Redis or RabbitMQ as message broker and result backend (lightweight, in-memory).

**Deployment options**:

- **Self-hosted on main instance** (Droplet/Fly machine): Run Redis container + Celery worker(s) via
  Docker Compose/supervisor. Low cost, full control.
- **Managed**: Redis Cloud (free tier sufficient) or DigitalOcean Managed Redis; Celery workers on
  App Platform background tasks or same host.

**Pros of managed**: Auto-scaling, backups, no persistence worries.

**Cons**: Additional vendor/cost (~$10–20/month).

### Error Monitoring & Performance Tracing

**Purpose**: Capture exceptions, performance bottlenecks (slow API endpoints, long recomputes), and
breadcrumbs for debugging.

**Options**:

- **Sentry.io SaaS** (open-source plan free for public projects): DSN integration in FastAPI,
  automatic error grouping, releases tracking.
- **Self-hosted Sentry**: Possible on Droplet but high overhead (multi-container: Postgres, Redis,
  workers) — not recommended for v0.

**Recommendation**: Start with Sentry.io free tier — zero setup beyond SDK, aligns with community
transparency.

### Additional Services

**Caching**:

- Redis (shared with Celery) for API endpoint caching (leaderboards, node details).
- Cloudflare CDN/proxy.

**Logging**:

- Structured JSON logs to stdout; provider capture (DigitalOcean (Betterstack or Papertrail add-on)
  or Fly logs).

**Monitoring & Alerts**:

- Betterstack, UptimeRobot, or Healthchecks.io for `/health` endpoint pings.
- Provider built-in metrics (DigitalOcean monitoring) or lightweight Prometheus exporter.

**Backups**:

- Database dumps (Postgres pg_dump and/or JanusGraph snapshots) to S3-compatible bucket or repo
  artifacts.
- Automated via cron/GitHub Actions.

<!-- FUTURE SELF: Integrate Sentry performance tracing once API endpoints stabilized. -->

## Open Questions

- Budget ceiling and preferred vendor (DigitalOcean familiarity vs. cheaper alternatives)?
- Periodic job runtime needs (e.g., full recompute duration estimate)?
- xlm.sh feasibility for interactive dashboard (client-side graph rendering size/limits)?
- Any advantages to have billing in USDC through e.g. Rozo.ai or
  [Flashback](https://www.flashback.tech/)?
- Celery beat scheduler location (same worker or separate for reliability)?
- Acceptable cost threshold for managed auxiliaries?
- Alert channels (Discord webhook, email)?

<!-- FUTURE SELF: Benchmark job runtimes once prototype ready; test Actions schedule reliability for
crawls. -->

<!-- QUESTION FOR LEAD: Prioritize cost vs. managed features? Any veto on specific providers? -->
