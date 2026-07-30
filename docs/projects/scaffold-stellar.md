---
title: "Stellar Scaffold"
parent: Public Good Projects
proposal_issue: 62
proposer: chadoh
category: "Developer Experience"
budget: "50000"
---

# Stellar Scaffold

_Go from idea to app faster with a custom, pluggable CLI; a multi-framework template system; and a
customizable, modern frontend._

|                      |                                            |
| -------------------- | ------------------------------------------ |
| **Category**         | Developer Experience                       |
| **Website**          | <https://scaffoldstellar.org/>             |
| **Repository**       | <https://github.com/stellar-scaffold/cli/> |
| **First Released**   | May 2025                                   |
| **Intake**           | soft-launch                                |
| **Budget Requested** | 50000                                      |

## Project Description

Stellar Scaffold is an open-source developer toolkit for building decentralized applications (dApps)
and smart contracts on the Stellar blockchain. It helps developers go from idea to working full-stack
dApp faster by providing CLI tools, reusable contract templates, first-class integration with Stellar
Registry (now incubated out into its own project), and modern, customizable frontend templates for
multiple JS frameworks.

## Team & Experience

Stellar Scaffold is built and maintained by **The Aha Company** (formerly Aha Labs), a team of 10+
senior engineers deeply embedded in the Stellar ecosystem.

## Early Soroban origin

In 2022 (before Soroban had a name) SDF already had a clear ambition: launch their upcoming smart
contract platform with a “batteries-included” developer experience. The gap was execution capacity:
there was no in-house team available to design and implement the developer workflows needed to make
that promise real. Tyler van der Hoeven went to major blockchain conferences to find the right team,
and identified **The Aha Company** as the team with the right combination of product mindset and deep
technical ability to “install the batteries.”

## Foundational Stellar developer workflows we designed and shipped

We envisioned, architected, and implemented several of the workflows that have become core to Soroban
development on Stellar, including:

- **Stellar CLI smart contract workflows,** such as the `contract invoke` behavior and associated
  developer ergonomics that leapfrog, rather than ape, other blockchain ecosystems, simplifying
  testing, deployment, and interaction.
- **JavaScript developer experience patterns,** including the **Contract Client** behavior in
  **stellar-sdk-js**, which helps application developers interact with contracts more safely and
  predictably.

## Why we were selected for Stellar Scaffold and our SCF track record

In early 2025, SDF searched for a team that could bring a ScaffoldETH-like end-to-end experience to
Stellar. They selected us based on:

1. our deep **CLI & JS expertise** proven through shipped core tooling, and
2. our track record delivering developer infrastructure via SCF, including:
   - **Smart Deploy**:
     [https://communityfund.stellar.org/project/smart-deploy-yoj](https://communityfund.stellar.org/project/smart-deploy-yoj)
   - **Loam**:
     [https://communityfund.stellar.org/project/loam-qj5](https://communityfund.stellar.org/project/loam-qj5)

Stellar Scaffold is a direct continuation of that work: turning the hard-won Developer Experience
(DevX) knowledge from core tooling into a “front door” experience that helps developers go from idea
to proof-of-concept quickly, with strong defaults and a convention-over-configuration approach.

## Ongoing maintenance and production-grade integration experience

Since then, we have remained engaged with SDF to support and maintain key tooling (most recently
improving Stellar CLI handling of **hardware-based keys**) and we continue to operate as an
integration partner on production deployments. Notably, we **architected and developed Société
Générale’s EURCV** on Stellar (now live), bringing a rigorous, real-world perspective to developer
tooling and reliability requirements.

## Deep community participation and ecosystem leadership

Our team includes well-known ecosystem contributors. Several members hold key community roles (e.g.,
**SCF Pilot**, **category delegates**) and actively build their own SCF projects (e.g., **Moonlight,
Tansu, Stellar Merch Store, PG Atlas**). We contribute to protocol and tooling discussions, provide
developer support at hackathons and conferences, and invest heavily in community outreach and
education. We show up consistently at major events and actively communicate about Stellar, both its
strengths and the practical realities builders need to know.

## Cross-ecosystem perspective (DevX benchmarking)

Beyond Stellar, The Aha Company is also an integration partner in other ecosystems (e.g., **Filecoin,
XRPL, Cardano, Canton, Starknet**). This gives us a unique ability to benchmark developer experience
across chains and bring proven patterns back to Stellar—while keeping Stellar Scaffold aligned with
what developers expect from modern, full-stack tooling.

## Retroactive Impact

- **Stellar Registry graduated into its own project.** What began as a Stellar Scaffold workstream
  matured enough over the last two quarters to be spun out as an independent public good with its own
  team, repos, and roadmap. The extraction of the Scaffold CLI into its own focused repository was
  completed this quarter (https://github.com/stellar-scaffold/cli/pull/535), and Scaffold remains the
  primary integration surface for publishing and consuming Registry contracts. This is the incubation
  model working as intended.
- **Same-cycle Stellar Protocol 27 support.** The CLI, contract templates, and generated projects
  were upgraded to Protocol 27 (https://github.com/stellar-scaffold/cli/pull/549) and released
  immediately (2026-06-30), so builders scaffolding new projects were never stuck on an old protocol.
- **Continuous releases.** Three `stellar-scaffold-cli` releases shipped this quarter (v0.0.22,
  v0.0.23, v0.0.24) plus supporting crates, with notes:
  https://github.com/stellar-scaffold/cli/releases
- **Upstream documentation contributions**, e.g. improving prerequisites on the official Stellar docs
  (https://github.com/stellar/stellar-docs/pull/2267).
- Stellar Scaffold remains in the "recommended resources" for Stellar hackathons and is recommended
  in [the official SKILL](https://github.com/stellar/stellar-dev-skill/blob/main/skill/resources.md).

## Past Deliverables

**Q2 in summary.** We made Q2 a deliberate re-architecture quarter. Three structural efforts — the
Registry split, the multi-framework Template Monorepo, and the Protocol 27 upgrade — consumed most of
the quarter and touched nearly every deliverable below. That investment is what makes the Q3 list
finishable: wallet integration now lands once in a shared package instead of per-template, community
templates have a real extension point, and the config-file migration has its first slice shipped. Of
the eight committed deliverables, one shipped fully, two shipped substantially, and the remainder
have completed discovery/design with implementation carried into Q3 — several with open PRs already.

### D1: Support Stellar-Wallets-Kit v2

> - Update to Stellar-Wallets-Kit v2, released v2 in Feb 2025, to streamline Developers' experience
>   and keep up to date with the latest standards in the ecosystem.
> - Measure: update shipped in frontend
> - Issue: https://github.com/stellar-scaffold/cli/issues/441

**Shipped.** Upgraded integration, improved UX, and network polling workaround merged in
https://github.com/stellar-scaffold/ui/pull/241. The Template Monorepo restructure (see D3, D8) moved
wallet integration into the shared `@stellar-scaffold/app-lib` package, so the v2 upgrade now lands
once for every framework template instead of once per template. Finishing this is committed in Q3
(see Proposed D3).

### D2: Allow package manager of choice

> - Rather than forcing people to use NPM with Scaffold, allow them to pick the JS package manager of
>   their choosing (yarn, bun, deno, etc)
> - Measure: feature shipped, tested, & documented
> - Issue: https://github.com/stellar-scaffold/cli/issues/162

**Shipped.** Core package-manager-agnostic behavior merged in
https://github.com/stellar-scaffold/cli/pull/345, with follow-up improvements in
https://github.com/stellar-scaffold/cli/pull/491, released in `stellar-scaffold-cli` v0.0.24. The
tracking issue is closed.

### D3: BYOFrontend

> - Create two new Aha-maintained Scaffold frontend plugins: 1. no frontend, 2. Svelte. In addition,
>   create documentation for how community members can contribute their own frontend templates for
>   use with Stellar Scaffold.
> - Measure: feature shipped, tested, documented.
> - Issue: https://github.com/stellar-scaffold/cli/issues/161

**Substantially shipped** via the Template Monorepo effort
(https://github.com/stellar-scaffold/cli/pull/543, https://github.com/stellar-scaffold/ui/pull/234,
and https://github.com/stellar-scaffold/cli/pull/564):

- The single React frontend repo became a multi-framework template monorepo (`templates/react`,
  `templates/svelte`, plus a shared `app-lib` package for wallet, storage, and formatting logic),
  delivering the official **Svelte template**.
- `stellar scaffold init --template` accepts either an official framework name (e.g. `svelte`) or an
  `org/repo` community template, establishing the "bring your own frontend" path.
- A new `scaffold.yml` `config:` section lets any template declare where its contracts, TypeScript
  bindings, and contract clients live, so community templates can follow their own framework
  conventions.
- `--no-template` or `--template none` allows a contract-only workflow without any frontend

A community-template contribution guide — was not delivered in Q2 and is explicitly committed in Q3
(Proposed D5).

### D4: SKILL.md to help agentic workflows

> - Add SKILL.md to Stellar Scaffold repository to facilitate more powerful and accurate AI & agentic
>   workflows.
> - Measure: feature shipped, tested, and documented.
> - Issue: https://github.com/stellar-scaffold/cli/issues/394

Not shipped in Q2; design work completed. The Registry split re-scoped this deliverable: each product
now needs its own agent-facing doc (Scaffold's `SKILL.md` hosted at scaffoldstellar.org, Registry's
own alongside its site), and the template monorepo introduced a second need — in-project agent docs
that `init` carries into generated end-user projects. The re-scoped design is committed in Q3 (see
Proposed D4).

### D5: Improve Scaffold info on main Stellar docs

> - Minimize the info on the Stellar Scaffold page on the main Stellar docs in line with other tools
>   that have their own documentations sites, linking prominently to https://scaffoldstellar.org
> - Measure: new documentation page shipped to main Stellar docs
> - Issue: https://github.com/stellar-scaffold/cli/issues/361

**Shipped.** Scope was agreed in the issue discussion (minimize the page, link prominently to the
dedicated docs site), and smaller upstream improvements shipped in the meantime
(https://github.com/stellar/stellar-docs/pull/2267). Multiple pages reworked on Stellar docs
(https://github.com/stellar/stellar-docs/pull/2708) and contain pointers to updated documentation on
new, redesigned Scaffold docs site (https://github.com/stellar-scaffold/cli/pull/577).

### D6: Monitor releases of ecosystem projects

> - For Scaffold itself and all projects that are built with it, provide automatic notifications
>   (perhaps in the form of GitHub issues or pull requests) when complex ecosystem dependencies, such
>   as Stellar-Wallets-Kit, are updated.
> - Measure: system in place for notifying Scaffold team of ecosystem project updates
> - Issue: https://github.com/stellar-scaffold/cli/issues/301

Not shipped; design discussion in the issue converged on an approach: scheduled CI (cron) jobs that
test against dependency releases (or HEAD/nightly builds for early warning), structured so that
projects _built with_ Scaffold can inherit the same alerts. Our existing scheduled-update flow for
the OpenZeppelin example contracts serves as the prototype. Carried into Q3 as a stretch goal
(Proposed D9) behind the committed re-architecture work.

### D7: Allow building for testnet when localnet unhealthy

> - Scaffold currently requires running a local Stellar network, which it can do automatically, even
>   when building for a testnet target. We will fix this.
> - Measure: bug fix shipped
> - Issue: https://github.com/stellar-scaffold/cli/issues/267

Not shipped as a point fix — investigation showed the network-health check is baked into the build
internals being reworked under D8, and that a point fix would fight the old config model. The durable
fix lands with the Q3 `scaffold.yml` networks rework (Proposed D2), which decouples target-network
builds from localnet state; the new `scaffold doctor` command (Proposed D1) then gives users
self-serve diagnosis of unhealthy localnets instead of a confusing failure.

### D8: Re-architect stellar scaffold build internals & update to latest best practices

> - Various bugs and sub-optimal behavior can be pinned on some early, messy architectural decisions
>   made in stellar-scaffold-cli, the core of which is now nearly a year old. We will rework this
>   core logic to improve functionality, fix bugs, and adopt latest best practices.
> - Measure: features shipped, tested, and documented.
> - Issues: https://github.com/stellar-scaffold/cli/issues/329,
>   https://github.com/stellar-scaffold/cli/issues/346,
>   https://github.com/stellar-scaffold/cli/issues/181

**Major structural work shipped:**

- Extracted the Scaffold CLI into its own focused repository as part of the Registry split
  (https://github.com/stellar-scaffold/cli/pull/535).
- Rebuilt `init`, `upgrade`, and `clean` around the new template monorepo, factoring `init` into
  three clean steps — acquire, instantiate, prepare — replacing the original single-repo degit logic
  (https://github.com/stellar-scaffold/cli/pull/543).
- Shipped the first slice of the new `scaffold.yml` configuration file (the per-template `config:`
  section), the replacement for `environments.toml` proposed in issue 181.
- Upgraded the toolchain to Stellar Protocol 27 (https://github.com/stellar-scaffold/cli/pull/549).

The discovery work here defined the remaining schema migration (networks and contract-client config)
and the `--optimize` passthrough, both committed in Q3 (Proposed D2).

### Ongoing maintenance, releases, and field feedback loop

Regular tagged releases with notes continued throughout the quarter
(https://github.com/stellar-scaffold/cli/releases), including three `stellar-scaffold-cli` releases,
OpenZeppelin example-contract updates, and the Protocol 27 upgrade.

## Proposed Impact

With Stellar Registry incubated out as its own public good, Stellar Scaffold enters Q3 with a sharper
scope: the front door of the Stellar ecosystem. The template monorepo shipped in Q2 turns "the
official React starter" into a multi-framework template system — Svelte is live, and the `org/repo`
template flag opens the door to community-maintained frontends, letting the ecosystem grow templates
without growing our payroll. Agent-facing documentation will make Scaffold the most reliable way for
AI-assisted builders (the majority at recent hackathons) to produce working Stellar dApps. And
`scaffold doctor` cuts the support burden that environment problems create at every hackathon.

We are deliberately committing to a shorter list this quarter than last: the Q2 re-architecture is
done, and Q3 is about finishing what it unblocked. Every committed deliverable below either has an
open PR, a shipped first slice, or a completed design from Q2 discovery.

### A note on budget

The Registry split moves that workstream to its own proposal, but it does not shrink this one
proportionally: the template surface we maintain grew from one framework to a monorepo of shared
core + multiple templates (each needing e2e coverage, releases, and protocol upgrades), and Scaffold
remains the integration surface for Registry, wallets, and other ecosystem dependencies. The budget
now buys depth and reliability on that wider surface rather than breadth of new workstreams.

## Proposed Deliverables

## D1: Create `scaffold doctor` command

- A new command that examines and diagnoses environment problems in the user's project: wrong Rust
  toolchain, missing dependencies (e.g. Docker), an unhealthy localnet, incorrect `scaffold.yml`
  values.
- Measure: command shipped, tested, and documented.
- Issues: https://github.com/stellar-scaffold/cli/issues/557 (and resolves the failure mode reported
  in https://github.com/stellar-scaffold/cli/issues/267)
- Ecosystem value: Q2 bug investigation showed that a large share of Scaffold support requests are
  environment problems, not Scaffold bugs. Self-serve diagnosis shortens time-to-first-success for
  new builders — especially at hackathons — and reduces maintainer support load across the ecosystem.
  It also provides value to projects bootstrapped by other means (not Scaffold) that end up with
  environment and version problems.

## D2: Complete the `scaffold.yml` configuration migration

- Finish the CLI configuration rework begun in Q2: fold network and contract-client configuration
  into `scaffold.yml` (whose `config:` section shipped with the template monorepo), retire
  `environments.toml`, and pass through the `--optimize` flag to `stellar contract build`.
- Measure: new schema shipped, tested, and documented; `environments.toml` deprecated with a
  migration path; optimize passthrough shipped.
- Issues: https://github.com/stellar-scaffold/cli/issues/181,
  https://github.com/stellar-scaffold/cli/issues/329
- Stretch: specify a contract from a live network as a project dependency
  (https://github.com/stellar-scaffold/cli/issues/346)
- Ecosystem value: one obvious, well-named config file instead of a misleadingly-named split; this
  rework also decouples target-network builds from localnet state (the root cause behind issue 267)
  and enables per-framework directory conventions for community templates.

## D3: Ship Stellar-Wallets-Kit v2 through the shared wallet module

- Land the in-review Wallets-Kit v2 upgrade in the shared `@stellar-scaffold/app-lib` package so all
  framework templates (React, Svelte, and future Vue) get the upgrade from a single integration
  point.
- Measure: upgrade merged and released across all official templates.
- Issue: https://github.com/stellar-scaffold/cli/issues/441 (implementation:
  https://github.com/stellar-scaffold/ui/pull/241)
- Ecosystem value: keeps scaffolded apps current with the latest wallet standards, and validates the
  shared-app-lib architecture: one wallet integration maintained once, consumed by every template.

## D4: Agent-facing docs: hosted `SKILL.md` + in-project `AGENTS.md`

- Publish a self-contained `SKILL.md` at scaffoldstellar.org teaching AI agents Scaffold as a system,
  and ship `AGENTS.md` files in generated projects (with `init` stripping contributor-only content so
  end users get docs scoped to _their_ app).
- Measure: `SKILL.md` live and fetchable by URL; generated projects include a correct `AGENTS.md`;
  both documented.
- Issue: https://github.com/stellar-scaffold/cli/issues/394
- Ecosystem value: many hackathon participants and serious builders prefer to use AI tools in
  addition to, or rather than, coding by hand. Accurate agent-facing docs make that experience
  fool-proof, preventing AIs from making silly mistakes both when scaffolding a project and when
  working inside one.

## D5: Complete BYOFrontend: "no frontend" option + community-template guide

- Finish the remaining scope from Q2's BYOFrontend deliverable: a "no frontend" init option
  (contracts and clients without a UI layer) and a contribution guide documenting how community
  members build and publish their own framework templates for
  `stellar scaffold init --template org/repo`.
- Measure: no-frontend option shipped and tested; contribution guide published on the docs site; at
  least the existing official templates documented as reference implementations.
- Issue: https://github.com/stellar-scaffold/cli/issues/161
- Ecosystem value: closes out a Q2 commitment, and shifts template growth to the community — the
  ecosystem gets more framework options (Vue, Solid, etc.) without every template landing on one
  team's maintenance budget.

## D6: Documentation consolidation & redesign

- Redesign the Scaffold docs website (taking inspiration from the new Registry site), update the
  tutorial to cover the latest Registry publish/deploy integration, complete the domain migration,
  and minimize the Scaffold page on the main Stellar docs to link prominently to the dedicated site.
- Measure: redesigned docs site live; tutorial updated; upstream Stellar docs page PR merged.
- Issues: https://github.com/stellar-scaffold/cli/issues/556,
  https://github.com/stellar-scaffold/cli/issues/437,
  https://github.com/stellar-scaffold/cli/issues/361,
  https://github.com/stellar-scaffold/cli/issues/550
- Ecosystem value: consolidates Scaffold documentation to a single, current place, minimizing stale
  information across the ecosystem and keeping the Registry integration path — now a cross-project
  concern — accurately documented.

## D7: Ongoing maintenance & releases

- Regular tagged releases with changelogs, protocol upgrades, OpenZeppelin example-contract updates,
  issue/PR triage, and CI reliability work as the template matrix grows.
- Measure: regular tagged releases + changelogs + documented learnings from events.
- Ecosystem value: a "front door" tool must always work with the current protocol and ecosystem
  libraries; reliability is the feature.

## D8 (Stretch): At least one ecosystem-contributed UI template

- Work with a specific community partner or host a hackathon to solicit at least one new UI template.
  This could be a new JS view engine such as Vue, or an existing view engine (React, Svelte)
  configured differently (such as React with NextJS and different styling opinions). This will be
  selectable via `stellar scaffold init`.
- Measure: template shipped with e2e coverage, selectable in `init`, documented.
- Issue: https://github.com/stellar-scaffold/cli/issues/558
- Ecosystem value: exercises the multi-template architecture with a third framework and serves as a
  worked example for the community-template guide (D5). Stretch rather than committed: we'd rather
  demand for Vue prove itself via the community path than pre-commit maintenance of a third official
  template.

## D9 (Stretch): Monitor releases of ecosystem projects

- Implement the scheduled-CI monitoring approach designed in Q2: automatic notifications (issues or
  PRs) when complex ecosystem dependencies such as Stellar-Wallets-Kit publish updates, structured so
  projects built with Scaffold can adopt the same alerts.
- Measure: system in place for notifying the Scaffold team of ecosystem project updates.
- Issue: https://github.com/stellar-scaffold/cli/issues/301
- Ecosystem value: ecosystem dependencies ship breaking changes; catching them early keeps Scaffold —
  and every project scaffolded from it — working and current.

## D10 (Stretch): Anonymous usage telemetry

- Add basic, anonymous usage telemetry to the CLI (e.g. `scaffold init` counts, deploys per network)
  so the team can measure real adoption instead of relying on anecdote. Do this in conjunction with
  indexing already-available on-chain data, and prefer on-chain data as the source when possible.
- Measure: telemetry system shipped with clear disclosure; adoption metrics available to the team.
- Issues: https://github.com/stellar-scaffold/cli/issues/448,
  https://github.com/stellar-scaffold/cli/issues/479
- Ecosystem value: lets us (and SCF) evaluate Scaffold's actual ecosystem impact quantitatively and
  prioritize future work by evidence.

## D11 (Stretch): Interactive OpenZeppelin contract wizard

- An interactive CLI mirroring wizard.openzeppelin.com for adding OZ-based contracts to a Scaffold
  project (building on the draft in https://github.com/stellar-scaffold/cli/pull/391).
- Measure: feature shipped, tested, and documented.
- Issue: https://github.com/stellar-scaffold/cli/issues/156
- Ecosystem value: safe, audited building blocks become the path of least resistance for new
  contracts.

## D12 (Stretch): Update starter app's Debug page

- Improve the generated app's contract Debug page: clearer results display, additional transaction
  details, and a persistent block-explorer link.
- Measure: updated Debug page shipped in templates.
- Issue: https://github.com/stellar-scaffold/cli/issues/248
- Ecosystem value: the Debug page is many builders' first contract interaction; better feedback loops
  mean faster learning.

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Ascaffold_stellar&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Ascaffold_stellar)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Ascaffold_stellar&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Ascaffold_stellar)
[![Criticality](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Ascaffold_stellar&query=%24.criticality_score&label=Criticality&color=E5484D)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Ascaffold_stellar)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Ascaffold_stellar&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Ascaffold_stellar)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Ascaffold_stellar&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Ascaffold_stellar)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
