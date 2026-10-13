---
title: "RefractorSpace"
canonical_id: daoip-5:scf:project:refractorspace
parent: Public Good Projects
proposal_issue: 38
proposer: orbitlens
category: "Governance Tools"
budget: "25,500"
---

# RefractorSpace

_Pending transactions storage and multisig aggregator for Stellar Network._

|                         |                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------- |
| **Category**            | Governance Tools                                                                                   |
| **Website**             | <https://refractor.space>                                                                          |
| **Repository**          | <https://github.com/stellar-expert/refractor>                                                      |
| **First Released**      | March 2021                                                                                         |
| **Intake**              | <https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io/issues/26> |
| **Budget Requested**    | 25,500                                                                                             |
| **Maintenance Reserve** | 2,000                                                                                              |
| **Other**               | 23,500                                                                                             |

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
services. There are 2 new integrations with DeFi services in progress, expected to go live in
Q3 2026. According to our logs, the service reached the SLA of 99.992% since the beginning of 2026.

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

## Proposed Impact

We aim to improve the website, documentation, provide relevant usage examples, and perform some
direct outreach to Stellar developers community to showcase how they can streamline their complex
multisig workflows using our service. This may significantly simplify life for any developers that
have to deal with multi-party controlled wallets, preauthorized transactions, or escrow services
backed by by Stellar.

## Proposed Deliverables

- Allow adding signatures for `SIGNER_KEY_TYPE_HASH_X` and `SIGNER_KEY_TYPE_ED25519` directly from
  the interface without wallet invocation ($1000)
- Add a preview block to the "Upload transaction" page. It should display extended transaction
  information before the transaction is uploaded and processed on the server side: whether all
  potential signer accounts exist on-chain, whether the transaction is valid, whether it has already
  been uploaded or executed, the expiration date and minimum execution date (if set), and the full
  list of signers. ($2000)
- In addition to pasting transaction XDR, allow uploading binary XDR files, as well as SEP-7 and
  Stellar Lab-formatted links. ($600)
- Add a new simulation interface that allows simulating signatures and checking whether a specific
  set of signatures allows submitting a transaction to the network. ($2000)
- Add a "Send test callback" function to the uploaded transaction so that users can check their
  server-side transaction handling code. ($1000)
- Add interfaces for uploading and processing (signing) Soroban auth entries separately from
  transactions. The interfaces will be significantly different, since an auth entry doesn't have
  timebounds, cannot contain some signer types (like HashX), and cannot be submitted to the network.
  The unique auth entry ID will be derived from the hash of its contents. ($7000)
- Display a detailed activity trail for a transaction: when it was uploaded to Refractor, when it was
  first signed, when the last signature was added, and when it was submitted to the network. ($3000)
- Provide a more user-friendly description of transaction contents so that signers understand exactly
  what they are signing: display the protocol name for known smart contract calls, highlight
  addresses that match signers (transfer to/from one of the signers), and mark potentially dangerous
  operations. Show a short summary of the transaction in the title instead of the hash. ($6000)
- Display decoded transaction submission results: ledger, fee charged, and per-operation result
  codes. ($500)
- Add a sharing widget to the transaction page with a QR code and a direct link to copy. ($200)
- Introduce additional transaction XDR actions: "Download", "Open in Stellar Lab". ($200)

**Maintenance Reserve: $2,000**. Covers hosting costs, protocol updates, and all on-going bug fixes.

## Metrics loaded from PG Atlas

[![PG Atlas](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Arefractorspace&query=%24.activity_status&label=PG+Atlas&color=914CFF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Arefractorspace)
[![90d Contributors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Arefractorspace&query=%24.active_contributors_90d&label=90d+Contributors&color=00B578)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Arefractorspace)
[![Pony Factor](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Arefractorspace&query=%24.pony_factor&label=Pony+Factor&color=0090FF)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Arefractorspace)
[![Adoption](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.pgatlas.xyz%2Fprojects%2Fdaoip-5%3Ascf%3Aproject%3Arefractorspace&query=%24.adoption_score&label=Adoption&color=FF9900)](https://www.pgatlas.xyz/projects/daoip-5%3Ascf%3Aproject%3Arefractorspace)

## Legal Acknowledgements

- [x] As the project representative, I agree to the Legal Acknowledgements.
