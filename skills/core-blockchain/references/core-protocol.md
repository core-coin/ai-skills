# Core protocol

Use this reference for Core addresses, HD wallet derivation, hashing, signatures, transactions, CVM execution, precompile calls, and consensus. The rules below describe the inspected [`go-core` client](repositories/core-coin/go-core.md), the behavioral reference for the existing network. Check the target implementation and revision before applying them to another client or SDK; the separate Rust [`cvm`](repositories/core-coin/cvm.md) project is not the Go interpreter. See [protocol and compatibility](protocol-and-compatibility.md) for modernization goals and cross-client compatibility work.

Read the sections relevant to the task:

- [Fork baseline](#fork-baseline), [addresses and ICAN](#addresses-and-ican), and [HD wallet derivation](#hd-wallet-derivation).
- [Hashing](#hashing): ABI selectors, event IDs, tries, and contract creation.
- [Signatures and address derivation](#signatures-and-address-derivation), including [messages and typed data](#message-and-typed-data-signing).
- [Transactions](#transactions): wire encoding, signing hash, replay protection, and pool limits.
- [CVM execution](#cvm-execution), [precompile addresses](#precompile-addresses), and [ecrecover](#ecrecover).
- [Consensus](#consensus): proof of work, difficulty, rewards, and block parameters.

## Fork baseline

Core derives from pre-Merge Ethereum, specifically **Go Ethereum (Geth) v1.9.12 stable**, forked at commit [`b6f1c8dcc058a936955eb8e5766e2962218924bc`](https://github.com/ethereum/go-ethereum/commit/b6f1c8dcc058a936955eb8e5766e2962218924bc) (`params: release Geth v1.9.12`). This corresponds to the **Istanbul / Muir Glacier** protocol stage, before Berlin, London, and Paris. Inspect current Core sources for subsequent changes and backports before assuming which Ethereum rules apply.

## Addresses and ICAN

- Core account addresses are **22 bytes**: one network-prefix byte, one checksum byte, and a 20-byte account identifier. The hexadecimal network prefixes are `cb` for mainnet, `ab` for Devin, and `ce` for private networks.
- Normal ICAN validation checks the network prefix and the mod-97-derived checksum. Preserve the full address width when encoding addresses for contracts or clients.
- In `go-core`, `VerifyAddress` deliberately bypasses both checks for the zero-padded numeric addresses **0 through 9** and the specific `DevAddress` constant. This is an explicit allowlist, not a general exemption for arbitrary addresses. The active precompile set is narrower: see [precompile addresses](#precompile-addresses).

Source: [`common/types.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/common/types.go), particularly `AddressLength`, `CalculateChecksum`, `VerifyAddress`, and `NetworkID`.

### HD wallet derivation

Core uses **coin type 654** in its HD wallet path convention: the hardened component is `654'` (`0x8000028e`). This is a wallet compatibility setting, separate from the network ID and ICAN network prefix.

At the recorded go-core revision:

| Purpose | Path |
| --- | --- |
| `DefaultRootDerivationPath` | `m/44'/654'/0'/0` |
| `DefaultBaseDerivationPath` (first address) | `m/44'/654'/0'/0/0` |
| Address index `i` under that root | `m/44'/654'/0'/0/i` |

An apostrophe marks a hardened component. `ParseDerivationPath("0")` appends index 0 to the default root; `DefaultIterator(DefaultBaseDerivationPath)` increments the final address index. Distinguish the root from a complete address path.

When restoring a wallet or matching accounts across implementations, preserve the full path, hardening, account/index selection, mnemonic-to-seed processing, passphrase, and the backend's Ed448 derivation scheme. Coin type alone does not establish compatibility. Preserve an existing wallet's actual path rather than silently replacing it with a default.

These path definitions do not establish HD support in every wallet backend: go-core's plain keystore wallet returns `ErrNotSupported` from `Derive`. Check the target implementation before offering mnemonic recovery or derived-account selection.

Sources: `DefaultRootDerivationPath`, `DefaultBaseDerivationPath`, `ParseDerivationPath`, and `DefaultIterator` in [`accounts/hd.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/accounts/hd.go), path examples in [`accounts/hd_test.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/accounts/hd_test.go), and backend support in [`accounts/keystore/wallet.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/accounts/keystore/wallet.go).

This records Core's implemented convention, not a claim of current SLIP-0044 registration. The [registry snapshot checked on 2026-11-15](https://github.com/satoshilabs/slips/blob/7a2abdd1e823f5180e0997434250eda88b57cb75/slip-0044.md) assigns 654 to USDG; the assignment comment in `accounts/hd.go` does not match that registry.

## Hashing

Core uses **NIST SHA3-256** for the operations below; Ethereum's Keccak-256 produces different results. In the formulas in this reference, `H` means NIST SHA3-256 and `||` means byte concatenation.

| Operation | Core behavior |
| --- | --- |
| ABI function selector | First four bytes of `H(canonicalFunctionSignature)` |
| Event signature ID | `H(canonicalEventSignature)`; topic 0 for non-anonymous events |
| Block and transaction IDs | `H(RLP(header))` and `H(RLP(signedTransaction))`; preserve Core's fields and their order |
| Tries and log blooms | Trie node hashing, secure-trie key hashing, and bloom bit selection use SHA3-256 |
| Account addresses | See [public-key address derivation](#signatures-and-address-derivation) |

Contract creation derives a 20-byte account identifier, then adds the network prefix and checksum:

```text
CREATE:  last20(H(RLP([sender, nonce])))
CREATE2: last20(H(0xff || sender || salt32 || H(init_code)))
```

`sender` is the full **22-byte** Core address in both formulas. Recompute selectors, event IDs, and application hash-derived constants with Core hashing and encoding. Preserve explicit protocol constants such as `EmptyRootHash` / `emptyRoot` from the client: switching the hash function does not authorize recomputing historical constants.

Sources: [`crypto/crypto.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/crypto/crypto.go), [`accounts/abi/method.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/accounts/abi/method.go), [`accounts/abi/event.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/accounts/abi/event.go), [`core/types/block.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/types/block.go), [`core/types/bloom9.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/types/bloom9.go), [`trie/hasher.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/trie/hasher.go), [`trie/secure_trie.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/trie/secure_trie.go), [`trie/trie.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/trie/trie.go), and [`core/vm/cvm.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/vm/cvm.go).

## Signatures and address derivation

Core uses **Ed448**. In `go-core`, private and public keys are each **57 bytes**, and the cryptographic signature is **114 bytes**. The Core recoverable signature is **171 bytes**, with this layout:

```text
Ed448 signature (114 bytes) || public key (57 bytes)
```

The public key is carried in the signature blob. Recovery verifies the signature against the supplied digest and that public key, then derives the account identifier from the last 20 bytes of the public key's **NIST SHA3-256** hash. The network prefix and checksum produce the full [ICAN address](#addresses-and-ican). Do not substitute Ethereum's `V/R/S` representation or Keccak-256. Distinguish a library's raw Ed448 signature from Core's extended signature when integrating cryptographic libraries.

Sources: [`crypto/crypto.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/crypto/crypto.go), [`crypto/signature_cgo.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/crypto/signature_cgo.go), and [`crypto/signature_nocgo.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/crypto/signature_nocgo.go).

### Message and typed-data signing

The `personal_sign` / `xcb_sign` text-signing path hashes the decoded message bytes with the Core domain prefix:

```text
messageDigest = H("\x19Core Signed Message:\n" || decimalByteLength(message) || message)
```

The length is an ASCII decimal count of **bytes**, not Unicode characters or hexadecimal digits. Signing a 32-byte digest through this path uses `"\x19Core Signed Message:\n32" || digest`; it adds a new hashing layer. Signing the digest directly is a different operation.

The correct Core typed-data domain name is **`EIP712Domain`**, with **`networkId`**, as confirmed by the developer and implemented in [CoreOZ](repositories/bchainhub/CoreOpenZeppelin.md#typed-data-compatibility). Use the exact domain fields and order required by the verifying contract. The final digest is:

```text
typedDataDigest = H(0x19 || 0x01 || domainSeparator || structHash)
```

The type, domain, and struct hashing also use NIST SHA3-256. Address values occupy a 32-byte word containing the full 22-byte Core address, left-padded with zeros. Match the domain type, field names, and encoding on both sides; Ethereum `chainId`-based digests are not interchangeable with Core `networkId`-based digests. Sign the typed-data digest directly without the signed-message prefix. Both paths use the [same Core signature blob](#signatures-and-address-derivation); transaction signing has its own [digest construction](#transactions).

**Implementation error in go-core:** at the recorded commit, `SignerAPI.signTypedData` in `signer/core/signed_data.go` calls `HashStruct("CIP712Domain", ...)`. The developer confirmed that `CIP712Domain` is erroneous; it is not another valid Core domain name. The type name participates in the hash, so this path produces a different digest from an otherwise identical `EIP712Domain`. Its `TypedDataDomain` supports `name`, `version`, `networkId`, `verifyingContract`, and `salt`, with encoded fields determined by the supplied type definition. Account for the mismatch when using this client API; do not propagate the erroneous name into new contracts or signing helpers.

Sources: `TextAndHash` in [`accounts/accounts.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/accounts/accounts.go), `SignText` / `SignTextWithPassphrase` in [`accounts/keystore/wallet.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/accounts/keystore/wallet.go), signing RPCs in [`internal/xcbapi/api.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/internal/xcbapi/api.go), and `TypedDataDomain`, `signTypedData`, `HashStruct`, and `EncodePrimitiveValue` in [`signer/core/signed_data.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/signer/core/signed_data.go).

## Transactions

The inspected client encodes a signed transaction as this RLP list:

```text
[nonce, energyPrice, energyLimit, networkId, to, value, input, signature]
```

The signature is the [171-byte Core blob](#signatures-and-address-derivation), replacing Ethereum's `V`, `R`, and `S`. An absent recipient (`nil`, encoded as an empty RLP string) means contract creation. A present `to` is a full 22-byte address and passes through `VerifyAddress`, including its [explicit exceptions](#addresses-and-ican). Sending to the zero address is not the contract-creation encoding.

The **signing hash has a different field order**: `networkId` is last, and the signature is excluded.

```text
signingHash = H(RLP([nonce, energyPrice, energyLimit, to, value, input, networkId]))
transactionHash = H(RLP(signedTransaction))
```

`SignTx` sets the network ID from the signer before hashing. Sender recovery validates it for replay protection. Mainnet uses **1** and Devin **3**; ID **2** is reserved and invalid. Preserve the exact historical exception keyed by `params.ZeroNetworkIDTxHash` when reproducing client behavior; do not generalize it into accepting arbitrary mismatched network IDs.

Use the target API's actual field names: `txdata` JSON and transaction RPC structs use `network_id`, `energy`, and `energyPrice`, while chain configuration and typed-data domains use `networkId`. Do not infer JSON spelling or RLP order from SDK property names, or substitute Ethereum EIP-155 signature packing or typed transaction envelopes.

The transaction pool rejects RLP-encoded transactions **larger than 128 KiB** (`txMaxSize`). This is a pool admission limit, not evidence of a consensus-wide transaction-size rule. Keep pool policy separate from block execution and [contract runtime code limits](#cvm-execution).

Sources: `txdata`, `EncodeRLP`, and `Hash` in [`core/types/transaction.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/types/transaction.go), `NucleusSigner` and `SignTx` in [`core/types/transaction_signing.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/types/transaction_signing.go), [`core/tx_pool.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/tx_pool.go), [`params/config.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/params/config.go), [`common/types.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/common/types.go), and [`internal/xcbapi/api.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/internal/xcbapi/api.go).

## CVM execution

- Execution inherits the Istanbul baseline, including EIP-2200-style storage metering. `go-core` does not activate Berlin, London, or Paris as complete Ethereum fork rule sets. Its `ChainConfig` has no corresponding activation schedule. Later individual changes and backports still exist; use the actual instruction table and energy rules for compatibility work.
- Use Core terminology: **CVM**, **energy**, and **networkId**. Contract calls and estimates are exposed through `xcb_call` and `xcb_estimateEnergy`.
- The `SHA3` instruction computes **NIST SHA3-256**. Ethereum Keccak-256 results are not interchangeable with it. Precompile No. 2 remains SHA-256; it is a different operation.
- Opcode `0x46` is `NETWORKID`. The default instruction table includes `BEGINSUB` (`0x5c`), `RETURNSUB` (`0x5d`), and `JUMPSUB` (`0x5e`). Do not infer supported instructions from a modern Ethereum fork name.
- The maximum deployed contract code size is **50,000 bytes**. This is the runtime bytecode returned by contract creation, not the source-file or transaction size.

Sources: [`params/config.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/params/config.go), [`params/protocol_params.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/params/protocol_params.go), [`core/vm/interpreter.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/vm/interpreter.go), [`core/vm/jump_table.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/vm/jump_table.go), [`core/vm/instructions.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/vm/instructions.go), [`core/vm/energy_table.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/vm/energy_table.go), and [`internal/xcbapi/api.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/internal/xcbapi/api.go).

## Precompile addresses

The inspected `go-core` registers these native contracts:

| Numeric address | Operation |
| --- | --- |
| `1` | Core Ed448 address recovery (`ecrecover`) |
| `2` | SHA-256 |
| `3` | RIPEMD-160 |
| `4` | Identity / data copy |
| `5` | Modular exponentiation |
| `6` | bn256 point addition |
| `7` | bn256 scalar multiplication |
| `8` | bn256 pairing check |
| `9` | BLAKE2F compression |

Each entry is a **22-byte, zero-padded numeric address**, as constructed by `common.BytesToAddress([]byte{n})`. Do not add an ICAN network prefix or checksum to these values: that produces a different address and will not select the registered precompile. Address 0 and `DevAddress` have [validation exceptions](#addresses-and-ican) but are not entries in this precompile table.

Sources: `PrecompiledContracts` in [`core/vm/contracts.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/vm/contracts.go) and dispatch in [`core/vm/cvm.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/vm/cvm.go).

### ecrecover

The Ylem builtin has this signature and calls precompile No. 1:

```solidity
ecrecover(bytes32 hash, bytes memory signature) returns (address)
```

`signature` uses the [Core signature format](#signatures-and-address-derivation). The precompile verifies it against `hash` and returns the corresponding Core address. The native return value is the address left-padded to a 32-byte word.

A signature-verification error is an execution failure, not `ErrExecutionReverted` (`REVERT`). The CVM call consumes all energy forwarded to that invocation and returns no unused energy. Low-level `CALL` or `STATICCALL` reports failure, which the caller can handle; it does not automatically revert the whole transaction. A higher-level wrapper may propagate the failure.

The **63/64 rule limits forwarded energy**, rather than imposing a fixed burn on every failure. After the call's base costs, the forwarding cap is `available - floor(available / 64)`. If the caller explicitly forwards a smaller budget, that budget is consumed on failure. Do not describe this as always burning 63/64 of the transaction's total energy.

Sources: `ecrecover.Run` in [`core/vm/contracts.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/vm/contracts.go), call error handling in [`core/vm/cvm.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/vm/cvm.go), forwarding in [`core/vm/energy.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/vm/energy.go), and the builtin declaration in Ylem's [`libsolidity/analysis/GlobalContext.cpp`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/libsolidity/analysis/GlobalContext.cpp).

## Consensus

Mainnet and Devin select **Cryptore proof of work**. At the inspected revision, seal verification calls **RandomY** through `go-randomy`; Ethereum Ethash/DAG assumptions do not apply. For the underlying implementation and bindings, use the [RandomY](repositories/core-coin/RandomY.md) and [go-randomy](repositories/core-coin/go-randomy.md) references and check the dependency version.

- The Core header has a nonce and **no `mixDigest` field**. `Cryptore.SealHash` hashes the RLP header fields excluding the nonce using NIST SHA3-256. RandomY receives that seal hash and the nonce; its result must be at most `floor(2^256 / difficulty)`. The full [block hash](#hashing) includes the nonce and is distinct from the seal hash and RandomY result.
- Difficulty uses Core's implemented adjustment below, with **no difficulty bomb** or Ethereum fork-dependent reward/difficulty schedule.
- The base block reward is **5 CORE** (`5 × 10^18` ore), with at most **two uncles** per block. For a valid included uncle at height `u` in a block at height `n`, its reward is `(u + 8 - n) × baseReward / 8`; the including miner receives an additional `baseReward / 32` per uncle. The inspected reward function has no halving schedule.
- A block timestamp must exceed its parent's. Ordinary header verification allows up to **8 seconds** ahead of the local clock; uncle validation has its own path.
- Default mainnet mining targets are an energy floor of **12,500,000** and ceiling of **14,700,000**. These configurable targets do not establish a fixed consensus ceiling: validation checks the header limit against its parent and the protocol bounds.

For exact difficulty calculations, let `D` be the parent difficulty, `dt` the positive timestamp difference in seconds, and `U` be 1 if the parent has no uncles, otherwise 2:

```text
adjustment = max(U - floor(dt / 5), -99)
nextDifficulty = max(8192, D + floor(D / 2048) * adjustment)
```

The developer reference describes a 6-second target and `params.DurationLimit` is 6, but the active calculation divides by **5** and does not read `DurationLimit`. Preserve the implemented formula for compatibility; derive neither the divisor nor a fixed block interval from that target or inherited comments.

Sources: `verifyHeader`, `makeDifficultyCalculator`, `verifySeal`, `SealHash`, and `accumulateRewards` in [`consensus/cryptore/consensus.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/consensus/cryptore/consensus.go), header fields in [`core/types/block.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/core/types/block.go), [`params/config.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/params/config.go), [`params/protocol_params.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/params/protocol_params.go), [`params/denomination.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/params/denomination.go), mining defaults in [`xcb/config.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/xcb/config.go), and the dependency in [`go.mod`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/go.mod).

## Evidence

The fork origin was supplied in the developer's `go-core` reference. On **2026-11-15**, the release version and upstream fork configuration were checked in [`params/version.go`](https://github.com/ethereum/go-ethereum/blob/b6f1c8dcc058a936955eb8e5766e2962218924bc/params/version.go) and [`params/config.go`](https://github.com/ethereum/go-ethereum/blob/b6f1c8dcc058a936955eb8e5766e2962218924bc/params/config.go) at the fork commit. Git ancestry was verified against the client revision below.

The Core-specific sections were selected from the developer's `go-core` reference and checked against the source files linked above:

| Source | Local branch inspected | Commit | Scope |
| --- | --- | --- | --- |
| `core-coin/go-core` | `audit` | `a091fe2d31ea1d3926db64da7621f26ed01c92a9` | Addresses and HD wallet paths, hashing, signatures and typed data, transaction encoding and pool limits, CVM, precompiles, and consensus |
| `core-coin/ylem` | `fix/version` | `eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7` | `ecrecover` builtin declaration and call generation |

This protocol inspection and the later Ylem/CoreOZ card updates are recorded in [research status](research-status.md). The correct typed-data domain name was confirmed by the developer during the 2026-11-15 follow-up; the client implementation error is explicitly distinguished from that requirement. No client or compiler builds, tests, or CVM execution checks were performed; separate compiler CLI inspection is recorded in the [Ylem card](repositories/core-coin/ylem.md#inspection-scope).
