---
title: "Hyperledger Solang"
parent: Public Good Projects
proposal_issue: 49
proposer: salaheldinsoliman
category: "Other"
budget: "20000"
---

# Hyperledger Solang

_Solang is a Solidity compiler for Stellar._

|                      |                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| **Category**         | Other                                                                                              |
| **Website**          | <https://solang.io/>                                                                               |
| **Repository**       | <https://github.com/hyperledger-solang/solang>                                                     |
| **First Released**   | November 2025                                                                                      |
| **Intake**           | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/24> |
| **Budget Requested** | 20000                                                                                              |

## Project Description

Solang is a Solidity compiler for Stellar which lives under
[LFDT](https://www.lfdecentralizedtrust.org/). We aim to have the following impact on Stellar
ecosystem.

### Long-term impact

- Enable a production-ready compiler for Stellar.
- Lower the barrier for Solidity developers to build on Stellar.

### Short-term impact

- Build an open-source contributor community with deep knowledge of both Solidity and the Soroban VM
  architecture through yearly
  [LFDT mentorships](https://www.lfdecentralizedtrust.org/blog/tag/mentorship-program).
- Provide a practical onboarding path for EVM developers who want to experiment with Soroban.
- Produce comparative research between Solang and the Soroban Rust SDK, generating insights about
  where each approach performs best and for which use cases.
- Gather early feedback on Solang tooling, developer experience, and developer pain points.

## Team & Experience

@salaheldinsoliman: A compiler engineer working on Solang to support the Soroban target.

@mohamedbasuony: A software engineer in the university of Göttingen, with an interest in developer
tooling.

@abdallah-abdelnaby: A software engineer in the university of Göttingen, with an interest in compiler
engineering.

@Imran-S-heikh: A full stack engineer, mainly working on Solang Playground and the Solang language
server

## Retroactive Impact

- Since
  [soft launching Solang and its Playground](https://medium.com/@salaheldin_sameh/announcing-solang-compiler-suite-solidity-support-for-stellars-soroban-1fa82335101b),
  we've had ~20 monthly active users, from which we are receiving feedback to improve the compiler
  and its tooling.

- We've completed a
  [Linux Foundation mentorship](https://medium.com/@pratykshgupta9999/my-journey-as-an-lfx-mentee-enhancing-solangs-soroban-integration-for-stellar-285b8907502f),
  and are on the way to completing
  [another mentorship with a focus on comparing Solang to the Stellar Rust SDK](https://github.com/LF-Decentralized-Trust-Mentorships/mentorship-program/issues/74).

## Past Deliverables

The target last quarter was to support the following
[Soroban examples](https://github.com/stellar/soroban-examples) by making Solang able to compile the
logically equivalent Solidity:

- [Atomic Swap](https://github.com/stellar/soroban-examples/blob/main/atomic_swap/src/lib.rs)
- [Atomic Multi Swap](https://github.com/hyperledger-solang/solang/tree/main/examples/soroban/atomic_swap)
- [Liquidity Pool](https://github.com/hyperledger-solang/solang/tree/main/examples/soroban/liquidity_pool)
- [Timelock](https://github.com/hyperledger-solang/solang/tree/main/examples/soroban/timelock)

The proof of completion is basically copying the contract, compiling it via Solang, and calling it as
you would with the Stellar CLI or the JS SDK.

Alternatively, they can be tested in the playground https://solang.io/. (Not up to date at the time
of writing this, will update this PR once it supports the latest version)

## Proposed Impact

- Onboard an open-source contributor to Solang and Stellar via this
  [mentorship](https://github.com/LF-Decentralized-Trust-Mentorships/mentorship-program/issues/74),
  starting in June 2026.

- Release a new version of Solang and Playground, announce it, and get more feedback.

## Proposed Deliverables

The main goal of trying to include Solang in the PG awards is to _**bring it to production**_.
Bringing Solang to production involves covering all Solidity features and then auditing the codebase.
To know how much Solidity is already covered, and how much work is left, a fuzzer that compares the
behavior of Solidity contracts on `solc`+`ethereum` vs `solang` + `Stellar` is needed. This will give
us an idea of what work is left besides supporting the
[Soroban-examples](https://github.com/stellar/soroban-examples).

This quarter/PG-proposal is focused on completing the remaining work on the Soroban examples, and
starting work on the fuzzer. Future proposals are expected to focus on completing the work the fuzzer
outputs, and then auditing the codebase.

Our specific goals for the next quarter are:

### Codebase maintenance

- A current issue of the codebase is the entangled target logic in
  [`codegen`](https://github.com/hyperledger-solang/solang/tree/main/src/codegen). As Solang supports
  multiple compilation targets, some target-specific logic and conditionals are scattered in codegen
  (Solang's IR emission stage). Detangling here means that each target should have its own
  implementation of `codegen`, rather than injecting target-specific logic.

### Developer Experience

- Make [Solang docs](https://solang.readthedocs.io/en/v0.3.4/) up to date: clearly state what is
  currently supported and what is not.
- Improve compiler error reporting: As of now, for the currently unsupported Solidity syntax or
  Soroban-specific features, Solang most often fails with a vague error message. We aim to fix this
  in this quarter.
- More useful error reporting in Solang Playground.

### Feature Completion

- Support the remaining [Soroban-examples](https://github.com/stellar/soroban-examples)

### Fuzzer

- Plan and start working on a fuzzer that compares a corpus of Solidity contracts' behavior on
  `solc`+`ethereum` vs `solang` + `Stellar`. This will give us an idea of what work is left besides
  supporting the [Soroban-examples](https://github.com/stellar/soroban-examples). **At the end of
  this quarter, the fuzzer should be able to take a corpus of Solidity contracts and report Solang
  compilation errors.**

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
