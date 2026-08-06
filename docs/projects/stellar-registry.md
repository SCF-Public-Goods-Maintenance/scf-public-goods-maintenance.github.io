---
title: "Stellar Registry"
parent: Public Good Projects
proposal_issue: 64
proposer: chadoh
category: "Developer Experience"
budget: "50000"
---

# Stellar Registry

_Stellar Registry is an on-chain smart contract registry for Soroban that lets developers publish,
version, discover, and deploy Wasm binaries and contract instances, making contracts reusable across
the ecosystem like packages._

|                      |                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| **Category**         | Developer Experience                                                                               |
| **Website**          | <https://rgstry.xyz>                                                                               |
| **Repository**       | <https://github.com/stellar-registry>                                                              |
| **First Released**   | March 2026                                                                                         |
| **Intake**           | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/23> |
| **Budget Requested** | 50000                                                                                              |

## Project Description

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

## Team & Experience

Scaffold Stellar is built and maintained by **The Aha Company**, a team of 13+
senior engineers deeply embedded in the Stellar ecosystem.

_Copy/update rest of bio from [Q3 proposal](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/pull/117)_

## Retroactive Impact

In Q3 2026...

## Q3 Deliverables

### D1: Complete the Mainnet Launch (carried from Q2)

Description from last quarter:

> With the registry contract live on mainnet, finish the public rollout: run the mainnet indexer
pipeline, point rgstry.xyz at the mainnet API and remove the "Coming Soon" banner, and land
secure-store/Ledger signing in the CLI (stellar-registry/cli#14) so admin operations never expose a
raw secret key.
>
> Proof: mainnet data live and browsable at rgstry.xyz, the contract visible on Stellar Expert, and
named contracts resolvable via `stellar registry` CLI.

#### ✅ Complete

- Mainnet data is now fully indexed in Goldsky (https://github.com/stellar-registry/indexer/pull/25) and queryable via API calls at https://stellar-registry-mainnet.fly.dev/
- [stellar.rgstry.xyz](https://stellar.rgstry.xyz) now live as the "primary" subdomain (with [rgstry.xyz](https://rgstry.xyz) redirecting to it)
- [Registry contract](https://stellar.rgstry.xyz/contracts/registry) visible [on Stellar Expert](https://stellar.expert/explorer/public/contract/CDU4M3LDIOUJJ5F3YXKJ4EJEP5VPRPG6N2LJ5HOQIMN7MNGL3NS3EGUY)
- All `stellar registry` commands working across both testnet and mainnet (see @kalepail's request at stellar-registry/gov#1 as proof)

#### ⚠️ Pending

Q3 stretch goal (not hard-committed in Q3 deliverables; nice-to-have):

- stellar-registry/cli#14

### D2: Release `import_contract!` (carried from Q2)

Description from last quarter:

> Merge stellar-registry/cli#17 and publish the macro in released crates, documented with at least one working example and covered by integration tests.
>
> Proof: a crates.io release containing `import_contract!`, linked docs and example, CI running the integration tests.

#### ✅ Complete

The macro has landed! This was a hefty engineering task that entailed two large-scale re-architectures, code consolidation from other repositories (`stellar-scaffold/cli` repo is no longer the home of related macros `import_contract_client!` and `import_asset!`), and the creation of a new [`stellar-registry-name` crate](https://crates.io/crates/stellar-registry-name). With this release, we declared all Stellar Registry crates to have reached official beta, marking them all as [version 0.1.0](https://github.com/stellar-registry/cli/releases).

- See `import_contract!` documentation and examples at both [crates.io](https://crates.io/crates/stellar-registry) and [docs.rs](https://docs.rs/stellar-registry)
- Comprehensive unit tests for `import_contract!` added in macro's [introductory PR at `crates/stellar-registry-macro/src/contract.rs`](https://github.com/stellar-registry/cli/pull/17/changes#diff-c9fd228d9177e15a059824ea2767bae20b7a7a80a87ddcbed776737b87f3b191); all tests run [on every commit to the GitHub repo](https://github.com/stellar-registry/cli/actions/workflows/rust.yml)

#### ⚠️ Pending

Q3 stretch goal (not hard-committed in Q3 deliverables; nice-to-have):

- stellar-registry/contracts#24

Once this is done, people will have not just the documentation examples from crates.io and docs.rs, but a cookbook-style example using real working code.

### D3: Flagged Contract Enforcement at Build Time (carried from Q2)

Description from last quarter:

> Extend `import_contract!` / `import_contract_client!` to fail compilation when the referenced Wasm or Contract is flagged in the Registry, building on the on-chain flagging that shipped in April.
>
> Proof: a test demonstrating a flagged contract causes a build failure, and documented behavior.

#### ✅ Complete

- `import_contract!` introductory PR added flagged-contract handling (see [in PR's `crates/stellar-registry-macro/src/contract.rs#157`](https://github.com/stellar-registry/cli/pull/17/changes#diff-c9fd228d9177e15a059824ea2767bae20b7a7a80a87ddcbed776737b87f3b191R157-R161) or [on `main`](https://github.com/stellar-registry/cli/blob/a492843105391d401b5bab351a591dea2c6ca2d3/crates/stellar-registry-macro/src/contract.rs#L157-L161))
- Integration test demonstrating/proving this behavior added in follow-up stellar-registry/cli#60 (Note that this test enforces `stellar registry fetch-contract-id` to fail-by-default for flagged contracts. Since `import_contract!` relies on `fetch-contract-id`, it also satisfies the requirement to prove the behavior for the macro.)

### D4: Finish Search, Pagination & Sorting on rgstry.xyz (carried from Q2)

Description from last quarter:

> Extend server-side search to contracts (stellar-registry/indexer#24), fix search-result updating (stellar-registry/ui#22), and ship pagination and sorting so the explorer handles 1,000+ entries without degraded load time.
>
> Proof: live on rgstry.xyz; search, pagination, and sorting demonstrated against a 1,000+ entry dataset.

#### ✅ Complete

- stellar-registry/indexer#24

### D5: Contract Explorer, Deploy Button & Verified-Build Badges (carried from Q2)

Description from last quarter:

> Ship the remaining explorer features: the embedded Contract Explorer on contract detail pages, a "deploy this Wasm" button, the remaining `stellar contract info meta` fields surfaced on detail pages, and verified-build status from Stellar Expert on contract detail pages.
>
> Proof: all features live on production rgstry.xyz, manually verified against at least one mainnet contract.

#### ⚠️ Pending

- https://github.com/stellar-registry/ui/pull/23
  - prereqs completed by @b4sen
    - https://github.com/stellar-registry/indexer/pull/32
    - https://github.com/stellar-registry/indexer/pull/35
    - https://github.com/stellar-registry/indexer/pull/36
  - no one currently leading ui effort
- https://github.com/stellar-registry/ui/pull/24 (@zachfedor to complete)

### D6: Governance Operations UI

Description from last quarter:

> Ship the governance proposal forms (stellar-registry/ui#16): propose adding a Wasm or contract to the root registry, creating a subregistry, or changing owners — executed through the Tansu-DAO-gated registry manager contract that merged in Q2.
>
> Proof: a governance proposal created from rgstry.xyz, voted on in Tansu, and executed on-chain via `trigger`, with the transaction linked.

#### ⚠️ Pending

No current associated issues/PRs. No one assigned.

### D7: Registry Documentation & Education (carried from Q2)

Description from last quarter:

> Publish the Registry docs site and video series covering publishing a Wasm, deploying named and unnamed contracts, using `import_contract!`, and publishing/releasing via the verified-build CI workflow.
>
> Proof: documentation live on the Registry docs site and videos on The Aha Company's YouTube channel.

#### ⚠️ Pending

- https://github.com/stellar-registry/cli/issues/50 (assigned to @chadoh, who would indeed like to work on this after D5 is complete, but is willing to let someone else take the lead if they really wanna)

### D8: Support named G-addresses

Description from last quarter:

> Just as Registry today allows giving names to Wasms and Contracts, expand it to also allow giving names to G-addresses. These will be displayed in the rgstry.xyz UI, so that the "Deployer" and "Admin" fields become human-friendly names.
>
> Value to ecosystem: a central, open, and collaborative system to add human-friendly names to G-addresses will allow other Stellar tools such as Stellar.Expert to also show friendly names, making the entire ecosystem more usable by existing participants and more welcoming to newcomers.
>
> Proof: code shipped; address system available, documented, and advertised to the community; more than just Aha addresses added and available.

#### ⚠️ Pending

Currently under discussion in internal `#stellar-registry` channel. Tracking issue unassigned:

- https://github.com/stellar-registry/cli/issues/51

### D9: Surface emerging Source Verification information

Description from last quarter:

> The Registry team submitted a [proposal for the Source Verification system RFP](https://communityfund.stellar.org/dashboard/submissions/receWOpMjj7FxAydj). Whether or not our team is awarded this contract, Q3 will see the finalization of underlying SEP-58 and the launch of independent Source Verification services. Registry is a natural place to surface and organize this information and make it useful to the ecosystem.
>
> Value to ecosystem: As the hub that makes Wasms on Stellar discoverable and reusable, Registry is a natural place to surface the Wasm metadata added by SEP-58. Registry is also not _a source verification service_, but a neutral third party that hosts the information provided by many source verification services. A lot of information is being added to the blockchain by this new standard, and Registry gives everyone a way to view and make sense of this information.
>
> Proof: all SEP-58 fields viewable on rgstry.xyz; verification status of those fields by independent Source Verification services also shown in a way that exposes, rather than flattens, disagreement.

#### ⚠️ Pending

- We did not receive the grant to work on this RFP.
- We continue to participate in [ongoing RFP discussions](https://github.com/orgs/stellar/discussions/1945#discussioncomment-17897997).
- Who won the RFP? Do they want us to do anything?

### D10: guide Tansu evolution to support Registry needs

Description from last quarter:

> Harnessing Tansu for Registry's governance required significant effort and an unsatisfying technical workaround (see above discussion of Tansu-DAO-gated registry manager). We will collaborate with the Tansu team to guide Tansu's evolution, either obsolescing this workaround or sculpting it into a more general and generally-usable shape.
>
> Value to ecosystem: whether for security guarantees as in the case of Registry, or just for open & participatory governance of open-source projects, on-chain governance provides a crucial role to any blockchain ecosystem. Registry's partnership with Tansu ensures the maturity of this solution for all community projects.
>
> Proof: [Registry Tansu Manager contract](https://github.com/stellar-registry/contracts/tree/main/contracts/registry-tansu-manager) either migrates out of the stellar-registry repository to Tansu, becoming easier to use for all ecosystem projects, or becomes altogether unnecessary.

#### ⚠️ Pending

No current tracking issues or PRs. Needs engineering design discussion with Tansu team.

### D11: Registry GH Workflow to publish Wasms and upgrade contracts

Description from last quarter:

> Wrap the [stellar-expert/soroban-build-workflow](https://github.com/stellar-expert/soroban-build-workflow) and add Registry-specific things:
>
> - build with `stellar scaffold build` instead of `stellar contract build` to ensure inter-contract dependency build order correctness
> - when already-published Wasms are updated with new versions, publish these new versions to Registry
>
> We are intentionally leaving contract upgrades as future work, as this gets into the thorny issue of migrations. It is best to leave contract upgrades as a manual task until tooling around migrations has matured.
>
> This task requires research into how to securely provision keys which only have permission to invoke `publish` on the registry and can be stored in a GitHub workflow and which do not have risky privilege levels.
>
> Proof: new repository available at, say, `stellar-registry/gh-build-workflow`. Documented and tested in production with the Registry wasm itself.

#### ⚠️ Pending

- https://github.com/stellar-registry/oz-combined-wasms/issues/1 (@willemneal assigned; work to start Aug 17, ~1w effort???)

### D12: UI: Expose full contract version history

Description from last quarter:

> The Registry API [now exposes full version history](https://stellar-registry-testnet.fly.dev/v1/contracts/registry), which notably extends into the full history of the blockchain, beyond the launch of the Registry contract itself. This information is not yet exposed [in the rgstry.xyz UI](https://testnet.rgstry.xyz/contracts/registry). This deliverable addresses that mismatch.
>
> Value to ecosystem: making contract upgrades easy to find and analyze aids in troubleshooting and full-blockchain comprehensibility.
>
> Proof: Contract detail pages on [rgstry.xyz/contracts](https://testnet.rgstry.xyz/contracts) display information about full contract history.

#### ⚠️ Pending

No current issues/PRs

### D13: Documentation consolidation & redesign; potential migration of rgstry.xyz

Description from last quarter:

> Implement new logo and design elements, secured in Q2, across rgstry.xyz site and other Registry properties such as GitHub. Organize videos created as part of D7 into landing page and other relevant locations throughout rgstry.xyz.
>
> Discuss with ecosystem partners and SDF potential for a new domain for Registry: rgstry.xyz was never intended to be permanent. Registry could live under an SDF-owned domain, such as registry.stellar.org. This, in turn, may require frontend redesign, swapping current subdomain-based network specification (`testnet.rgstry.xyz` / `stellar.rgstry.xyz`) for URL-based specification.  Depending on scope, the actual implementation of any such plan may be a Q4 concern.
>
> Value to ecosystem: consolidates Registry documentation to a single, searchable place, making it simple to onboard and make the most of Registry.
>
> Proof: redesigned site live, videos highlighted throughout, and question of domain's permanent home settled with decision documented and justified.

#### ⚠️ Pending

No current issues/PRs

### D14: Extend `import_contract!` macro to support SAC and XLM

Description from last quarter:

> Currently it is difficult to work with Stellar Asset Contracts, you need to know the asset encoding or provide the contract Id. Furthermore, writing unit tests which use SACs, particularly the native `xlm` asset, are difficult. We have previous work which helped this and is our [guess the number contract](https://github.com/stellar-scaffold/ui/blob/main/contracts/guess-the-number/src/xlm.rs). The other big improvement is for testing on a standalone network. Currently the xlm SAC isn't deployed by default on standalone quickstart image, this work would make this happen lazily on a contract's deployment.
>
> Value to ecosystem: make it fun and easy for new developers to use and test SAC assets, especially the native.
>
> Proof: published macro which can detect if a contract is a stellar asset contract and generate the required code to make using and testing the asset easy.

Note that `import_asset!` was already available and reasonable as an alternative at the end of Q2. The goal here is to ensure that `import_contract!(xlm)` and similar (such as `import_contract!("circle/usdc")`) work as-expected, so that users have a choice between `import_asset!` and `import_contract!`, where `import_contract!` alternative works for any SAC registered in [stellar.rgstry.xyz](https://rgstry.xyz).

#### ⚠️ Pending

No current issues/PRs. @willemneal, in a conversation with @chadoh, committed to working on this after D11. ~2d effort.

### D15: Verified Build Integration with Stellar Expert

This is copied from D6 in Q2, as outlined in the [Q3 Proposal discussion](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/pull/117#issuecomment-5125268576). It was not hard-committed in the Tansu vote, but was soft-committed in the linked discussion.

Description from Q2:

> Display verified build status from Stellar Expert's API on Registry Wasm and Contract detail pages.
>
> Measure: the verified build badge or indicator is visible on at least one Wasm detail page with a
> known verified contract, and the integration is live in production on `rgstry.xyz`.

Extra details from [Q3 Proposal discussion](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/pull/117#issuecomment-5125268576):

> There was some real confusion amongst our team about the goal here. The initial Q2 D6 milestone was about helping our users implement the Verified Build workflow from Stellar Expert. In our write-up of what we did in the quarter, we instead referenced our own use of the Stellar Expert verified build workflow.
>
> While this served as useful research for how to help our users, it did not satisfy the original task. D6 should have also been marked as a carry-over for Q3.
>
> In addition, in our "completion notes" for D6, we stated that we were targeting contract pages, "since we established Stellar Expert has no Wasm-level pages." We've changed our thinking on this, as documented in a new issue, stellar-registry/ui#38. This is a sub-issue of our original tracking issue stellar-registry/cli#35, which we will continue to use as our tracking issue for Q3.

#### ⚠️ Pending

- stellar-registry/ui#38
- stellar-registry/ui#35

## Q3 Stretch Goals

- https://github.com/stellar-registry/contracts/issues/25
- https://github.com/stellar-registry/ui/issues/35
- https://github.com/stellar-registry/ui/issues/36

## Proposed Q4 Impact

...

## Proposed Q4 Deliverables

...

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_registry&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_registry)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_registry&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_registry)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_registry&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_registry)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Astellar_registry&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Astellar_registry)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
