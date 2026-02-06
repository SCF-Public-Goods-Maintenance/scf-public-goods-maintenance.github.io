---
title: Security & Privacy
parent: PG Atlas Architecture
nav_order: 8
---

# Security & Privacy

## Overview

PG Atlas handles public ecosystem data (dependency graphs, metrics, pony factor from git logs) with
no personal user data in v0 (read-only API/dashboard, no accounts/logins). Security and privacy
design emphasizes defense-in-depth, minimalism, and transparency to protect ecosystem integrity and
community trust.

**Core principles**:

- **Privacy-first**: No tracking of individual users; avoid cookies/session storage.
- **Personal data minimization**: Collect zero PII; git logs processed only for aggregate contributor
  stats (no email exposure).
- **Auditability for maintainers**: Multiple community maintainers access backend — all actions
  logged immutably.
- **CIA triad alignment**:
  - Confidentiality (public data only, but protect ingest sources)
  - Integrity (verified inputs, reproducible metrics)
  - Availability (resilient hosting, DoS mitigation)

**Threat model (v0)**:

- Primary risks:
  - API abuse/DoS
  - ingestion tampering (fake SBOMs)
  - maintainer compromise
- Low risk: Data exfiltration (all public anyway).

## Confidentiality

- **Data classification**: All stored/computed data public by design (open-source manifests, git
  logs, metrics).
- **Ingest protection**: SBOM webhooks validate GitHub signatures (if Action-signed) or repo
  provenance; shadow crawls from trusted registries only.
- **No secrets exposure**: API keys/secrets in environment variables or provider vaults; never in
  repo.
- **Future**: Optional maintainer 2FA/multi-sig for admin actions.

## Integrity

- **Input validation**: Strict schema checks on SBOMs (CycloneDX/SPDX validation libraries); reject
  malformed.
- **Reproducibility**: Raw artifacts retained; metric computation is deterministic.
- **Maintainer actions**: Audit log all admin changes insofar this is possible.
- **Code integrity**: Signed Git commits; dependabot alerts; reproducible builds where possible.

**Open practice**: Public issue tracker for reported discrepancies (e.g., wrong edges) — resolved via
PR.

## Availability

- **DoS mitigation**: API rate limiting (token bucket); CDN caching for static/dashboard.
- **Resilience**: Provider health checks/auto-restart; database backups (daily snapshots).
- **Incident response**: Health endpoint and error monitoring; rollback via git/deploy history.
- **Scalability guardrails**: Single-machine limits enforced; alert on resource spikes.

## Privacy-Specific Measures

- **Web analytics**: [Plausible](https://plausible.io) — cookie-less, privacy-respecting aggregate
  stats only (page views, referrers anonymized).
- **No trackers**: Avoid Google Analytics, Meta pixels, etc.; no client-side fingerprinting.
- **Dashboard**: Local storage optional for preferences (e.g., dark mode) — no server sync.
- **Git log handling**: Obfuscate author emails by hashing or ellipsis redaction.

## Open Questions

- Maintainer access method (SSH keys vs. ~~provider IAM roles~~)?
- Formal incident response playbook needed for v0 launch?
- SBOM signature enforcement level (optional vs. required)?

<!-- FUTURE SELF: Review after first ingestion events — test fake SBOM rejection. -->

<!-- QUESTION FOR LEAD: Any specific compliance needs (e.g., GDPR minimalism already met)? -->
