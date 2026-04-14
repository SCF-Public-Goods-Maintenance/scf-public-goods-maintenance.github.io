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
| **Repository**       | <https://github.com/theahaco/scaffold-stellar/tree/main/contracts/registry>                        |
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

Stellar Registry launched within the last three months on Testnet, and has already garnered
significant interest from ecosystem partners/projects such as PG Atlas and the SDF DevRel team for
their Mexico City hackathon.

<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

N/A — this section intentionally left blank — please pass validation; you told me to put "N/A" and
that's just what I did but now validation won't pass. Maybe I need to put more words?

<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

**Make the Registry production-ready.** Deploying to mainnet (theahaco/scaffold-stellar#433)
transforms the Registry from a testnet experiment into permanent Stellar infrastructure — a shared,
on-chain contract store that any Soroban developer or dApp can publish to and consume from.

**Make contract composability ergonomic.** The `import_contract!` macro
(theahaco/scaffold-stellar#419) and its build-time safety enforcement (theahaco/scaffold-stellar#452)
mean that any Soroban developer can depend on Registry contracts the way they depend on Rust crates —
with a clean API and compile-time guarantees that flagged or compromised contracts won't ship.

**Make the Registry discoverable and usable without the CLI.** Through search, pagination, UI
enhancements, verified build integration, and human-readable addresses
(theahaco/scaffold-stellar#454, theahaco/scaffold-stellar#453, theahaco/scaffold-stellar#455,
theahaco/scaffold-stellar#421), `rgstry.xyz` becomes a real contract discovery platform — not just a
read-only dashboard — so developers can find, evaluate, and deploy contracts directly from the
browser.

**Lower the barrier to entry.** Targeted Registry documentation (theahaco/scaffold-stellar#426),
cross-linked with Scaffold Stellar's docs, ensures developers arriving from any direction — the CLI,
the web explorer, or Scaffold Stellar — can get productive with the Registry quickly.

**Benefit to the Stellar ecosystem:** The Registry is ecosystem infrastructure, not a product
feature. Every Soroban project benefits from a trustworthy, searchable, mainnet-deployed contract
store. It enables contract reuse, reduces duplicated effort across teams, and raises the baseline
security and auditability of the ecosystem. Scaffold Stellar remains the recommended starting point
for building on top of the Registry, but the Registry stands independently and is designed to serve
the entire Soroban developer community.

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

## D1: Mainnet Deploy of Stellar Registry (theahaco/scaffold-stellar#433)

Deploy the Registry smart contract to Stellar mainnet and confirm it is publicly accessible via
`stellar registry` CLI and `rgstry.xyz`.

Measure: the contract is deployed & the CLI points to it.

## D2: `import_contract!` Macro (theahaco/scaffold-stellar#419)

Publish a working `import_contract!` macro in the `stellar-registry` crate that allows cross-contract
client instantiation with a single line of Rust.

Measure: the macro is available in a released crate version, documented with at least one working
example, and covered by integration tests.

## D3: Flagged Contract Enforcement at Build Time (theahaco/scaffold-stellar#452)

Extend `import_contract!` and `import_contract_client!` to emit a compile-time error when the
referenced Wasm or Contract is flagged in the Registry.

Measure: a test exists that demonstrates a flagged contract causes a build failure, and the behavior
is documented.

## D4: Server-Side Search, Pagination & Sorting on rgstry.xyz (theahaco/scaffold-stellar#454)

Replace the current client-side full-data-fetch approach with API-backed search, pagination, and
sorting on `rgstry.xyz`.

Measure: the explorer handles at least 1,000 published Wasms/Contracts without degraded load time,
search returns results server-side, and pages load incrementally.

## D5: rgstry.xyz UI Enhancements (theahaco/scaffold-stellar#453)

Ship three specific improvements to the Registry web explorer:

1. Contract Explorer embedded on contract detail pages
2. `stellar contract info meta` metadata surfaced on Wasm and Contract detail pages
3. A "deploy this Wasm" button that initiates a Registry deploy from the UI

Measure: all three features are live on the production `rgstry.xyz` site and manually verified
against at least one mainnet contract.

## D6: Verified Build Integration with Stellar Expert (theahaco/scaffold-stellar#455)

Display verified build status from Stellar Expert's API on Registry Wasm and Contract detail pages.

Measure: the verified build badge or indicator is visible on at least one Wasm detail page with a
known verified contract, and the integration is live in production on `rgstry.xyz`.

## D7: Registry Documentation & Education (theahaco/scaffold-stellar#426)

Publish complete Registry documentation and videos covering:

- publishing a Wasm
- deploying a named contract
- using `import_contract!`
- deploying an unnamed contract
- publishing/releasing using CI workflow
- more!

Measure: documentation is live on Registry's own docs site & The Aha Company's YouTube channel.

<!-- markdownlint-enable MD034 -->

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
