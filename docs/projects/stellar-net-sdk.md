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

In Q3 2026 the work split between the two committed deliverables and an unplanned round of fixes in
the Soroban RPC client. Both deliverables merged on 2026-10-02. All of the quarter's work is in the
[16.0.0](https://github.com/Beans-BV/dotnet-stellar-sdk/releases/tag/16.0.0) stable release,
available on NuGet since 2026-10-03.

Our unit tests for the Soroban RPC client ran against mocked JSON. This quarter we compared the
request and response models with what a real stellar-rpc server sends and accepts, and found bugs
that had shipped. Since 14.0.0, `SimulateTransaction` sent `authMode` in a form stellar-rpc rejects
(a number in 14.x, upper case in 15.x), so every call that set it failed
([#209](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/209)). `getEvents` dropped the caller's
pagination ([#219](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/219)), JSON-RPC error
responses were swallowed ([#217](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/217)), and
`RestorePreamble.SorobanTransactionData` always threw
([#222](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/222)). Status enums accepted bare
numbers, so a malformed value could read as a real status
([#235](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/235),
[#236](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/236)). The fixes took 15 PRs, and each one
adds tests pinned to the upstream wire format.

We also completed Protocol 27 (CAP-71) authorization. Stellar's SDK team asked for a
`useUpgradedAuth` simulation flag in
[#206](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/206), and
[#209](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/209) adds it. With the flag, .NET apps can
request address-bound v2 credentials, which cannot be replayed against another account, and 16.0.0
makes them the default ([#244](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/244)). New live
Testnet tests sign and submit both credential variants, so the network itself confirms the SDK's v2
signature preimage.

For Deliverable 1, SEP-7, SEP-12 and SEP-38 shipped in 16.0.0, each with a compatibility matrix at
100% field coverage. For Deliverable 2, we validated the SDK through .NET MAUI on an Android
emulator, four physical Android devices, an iPhone 15 Pro (which runs AOT-only), the iOS Simulator
and Mac Catalyst. The compatibility report lists every workaround and the remaining risk. The
validation also showed that 15.1.0 fails on Android; 16.0.0 fixes that for .NET 10 MAUI apps.

16.0.0 is our first multi-target package on NuGet (`net10.0`, `net8.0`, `netstandard2.1`) and adds
Protocol 28 support. Protocol 29, on Mainnet since 2026-10-01, changed no XDR, so 16.0.0 reads the
network as it runs today.

<!-- markdownlint-enable MD034 -->

## Past Deliverables

<!-- markdownlint-disable MD034 -->

### 2026 Q3

**Verification target:** release tag
[`16.0.0`](https://github.com/Beans-BV/dotnet-stellar-sdk/releases/tag/16.0.0) @
[`9440e88e`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/9440e88e) on `main` (2026-10-03).
It sits one commit above [`51cc50c4`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/51cc50c4)
(2026-10-02, the last deliverable merged) and changes only the CHANGELOG, version numbers, matrix
headers and one publish-workflow flag, not code or tests · CI on the tag commit: green — Pack and
Test ([run 37089117259](https://github.com/Beans-BV/dotnet-stellar-sdk/actions/runs/37089117259)),
Integration Tests against live Testnet
([run 37089117283](https://github.com/Beans-BV/dotnet-stellar-sdk/actions/runs/37089117283), 56/56),
XDR Generator Tests
([run 37089117258](https://github.com/Beans-BV/dotnet-stellar-sdk/actions/runs/37089117258)), CodeQL
([run 37089116601](https://github.com/Beans-BV/dotnet-stellar-sdk/actions/runs/37089116601)) ·
Published to NuGet as
[`stellar-dotnet-sdk` 16.0.0](https://www.nuget.org/packages/stellar-dotnet-sdk/16.0.0) and
[`stellar-dotnet-sdk-xdr` 16.0.0](https://www.nuget.org/packages/stellar-dotnet-sdk-xdr/16.0.0)
([publish run 37090782596](https://github.com/Beans-BV/dotnet-stellar-sdk/actions/runs/37090782596))
· **Activity window:** 2026-07-03 → 2026-10-02, starting the day after the Q2 report's cutoff so no
work is counted twice.

| Item                                     | Result                                                                                                           |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Deliverable 1: SEP-7, SEP-12, SEP-38     | ✅ Delivered and released in 16.0.0                                                                              |
| Deliverable 2: MAUI validation           | ✅ Delivered: Android (emulator + 4 physical devices), iPhone, iOS Simulator and Mac Catalyst                    |
| Non-deliverable 1: support & maintenance | ✅ 13 issues closed (11 bugs), 30 PRs merged; two issues from Stellar's SDK team got no reply                    |
| Non-deliverable 2: capacity buffer       | ✅ Fully used: Soroban RPC correctness, Protocol 27 follow-ups, Protocol 28                                      |
| Release                                  | ✅ Completed: 16.0.0 available on [NuGet](https://www.nuget.org/packages/stellar-dotnet-sdk/16.0.0) (2026-10-03) |

#### 0. One-command verification

Every deliverable is in the 16.0.0 release, so one checkout of the tag reproduces every number below
in a few minutes. The MAUI checks need network access to Stellar Testnet.

```bash
git clone https://github.com/Beans-BV/dotnet-stellar-sdk.git
cd dotnet-stellar-sdk
git checkout -q 16.0.0

# The NuGet package ships three target frameworks
curl -sL https://api.nuget.org/v3-flatcontainer/stellar-dotnet-sdk/16.0.0/stellar-dotnet-sdk.16.0.0.nupkg -o sdk.nupkg
unzip -l sdk.nupkg | grep -oE "lib/[^ ]+\.dll"

# Full unit suite (expect 3756 passed on net8.0; the Q2 report had 1927)
dotnet test StellarDotnetSdk.Tests -f net8.0 --nologo 2>&1 | tail -1

# Deliverable 1: SEP unit tests and matrix coverage
for sep in 0007 0012 0038; do
  dotnet test StellarDotnetSdk.Tests -f net8.0 --no-build --nologo \
    --filter "FullyQualifiedName~Tests.Sep.Sep${sep}" 2>&1 | tail -1
  grep -h "Total Coverage" "StellarDotnetSdk/Compatibility/sep/SEP-${sep}_COMPATIBILITY_MATRIX.md"
done
ls StellarDotnetSdk/Compatibility/sep/ | wc -l   # SEP matrices

# Deliverable 2: the six MAUI validation checks as a desktop app, built from source
dotnet run --project StellarDotnetSdk.MauiValidation/Desktop -c Release 2>&1 | grep RESULT

# Deliverable 2: the same six checks against the published NuGet package (run next to the clone)
cd ..
dotnet new console --framework net10.0 -o pkgcheck
cp dotnet-stellar-sdk/StellarDotnetSdk.MauiValidation/{ValidationRunner.cs,StreamSearch.cs,Desktop/Program.cs} pkgcheck/
dotnet add pkgcheck package stellar-dotnet-sdk --version 16.0.0
dotnet run --project pkgcheck 2>&1 | grep -E "assemblies|RESULT"
```

Expected output (unit test lines trimmed after `Total`):

```txt
lib/net10.0/StellarDotnetSdk.dll
lib/net8.0/StellarDotnetSdk.dll
lib/netstandard2.1/StellarDotnetSdk.dll
Passed!  - Failed:     0, Passed:  3756, Skipped:     1, Total:  3757   # full suite
Passed!  - Failed:     0, Passed:   589, Skipped:     0, Total:   589   # SEP-7
**Total Coverage:** 100.0% (31/31 fields)
Passed!  - Failed:     0, Passed:   368, Skipped:     0, Total:   368   # SEP-12
**Total Coverage:** 100.0% (90/90 fields)
Passed!  - Failed:     0, Passed:   284, Skipped:     0, Total:   284   # SEP-38
**Total Coverage:** 100.0% (75/75 fields)
9                                                                       # SEP matrices
STELLAR-MAUI-VALIDATION RESULT PASS 6/6                                 # from source
STELLAR-MAUI-VALIDATION INFO assemblies StellarDotnetSdk 16.0.0+9440e88e3cb953e4a2b7ed34d1bdef472533af14, NSec.Cryptography 26.4.0+…
STELLAR-MAUI-VALIDATION RESULT PASS 6/6                                 # from the NuGet package
```

The test counts include every `[DataRow]` case. The one skipped unit test is network-gated by design,
as in Q2. The suite also passes on `net10.0` (3,766) and on the `netstandard2.1` build (3,762).

---

#### 1. Evidence per deliverable

##### Deliverable 1: SEP Expansion (SEP-7, SEP-12, SEP-38, with matrices)

**Status: delivered and released.** All three PRs were opened on 2026-09-30 and merged on 2026-10-02,
after maintainer review and green CI, and shipped in
[16.0.0](https://github.com/Beans-BV/dotnet-stellar-sdk/releases/tag/16.0.0) on 2026-10-03. The plan
was to ship them "in one or more 16.x minors as they complete"; they shipped together in 16.0.0
instead.

| PR                                                                                       | Merge commit                                                                 | Magnitude              | SEP version | Matrix                                                                                                                                             | Unit tests |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [#238](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/238) SEP-7 URI scheme         | [`674980e0`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/674980e0) | 32 files, +7,392 / −5  | 2.1.0       | [100.0% (31/31)](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/9440e88e/StellarDotnetSdk/Compatibility/sep/SEP-0007_COMPATIBILITY_MATRIX.md) | 589 passed |
| [#239](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/239) SEP-12 KYC API client    | [`51cc50c4`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/51cc50c4) | 51 files, +7,810 / −58 | 1.15.0      | [100.0% (90/90)](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/9440e88e/StellarDotnetSdk/Compatibility/sep/SEP-0012_COMPATIBILITY_MATRIX.md) | 368 passed |
| [#243](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/243) SEP-38 Anchor RFQ client | [`756a589f`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/756a589f) | 45 files, +7,320 / −15 | 2.5.0       | [100.0% (75/75)](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/9440e88e/StellarDotnetSdk/Compatibility/sep/SEP-0038_COMPATIBILITY_MATRIX.md) | 284 passed |

| Criterion (from the proposal)                                | Evidence                                                                                                                                                                                              |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3 new SEP namespaces with passing unit tests                 | `Sep/Sep0007` (`UriScheme`, `Sep7Uri`), `Sep/Sep0012` (`KycService`, `KycCallbackSignature`), `Sep/Sep0038` (`QuoteService`, `AssetIdentifier`); 1,241 SEP unit tests, 0 failing                      |
| Matrix count grows from 6 to 9                               | 9 matrices in [`StellarDotnetSdk/Compatibility/sep/`](https://github.com/Beans-BV/dotnet-stellar-sdk/tree/9440e88e/StellarDotnetSdk/Compatibility/sep), each at 100% field coverage, in the Q2 format |
| SDK goes from 6 to 9 implemented SEPs                        | SEP-1, 6, 7, 9, 10, 12, 24, 38 and 45                                                                                                                                                                 |
| SEP-12 and SEP-38 reuse the SEP-10/45 WebAuth infrastructure | Both clients take the JWT that the existing SEP-10 and SEP-45 clients produce, and discover their endpoints from `stellar.toml` like SEP-6 and SEP-24                                                 |

With SEP-6 and SEP-24 already in the SDK, a .NET client can now run the standard client-side anchor
flow with SDK calls only: SEP-1 (discover) → SEP-10/45 (authenticate) → SEP-12 (KYC) → SEP-38 (quote)
→ SEP-6/24 (deposit or withdraw).

The matrices use the same field-level format as the other Stellar SDKs, so the percentages are
comparable. For SEP-38 v2.5.0 our matrix lists 75 fields where the Flutter SDK's lists 58; ours also
covers the buy-side `/prices` fields added in v2.3.0 and the delivery-method fields.

All three clients carry the hardening established for SEP-45 in Q2: https-only endpoints (plain http
only for an explicit loopback host), capped response bodies (512 KiB for SEP-7's `stellar.toml` and
callback reads, 1 MiB for SEP-12 and SEP-38), no automatic redirect following on the SDK's own HTTP
client (SEP-7's `stellar.toml` fetch allows up to five https redirects), rejection of duplicate JSON
properties, JWTs and KYC data redacted from request `ToString()`, and bounded, sanitized exception
messages.

**Demo snippet** (compiles against the NuGet package 16.0.0 with warnings as errors):

```csharp
using StellarDotnetSdk.Sep.Sep0007;
using StellarDotnetSdk.Sep.Sep0012;
using StellarDotnetSdk.Sep.Sep0012.Requests;
using StellarDotnetSdk.Sep.Sep0038;
using StellarDotnetSdk.Sep.Sep0038.Requests;

// SEP-7: build a payment request, then validate it on the wallet side
string uri = UriScheme.GeneratePayOperationUri(
    destination: "GDR6DXASQP4XMGFBCU4NQEU63WY3WEOMPQAQLBJN533GKGBV3MOWIJTL",
    amount: "120.5",
    assetCode: "USDC",
    assetIssuer: "GBBD47IF6LWK7P7MDEVSCWR7DPUWV3NY3DTQEVFL4NAT4AQH3ZLLFLA5");
Sep7ValidationResult check = UriScheme.ValidateUri(uri); // check.IsValid == true

// SEP-12: the customer's KYC status (the JWT comes from SEP-10 or SEP-45)
var kyc = await KycService.FromDomainAsync("testanchor.stellar.org");
var customer = await kyc.GetCustomerInfoAsync(new GetCustomerInfoRequest { Jwt = jwt });
// customer.Status: Accepted | Processing | NeedsInfo | Rejected

// SEP-38: a firm quote, USD by wire -> USDC
var quotes = await QuoteService.FromDomainAsync("testanchor.stellar.org");
var quote = await quotes.PostQuoteAsync(new QuoteRequest
{
    Context = QuoteContext.Sep6,
    SellAsset = AssetIdentifier.Iso4217("USD"),
    BuyAsset = AssetIdentifier.Stellar("USDC", "GBBD47IF6LWK7P7MDEVSCWR7DPUWV3NY3DTQEVFL4NAT4AQH3ZLLFLA5"),
    SellAmount = 100m,
    SellDeliveryMethod = "WIRE",
    CountryCode = "US",
    Jwt = jwt,
});
```

---

##### Deliverable 2: MAUI Validation (incl. environment setup)

**Status: delivered.** Two PRs:

- [PR #242](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/242) (merge commit
  [`ed597e26`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/ed597e26), 2026-10-02, 27 files,
  +1,829 / −3): the validation app
  ([`StellarDotnetSdk.MauiValidation/`](https://github.com/Beans-BV/dotnet-stellar-sdk/tree/17450661/StellarDotnetSdk.MauiValidation)),
  the desk check, the Android environment and runs, and the compatibility report
  ([`docs/maui-compatibility.md`](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/17450661/docs/maui-compatibility.md)).
- [PR #256](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/256) (merge commit
  [`17450661`](https://github.com/Beans-BV/dotnet-stellar-sdk/commit/17450661), 2026-10-03, 8 files,
  +228 / −22): the macOS environment and the Apple runs on iPhone, iOS Simulator and Mac Catalyst,
  against both `main` and the published NuGet package 16.0.0. It changes only the validation app and
  the report, not SDK code.

The report's own coverage table
([§5](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/17450661/docs/maui-compatibility.md#5-deliverable-coverage-scf-q3-2026-deliverable-2))
maps every commitment to its status:

| Commitment                                                                                       | Status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Desk check: do NSec and Sodium.Core load on iOS and Android; pick a fallback                     | ✅ Done on 2026-09-30, not in the first week of July as planned. Decision: keep NSec as the only backend on the MAUI path, with no libsodium bundling and no managed fallback ([§1](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/17450661/docs/maui-compatibility.md#1-desk-check-does-the-ed25519-backend-load-on-ios-and-android)). The Apple runs confirmed its predictions                                                                                                                                            |
| Environment for Android: SDK, emulator, MAUI workloads, pinned versions                          | ✅ Reproducible from a script: .NET SDK 10.0.401, workload set 10.0.401.1 (MAUI 10.0.110, Android 36.1.69), android-36 platform, API 28 x86_64 emulator image ([§2](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/17450661/docs/maui-compatibility.md#2-environment-setup))                                                                                                                                                                                                                                                |
| Environment for iOS: macOS host, Xcode, simulators, signing and provisioning                     | ✅ Apple silicon Mac, macOS 26.6, Xcode 27.0, iOS 27.0 simulator runtime, Apple Development certificate with a team provisioning profile, with build and run commands ([§2](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/17450661/docs/maui-compatibility.md#2-environment-setup))                                                                                                                                                                                                                                        |
| Validation app, Release build with trimming                                                      | ✅ `TrimMode=partial` (the MAUI default, no changes needed) and `TrimMode=full` (needs a documented linker descriptor; without it the first Horizon call fails) ([§3.2](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/17450661/docs/maui-compatibility.md#32-trimming))                                                                                                                                                                                                                                                    |
| Core flows: key pair generation and signing, Horizon query, transaction submit, Soroban simulate | ✅ All pass against Testnet on the Android emulator, four physical Android devices, an iPhone, the iOS Simulator and Mac Catalyst                                                                                                                                                                                                                                                                                                                                                                                                |
| Ed25519 native library loading, HTTP/SSE, trimming                                               | ✅ libsodium loads on every platform: dynamically on Android, statically linked on iOS. Found an Android-only SDK limitation: the default Android HTTP handler holds SSE events back by about 47 s; a documented `SocketsHttpHandler` workaround delivers them in under 4 s ([§3.3](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/17450661/docs/maui-compatibility.md#33-sse-streaming-on-android-the-default-http-handler-holds-events-back)). Apple platforms deliver SSE events in about 2–4 s with the default handler |
| Android emulator                                                                                 | ✅ x86_64, API 28                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| At least one physical Android device                                                             | ✅ Four arm64 devices on 2026-10-02: Pixel XL (Android 10, API 29), Galaxy S21 Ultra (Android 15, API 35), Find X9 Pro (Android 16, API 36), Galaxy S23 Ultra (Android 16, API 36), all with full trimming ([§3.1](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/17450661/docs/maui-compatibility.md#31-android-results-mono-runtime-release))                                                                                                                                                                             |
| iOS simulator                                                                                    | ✅ 6/6 on iOS 27.0 (arm64). The libsodium package has no simulator build, so the link fails, as the desk check predicted; the new `build-libsodium-simulator.sh` builds one from the signed upstream release ([§3.4](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/17450661/docs/maui-compatibility.md#34-ios-and-mac-catalyst-results-release-trimmodefull--workaround-2026-10-03))                                                                                                                                       |
| iOS device smoke test                                                                            | ✅ 6/6 on an iPhone 15 Pro (iOS 26.6.2) with `TrimMode=full`, AOT-only (`dynamicCode=False`, no JIT), with the SDK from `main` and with NuGet 16.0.0 ([§3.4](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/17450661/docs/maui-compatibility.md#34-ios-and-mac-catalyst-results-release-trimmodefull--workaround-2026-10-03))                                                                                                                                                                                               |
| Mac Catalyst (beyond the plan)                                                                   | ✅ 6/6 on macOS 26.6 (arm64), with `main` and with NuGet 16.0.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Validation after the multi-target package is published                                           | ✅ On iPhone and Mac Catalyst with NuGet 16.0.0, and on desktop (osx-arm64). The Android runs used `main` @ `83303a27`, before the release; it resolves the same crypto dependencies as 16.0.0 (NSec 26.4.0, libsodium 1.0.22)                                                                                                                                                                                                                                                                                                   |
| Compatibility report with workarounds and residual risk                                          | ✅ [`docs/maui-compatibility.md`](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/17450661/docs/maui-compatibility.md)                                                                                                                                                                                                                                                                                                                                                                                                       |

The validation also produced concrete findings for app developers:

- **15.1.0 does not work on Android.** It fails at the first crypto call
  (`PlatformNotSupportedException`), because its libsodium has no Android binaries. The multi-target
  16.0.0 package fixes this for .NET 10 MAUI apps; a .NET 9 MAUI app resolves the `net8.0` target and
  still needs an explicit `NSec.Cryptography` 26.4.0 reference.
- **iOS 27 stops MAUI apps without the UIScene lifecycle at launch.** This is a MAUI template gap,
  not an SDK one; the report documents the fix (a scene manifest and a `SceneDelegate`).
- **The iOS Simulator needs a simulator build of libsodium**, which the validation app shows how to
  build and link. Devices and Mac Catalyst need nothing.

The report lists the remaining risk plainly
([§4](https://github.com/Beans-BV/dotnet-stellar-sdk/blob/17450661/docs/maui-compatibility.md#4-residual-risk-what-was-not-validated)):
one physical iOS device (iOS 26.6.2) and no iOS 15–17 or physical iOS 27 device, the MAUI default
trim mode and NativeAOT on iOS not run, and the Android runs not repeated against the 16.0.0 package.

---

##### Non-deliverable 1: Developer Support & Maintenance Responsiveness

Operational metrics for the activity window (2026-07-03 → 2026-10-02), reproducible via `gh` and
`git`:

| Metric                        | Count                                                                                                                                                                                                                                                     | Command                                                                                                                              |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Commits on `main`             | **30** (cuongph87 24, Jop Middelkamp 6)                                                                                                                                                                                                                   | `git rev-list --count --since=2026-07-03T00:00Z --until=2026-10-03T00:00Z main`                                                      |
| PRs merged                    | **30** (28 into `main`, 2 into stacked PR branches), of which 9 merged on 2026-10-02, including all four deliverable PRs (#238, #239, #242, #243)                                                                                                         | `gh pr list --state merged --search "merged:2026-07-03..2026-10-02"`                                                                 |
| Issues opened / closed        | **23** / **13** (11 of the 13 are bugs)                                                                                                                                                                                                                   | `gh issue list --state all --search "created:2026-07-03..2026-10-02"`, and `--state closed --search "closed:2026-07-03..2026-10-02"` |
| Unit tests on `main` (net8.0) | **1,927 → 2,311** at the last September merge (`83303a27`), **3,756** at the 16.0.0 tag                                                                                                                                                                   | see §0                                                                                                                               |
| Integration test methods      | **52 → 56** (CAP-71 v2 and Protocol 28 live tests); 29 of 30 runs on `main` pushes green, the red one ([run 33148039960](https://github.com/Beans-BV/dotnet-stellar-sdk/actions/runs/33148039960)) was three tests hitting Horizon Testnet 502/503 errors | `grep -rE '^\s*\[Test\]' --include='*.cs' StellarDotnetSdk.IntegrationTests \| wc -l`                                                |
| Releases published            | **1**: [16.0.0](https://github.com/Beans-BV/dotnet-stellar-sdk/releases/tag/16.0.0) (2026-10-03), available on NuGet                                                                                                                                      | `gh release list`                                                                                                                    |
| NuGet downloads (lifetime)    | stellar-dotnet-sdk 566,582; stellar-dotnet-sdk-xdr 481,996                                                                                                                                                                                                | NuGet search API, 2026-10-03                                                                                                         |

Two issues came from Stellar's SDK team this quarter, and both were acted on but neither got a direct
reply. [#206](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/206) (the `useUpgradedAuth` flag)
was fixed 15 days after it was filed (2026-08-28).
[#207](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/207) (Protocol 28) is addressed by
[#252](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/252), merged 2026-10-02 and released in
16.0.0.

---

##### Non-deliverable 2: Capacity Buffer

The buffer, and more than the buffer, went to unplanned work, so SEP-30 (what an unused buffer would
have funded) was not started. About half of it fixed SDK features that did not work for users; the
rest tightened behaviour that mostly worked and could have waited for a later release:

- **Soroban RPC correctness (15 PRs).** Fixes for features that did not work: `authMode` sent in a
  form stellar-rpc rejects (a number in 14.x, upper case in 15.x), broken in every release since
  14.0.0 ([#209](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/209)); `getEvents` pagination
  silently dropped ([#219](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/219)); JSON-RPC errors
  swallowed ([#217](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/217),
  [#218](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/218)), which also closes the Q2
  carry-over [#197](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/197);
  `RestorePreamble.SorobanTransactionData` always throwing
  ([#222](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/222)); contract return values missing
  from V3 transaction metas ([#228](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/228)); and
  legitimate fees failing on the `MinResourceFee` type
  ([#221](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/221)). Stricter handling that could
  have waited: nullability, field presence and enum wire formats
  ([#220](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/220),
  [#225](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/225),
  [#234](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/234),
  [#235](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/235),
  [#236](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/236)), bounded converter exception
  messages ([#232](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/232)), and wire-format tests
  ([#216](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/216),
  [#233](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/233)). Most of the stricter items are
  breaking changes, so they also lengthen the 16.0.0 migration notes.
- **Protocol 27 follow-up:** the `useUpgradedAuth` flag (#209) and CAP-71 v2 credentials as the
  default ([#244](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/244)), as the proposal's
  "post-Mainnet-vote Protocol 27 follow-ups" anticipated.
- **Multi-target hardening after #195:** the Q2 JSON protections (`AllowDuplicateProperties = false`,
  `RespectNullableAnnotations`), which #195 had limited to `net10.0`, restored on all target
  frameworks ([#201](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/201)); post-review fixes to
  the Ed25519 signer, retry handler and date converters
  ([#202](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/202)); and NuGet Trusted Publishing for
  the release pipeline ([#203](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/203)), which
  16.0.0 is the first release to use.
- **Protocol 28 support:** [#252](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/252) (59 files,
  +3,414 / −75), covering CAP-85 external executable references and CAP-83, with byte-exact handling
  of binary executable tags, known-answer tests against `@stellar/stellar-sdk` 17.2.0, and two live
  Testnet tests.
- **XML doc-tag warnings (Q2 gap):** the 61 remaining doc warnings fixed, and every doc-tag warning
  now fails the build ([#254](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/254)).

**Protocol timeline**, with dates read from the first ledger of each protocol version:

| Protocol            | Testnet                                                           | Mainnet                                                    | On NuGet               |
| ------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------- | ---------------------- |
| 27 (CAP-71)         | [2026-06-18](https://horizon-testnet.stellar.org/ledgers/3157753) | [2026-07-08](https://horizon.stellar.org/ledgers/63386819) | 16.0.0 (2026-10-03)    |
| 28 (CAP-83, CAP-85) | [2026-08-27](https://horizon-testnet.stellar.org/ledgers/4365284) | [2026-09-16](https://horizon.stellar.org/ledgers/64458446) | 16.0.0 (2026-10-03)    |
| 29                  | [2026-09-29](https://horizon-testnet.stellar.org/ledgers/4935524) | [2026-10-01](https://horizon.stellar.org/ledgers/64717645) | 16.0.0 (no XDR change) |

Protocol 29 needs no SDK change: stellar-core
[v29.0.0](https://github.com/stellar/stellar-core/tree/v29.0.0-internal/src/protocol-curr) builds on
the same stellar-xdr commit
([`9c9c145`](https://github.com/stellar/stellar-xdr/commit/9c9c145953e80990d6ff1ae3a6a973a0ce6d0694))
as Protocol 28.

---

#### 2. Q2 carry-over and review: what was promised and what happened

| Q2 report or review said                                                                                                   | Outcome                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stable 16.0.0 ships early in Q3; the review accepted v16 as "staged, pending a small P27 compatibility fix"                | ✅ Completed. The P27 fix merged on 2026-08-28 (#209); 16.0.0 is released (2026-10-03) and available on NuGet                                                                                                                                                                                                                                                                             |
| `getLatestLedger` fields and matrix re-pins in [#198](https://github.com/Beans-BV/dotnet-stellar-sdk/pull/198) (in review) | ✅ Merged 2026-10-02, also adding the `getHealth` close times; both matrices pinned to v28.0.1 at 100% (Horizon 50/50, RPC 12/12)                                                                                                                                                                                                                                                         |
| Bug [#197](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/197) (RPC error-response mapping)                         | ✅ Fixed in #217                                                                                                                                                                                                                                                                                                                                                                          |
| Bug [#193](https://github.com/Beans-BV/dotnet-stellar-sdk/issues/193) (pagination drops auth and resilience config)        | ⏭️ Moved to Q4. Bug-fix time went first to the Soroban RPC client, where bugs broke calls outright: every `simulateTransaction` that set `authMode` failed, and `getEvents` could not page (11 bugs fixed, see Non-deliverable 2). #193 affects Horizon reads from page 2 onward (`NextPage()`/`PreviousPage()`): those requests drop the bearer token, default headers and retry policy. |
| Protocol 27 tracking issues #186 and #188 close with the stable release                                                    | ✅ Shipped in 16.0.0 and closed                                                                                                                                                                                                                                                                                                                                                           |
| Priority-2 integration tests move to Q3                                                                                    | ⏭️ Moved to Q4. These were not part of the Q3 proposal; the Q2 report had moved them here. The Q3 integration-test work went to the two protocol upgrades that reached the network this quarter: 4 new live Testnet tests for Protocol 27 (CAP-71 v2 auth) and Protocol 28 (CAP-85), taking the suite from 52 to 56.                                                                      |
| ~175 non-CS1591 warnings (doc-tag hygiene) remain                                                                          | ✅ Doc-tag warnings at 0 and gated (#254)                                                                                                                                                                                                                                                                                                                                                 |
| The multi-target work was "harder to verify for the reviewer as a non-.NET developer"                                      | Both Q3 deliverables can be checked without .NET: the matrices are plain tables, the MAUI report's §5 maps every commitment to a status, and the NuGet package lists its three target frameworks                                                                                                                                                                                          |

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

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3A.net_stellar_sdk&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3A.net_stellar_sdk)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3A.net_stellar_sdk&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3A.net_stellar_sdk)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3A.net_stellar_sdk&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3A.net_stellar_sdk)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3A.net_stellar_sdk&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3A.net_stellar_sdk)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
