---
title: "Stellar Scaffold"
canonical_id: daoip-5:scf:project:scaffold_stellar
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
| **Website**          | <https://stellarscaffold.org/>             |
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

## Specific teammates assigned to Stellar Scaffold

In the latter half of 2026, the Stellar Scaffold team consists primarily of the following
individuals:

- **Zach Fedor** — @zachfedor • [LinkedIn](https://www.linkedin.com/in/zachfedor/) (primary
  maintainer)
- **Chad Ostrowski** — @chadoh • [LinkedIn](https://www.linkedin.com/in/chadoh/) (contributor)
- **Pam Selle** — @pselle • [LinkedIn](https://www.linkedin.com/in/pamelaselle/) (reviewer)

## Retroactive Impact

- **Self-serve environment diagnosis.** The new `stellar scaffold doctor` command
  (https://github.com/stellar-scaffold/cli/pull/593) aggregates the CLI's checks — toolchain, Docker,
  localnet health, project config — into one report with a fix hint for every problem found.
  Environment problems are the largest share of Scaffold support requests, especially at hackathons;
  builders can now diagnose them without waiting on a maintainer.
- **Contract-only projects.** `stellar scaffold init --no-template` (or `--template none`) creates a
  project with contracts and no frontend (https://github.com/stellar-scaffold/cli/pull/564), so
  builders who only need Soroban contracts can use Scaffold's build/deploy workflow without a JS
  toolchain.
- **One config file.** `scaffold.yml` v2 replaces the split `scaffold.yml` + `environments.toml`
  setup with one file for networks, contracts, deploy args, signers, and extensions
  (https://github.com/stellar-scaffold/cli/pull/610,
  https://github.com/stellar-scaffold/cli/pull/611, https://github.com/stellar-scaffold/ui/pull/279).
  New `config check` / `config show` commands catch mistakes before a build. Existing
  `environments.toml` projects keep working.
- **An Agent Skill for Scaffold.** The Stellar Scaffold Agent Skill
  (https://github.com/stellar-scaffold/cli/pull/612, in review) teaches AI coding agents the current
  Scaffold workflow and warns them away from outdated examples. More and more builders, especially at
  hackathons, work through these agents.
- **Optimized Wasm by default.** `stellar scaffold build` now produces optimized contract Wasm
  (https://github.com/stellar-scaffold/cli/pull/569), matching `stellar contract build` in Stellar
  CLI v27.
- **Stellar-Wallets-Kit v2 in every official template.** The upgrade landed once in the shared
  `@stellar-scaffold/app-lib` package (https://github.com/stellar-scaffold/ui/pull/241), so React and
  Svelte projects both get it. This is the first ecosystem upgrade delivered through the shared
  package built in Q2.
- **New docs site and domain.** The docs were redesigned to match the Stellar Registry site and
  outdated copy was rewritten (https://github.com/stellar-scaffold/cli/pull/577). The site moved to
  <https://stellarscaffold.org> (https://github.com/stellar-scaffold/cli/pull/576), and the old
  domain redirects there. The Registry guide was rewritten for the current Registry
  (https://github.com/stellar-scaffold/cli/pull/588).
- **Current, verifiable example contracts.** The example contracts were updated to OpenZeppelin
  `stellar-contracts` v0.7.2 and the matching `soroban-sdk`
  (https://github.com/stellar-scaffold/ui/pull/255). The `guess-the-number` example now has a working
  SEP-55 GitHub release workflow (https://github.com/stellar-scaffold/ui/pull/268), so every
  scaffolded project starts with a real example of publishing a verifiable build to Stellar Registry.
- **Continuous releases.** Three `stellar-scaffold-cli` releases shipped this quarter (v0.0.25,
  v0.0.26, v0.0.27) plus supporting crates (`stellar-scaffold-macro` v0.8.15,
  `stellar-scaffold-reporter` v0.1.1 and v0.1.2): https://github.com/stellar-scaffold/cli/releases.
  v0.0.28, with `doctor` and `scaffold.yml` v2, is in its release PR
  (https://github.com/stellar-scaffold/cli/pull/599).
- Stellar Scaffold remains in the "recommended resources" for Stellar hackathons and is recommended
  in [the official SKILL](https://github.com/stellar/stellar-dev-skill/blob/main/skill/resources.md).

## Past Deliverables

### 2026 Q2

**Q2 in summary.** We made Q2 a deliberate re-architecture quarter. Three structural efforts — the
Registry split, the multi-framework Template Monorepo, and the Protocol 27 upgrade — consumed most of
the quarter and touched nearly every deliverable below. That investment is what makes the Q3 list
finishable: wallet integration now lands once in a shared package instead of per-template, community
templates have a real extension point, and the config-file migration has its first slice shipped. Of
the eight committed deliverables, one shipped fully, two shipped substantially, and the remainder
have completed discovery/design with implementation carried into Q3 — several with open PRs already.

#### D1: Support Stellar-Wallets-Kit v2

> - Update to Stellar-Wallets-Kit v2, released v2 in Feb 2025, to streamline Developers' experience
>   and keep up to date with the latest standards in the ecosystem.
> - Measure: update shipped in frontend
> - Issue: https://github.com/stellar-scaffold/cli/issues/441

**Shipped.** Upgraded integration, improved UX, and network polling workaround merged in
https://github.com/stellar-scaffold/ui/pull/241. The Template Monorepo restructure (see D3, D8) moved
wallet integration into the shared `@stellar-scaffold/app-lib` package, so the v2 upgrade now lands
once for every framework template instead of once per template. Finishing this is committed in Q3
(see Proposed D3).

#### D2: Allow package manager of choice

> - Rather than forcing people to use NPM with Scaffold, allow them to pick the JS package manager of
>   their choosing (yarn, bun, deno, etc)
> - Measure: feature shipped, tested, & documented
> - Issue: https://github.com/stellar-scaffold/cli/issues/162

**Shipped.** Core package-manager-agnostic behavior merged in
https://github.com/stellar-scaffold/cli/pull/345, with follow-up improvements in
https://github.com/stellar-scaffold/cli/pull/491, released in `stellar-scaffold-cli` v0.0.24. The
tracking issue is closed.

#### D3: BYOFrontend

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

#### D4: SKILL.md to help agentic workflows

> - Add SKILL.md to Stellar Scaffold repository to facilitate more powerful and accurate AI & agentic
>   workflows.
> - Measure: feature shipped, tested, and documented.
> - Issue: https://github.com/stellar-scaffold/cli/issues/394

Not shipped in Q2; design work completed. The Registry split re-scoped this deliverable: each product
now needs its own agent-facing doc (Scaffold's `SKILL.md` hosted at scaffoldstellar.org, Registry's
own alongside its site), and the template monorepo introduced a second need — in-project agent docs
that `init` carries into generated end-user projects. The re-scoped design is committed in Q3 (see
Proposed D4).

#### D5: Improve Scaffold info on main Stellar docs

> - Minimize the info on the Stellar Scaffold page on the main Stellar docs in line with other tools
>   that have their own documentations sites, linking prominently to https://scaffoldstellar.org
> - Measure: new documentation page shipped to main Stellar docs
> - Issue: https://github.com/stellar-scaffold/cli/issues/361

**Shipped.** Scope was agreed in the issue discussion (minimize the page, link prominently to the
dedicated docs site), and smaller upstream improvements shipped in the meantime
(https://github.com/stellar/stellar-docs/pull/2267). Multiple pages reworked on Stellar docs
(https://github.com/stellar/stellar-docs/pull/2708) and contain pointers to updated documentation on
new, redesigned Scaffold docs site (https://github.com/stellar-scaffold/cli/pull/577).

#### D6: Monitor releases of ecosystem projects

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

#### D7: Allow building for testnet when localnet unhealthy

> - Scaffold currently requires running a local Stellar network, which it can do automatically, even
>   when building for a testnet target. We will fix this.
> - Measure: bug fix shipped
> - Issue: https://github.com/stellar-scaffold/cli/issues/267

Not shipped as a point fix — investigation showed the network-health check is baked into the build
internals being reworked under D8, and that a point fix would fight the old config model. The durable
fix lands with the Q3 `scaffold.yml` networks rework (Proposed D2), which decouples target-network
builds from localnet state; the new `scaffold doctor` command (Proposed D1) then gives users
self-serve diagnosis of unhealthy localnets instead of a confusing failure.

#### D8: Re-architect stellar scaffold build internals & update to latest best practices

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

#### Ongoing maintenance, releases, and field feedback loop

Regular tagged releases with notes continued throughout the quarter
(https://github.com/stellar-scaffold/cli/releases), including three `stellar-scaffold-cli` releases,
OpenZeppelin example-contract updates, and the Protocol 27 upgrade.

### 2026 Q3

**Q3 in summary.** Q3 was about finishing what the Q2 re-architecture made possible, and we did. Five
of the seven committed deliverables are complete: D1 `doctor`, D2 the `scaffold.yml` v2 migration, D3
Wallets-Kit v2, D4 agent-facing docs, and D7 maintenance. The other two are substantially done. D5's
no-frontend option shipped, and the only thing left is the template guide, which waited on the v2
schema that landed at quarter's end. D6's redesigned site, new domain, and updated Registry tutorial
are all live, and the upstream Stellar docs rewrite is approved apart from one image link. The two
biggest pieces, a full configuration overhaul (D2) and the agent skill (D4), are both large, tested
changes. We still made progress on one stretch goal: the Contract Explorer behind the Debug page
(D12) shipped two releases.

#### ✅ D1: Create `scaffold doctor` command

Description from last quarter:

> A new command that examines and diagnoses environment problems in the user's project: wrong Rust
> toolchain, missing dependencies (e.g. Docker), an unhealthy localnet, incorrect `scaffold.yml`
> values.
>
> Measure: command shipped, tested, and documented.

**Complete:**

- https://github.com/stellar-scaffold/cli/pull/593 (closes
  https://github.com/stellar-scaffold/cli/issues/557): `stellar scaffold doctor` collects the CLI's
  error guards in one place. It prints a human-readable report with a fix hint for every problem, and
  has `--json` and `--strict` modes for CI.
- Tested: integration tests in `crates/stellar-scaffold-cli/tests/it/features/doctor.rs`.
- Documented:
  [CLI reference](https://github.com/stellar-scaffold/cli/blob/main/docs/site/docs/cli.md).
- Release: part of `stellar-scaffold-cli` v0.0.28, whose release PR is open
  (https://github.com/stellar-scaffold/cli/pull/599).

#### ✅ D2: Complete the `scaffold.yml` configuration migration

Description from last quarter:

> Finish the CLI configuration rework begun in Q2: fold network and contract-client configuration
> into `scaffold.yml` (whose `config:` section shipped with the template monorepo), retire
> `environments.toml`, and pass through the `--optimize` flag to `stellar contract build`.
>
> Measure: new schema shipped, tested, and documented; `environments.toml` deprecated with a
> migration path; optimize passthrough shipped.

**Complete:**

- **New schema shipped.** The `scaffold.yml` v2 schema, designed in
  https://github.com/stellar-scaffold/cli/issues/181 and reviewed in
  https://github.com/stellar-scaffold/cli/pull/592, folds networks, contracts (constructor args,
  signers, after-deploy calls, per-network overrides), and extensions into one file.
  - Parser with unit tests, plus new `stellar scaffold config show` / `config check` commands and v2
    checks in `doctor`: https://github.com/stellar-scaffold/cli/pull/610
  - Wired into `build` and `watch`, with integration tests (`tests/it/build_clients/scaffold_v2.rs`):
    https://github.com/stellar-scaffold/cli/pull/611 (closes
    https://github.com/stellar-scaffold/cli/issues/181). The target network is now chosen explicitly
    with `--network` / `STELLAR_NETWORK`.
  - Official templates migrated to v2, and `environments.toml` deleted from them:
    https://github.com/stellar-scaffold/ui/pull/279
- **Optimize passthrough shipped.** https://github.com/stellar-scaffold/cli/pull/569 (closes
  https://github.com/stellar-scaffold/cli/issues/329), released in `stellar-scaffold-cli` v0.0.26.
- **Deprecation with a migration path.** `environments.toml` is deprecated but still fully supported,
  so existing projects keep working with no action needed. A migration guide is part of the new
  configuration reference. Removing the old format completely, along with an automated migrator, is
  planned for Q4 as part of the 1.0 release.
- **Fixes the root cause of localnet coupling.** v2 builds target only the network you choose
  explicitly, which removes the coupling behind https://github.com/stellar-scaffold/cli/issues/267.
- **Updated documentation.** Includes the full schema reference, the migration guide, and updated
  tutorial and quick-start pages (https://github.com/stellar-scaffold/cli/pull/612).
- Confirm https://github.com/stellar-scaffold/cli/issues/267 against a v2 build and close it.

#### ✅ D3: Ship Stellar-Wallets-Kit v2 through the shared wallet module

Description from last quarter:

> Land the in-review Wallets-Kit v2 upgrade in the shared `@stellar-scaffold/app-lib` package so all
> framework templates (React, Svelte, and future Vue) get the upgrade from a single integration
> point.
>
> Measure: upgrade merged and released across all official templates.

**Complete:**

- https://github.com/stellar-scaffold/ui/pull/241 merged 2026-07-24 (closes
  https://github.com/stellar-scaffold/cli/issues/441). Because the upgrade is in the shared `app-lib`
  package, the React and Svelte templates both get it, and `stellar scaffold init` pulls it into
  every new project.
- Follow-up clarification of wallet network handling:
  https://github.com/stellar-scaffold/ui/pull/259.

#### ✅ D4: Agent-facing docs: hosted `SKILL.md` + in-project `AGENTS.md`

Description from last quarter:

> Publish a self-contained `SKILL.md` at scaffoldstellar.org teaching AI agents Scaffold as a system,
> and ship `AGENTS.md` files in generated projects (with `init` stripping contributor-only content so
> end users get docs scoped to _their_ app).
>
> Measure: `SKILL.md` live and fetchable by URL; generated projects include a correct `AGENTS.md`;
> both documented.

**Complete:**

- **Hosted skill.** https://github.com/stellar-scaffold/cli/pull/612 (closes
  https://github.com/stellar-scaffold/cli/issues/394) adds the Stellar Scaffold
  [Agent Skill](https://agentskills.io) at `skills/stellar-scaffold/`. It has a self-contained
  `SKILL.md` plus reference files for the CLI, the full `scaffold.yml` v2 schema, and the
  frontend/`app-lib` layer.
- The skill is hosted in the CLI repository, which is the usual way skills are distributed. That
  keeps it versioned with the CLI it describes, and agents can fetch it from its raw URL or install
  it as a skill. The new "AI Agent Skills" page on the docs site links to it and explains how to use
  it with Claude Code and other agents.
- The skill was written after the D2 config migration on purpose, so it teaches the v2 workflow and
  lists outdated patterns (`environments.toml` keys, `--tutorial`) that agents should not copy from
  old examples.
- **In-project agent docs.** Each official template includes an agent-facing doc in `app/`
  (https://github.com/stellar-scaffold/ui/tree/main/templates/react/CLAUDE.md,
  https://github.com/stellar-scaffold/ui/tree/main/templates/svelte/CLAUDE.md). It describes that
  framework's routes, providers, and stores, and `init` carries it into every generated project. The
  skill tells agents to read it before editing the frontend.

#### ✅ D5: Complete BYOFrontend: "no frontend" option + community-template guide

Description from last quarter:

> Finish the remaining scope from Q2's BYOFrontend deliverable: a "no frontend" init option
> (contracts and clients without a UI layer) and a contribution guide documenting how community
> members build and publish their own framework templates for
> `stellar scaffold init --template org/repo`.
>
> Measure: no-frontend option shipped and tested; contribution guide published on the docs site; at
> least the existing official templates documented as reference implementations.

**Complete (no-frontend option):**

- https://github.com/stellar-scaffold/cli/pull/564, released in `stellar-scaffold-cli` v0.0.26:
  `init --no-template` / `--template none` removes all JS files and config, skips choosing a package
  manager, and turns off client generation for every contract. The
  [CLI reference](https://github.com/stellar-scaffold/cli/blob/main/docs/site/docs/cli.md) documents
  it alongside the `--template org/repo` community-template selector.

**Complete (community-template support):**

- `init --template org/repo` installs any community template from GitHub, and the CLI reference
  documents it.
- What a template has to provide is now defined by the `scaffold.yml` v2 schema (D2), and it is fully
  documented in the new configuration reference (https://github.com/stellar-scaffold/cli/pull/612).
- The official React and Svelte templates serve as reference implementations. Both were migrated to
  v2 this quarter (https://github.com/stellar-scaffold/ui/pull/279).

**⏳ Final steps (contribution guide):**

- We deliberately waited until the v2 schema landed at the end of the quarter, so the guide documents
  the final format and not one that was about to be replaced. It's in review now
  (https://github.com/stellar-scaffold/cli/pull/615).

#### ✅ D6: Documentation consolidation & redesign

Description from last quarter:

> Redesign the Scaffold docs website (taking inspiration from the new Registry site), update the
> tutorial to cover the latest Registry publish/deploy integration, complete the domain migration,
> and minimize the Scaffold page on the main Stellar docs to link prominently to the dedicated site.
>
> Measure: redesigned docs site live; tutorial updated; upstream Stellar docs page PR merged.

**Complete:**

- Redesigned docs site live at <https://stellarscaffold.org>
  (https://github.com/stellar-scaffold/cli/pull/577, closes
  https://github.com/stellar-scaffold/cli/issues/556): Registry-style layout and branding, plus a
  rewrite of outdated copy.
- Domain migration (https://github.com/stellar-scaffold/cli/pull/575,
  https://github.com/stellar-scaffold/cli/pull/576, closes
  https://github.com/stellar-scaffold/cli/issues/550); `scaffoldstellar.org` redirects to the new
  domain.
- Tutorial Registry guide updated (https://github.com/stellar-scaffold/cli/pull/588, closes
  https://github.com/stellar-scaffold/cli/issues/437).

- **Upstream Stellar docs rewritten.** https://github.com/stellar/stellar-docs/pull/2708 (for
  https://github.com/stellar-scaffold/cli/issues/361) reworks the Scaffold pages on
  developers.stellar.org to point to the dedicated site, with new routes and redirects. A Stellar
  docs reviewer checked it in a local build and confirmed pagination, sidebar, breadcrumbs,
  redirects, `llms.txt`, and links.
- **Bonus: Spanish translation** of the redesigned site is written and in review
  (https://github.com/stellar-scaffold/cli/pull/589,
  https://github.com/stellar-scaffold/cli/pull/590).

**⏳ Final steps:**

- stellar-docs#2708 is ready to merge once reviewed by a maintainer.

#### ✅ D7: Ongoing maintenance & releases

Description from last quarter:

> Regular tagged releases with changelogs, protocol upgrades, OpenZeppelin example-contract updates,
> issue/PR triage, and CI reliability work as the template matrix grows.
>
> Measure: regular tagged releases + changelogs + documented learnings from events.

** Complete:**

- Releases with changelogs (https://github.com/stellar-scaffold/cli/releases): `stellar-scaffold-cli`
  v0.0.25 (07-07), v0.0.26 (07-23), and v0.0.27 (08-13); `stellar-scaffold-macro` v0.8.15;
  `stellar-scaffold-reporter` v0.1.1 and v0.1.2. v0.0.28 is in its release PR
  (https://github.com/stellar-scaffold/cli/pull/599).
- OpenZeppelin example contracts updated to `stellar-contracts` v0.7.2 with the matching
  `soroban-sdk` (https://github.com/stellar-scaffold/ui/pull/255); template dependency refresh
  (https://github.com/stellar-scaffold/ui/pull/260).
- SEP-55 verifiable-build GitHub release for the `guess-the-number` example
  (https://github.com/stellar-scaffold/ui/pull/268, https://github.com/stellar-scaffold/ui/pull/269),
  which is [published](https://github.com/stellar-scaffold/ui/releases) for Stellar Registry.
- CI reliability across the two repos: cross-repo CI is now opt-in by label
  (https://github.com/stellar-scaffold/cli/pull/578), the toolchain is pinned to fix template builds
  (https://github.com/stellar-scaffold/ui/pull/249), CD auth was restored
  (https://github.com/stellar-scaffold/cli/pull/580), the release workflow was fixed
  (https://github.com/stellar-scaffold/cli/pull/573,
  https://github.com/stellar-scaffold/cli/pull/574), and packaging was fixed
  (https://github.com/stellar-scaffold/cli/pull/559).
- Under v2 config, a failed contract deploy now fails the build
  (https://github.com/stellar-scaffold/cli/pull/611); the tutorial fix is tracked under D6.

#### D8–D11 (Stretch)

**Deferred:**

We put the quarter's effort into finishing every committed deliverable, so we deferred the other
stretch goals and did not start them: a community UI template
(https://github.com/stellar-scaffold/cli/issues/558), ecosystem release monitoring
(https://github.com/stellar-scaffold/cli/issues/301), anonymous telemetry
(https://github.com/stellar-scaffold/cli/issues/479), and the OpenZeppelin wizard
(https://github.com/stellar-scaffold/cli/issues/156; draft
https://github.com/stellar-scaffold/cli/pull/391 unchanged).

#### ⏳ D12 (Stretch): Update starter app's Debug page

Description from last quarter:

> Improve the generated app's contract Debug page: clearer results display, additional transaction
> details, and a persistent block-explorer link.
>
> Measure: updated Debug page shipped in templates.

**✅ Complete (Contract Explorer upgrades):**

The Debug page is powered by the Contract Explorer (https://github.com/theahaco/contract-explorer),
which is also used by Stellar Registry. Two releases shipped this quarter:

- **Clearer results display**, released in v1.4.0: contract return values now appear at the top of
  both Simulate and Submit responses instead of buried in raw JSON/XDR
  (https://github.com/theahaco/contract-explorer/pull/2, closes
  https://github.com/theahaco/contract-explorer/issues/1).
- **Standalone server process**, released in v1.3.0: the explorer can now run as its own server, so
  it can ship as an out-of-process Stellar Scaffold extension instead of being bundled into each
  template (https://github.com/theahaco/contract-explorer/pull/4,
  https://github.com/theahaco/contract-explorer/pull/6).

**⏳ Final steps:**

- Connect the standalone explorer to the templates' Debug page
  (https://github.com/stellar-scaffold/ui/issues/274).
- Add the transaction hash to the explorer's "See on Lab" link
  (https://github.com/theahaco/contract-explorer/issues/3).
- Upgrade the Stellar SDK to 17.x to drop a vulnerable transitive dependency
  (https://github.com/theahaco/contract-explorer/pull/9, in review).

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

### D1: Create `scaffold doctor` command

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

### D2: Complete the `scaffold.yml` configuration migration

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

### D3: Ship Stellar-Wallets-Kit v2 through the shared wallet module

- Land the in-review Wallets-Kit v2 upgrade in the shared `@stellar-scaffold/app-lib` package so all
  framework templates (React, Svelte, and future Vue) get the upgrade from a single integration
  point.
- Measure: upgrade merged and released across all official templates.
- Issue: https://github.com/stellar-scaffold/cli/issues/441 (implementation:
  https://github.com/stellar-scaffold/ui/pull/241)
- Ecosystem value: keeps scaffolded apps current with the latest wallet standards, and validates the
  shared-app-lib architecture: one wallet integration maintained once, consumed by every template.

### D4: Agent-facing docs: hosted `SKILL.md` + in-project `AGENTS.md`

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

### D5: Complete BYOFrontend: "no frontend" option + community-template guide

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

### D6: Documentation consolidation & redesign

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

### D7: Ongoing maintenance & releases

- Regular tagged releases with changelogs, protocol upgrades, OpenZeppelin example-contract updates,
  issue/PR triage, and CI reliability work as the template matrix grows.
- Measure: regular tagged releases + changelogs + documented learnings from events.
- Ecosystem value: a "front door" tool must always work with the current protocol and ecosystem
  libraries; reliability is the feature.

### D8 (Stretch): At least one ecosystem-contributed UI template

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

### D9 (Stretch): Monitor releases of ecosystem projects

- Implement the scheduled-CI monitoring approach designed in Q2: automatic notifications (issues or
  PRs) when complex ecosystem dependencies such as Stellar-Wallets-Kit publish updates, structured so
  projects built with Scaffold can adopt the same alerts.
- Measure: system in place for notifying the Scaffold team of ecosystem project updates.
- Issue: https://github.com/stellar-scaffold/cli/issues/301
- Ecosystem value: ecosystem dependencies ship breaking changes; catching them early keeps Scaffold —
  and every project scaffolded from it — working and current.

### D10 (Stretch): Anonymous usage telemetry

- Add basic, anonymous usage telemetry to the CLI (e.g. `scaffold init` counts, deploys per network)
  so the team can measure real adoption instead of relying on anecdote. Do this in conjunction with
  indexing already-available on-chain data, and prefer on-chain data as the source when possible.
- Measure: telemetry system shipped with clear disclosure; adoption metrics available to the team.
- Issues: https://github.com/stellar-scaffold/cli/issues/448,
  https://github.com/stellar-scaffold/cli/issues/479
- Ecosystem value: lets us (and SCF) evaluate Scaffold's actual ecosystem impact quantitatively and
  prioritize future work by evidence.

### D11 (Stretch): Interactive OpenZeppelin contract wizard

- An interactive CLI mirroring wizard.openzeppelin.com for adding OZ-based contracts to a Scaffold
  project (building on the draft in https://github.com/stellar-scaffold/cli/pull/391).
- Measure: feature shipped, tested, and documented.
- Issue: https://github.com/stellar-scaffold/cli/issues/156
- Ecosystem value: safe, audited building blocks become the path of least resistance for new
  contracts.

### D12 (Stretch): Update starter app's Debug page

- Improve the generated app's contract Debug page: clearer results display, additional transaction
  details, and a persistent block-explorer link.
- Measure: updated Debug page shipped in templates.
- Issue: https://github.com/stellar-scaffold/cli/issues/248
- Ecosystem value: the Debug page is many builders' first contract interaction; better feedback loops
  mean faster learning.

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Ascaffold_stellar&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Ascaffold_stellar)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Ascaffold_stellar&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Ascaffold_stellar)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Ascaffold_stellar&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Ascaffold_stellar)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Ascaffold_stellar&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Ascaffold_stellar)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
