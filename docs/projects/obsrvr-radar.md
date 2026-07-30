---
title: "OBSRVR Radar"
parent: Public Good Projects
proposal_issue: 109
proposer: tmosleyIII
category: "Infrastructure Monitoring"
budget: "20000"
---

# OBSRVR Radar

<!-- markdownlint-disable MD036 -->

_A Stellar network explorer that turns validator, quorum, organization, and history archive data into
plain-language network health insights._

<!-- markdownlint-enable MD036 -->

|                      |                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| **Category**         | Infrastructure Monitoring                                                                          |
| **Website**          | <https://radar.withobsrvr.com>                                                                     |
| **Repository**       | <https://github.com/withObsrvr/stellarbeat>                                                        |
| **First Released**   | June 2025                                                                                          |
| **Intake**           | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/85> |
| **Budget Requested** | 20000                                                                                              |

## Project Description

<!-- markdownlint-disable MD034 -->

OBSRVR Radar is a Stellar network explorer and monitoring tool. It helps validators, infrastructure
operators, ecosystem teams, and network observers understand what is happening across the Stellar
public network and testnet.

Radar tracks validator reachability, organization health, quorum relationships, history archive
status, protocol/version alignment, and network risk. It combines a network crawler, backend scanner
services, frontend explorer views, history archive verification, organization/TOML processing, and
FBAS analysis tooling.

The long-term goal is to make Stellar network health understandable to humans, not only technically
observable.

Radar also uses OBSRVR's `rs-stellar-history-archive-hasher`, published as
`@withobsrvr/stellar-history-archive-hasher`, to support history archive verification.

<!-- markdownlint-enable MD034 -->

## Team & Experience

<!-- markdownlint-disable MD034 -->

Tillman Mosley III, OBSRVR, maintains Radar and related Stellar infrastructure tooling.

- GitHub: https://github.com/withObsrvr
- Discord: tillmanmosley
- LinkedIn: https://www.linkedin.com/in/tillmanmosleyiii/

I work on Stellar observability, validator operations, history archive tooling, data infrastructure,
and network analysis. Related work includes Radar/Stellarbeat maintenance, Stellar history archive
scanner support, validator diagnostics, DigitalOcean deployment automation, and the archive hasher
used by Radar's scanner.

OBSRVR's broader Stellar work focuses on making Stellar network and ledger data easier to operate,
inspect, and understand. Radar fits into that work as the network-health and validator-observability
layer.

<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->

Q2 2026 was mostly an operational-readiness quarter for OBSRVR Radar. I did not complete the full
roadmap I originally wanted for Q2. Larger product goals like design-token migration, data lake
analytics, and deeper trust graph improvements are still open and should carry into Q3.

The work that did land was still important. Radar stayed current with Stellar dependencies and
protocol defaults, deployments became more reliable, staging moved away from a permanent environment
toward an ephemeral pull-request lifecycle, history archive scanning became more resilient, the
archive hasher dependency was refreshed, and the UI gained targeted improvements for validator and
organization pages.

The main impact was reducing operational risk. Radar is now easier to build and deploy, better
aligned with current Stellar dependencies, more resilient when scanning newer history archive
formats, and more useful for operators inspecting validator and organization status.

<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

Maintenance, Protocol, and Dependency Updates

Proof of completion:

Q2 Radar PRs:
https://github.com/withObsrvr/stellarbeat/pulls?q=is%3Apr+is%3Amerged+merged%3A2026-04-01..2026-06-30

Completed work:

- Upgraded pnpm from 9.15.0 to 10.33.0.
- Updated Stellar protocol defaults to ledger protocol version 25, overlay version 40, and Stellar
  Core version 25.0.0.
- Upgraded `@stellar/stellar-base` to 15.0.0.
- Upgraded `@withobsrvr/stellar-history-archive-hasher` to 0.9.1.
- Updated package manifests and lockfile state across the app.
- Added build allowlisting for native/build packages such as `@swc/core`, `esbuild`, and
  `sodium-native`.

History Scanner Compatibility and Reliability

Proof of completion:

Q2 Radar PRs:
https://github.com/withObsrvr/stellarbeat/pulls?q=is%3Apr+is%3Amerged+merged%3A2026-04-01..2026-06-30

Completed work:

- Added support for `hotArchiveBuckets` in history archive state version 2.
- Included both live buckets and hot archive buckets when hashing archive state.
- Added regression tests for v1 and v2 archive hashing.
- Added fallback behavior when v2 archive states omit `hotArchiveBuckets`.
- Changed corrupted gzip bucket handling so Radar records a structured error and continues the scan.
- Added test coverage for corrupted bucket handling.

Archive Hasher Maintenance

Proof of completion:

Hasher repository: https://github.com/withObsrvr/rs-stellar-history-archive-hasher

Q2 version update commit:
https://github.com/withObsrvr/rs-stellar-history-archive-hasher/commit/3c04677f80d946d9900d2ef98d4b1d74dc663d74

Completed work:

- Updated the archive hasher crate version from 0.9.0 to 0.9.1.
- Updated Radar to use `@withobsrvr/stellar-history-archive-hasher` 0.9.1.
- Kept the hasher usable from JavaScript/WASM and Rust.
- Preserved the hashing functions Radar uses for Stellar history archive verification.

Deployment and Staging Improvements

Proof of completion:

Q2 Radar PRs:
https://github.com/withObsrvr/stellarbeat/pulls?q=is%3Apr+is%3Amerged+merged%3A2026-04-01..2026-06-30

Completed work:

- Moved staging tfvars generation into a shared script.
- Added a staging destroy workflow after merged PRs.
- Added separate destroy plan/apply handling.
- Added encrypted Terraform destroy plan artifacts.
- Restricted staging deploy/planning to pull request workflows.
- Began shifting staging from a permanent deployment to an ephemeral PR lifecycle.
- Added `DEPLOYED_SHA` wiring so DigitalOcean App Platform redeploys reliably when code changes.
- Added contact/legal frontend environment variables.
- Moved Python FBAS service deployment toward a prebuilt Docker image model.

Frontend and Operator Usability

Proof of completion:

Q2 Radar PRs:
https://github.com/withObsrvr/stellarbeat/pulls?q=is%3Apr+is%3Amerged+merged%3A2026-04-01..2026-06-30

Completed work:

- Added node detail fields for history URL, overlay version, overlay minimum version, ledger version,
  and externalize lag.
- Improved organization warning behavior.
- Added warning badges and tooltips to organization validator lists.
- Improved social/contact link tooltip handling.
- Added `docs/node-connectivity-test.sh`.
- The diagnostic script checks DNS, TCP connectivity, HTTP proxy issues, and Stellar Core admin API
  availability.

<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

Q3 will continue the goal of making Radar easier to operate and easier to understand.

The first priority is scanner reliability and observability related to both network scanning and
history archive scanning. Radar needs to crawl nodes, check archive status, detect version drift, and
explain failures clearly.

The second priority is network analyzer updates and plain-language network analysis. There are issues
with the current FBAS analysis tool in the UI. The main-page network analysis tool depends on this
FBAS pipeline, so improving the plain-language network analysis also requires fixing and hardening
the underlying analysis path.

The third priority is frontend cleanup and product polish. This includes finishing Bootstrap removal,
improving design-token usage, and making validator and organization views easier to understand.

This benefits the Stellar ecosystem by giving validators, infrastructure operators, and ecosystem
participants a clearer view of network health. Instead of requiring users to interpret raw quorum
data themselves, Radar should surface practical explanations and let users drill into the technical
details when needed.

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

Scanner Reliability and Readability

Improve network and history scanner reliability by surfacing more silent errors and making scan
results easier to understand.

Scope:

- Improve logs for cases where the scanner cannot connect to known peers.
- Add alerting or notification paths for repeated scanner failures that currently only show in logs.
- Improve operator docs for known peers, crawler rejection, and validator reachability.
- Add additional scanning node resources.

Ecosystem value:

More reliable scanner operations give validators, ecosystem teams, and network observers a more
dependable view of validator and archive health.

Measure:

Terraform/App Platform updates, scanner health or monitoring PRs, additional scanner resources where
needed, and updated operational documentation.

Plain-Language Network Analysis and FBAS Reliability

Build a human-readable analysis layer for Radar and fix the underlying FBAS/network-analysis path it
depends on. The network analysis tool on the main page currently depends on the FBAS analysis
pipeline, so the plain-language verdict work has to include reliability and compatibility updates to
that analysis layer.

Scope:

- Repair and harden the network analysis tool on the main page.
- Add plain-language explanations to the main-page network analysis.
- Update the FBAS analysis integration that powers liveness, safety, top-tier, blocking-set, and
  splitting-set results.
- Keep Stellar Core/protocol/overlay defaults current where they affect network analysis.
- Complete and validate Protocol 27 archive hasher alignment where it affects Radar's scanner and
  analysis path.

Ecosystem value:

This makes network safety and quorum information useful to more people. Validators and ecosystem
teams should not need to be FBAS experts to understand whether the network is healthy, fragile, or at
risk.

Measure:

Working main-page network analysis, updated FBAS-backed liveness and safety results, network verdict
UI in Radar, plain-language interpretation backed by scan/FBAS results, updated copy and tooltips,
archive hasher/protocol compatibility PRs where needed, screenshots or demo of the verdict flow, and
passing CI.

UI Cleanup and Ongoing Maintenance

Finish frontend cleanup work that carried forward from Q2 and keep Radar current with Stellar
protocol, dependency, and deployment changes.

Scope:

- Remove remaining Bootstrap usage where practical.
- Normalize detail pages, warnings, badges, tooltips, and graph styling.
- Continue polishing validator and organization detail pages.
- Track Stellar SDK/base package and protocol changes.

Ecosystem value:

A cleaner and more consistent UI makes Radar easier to use and easier to maintain. Keeping
dependencies and protocol settings current keeps Radar useful as the Stellar network evolves.

Measure:

Bootstrap removal PRs, maintenance PRs, dependency/protocol update PRs, and passing frontend
build/tests.

<!-- markdownlint-enable MD034 -->

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aobsrvr_radar&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aobsrvr_radar)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aobsrvr_radar&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aobsrvr_radar)
[![Criticality](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aobsrvr_radar&query=%24.criticality_score&label=Criticality&color=E5484D)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aobsrvr_radar)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aobsrvr_radar&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aobsrvr_radar)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aobsrvr_radar&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aobsrvr_radar)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
