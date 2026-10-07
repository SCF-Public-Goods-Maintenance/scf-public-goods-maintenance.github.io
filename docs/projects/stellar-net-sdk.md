---
title: "Stellar .NET SDK"
canonical_id: daoip-5:scf:project:.net_stellar_sdk
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

### 2026 Q2

#### 0. One-command full verification

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

```txt
Passed!  - Failed:     0, Passed:  1927, Skipped:     1, Total:  1928   # unit suite (net8.0)
52                                                                      # integration [Test] methods
Passed!  - Failed:     0, Passed:    82, Skipped:     0, Total:    82   # SEP-45 tests
**Total Coverage:** 100.0%  (× 6 — SEP-1, 6, 9, 10, 24, 45)
0                                                                       # CS1591 count
```

The one skipped unit test is `AuthorizeEntry_AgainstP27Testnet_SubmitsSuccessfully` (network-gated by
design).

---

#### 1. Deliverable-by-deliverable evidence

##### Deliverable 1 — Protocol 26 "Yardstick" Support

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

##### Deliverable 2 — Integration Test Suite

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

##### Deliverable 3 — Multi-Platform Preparation: Multi-Target + .NET Modernization

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

##### Deliverable 4 — SEP-45 Implementation + SEP Compatibility Matrices

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

##### Deliverable 5 — Release & Verification

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

##### Non-deliverable — Developer Support & Maintenance Responsiveness

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

#### 2. Cross-reference: Q1 reviewer expectations → Q2 evidence

| Expectation from Q1 review                             | Addressed by                                                                                                                                                               |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Explicit proof links per deliverable                   | Every deliverable above lists PRs with merge commits and +/− magnitudes                                                                                                    |
| Quantitative before/after                              | Tests 1,663 → 1,927; SEPs 5 → 6; SEP matrices 0 → 6 (all 100% field coverage); integration tests 0 → 52; targets net8.0 → net10.0 + net8.0 + netstandard2.1 (merged, #195) |
| Concrete issue/PR links per objective                  | Closing issues cited per deliverable (#155, #160, #161, #164–#168)                                                                                                         |
| SEP compatibility matrices (peers have them, we had 0) | Deliverable 4 — 6 matrices published in-tree                                                                                                                               |
| Automated test evidence                                | Unit suite + live-Testnet integration suite in CI ([run 28585099826](https://github.com/Beans-BV/dotnet-stellar-sdk/actions/runs/28585099826))                             |

---

#### 3. Honest gaps & carry-over (pre-empting follow-ups)

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

In Q4 2026 we want to keep the SDK correct for the people already running it in production, finish
the work our Q3 report moved to this quarter, and have Protocol 30 on NuGet before it reaches
Mainnet. Every item below is an issue on our [2026 Q4 milestone][milestone], so anyone can follow the
progress during the quarter.

**1. Fix what breaks real integrations first.** 16.0.0 has two known bugs. Our SEP-45 client rejects
the `ADDRESS_V2` challenges that servers built on the Java and Python SDKs now issue by default
([#240][i240]). Following a Horizon page link drops the caller's authentication, headers and retry
settings ([#193][i193]); our Q3 report moved this bug to Q4. We also found that liquidity pool
parameters reject the asset order the network requires ([#257][i257]), a bug the JS and Go SDKs fixed
recently. All three ship as a 16.0.x patch in October.

**2. Ship Protocol 30 to NuGet before the Mainnet vote.** Protocol 27 and 28 support was ready weeks
before Mainnet, but it only reached NuGet with 16.0.0, because we tied it to a major release. That's
on us. From now on, protocol support ships in a minor release of the current major, before the
Mainnet vote. Protocol 30 is the first test: CAP-84 adds a new contract address type and a `W...`
strkey, and CAP-88 adds ledger header variants that older XDR fails to decode from the first ledger
after the upgrade.

**3. Finish the integration test suite.** Our Q3 report moved the Priority-2 integration tests
([#156][i156]) to Q4. They cover the Horizon endpoints, operations and RPC methods that the 56
current Testnet tests don't reach yet. Mocked unit tests missed real bugs twice this year: the Q2
integration tests found two broken Soroban operations, and in Q3 the RPC client sent requests that
stellar-rpc rejects.

We sized this plan for one senior developer, with a buffer for Protocol 30 and privately reported
security issues. The Soroban developer layer is scoped and planned for Q1 2027: transaction lifecycle
helpers ([#259][ilifecycle]) and contract metadata and specs ([#260][iintro]). Cancellation tokens on
the core clients ([#262][icancel]) and the remaining HTTP and SEP client hardening ([#237][i237],
[#245][i245], [#205][i205]) follow in the same quarter.

<!-- markdownlint-enable MD034 -->

## Proposed Deliverables

<!-- markdownlint-disable MD034 -->

Each deliverable has an ID. Its issues are on the [2026 Q4 milestone][milestone], and its PRs carry
the ID in the title (for example `D2: regenerate XDR for Protocol 30`), so at the end of the quarter
one search finds the evidence.

### D1: Fixes for bugs that break integrations today

- **Specific:** Accept `ADDRESS_V2` SEP-45 challenges ([#240][i240]). Make page links reuse the
  caller's configured `HttpClient` ([#193][i193], carried over from Q3). Order assets by issuer key
  bytes, as stellar-core does ([#257][i257]). Fix any privately reported security issues under our
  [security policy][secpolicy].
- **Measurable:** A merged PR closes each issue, with a regression test that fails on 16.0.0. All
  three fixes ship in a 16.0.x patch release.
- **Achievable:** All three bugs are diagnosed. The SEP-45 fix is written and tested on a branch,
  #193 has a known root cause and fix, and we reproduced #257 with a small probe before we filed it.
- **Relevant:** #240 breaks SEP-45 sign-in against anchors that use the Java or Python SDK. #193
  silently drops authentication on paginated reads from hosted Horizon providers. For some asset
  pairs, #257 makes the SDK refuse a valid liquidity pool and accept the invalid one.
- **Time-bound:** The patch release in October.

### D2: Protocol 30 before Mainnet, and a written release policy

- **Specific:** Regenerate XDR for Protocol 30 and add CAP-84 muxed contract addresses with the new
  `W...` strkey ([issue][ip30]). Add a scheduled CI check that flags when upstream `stellar-xdr`
  moves past the version we generate from, so new XDR doesn't surprise us again. Publish a release
  policy ([issue][ipolicy]) that says which target frameworks we ship and why, what happens when a
  .NET version reaches end of support, and that protocol support lands in minor releases.
- **Measurable:** A 16.x release with Protocol 30 support is on NuGet before the Mainnet vote. If no
  vote is scheduled this quarter, we publish a pre-release built from the gated XDR instead. A test
  decodes a post-upgrade Testnet ledger header. The policy is merged and linked from the README.
- **Achievable:** We've done this three times this year (Protocols 26, 27 and 28) with our own XDR
  generator. The new part is the release step.
- **Relevant:** Without regenerated XDR, any .NET app that decodes ledger headers or close meta
  breaks at the upgrade. A written policy lets users plan around .NET end-of-life dates instead of
  finding out from a changelog.
- **Time-bound:** Pinned to SDF's Protocol 30 dates, which aren't announced yet. The policy goes out
  before .NET 8 reaches end of support on 2026-11-10.

### D3: Priority-2 integration tests (carried over from Q3)

- **Specific:** Add Testnet integration tests for the Priority-2 list in [#156][i156]: the remaining
  Horizon query endpoints (assets, claimable balances, effects, ledgers, offers, order book, trades,
  trade aggregations, fee stats, liquidity pools, strict-send and strict-receive paths, health), the
  remaining operations (account merge, manage data, bump sequence, passive sell offers, claimable
  balances, sponsorship, clawback, trustline flags, liquidity pool deposit and withdraw), the RPC
  methods `getTransactions`, `getLedgers`, `getVersionInfo` and `getFeeStats`, and SEP-1, federation
  and multi-operation transactions.
- **Measurable:** Every area on the Priority-2 list has at least one test that runs in the
  integration workflow on each push to `main`, and #156 is closed.
- **Achievable:** The test infrastructure is in place since Q2: a base class, a Friendbot helper,
  configurable endpoints and a CI workflow that runs 56 tests on every push to `main`. The new tests
  follow the same pattern.
- **Relevant:** These tests catch the gap between mocked JSON and the live network, where this year's
  footprint and RPC bugs came from.
- **Time-bound:** During the quarter, with the read-only endpoints first and the operations after.

### Non-deliverable 1: Developer support and maintenance responsiveness

- **Specific:** Triage and answer SDK-related GitHub issues, pull requests and Discord questions
  throughout the quarter. When we act on a request, we say so on the issue itself.
- **Measurable:** Each issue is acknowledged, then resolved, scoped onto a milestone, or declined
  with a reason.
- **Achievable:** Limited to SDK maintenance and usage. If support takes more time than reserved, it
  draws on the capacity buffer before it touches deliverable scope.
- **Relevant:** In Q3, we acted on two requests from Stellar's SDK team but never answered on the
  issues themselves.
- **Time-bound:** Ongoing throughout the quarter.

### Non-deliverable 2: Things with fixed dates

Each of these has a date we can't move:

- .NET 8 and .NET 9 reach end of support on 2026-11-10. The release policy in D2 records what happens
  to our `net8.0` target. Our current plan is to keep it through 16.x and drop it in 17.0.
- .NET 11 is expected in November 2026. We'll add it to the CI test matrix once it's out and repeat
  the MAUI validation there, because MAUI on .NET 11 runs only on CoreCLR.
- GitHub is moving `ubuntu-latest` runners to Ubuntu 26.04 between 2026-10-19 and 2026-11-19
  ([announcement][runner2604]). All our workflows run on `ubuntu-latest`, so we'll check them before
  the switch reaches us, including the live Testnet integration suite and the NuGet publish.

### Non-deliverable 3: Capacity buffer

The buffer covers this quarter's specific risks: Protocol 30 arriving with less notice than earlier
upgrades, privately reported security fixes, and Testnet resets or test-anchor changes that stall the
integration suite. If the quarter runs clean, the buffer goes to these items, in this order:

1. SEP-53 message signing and verification ([#261][isep53]).
2. The XDR decoding crashes on valid contract deployments ([#248][i248], [#249][i249]).
3. SourceLink, symbols, an SBOM and build provenance for our packages ([#263][iprov]).
4. The XDR codec's acceptance of non-canonical input ([#250][i250]).
5. The lossy XDR string round-trips ([#246][i246], [#247][i247]).
6. Size caps on the Horizon, RPC, stellar.toml and federation response bodies.
7. Replacing the 2019 SSE dependency behind the Android streaming delay.
8. Logging hooks ([#88][i88]).

We never spend the buffer on planned scope in advance.

[milestone]: https://github.com/Beans-BV/dotnet-stellar-sdk/milestone/1
[runner2604]: https://github.com/actions/runner-images/issues/14748
[secpolicy]: https://github.com/Beans-BV/dotnet-stellar-sdk/blob/main/SECURITY.md
[i88]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/88
[i156]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/156
[i193]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/193
[i205]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/205
[i237]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/237
[i240]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/240
[i245]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/245
[i246]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/246
[i247]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/247
[i248]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/248
[i249]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/249
[i250]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/250
[i257]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/257
[ip30]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/258
[ipolicy]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/264
[ilifecycle]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/259
[iintro]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/260
[isep53]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/261
[icancel]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/262
[iprov]: https://github.com/Beans-BV/dotnet-stellar-sdk/issues/263

<!-- markdownlint-enable MD034 -->

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3A.net_stellar_sdk&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3A.net_stellar_sdk)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3A.net_stellar_sdk&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3A.net_stellar_sdk)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3A.net_stellar_sdk&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3A.net_stellar_sdk)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3A.net_stellar_sdk&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3A.net_stellar_sdk)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
