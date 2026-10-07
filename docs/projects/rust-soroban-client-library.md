---
title: "Rust Soroban Client Library"
parent: Public Good Projects
proposal_issue: 189
proposer: rahul-soshte
category: "SDKs"
budget: "$15,000"
---
# Rust Soroban Client Library

<!-- markdownlint-disable MD036 -->
_A Rust SDK for building, signing and submitting Stellar transactions and calling Soroban smart contracts through Soroban RPC, covering every classic operation and kept current with each protocol upgrade._
<!-- markdownlint-enable MD036 -->
| | |
| --- | --- |
| **Category** | SDKs |
| **Website** | <https://docs.rs/soroban-client/latest/soroban_client/> |
| **Repository** | <https://github.com/rahul-soshte/rs-soroban-client> |
| **First Released** | November 2024 |
| **Intake** | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/141> |
| **Budget Requested** | $15,000 |
| **Maintenance Reserve** | 4000 |
| **Other** | 11000 |

## Project Description

<!-- markdownlint-disable MD034 -->
Rust Soroban Client is an open-source Rust SDK for Stellar and Soroban, similar to the JS stellar-sdk. It has two crates. stellar-baselib provides keypairs, accounts and all classic operations, and builds, hashes and signs transactions; it is published from https://github.com/rahul-soshte/rs-stellar-base. soroban-client is a high-level Soroban RPC client: it simulates, prepares, submits and polls transactions, and it reads contract data, events and ledger entries. It is used by bot authors, backend services, wallets, indexers and cross-chain bridges that need to work with Stellar without switching to JavaScript or hand-writing XDR.
<!-- markdownlint-enable MD034 -->

## Team & Experience

<!-- markdownlint-disable MD034 -->
Rahul Soshte created and maintains both crates, with around 145 commits since June 2023. He has
shipped every protocol upgrade this SDK has been through: Protocol 27, the CAP-71 upgraded-auth
simulation flag, Protocol 28 and the CAP-85 external-reference contract operations. He publishes
both crates to crates.io.

GitHub: https://github.com/rahul-soshte 
Discord: hunter0382 
LinkedIn: https://www.linkedin.com/in/rahul-s-138133ba/
<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->
In Q3 2026 the two crates shipped two releases each, and both went to keeping up with the protocol
rather than to new API surface. 0.5.9, on 2026-08-26, added the `useUpgradedAuth` simulation flag for
CAP-71 v2 auth credentials, ahead of the protocol that uses it. 0.6.0, on 2026-09-05, added Protocol
28 support including the CAP-85 external-reference contract operations, and was verified end to end
against testnet before release. Protocol 28 activated on mainnet on 2026-09-16, so the release landed
eleven days ahead of activation. The SDK has never missed a protocol activation.

Being straight about the rest of the quarter: protocol work took priority and no new features
shipped.

Stellar's official documentation lists `soroban-client` as the Rust client SDK:
https://developers.stellar.org/docs/tools/sdks/client-sdks#rust

Known downstream projects include Laina's liquidation bot, Templar
Protocol, HOT DAO's validation SDK, Credence, stellar-ibc-eureka, and Soneso's
`stellar-agent-wallet`, which pins `stellar-baselib` 0.6.0. On crates.io, `soroban-client` is past
74,000 downloads and `stellar-baselib` past 86,000 as of 2026-10-06. It is still the only maintained
Rust client SDK for Soroban.
<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->
N/A — this is a first Public Goods Award proposal.
<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->
The direction for this SDK is full SEP support. For the next three months that means making a start
on it.

The SDK is good at the protocol level and has nothing at the standards layer. It follows every protocol
upgrade, it has all 26 classic operations, the whole Soroban operation set and all 12 RPC methods,
but it implements almost no SEPs.

The biggest gap is contract interfaces. Every Soroban contract ships its own interface inside its
wasm, so a caller can look up what a function takes and returns and then pass normal values. This
SDK cannot read that, so a developer builds `ScVal` by hand for every argument and pulls apart raw
XDR for every return value. That is the single roughest part of using this SDK today, and it is
where most of this quarter goes.

Four smaller standards come next, picked because each one removes a real
problem: SEP-29 so a payment to an exchange that requires a memo cannot silently go missing, SEP-1 so
services on the network can be discovered, SEP-23 so strkey support is finally complete, and SEP-53
so someone can prove they hold an account by signing a line of text, with no transaction and no fee. Alongside them, fee-bump transactions, which the SDK cannot do at all today.

Everything implemented goes out as a crates.io release with its tests, so each claim below can be checked against a published version and a passing test.
<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->
Three deliverables, in the order they will be taken, and the maintenance that runs alongside them.

#### Deliverable 1 — SEP-46, SEP-47, SEP-48: contract interfaces and a typed contract client
The point of this one is simple: let someone call a Soroban contract from Rust by naming the
function and passing ordinary values, and get an ordinary value back.

Three standards make that possible, and all three describe data a contract already carries inside
its own wasm, in sections the runtime ignores. SEP-48 is the contract's interface: a
`contractspecv0` section holding, for every exported function, its name, its argument names and
types, its return type and its doc comment, plus definitions for any structs, unions, enums, error
enums and events it uses. SEP-46 is the contract's metadata: a `contractmetav0` section of key and
value strings, which is where the SDK and compiler versions a contract was built with live. SEP-47
is one agreed key inside that metadata — `sep`, holding a comma-separated list of the SEPs a
contract claims to implement, so a caller can ask whether a contract is a SEP-41 token without
probing its functions.

The specification handling is not being written from scratch. Stellar already publishes it as
libraries. `soroban-spec` pulls the `contractspecv0` and `contractmetav0` sections out of contract
wasm and parses them, and `soroban-spec-tools` converts between contract values and JSON both ways,
covering user-defined structs, unions and enums and 128- and 256-bit integers. Both track the
protocol and both are already used by the Stellar CLI, so depending on them beats reimplementing
them and drifting. The work here is the layer around them: look up a contract's interface over RPC
from its contract id, convert the arguments going in, build and simulate the invocation through the
path that already exists, convert the result coming back, and turn a contract error into a typed
`Result` instead of a string. The dependency goes behind a feature flag so the core crate can still
release on its own schedule.

- **Specific:** `Server::get_contract_spec` and a matching reader for a contract's metadata and its
  declared SEP claims, a `Client` built from a contract id, argument and return conversion driven by
  the contract's own interface, typed contract errors, and the specification dependency behind a
  feature flag.
- **Measurable:** a testnet test that deploys a contract, calls it with native Rust arguments and
  checks a native return value, without the test building a single `ScVal`; round-trip tests for
  user-defined structs, unions, enums and 128- and 256-bit integers; a contract error coming back as
  a typed variant instead of a string; a contract's metadata and its declared SEP claims read back
  from a deployed contract; the core crate still compiling with the feature turned off.
- **Achievable:** the parsing, conversion and big-integer handling exist in the libraries above, and
  `get_contract_wasm_by_contract_id`, `Operation::invoke_contract`, `prepare_transaction` and
  simulation parsing already exist in these crates. What is left is the client layer and the API
  boundary around it.
- **Relevant:** calling a contract is the most common thing anyone does with this SDK, and right now
  it is the roughest part of it.
- **Time-bound:** released on crates.io inside the quarter.
- **Proof:** the merged pull requests, the crates.io release that adds SEP-46, SEP-47 and SEP-48, the
  testnet test, and a worked example under `examples/`.

#### Deliverable 2 — SEP-1, SEP-23, SEP-29, SEP-53: the smaller standards
Four standards that are small individually and add up to a noticeable difference, taken in this
order.

SEP-29 checks whether a destination account requires a memo before paying it, wired into the submit
path by default — that is the mistake that loses people's deposits to exchanges. SEP-1 fetches a
domain's `stellar.toml`, enforces the size limit and parses it into Rust, which is how every service
on the network is discovered and the prerequisite for the authentication standards later. SEP-23
finishes strkey support: liquidity pool and claimable balance addresses are missing today, because
the crate pins an old version of the strkey dependency and represents a pool id as a plain string and
a claimable balance id as hex. SEP-53 signs and verifies plain messages under the standard prefix, so
a service can check that someone controls an account without putting a transaction on the network.

- **Specific:** SEP-29 memo-required checking in the submit path, SEP-1 fetching and parsing,
  liquidity pool and claimable balance strkeys exposed as proper types with validation, and SEP-53
  message signing and verification.
- **Measurable:** SEP-29 refusing a payment to a memo-required account and allowing one to a muxed
  destination; SEP-1 parsing every documented field group, tested against three real anchor
  `stellar.toml` files and against one that exceeds the size limit; `L` and `B` strkeys round-tripped
  against known values with bad checksums rejected; SEP-53 checked against the test cases in its
  specification.
- **Achievable:** all four are small and specification-exact rather than design-heavy. SEP-53
  publishes test cases in its specification, the strkey work is a dependency bump plus wiring since
  the underlying crate already supports both types, and SEP-29 and SEP-1 are checkable against a
  live testnet account and real anchor files.
- **Relevant:** SEP-29 prevents lost funds, SEP-1 is what every other discovery and anchor standard
  builds on, complete strkey support is something users expect to be there, and SEP-53 is
  what an airdrop form or a bot handing out roles needs to check that someone holds an account,
  without asking them to send a transaction.
- **Time-bound:** released on crates.io inside the quarter, in the order listed.
- **Proof:** the merged pull requests, the crates.io release for each item, and its tests.

#### Deliverable 3 — Fee-bump transactions
Fee bumps do not work at all today. `to_envelope` refuses a fee-bump transaction and
`from_xdr_envelope` panics if handed one, so nobody using this SDK can raise the fee on a transaction
that is stuck, and nobody can read a fee-bump envelope someone else sends them. Anything that has to
get a transaction confirmed under fee pressure — a liquidation bot, a payment processor, anything
working to a deadline — has no way to do it here.

This deliverable adds fee-bump construction with an explicit fee source, signing, submission and
envelope parsing in both directions, with the network's minimum-fee rule for fee bumps checked at
construction time instead of being discovered when the network rejects the transaction.

- **Specific:** building, signing, submitting and parsing fee-bump transactions, including the inner
  transaction hash and the fee-bump minimum-fee check, and removing the panic from envelope parsing.
- **Measurable:** a fee bump built, signed, submitted and confirmed on testnet over an inner
  transaction from a different source account; a fee-bump envelope read back from base64 XDR with its
  inner transaction recovered; a fee below the protocol minimum refused at construction with a typed
  error rather than a panic or a network rejection; and `from_xdr_envelope` no longer panicking on any
  valid envelope type, with a test per envelope variant.
- **Achievable:** the XDR types are already in `stellar-xdr` and the signing machinery is in place.
  The work is a new transaction type rather than plumbing, because a fee bump holds a fee source and
  an inner envelope instead of a source, sequence and operations, and its fee is an `i64` where the
  current field is a `u32`. It needs its own signature payload tagged `TxFeeBump`, and the submit path
  has to accept either kind. That can be done additively, so existing callers keep compiling, but the
  new type lives in the base crate, so the two releases have to go out in order.
- **Relevant:** it unblocks every service that needs a transaction to land under fee pressure, and it
  removes a panic from a public parsing function that any caller can hit with input from the network.
- **Time-bound:** released on crates.io inside the quarter.
- **Proof:** the merged pull requests, the crates.io release that adds fee-bump support, and the
  testnet and parsing tests.

#### Ongoing maintenance
Alongside the deliverables, part of the quarter goes to work that cannot be listed in advance:
protocol releases and support across both repositories, dependency and security updates, and
cutting releases. Every protocol release gets supported before it activates on mainnet, verified
against testnet first, as it was for Protocol 28.
<!-- markdownlint-enable MD034 -->

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.

