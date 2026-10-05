---
title: "Soroban-ret"
parent: Public Good Projects
proposal_issue: 175
proposer: SurfingBowser
category: "Security & Auditing Tools"
budget: "$20,000"
---

# Soroban-ret

<!-- markdownlint-disable MD036 -->

_Compile Rust to WebAssembly, disassemble Soroban contracts, and inspect on-chain bytecode._
<!-- markdownlint-enable MD036 -->

|                      |                                                                                                     |
| -------------------- | --------------------------------------------------------------------------------------------------- |
| **Category**         | Security & Auditing Tools                                                                           |
| **Website**          | <https://stellarsecurityportal.com/dev-tools>                                                       |
| **Repository**       | <https://github.com/Inferara/soroban-ret>                                                           |
| **First Released**   | July 2026                                                                                           |
| **Intake**           | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/150> |
| **Budget Requested** | $20,000                                                                                             |

## Project Description

<!-- markdownlint-disable MD034 -->

The Soroban Disassembler is an open-source specialized decompilation tool that can receive the WASM
file of a Soroban smart contract and output easily readable WAT and relevant Rust code. It was built
to create a higher level of accuracy than previous WASM to WAT conversion tools.

The project was started through an RFP during
[SCF round #41](https://communityfund.stellar.org/dashboard/submissions/recNoycw142XsaEvq). We passed
the final tranche review on July 17th, 2026 and have been actively maintaining and improving it
since. The tools are available through both crate.io
[![soroban-ret on crates.io](https://img.shields.io/crates/v/soroban-ret.svg?label=soroban-ret)](https://crates.io/crates/soroban-ret)
[![soroban-ret-cli on crates.io](https://img.shields.io/crates/v/soroban-ret-cli.svg?label=soroban-ret-cli)](https://crates.io/crates/soroban-ret-cli)
as well as in browser through the Stellar Security Portal
[Dev-tools page](https://stellarsecurityportal.com/dev-tools).
<!-- markdownlint-enable MD034 -->

## Team & Experience

<!-- markdownlint-disable MD034 -->

Our Team members are Georgii, Dominik and Andrey from Inferara. Georgii and Dominik are both Pilots
and have acted as SCF delegates on the Open & RFP tracks. Andrey has been actively maintaining and
contributing to the Stellar Security Portal. As a team we have built and maintain the SCF projects
[Stellar Security Portal](https://stellarsecurityportal.com/) and the
[Inference Programming Language](https://github.com/Inferara/inference). We also actively advise and
inform companies locally and abroad about the Stellar ecosystem and its initiatives.

Individual team member details: Georgii - [linkedin](https://www.linkedin.com/in/0xgeorgii/),
[Github](https://github.com/0xGeorgii), discord: .spaceinvader Dominik -
[Github](https://github.com/SurfingBowser), discord: andykaufman Andrey -
[Github](https://github.com/AKercha1), discord: andreykerchin
<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->

General Impact Overview Over the last 3 months we have focused on maintaining the project while also
looking for opportunities for other teams to integrate the tool into their own projects. We have seen
a total of 880 downloads across 4 versions of the tool (including the cli) so far according to our
[crates.io](https://crates.io/crates/soroban-ret) page. As these are anonymized reports we can't be
sure of all our users, however we have worked with the rumblefish team directly to integrate it with
their [Soroscan.io](https://soroscan.io/) block explorer tool.

Additionally it was used by a community pilot Tupui to build a python to WASM sdk (comment
[here](https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/150#issuecomment-5886527294)).

These are just 2 examples where the tool is useful on different levels. For those curious about WASM
dissasembly it is available on the Security Portal and Soroscan, and for serious developers they can
use it to fit their specific project goals.

The following section is about the technical changes that occured which can be measured directly.

#### Technical Overview

_(this section of techincal overview was written with AI assistance but was reviewed & edited
manually)_

1. Release v0.0.4 — the correctness-first release

The headline of this period is the release of
**[v0.0.4](https://github.com/Inferara/soroban-ret/releases/tag/v0.0.4)** (July 26, 2026) with many
improvements made such as:

- **Hard errors across the 24-contract mainnet test corpus: 1,042 → 326, a 68% reduction.**
  Decompiled contracts that previously failed to recompile now produce valid Rust far more often.
- **Behavioral match rate: 99.2% on the tool's verification suite.** The project maintains an
  automated check that decompiles each contract in its test set (39 example fixtures plus the
  24-contract mainnet corpus), recompiles the result, and runs original and rebuilt contract side by
  side on hundreds of generated inputs (479 cases across 68 functions).
- **Three real-world contracts decompile to cleanly compiling Rust** (digicus, fxdao-oracle,
  unknown-oracle), up from zero.
- **First contract recovered completely, with no gaps:** the `num_list` function in `test_alloc` now
  decompiles perfectly and behaves identically to the original on every tested input.

2. What was improved

#### Guessing eliminated in favor of honesty

- Unknown map/vector contents are no longer replaces with empty collections; they are shown as
  explicit gaps ([#36](https://github.com/Inferara/soroban-ret/issues/36),
  [#39](https://github.com/Inferara/soroban-ret/pull/39)).
- Storage keys built inside loops are now correctly recovered as their real names instead of
  placeholder guesses ([#61](https://github.com/Inferara/soroban-ret/issues/61),
  [#62](https://github.com/Inferara/soroban-ret/pull/62)).
- One contract function that had collapsed to a bare crash now shows its real storage logic again
  ([#33](https://github.com/Inferara/soroban-ret/pull/33)).
- Edge cases where recompiled code could crash on inputs the original handled fine (arithmetic
  overflow behavior) were fixed ([#64](https://github.com/Inferara/soroban-ret/pull/64)).

#### Much smarter storage recovery

Contracts store their data under typed keys, and recovering how that data is read and written is the
heart of good decompilation. This period added:

- Recognition of the common "read with default" and "read or fail with a clear error" storage
  patterns, including structs with multiple fields and TTL handling
  ([#41](https://github.com/Inferara/soroban-ret/pull/41)–[#47](https://github.com/Inferara/soroban-ret/pull/47)).
- Recovery of keyed storage entries (e.g. `Positions(user)`, `ResConfig(asset)`) by safely
  re-executing the key-construction logic at analysis time, replacing incorrect keyless guesses
  ([#50](https://github.com/Inferara/soroban-ret/pull/50),
  [#51](https://github.com/Inferara/soroban-ret/pull/51)).

#### Loop reconstruction

Loops were previously one of the weakest areas of the output. With changes in
([#57](https://github.com/Inferara/soroban-ret/pull/57)–[#64](https://github.com/Inferara/soroban-ret/pull/64))
now reconstructs loops that build up vectors element by element into natural, idiomatic Rust
(`let mut vec = Vec::new(&env); … vec.push_back(x)`), and correctly evaluates loops that compute
constant values. This is what made the first complete, gap-free contract recovery possible.

#### Tooling and documentation

Per-contract recovery quality is now measured and reported, and the README and pattern-coverage
documentation were re-measured against the actual state of the tool so the docs reflect reality
([#70](https://github.com/Inferara/soroban-ret/pull/70)).

3. Retroactive assessment

The work in the last 3 months goes well beyond what was needed to pass the final tranche review. It
made the tool meaningfully more useful. Decompiled output is now far more likely to compile as valid
Rust, and where the tool cannot yet fully understand a contract, it says so loudly and explicitly
instead of guessing. With these changes and improvements the tool is now more dependant for anyone
auditing, studying, or migrating a Soroban contract since every uncertainty is clearly flagged.
<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

N/A
<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

Continued maintenance as Soroban/protocol versions change, keeping disassembly accuracy ahead of
generic WASM to WAT tools, and growing usage through ecosystem partnerships similar to the Soroscan
collaboration. As suggested we will look into integrations of Stellar Labs and Stellar Expert. It
could also be used as an education tool to enhance understanding for developer. Our team member
Dominik will explore relevant projects within Stellar to integrate and use the tool.
<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

Building on the retroactive technical overview above, the Q4 deliverables focus on working down the
measurable backlog the verification suite has already mapped, keeping the tool current with the
Soroban toolchain, and broadening the contract coverage it is tested against.

#### 1. Backlog burn-down: hard errors and behavioral divergences

The verification suite currently reports **326 hard errors** across the 24-contract mainnet corpus
and **4 behavioral divergences** (all in `digicus`), each itemized with reproducing inputs.

**Deliverable:** reduce the hard-error count and close the remaining behavioral divergences by the
end of Q4 2026, verified against the project's own automated suite (decompile, recompile, run side by
side on generated inputs). Progress is reproducible and publicly visible in the repo's benchmark data
and changelog.

**Ecosystem value:** every hard error removed means a real deployed contract decompiles to valid,
recompilable Rust instead of failing; every divergence closed means one fewer case where auditors or
developers must fall back to manual bytecode reading. This directly raises the floor of what anyone
can inspect on-chain.

#### 2. Ongoing maintenance: soroban-rs compatibility

The tool is currently pinned to `soroban-spec`/`soroban-meta` **26.0.0-rc.1**. As the Soroban SDK and
protocol evolve, decompilation accuracy degrades unless the tool tracks upstream changes.

**Deliverable:** track new soroban-rs / protocol releases through Q4 2026 and into Q1 2027, and cut
compatible releases of `soroban-ret` and `soroban-ret-cli` on crates.io within a reasonable window of
each upstream release.

**Ecosystem value:** downstream integrations (Soroscan, the Stellar Security Portal dev-tools page
and future collaborations) and CLI users depend on the tool understanding contracts built with
current SDK versions. Keeping pace with soroban-rs keeps the whole inspection pipeline usable as the
network upgrades.

#### Bonus goals

Additional partnerships or usage of the tool through collaboration initiatives.
<!-- markdownlint-enable MD034 -->

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
