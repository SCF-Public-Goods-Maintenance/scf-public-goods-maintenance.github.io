---
title: "Hyperledger Solang"
canonical_id: daoip-5:scf:project:solidity_contracts_on_soroban
parent: Public Good Projects
proposal_issue: 122
proposer: salaheldinsoliman
category: "Developer Experience"
budget: "$28,000"
---

# Hyperledger Solang

<!-- markdownlint-disable MD036 -->

_A Solidity compiler for Stellar_

<!-- markdownlint-enable MD036 -->

|                         |                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------- |
| **Category**            | Developer Experience                                                                               |
| **Website**             | <https://solang.io/>                                                                               |
| **Repository**          | <https://github.com/hyperledger-solang/solang>                                                     |
| **First Released**      | November 2025                                                                                      |
| **Intake**              | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/24> |
| **Budget Requested**    | $28,000                                                                                            |
| **Maintenance Reserve** | $5,000                                                                                             |
| **Other**               | $23,000                                                                                            |

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

### 2026 Q2

The deliverables of Q2 were categorized as follows:

#### Codebase maintenance

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

#### Developer Experience

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

#### Feature Completion

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

#### Fuzzer

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

- **Cover more Solidity features:** At the end of `2026Q3`, Testing with `Sorobench` against `solc`
  semantic tests produced a `pass` result on `25.7%` of the tests. The proposed impact is raising
  `pass` to reach `50%` in `2026Q4`. The ultimate goal is full Solidity support on Soroban, except
  where a Solidity feature is impossible in Soroban; According to this
  [report](https://github.com/Islam-Imad/sorobench/blob/main/report/summary.md), the ultimate support
  count is `~90%`.

- **Address the wider open-source ecosystem:** Most of Solang's development has been discussed and
  carried out internally. We propose a more open discussion and planning, thus engaging more
  open-source contributors. This way, we utilize Solang's popularity, to: Get more contributions, and
  further increase Solang's popularity Have a bigger developer base that have either contributed to
  or used the compiler

- **Expand the existing Solang developer community in Egypt and Arabic speaking countries** Put the
  newer releases, the Playground, and the language server in front of users and collect feedback on
  the compiler and its tooling to prioritize the next round of work.

- **Complete the LFDT mentorship.** Finish the ongoing
  [mentorship](https://github.com/LF-Decentralized-Trust-Mentorships/mentorship-program/issues/74),
  growing an open-source contributor with deep Solang and Soroban knowledge.

- **Make Stellar easier to onboard via Solang.** Lower the barrier for Solidity/EVM developers to
  build on Stellar.

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

### 1. Reach 45-50% Solidity coverage

Solang's Soroban support is measured on every commit: the
[Sorobench](https://github.com/Islam-Imad/sorobench) CI job runs the 1,503 `solc` v0.8.22 semantic
tests on Solang for Soroban, and compares with the EVM result. **386 of the 1,235 applicable tests
pass (31.3%)**. **382** of the failures can be fixed by implementing the following Solidity features:

- **[Returning multiple values](https://docs.soliditylang.org/en/v0.8.22/contracts.html#returning-multiple-values)**
  from public functions, encoded as a Soroban `Vec` the way Rust contracts return tuples.
- **[Small integer types](https://docs.soliditylang.org/en/v0.8.22/types.html#integers)** (`uint8`,
  `int16`, …) computed at their declared width, so overflow checks, casts and sign extension behave
  as in Solidity. Currently, 38 tests return fail because of this.
- **[User-defined value types](https://docs.soliditylang.org/en/v0.8.22/types.html#user-defined-value-types)**
  and **[contract types](https://docs.soliditylang.org/en/v0.8.22/types.html#contract-types)** passed
  across the contract boundary, which currently crash the Soroban encoder (42 tests).
- **[Function modifiers](https://docs.soliditylang.org/en/v0.8.22/contracts.html#function-modifiers)**,
  which crash Soroban's function dispatch (19 tests).
- **[External calls returning `bytes`, `string` and dynamic arrays](https://docs.soliditylang.org/en/v0.8.22/control-structures.html#external-function-calls)**,
  which crash codegen (25 tests).
- **Correctness bugs** in [enum](https://docs.soliditylang.org/en/v0.8.22/types.html#enums) and
  [`bool`](https://docs.soliditylang.org/en/v0.8.22/types.html#booleans) range checks and
  [shifts](https://docs.soliditylang.org/en/v0.8.22/types.html#shifts) by the full bit width (14
  tests).

**SMART alignment:** specific and measurable — raise the Sorobench pass rate from 386 to **≥ 618 of
1,235 applicable tests (31.3% → 45-50%)**, as reported by the Sorobench CI run on Solang `main` at a
pinned Sorobench commit, so changes to the tool cannot move the number; achievable, as the failures
behind this target trace to six root causes, each already pinned to a location in the compiler;
relevant, because every test that passes is a Solidity feature that behaves on Stellar as it does on
Ethereum, which is what lets EVM developers port contracts with confidence; and time-bound to the
quarter.

### 2. Support Soroban custom `Account` Examples

Solang supports 20 of the 25 language-feature examples in
[stellar/soroban-examples](https://github.com/stellar/soroban-examples) (80%), tracked in
[#1901](https://github.com/hyperledger-solang/solang/issues/1901). The remaining 5 are custom account
contracts: `simple_account`, `multisig_1_of_n_account`, `bls_signature`, `account` and
`modular_account`.

A custom account is a contract with a `__check_auth` function. When a contract calls `requireAuth()`
on the account's address, the Soroban host calls `__check_auth` with the signed payload, the
account's signature and `Vec<Context>`, the list of calls being authorized. `Context` is a Rust enum
whose variants carry data, while Solidity enums only support integers. The examples also use
signature-verification builtins and contract error codes that Solang currently doesn't support.

We aim to support:

1. **`ed25519_verify(bytes32 key, bytes32 message, bytes signature)`**, using the host function
   `verify_sig_ed25519`.
2. **`bls12_381_hash_to_g2(bytes message, bytes dst)`**, using the existing host function.
3. **A `Context` struct provided by Solang** for the `__check_auth` parameter. It says which kind of
   call is being authorized, which contract and function are called, and holds the call's arguments
   as `bytes`, read with `abi.decode`. Contracts that do not read it pay nothing for it. We will
   agree the exact design with the maintainers in a public issue before building it.
4. **Contract error codes from Solidity custom errors**: `revert UnknownSigner()` returns
   `Error(Contract, 1)`, as the Rust examples do, instead of aborting the call.

**SMART alignment:** specific and measurable — merge `simple_account`, `multisig_1_of_n_account`,
`bls_signature` and `account` as Solidity examples with tests that run through the host's
authorization flow, raising coverage from 20 of 25 (80%) to 25 of 25 (100%).

### 3. Grow developer reach and run another feedback round

Produce Solidity-on-Stellar developer content — blog posts, video walkthroughs, and a live workshops
then collect and triage feedback. This lowers the onboarding barrier for Solidity/EVM developers to
Stellar, grows adoption, and creates a prioritized feedback loop that steers future work.

**SMART alignment:** specific and measurable — publish ≥ 2 blog posts and ≥ 1 video, run ≥ 1
workshop/live session; achievable given our ~40 monthly active users and prior launch reach; relevant
to adoption and onboarding; and time-bound to the next three months.

### 4. Make Solang development process more open

Currently, most of the work and design decisions in Solang are made internally by ABS GmbH. We intend
to make the development process more open, that is to attract more contributions from the open-source
ecosystem. This achieves two goals: 1- Attract more developers wanting to contribute to open-source,
giving them an intro to the Stellar ecosystem. 2- Solang gains more popularity.

**SMART alignment:** specific and measurable — a public design issue for each new language feature in
this proposal before it is built, and ~10 `good first issue` issues; achievable, as the tracker and
Sorobench reports are already public; relevant, as it brings in new contributors and community
review; and time-bound to the quarter.

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Asolidity_contracts_on_soroban)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
