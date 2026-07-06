---
title: "Stellar Registry"
parent: Public Good Projects
proposal_issue: 64
proposer: chadoh
category: "Developer Experience"
budget: "50000"
---

# Stellar Registry

<!-- markdownlint-disable MD036 -->

_Stellar Registry is an on-chain smart contract registry for Soroban that lets developers publish,
version, discover, and deploy Wasm binaries and contract instances, making contracts reusable across
the ecosystem like packages._

<!-- markdownlint-enable MD036 -->

|                      |                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| **Category**         | Developer Experience                                                                               |
| **Website**          | <https://rgstry.xyz>                                                                               |
| **Repository**       | <https://github.com/stellar-registry>                                                              |
| **First Released**   | March 2026                                                                                         |
| **Intake**           | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/23> |
| **Budget Requested** | 50000                                                                                              |

## Project Description

<!-- markdownlint-disable MD034 -->

Registry is the missing infrastructure layer between "I wrote a smart contract" and "the ecosystem
can safely use my smart contract."

Registry tracks two things:

1. **Contracts**: Registry gives contracts human-friendly _names_, rather than gobbledigook IDs, as
   well as tracking a contract's owner and its _Wasm_.
2. **Wasms**: Stellar separates a contract _instance_, if you will (see item 1), from the WebAssembly
   (Wasm) binary that defines its behavior. Many contracts can use the same Wasm binary, but today
   that's impractical because Wasms are identified only by a gobbledigook ID.

Registry makes these usable. It gives them both names and _versions_, making the development
experience feel like familiar package management—like crates.io or NPM.

<!-- markdownlint-enable MD034 -->

## Team & Experience

<!-- markdownlint-disable MD034 -->

Scaffold Stellar is built and maintained by **The Aha Company** (formerly Aha Labs), a team of 10+
senior engineers deeply embedded in the Stellar ecosystem.

**Early Soroban origin:**

In 2022 (before Soroban had a name) SDF already had a clear ambition: launch their upcoming smart
contract platform with a “batteries-included” developer experience. The gap was execution capacity:
there was no in-house team available to design and implement the developer workflows needed to make
that promise real. Tyler van der Hoeven went to major blockchain conferences to find the right team,
and identified **The Aha Company** as the team with the right combination of product mindset and deep
technical ability to “install the batteries.”

**Foundational Stellar developer workflows we designed and shipped:**

We envisioned, architected, and implemented several of the workflows that have become core to Soroban
development on Stellar, including:

- **Stellar CLI smart contract workflows,** such as the `contract invoke` behavior and associated
  developer ergonomics that leapfrog, rather than ape, other blockchain ecosystems, simplifying
  testing, deployment, and interaction.
- **JavaScript developer experience patterns,** including the **Contract Client** behavior in
  **stellar-sdk-js**, which helps application developers interact with contracts more safely and
  predictably.

**Why we were selected for Scaffold Stellar and our SCF track record:**

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

**Ongoing maintenance and production-grade integration experience:**

Since then, we have remained engaged with SDF to support and maintain key tooling (most recently
improving Stellar CLI handling of **hardware-based keys**) and we continue to operate as an
integration partner on production deployments. Notably, we **architected and developed Société
Générale’s EURCV** on Stellar (now live), bringing a rigorous, real-world perspective to developer
tooling and reliability requirements.

**Deep community participation and ecosystem leadership:**

Our team includes well-known ecosystem contributors. Several members hold key community roles (e.g.,
**SCF Pilot**, **category delegates**) and actively build their own SCF projects (e.g., **Moonlight,
Tansu, Stellar Merch Store, PG Atlas**). We contribute to protocol and tooling discussions, provide
developer support at hackathons and conferences, and invest heavily in community outreach and
education. We show up consistently at major events and actively communicate about Stellar, both its
strengths and the practical realities builders need to know.

**Cross-ecosystem perspective (DevX benchmarking):**

Beyond Stellar, The Aha Company is also an integration partner in other ecosystems (e.g., **Filecoin,
XRPL, Cardano, Canton, Starknet**). This gives us a unique ability to benchmark developer experience
across chains and bring proven patterns back to Stellar—while keeping Scaffold Stellar aligned with
what developers expect from modern, full-stack tooling.

<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->

In Q2 2026 the Registry grew from a testnet prototype into production infrastructure — deployed to
mainnet at the close of the quarter — with its own organization, on-chain governance, verified
builds, and a real data platform behind rgstry.xyz.

**The Registry is live on mainnet.** The registry contract is deployed to Stellar mainnet at its
deterministic, salt-derived ID `CDU4M3LDIOUJJ5F3YXKJ4EJEP5VPRPG6N2LJ5HOQIMN7MNGL3NS3EGUY` (baked into
the CLI) via the phased deploy pipeline (stellar-registry/contracts#14, merged 2026-07-06), seeded
with verified ecosystem contracts (circle, soroswap, blend, defindex, xlm). The mainnet indexer
pipeline and the rgstry.xyz mainnet cutover are rolling out this week.

**Registry became standalone infrastructure.** The Registry was split out of the
theahaco/scaffold-stellar monorepo into its own GitHub organization,
[github.com/stellar-registry](https://github.com/stellar-registry), with four repos — `cli`,
`contracts`, `ui`, and `indexer` — each with full history preserved, scoped CI, dependabot, and
rewritten documentation. The Registry now stands on its own, as promised in our Q2 proposal ("the
Registry stands independently and is designed to serve the entire Soroban developer community").

**Five on-chain registry releases.** Registry contract versions v0.5.0 through v0.6.2 shipped in
April, adding contract flagging with a gas-optimized storage encoding (unflagged entries pay zero
overhead on the hot invocation path), `SubRegistry` events, cross-registry deploys
(`deploy_with_subregistry`) that record provenance on Deploy events, deterministic salt-derived
contract IDs, and dry-run deploy options.

**On-chain governance shipped.** The Tansu-DAO-gated registry manager contract merged
(stellar-registry/contracts#5): a manager whose `trigger(proposal_id)` entry point executes an
approved Tansu DAO proposal (e.g. `registry.publish_hash` / `registry.deploy`) in a single
transaction. Verified live end-to-end on testnet: proposal → vote → trigger → publish, with
replay-guard rejection confirmed.

**Verified builds are live.** We adopted the stellar-expert/soroban-build-workflow for releases
(stellar-registry/contracts#10), replacing 243 lines of bespoke CI with environment-gated, OIDC
build-provenance-attested releases, and published the first verified build of the registry contract.
We also submitted a Contract Source Verification Service RFP to the SCF Build Award RFP track and
collaborated with Ethan Frey (Confio) on its technical architecture.

**The indexer went v1.** The first mainnet-ready pipeline & API (stellar-registry/indexer#5) moved
data into a versioned schema, added auto-discovery of named subregistries (oz, blend, soroswap,
defindex), and grew an archive pipeline exposing full per-contract version history
(stellar-registry/indexer#14). June added structured logging with request-id tracing and a trigram
index enabling fuzzy server-side search (stellar-registry/indexer#23).

**rgstry.xyz matured.** The UI gained a testnet/mainnet network switch with per-environment
Cloudflare Worker deploys, in-UI usage guides for the import macros, README/LICENSE rendering from a
contract's GitHub repo, contract metadata on detail pages, server-side search, and request-id-traced
error reporting — 18 merged PRs in the quarter.

**Releases and toolchain.** Crates published: `stellar-registry` v0.0.8–v0.0.10,
`stellar-registry-cli` v0.0.20/v0.0.21, `stellar-registry-build` v0.0.8. The contracts moved to
soroban-sdk v27 / stellar-cli v27 (stellar-registry/contracts#11); the CLI's v27 migration is in
review (stellar-registry/cli#13). Registry intake forms are now CI-validated with strkey, sha256, and
semver validators and IssueOps labeling.

<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

Every deliverable below has merged, verifiable work behind it this quarter; where release mechanics
remain, the item states exactly what is left. We also shipped substantial infrastructure beyond the
proposed scope — see "Beyond the proposal" at the end of this section.

### D1. Mainnet Deploy of Stellar Registry

Description from last quarter:

> Deploy the Registry smart contract to Stellar mainnet and confirm it is publicly accessible via
> `stellar registry` CLI and `rgstry.xyz`.
>
> Measure: the contract is deployed & the CLI points to it.

Proof of completion:

- https://stellar.expert/explorer/public/contract/CDU4M3LDIOUJJ5F3YXKJ4EJEP5VPRPG6N2LJ5HOQIMN7MNGL3NS3EGUY
  — the registry contract live on mainnet at its deterministic, salt-derived ID
- https://github.com/stellar-registry/contracts/pull/14 — merged 2026-07-06: phased,
  dry-run-by-default `deploy_mainnet.sh` plus verified mainnet seed data (circle, soroswap, blend,
  defindex, xlm), with every contract ID resolved from authoritative sources and confirmed live on
  Pubnet
- https://github.com/stellar-registry/indexer/pull/5 — "the first mainnet-ready pipeline & API"
- https://github.com/stellar-registry/ui/pull/1 — testnet/mainnet network switch and per-environment
  Cloudflare Worker deploys; Mainnet UI scaffolding at stellar.rgstry.xyz

**Deployed to mainnet.** The phased deploy pipeline merged and executed at the close of the quarter:
the registry contract is live on Pubnet at its deterministic ID, seeded with verified ecosystem
contracts, and resolvable via the `stellar registry` CLI (the mainnet ID ships baked into the CLI).
Remaining for full public accessibility: the mainnet indexer pipeline and pointing rgstry.xyz at
mainnet — rolling out this week — plus secure-store/Ledger signing for admin operations
(stellar-registry/cli#14).

### D2. `import_contract!` Macro

Description from last quarter:

> Publish a working `import_contract!` macro in the `stellar-registry` crate that allows
> cross-contract client instantiation with a single line of Rust.
>
> Measure: the macro is available in a released crate version, documented with at least one working
> example, and covered by integration tests.

Proof of completion:

- https://github.com/stellar-registry/cli/pull/17 — full implementation: a proc-macro crate where
  `stellar_registry::import_contract!(env, name)` returns a soroban Client pre-bound to the named
  contract's deployed address, resolved at build time, with 13 unit tests
- https://github.com/stellar-registry/ui/pull/6 — in-UI usage guides for the import macros
- https://github.com/stellar-registry/ui/pull/10 — real contract IDs in the macro examples shown on
  every contract page

**Shipped — release mechanics left.** The macro is implemented, tested (13 unit tests,
pedantic-clippy clean), and in final review, and rgstry.xyz already teaches developers how to use the
import macros on every contract page. The crates.io publish lands days into Q3.

### D3. Flagged Contract Enforcement at Build Time

Description from last quarter:

> Extend `import_contract!` and `import_contract_client!` to emit a compile-time error when the
> referenced Wasm or Contract is flagged in the Registry.
>
> Measure: a test exists that demonstrates a flagged contract causes a build failure, and the
> behavior is documented.

Proof of progress:

- https://github.com/stellar-registry/contracts/commit/de06277 — on-chain contract flagging with a
  gas-optimized storage encoding (flag encoded in vec length, so unflagged entries pay zero overhead
  on the hot path), `FlagContract` events, and error types
- https://github.com/stellar-registry/cli/commit/1413f7f — registry intake CI validation (strkey,
  sha256, semver validators with IssueOps labeling), the curation pipeline enforcement sits on

**On-chain half shipped; compile-time half sequenced by design.** Flag storage, `FlagContract`
events, and error types shipped in April. The build-time check extends `import_contract!` (D2), so it
was deliberately sequenced behind that macro's implementation and follows it in early Q3.

### D4. Server-Side Search, Pagination & Sorting on rgstry.xyz

Description from last quarter:

> Replace the current client-side full-data-fetch approach with API-backed search, pagination, and
> sorting on `rgstry.xyz`.
>
> Measure: the explorer handles at least 1,000 published Wasms/Contracts without degraded load time,
> search returns results server-side, and pages load incrementally.

Proof of completion:

- https://github.com/stellar-registry/indexer/pull/23 — trigram index enabling fuzzy server-side
  search
- https://github.com/stellar-registry/ui/pull/21 — wasm list wired to the backend search API with a
  debounced search hook
- https://github.com/stellar-registry/indexer/pull/24 — (open) extends trigram/full-text search to
  the contracts table

**Shipped for Wasms — live in production.** Server-side fuzzy search is merged and answering queries
on rgstry.xyz today, and the API already supports limit/cursor pagination. Remaining: the same
treatment for contracts (stellar-registry/indexer#24, open), the explorer's pagination/sorting UX,
and validation against a 1,000+ entry dataset.

### D5. rgstry.xyz UI Enhancements

Description from last quarter:

> Ship three specific improvements to the Registry web explorer:
>
> 1. Contract Explorer embedded on contract detail pages
> 2. `stellar contract info meta` metadata surfaced on Wasm and Contract detail pages
> 3. A "deploy this Wasm" button that initiates a Registry deploy from the UI
>
> Measure: all three features are live on the production `rgstry.xyz` site and manually verified
> against at least one mainnet contract.

Proof of completion:

- https://github.com/stellar-registry/indexer/pull/15 — `stellar contract info meta` metadata parsed
  and exposed in the wasm-detail API (item 2, backend half — the API serves rsver, SDK, CLI, and
  build versions plus source repo)
- https://github.com/stellar-registry/ui/pull/13 — README.md and LICENSE fetched and rendered from a
  contract's GitHub repo
- https://github.com/stellar-registry/ui/pull/18 — request-id-traced error reporting

**Backend and page richness shipped.** The metadata API (item 2's backend) is live and serving the
full `contract info meta` fields, and contract pages gained README/LICENSE rendering and traceable
error reporting beyond the proposed scope. Remaining: surfacing the rest of the metadata fields in
the UI, the embedded Contract Explorer (item 1), and the deploy button (item 3) — the latter now has
a clearer path via the governance proposal forms in stellar-registry/ui#16.

### D6. Verified Build Integration with Stellar Expert

Description from last quarter:

> Display verified build status from Stellar Expert's API on Registry Wasm and Contract detail pages.
>
> Measure: the verified build badge or indicator is visible on at least one Wasm detail page with a
> known verified contract, and the integration is live in production on `rgstry.xyz`.

Proof of completion:

- https://github.com/stellar-registry/contracts/pull/10 — releases now use the
  stellar-expert/soroban-build-workflow: environment-gated, with OIDC build-provenance attestation
- https://github.com/stellar-registry/contracts/releases — first verified build of the registry
  contract published
- https://github.com/stellar-registry/cli/pull/9 — Contract Source Verification Service RFP submitted
  to the SCF Build Award RFP track, with architecture collaboration from Ethan Frey (Confio)
  (stellar-registry/cli#11, #12)

**Shipped — Registry releases are themselves verified builds.** Every registry contract release is
now built by the stellar.expert workflow with OIDC build-provenance attestation, and the first
attested release is public. Remaining: displaying the badge on rgstry.xyz detail pages — targeting
contract pages, since we established Stellar Expert has no Wasm-level pages (stellar-registry/ui#17).

### D7. Registry Documentation & Education

Description from last quarter:

> Publish complete Registry documentation and videos covering:
>
> - publishing a Wasm
> - deploying a named contract
> - using `import_contract!`
> - deploying an unnamed contract
> - publishing/releasing using CI workflow
> - more!
>
> Measure: documentation is live on Registry's own docs site & The Aha Company's YouTube channel.

Proof of completion:

- https://scaffoldstellar.org/docs/registry — the Registry Guide is live (overview,
  verified/unverified registries, name resolution, publish/deploy CLI usage) and linked as "Guide"
  from the rgstry.xyz nav
- https://github.com/stellar-registry/ui/pull/6 — in-UI usage guides for the import macros, shown on
  every contract and wasm page
- https://github.com/stellar-registry/cli — README and contributor docs rewritten for the standalone
  repo (likewise for contracts, ui, and indexer)
- https://github.com/stellar-registry/cli/pull/17 — design spec and implementation plan documents for
  `import_contract!`

**Docs shipped in the product; the guide is live.** The Registry Guide is live and linked from the
rgstry.xyz nav, every contract and wasm page carries usage guides, and all four standalone repos got
rewritten documentation. Remaining: moving the guide to Registry's own docs site, `import_contract!`
coverage (follows the D2 release), and the video series.

### Beyond the proposal

Infrastructure we shipped this quarter that was not in the Q2 deliverables:

- **Standalone organization**: the Registry split out of the scaffold-stellar monorepo into
  https://github.com/stellar-registry — four repos (cli, contracts, ui, indexer) with full history
  preserved, scoped CI, and dependabot.
- **On-chain governance**: the Tansu-DAO-gated registry manager contract
  (stellar-registry/contracts#5), merged and verified live on testnet end-to-end (proposal → vote →
  trigger → publish, replay-guard confirmed).
- **Protocol currency**: contracts migrated to soroban-sdk v27 / stellar-cli v27
  (stellar-registry/contracts#11); the CLI's v27 migration is in review (stellar-registry/cli#13).
- **Registry intake pipeline**: CI-validated intake forms with strkey, sha256, and semver validators
  and IssueOps labeling.
- **Contract version history**: an archive indexer pipeline capturing factory-pattern deploys and
  exposing full per-contract version history (stellar-registry/indexer#14).
- **Source verification RFP**: a Contract Source Verification Service RFP submitted to the SCF Build
  Award track, with architecture collaboration from Ethan Frey (Confio).

<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

**Complete the mainnet launch.** The Registry contract is live on mainnet as of this proposal. Q3
finishes the public rollout: the mainnet indexer pipeline, rgstry.xyz serving mainnet data with the
"Coming Soon" banner removed, and secure-store/Ledger signing for admin operations
(stellar-registry/cli#14) so permanent ecosystem infrastructure is never administered from a raw
secret key — alongside the Tansu DAO-gated governance already in place.

**Complete the composability story.** Releasing `import_contract!` (stellar-registry/cli#17) lets any
Soroban developer depend on Registry contracts the way they depend on Rust crates, and the
flagged-contract build-time enforcement extends that with compile-time guarantees that compromised
contracts won't ship.

**Make rgstry.xyz a real discovery platform.** Finish server-side search across contracts and Wasms,
pagination and sorting, verified-build badges from Stellar Expert, and governance proposal forms that
let anyone propose adding a Wasm or contract to the root registry directly from the browser — closing
the loop from "found a contract" to "deployed it" without leaving the site.

**Benefit to the Stellar ecosystem:** The Registry is ecosystem infrastructure, not a product
feature. A mainnet Registry with DAO governance, verified builds, and compile-time safety raises the
baseline security and auditability of every Soroban project that consumes shared contracts, and gives
the ecosystem its first crates.io-style package experience for on-chain code.

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

### D1: Complete the Mainnet Launch (carried from Q2)

With the registry contract live on mainnet, finish the public rollout: run the mainnet indexer
pipeline, point rgstry.xyz at the mainnet API and remove the "Coming Soon" banner, and land
secure-store/Ledger signing in the CLI (stellar-registry/cli#14) so admin operations never expose a
raw secret key.

Proof: mainnet data live and browsable at rgstry.xyz, the contract visible on Stellar Expert, and
named contracts resolvable via `stellar registry` CLI.

### D2: Release `import_contract!` (carried from Q2)

Merge stellar-registry/cli#17 and publish the macro in released crates, documented with at least one
working example and covered by integration tests.

Proof: a crates.io release containing `import_contract!`, linked docs and example, CI running the
integration tests.

### D3: Flagged Contract Enforcement at Build Time (carried from Q2)

Extend `import_contract!` / `import_contract_client!` to fail compilation when the referenced Wasm or
Contract is flagged in the Registry, building on the on-chain flagging that shipped in April.

Proof: a test demonstrating a flagged contract causes a build failure, and documented behavior.

### D4: Finish Search, Pagination & Sorting on rgstry.xyz (carried from Q2)

Extend server-side search to contracts (stellar-registry/indexer#24), fix search-result updating
(stellar-registry/ui#22), and ship pagination and sorting so the explorer handles 1,000+ entries
without degraded load time.

Proof: live on rgstry.xyz; search, pagination, and sorting demonstrated against a 1,000+ entry
dataset.

### D5: Contract Explorer, Deploy Button & Verified-Build Badges (carried from Q2)

Ship the remaining explorer features: the embedded Contract Explorer on contract detail pages, a
"deploy this Wasm" button, the remaining `stellar contract info meta` fields surfaced on detail
pages, and verified-build status from Stellar Expert on contract detail pages.

Proof: all features live on production rgstry.xyz, manually verified against at least one mainnet
contract.

### D6: Governance Operations UI

Ship the governance proposal forms (stellar-registry/ui#16): propose adding a Wasm or contract to the
root registry, creating a subregistry, or changing owners — executed through the Tansu-DAO-gated
registry manager contract that merged in Q2.

Proof: a governance proposal created from rgstry.xyz, voted on in Tansu, and executed on-chain via
`trigger`, with the transaction linked.

### D7: Registry Documentation & Education (carried from Q2)

Publish the Registry docs site and video series covering publishing a Wasm, deploying named and
unnamed contracts, using `import_contract!`, and publishing/releasing via the verified-build CI
workflow.

Proof: documentation live on the Registry docs site and videos on The Aha Company's YouTube channel.

<!-- markdownlint-enable MD034 -->

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
