---
title: "Stellar Registry"
canonical_id: daoip-5:scf:project:stellar_registry
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

Stellar Registry is built and maintained by **The Aha Company**, a team of 10+ senior engineers
deeply embedded in the Stellar ecosystem.

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
- **Stellar Scaffold**, helping newcomers, experts, and AI agents ship quickly, reduce bugs, and
  focus on app logic not nuts-and-bolts wiring and boilerplate.

**Deep community participation and ecosystem leadership:**

Our team includes well-known ecosystem contributors. Several members hold key community roles (e.g.,
**SCF Pilot**, **category delegates**) and actively build their own SCF projects (e.g., **Moonlight,
Tansu, Stellar Merch Store, PG Atlas, Turbolong**). We contribute to protocol and tooling
discussions, provide developer support at hackathons and conferences, and invest heavily in community
outreach and education. We show up consistently at major events and actively communicate about
Stellar, both its strengths and the practical realities builders need to know.

**Cross-ecosystem perspective (DevX benchmarking):**

Beyond Stellar, The Aha Company is also an integration partner in other ecosystems (e.g., **Filecoin,
XRPL, Cardano, Canton, Starknet**). This gives us a unique ability to benchmark developer experience
across chains and bring proven patterns back to Stellar—while keeping Stellar Registry aligned with
what developers expect from modern, full-stack tooling.

**Specific teammates assigned to Stellar Registry:**

In the latter half of 2026, the Stellar Registry team consists primarily of the following
individuals, in order of involvement:

- **Pam Selle** — @pselle • [LinkedIn](https://www.linkedin.com/in/pamelaselle/)
- **Willem Wyndham** — @willemneal • [LinkedIn](https://www.linkedin.com/in/willem-wyndham/)
- **Chad Ostrowski** — @chadoh • [LinkedIn](https://www.linkedin.com/in/chadoh/)
- **Zach Fedor** — @zachfedor • [LinkedIn](https://www.linkedin.com/in/zachfedor/) (limited to UI
  involvement on Registry for 2026 half 2)

<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->

In Q3 2026 the Registry finished its mainnet launch and grew from infrastructure you can query into a
toolkit developers can build with: `import_contract!` shipped in a released crate, rgstry.xyz became
a full discovery and deployment platform, and the governance machinery we built for Registry was
adopted upstream by Tansu for every project that uses it.

**The mainnet launch is complete.** Mainnet data is fully indexed in Goldsky
(stellar-registry/indexer#25) and served from https://stellar-registry-mainnet.fly.dev/.
[stellar.rgstry.xyz](https://stellar.rgstry.xyz) is now the primary subdomain (with rgstry.xyz
redirecting to it), the registry contract is visible on Stellar Expert, and every `stellar registry`
command works across both testnet and mainnet.

**Registry is now composable from Rust.** `import_contract!` is released, documented on
[crates.io](https://crates.io/crates/stellar-registry) and
[docs.rs](https://docs.rs/stellar-registry), and covered by unit tests that run on every commit.
Shipping it took two large re-architectures, the consolidation of the related
`import_contract_client!` and `import_asset!` macros into the Registry repo, and a new
[`stellar-registry-name`](https://crates.io/crates/stellar-registry-name) crate. With that release,
all Stellar Registry crates reached official beta at version 0.1.0. Compile-time safety came with it:
flagged contracts fail to resolve by default, proven by an integration test
(stellar-registry/cli#60). The macro also now handles Stellar Asset Contracts, so
`import_contract!(xlm)` and `import_contract!("circle/usdc")` work for any SAC registered in Registry
(stellar-registry/cli#64).

**rgstry.xyz became a real discovery platform.** Server-side fuzzy search now covers contracts as
well as Wasms (stellar-registry/indexer#24), e.g. every mainnet contract matching
[`kal`](https://stellar.rgstry.xyz/contracts?query=kal). Wasm pages gained a "deploy this Wasm" form
(stellar-registry/ui#23) and contract pages an embedded Contract Explorer (stellar-registry/ui#24).
Verified-build (SEP-55) badges from Stellar Expert data now appear on contracts
(stellar-registry/ui#57), and SEP-58 source-verification fields are surfaced on Wasm and contract
pages (stellar-registry/indexer#49, stellar-registry/ui#82, stellar-registry/ui#83).

**Governance became shared infrastructure.** A new Governance section on rgstry.xyz provides forms to
propose adding a contract to the root registry (stellar-registry/ui#67), adding a Wasm
(stellar-registry/ui#71), or creating a subregistry (stellar-registry/ui#81). Meanwhile, the
workaround we built last quarter to act on Tansu proposals was merged into Tansu itself (merged to
Tansu `main` 2026-09-02), builds against the real Tansu contract, and is documented in Tansu's
governance docs, so any ecosystem project can now use it. We deleted our duplicate
`registry-tansu-manager` and `tansu-stub` (stellar-registry/contracts#55).

**Secure CI publishing, and a new product.** The Registry contract now auto-publishes its Wasm on
commits to `main` (stellar-registry/contracts#53). Keeping keys on GitHub safe led us to design and
ship [Perch](https://github.com/stellar-registry/perch), a composable policy layer for Soroban smart
accounts.

**Also shipped.** Foundational support for named G-addresses in the registry contract
(stellar-registry/contracts#37, stellar-registry/contracts#38); full contract version history on
contract detail pages (stellar-registry/ui#40); a
[Stellar Registry Full Walk-Through video](https://www.youtube.com/watch?v=xAlWmJOdMSQ) on The Aha
Company's YouTube channel; and a new logo and consolidated documentation.

<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

### 2026 Q2

Every deliverable below has merged, verifiable work behind it this quarter; where release mechanics
remain, the item states exactly what is left. We also shipped substantial infrastructure beyond the
proposed scope — see "Beyond the proposal" at the end of this section.

#### D1. Mainnet Deploy of Stellar Registry

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
the registry contract is live on mainnet at its deterministic ID, seeded with verified ecosystem
contracts, and resolvable via the `stellar registry` CLI (the mainnet ID ships baked into the CLI).
Remaining for full public accessibility: the mainnet indexer pipeline and pointing
[rgstry.xyz](https://rgstry.xyz) at mainnet — rolling out this week — plus secure-store/Ledger
signing for admin operations (stellar-registry/cli#14).

#### D2. `import_contract!` Macro

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

#### D3. Flagged Contract Enforcement at Build Time

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
- https://github.com/stellar-registry/cli/pull/17 – PR for D2 implements compile-time error
  mechanics, preventing contracts from building when their source contracts have been flagged.

#### D4. Server-Side Search, Pagination & Sorting on rgstry.xyz

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

#### D5. rgstry.xyz UI Enhancements

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
- https://github.com/stellar-registry/ui/pull/23 — (open) form for deploying unnamed (unregistered)
  contract from a Wasm detail page, shipping days into Q3
- https://github.com/stellar-registry/ui/pull/24 — (open) form for interacting with a deployed
  contract from its rgstry.xyz detail page, shipping days into Q3

**Backend and page richness shipped.** The metadata API (item 2's backend) is live and serving the
full `contract info meta` fields, and contract pages gained README/LICENSE rendering beyond the
proposed scope. Remaining: surfacing the rest of the metadata fields in the UI, the embedded Contract
Explorer (item 1), and the deploy button (item 3).

#### D6. Verified Build Integration with Stellar Expert

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

#### D7. Registry Documentation & Education

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

#### Beyond the proposal

Infrastructure we shipped this quarter that was not in the Q2 deliverables:

- **Standalone organization**: the Registry split out of the scaffold-stellar monorepo into
  https://github.com/stellar-registry — four repos (cli, contracts, ui, indexer) with full history
  preserved, scoped CI, and dependabot.
- **On-chain governance**: the Tansu-DAO-gated registry manager contract
  (stellar-registry/contracts#5), merged and verified live on testnet end-to-end (proposal → vote →
  trigger → publish, replay-guard confirmed).
- **Protocol currency**: contracts migrated to soroban-sdk v27 / stellar-cli v27
  (stellar-registry/contracts#11; stellar-registry/cli#13).
- **Contract version history**: an archive indexer pipeline capturing factory-pattern deploys and
  exposing full per-contract version history beyond Registry's existence
  (stellar-registry/indexer#14).
- **Source verification RFP**: a Contract Source Verification Service RFP submitted to the SCF Build
  Award track, with architecture collaboration from Ethan Frey (Confio).

### 2026 Q3

#### ✅ D1: Complete the Mainnet Launch (carried from Q2)

Description from last quarter:

> With the registry contract live on mainnet, finish the public rollout: run the mainnet indexer
> pipeline, point rgstry.xyz at the mainnet API and remove the "Coming Soon" banner, and land
> secure-store/Ledger signing in the CLI (stellar-registry/cli#14) so admin operations never expose a
> raw secret key.
>
> Proof: mainnet data live and browsable at rgstry.xyz, the contract visible on Stellar Expert, and
> named contracts resolvable via `stellar registry` CLI.

**✅ Complete:**

- Mainnet data is now fully indexed in Goldsky (https://github.com/stellar-registry/indexer/pull/25)
  and queryable via API calls at https://stellar-registry-mainnet.fly.dev/
- [stellar.rgstry.xyz](https://stellar.rgstry.xyz) now live as the "primary" subdomain (with
  [rgstry.xyz](https://rgstry.xyz) redirecting to it)
- [Registry contract](https://stellar.rgstry.xyz/contracts/registry) visible
  [on Stellar Expert](https://stellar.expert/explorer/public/contract/CDU4M3LDIOUJJ5F3YXKJ4EJEP5VPRPG6N2LJ5HOQIMN7MNGL3NS3EGUY)
- All `stellar registry` commands working across both testnet and mainnet (see @kalepail's request at
  stellar-registry/gov#1 as proof)

#### ✅ D2: Release `import_contract!` (carried from Q2)

Description from last quarter:

> Merge stellar-registry/cli#17 and publish the macro in released crates, documented with at least
> one working example and covered by integration tests.
>
> Proof: a crates.io release containing `import_contract!`, linked docs and example, CI running the
> integration tests.

**✅ Complete:**

The macro has landed! This was a hefty engineering task that entailed two large-scale
re-architectures, code consolidation from other repositories (`stellar-scaffold/cli` repo is no
longer the home of related macros `import_contract_client!` and `import_asset!`), and the creation of
a new [`stellar-registry-name` crate](https://crates.io/crates/stellar-registry-name). With this
release, we declared all Stellar Registry crates to have reached official beta, marking them all as
[version 0.1.0](https://github.com/stellar-registry/cli/releases).

- See `import_contract!` documentation and examples at both
  [crates.io](https://crates.io/crates/stellar-registry) and
  [docs.rs](https://docs.rs/stellar-registry)
- Comprehensive unit tests for `import_contract!` added in macro's
  [introductory PR at `crates/stellar-registry-macro/src/contract.rs`](https://github.com/stellar-registry/cli/pull/17/changes#diff-c9fd228d9177e15a059824ea2767bae20b7a7a80a87ddcbed776737b87f3b191);
  all tests run
  [on every commit to the GitHub repo](https://github.com/stellar-registry/cli/actions/workflows/rust.yml)

#### ✅ D3: Flagged Contract Enforcement at Build Time (carried from Q2)

Description from last quarter:

> Extend `import_contract!` / `import_contract_client!` to fail compilation when the referenced Wasm
> or Contract is flagged in the Registry, building on the on-chain flagging that shipped in April.
>
> Proof: a test demonstrating a flagged contract causes a build failure, and documented behavior.

**✅ Complete:**

- `import_contract!` introductory PR added flagged-contract handling (see
  [in PR's `crates/stellar-registry-macro/src/contract.rs#157`](https://github.com/stellar-registry/cli/pull/17/changes#diff-c9fd228d9177e15a059824ea2767bae20b7a7a80a87ddcbed776737b87f3b191R157-R161)
  or
  [on `main`](https://github.com/stellar-registry/cli/blob/a492843105391d401b5bab351a591dea2c6ca2d3/crates/stellar-registry-macro/src/contract.rs#L157-L161))
- Integration test demonstrating/proving this behavior added in follow-up stellar-registry/cli#60
  (Note that this test enforces `stellar registry fetch-contract-id` to fail-by-default for flagged
  contracts. Since `import_contract!` relies on `fetch-contract-id`, it also satisfies the
  requirement to prove the behavior for the macro.)

#### ✅ D4: Finish Search, Pagination & Sorting on rgstry.xyz (carried from Q2)

Description from last quarter:

> Extend server-side search to contracts (stellar-registry/indexer#24), fix search-result updating
> (stellar-registry/ui#22), and ship pagination and sorting so the explorer handles 1,000+ entries
> without degraded load time.
>
> Proof: live on rgstry.xyz; search, pagination, and sorting demonstrated against a 1,000+ entry
> dataset.

**✅ Complete:**

- https://github.com/stellar-registry/indexer/pull/24, trigram index and full-text search on the
  contracts table
- https://github.com/stellar-registry/ui/pull/22, fix search results updating as the query changes
- https://github.com/stellar-registry/ui/pull/29, common search component; contracts wired to
  server-side search
- https://github.com/stellar-registry/ui/pull/34, fix stale results leaking into search
- See every mainnet contract matching `kal`: https://stellar.rgstry.xyz/contracts?query=kal

#### ✅ D5: Contract Explorer, Deploy Button & Verified-Build Badges (carried from Q2)

Description from last quarter:

> Ship the remaining explorer features: the embedded Contract Explorer on contract detail pages, a
> "deploy this Wasm" button, the remaining `stellar contract info meta` fields surfaced on detail
> pages, and verified-build status from Stellar Expert on contract detail pages.
>
> Proof: all features live on production rgstry.xyz, manually verified against at least one mainnet
> contract.

**✅ Complete:**

- https://github.com/stellar-registry/ui/pull/23, Deploy from Wasm
  - prereq: https://github.com/stellar-registry/indexer/pull/32, Extract Wasm Details webhook
- https://github.com/stellar-registry/ui/pull/24, Contract Explorer
- https://github.com/stellar-registry/ui/pull/57, Verified Build (SEP-55) badge from Stellar Expert
  data
  - prereq: https://github.com/stellar-registry/indexer/pull/40, Fetch data once-per-registered
    contract on the indexer side

#### ✅ D6: Governance Operations UI

Description from last quarter:

> Ship the governance proposal forms (stellar-registry/ui#51): propose adding a Wasm or contract to
> the root registry, creating a subregistry, or changing owners — executed through the
> Tansu-DAO-gated registry manager contract that merged in Q2.
>
> Proof: a governance proposal created from rgstry.xyz, voted on in Tansu, and executed on-chain via
> `trigger`, with the transaction linked.

**✅ Complete:**

Tracking issue: https://github.com/stellar-registry/ui/issues/51 (context; closed October 7 once
every sub-issue was complete; the delivery is the merged PRs below). A new Governance section on
rgstry.xyz hosts one form per operation. On testnet, a form builds the on-chain outcome transaction,
pins `proposal.md` to IPFS, and creates a Tansu proposal signed with the user's wallet. On mainnet,
the form opens a prefilled issue in https://github.com/stellar-registry/gov.

- https://github.com/stellar-registry/ui/pull/67, add contract to root registry
  (https://github.com/stellar-registry/ui/issues/53)
- https://github.com/stellar-registry/ui/pull/68, same-origin IPFS pinning route for governance
  proposals
- https://github.com/stellar-registry/ui/pull/71, add Wasm to root registry
  (https://github.com/stellar-registry/ui/issues/52); mainnet issue template
  https://github.com/stellar-registry/gov/pull/2
- https://github.com/stellar-registry/ui/pull/81, create a new subregistry
  (https://github.com/stellar-registry/ui/issues/54); mainnet issue template
  https://github.com/stellar-registry/gov/pull/3
- "Change wasm owner" / "change contract owner" forms dropped
  (https://github.com/stellar-registry/ui/issues/55,
  https://github.com/stellar-registry/ui/issues/56): Wasm authorship transfer is now handled via
  `preauthorize_author_transfer` (https://github.com/stellar-registry/contracts/pull/34), but
  long-term need for this as a governance form has been judged dubious upon further review. (In the
  short-term, Wasms & Contracts seeded as part of initial Registry rollout need to be transferred to
  their appropriate teams. Beyond this one-time mass authorship reassignment, there will be no
  steady-state demand for this governance operation.)
- Tested end-to-end:
  - Governance form (https://testnet.rgstry.xyz/governance/add-wasm) used to request a Wasm be added
    to root registry
  - Created Tansu proposal https://testnet.tansu.dev/proposal/?id=11&name=stellarregistry
  - Security council approved, vote closed, out-of-band anyone-can-fire run of

    ```bash
    stellar contract invoke --id registry-tansu-manager -- trigger --proposal_id 11
    ```

  - Requested Wasm `verified-build-demo` now in Root Registry!
    https://testnet.rgstry.xyz/wasms/verified-build-demo

#### 🟩 D7: Registry Documentation & Education (carried from Q2)

Description from last quarter:

> Publish the Registry docs site and video series covering publishing a Wasm, deploying named and
> unnamed contracts, using `import_contract!`, and publishing/releasing via the verified-build CI
> workflow.
>
> Proof: documentation live on the Registry docs site and videos on The Aha Company's YouTube
> channel.

**✅ Complete:**

- Stellar Registry Full Walk-Through published to The Aha Company YouTube,
  https://www.youtube.com/watch?v=xAlWmJOdMSQ, takes the place of originally-planned many-video
  approach (https://github.com/stellar-registry/cli/issues/46,
  https://github.com/stellar-registry/cli/issues/47,
  https://github.com/stellar-registry/cli/issues/48)
- https://github.com/stellar-scaffold/cli/issues/437, Scaffold Tutorial's Registry docs updated

**⚠️ Pending:**

- https://github.com/stellar-registry/cli/issues/34, Present at Stellar Community Call: Kaan aware of
  intent to present; waiting to be scheduled

#### ✅ D8: Support named G-addresses

Description from last quarter:

> Just as Registry today allows giving names to Wasms and Contracts, expand it to also allow giving
> names to G-addresses. These will be displayed in the rgstry.xyz UI, so that the "Deployer" and
> "Admin" fields become human-friendly names.
>
> Value to ecosystem: a central, open, and collaborative system to add human-friendly names to
> G-addresses will allow other Stellar tools such as Stellar.Expert to also show friendly names,
> making the entire ecosystem more usable by existing participants and more welcoming to newcomers.
>
> Proof: code shipped; address system available, documented, and advertised to the community; more
> than just Aha addresses added and available.

**✅ Complete:**

Scope was narrowed during Q3 to foundational contract-level support; see tracking issue
https://github.com/stellar-registry/cli/issues/51 (context; closed after the quarter, with remaining
G-address work moving to new Q4 issues; the delivery is the merged PRs below).

- https://github.com/stellar-registry/contracts/pull/37, register named G-addresses: new `account`
  namespace in the registry contract with `register_account` and
  `fetch_account_id`/`fetch_account_owner`, using the same auth style as `register_contract`
- https://github.com/stellar-registry/contracts/pull/38, account lifecycle management for named
  G-address entries
- M-addresses are out of scope: Soroban's `Address` has no muxed variant, so muxed IDs can't be
  represented on-chain

Displaying names in the rgstry.xyz UI (e.g. "Deployer" and "Admin" fields), CLI support,
documentation and community outreach, and onboarding non-Aha addresses will be proposed as Q4 work.

#### ✅ D9: Surface emerging Source Verification information

Description from last quarter:

> The Registry team submitted a
> [proposal for the Source Verification system RFP](https://communityfund.stellar.org/dashboard/submissions/receWOpMjj7FxAydj).
> Whether or not our team is awarded this contract, Q3 will see the finalization of underlying SEP-58
> and the launch of independent Source Verification services. Registry is a natural place to surface
> and organize this information and make it useful to the ecosystem.
>
> Value to ecosystem: As the hub that makes Wasms on Stellar discoverable and reusable, Registry is a
> natural place to surface the Wasm metadata added by SEP-58. Registry is also not _a source
> verification service_, but a neutral third party that hosts the information provided by many source
> verification services. A lot of information is being added to the blockchain by this new standard,
> and Registry gives everyone a way to view and make sense of this information.
>
> Proof: all SEP-58 fields viewable on rgstry.xyz; verification status of those fields by independent
> Source Verification services also shown in a way that exposes, rather than flattens, disagreement.

**✅ Complete:**

- https://github.com/stellar-registry/indexer/pull/49, SEP-58 build fields exposed in the indexer's
  Wasm meta
- https://github.com/stellar-registry/ui/pull/82, SEP-58 Source Verification section on Wasm detail
  pages
- https://github.com/stellar-registry/ui/pull/83, same Source Verification section on contract detail
  pages

**⚠️ Pending:**

- Registry could do more! New 3rd-party, off-chain Build Verification Services never got in touch to
  update Registry with their build-verification information.

#### ✅ D10: guide Tansu evolution to support Registry needs

Description from last quarter:

> Harnessing Tansu for Registry's governance required significant effort and an unsatisfying
> technical workaround (see above discussion of Tansu-DAO-gated registry manager). We will
> collaborate with the Tansu team to guide Tansu's evolution, either obsolescing this workaround or
> sculpting it into a more general and generally-usable shape.
>
> Value to ecosystem: whether for security guarantees as in the case of Registry, or just for open &
> participatory governance of open-source projects, on-chain governance provides a crucial role to
> any blockchain ecosystem. Registry's partnership with Tansu ensures the maturity of this solution
> for all community projects.
>
> Proof:
> [Registry Tansu Manager contract](https://github.com/stellar-registry/contracts/tree/41013ac87f35ce025879b598e199cf5f477dc5c7/contracts/registry-tansu-manager)
> either migrates out of the stellar-registry repository to Tansu, becoming easier to use for all
> ecosystem projects, or becomes altogether unnecessary.

**✅ Complete:**

- The delivery: Tansu merged the manager into its own repo:
  [`841dd84`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/841dd84790f3b8f2c8ae4fbf65ca10d5a9adab69),
  "Add the registry manager to tansu itself", merged to Tansu `main` on 2026-09-02 (Radicle tracking
  issue
  https://radicle.network/nodes/radicle.consulting-manao.com/rad%3AzssaAF91kxuquZmZCV2SiK2FNX6s/issues/3111b944792c0b5da9f6c8f88e52cdeebd1a3d82)
- Tansu's copy builds against the real Tansu contract rather than our `tansu-stub`
- Documented in Tansu's governance docs:
  https://github.com/Consulting-Manao/tansu/blob/main/website/docs/developers/governance.mdx#acting-on-other-contracts
- Follow-up cleanup (context; merged October 1, just after the quarter closed): remove the
  now-duplicate `registry-tansu-manager` and `tansu-stub` from stellar-registry/contracts,
  https://github.com/stellar-registry/contracts/pull/55

#### ✅ D11: Registry GH Workflow to publish Wasms and upgrade contracts

Description from last quarter:

> Wrap the
> [stellar-expert/soroban-build-workflow](https://github.com/stellar-expert/soroban-build-workflow)
> and add Registry-specific things:
>
> - build with `stellar scaffold build` instead of `stellar contract build` to ensure inter-contract
>   dependency build order correctness
> - when already-published Wasms are updated with new versions, publish these new versions to
>   Registry
>
> We are intentionally leaving contract upgrades as future work, as this gets into the thorny issue
> of migrations. It is best to leave contract upgrades as a manual task until tooling around
> migrations has matured.
>
> This task requires research into how to securely provision keys which only have permission to
> invoke `publish` on the registry and can be stored in a GitHub workflow and which do not have risky
> privilege levels.
>
> Proof: new repository available at, say, `stellar-registry/gh-build-workflow`. Documented and
> tested in production with the Registry wasm itself.

**✅ Complete:**

- New [stellar-registry/actions](https://github.com/stellar-registry/actions) repo shipped along with
  [stellar-registry/actions-demo](https://github.com/stellar-registry/actions-demo) showing how to
  use it. These two repos are the in-quarter delivery.
- https://github.com/stellar-registry/contracts/pull/53 updates Registry's own contract to
  auto-publish Wasm on commits to `main`,
  https://stellar.expert/explorer/testnet/tx/5793597e4fce5cc536d22263d57bd583d06da2d8e4a648e3b268bc29c0a52cbc
  demonstrates that it works. (Opened September 30; merged, with its first publish, on October 1,
  just after the quarter closed.)
- **Secure on-GitHub keys**: accomplished via new product,
  [Perch](https://github.com/stellar-registry/perch), a "composable policy layer for Soroban smart
  accounts", which we designed and shipped this quarter.

#### ✅ D12: UI: Expose full contract version history

Description from last quarter:

> The Registry API
> [now exposes full version history](https://stellar-registry-testnet.fly.dev/v1/contracts/registry),
> which notably extends into the full history of the blockchain, beyond the launch of the Registry
> contract itself. This information is not yet exposed
> [in the rgstry.xyz UI](https://testnet.rgstry.xyz/contracts/registry). This deliverable addresses
> that mismatch.
>
> Value to ecosystem: making contract upgrades easy to find and analyze aids in troubleshooting and
> full-blockchain comprehensibility.
>
> Proof: Contract detail pages on [rgstry.xyz/contracts](https://testnet.rgstry.xyz/contracts)
> display information about full contract history.

**✅ Complete:**

- Work completed in PR: https://github.com/stellar-registry/ui/pull/40
  - Some fixes: https://github.com/stellar-registry/ui/pull/62
- Contract detail pages display contract history; example:
  https://stellar.rgstry.xyz/contracts/kale/kale

#### 🟩 D13: Documentation consolidation & redesign; potential migration of rgstry.xyz

Description from last quarter:

> Implement new logo and design elements, secured in Q2, across rgstry.xyz site and other Registry
> properties such as GitHub. Organize videos created as part of D7 into landing page and other
> relevant locations throughout rgstry.xyz.
>
> Discuss with ecosystem partners and SDF potential for a new domain for Registry: rgstry.xyz was
> never intended to be permanent. Registry could live under an SDF-owned domain, such as
> registry.stellar.org. This, in turn, may require frontend redesign, swapping current
> subdomain-based network specification (`testnet.rgstry.xyz` / `stellar.rgstry.xyz`) for URL-based
> specification. Depending on scope, the actual implementation of any such plan may be a Q4 concern.
>
> Value to ecosystem: consolidates Registry documentation to a single, searchable place, making it
> simple to onboard and make the most of Registry.
>
> Proof: redesigned site live, videos highlighted throughout, and question of domain's permanent home
> settled with decision documented and justified.

**✅ Complete:**

- logo & icons: https://github.com/stellar-registry/ui/issues/41
- docs consolidation: https://github.com/stellar-registry/ui/issues/42

**⚠️ Pending:**

- domain move discussion: no public link. History of discussion:

  - @chadoh raised the issue in a thread within
    [SDF Slack](https://theahaco.slack.com/archives/C04B02ABF37/p1783975268185649?thread_ts=1783975086.044619&cid=C04B02ABF37);
    no one responded
  - @chadoh to raise again in Stellar Community Call when presenting Registry (see
    [D7](#d7-registry-documentation--education-carried-from-q2))

#### ✅ D14: Extend `import_contract!` macro to support SAC and XLM

Description from last quarter:

> Currently it is difficult to work with Stellar Asset Contracts, you need to know the asset encoding
> or provide the contract Id. Furthermore, writing unit tests which use SACs, particularly the native
> `xlm` asset, are difficult. We have previous work which helped this and is our
> [guess the number contract](https://github.com/stellar-scaffold/ui/blob/main/contracts/guess-the-number/src/xlm.rs).
> The other big improvement is for testing on a standalone network. Currently the xlm SAC isn't
> deployed by default on standalone quickstart image, this work would make this happen lazily on a
> contract's deployment.
>
> Value to ecosystem: make it fun and easy for new developers to use and test SAC assets, especially
> the native.
>
> Proof: published macro which can detect if a contract is a stellar asset contract and generate the
> required code to make using and testing the asset easy.

Note that `import_asset!` was already available and reasonable as an alternative at the end of Q2.
The goal here is to ensure that `import_contract!(xlm)` and similar (such as
`import_contract!("circle/usdc")`) work as-expected, so that users have a choice between
`import_asset!` and `import_contract!`, where `import_contract!` alternative works for any SAC
registered in [stellar.rgstry.xyz](https://rgstry.xyz).

**✅ Complete:**

- https://github.com/stellar-registry/cli/pull/64

#### ✅ D15: Verified Build Integration with Stellar Expert

This is copied from D6 in Q2, as outlined in the
[Q3 Proposal discussion](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/pull/117#issuecomment-5125268576).
It was not hard-committed in the Tansu vote, but was soft-committed in the linked discussion.

Description from Q2:

> Display verified build status from Stellar Expert's API on Registry Wasm and Contract detail pages.
>
> Measure: the verified build badge or indicator is visible on at least one Wasm detail page with a
> known verified contract, and the integration is live in production on `rgstry.xyz`.

Extra details from
[Q3 Proposal discussion](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/pull/117#issuecomment-5125268576):

> There was some real confusion amongst our team about the goal here. The initial Q2 D6 milestone was
> about helping our users implement the Verified Build workflow from Stellar Expert. In our write-up
> of what we did in the quarter, we instead referenced our own use of the Stellar Expert verified
> build workflow.
>
> While this served as useful research for how to help our users, it did not satisfy the original
> task. D6 should have also been marked as a carry-over for Q3.
>
> In addition, in our "completion notes" for D6, we stated that we were targeting contract pages,
> "since we established Stellar Expert has no Wasm-level pages." We've changed our thinking on this,
> as documented in a new issue, stellar-registry/ui#38. This is a sub-issue of our original tracking
> issue stellar-registry/cli#35, which we will continue to use as our tracking issue for Q3.

**✅ Complete:**

- https://github.com/stellar-registry/ui/pull/57, Verified Build (SEP-55) badge from Stellar Expert
  data for _Contracts_ (done to satisfy
  [D5](#d5-contract-explorer-deploy-button--verified-build-badges-carried-from-q2))
  - prereq: https://github.com/stellar-registry/indexer/pull/40, Fetch data once-per-registered
    contract on the indexer side
- stellar-registry/ui#38
  - stellar-registry/ui#57
  - stellar-registry/ui#64
  - stellar-registry/indexer#48
  - stellar-registry/indexer#40
- stellar-registry/cli#35

<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

Overarching Q4 story: Registry is ready, now drive adoption.

Q3 saw Registry become a sophisticated product offering huge productivity gains to any team that
adopts it. And: the more everyone adopts it, the more everyone benefits. In Q4 we accelerate those
gains.

We'll also ship the stuff early adopters have already asked for.
<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

### D1: Help Community Projects Use Registry Internally

Work intensively with at least two key partners to onboard their projects to Registry, specifically
focusing on improvements to their toolchains and processes. This deliverable is about getting
partners to use Registry in their own workflows. Along the way, we will discover Registry gotchas,
improving the product to accelerate further rollout.

Possible partners & projects: XOXNO, Reflector (Orbitlens), Stellar Broker (Orbitlens), Crossmint
(Overcat), Rozo (Shawn), LiFi, Soroswap (Palta Labs / Esteblock).

Value to ecosystem: more teams are saving time by using Registry and their contracts and Wasms are
easier to find & use for the rest of the ecosystem.

Issue: https://github.com/stellar-registry/ui/issues/102

Proof:

- Merged PRs to integrate Registry into their codebases/workflows
- Partner teams' contracts & Wasms exist on Registry and are owned by their teams' accounts

### D2: Help Community Projects Show Registry Info

Starting with Stellar.Expert, we'll help community partners display Registry info, turning opaque
hashes and IDs into human-friendly names.

Value to ecosystem: in the systems that people are already relying on, contracts and Wasms are
identified by human-friendly names and versions, rather than opaque hashes and IDs.

Issues:

- stellar-registry/indexer#TODO: Update Stellar.Expert to show Registry names/versions in place of
  Wasm hashes and contract IDs, when available

Proof:

- Linked issue closed with implementing PR
- Registry info displays on Stellar.Expert when available

### D3: Developer outreach & education

We will continue to present and teach about Registry at Stellar community events and support other
teams who do the same.

Value to ecosystem: help people learn about and onboard to Registry.

Issues:

- https://github.com/stellar-registry/cli/issues/34, Stellar Community Call
- https://github.com/stellar-registry/ui#TODO: Present Registry at HackMeridian
- https://github.com/stellar-registry/ui#TODO: Host monthly Office Hours to teach people about
  Registry or answer their questions

Proof: links to recorded videos or event links

### D4: Smart account support in the `account` namespace

The `account` namespace shipped in Q3 only accepts classic G-addresses: `register_account` rejects
contract addresses with `NotAccountAddress`. Smart wallets such as [Nido](https://github.com/nidohq)
(passkey-based) are contract accounts (C-addresses), so their users can't get a name today.

Issues:

- stellar-registry/contracts#TODO: Accept smart-account contract addresses in `register_account` and
  the account lifecycle functions, while keeping them distinct from entries in the `contract`
  namespace
- nidohq/nido#TODO: Add wallet names to Stellar Registry

Value to ecosystem: one naming system for every kind of Stellar account, so passkey and other
smart-wallet users get the same human-readable names as classic accounts.

Proof: registry contract released with smart-account support; at least one Nido wallet registered
under a name and resolvable on rgstry.xyz and from the CLI.

### D5: Named G-addresses, from contract to ecosystem (follow-on from Q3 D8)

Q3 shipped named G-address support in the registry contract (stellar-registry/contracts#37,
stellar-registry/contracts#38). Make it usable and adopted.

This follows D4 intentionally: either style of named account (whether backed by a G-address or a
smart account C-address) must be supported in all situations.

Issues:

- stellar-registry/ui#TODO: Display account names anywhere accounts appear (e.g. "Deployer" and
  "Admin" fields)
- stellar-registry/ui#TODO: Governance form to request named account in root Registry
- stellar-registry/cli#TODO: register, resolve, and manage named (G- or C-) accounts
- stellar-scaffold/cli#TODO: Document Registry's named (G- and C-) account support
- stellar-registry/ui#TODO: Work with partner network to register names for the (G- and C-) accounts
  listed in their Wasms & contracts
- stellar-registry/indexer#TODO: Show Registry's (G- & C-) account names in Stellar.Expert
- stellar-registry/contracts#TODO: Create a SEP for resolving named G-addresses, so wallets and other
  tools can adopt the same names

Value to ecosystem: human-readable names for accounts, not only contracts & Wasms; reduce copy-paste
mistakes and make on-chain activity legible.

Proof: names shown on rgstry.xyz and resolvable from the CLI; docs published and announced; named
addresses registered by at least one team other than Aha; SEP draft or discussion linked.

### D6: Simplify `import_contract!` testing

`import_contract!` works well on testnet and mainnet, but local development and unit tests need a
registry with the depended-on contracts already registered, which each team has to set up themselves.
Build the workaround from stellar-registry/cli#64 into the library

Issue: stellar-registry/cli#65

Value to ecosystem: teams adopting `import_contract!` get a working dev and test setup without
retracing our steps.

Proof: linked issue address with a PR using a newly-cut release of `stellar-registry` crate

### D7: Contract Details UI Revamp

The amount of information shown on Contract Details pages has grown, and it's starting to feel
cluttered. Let's clean it up and prioritize what's important.

- Issue: stellar-registry/ui#94

### D8: Fix core `deploy` workflow when using Secure Store

When following security best practices, keeping secret keys and seed phrases off the file system and
instead using macOS Secure Store or a hardware wallet like Ledger, the Registry CLI falls victim to
an upstream Stellar CLI bug.

Issue: stellar-registry/cli#14

Value to ecosystem: No longer force users into clumsy and potentially insecure workarounds for core
Registry CLI workflows.

Proof: Issues and PRs _created_ in https://github.com/stellar/stellar-cli, and communications sent to
Stellar CLI via our shared Slack channel to attempt to secure a review of these issues & PRs.

### D9: `stellar-registry/actions` maturation & adoption

Q3's D11 saw us add automatic Wasm publishing to Registry via GitHub Workflow, added to Registry's
own Wasm in stellar-registry/contracts#53. In Q4 we add contract upgrades to the core actions
workflow, add more discerning Mainnet publish pathway, and adopt these workflows in all
Aha-maintained projects. Along the way, we turn any rough edges or tooling/documentation gaps into
new issues or PRs.

Issues:

- stellar-registry/actions#TODO: add "Contract `upgrade`" workflow step
- stellar-registry/actions#TODO: add human-initiated "Mainnet publish/deploy" workflow step
- stellar-scaffold/ui#TODO: adopt stellar-registry/actions for Wasm publish & contract upgrade
- stellar-registry/oz-combined-wasms#TODO: adopt stellar-registry/actions for Wasm publish & contract
  upgrade
- Consulting-Manao/tansu#TODO: adopt stellar-registry/actions for Wasm publish & contract upgrade
- nidohq/nido#TODO: adopt stellar-registry/actions for Wasm publish & contract upgrade
- stellar-registry/perch#TODO: adopt stellar-registry/actions for Wasm publish & contract upgrade
- Moonlight-Protocol/soroban-core#TODO: adopt stellar-registry/actions for Wasm publish & contract
  upgrade

Value to ecosystem: maturation of `stellar-registry/actions` ahead of Q1 rollout to partner teams and
broader ecosystem; simplified & automatic best-practices publishing of Wasms with associated contract
upgrades for all projects that adopt the workflow.

Proof:

- Issues closed with implementing PRs
- Successful workflow runs on linked Aha repos

<!-- markdownlint-enable MD034 -->

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_registry&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_registry)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_registry&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_registry)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_registry&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_registry)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_registry&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_registry)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
