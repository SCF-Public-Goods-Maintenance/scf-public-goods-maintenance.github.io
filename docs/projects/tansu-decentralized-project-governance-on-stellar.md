---
title: "Tansu - Decentralized project governance on Stellar"
parent: Public Good Projects
proposal_issue: 105
proposer: tupui
category: "Governance Tools"
budget: "$50,000 in XLM"
---

# Tansu - Decentralized project governance on Stellar

<!-- markdownlint-disable MD036 -->

_Tansu provides cryptographic proof of code integrity and transparent governance for open-source
projects._
<!-- markdownlint-enable MD036 -->

|                      |                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| **Category**         | Governance Tools                                                                                   |
| **Website**          | <https://tansu.dev>                                                                                |
| **Repository**       | <https://github.com/Consulting-Manao/tansu>                                                        |
| **First Released**   | October 2025                                                                                       |
| **Intake**           | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/88> |
| **Budget Requested** | $50,000 in XLM                                                                                     |

## Project Description

<!-- markdownlint-disable MD034 -->

Tansu is a governance and versioning layer for open source projects, built on the Stellar blockchain.
It brings transparency, security, and decentralized decision-making to software development by
combining on-chain project tracking, a powerful voting platform, and a flexible membership system. It
integrates well with the Neural Quorum Governance score making it a great tool for the Stellar
community. It is the first platform to offer anonymous voting on Stellar.
<!-- markdownlint-enable MD034 -->

## Team & Experience

<!-- markdownlint-disable MD034 -->

It's been mostly me, Pamphile Tupui Roy [LinkedIn](https://www.linkedin.com/in/tupui). I am a Pilot
and delegate. I have contributed to the Stellar developer documentation, helped with hackathons and
participated in multiple Stellar Enhancement Proposals (co-authored SEP-52 and SEP-53). I am also
active in the Python sphere, acting as maintainer of SciPy (2M+ daily downloads) and SALib, and
serving on the Scientific Python Steering Committee. I know what it means to develop open source
solutions, what backward compatibility and maintenance truly mean.

I have been working on Tansu in my free time since around May 2024. I got some help there and there
from friends and hired a few people along the years mostly to do frontend related tasks.

Now, I am a Principal Engineer at [The Aha Co](https://www.theaha.co/)
([GitHub](https://github.com/theahaco) | [LinkedIn](https://www.linkedin.com/company/aha-labs-dev)).
We are advising many projects on Stellar as an official integration partner as well as part of the
architect program. We are more than 15 devs and still growing strong. Depending on the task, I will
leverage 1 to 2 people from the team. Mostly, but not limited:

- Chad Ostrowski ([GitHub](https://github.com/chadoh),
  [LinkedIn](https://www.linkedin.com/in/chadoh), Discord @chadoh) on the architecutre and general
  flow.
- Willem Wyndham ([GitHub](https://github.com/willemneal),
  [LinkedIn](https://www.linkedin.com/in/willem-wyndham), Discord @sirwillem), to review my work on
  smart contracts.
- Hugo Heer ([GitHub](https://github.com/hugo-heer),
  [LinkedIn](https://www.linkedin.com/in/hugo-heer-b29a0419b)), a frontend guru.

<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->

In Q2 2026, Tansu operated the first SCF Public Goods Award round on its dedicated testnet project.
SCF Pilots voted anonymously with NQG-weighted ballots; 17 projects were funded and around $400,000
was disbursed. Write-up: [blog](https://tansu.dev/blog/public-goods-award-q2),
[program docs](https://scf-public-goods-maintenance.github.io).

Running the round drove several governance features: on-chain conflict-of-interest lists (and
management in the dApp), replacement of Soroban Domains with a collateral and unique on-chain names,
anonymous and token-weighted voting, outcome-contract hooks, and a malicious-proposal revoke flow.

While the voting was running, some issues around computational cost required by the anonymous setup
where identified early enough that no-one was impacted. This also highlighted the need to rework the
collateral system during voting.

On the infrastructure side, I had to migrate urgently away from Storacha (IPFS) as they close down
their operations. All was migrated to Filebase (with some optional pinning to Pinata in the code.)

I participated in all Drips Waves and a lot of work went into stabilizing features and adding new
exciting things: a concept of evidence for SBOM/CVE/attestation CIDs; support for any forge including
Radicle; and a linking of Git identity with a G-address. Tansu is now seeing a few contributors
coming back and helping out which is a way to increase the pony factor. On that front, the team at
Aha is fully onboarded as maintainers.
<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

**P1: Q2 Public Goods Award on Tansu testnet**

Proof of completion:

- Round completed on `stellarpg` (on the sub-project `stellarpga`) on testnet:
  [testnet.tansu.dev](https://testnet.tansu.dev)
- [Q2 round blog post](https://tansu.dev/blog/public-goods-award-q2)
- [Program repository](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io)

First PG Award round with anonymous NQG-weighted pilot voting on testnet; 17 projects funded, more
than $400,000 disbursed. The work was done as part of a
[SCF Build Award](https://communityfund.stellar.org/project/pg-atlas-dse).

**P2: Governance stack**

Proof of completion:

- Conflict of interest: [#94](https://github.com/Consulting-Manao/tansu/pull/94),
  [#151](https://github.com/Consulting-Manao/tansu/pull/151)
- Soroban Domains removed and collateral system:
  [#157](https://github.com/Consulting-Manao/tansu/pull/157),
  [blog](https://tansu.dev/blog/docs-update-collateral-forges-weights)
- Anonymous voting, token-weighted ballots, outcome contracts, malicious-proposal flow:
  [governance docs](https://tansu.dev/docs/developers/governance)

**P3: NQG + `scf-membership`**

Proof of completion:

- `NqgProjectKey` and `contracts/scf-membership/`:
  [#50](https://github.com/Consulting-Manao/tansu/pull/50)
- Viewer: https://scf.pgatlas.xyz https://github.com/Consulting-Manao/scf-member-explorer

**P4: Supply chain and evidence**

Proof of completion:

- Unified `set_evidence` API: [#186](https://github.com/Consulting-Manao/tansu/pull/186),
  `tools/evidence/publish.sh`
- SBOM CI and on-chain recording: [#145](https://github.com/Consulting-Manao/tansu/pull/145),
  .github/workflows/sbom.yml`
- Workflows improvements: `.github/workflows`

**P5: Maintainance**

Proof of completion:

- Storacha to Filebase IPFS: [#56](https://github.com/Consulting-Manao/tansu/pull/56),
  [#139](https://github.com/Consulting-Manao/tansu/pull/139),
  [#141](https://github.com/Consulting-Manao/tansu/pull/141)
- See the improved
  [CONTRIBUTING.md](https://github.com/Consulting-Manao/tansu/blob/main/CONTRIBUTING.md).
- Migrating to
  [radicle.consulting-manao.com](https://radicle.network/nodes/radicle.consulting-manao.com)

<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

1. **PG Award Q3 on Tansu:** same testnet stack as Q2; definition of a program-specific NQG score
   with the SDF engineering and SCF teams; `scf-membership` and NQG on mainnet; mid-grant reviews
   process figured out with possibly some actions on Tansu; collateral system refactoring and other
   Q2 voting fixes ([#112](https://github.com/Consulting-Manao/tansu/issues/112)).

2. **Stellar Registry:** `registry-tansu-manager` factory, proposal/outcome templates, registry name
   resolution in outcomes, documented register/propose/vote/deploy lifecycle.

3. **Governance:** evidence in the UI, Nido wallet support, per-project voting config (e.g. gatekeep
   voting), yes/no outcome rework where feasible; result types, storage/TTL, vote-casting cost
   ([#111](https://github.com/Consulting-Manao/tansu/issues/111)).

4. **Maintenance:** audit-bank prep (internal perimeter map and runbook), dependency updates,
   progress on the Radicle migration.

**Conditional:** If
[Nouns Builder on Stellar](https://communityfund.stellar.org/dashboard/submissions/recinNIkq2DGjZ8Hq)
is funded, coordinate on NQG/Tansu per their [roadmap](https://hackmd.io/@dan13ram/r123BqdJMl).
<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

**D1: Public Goods Award**

Tansu hosts the PG Award program.

- **Program NQG score:** with SDF engineering and SCF team on PG Award-specific scoring;
- **SCF NFT:** workflow to sync the data with the source of truth;
- **Mid-grant reviews:** tranche-2 review flow can be moved to GitHub and Tansu (template, outcome
  hooks);
- **Collateral rework:** Merkle-based collateral or other mechanism to alleviate the contract
  constraints
  [#111](https://github.com/Consulting-Manao/tansu/issues/111)[#112](https://github.com/Consulting-Manao/tansu/issues/112);
- **Q3 round:** intake, D&R, on-chain vote, open office hours, execution with SDF Community;
- **Conditional:** Nouns Builder NQG alignment if their grant is approved.

Measure: Q3 vote on testnet; mainnet NFT/NQG populated; mid-grant template shipped; collateral fix
merged.

**D2: Stellar Registry**

Registry Security Council vote on Tansu.

- **`registry-tansu-manager` factory:** authorization contracts governed via Tansu
  ([stellar-registry/contracts](https://github.com/stellar-registry/contracts/tree/main/contracts/registry-tansu-manager));
- **Proposal and outcome templates:** registry publish, flag, namespace, etc.
- **Registry name to address:** outcome contracts reference registry names; dApp resolves at
  creation/execution;
- **Contract lifecycle:** document register, propose, vote, deploy, version with Tansu in the loop;

Measure: Testnet demo: Tansu vote executes a registry action; templates in dApp; name resolution
works.

**D3: Governance features**

- **Evidence in dApp:** SBOM/CVE/Attestation on project pages
  [#204](https://github.com/Consulting-Manao/tansu/issues/204)[#196](https://github.com/Consulting-Manao/tansu/issues/196)
- **Nido wallet support:** passkey smart accounts with [nido.fyi](https://nido.fyi);
- **Governance configuration:** rethink a per-project configuration for membership, weight mode,
  collateral;
- **Yes/no outcomes:** rethink the outcome flow.

Measure: Evidence on project pages and management in the dApp itself; Nido support with a transparent
on-boarding and usage of Tansu; per-project config documented; yes/no approach documented.

**D4: Maintenance, Security and Operations**

- **Result types** across contract, SDK, and dApp;
- **Storage / TTL:** rent bump and TTL policy for Soroban storage;
- **Audit-bank prep**: perimeter map, risk notes, runbook;
- **Dependencies:** Soroban SDK, Stellar JS, CI deps current;
- **Radicle:** assess gaps and use more
  ([radicle.consulting-manao.com](https://radicle.network/nodes/radicle.consulting-manao.com)).

Measure: Result types consistency; TTL strategy documented and applied; #111 merged or scoped with
plan; runbook published; assessment addendum; dependencies up-to-date; Radicle usage with some
patches and issues.
<!-- markdownlint-enable MD034 -->

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
