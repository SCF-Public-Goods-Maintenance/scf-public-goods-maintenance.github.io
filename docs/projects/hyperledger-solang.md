---
title: "Hyperledger Solang"
parent: Public Good Projects
proposal_issue: 122
proposer: salaheldinsoliman
category: "Developer Experience"
budget: "$25,000"
---

# Hyperledger Solang

<!-- markdownlint-disable MD036 -->

_A Solidity compiler for Stellar_

<!-- markdownlint-enable MD036 -->

|                      |                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| **Category**         | Developer Experience                                                                               |
| **Website**          | <https://solang.io/>                                                                               |
| **Repository**       | <https://github.com/hyperledger-solang/solang>                                                     |
| **First Released**   | November 2025                                                                                      |
| **Intake**           | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/24> |
| **Budget Requested** | $25,000                                                                                            |

## Project Description

<!-- markdownlint-disable MD034 -->

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

<!-- markdownlint-enable MD034 -->

## Team & Experience

<!-- markdownlint-disable MD034 -->

@salaheldinsoliman: A compiler engineer working on Solang to support the Soroban target.

@mohamedbasuony: A software engineer in the university of Göttingen, with an interest in developer
tooling.

@abdallah-abdelnaby: A software engineer in the university of Göttingen, with an interest in compiler
engineering.

@Islam-Imad: A software engineer with an interest in compilers and low-level systems programming

<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->

- Since
  [soft launching Solang and its Playground](https://medium.com/@salaheldin_sameh/announcing-solang-compiler-suite-solidity-support-for-stellars-soroban-1fa82335101b),
  we've had ~20 monthly active users, from which we are receiving feedback to improve the compiler
  and its tooling.

- LFDT accepted a Solang Mentorship in it's Mentorship program; we've selected @aryanbaranwal001 who
  will be working on
  [comparing Solang to the Stellar Rust SDK](https://github.com/LF-Decentralized-Trust-Mentorships/mentorship-program/issues/74)
  in terms of behavior, performance and binary size.

<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

The deliverables of Q2 were categorized as follows:

### Codebase maintenance

- `Deliverable`: A current issue of the codebase is the entangled target logic in
  [`codegen`](https://github.com/hyperledger-solang/solang/tree/main/src/codegen). As Solang supports
  multiple compilation targets, some target-specific logic and conditionals are scattered in codegen
  (Solang's IR emission stage). Detangling here means that each target should have its own
  implementation of `codegen`, rather than injecting target-specific logic.
- `Proof of completion`: This [PR](https://github.com/hyperledger-solang/solang/pull/1923) introduces
  a `TargetCodegen` trait, relocates the Solana / Polkadot / Soroban backends under
  `src/codegen/targets/`, threads the target through the lowering call graph, and routes
  target-specific hooks (abi encode/decode, storage arrays, events, builtins, load/store) through the
  trait. This separates target concerns and detangles target-specific logic in codegen, reducing the
  amount of code that needs auditing.

### Developer Experience

`Deliverables:`

- Make [Solang docs](https://solang.readthedocs.io/en/v0.3.4/) up to date: clearly state what is
  currently supported and what is not.
- Improve compiler error reporting: As of now, for the currently unsupported Solidity syntax or
  Soroban-specific features, Solang most often fails with a vague error message. We aim to fix this
  in this quarter.
- More useful error reporting in Solang Playground.

`Proof of Completion:`

- Docs: the Soroban documentation was reorganized to clearly separate supported vs. unsupported
  features and state the current support status:
  [#1883](https://github.com/hyperledger-solang/solang/pull/1883).
- Compiler error reporting: unsupported Soroban ABI types are now rejected _before_ codegen with a
  clear diagnostic instead of a vague, late failure:
  [#1903](https://github.com/hyperledger-solang/solang/pull/1903) (fixes
  [#1897](https://github.com/hyperledger-solang/solang/issues/1897)).
- Playground error reporting: full Solang compiler diagnostics (warnings, multi-line source spans,
  and fallback output) are now propagated end-to-end through the Playground compile flow to the UI,
  instead of being truncated to a single stripped `error:` line:
  [solang-playground#35](https://github.com/hyperledger-solang/solang-playground/pull/35) (merged to
  `develop`).

### Feature Completion

`Deliverable:`

- Support the remaining [Soroban-examples](https://github.com/stellar/soroban-examples).

`Proof of Completion:`

- The upstream Soroban **`events`** example — previously unsupported (Solang panicked on `emit` for
  Soroban) — is now compiled and tested, enabled by implementing event emission via the
  `contract_event` host function ([#1893](https://github.com/hyperledger-solang/solang/pull/1893)).
  Covered by
  [`tests/soroban_testcases/events.rs`](https://github.com/hyperledger-solang/solang/blob/v0.3.5/tests/soroban_testcases/events.rs).
- The new `string` / `bytes` / `bytesN` support
  ([#1927](https://github.com/hyperledger-solang/solang/pull/1927)) together with struct and vector
  support now makes several previously-blocked upstream examples expressible in Solidity (tracked in
  [#1901](https://github.com/hyperledger-solang/solang/issues/1901)) — e.g. `custom_types`
  (struct-backed values returned from public APIs), `atomic_multiswap` (a `SwapSpec` struct +
  vectors), `single_offer` (token + cross-contract trading), and `other_custom_types`
  (structs/enums/vectors/events).
- A reusable `pause` example was added
  ([#1907](https://github.com/hyperledger-solang/solang/pull/1907)), with `increment_with_pause` in
  progress ([#1911](https://github.com/hyperledger-solang/solang/pull/1911)).
- Coverage continues to expand via in-flight work: dynamic `bytes` in the ABI/codec
  ([#1904](https://github.com/hyperledger-solang/solang/pull/1904)), `bytesN` parameters/returns
  ([#1908](https://github.com/hyperledger-solang/solang/pull/1908)), storage vectors
  ([#1848](https://github.com/hyperledger-solang/solang/pull/1848)), and `sha256`/`keccak256`
  builtins ([#1919](https://github.com/hyperledger-solang/solang/pull/1919)) — which unlock
  bytes-heavy and hash-based examples such as `eth_abi` and `merkle_distribution`.
- All of the above build on the already-supported set (token, atomic_swap, liquidity_pool, timelock,
  auth, TTL, cross-contract calls, `print` logging, storage/arrays) and were shipped in Solang
  **v0.3.5 "Luxor"** ([#1930](https://github.com/hyperledger-solang/solang/pull/1930) ·
  [crates.io](https://crates.io/crates/solang/0.3.5)).
- **Status (2026-07-26):** per-example coverage is now tracked in
  [#1901](https://github.com/hyperledger-solang/solang/issues/1901) with the calculation shown
  openly: **40% merged** (10 of the 25 upstream examples that are language features), **60% when open
  PRs are included** — `mint-lock` ([#1985](https://github.com/hyperledger-solang/solang/pull/1985)),
  `other_custom_types` ([#1983](https://github.com/hyperledger-solang/solang/pull/1983)), the
  idiomatic `atomic_multiswap` via arrays-of-structs support
  ([#1986](https://github.com/hyperledger-solang/solang/pull/1986)), `single_offer`
  ([#1968](https://github.com/hyperledger-solang/solang/pull/1968)) and `increment_with_pause`
  ([#1977](https://github.com/hyperledger-solang/solang/pull/1977)). The remaining work is explicitly
  carried into this proposal as Deliverable 4 below.

### Fuzzer

`Deliverable:`

- Plan and start a fuzzer that compares a corpus of Solidity contracts' behavior on `solc`+`ethereum`
  vs `solang`+`Stellar`. At the end of this quarter, the fuzzer should be able to take a corpus of
  Solidity contracts and report Solang compilation errors.

`Proof of Completion:`

- The fuzzing harness [`solang-fuzz`](https://github.com/salaheldinsoliman/fuzzer) — originally
  authored by [@jubnzv](https://github.com/jubnzv)
  ([jubnzv/solang-fuzz](https://github.com/jubnzv/solang-fuzz), built on their `multifuzz`, `afl-ts`
  and `tsgen` tooling) — is an AFL++ harness with a `tree-sitter-solidity` mutator that targets
  Solang's `codegen` and `sema` passes across the Solana, Polkadot and Soroban targets.
- The fuzzer took a corpus of Solidity contracts and surfaced **25 distinct, reproducible compiler
  crashes**, each triaged and reported as an issue on Solang by [@jubnzv](https://github.com/jubnzv),
  some of them are:
  - sema panics: [#1868](https://github.com/hyperledger-solang/solang/issues/1868),
    [#1869](https://github.com/hyperledger-solang/solang/issues/1869),
  - codegen panics: [#1862](https://github.com/hyperledger-solang/solang/issues/1862),
    [#1863](https://github.com/hyperledger-solang/solang/issues/1863),
    [#1880](https://github.com/hyperledger-solang/solang/issues/1880)
  - Soroban-specific crashes: [#1872](https://github.com/hyperledger-solang/solang/issues/1872),
    [#1905](https://github.com/hyperledger-solang/solang/issues/1905),
    [#1910](https://github.com/hyperledger-solang/solang/issues/1910)
  - a const-fold miscompile: [#1926](https://github.com/hyperledger-solang/solang/issues/1926)

<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

- **Expand Solidity support via fuzzing.** Keep running and improving the
  [Solang fuzzer](https://github.com/salaheldinsoliman/fuzzer) to harden the compiler and widen
  Solidity coverage — triaging and fixing the crashes it surfaces.

- **Announce the new "Luxor" release.** Publish and announce Solang
  [v0.3.5 "Luxor"](https://github.com/hyperledger-solang/solang/releases/tag/v0.3.5), which adds new
  Soroban examples (e.g. `events`) and a batch of Solidity/compiler fixes, so the Stellar ecosystem
  can build on the latest compiler.

- **Gather another round of feedback.** Put the new release, the Playground, and the language server
  in front of users and collect feedback on the compiler and its tooling to prioritize the next round
  of work.

- **Complete the LFDT mentorship.** Finish the ongoing
  [mentorship](https://github.com/LF-Decentralized-Trust-Mentorships/mentorship-program/issues/74),
  growing an open-source contributor with deep Solang and Soroban knowledge.

- **Make Stellar easier to onboard via Solang.** Lower the barrier for Solidity/EVM developers to
  build on Stellar.

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

## Proposed Deliverables (next three months)

### 1. Extend Solidity support via fuzzing — harden the compiler

Continue running and improving the [Solang fuzzer](https://github.com/salaheldinsoliman/fuzzer),
triaging and fixing the compiler crashes it surfaces. Robustness is the gating requirement to bring
Solang to production, so fewer compiler crashes directly de-risk deploying Solidity contracts on
Soroban.

- **SMART alignment:** specific and measurable — fix ≥ 20 of the ~25 open fuzzer-found crashes (plus
  any new ones), keep the fuzzer running continuously with triaged issue reports, and extend its
  coverage (mutators / target passes) to reach different compiler paths; achievable, as the fuzzer
  already exists and a wave of fixes is already in flight (e.g. #1884–#1894, #1915, #1924); relevant
  to bringing Solang to production; and time-bound to the next three months.

### 2. Differential tester — first working version (via the LFDT mentorship)

Through the
[LFDT mentorship](https://github.com/LF-Decentralized-Trust-Mentorships/mentorship-program/issues/74),
build a differential tester — a separate tool from the fuzzer — that compiles and runs the same
Solidity contract on `solc`+EVM and `solang`+Soroban and compares observable behavior to surface
_miscompiles_ (semantic divergences), not just crashes. This catches correctness bugs a crash-fuzzer
cannot, the next level of production-readiness assurance for Solidity on Stellar.

- **SMART alignment:** specific and measurable — deliver a first working version that runs a set of
  Solidity contracts through both toolchains and reports behavioral divergences; achievable, as the
  mentorship is already underway
  ([#74](https://github.com/LF-Decentralized-Trust-Mentorships/mentorship-program/issues/74));
  relevant to compiler correctness for Stellar; and time-bound to the next three months, when the
  mentorship concludes.

### 3. Grow developer reach and run a structured feedback round

Produce Solidity-on-Stellar developer content — blog posts, a video walkthrough, and a live workshop
— centered on the new **Luxor (v0.3.5)** release and the Playground, then collect and triage
feedback. This lowers the onboarding barrier for Solidity/EVM developers to Stellar, grows adoption,
and creates a prioritized feedback loop that steers future work.

- **SMART alignment:** specific and measurable — publish ≥ 2 blog posts and ≥ 1 video, run ≥ 1
  workshop/live session, gather feedback from ≥ 25 developers, and convert it into ≥ 15 prioritized
  GitHub issues; achievable given our ~20 monthly active users and prior launch reach; relevant to
  adoption and onboarding; and time-bound to the next three months.

### 4. Support the remaining Soroban examples (carried over from Q2)

Complete the remaining feasible upstream
[soroban-examples](https://github.com/stellar/soroban-examples), fixing the compiler gaps they expose
along the way — this quarter showed that most "example" work is really compiler work (array
allocation, ABI returns, arrays of structs as parameters). Progress is tracked per example, with
coverage percentages and the calculation shown, in
[#1901](https://github.com/hyperledger-solang/solang/issues/1901).

- **SMART alignment:** specific and measurable — raise **merged** coverage from 40% (10/25) to ≥ 68%
  (17/25) by landing the five examples currently in open PRs
  ([#1983](https://github.com/hyperledger-solang/solang/pull/1983),
  [#1985](https://github.com/hyperledger-solang/solang/pull/1985),
  [#1986](https://github.com/hyperledger-solang/solang/pull/1986),
  [#1968](https://github.com/hyperledger-solang/solang/pull/1968),
  [#1977](https://github.com/hyperledger-solang/solang/pull/1977)) and adding `eth_abi` and
  `merkle_distribution`; the 8 examples requiring new host-function support (custom accounts,
  deploy/upgrade, BLS/ZK) are explicitly out of scope for this quarter and tracked separately in
  #1901; achievable, as the blocking compiler fixes are already in review; relevant to
  Solidity-on-Stellar parity; and time-bound to the next three months.

<!-- markdownlint-enable MD034 -->

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban)
[![Criticality](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban&query=%24.criticality_score&label=Criticality&color=E5484D)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
