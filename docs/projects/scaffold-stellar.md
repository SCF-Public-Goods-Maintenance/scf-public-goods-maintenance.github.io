---
title: "Scaffold Stellar"
parent: Public Good Projects
proposal_issue: 62
proposer: chadoh
category: "Developer Experience"
budget: "50000"
---

# Scaffold Stellar

_Go from idea to app faster with a custom, pluggable CLI; industry-redefining composability powered
by Stellar Registry; and a customizable, modern frontend._

|                      |                                                 |
| -------------------- | ----------------------------------------------- |
| **Category**         | Developer Experience                            |
| **Website**          | <https://scaffoldstellar.org/>                  |
| **Repository**       | <https://github.com/theahaco/scaffold-stellar/> |
| **First Released**   | May 2025                                        |
| **Intake**           | soft-launch                                     |
| **Budget Requested** | 50000                                           |

## Project Description

Scaffold Stellar is an open-source developer toolkit for building decentralized applications (dApps)
and smart contracts on the Stellar blockchain. It helps developers go from idea to working full-stack
dApp faster by providing CLI tools, reusable contract templates, integration with Stellar Registry,
and a modern customizable frontend.

## Team & Experience

Scaffold Stellar is built and maintained by **The Aha Company** (formerly Aha Labs), a team of 10+
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

## Why we were selected for Scaffold Stellar and our SCF track record

In early 2025, SDF searched for a team that could bring a ScaffoldETH-like end-to-end experience to
Stellar. They selected us based on:

1. our deep **CLI & JS expertise** proven through shipped core tooling, and
2. our track record delivering developer infrastructure via SCF, including:
   - **Smart Deploy**:
     [https://communityfund.stellar.org/project/smart-deploy-yoj](https://communityfund.stellar.org/project/smart-deploy-yoj)
   - **Loam**:
     [https://communityfund.stellar.org/project/loam-qj5](https://communityfund.stellar.org/project/loam-qj5)

Scaffold Stellar is a direct continuation of that work: turning the hard-won Developer Experience
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
across chains and bring proven patterns back to Stellar—while keeping Scaffold Stellar aligned with
what developers expect from modern, full-stack tooling.

## Retroactive Impact

- Scaffold Stellar is in the "recommended resources" for all Stellar hackathons, and was used heavily
  (and enjoyed) in the Mexico City hackathon in March. -Shipped Testnet Registry frontend (current
  URL: https://testnet.rgstry.xyz/) and added relevant Testnet contracts & Wasms to it ahead of
  Mexico City hackathon, as requested by SDF DevRel
- Recommended in
  [the official SKILL](https://github.com/stellar/stellar-dev-skill/blob/main/skill/resources.md).

## Past Deliverables

## Workstream 1 - Stellar Contract Registry: Launch + Trust + Reproducibility

### D1. Registry UI (beta) shipped and publicly deployed

> - Deliver a frontend for exploring and consuming contracts (search/browse, contract pages,
>   provenance/metadata, usage instructions).
> - Measure: UI deployed to a public URL + documented usage flows.
> - Issue: https://github.com/theahaco/scaffold-stellar/issues/169
> - Ecosystem value: makes contract discovery and reuse real for app developers; reduces repeated
>   reinventing of standard components.

Testnet Registry frontend is live at https://testnet.rgstry.xyz/

### D2. Namespaces + Security Council operationalization

> - Ship namespace support and publish a clear policy/process for trusted namespaces, backed by an
>   active security council.
> - Measure: namespaces live + published policy + initial set of trusted namespaces created.
> - Issue: https://github.com/theahaco/scaffold-stellar/issues/22
> - Ecosystem value: reduces name-squatting/confusion and establishes a trust layer for contract
>   reuse.

Wasms and contracts can only be deployed to `unverified` namespace by general users; find
`unverified` Wasms & contracts in the testnet registry with the `unverified/` channel prefix. These
are tracked by a separate registry contract that is itself registered in the root/main registry with
the name `unverified` (https://testnet.rgstry.xyz/contracts/unverified). This same sub-registry
prefixing strategy will be used in mainnet (https://github.com/theahaco/scaffold-stellar/issues/433)
to create dedicated sub-registries / prefixes for popular ecosystem projects & partners like `oz`,
`blend`, and `defindex`. While the root / main registry contract is managed by the Registry Security
Council multisig wallet, these other subregistries will be managed by each ecosystem's own wallet
(whether or not they use multisig is up to them).

### D3. Registry documentation and publishing/consumption flows

> - Publish comprehensive docs for publishing and consuming contracts via CLI/Rust SDK; include
>   security model and best practices.
> - Measure: docs live + linked from scaffoldstellar.org + examples runnable end-to-end.
> - Issue: https://github.com/theahaco/scaffold-stellar/issues/102
> - Ecosystem value: lowers onboarding friction and makes registry usage self-serve.

Registry documentation exists at https://scaffoldstellar.org/docs/registry, which is also linked from
top navigation bar on https://testnet.rgstry.xyz/. Additionally, the Registry web app also shows how
to use registered contracts; see https://testnet.rgstry.xyz/contracts/unverified for an example.

### D4. Supply-chain safety design implemented

> - Implement mitigations and clear behavior for common supply-chain risks (e.g., name confusion,
>   publisher ambiguity), building on the “supply chain brainstorming” work.
> - Measure: documented threat model + implemented checks/UX cues + test coverage.
> - Issue: https://github.com/theahaco/scaffold-stellar/issues/350
> - Ecosystem value: improves ecosystem security posture as reuse increases.

"Flagging" behavior agreed upon by SDF project manager (Steph). "Registry as cross-contract proxy"
functionality implemented in https://github.com/theahaco/scaffold-stellar/pull/461. Additional
functionality based on contract & wasm flagging to be implemented in Q2,
https://github.com/theahaco/scaffold-stellar/issues/452, then communicated to ecosystem.

### D5. Reset/reseed tooling for testnet & futurenet

> - Provide deterministic redeploy/reseed workflows for well-known contracts and registry state after
>   network resets.
> - Measure: scripts + runbook + successful internal dry-run demonstration.
> - Issues: https://github.com/theahaco/scaffold-stellar/issues/330 and
>   https://github.com/theahaco/scaffold-stellar/issues/21
> - Ecosystem value: removes recurring ecosystem friction; supports all builders, not just Scaffold
>   users.

Implemented in https://github.com/theahaco/registry-indexer/pull/3; to be tested during next Testnet
reset.

### D6. Publish standard OpenZeppelin-based contracts into the registry

> - Deploy and register canonical standard contracts (with provenance metadata) as safe building
>   blocks.
> - Measure: at least a defined set of standard contracts available with documentation and example
>   usage.
> - Issue: https://github.com/theahaco/scaffold-stellar/issues/168
> - Ecosystem value: safer defaults and faster iteration for most new apps.

See `oz-` prefixed Wasms here: https://testnet.rgstry.xyz/wasms

## Workstream 2 - Scaffold Stellar Extension/Plugin System + Integrations

### D7. Extension/Plugin system shipped

> - Define and implement an extension interface that allows third parties to integrate services
>   without forking core Scaffold.
> - Measure: extension API spec + developer docs + at least 2 reference extensions.
> - Issue:
>   [https://github.com/theahaco/scaffold-stellar/issues/160](https://github.com/theahaco/scaffold-stellar/issues/160)
> - Ecosystem value: turns Scaffold Stellar into a distribution surface for other public goods and
>   ecosystem tooling.

Core extension system shipped in https://github.com/theahaco/scaffold-stellar/pull/414; reporter
extension shipped in https://github.com/theahaco/scaffold-stellar/pull/463.

D8. Wallet integration expansion via wallet kit

> - Support additional wallets in the default scaffolded apps through wallet kit integration and
>   configuration templates.
> - Measure: additional wallet support shipped + documented setup + example project(s).
> - Issue:
>   [https://github.com/theahaco/scaffold-stellar-frontend/issues/93](https://github.com/theahaco/scaffold-stellar-frontend/issues/93)
> - Ecosystem value: reduces onboarding friction and enables broader end-user compatibility for new
>   dApps.

Support for all wallet modules shipped in
https://github.com/theahaco/scaffold-stellar-frontend/pull/204.

### D9. Indexing services and API integrations as extensions

> - Provide extensions for popular indexing services and explore integration of commonly requested
>   APIs (e.g., Soroswap API) as optional add-ons.
> - Measure: at least one indexing extension + one API integration prototype + docs.
> - Ecosystem value: makes it easy for teams to adopt ecosystem infrastructure from day one.

Extensively researched and built with Goldsky to build Stellar Registry UI, and determined this
offering is both too immature to build as a Scaffold Stellar Extension for now, as well as being too
much of an edge case for how the extension system ended up working. We now have prior art to use to
implement a Goldsky extension later, which is being tracked in
https://github.com/theahaco/scaffold-stellar/issues/164

## Workstream 3 - Core DX Improvements

### D10. New project page design update

> - Improve the first-run experience and reduce time-to-first-success for new builders.
> - Measure: new UX shipped + updated onboarding steps + reduced “setup steps” documented.
> - Issue:
>   [https://github.com/theahaco/scaffold-stellar-frontend/issues/136](https://github.com/theahaco/scaffold-stellar-frontend/issues/136)
> - Ecosystem value: faster onboarding and improved conversion for first-time Stellar developers.

Shipped in https://github.com/theahaco/scaffold-stellar-frontend/pull/158

### D11. Import existing Soroban contracts into Scaffold projects

> - Enable importing contracts from existing Soroban contract sources to accelerate development and
>   reuse.
> - Measure: working import workflow + docs + example.
> - Issue:
>   [https://github.com/theahaco/scaffold-stellar/issues/151](https://github.com/theahaco/scaffold-stellar/issues/151)
> - Ecosystem value: reinforces reuse and reduces redundant contract development.

Shipped in https://github.com/theahaco/scaffold-stellar/pull/327

### D12. stellar scaffold clean to improve iteration loops

> - Allow developers to clear scaffold artifacts in the dev environment to reduce friction and avoid
>   state-related confusion.
> - Measure: command shipped + tests + docs.
> - Issue:
>   [https://github.com/theahaco/scaffold-stellar/issues/259](https://github.com/theahaco/scaffold-stellar/issues/259)
> - Ecosystem value: improves productivity and reduces support burden.

The command was shipped here: https://github.com/theahaco/scaffold-stellar/pull/352

## Maintenance, Release Management, and Community Support

### D13. Ongoing maintenance, releases, and field feedback loop

> - Keep templates current (including OpenZeppelin updates), ship releases, triage issues/PRs, and
>   collect feedback from builders at upcoming events.
> - Measure: regular tagged releases + changelogs + public roadmap updates + documented learnings
>   from events.

See all our releases with notes at https://github.com/theahaco/scaffold-stellar/releases

## Proposed Impact

Scaffold Stellar has now launched Stellar Registry as a separate project, highlighting that this is
not merely a useful tool for learners and first-time Stellar builders. It's the foundation, the hub,
for much of the activity of the Stellar development community. With its recently-launched extension
system, Scaffold is poised to become the test ground, the proving site, for a diverse and composable
ecosystem of plugins, apps, and integrations.

This quarter we will continue to see Scaffold Stellar used as the entrypoint for the Stellar
ecosystem, both in documentation and at hackathons. The new extension system provides a focal point
for a themed hackathon of its own; we will advocate with DevRel to realize this. We will also reach
out to James Bachini to get Scaffold integrated directly into his web IDE, another project in this
Public Goods cohort.

## Proposed Deliverables

## D1: Support Stellar-Wallets-Kit v2

- Update to Stellar-Wallets-Kit v2, released v2 in Feb 2025, to streamline Developers' experience and
  keep up to date with the latest standards in the ecosystem.
- Measure: update shipped in frontend
- Issue: https://github.com/theahaco/scaffold-stellar/issues/441
- Ecosystem value: simplifies Scaffold codebase; keeps apps up-to-date with evolving ecosystem

## D2: Allow package manager of choice

- Rather than forcing people to use NPM with Scaffold, allow them to pick the JS package manager of
  their choosing (yarn, bun, deno, etc)
- Measure: feature shipped, tested, & documented
- Issue: https://github.com/theahaco/scaffold-stellar/issues/162
- Ecosystem value: Scaffold today locks users to npm. This is a reasonable default and a common
  preference, but the JS ecosystem is fractured, with many people preferring more recent package
  managers such as yarn, bun, and deno. Supporting these options within Scaffold prevents fracturing
  the Stellar ecosystem, enabling people to use Scaffold while keeping their preferred JS tooling.

## D3: BYOFrontend

- Create two new Aha-maintained Scaffold frontend plugins: 1. no frontend, 2. Svelte. In addition,
  create documentation for how community members can contribute their own frontend templates for use
  with Scaffold Stellar.
- Measure: feature shipped, tested, documented.
- Issue: https://github.com/theahaco/scaffold-stellar/issues/161
- Ecosystem value: Like D2, this allows people to use Scaffold Stellar even if they don't prefer its
  default options of React and Vite, making the entire stack opinionated but also flexible.

## D4: SKILL.md to help agentic workflows

- Add SKILL.md to Scaffold Stellar repository to facilitate more powerful and accurate AI & agentic
  workflows.
- Measure: feature shipped, tested, and documented.
- Issue: https://github.com/theahaco/scaffold-stellar/issues/394
- Ecosystem value: many hackathon participants and serious builders prefer to use AI tools in
  addition to, or rather than, coding by hand. This will make that experience more fool-proof and
  powerful, preventing AIs from making silly mistakes.

## D5: Improve Scaffold info on main Stellar docs

- Minimize the info on the Scaffold Stellar page on the main Stellar docs in line with other tools
  that have their own documentations sites, linking prominently to https://scaffoldstellar.org
- Measure: new documentation page shipped to main Stellar docs
- Issue: https://github.com/theahaco/scaffold-stellar/issues/361
- Ecosystem value: consolidate Scaffold documentation to a single place to minimize the amount of
  stale information and highlight important resources, such as the Scaffold Showcase.

## D6: Monitor releases of ecosystem projects

- For Scaffold itself and all projects that are built with it, provide automatic notifications
  (perhaps in the form of GitHub issues or pull requests) when complex ecosystem dependencies, such
  as Stellar-Wallets-Kit, are updated.
- Measure: system in place for notifying Scaffold team of ecosystem project updates
- Issue: https://github.com/theahaco/scaffold-stellar/issues/301
- Ecosystem value: These projects release their own updates, sometimes with breaking changes that
  could cause Scaffold Stellar to not work at all, or to be out of date with the latest releases of
  ecosystem projects. Updating the corresponding ecosystem project is not always as simple as
  "increment version number" (although sometimes it is), since, in Stellar Wallets Kit's example, the
  tool may be deeply integrated into Scaffold.

## D7: Allow building for testnet when localnet unhealthy

- Scaffold currently requires running a local Stellar network, which it can do automatically, even
  when building for a testnet target. We will fix this.
- Measure: bug fix shipped
- Issue: https://github.com/theahaco/scaffold-stellar/issues/267
- Ecosystem value: smoothing the rough edges of Scaffold Stellar makes it a more reliable,
  easy-to-use, mature offering, enabling more confident building.

## D8: Re-architect stellar scaffold build internals & update to latest best practices

- Various bugs and sub-optimal behavior can be pinned on some early, messy architectural decisions
  made in stellar-scaffold-cli, the core of which is now nearly a year old. We will rework this core
  logic to improve functionality, fix bugs, and adopt latest best practices. Some possible
  improvements: optimize contracts if stellar-cli built with optimize feature; specify contract from
  live network; rework entire environments.toml file name & structure.
- Measure: features shipped, tested, and documented.
- Issues: https://github.com/theahaco/scaffold-stellar/issues/329,
  https://github.com/theahaco/scaffold-stellar/issues/346,
  https://github.com/theahaco/scaffold-stellar/issues/181
- Ecosystem value: we've learned a lot since originally authoring Scaffold Stellar, and this will
  enable us to continue to iterate on it quickly over the next year, providing the ecosystem with a
  central tool that allows builders to quickly integrate various emerging solutions and best
  practices.

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
