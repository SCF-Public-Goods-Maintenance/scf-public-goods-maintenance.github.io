---
title: "Stellar .NET SDK"
parent: Public Good Projects
proposal_issue: 48
proposer: jopmiddelkamp
category: "SDKs"
budget: "$15,000"
---

# Stellar .NET SDK

<!-- markdownlint-disable MD036 -->

_.NET Stellar SDK that supports API backends with Horizon and Soroban._

<!-- markdownlint-enable MD036 -->

|                      |                                                  |
| -------------------- | ------------------------------------------------ |
| **Category**         | SDKs                                             |
| **Website**          | <https://beans-bv.github.io/dotnet-stellar-sdk/> |
| **Repository**       | <https://github.com/Beans-BV/dotnet-stellar-sdk> |
| **First Released**   | April 2018                                       |
| **Intake**           | soft-launch                                      |
| **Budget Requested** | $15,000                                          |

## Project Description

<!-- markdownlint-disable MD034 -->

The .NET Stellar SDK (`stellar-dotnet-sdk`) is the official community-maintained SDK for building on
Stellar using C# and .NET. Originally ported from the official Java SDK and expanded by Beans BV, it
serves .NET developers building backends, APIs, anchors, and Soroban-enabled applications on Stellar.

The SDK is published as two NuGet packages (`stellar-dotnet-sdk` and `stellar-dotnet-sdk-xdr`) and is
used by .NET developers building production Stellar integrations. XDR types are auto-generated from
the official Stellar XDR definitions via `xdrgen`, ensuring protocol fidelity.

**Ecosystem relevance:**

.NET is the one of the most popular programming language ecosystem globally and the primary backend
technology for enterprises in financial services, government, and healthcare. The Stellar .NET SDK
enables these developers to integrate with Stellar without maintaining forks or custom
implementations.

<!-- markdownlint-enable MD034 -->

## Team & Experience

<!-- markdownlint-disable MD034 -->

**Cuong Pham** — Software Engineer, primary maintainer

- GitHub: [@cuongph87](https://github.com/cuongph87)
- Discord: cleft931
- Primary developer responsible for core development, feature implementation, and testing
- Has extensive experience building on Stellar, with contributions spanning the full protocol surface
  (Horizon, Soroban RPC, SEPs)
- Delivered the Json.NET → System.Text.Json migration, all 5 SEP implementations, response model
  overhaul, and retry mechanism in recent quarters

**Jop Middelkamp** — Maintainer and reviewer

- GitHub: [@jopmiddelkamp](https://github.com/jopmiddelkamp)
- Discord: qbarz
- Oversees roadmap planning, aligns development with ecosystem needs, and manages the grant
  relationship with SCF
- Co-Founder of Beans BV, which has maintained the .NET Stellar SDK since 2024 after taking over
  stewardship from the original creator (Elucidsoft)
- Previous SCF participation: Infrastructure Grant (completed), Public Goods Award Q1 2026

**Michael Pham** — Software Engineer, maintainer

- GitHub: [@michaelpham-rgb](https://github.com/michaelpham-rgb)
- Developer responsible for core development, feature implementation, and testing
- Has some experience building on Stellar trough it's development on the Beans App

The team collaborates with other Stellar ecosystem developers and maintains active communication
through GitHub issues and Stellar developer channels. Contributions are reviewed and merged regularly
to keep the SDK aligned with the latest network standards.

<!-- markdownlint-enable MD034 -->

## Retroactive Impact

<!-- markdownlint-disable MD034 -->

Over the next three months, our goal is to transform the .NET Stellar SDK from a backend-only library
into a reliable, multi-platform foundation — while keeping .NET backend developers as the primary
audience.

**1. Protocol 26 readiness — protecting production integrators** Protocol 26 "Yardstick" hits Testnet
on April 16 and Mainnet on May 6. The SDK must support the new XDR types, result codes, and RPC
changes before these dates. Failure to update would break existing .NET integrations and block new
ones. This is the most time-sensitive deliverable.

**2. Integration tests — shifting from "it compiles" to "it works"** The SDK currently has 186 unit
test files, but they all run against mocked JSON responses. If Horizon or Stellar RPC change field
names, add headers, or subtly change behavior, our tests still pass green while production users
break. An integration test suite running against Testnet on every release is the single highest-ROI
investment for SDK reliability.

**3. Multi-platform preparation — unlocking MAUI, Unity, and Tizen** The SDK currently targets .NET 8
only and hasn't adopted any runtime improvements since .NET 6. This quarter we lay the foundation for
multi-platform expansion (the main focus of Q3) by:

- **Multi-targeting to `net10.0 + net8.0 + netstandard2.1`**, which lays the technical foundation for
  .NET MAUI (iOS/Android), Unity 2022.3+ (games/XR), and Tizen 5.5+ (Samsung smart TVs/wearables)
  support planned in Q3/Q4
- **Upgrading the codebase to use modern .NET 7–10 APIs** where they improve reliability,
  performance, or multi-platform compatibility — including `FrozenDictionary` for faster static
  lookups, `Stream.ReadExactly()` for safer XDR binary decoding, strict JSON validation with
  `AllowDuplicateProperties`, and `RespectNullableAnnotations` for stronger response model validation
- **Gaining free JIT performance wins** from targeting net10.0: stack allocation for small arrays,
  array interface devirtualization, delegate escape analysis, and improved PGO — all without code
  changes

This makes the .NET Stellar SDK the most broadly deployable Stellar SDK in the ecosystem and sets up
Q3's full MAUI validation and Wallet SDK development.

**4. SEP-45 — closing the most visible feature gap** Every peer SDK (Flutter, iOS, Java) has
implemented SEP-45 (Stellar Web Authentication with Contract Accounts). We are the only SDK without
it. Shipping SEP-45 plus per-SEP compatibility matrices closes this gap and provides field-level
coverage transparency for all implemented SEPs.

<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

### 0. One-command full verification

Every claim below is reproducible in ~1 minute (excluding the live-network integration suite):

```bash
git clone https://github.com/Beans-BV/dotnet-stellar-sdk.git
cd dotnet-stellar-sdk

# Deliverable 5 — Unit test suite (expect 1927 passed, 0 failed; net8.0 shown,
# the suite also runs on net10.0 since #195 merged)
dotnet test StellarDotnetSdk.Tests/StellarDotnetSdk.Tests.csproj -c Release -f net8.0 --nologo 2>&1 | tail -3

# Deliverable 2 — Integration test suite (52 test methods; runs against live Testnet in CI)
grep -rE '^\s*\[Test\]' --include='*.cs' StellarDotnetSdk.IntegrationTests | wc -l

# Deliverable 4 — SEP-45 unit tests (expect 82 passed) + 6 SEP matrices at 100%
dotnet test StellarDotnetSdk.Tests --filter "FullyQualifiedName~Sep0045" --nologo 2>&1 | tail -3
grep -h "Total Coverage" StellarDotnetSdk/Compatibility/sep/*.md

# XML doc gate carried over from Q1 (expect 0 CS1591)
dotnet build StellarDotnetSdk/StellarDotnetSdk.csproj -c Release --nologo 2>&1 | grep -c "CS1591"
```

Expected output verbatim:

```
Passed!  - Failed:     0, Passed:  1927, Skipped:     1, Total:  1928   # unit suite (net8.0)
52                                                                      # integration [Test] methods
Passed!  - Failed:     0, Passed:    82, Skipped:     0, Total:    82   # SEP-45 tests
**Total Coverage:** 100.0%  (× 6 — SEP-1, 6, 9, 10, 24, 45)
0                                                                       # CS1591 count
```

The one skipped unit test is `AuthorizeEntry_AgainstP27Testnet_SubmitsSuccessfully` (network-gated by
design).

---

### 1. Deliverable-by-deliverable evidence

#### Deliverable 1 — Protocol 26 "Yardstick" Support

**Closing issue:**
[#155 — SDK Updates for Protocol 26 Compatibility](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/155)
(closed 2026-06-07, together with the 15.1.0 stable release).

**Delivery PRs:**

| PR                                                                                                                              | Commit                                                                       | Magnitude                       |
| ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------- |
| [#169](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/169) migrate XDR generator from xdrgen                               | [`67ca1e48`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/67ca1e48) | 82 files, +8,305 / −34          |
| [#170](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/170) regenerate XDR classes with the new generator                   | [`80761a3e`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/80761a3e) | **478 files, +17,043 / −3,176** |
| [#176](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/176) bump stellar-xdr to v26                                         | [`945633a2`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/945633a2) | 29 files, +559 / −56            |
| [#177](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/177) SDK types for v26 frozen ledger keys + trustline-frozen results | [`80ae353c`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/80ae353c) | 43 files, +1,109 / −59          |

**Plan scorecard** (every Protocol 26 item from the submission, verified in code at `f065324f`):

| Planned item                                   | Status               | Where                                                                                                                                                                                                                                                            |
| ---------------------------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5 new frozen-ledger-key XDR types (CAP-77)     | ✅ 5/5               | `EncodedLedgerKey`, `FreezeBypassTxs`, `FreezeBypassTxsDelta`, `FrozenLedgerKeys`, `FrozenLedgerKeysDelta` (all in `StellarDotnetSdk.Xdr/`, added by #176)                                                                                                       |
| 4 new ConfigSettingID values                   | ✅ 4/4               | `ConfigSettingID.cs` — values 17–20 (`CONFIG_SETTING_FROZEN_LEDGER_KEYS` … `FREEZE_BYPASS_TXS_DELTA`)                                                                                                                                                            |
| 16 new BN254 ContractCostType entries (CAP-80) | ✅ 16/16             | `ContractCostType.cs` — `Bn254EncodeFp`=70 … `Bn254G1Msm`=85                                                                                                                                                                                                     |
| 4 new result codes                             | ✅ 4/4               | `txFROZEN_KEY_ACCESSED`, `CLAIM_CLAIMABLE_BALANCE_TRUSTLINE_FROZEN`, `LIQUIDITY_POOL_DEPOSIT_TRUSTLINE_FROZEN`, `LIQUIDITY_POOL_WITHDRAW_TRUSTLINE_FROZEN` (XDR enums + SDK result wrappers + tests)                                                             |
| 7 contract-spec unbounded-array changes        | ✅ 7/7               | `SCSpecEventV0`, `SCSpecFunctionV0`, `SCSpecUDTEnumV0`, `SCSpecUDTErrorEnumV0`, `SCSpecUDTStructV0`, `SCSpecUDTUnionCaseTupleV0`, `SCSpecUDTUnionV0` (all touched by #176)                                                                                       |
| Matrices updated to v26                        | ✅ Done (2026-07-02) | `horizon_matrix.md` pins Horizon v27.0.0, `rpc_matrix.md` pins RPC v26.0.1 — verified against upstream release notes: no new endpoints or RPC methods in either version (Horizon v26/v27 changes are result codes + effects the SDK already ships via #177/#179) |
| `getLatestLedger` v26 response fields          | ✅ Done (2026-07-02) | `CloseTime` / `HeaderXdr` / `MetadataXdr` added to `GetLatestLedgerResponse` (6/6 response fields, verified against the `stellar-rpc` v26.0.1 handler source) with unit tests                                                                                    |

**Timeline vs plan:** 15.1.0-beta with full Protocol 26 support shipped **2026-04-22** — six days
after the Testnet upgrade (Apr 16) and two weeks **before** the Mainnet vote (May 6). No .NET
integrator broke on the Mainnet upgrade. Stable
[15.1.0](https://github.com/Beans-BV/dotnet-stellar-sdk/releases/tag/15.1.0) (2026-06-07) contains
exactly #169, #170, #176, #177 (verified via release notes).

**Bonus — Protocol 27 "Zipper" (CAP-71), pulled forward from Q3/Q4:**
[PR #187](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/187) (merged **2026-06-18, the day of
the Protocol 27 Testnet upgrade**; commit
[`deb388b7`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/deb388b7), 18 files, +3,277 /
−165) delivers `SorobanAddressCredentialsV2`, delegated credentials
(`SOROBAN_CREDENTIALS_ADDRESS_WITH_DELEGATES`), and signing helpers (`AuthorizeEntry`,
`AuthorizeEntryWithDelegates`, `BuildAuthorizationEntryPreimageHash`), KAT-verified against
`@stellar/stellar-sdk` 16.0.0-rc.1. Shipped in
[16.0.0-beta](https://github.com/Beans-BV/dotnet-stellar-sdk/releases/tag/16.0.0-beta) (2026-06-25).
Tracking issues
[#186](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/186)/[#188](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/188)
stay open until the stable 16.0.0 release closes out the remaining RPC-flag follow-up.

---

#### Deliverable 2 — Integration Test Suite

| Metric                   | Planned                  | Delivered                                                                                                                                                   |
| ------------------------ | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Priority 1 MUST areas    | 17                       | **17/17 covered**                                                                                                                                           |
| Test methods             | est. 30–40               | **52** (33 live-network + 19 offline config-hardening)                                                                                                      |
| CI gating                | release tags only        | release tags **+ every push to `main`** + manual dispatch (superset of plan)                                                                                |
| Testnet-reset resilience | required (June 17 reset) | all tests self-provision via Friendbot; suite green post-reset ([run 28585099826](https://github.com/Beans-BV/dotnet-stellar-sdk/actions/runs/28585099826)) |

**Delivery PRs:**

| PR                                                                                               | Commit                                                                       | Magnitude              |
| ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | ---------------------- |
| [#185](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/185) integration test suite (phase 1) | [`539530e4`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/539530e4) | 14 files, +647 / −4    |
| [#196](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/196) integration test suite (phase 2) | [`f065324f`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/f065324f) | 30 files, +1,258 / −15 |

**All 17 Priority-1 MUST areas, each with a named test class** in
[`StellarDotnetSdk.IntegrationTests/`](https://github.com/Beans-BV/dotnet-stellar-sdk/tree/main/StellarDotnetSdk.IntegrationTests):

| #   | Area                                                          | Test class                                                    |
| --- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| 1   | Friendbot funding                                             | `FriendbotTests`                                              |
| 2   | `Server.RootAsync()`                                          | `RootTests`                                                   |
| 3   | SubmitTransaction — sync / async / fee bump                   | `SubmitTransactionTests` (3 tests)                            |
| 4   | CheckMemoRequired (SEP-29)                                    | `CheckMemoRequiredTests` (4 tests)                            |
| 5   | AccountsRequestBuilder                                        | `AccountsRequestBuilderTests`                                 |
| 6   | TransactionsRequestBuilder + pagination                       | `TransactionsRequestBuilderTests`                             |
| 7   | PaymentsRequestBuilder                                        | `PaymentsRequestBuilderTests`                                 |
| 8   | CreateAccountOperation                                        | `CreateAccountOperationTests`                                 |
| 9   | PaymentOperation (native + non-native)                        | `PaymentOperationTests`                                       |
| 10  | PathPayment StrictReceive + StrictSend (real orderbook)       | `PathPaymentStrictReceiveTests`, `PathPaymentStrictSendTests` |
| 11  | ManageSellOffer + ManageBuyOffer                              | `ManageOffersTests`                                           |
| 12  | ChangeTrust + SetOptions                                      | `ChangeTrustOperationTests`, `SetOptionsOperationTests`       |
| 13  | InvokeHostFunctionOperation (Soroban)                         | `InvokeHostFunctionTests`                                     |
| 14  | ExtendFootprint + RestoreFootprint                            | `FootprintTests`                                              |
| 15  | Soroban RPC full flow (all 8 planned methods)                 | `SorobanRpcFlowTests`                                         |
| 16  | SSE streaming (live Horizon events)                           | `SseStreamingTests`                                           |
| 17  | SEP-10 full auth flow vs real anchor (testanchor.stellar.org) | `Sep10AuthTests`                                              |

The CI workflow
([`integration_tests.yml`](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/main/.github/workflows/integration_tests.yml),
typical wall clock ~9 min) uses env-configurable endpoints with public-Testnet defaults and
secrets-based tokens, and uploads a TRX result artifact.

Writing the tests also surfaced and fixed **2 real SDK bugs** shipped inside #196:
`ExtendFootprintOperation.cs` and `RestoreFootprintOperation.cs` — exactly the class of "mocked tests
pass while production breaks" defect this deliverable was funded to catch.

**Priority-2 SHOULD tests:** none implemented in Q2. Per the submission's explicit rule ("Any items
not completed in Q2 move to Q3"), the full SHOULD list carries into Q3.

---

#### Deliverable 3 — Multi-Platform Preparation: Multi-Target + .NET Modernization

**Part B — Modern .NET APIs: all 6 PRs merged** (closing issues
[#164](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/164),
[#165](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/165),
[#166](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/166),
[#167](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/167),
[#168](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/168) — all closed):

| PR                                                                                                                                                                        | Commit                                                                       | Magnitude               | Landed at                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------- |
| [#180](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/180) `FrozenDictionary` for static lookup tables                                                               | [`360e040f`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/360e040f) | 6 files, +464 / −279    | `OperationResponseJsonConverter`, `EffectResponseJsonConverter`, 2 enum converters        |
| [#181](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/181) `AllowDuplicateProperties = false`                                                                        | [`1cadace0`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/1cadace0) | 3 files, +108 / −0      | `Converters/JsonOptions.cs:51`                                                            |
| [#182](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/182) `RespectNullableAnnotations`                                                                              | [`e03da676`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/e03da676) | 2 files, +75 / −0       | `Converters/JsonOptions.cs:54`                                                            |
| [#183](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/183) `JsonSerializerOptions.MakeReadOnly()`                                                                    | [`f0eb9987`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/f0eb9987) | 2 files, +94 / −33      | `Converters/JsonOptions.cs:85`                                                            |
| [#189](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/189) `Stream.ReadExactly()` in XDR decoding                                                                    | [`f33f13f2`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/f33f13f2) | 22 files, +688 / −752   | `XdrDataInputStream.cs` (7 call sites) + generator template                               |
| [#184](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/184) HTTP retry overhaul (`ForSoroban`/`ForHorizon` presets, POST retry on 408/429/5xx, `Retry-After` honored) | [`d72fa82c`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/d72fa82c) | 20 files, +2,591 / −370 | `Requests/HttpResilienceOptions.cs`, new `RetryingHttpMessageHandler`, `RetryAfterParser` |

Every planned Part B item from the submission (FrozenDictionary, ReadExactly,
AllowDuplicateProperties, RespectNullableAnnotations, MakeReadOnly) is merged and verifiable by
`grep` at the file/line references above.

**Part A — Multi-target `net10.0 + net8.0 + netstandard2.1`: merged as
[PR #195](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/195)** (merged 2026-07-02, commit
[`56671eb4`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/56671eb4), closing issue
[#162](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/162)):

| Criterion                          | Status                                                                                                                                                                                           |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Scope                              | 64 files, +1,440 / −248, opened 2026-06-26, merged 2026-07-02 after maintainer review rounds                                                                                                     |
| Both packages retargeted           | `StellarDotnetSdk` and `StellarDotnetSdk.Xdr` → `<TargetFrameworks>net10.0;net8.0;netstandard2.1</TargetFrameworks>`                                                                             |
| Crypto abstraction                 | internal `Ed25519` facade (`Crypto/Ed25519.cs`): NSec.Cryptography on net8.0/net10.0, Sodium.Core 1.4.1 on netstandard2.1, with cross-provider equivalence tests (`Ed25519CrossProviderTest.cs`) |
| Polyfills / compat                 | `CompilerPolyfills.cs`, `Throw.cs` (ThrowIfNull/ThrowIfNullOrEmpty), `NetstandardCompat.cs` (ReadExactly shim), `DateOnly` conditional handling for SEP-9                                        |
| Dedicated netstandard2.1 test host | new `StellarDotnetSdk.NetStandard21.Tests` project; CI packs and tests all three TFMs                                                                                                            |
| CI on merge commit                 | green ([run 28589757927](https://github.com/Beans-BV/dotnet-stellar-sdk/actions/runs/28589757927))                                                                                               |

With #195 merged, every planned D3 item — Part A and Part B — landed on `main` inside the Q2 window.
The multi-target package ships to NuGet with the stable 16.0.0 release early in Q3.

---

#### Deliverable 4 — SEP-45 Implementation + SEP Compatibility Matrices

**Closing issues:**
[#160 — SEP-45 Implementation](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/160) (closed
2026-06-25),
[#161 — SEP Compatibility Matrices](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/161)
(closed 2026-06-24).

**Delivery PRs:** [#190](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/190) SEP-45
implementation (merged 2026-06-24, commit
[`32f72f11`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/32f72f11), 39 files, +5,540 / −0)
and [#191](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/191) SEP matrices (6 files, +1,320,
merged into the feature branch 2026-06-23 and landed on `main` via #190 — the two PRs' line counts
overlap and must not be summed).

| Criterion           | Evidence                                                                                                                                                                           |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Implementation      | `StellarDotnetSdk.Sep.Sep0045` — 28 files: `ClientWebAuthContract` (toml discovery, challenge, validation, auth-entry signing, JWT), `Sep45Challenge` helpers, 22 typed exceptions |
| Security hardening  | 512 KiB response cap, https-only auth endpoint, no cross-origin credential forwarding, network-passphrase fail-fast                                                                |
| Unit tests          | **82 passed / 0 failed** (`dotnet test --filter "FullyQualifiedName~Sep0045"`)                                                                                                     |
| Peer-SDK gap closed | Flutter, iOS, and Java all shipped SEP-45 before us (issue #158's own framing: "we are the only SDK without it") — no longer true                                                  |
| Matrices            | 6 published in [`StellarDotnetSdk/Compatibility/sep/`](https://github.com/Beans-BV/dotnet-stellar-sdk/tree/main/StellarDotnetSdk/Compatibility/sep) — exactly the promised set     |

| Matrix   | Coverage                                                                                                                                                      |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SEP-0001 | 100.0% (70/70 fields)                                                                                                                                         |
| SEP-0006 | 100.0% (95/95 fields)                                                                                                                                         |
| SEP-0009 | 100.0% (76/76 fields)                                                                                                                                         |
| SEP-0010 | 100.0% (22/22 applicable fields)                                                                                                                              |
| SEP-0024 | 100.0% (94/94 fields)                                                                                                                                         |
| SEP-0045 | 100.0% (35/35 applicable fields) — `jwt_token_generation` marked N/A (server-side anchor responsibility; unimplemented in Flutter/Java/Python/JS/Go SDKs too) |

**Demo snippet using the new surface:**

```csharp
using StellarDotnetSdk.Sep.Sep0045;

// Discover config from the anchor's stellar.toml
using var webAuth = await ClientWebAuthContract.FromDomainAsync(
    "anchor.example.com", Network.Test(), "https://soroban-testnet.stellar.org");

// End-to-end SEP-45: GET challenge → validate → sign auth entries → POST → JWT
string jwt = await webAuth.JwtTokenAsync(
    clientAccountId: "C...CONTRACT_ADDRESS",
    signers: new[] { KeyPair.FromSecretSeed("S...") });
```

---

#### Deliverable 5 — Release & Verification

| Criterion                    | Evidence                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Releases shipped             | [15.0.0](https://github.com/Beans-BV/dotnet-stellar-sdk/releases/tag/15.0.0) (2026-04-09) · [15.1.0-beta](https://github.com/Beans-BV/dotnet-stellar-sdk/releases/tag/15.1.0-beta) (2026-04-22) · [15.1.0](https://github.com/Beans-BV/dotnet-stellar-sdk/releases/tag/15.1.0) (2026-06-07, current Latest) · [16.0.0-beta](https://github.com/Beans-BV/dotnet-stellar-sdk/releases/tag/16.0.0-beta) (2026-06-25) |
| Unit test suite              | **1,663 → 1,927 passed (+264, +15.9%)**, 0 failed                                                                                                                                                                                                                                                                                                                                                                 |
| Integration suite            | 52 tests, green in CI against live Testnet on every `main` push and release tag                                                                                                                                                                                                                                                                                                                                   |
| XML doc gate (Q1 carry-over) | 0 × CS1591, still enforced via `<WarningsAsErrors>CS1591</WarningsAsErrors>`                                                                                                                                                                                                                                                                                                                                      |
| CI on `main` @ `56671eb4`    | all green: Pack and Test, Integration Tests, CodeQL                                                                                                                                                                                                                                                                                                                                                               |
| Endpoint matrices            | Horizon 100.0% (50/50), RPC 100% — parity maintained                                                                                                                                                                                                                                                                                                                                                              |

Stable **16.0.0** (Protocol 27 + SEP-45 + modernization + multi-target, all now on `main`) is staged
as a draft and ships early Q3 — tracked in
[#159](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/159).

---

#### Non-deliverable — Developer Support & Maintenance Responsiveness

Operational metrics across the Q2 '26 window (2026-04-01 → 2026-07-02), reproducible via `gh`/`git`:

| Metric              | Count                                                                                                                                                                                                                                                                                                                                                                                                                | Command                                                                                                                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Commits on `main`   | **27**                                                                                                                                                                                                                                                                                                                                                                                                               | `git rev-list --count --since=2026-04-01 main`                                                                                                                     |
| PRs merged          | **22**                                                                                                                                                                                                                                                                                                                                                                                                               | `gh pr list --state merged --search "merged:2026-04-01..2026-07-02"`                                                                                               |
| Issues closed       | **16**                                                                                                                                                                                                                                                                                                                                                                                                               | `gh issue list --state closed --search "closed:2026-04-01..2026-07-02"` (13 via search; #157/#158/#163 verified via direct API — GitHub's search index omits them) |
| Goal-closing issues | 10 — [#155](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/155), [#160](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/160), [#161](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/161), [#162](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/162), [#164](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/164)–[#168](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/168) |                                                                                                                                                                    |
| Bug fixes           | 2 ([#179](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/179) missing `contract_credited`/`contract_debited` handling, closing [#172](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/172); [#178](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/178) docs build)                                                                                                                                   |                                                                                                                                                                    |
| Releases shipped    | **4** (2 stable, 2 beta)                                                                                                                                                                                                                                                                                                                                                                                             | `gh release list`                                                                                                                                                  |
| Author split        | cuongph87: 18 commits · jopmiddelkamp: 8 commits · michaelpham-rgb: 1 commit                                                                                                                                                                                                                                                                                                                                         | `git shortlog -sn --since=2026-04-01`                                                                                                                              |

**Continuity backlog already scoped for Q3:**
[#188](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/188) Protocol 27 close-out,
[#156](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/156) integration-test umbrella
(Priority-2), [PR #198](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/198) `getLatestLedger`
fields + matrix re-pins (in review), plus newly triaged bugs
[#193](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/193) (pagination drops auth/resilience
config) and [#197](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/197) (RPC error-response
mapping).

---

### 2. Cross-reference: Q1 reviewer expectations → Q2 evidence

| Expectation from Q1 review                             | Addressed by                                                                                                                                                               |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Explicit proof links per deliverable                   | Every deliverable above lists PRs with merge commits and +/− magnitudes                                                                                                    |
| Quantitative before/after                              | Tests 1,663 → 1,927; SEPs 5 → 6; SEP matrices 0 → 6 (all 100% field coverage); integration tests 0 → 52; targets net8.0 → net10.0 + net8.0 + netstandard2.1 (merged, #195) |
| Concrete issue/PR links per objective                  | Closing issues cited per deliverable (#155, #160, #161, #164–#168)                                                                                                         |
| SEP compatibility matrices (peers have them, we had 0) | Deliverable 4 — 6 matrices published in-tree                                                                                                                               |
| Automated test evidence                                | Unit suite + live-Testnet integration suite in CI ([run 28585099826](https://github.com/Beans-BV/dotnet-stellar-sdk/actions/runs/28585099826))                             |

---

### 3. Honest gaps & carry-over (pre-empting follow-ups)

- **Two D1 sub-items landed at window close, via
  [PR #198](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/198) (in review).** The Horizon/RPC
  matrix version bump (v27.0.0 / v26.0.1) and the `getLatestLedger` response fields (`closeTime`,
  `headerXdr`, `metadataXdr`) were completed on 2026-07-02, after the rest of this evidence was
  gathered. The research confirmed Horizon v26/v27 added no new endpoints (result codes and effects
  were already covered by #177/#179), so endpoint coverage remains 50/50.
- **Priority-2 SHOULD integration tests: 0 of the stretch list.** Priority 1 landed 17/17; the SHOULD
  list moves to Q3 exactly as the submission's overflow rule specified.
- **16.0.0 stable not yet published.** Protocol 27, SEP-45, and multi-target are all merged on `main`
  (multi-target since 2026-07-02); the stable major ships early Q3 rather than cutting a same-day
  release at window close.
- **Protocol 27 tracking issues (#186/#188) still open** although the CAP-71 code is merged and
  beta-shipped — they close with the stable release.
- **~175 non-CS1591 build warnings remain** (CS1572/1573/1574 doc-tag hygiene, some in the new SEP-45
  files). The CS1591 missing-doc gate from Q1 stays at zero; tag hygiene continues under the capacity
  buffer.

<!-- markdownlint-enable MD034 -->

## Proposed Impact

<!-- markdownlint-disable MD034 -->

Over the next three months Q3 2026, our goals are to close the SDK's most-used SEP gaps and to
validate the newly multi-targeted SDK on iOS and Android, while keeping the SDK reliable for its
existing production users.

**1. SEP expansion: SEP-7, SEP-12, SEP-38** The base SDK implements six SEPs today (SEP-1, 6, 9, 10,
24, 45). This quarter we implement three more: SEP-12 (KYC API) and SEP-38 (anchor RFQ/quotes), which
build directly on the SEP-10/45 WebAuth infrastructure already in the SDK and together complete the
anchor deposit/withdraw/quote flows that SEP-6 and SEP-24 integrators need in practice, and SEP-7,
the standard URI scheme for payment requests and delegated signing. Each ships with unit tests and a
per-SEP compatibility matrix in the format we established in Q2, taking the SDK from 6 to 9
implemented SEPs and giving .NET developers complete client-side coverage of the standard anchor
integration flows.

**2. Validate the SDK on iOS and Android via .NET MAUI** With the multi-target packages published, we
validate the SDK on iOS and Android via .NET MAUI: crypto (libsodium), the HTTP/SSE stack, and linker
trimming. The first week of July includes a short desk check of the one risk we already know is
concrete: neither NSec nor Sodium.Core ships iOS/Android native libsodium binaries in its standard
runtime packages, so the fallback choice (build libsodium for those targets, or a managed Ed25519
path) gets decided before dependent work starts. Validation runs Release builds with trimming
enabled, on iOS simulator and Android emulator plus at least one physical Android device; we add an
iOS device smoke test if the provisioning set up in this deliverable allows it, and if it does not,
the compatibility report states plainly that physical-iOS behavior (where AOT is enforced and there
is no JIT) remains unvalidated risk. This includes standing up the MAUI development and test
environment itself (Xcode + iOS simulators, Android SDK + emulators, MAUI workloads,
signing/provisioning), planned as its own work item from prior MAUI experience. This is a validation
milestone, not a sample app.

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

### Deliverable 1 — SEP Expansion: SEP-7, SEP-12, SEP-38 (+ matrices)

- **Specific:** Implement SEP-7 (URI scheme for payment requests and delegated signing), SEP-12 (KYC
  API), and SEP-38 (anchor RFQ/quotes), each with unit tests and a per-SEP compatibility matrix in
  `StellarDotnetSdk/Compatibility/sep/`, following the 100%-field-coverage format established in Q2.
  SEP-12 and SEP-38 build on the SEP-10/45 WebAuth infrastructure already in the SDK; SEP-7 is
  standalone and the smallest of the three.
- **Measurable:** 3 new SEP namespaces with passing unit tests; SEP matrix count grows from 6 to 9;
  SDK goes from 6 to 9 implemented SEPs.
- **Achievable:** All three SEP specifications are stable, two of the three reuse the SEP-10/45
  WebAuth infrastructure already in the SDK, and the matrix format is established practice from Q2.
- **Relevant:** SEP-12 and SEP-38 complete the anchor flow story: KYC and quotes are what
  SEP-6/SEP-24 integrations need alongside the deposit/withdraw support the SDK already ships. SEP-7
  gives wallets the standard URI scheme for payment requests and delegated signing. Together they are
  the three SEPs that unlock the most integrations for .NET developers today. SEP-30 (account
  recovery) stays at the top of the backlog (see ROADMAP.md); deferring it costs the least because
  its ecosystem adoption is the thinnest.
- **Time-bound:** Complete by end of the 3-month period, shipped in one or more 16.x minors as they
  complete.

### Deliverable 2 — MAUI Validation (incl. environment setup)

- **Specific:** Three parts. **Part 0, desk check (week 1 of July):** confirm whether the crypto
  backends (NSec, Sodium.Core) load on iOS/Android at all, given that neither ships native libsodium
  for those targets in its standard runtime packages, and pick the fallback (build libsodium for
  ios-arm64 and the Android ABIs, or a managed Ed25519 path) so the decision lands before dependent
  work starts. **Part A, environment:** stand up a reproducible MAUI development and test environment
  (macOS host with Xcode and iOS simulators, Android SDK with emulator images, .NET MAUI workloads,
  signing/provisioning configuration), documented with pinned workload and Xcode versions so it can
  be rebuilt on demand. **Part B, validation:** validate the multi-target SDK via a minimal .NET MAUI
  validation app, built in Release with trimming enabled: Ed25519 crypto (native library loading),
  HTTP/SSE stack behavior, and linker/trimming compatibility, on iOS simulator, Android emulator, and
  at least one physical Android device, plus an iOS device smoke test if provisioning allows. Produce
  a documented compatibility report with any required workarounds (e.g. linker descriptors). If
  physical iOS is not exercised, the report says so explicitly, because iOS devices enforce AOT with
  no JIT and a green simulator run does not cover that condition.
- **Measurable:** Desk-check decision recorded in week 1; environment setup documented and
  reproducible; validation app builds and runs core SDK flows (keypair generation/signing, Horizon
  query, transaction submit, Soroban simulate) on the platforms listed above; findings and any
  residual unvalidated risk documented in-repo.
- **Achievable:** Scoped strictly to validation, not a product sample; the crypto abstraction from PR
  #195 was designed for exactly this portability. Environment setup is planned as its own work item
  from prior MAUI experience, not overhead absorbed elsewhere. If the desk check forces building
  native libsodium for iOS/Android, that work draws on the capacity buffer, and the validation scope
  (not the SEP or release work) is what shrinks if the buffer is exhausted.
- **Relevant:** The multi-target packages make the SDK installable on iOS and Android for the first
  time; this deliverable turns "it should work there" into a tested, documented answer. Mobile
  developers get a compatibility report with known workarounds instead of discovering platform
  blockers themselves, and the native-crypto question — the single most likely blocker — is answered
  in week 1. This is the quarter's highest-uncertainty item, which the capacity buffer is sized for.
- **Time-bound:** Desk check in week 1 of July; environment and validation in the second half of the
  quarter, after the multi-target package is published.

### Non-deliverable 1 — Developer Support & Maintenance Responsiveness

- **Specific:** Triage and respond to SDK-related GitHub issues, feature requests, and Discord
  inquiries throughout the quarter. The two already-triaged bugs (#193, #197) are part of the Q2
  carry-over, not this bucket.
- **Measurable:** Issues acknowledged and either resolved, scoped, or explicitly deferred.
- **Achievable:** Bounded strictly to SDK maintenance and usage; if support demand exceeds the
  reservation, it draws on the capacity buffer before it touches deliverable scope.
- **Relevant:** Maintains developer trust and reduces adoption friction.
- **Time-bound:** Ongoing throughout the 3-month period.

### Non-deliverable 2 — Capacity Buffer

A contingency reserve sized for this quarter's specific risks: native-crypto or trimming surprises
during MAUI validation, netstandard2.1 regressions surfacing after the multi-target package reaches
real consumers, post-Mainnet-vote Protocol 27 follow-ups, and the external dependencies the
integration suite leans on (a Testnet reset or an SDF test-anchor change would stall
integration-gated releases for days). If the quarter runs clean and the buffer goes unused, it funds
pulling the next backlog item (SEP-30, see ROADMAP.md) forward; it is never pre-spent on planned
scope.

<!-- markdownlint-enable MD034 -->

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
