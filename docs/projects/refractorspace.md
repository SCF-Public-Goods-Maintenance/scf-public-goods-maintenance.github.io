---
title: "RefractorSpace"
canonical_id: daoip-5:scf:project:refractorspace
parent: Public Good Projects
proposal_issue: 38
proposer: orbitlens
category: "Governance Tools"
budget: "18,000"
---

# RefractorSpace

_Pending transactions storage and multisig aggregator for Stellar Network._

|                                |                                                                                                    |
| ------------------------------ | -------------------------------------------------------------------------------------------------- |
| **Category**                   | Governance Tools                                                                                   |
| **Website**                    | <https://refractor.space>                                                                          |
| **App Repository**             | <https://github.com/stellar-expert/refractor>                                                      |
| **SignerInspector Repository** | <https://github.com/stellar-expert/stellar-tx-signers-inspector>                                   |
| **First Released**             | March 2021                                                                                         |
| **Intake**                     | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/26> |
| **Budget Requested**           | 18,000                                                                                             |

## Project Description

Refractor is a pending transactions storage and multisig aggregator for Stellar Network.

It's a developer-focused service in the first place, but anyone can use it to store transactions and
gather signatures required to match the signing threshold. Users can explicitly set expiration date
and custom callback URL. Refractor automatically discovers potential signers and computes the
thresholds, ensuring that signatures are valid and consistent.

Other services and wallets can access and sign a transaction using a standard URL where its hash
serves as a unique identifier. The website displays current signing status, suitable signers, and
thresholds. Any eligible signer can sign the transaction. As soon as it reaches the required
threshold (calculated automatically), the service either submits the transaction to Stellar network
or executes a callback.

## Team & Experience

Refractor is maintained by the [StellarExpert team](https://stellar.expert/). We build infrastructure
tools on Stellar since 2016. Our notable projects: [StellarExpert](https://stellar.expert/),
[Reflector](https://reflector.network/), [StellarBroker](https://stellar.broker/),
[Albedo](https://albedo.link/), [LedgersTax](https://ledgers.tax/).

Active developers of the Refractor service:

- OrbitLens (GitHub profile: [orbitlens](https://github.com/orbitlens), Discord `@orbitlens`)
- HawthorneAbendsen (GitHub profile: [hawthorne-abendsen](https://github.com/hawthorne-abendsen),
  Discord `@hawthorne7187`)
- Yazadzhy (GitHub profile: [yazadzhy](https://github.com/yazadzhy))

## Retroactive Impact

Our service is actively used by Aquarius DAO, Reflector DAO, YieldBlox DAO, Stratum, and other
services. We have several new integrations. Currently discussing an option to add Refractor to the
dapp explorer with the Freighter team. According to our logs, the service reached the SLA of 99.994%
since the beginning of 2026.

## Past Deliverables

### 2026 Q2

- We revamped the website home page with a focus on key product features (available here:
  https://refractor.space)
- The webiste now highlights various usage scenarios and contains a simple step-by-step explanation
  of how it works.
- API infrastructure has been moved to a new dedicated server to provide more room for the database
  growth.
- Refractor now supports 6 new extension-based wallets in the signing interface: Bitget, ForDeFi,
  CactusLink, Hana, Klever, OneKey, Rabet.
- Server-side aggregator, website, and all dependency libs updated to support the upcoming Stellar
  protocol upgrade.

### 2026 Q3

- The automatic signer scheme detection algorithm has been reviewed and extended to fully account for
  Soroban transaction authorization entries, so the required signers for smart contract invocations
  are now identified correctly. Our signature scheme discovery algorithm has been reworked to analyze
  and aggregate signatures for Soroban authorization entries. It also autodetects authorization
  entries requirements inside transactions wrapped with FeeBumpTransaction.
- Signer detection now properly handles CAP-0071-01 (delegated authentication for custom accounts)
  and CAP-0071-02 (address-bound Soroban address credentials). Delegated authentication supports
  parsing of `SorobanAddressCredentialsWithDelegates` + `SOROBAN_CREDENTIALS_ADDRESS_V2` and
  recursive authentication resolution tree.
- The transaction analyzer follows ledger entry sponsorship changes and associated signature
  requirements. In addition, it produces warnings for invalid/malformed sponsorship transactions
  (missing EndSponsorshipOp, mismatched sponsorship recepient, etc).
- We added direct WalletConnect integration and reworked the signing UX to better support mobile
  wallets flow. Freighter and Albedo are available through direct shortcuts, other wallet that
  support WalletConnect can sign a transaction either through QR code scan or direct wc:// protocol
  link.

Incomplete deliverable:

- Allow adding signatures for `SIGNER_KEY_TYPE_HASH_X` and `SIGNER_KEY_TYPE_ED25519` directly from
  the interface without wallet invocation ($1000).

## Proposed Impact

We aim to improve the website, documentation, provide relevant usage examples, and perform some
direct outreach to Stellar developers community to showcase how they can streamline their complex
multisig workflows using our service. This may significantly simplify life for any developers that
have to deal with multi-party controlled wallets, preauthorized transactions, or escrow services
backed by by Stellar.

## Proposed Deliverables

- Review the automatic signer scheme detection algorithm to fully account for:
  - Soroban transaction authorization entries ($4000)
  - CAP-0071-01 (delegated authentication for custom accounts) ($2000)
  - CAP-0071-02 (address-bound Soroban address credentials, `SOROBAN_CREDENTIALS_ADDRESS_V2`) ($2000)
  - Ledger entry sponsorship changes ($1000)
- Allow adding signatures for `SIGNER_KEY_TYPE_HASH_X` and `SIGNER_KEY_TYPE_ED25519` directly from
  the interface without wallet invocation ($1000)
- Add ability to sign not only transactions, but also Soroban Auth entries ($6000)
- Improve signing flow on mobile devices ($2000)

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Arefractorspace&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Arefractorspace)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Arefractorspace&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Arefractorspace)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Arefractorspace&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Arefractorspace)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Arefractorspace&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Arefractorspace)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
