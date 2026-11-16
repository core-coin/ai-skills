# CoreOZ: standard and upgradeable contracts

One card covers both CoreZeppelin libraries. The developer confirmed these as the current CoreOZ repositories; their public `main` heads matched the local source revisions below on 2026-11-15.

## Inspected repositories

### Standard contracts

- Repository: https://github.com/bchainhub/openzeppelin-contracts
- Research status: **source inspected**
- Inspection date: 2026-11-15
- Inspected branch: `main`
- Inspected commit: `672b803bebe64fbb2b122f8520dc1f08313530f0`
- README: no root README at this revision; use [`AGENTS.md`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/AGENTS.md), [`foxar.toml`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/foxar.toml), source, and tests

### Upgradeable contracts

- Repository: https://github.com/bchainhub/openzeppelin-contracts-upgradeable
- Research status: **source inspected**
- Inspection date: 2026-11-15
- Inspected branch: `main`
- Inspected commit: `42f9882a4e989274afaa40981e1ed884e1902154`
- README: no root README at this revision; use [`AGENTS.md`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/AGENTS.md), [`foxar.toml`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/foxar.toml), source, and tests

## Purpose and selection

Use CoreOZ for reusable Core contracts: token implementations, access control, signature helpers, and proxies. Use the standard library for constructor-based modules and the upgradeable library for implementation modules initialized through a proxy. Read the [Ylem card](../core-coin/ylem.md) for compiler, ABI, and storage assumptions.

Both repositories configure `src/`, `out/`, and `lib/` in `foxar.toml`, and keep ported tests under `test/`. Import the Core implementations under `src/`. The standard repository's `openzeppelin_contracts/` and `openzeppelin_tests/`, and the upgradeable repository's corresponding `_upgradeable` directories, are read-only upstream references. Preserve their relative structure when porting into `src/` and `test/`.

The upgradeable repository also carries `core_openzeppelin/` and `core_openzeppelin_tests/` as references to the standard Core port. Consult the matching Core implementation and tests before adapting a module to the upgradeable lifecycle.

## Modules and naming

| Task | Standard entry point | Upgradeable entry point |
| --- | --- | --- |
| Fungible tokens | [`src/token/CRC20/CRC20.sol`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/src/token/CRC20/CRC20.sol) | [`src/token/CRC20/CRC20Upgradeable.sol`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/src/token/CRC20/CRC20Upgradeable.sol) |
| Non-fungible tokens | [`src/token/CRC721/CRC721.sol`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/src/token/CRC721/CRC721.sol) | [`src/token/CRC721/CRC721Upgradeable.sol`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/src/token/CRC721/CRC721Upgradeable.sol) |
| ICAN helpers | [`src/utils/Checksum.sol`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/src/utils/Checksum.sol) | [`src/utils/ChecksumUpgradeable.sol`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/src/utils/ChecksumUpgradeable.sol) |
| Signature recovery | [`src/utils/cryptography/EDDSA.sol`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/src/utils/cryptography/EDDSA.sol) | [`src/utils/cryptography/EDDSAUpgradeable.sol`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/src/utils/cryptography/EDDSAUpgradeable.sol) |
| Typed-data domain and digest | [`src/utils/cryptography/EIP712.sol`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/src/utils/cryptography/EIP712.sol) | [`src/utils/cryptography/EIP712Upgradeable.sol`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/src/utils/cryptography/EIP712Upgradeable.sol) |
| EOA or contract-signature verification | [`src/utils/cryptography/SignatureChecker.sol`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/src/utils/cryptography/SignatureChecker.sol) | [`src/utils/cryptography/SignatureCheckerUpgradeable.sol`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/src/utils/cryptography/SignatureCheckerUpgradeable.sol) |
| Proxy upgrade slots and logic | [`src/proxy/ERC1967/ERC1967Upgrade.sol`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/src/proxy/ERC1967/ERC1967Upgrade.sol) | [`src/proxy/ERC1967/ERC1967UpgradeUpgradeable.sol`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/src/proxy/ERC1967/ERC1967UpgradeUpgradeable.sol) |

The Core ports use `CRC20`, `CRC721`, `SafeCRC20`, and `EDDSA`, with `Upgradeable` variants where supplied. Keep those names in new ported modules and tests. Names such as `EIP712`, `ERC1967`, and `IERC1271` remain in this codebase; do not apply a blanket ERC-to-CRC rename.

The inspected `src/` trees contain CRC20 and CRC721 implementations. CRC1155 is mentioned in porting guidance but has no implementation in these trees at the recorded revisions; a naming convention is not evidence of an available module.

## Addresses and zero values

Use `Checksum` / `ChecksumUpgradeable` for `toIcan(uint160)`, `isValid(address)`, and `zeroAddress()`. The underlying address format and native-call exceptions are in [ICAN rules](../../core-protocol.md#addresses-and-ican) and [precompile addresses](../../core-protocol.md#precompile-addresses). Apply ICAN helpers to ordinary accounts, not numeric precompile addresses.

For validations that require a nonzero account, reject both `address(0)` and the network-specific `Checksum.zeroAddress()` (or its upgradeable equivalent). For mint/burn `Transfer` events, use the real `address(0)` sentinel. See `_isZeroAddress`, `_mint`, and `_burn` in the CRC20 implementations linked above and [`test/utils/Checksum.t.sol`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/test/utils/Checksum.t.sol).

## Signature API

Use the [Core signature format](../../core-protocol.md#signatures-and-address-derivation) and [message/digest rules](../../core-protocol.md#message-and-typed-data-signing) when constructing inputs.

Both EDDSA libraries expose:

- `tryRecover(bytes32 hash, bytes memory signature)`: an internal `view` function returning `(address, RecoverError)`. It rejects a non-171-byte blob with `InvalidSignatureLength`; its bounded low-level call to precompile 1 maps failed recovery to `InvalidSignature`.
- `recover(bytes32 hash, bytes memory signature)`: an internal `view` function returning the recovered address or reverting with the corresponding EDDSA error string.
- `toCoreSignedMessageHash`, `toTypedDataHash`, and `toDataWithIntendedValidatorHash`: helpers for the selected signing construction. Choose the helper matching the caller's actual digest.

This describes the library wrapper's error handling. For a direct language builtin call, read [ecrecover behavior](../../core-protocol.md#ecrecover). Use `SignatureChecker.isValidSignatureNow` (or its upgradeable equivalent) when the signer may be a contract wallet; it includes an IERC1271 verification path.

Sources: the EDDSA and SignatureChecker implementations above, [`test/utils/cryptography/EDDSA.t.sol`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/test/utils/cryptography/EDDSA.t.sol), and [`test/utils/cryptography/EDDSAUpgradeable.t.sol`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/test/utils/cryptography/EDDSAUpgradeable.t.sol).

## Typed-data compatibility

Both `EIP712` and `EIP712Upgradeable` use this exact domain type:

```text
EIP712Domain(string name,string version,uint256 networkId,address verifyingContract)
```

The network value comes from `block.chainid`; the verifying contract is `address(this)`. Construct the application's struct hash and pass it to `_hashTypedDataV4`.

`EIP712Domain` is the correct Core domain name, confirmed by the developer and implemented in these libraries. In go-core, `SignerAPI.signTypedData` currently hashes a domain named `CIP712Domain`; this is an implementation error, not an alternative Core standard. See the [client signing implementation and compatibility note](../../core-protocol.md#message-and-typed-data-signing). The names produce different type hashes even with identical fields, so a client using the erroneous name produces a different digest. Use `EIP712Domain` for new integrations, match the complete fields and encoding, and handle existing incompatible callers explicitly. Do not silently change a deployed contract's domain.

For tests, build the digest expected by the contract and sign it directly using the [Foxar signature helpers](foxar.md#signature-tests-and-typed-data). Examples: [`test/utils/cryptography/EIP712.t.sol`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/test/utils/cryptography/EIP712.t.sol) and [`test/utils/cryptography/EIP712Upgradeable.t.sol`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/test/utils/cryptography/EIP712Upgradeable.t.sol).

## Proxy slots and selectors

CoreOZ uses Core SHA3-256-derived ERC1967 slots. The following values appear in both ERC1967 upgrade implementations linked above:

| Slot | Value |
| --- | --- |
| Implementation | `0x169aa7877a62aec264f92a4c78812101abc42f65cbb20781a5cb4084c2d639d7` |
| Admin | `0x5846d050da0e75d43b6055ae3cd6c2c65e1941ccb45afff84b891ff0c7a8e50e` |
| Beacon | `0x79d0e26f0ed6a26bf96d37944c615e11aedbfafe56e064339e13dad9525cda31` |
| Rollback | `0x9918ff29762f88fdc924c0a0ba5589b288a6baef366b4981f9a6f4309baada55` |

Use the [Core hashing rules](../../core-protocol.md#hashing) for new selectors and hash-derived constants. Prefer the compiler's `.selector` and `type(...).interfaceId` where applicable. Common selector values, checked with NIST SHA3-256, are:

| Signature | Selector |
| --- | --- |
| `admin()` | `0xeb8325fb` |
| `implementation()` | `0xf5d97006` |
| `isValidSignature(bytes32,bytes)` | `0x95f9a59b` |
| `supportsInterface(bytes4)` | `0x80ada41b` |

For existing proxies, preserve the deployed slot values and storage layout. The formula for a new constant does not authorize changing an existing deployment's layout. Inspect [`src/proxy/transparent/TransparentUpgradeableProxy.sol`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/src/proxy/transparent/TransparentUpgradeableProxy.sol), [`src/proxy/transparent/ProxyAdmin.sol`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/src/proxy/transparent/ProxyAdmin.sol), [`src/interfaces/IERC1271.sol`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/src/interfaces/IERC1271.sol), and [`test/proxy/ERC1967/ERC1967Proxy.t.sol`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/test/proxy/ERC1967/ERC1967Proxy.t.sol) when working on these interfaces.

## Upgradeable lifecycle

Use the upgradeable module's `__Module_init` functions from an initializer protected by `initializer`; handle parent initialization explicitly and avoid calling the same parent twice. Reserve `reinitializer(version)` for the intended later initialization step. For proxy implementation contracts, follow the project's `_disableInitializers()` constructor pattern to prevent direct initialization of the implementation. See [`src/proxy/utils/Initializable.sol`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/src/proxy/utils/Initializable.sol).

Preserve storage variable order, types, inheritance layout, and the modules' reserved `__gap` space. Compare storage layouts produced by the actual Ylem versions used for the old and new implementations before an upgrade; a similar upstream contract or class name does not establish layout compatibility.

For porting tests, reuse the standard Core test patterns from `core_openzeppelin_tests/`. This repository's proxy tests use helpers from `src/mocks/proxy/`; examples are [`test/proxy/ERC1967/ERC1967ProxyUpgradeable.t.sol`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/test/proxy/ERC1967/ERC1967ProxyUpgradeable.t.sol) and [`test/token/CRC20/CRC20Upgradeable.t.sol`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/test/token/CRC20/CRC20Upgradeable.t.sol). Use [Foxar account and signature helpers](foxar.md#signature-tests-and-typed-data) when constructing test signers.

## Toolchain and verification

Both libraries use Ylem and Foxar. Their project guidance targets `pragma solidity ^1.1.2`; some files pin `1.1.2` exactly. Resolve the declared `lib/spark-std` submodule and use the compiler accepted by the imported modules. See the standard [`.gitmodules`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/.gitmodules) and upgradeable [`.gitmodules`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/.gitmodules) files.

Run project builds and tests from the selected library root using the [Foxar workflow](foxar.md#contract-project-workflow). At these revisions, each repository's `ci.yml` selects Foxar release `1.0.9`, builds with `spark build --skip test` and rejects build warnings, runs `spark test -vvv`, and checks `spark fmt --check`. These are the libraries' CI settings, distinct from the Foxar CLI version inspected in its card.

Sources: standard [`CI`](https://github.com/bchainhub/openzeppelin-contracts/blob/672b803bebe64fbb2b122f8520dc1f08313530f0/.github/workflows/ci.yml) and upgradeable [`CI`](https://github.com/bchainhub/openzeppelin-contracts-upgradeable/blob/42f9882a4e989274afaa40981e1ed884e1902154/.github/workflows/ci.yml). Focus checks on the changed module, its error paths, signature digest compatibility, and initialization or proxy behavior where relevant.

Inspection used local source checkouts matching public `main` heads. No dependencies were installed, library builds or tests run, deployments performed, or transactions signed. Commands above were read from configuration and CI; they are not reported as successful runtime checks.
