---
title: "OBSRVR Radar"
canonical_id: daoip-5:scf:project:obsrvr_radar
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

Q3 2026 delivered all three committed deliverables for OBSRVR Radar.

There were a few issues that were resolved that made failures invisible that were related to network
scanning and history scanning. For network scanning, there were instances where even though the site
would say that a node was live there was no indication that the scan of that node failed. Even though
the scan failed, we were still able to figure out that a node was validating correctly but there was
no indication to the owner that there was a problem. The other silent failure was related to history
scanning, there were failures in the scanning but those did not appear in any logs. These were
related to protocol updates to upstream packages not producing the desired result.

Radar now reports network safety in close to plain language as possible. The network analysis section
carries a verdict block that answers what halts the network, what could fork it, and what could cut a
node off from it, with each figure linked to an explanation of what it means and why it is that
value. Another invisible issue was related to Network Analysis not running correctly. The analysis
beneath it was repaired and hardened: output parsing now fails loudly instead of returning zero,
analysis levels degrade independently instead of all-or-nothing, and a statistic that cannot be
computed is reported as unknown rather than as a number.

The frontend cleanup is complete. Bootstrap, jQuery, popper.js and Bootstrap Icons were removed, CSS
dropped from 345 kB to 127 kB, and roughly 7,400 lines of unreachable code were deleted after
verifying they were unreachable.

<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

### 2026 Q3

**Scanner Reliability and Readability**

Proof of completion:

Scanner reliability and readability: https://github.com/withObsrvr/stellarbeat/pull/63

History archive cache misconfiguration detection: https://github.com/withObsrvr/stellarbeat/pull/64

Q3 deliverables PR: https://github.com/withObsrvr/stellarbeat/pull/65

Completed work:

- Added structured connection-failure reporting to the network crawler so unreachable peers are
  logged with a cause rather than silently dropped.
- Added overlay protocol probing and typed connection errors to distinguish refused, timed-out,
  protocol-incompatible, and authentication failures.
- Added detection of history archive cache misconfiguration, so an archive served from a stale cache
  is no longer reported as "behind". Three outcomes that were collapsed into one are now
  distinguished: genuinely behind, unreachable, and served from a stale cache.
- Fixed a rollup failure that discarded every scan result before persistence. A nullable column was
  aggregated with `sum()`, which returns null rather than zero when no node reports a value, and the
  NOT NULL target column rejected the row.
- Fixed geo lookups never being retried after failure. Lookups were only performed for nodes whose IP
  had changed, so a node located once during a provider outage stayed without country or ISP data
  indefinitely. This was the root cause of country and ISP analysis returning meaningless results.
  After the fix a single scan went from 4 stored geo records to 226.
- Made FBAS analysis levels degrade independently. Node, organization, country and ISP previously ran
  through a single `Promise.all`, so a failure at one level discarded the results of all four.
- Fixed the nix development shell corrupting `NETWORK_QUORUM_SET`. The shell sourced the `.env`
  files, and shell quote removal turned the value into invalid JSON, so no scan could start inside
  the development environment.
- Added `docs/local-development.md` covering environment setup, the FBAS service image, and a
  troubleshooting section built from the failures encountered this quarter, each listed with the
  symptom that identifies it.

**Plain-Language Network Analysis and FBAS Reliability**

Proof of completion:

Q3 deliverables PR: https://github.com/withObsrvr/stellarbeat/pull/65

Archive hasher update: https://github.com/withObsrvr/stellarbeat/pull/62

Hasher repository: https://github.com/withObsrvr/rs-stellar-history-archive-hasher

Completed work:

- Repaired the main-page network analysis tool, which had never worked. Clicking "Perform analysis"
  threw `DataCloneError` before the worker started, because Vue refs and the shared Node and
  Organization objects were passed to `postMessage` and neither is structured-cloneable. The worker
  serialised its input to JSON regardless, so the callers now serialise once.
- Added a network verdict block to the main page, presenting safety in plain language: what halts the
  network, what could fork the top tier, what could cut a node off from it, the top tier size and
  symmetry, and concentration by organization, ISP and country.
- Implemented the verdict wording as a pure function over scan statistics, covered by 24 tests that
  pin the copy rather than only the numbers.
- Added separate top-tier and network-wide organization safety thresholds. Radar previously computed
  only the top-tier figure while labelling it as network-wide, which was the source of a discrepancy
  reported by the python-fbas author. Both are now computed and displayed.
- Implemented the symmetric top tier check, which had been hardcoded to `false` under a TODO. Every
  visitor had been shown a permanent "top tier is not symmetric, analysis could be slow" warning.
- Rewrote the four FBAS explainers for the reader looking at a number rather than at the analysis
  tool, including the arithmetic that makes the figures actionable, and corrected attribution to
  python-fbas.
- Made the FBAS service output parsers fail loudly. Every parser previously defaulted to zero or an
  empty set when the expected line was missing, so a CLI format change, a crash, and a genuine "no
  result" all arrived as a real-looking answer. The parsers now raise, naming the command and the
  actual output, with fixture tests per format. This caught a live break within hours of landing,
  when a python-fbas sync changed the `min-quorum` output label.
- Stopped using zero to mean "not computed". Splitting-set sizes are nullable end to end. This was
  not cosmetic: the notification system treats a splitting set of zero as total loss of safety and
  notifies subscribers, so a network that became more robust would have raised the alarm.
- Fixed aggregated quorum sets that could require more participants than existed, which produced
  unsatisfiable configurations and a reported safety threshold of zero.
- Updated the history archive hasher to `@withobsrvr/stellar-history-archive-hasher` 0.11.0 and fixed
  the service image build, which could no longer be rebuilt because `python-sat==1.8.dev13` has been
  removed from PyPI.
- Added Playwright end-to-end coverage driving the real UI: the analysis tool running, each verdict
  explainer opening, and the main pages rendering.

**UI Cleanup and Ongoing Maintenance**

Proof of completion:

Q3 deliverables PR: https://github.com/withObsrvr/stellarbeat/pull/65

Navigation styling fix: https://github.com/withObsrvr/stellarbeat/pull/61

Completed work:

- Settled a single design token set. Three palettes had been live at once; the canonical set is now
  surface, border and text tokens for the neutral ground, an accent family for brand, and a signal
  family reserved for severity so that green, amber and red consistently mean safe, fragile and at
  risk.
- Removed Bootstrap, jQuery, popper.js, Bootstrap Icons, and the `@types` packages for jQuery and
  Bootstrap.
- Removed the vendored Tabler UI theme, 63 stylesheet files.
- Reduced CSS from 345 kB to 127 kB. The application used roughly 60 class names from those
  stylesheets, which are now reimplemented on Radar's tokens in about 340 lines, so the remaining
  per-component migration can proceed incrementally.
- Converted the quorum set dialogs from raw Bootstrap markup to the shared modal component. They
  could not open, because Bootstrap's JavaScript was never loaded.
- Deleted roughly 7,400 lines of unreachable code after verifying unreachability, including the
  orphaned node sidebar chain, a 1,360-line unused compatibility layer, and a globally registered
  icon component whose font was never imported.
- Fixed inert controls left behind by the earlier Bootstrap migration, including four information
  buttons in the network analysis tool that set state nothing read.
- Added accessible names to icon-only controls that previously had none.
- Verified with 1,143 unit tests across 243 suites, a clean production build, and Playwright coverage
  of the main pages.

### 2026 Q2

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
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aobsrvr_radar&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aobsrvr_radar)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Aobsrvr_radar&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Aobsrvr_radar)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
