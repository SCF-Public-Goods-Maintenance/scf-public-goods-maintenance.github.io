---
title: "Tansu - Decentralized project governance on Stellar"
canonical_id: daoip-5:scf:project:tansu_-_soroban_versioning
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
| **Budget Requested** | 50000                                                                                              |

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

In Q3 2026, Tansu hosted the second SCF Public Goods Award round. SCF Pilots voted anonymously with
NQG-weighted ballots on the `stellarpgq3` project on testnet. 18 projects were approved for a total
of $453,000, with a median ask of $16,500. 22 Pilots voted, with a median of 17.5 voters per
proposal. The vote went through without incident. The computational cost and collateral issues seen
in Q2 did not come back.

The Stellar Registry became the second user of Tansu. Its root registry is governed by Tansu votes,
and the Registry's web app now creates Tansu proposals directly from its own forms.

Most of the quarter went into the membership stack, well beyond the sync workflow the deliverable
asked for. The SCF membership contract was moved out of Tansu and rebuilt as
[`stellar-membership`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:z4KRDyBiL6kP6n5FWP6kJWga6BXJV):
a soulbound membership token with verified Discord, GitHub and email and PG Atlas projects, an app
and an API, recovery, and operators. Members are now promoted by the Pilots through votes on Tansu,
weighed by their NQG, and the membership contract serves NQG to Tansu as voting power. It has 202
commits, all on Radicle.

On Tansu itself, maintainers can now attest commits and evidence until a release is final,
discussions travel with proposals, governance is configured per project, and passkey wallets are
supported. The quarter ended with a security round: a fresh pre-audit of the contracts, followed by
fixes for its Critical and High findings. A second review after the fixes found no Critical or High
issue left. The documentation and an operations runbook were brought up to date.

I kept taking part in the Drips Waves. Twelve `Stellar Wave` issues were closed this quarter, 47 in
total.

<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

### 2026 Q3

#### Q3 D1: Public Goods Award

Proof of completion:

- Q3 round: [`stellarpgq3`](https://testnet.tansu.dev/governance/?name=stellarpgq3) on the testnet
  contract
  [`CBXKUSLQPVF35FYURR5C42BPYA5UOVDXX2ELKIM2CAJMCI6HXG2BHGZA`](https://stellar.expert/explorer/testnet/contract/CBXKUSLQPVF35FYURR5C42BPYA5UOVDXX2ELKIM2CAJMCI6HXG2BHGZA).
  19 anonymous proposals, 17 approved on 11 August and a revised Stellarlight proposal approved on 23
  September. 18 projects approved for $453,000, median ask $16,500, 22 Pilots voting with a median of
  17.5 per proposal. Stellarlight is counted once, at its revised budget.
- Program NQG score: each Tansu project sets its own NQG contract, read as a `u32` weight
  [`f0aef91`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/f0aef910d7fe48b2d6f74ba55479f6abe977f123).
  The membership contract answers it with a member's NQG
  [`2e6166f`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:z4KRDyBiL6kP6n5FWP6kJWga6BXJV/commits/2e6166fecfa74a3dcb7a7f0d2ad15e9e7d14b534),
  [`825e3d7`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:z4KRDyBiL6kP6n5FWP6kJWga6BXJV/commits/825e3d71a2f79edb19484ed8494e47f83b8c0656),
  so a program's score plugs in per project.
- SCF NFT and Neurons, met and exceeded: membership rebuilt as
  [`stellar-membership`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:z4KRDyBiL6kP6n5FWP6kJWga6BXJV)
  [`ccc3d5f`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:z4KRDyBiL6kP6n5FWP6kJWga6BXJV/commits/ccc3d5fb1399ec0886ba1c7db00b1649caae2e90)
  and moved out of Tansu
  [`07b55bd`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/07b55bda37b2f5408fa52d69113b98285b370f5c),
  [`f1631dc`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/f1631dcae8ed7a1978d58bd5fc06efa687ec861e).
  On top of the sync with the source of truth, it adds recovery, several operators
  [`7d00ec2`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:z4KRDyBiL6kP6n5FWP6kJWga6BXJV/commits/7d00ec2aa89c47f112d7dbd61777ce9769a2a820),
  promotions to the next role voted by the Pilots on Tansu
  [`d85c76b`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:z4KRDyBiL6kP6n5FWP6kJWga6BXJV/commits/d85c76b0ec2561fc446ad14735073ba43ce25850),
  two audit passes
  [`2b7565f`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:z4KRDyBiL6kP6n5FWP6kJWga6BXJV/commits/2b7565f32052946bff0838e2de5d69d9393530a3),
  [`166d59c`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:z4KRDyBiL6kP6n5FWP6kJWga6BXJV/commits/166d59c756227e3f8eab0feda7b55cac36986ee8)
  and full documentation
  [`6f80468`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:z4KRDyBiL6kP6n5FWP6kJWga6BXJV/commits/6f80468b14c96c306559c80bac42b1e87950c172).
  Deployed on testnet. Mainnet with SCF's member data follows with SDF.
- Mid-grant reviews: the grant review process was worked out with the working group. An AI layer
  takes over the repetitive steps of the reviews.
- Nouns Builder: postponed, as their work is not ready. We held calls with the team to work on the
  topic and support them.

#### Q3 D2: Stellar Registry

Proof of completion:

- Registry governed by Tansu: Tansu-DAO-gated registry manager
  ([stellar-registry/contracts#5](https://github.com/stellar-registry/contracts/pull/5)), verified
  end to end on testnet: proposal, vote, `trigger`, publish.
- Proposals from the Registry: the Registry's web app creates Tansu proposals
  ([stellar-registry/ui#67](https://github.com/stellar-registry/ui/pull/67),
  [#68](https://github.com/stellar-registry/ui/pull/68)).
- Templates and name resolution in the dApp: 7 proposal templates and outcome templates, including a
  Registry publish
  [`8f5c61e`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/8f5c61e8326d6d9dea06b6d36c9cdb9089f573a6),
  [`9b7535b`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/9b7535b53f3d7189768ae8ef3b0067578370594c),
  and the Registry's own proposal forms. Registry names resolve to addresses when the proposal is
  created
  [`85e7a6b`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/85e7a6baba813a3cdb1287cea3726164329d4901),
  and the name is checked again at execution, with a warning if it now points elsewhere
  [`ba43800`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/ba43800a793217fd542aab1ae8d7ac2d43904b0a).
- Contract lifecycle: documented in
  [Acting on other contracts](https://tansu.dev/docs/developers/governance#acting-on-other-contracts)
  [`dfba035`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/dfba0358bde72cb88f6d8bb34e38fac5d27e664f).
  Outcomes now run from a separate executor contract, so they never act with Tansu's own authority
  [`f490db1`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/f490db1250085ba889cd049b70e585cec11f4684).

#### Q3 D3: Governance features

Proof of completion:

- Evidence in the dApp: SBOM, CVE and attestation evidence uploaded and listed per commit
  [`c21688c`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/c21688cd3bbcaabd7974c4067583fb627dffce8f),
  [`242cfad`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/242cfad14480f45e7cc24b4b9e15dafad3839941).
- Endorsement: maintainers attest a commit or an evidence artifact until it is final
  [`6c47a83`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/6c47a833f591a6ae37affcc495933065b2e48da4),
  documented in [Code Finality](https://tansu.dev/docs/developers/code_finality)
  [`958f391`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/958f391d7adac05721aac5a7e6f8181cb77fbe71).
- Governance configuration: voting period, execution delay and finality threshold per project
  [`2f97539`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/2f97539ab7fb2a2ee46573906495d82b4267131f),
  [`4ee9d62`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/4ee9d627fc6bf6411363248ba6b73c1f391bb890),
  [`258923e`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/258923e6d978724053a50c789932ac2a827e4628);
  NQG weight per project
  [`f0aef91`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/f0aef910d7fe48b2d6f74ba55479f6abe977f123);
  token-weighted proposals reserved to maintainers
  [`a9b9334`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/a9b9334c15a7fb5136e121830cf912ff7622c715).
- Collateral: voting no longer takes collateral
  [`526395e`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/526395e941a6e1ec3f573f66446952d9eb05c4f7).
  Sybil resistance relies on voting weight, NQG score or badges, and at most 20 weight-1 votes per
  proposal
  [`720e640`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/720e640c1b43659c510cc51952cbf5ed15a4c9c9).
  Documented in
  [Spam and Sybil resistance](https://tansu.dev/docs/developers/governance#spam-and-sybil-resistance)
  [`dfba035`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/dfba0358bde72cb88f6d8bb34e38fac5d27e664f).
- Discussions: rendered on proposals
  [`844f8c1`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/844f8c19de4ceda4695ded88cac858b22de4a325),
  and produced from the GitHub thread by this repository's
  [`pg-award-proposal-onchain.yml`](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/blob/main/.github/workflows/pg-award-proposal-onchain.yml)
  workflow.

#### Q3 D4: Maintenance, Security and Operations

Proof of completion:

- Passkey wallets: Nido smart accounts and GHOSTSIG
  [`c66c39c`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/c66c39c5c1f231470371f7c373cdffdd7fbd02bd),
  [`5c21a20`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/5c21a20a8223cb84eca2a78108b4435d3689d43a),
  [`95d3741`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/95d374155fba765fc79fb6fccf71ba68b084d7c7).
- Result types: not needed, by design. Every failure is a typed error of one enum. Soroban reports a
  typed panic and a returned `Err` the same way to the caller, `Error(Contract, #code)`, and rolls
  back both. The dApp maps each code to a message, kept in sync with the contract by a lint check.
  Changing every entry point to return `Result` would change every signature and binding, and users
  would see the same errors.
- Storage and TTL: users pay for what they use, by design. An archived entry is restored
  automatically, data intact, by the next transaction that touches it, which pays for it. Extending
  TTL in the contract would make every caller pay rent for data they may never read, or need a
  treasury and a keeper forever. Documented for operators in the runbook
  [`51b3318`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/51b3318def2c34a4a8954760e768ae94928ca0b3).
- Audit-bank prep: fresh pre-audit of the contracts
  [`afcd58f`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/afcd58f3bd361a3b255226f8a76a7d0a07686d25),
  fixes
  [`f490db1`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/f490db1250085ba889cd049b70e585cec11f4684)
  to
  [`f8985ff`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/f8985ff045c7de78e6f9c30dc6d70eabf31722ef),
  and the status of each finding
  [`ef1e095`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/ef1e095d44b5c20ed8c5561dec837291686710f2).
  A second pre-audit after the fixes
  [`55ace02`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/55ace02f5388f0fca9be52f99db3fd3c51df5764)
  finds 0 Critical, 0 High and 2 Medium issues, and rates the contracts close to audit-ready.
  Operations runbook
  [`51b3318`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/51b3318def2c34a4a8954760e768ae94928ca0b3).
- Dependencies: `soroban-sdk` 28.0.0
  [`7d9b274`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/7d9b2743ed91b98b3324506c15a9b6593cd0a78a),
  Protocol 28
  [`30984c2`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/30984c2828ddddc3031c12c23102e22bbd30070b),
  every dApp dependency updated
  [`90b7a62`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/90b7a626185fe1b708d5f19541176c959caa8e30),
  [`f07f86c`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/f07f86c0d6eb8c9264d7a51725ef6bbf77c05655),
  Dependabot across Rust, Bun and GitHub Actions.
- Upgrade: the testnet contract was upgraded in place, with a migration of proposals to their new
  storage that kept the Q2 and Q3 rounds
  [`575e2ae`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/575e2ae151f176eb1332f3eb9310311239122ae0),
  [`f48aca4`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/f48aca48fe8e811b6b58480f54c98eadfbb5762f),
  [`7027798`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/7027798a94382da122cafddc94a58d408b676976).
- Maintenance: the dApp reads the contract through a persistent query cache
  [`b3bfd33`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/b3bfd33ab1f35d8b408a8b65eb259a02e81a2411),
  lands every write through one path
  [`a1fee21`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/a1fee2182950327d662079593797a1d89c3c30ef),
  installs as an accessible app that works offline
  [`31ce603`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/31ce6039c903ce67a0b947580e3ae31a5cbc862d),
  [`f9638ae`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/f9638ae7c147e7decdbd6964d4f9dbd0b888f273),
  and runs its end-to-end flows on testnet
  [`30d5b11`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/30d5b1132f61a22e2f9bb719fe3ee080cc8b0d3f).
- Drips Wave: for instance [#15](https://github.com/Consulting-Manao/tansu/issues/15),
  [#26](https://github.com/Consulting-Manao/tansu/issues/26),
  [#25](https://github.com/Consulting-Manao/tansu/issues/25) (evidence),
  [#215](https://github.com/Consulting-Manao/tansu/issues/215) (discussions),
  [#230](https://github.com/Consulting-Manao/tansu/issues/230),
  [#232](https://github.com/Consulting-Manao/tansu/issues/232) (outcome templates and Registry
  names), [#16](https://github.com/Consulting-Manao/tansu/issues/16) (Git identity),
  [#229](https://github.com/Consulting-Manao/tansu/issues/229) (voting receipt).
- Radicle: development happens on
  [radicle.consulting-manao.com](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s)
  with patches merged there
  [`f737729`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/f73772921405f7dd8769c8964ffb1659bdbc9384),
  Radicle is a supported forge in Tansu
  [`e75becc`](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/commits/e75becc560c0a05c92d06baac61688d12051bf3d),
  and every commit linked on this page is on Radicle.

### 2026 Q2

#### P1: Q2 Public Goods Award on Tansu testnet

Proof of completion:

- Round completed on `stellarpg` (on the sub-project `stellarpga`) on testnet:
  [testnet.tansu.dev](https://testnet.tansu.dev)
- [Q2 round blog post](https://tansu.dev/blog/public-goods-award-q2)
- [Program repository](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io)

First PG Award round with anonymous NQG-weighted pilot voting on testnet; 17 projects funded, more
than $400,000 disbursed. The work was done as part of a
[SCF Build Award](https://communityfund.stellar.org/project/pg-atlas-dse).

#### P2: Governance stack

Proof of completion:

- Conflict of interest: [#94](https://github.com/Consulting-Manao/tansu/pull/94),
  [#151](https://github.com/Consulting-Manao/tansu/pull/151)
- Soroban Domains removed and collateral system:
  [#157](https://github.com/Consulting-Manao/tansu/pull/157),
  [blog](https://tansu.dev/blog/docs-update-collateral-forges-weights)
- Anonymous voting, token-weighted ballots, outcome contracts, malicious-proposal flow:
  [governance docs](https://tansu.dev/docs/developers/governance)

#### P3: NQG + `scf-membership`

Proof of completion:

- `NqgProjectKey` and `contracts/scf-membership/`:
  [#50](https://github.com/Consulting-Manao/tansu/pull/50)
- Viewer: https://scf.pgatlas.xyz https://github.com/Consulting-Manao/scf-member-explorer

#### P4: Supply chain and evidence

Proof of completion:

- Unified `set_evidence` API: [#186](https://github.com/Consulting-Manao/tansu/pull/186),
  `tools/evidence/publish.sh`
- SBOM CI and on-chain recording: [#145](https://github.com/Consulting-Manao/tansu/pull/145),
  .github/workflows/sbom.yml`
- Workflows improvements: `.github/workflows`

#### P5: Maintainance

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

Q3's objective is about making Tansu reliable and usable for our first users. The main goals are:

1. **PG Award Q3 on Tansu:** same testnet stack as Q2, we are going to run the Q3 program on Tansu
   and there are lots of things to figure out.

2. **Stellar Registry:** this is our second use case, the registry has it's own set of constraints
   and we need to see how to effectively support the project.

3. **Governance:** there are many things to improve, from the collateral system overall to new
   features around supply chain. Now that we have the first set of users, we have a better
   understanding of the scope and what we should do and not.

4. **Maintenance:** from the preparation to an audit, the migration to Radicle to many small code
   adjustments, there is a lot of continuous work.

**Conditional:** If
[Nouns Builder on Stellar](https://communityfund.stellar.org/dashboard/submissions/recinNIkq2DGjZ8Hq)
is funded, coordinate on NQG/Tansu per their [roadmap](https://hackmd.io/@dan13ram/r123BqdJMl).

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

### D1: Public Goods Award

Tansu hosts the PG Award program.

- **Program NQG score:** with SDF engineering and SCF team on PG Award-specific scoring
  [e07f96daae8e8bc9075dbe128b16e54357838f48](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/issues/e07f96daae8e8bc9075dbe128b16e54357838f48);
- **SCF NFT:** workflow to sync the data with the source of truth and work on Neurons
  [33d6cff5b33baf6171b686f51167eeb302407cd4](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/issues/33d6cff5b33baf6171b686f51167eeb302407cd4);
- **Mid-grant reviews:** tranche-2 review flow can be moved to GitHub and Tansu (template, outcome
  hooks);
- **Q3 round:** intake, D&R, on-chain vote, open office hours, execution with SDF Community;
- [Conditional **Nouns:**] Nouns Builder NQG alignment if their grant is approved
  [32e2f0739c61e8b739fc45053848b0b59f74a19d](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/issues/32e2f0739c61e8b739fc45053848b0b59f74a19d).

Measure: Q3 vote on testnet at https://testnet.tansu.dev/project/?name=stellarpgq3 ; (conditional on
SDF) mainnet NFT/NQG populated; mid-grant template shipped or new process proposal documented.

### D2: Stellar Registry

Registry Security Council vote on Tansu and further support
[3111b944792c0b5da9f6c8f88e52cdeebd1a3d82](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/issues/3111b944792c0b5da9f6c8f88e52cdeebd1a3d82).

- **`registry-tansu-manager` factory:** authorization contracts governed via Tansu
  ([stellar-registry/contracts](https://github.com/stellar-registry/contracts/tree/main/contracts/registry-tansu-manager));
- **Proposal and outcome templates:** registry publish, flag, namespace, etc.
- **Registry name to address:** outcome contracts reference registry names; dApp resolves at
  creation/execution;
- **Contract lifecycle:** document register, propose, vote, deploy, version with Tansu in the loop;

Measure: Testnet demo: Tansu vote executes a registry action; templates in dApp; name resolution
works.

### D3: Governance features

- **Evidence in dApp:** SBOM/CVE/Attestation usable
  [#204](https://github.com/Consulting-Manao/tansu/issues/204)[#196](https://github.com/Consulting-Manao/tansu/issues/196)
- **Governance configuration:** rethink a per-project configuration for membership, weight mode,
  rethink the outcome flow;
- **Collateral rework:** Merkle-based collateral or other mechanism to alleviate the contract
  constraints
  [c6a71ed20bd6bfd9af5f34c838135919c21ac2f4]([https://github.com/Consulting-Manao/tansu/issues/111)[#112](<https://github.com/Consulting-Manao/tansu/issues/112](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/issues/c6a71ed20bd6bfd9af5f34c838135919c21ac2f4)>);
- **Endorsement:** mechanism to attest a specific commit
  [8dea8085473cec6026e3a5c1126011fc4071e96a](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/issues/8dea8085473cec6026e3a5c1126011fc4071e96a).
- **Discussions:** improve the integration on Tansu of the discussions from GitHub
  [850a9420a6a4ac1fc0f091677455764fce3ab5b0](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/issues/850a9420a6a4ac1fc0f091677455764fce3ab5b0)

Measure: Evidence on project pages and management in the dApp itself; Nido support with a transparent
on-boarding and usage of Tansu; per-project config documented; yes/no approach documented; better
management of discussions and other artifacts.

### D4: Maintenance, Security and Operations

- **Nido wallet support:** passkey smart accounts with [nido.fyi](https://nido.fyi)
  [62fa73dfad0c043a58c90feb9ad92ea7310656b7](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/issues/62fa73dfad0c043a58c90feb9ad92ea7310656b7)
  and considering to use Blux;
- **Result types** across contract, SDK, and dApp. Evaluate the change from panics;
- **Storage / TTL:** rent bump and TTL policy for Soroban storage
  [40170febe4f792b0c802c79130e9d778f1cea7c4](https://radicle.network/nodes/radicle.consulting-manao.com/rad:zssaAF91kxuquZmZCV2SiK2FNX6s/issues/40170febe4f792b0c802c79130e9d778f1cea7c4);
- **Audit-bank prep**: perimeter map, risk notes, runbook;
- **Dependencies:** Soroban SDK, Stellar JS, CI deps kept current;
- **Drips Wave:** continue to promote Stellar and the Drips Wave platform;
- **Radicle:** assess gaps and use more
  ([radicle.consulting-manao.com](https://radicle.network/nodes/radicle.consulting-manao.com)).

Measure: UX improved with passkey based account supported, result types consistency documented; TTL
strategy documented and applied; runbook published; audit assessment addendum; dependencies
up-to-date; Radicle usage with some patches and issues.

<!-- markdownlint-enable MD034 -->

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Atansu_-_soroban_versioning&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Atansu_-_soroban_versioning)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Atansu_-_soroban_versioning&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Atansu_-_soroban_versioning)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Atansu_-_soroban_versioning&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Atansu_-_soroban_versioning)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Atansu_-_soroban_versioning&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Atansu_-_soroban_versioning)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
