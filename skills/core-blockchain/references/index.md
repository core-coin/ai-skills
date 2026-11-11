# Repository index

Select the smallest set of references relevant to the task. These references capture inspected revisions; recheck current source before changing code.

Coverage: **88 repository identities**: 85 inspected source trees, 2 user-supplied READMEs without source access, and 1 inaccessible repository. See [research status](research-status.md).

## Routing guide

- Client consensus and compatibility: start with [`go-core`](repositories/core-coin/go-core.md), then [protocol and compatibility](protocol-and-compatibility.md).
- Dart transaction signing or wallet integration: inspect [`core_web3dart`](repositories/CorePass/core_web3dart.md) and [`flutter_ed448`](repositories/CorePass/flutter_ed448.md).
- Air-gapped animated QR transport: inspect the [`flutter_barcodetx`](repositories/DataLayerHost/flutter_barcodetx.md) encoder and the desktop [`ScanBarcode`](repositories/DataLayerHost/ScanBarcode.md) receiver. Check deeplink handoff and update behavior before assuming the receiving device stays offline.
- Mining: inspect [`RandomY`](repositories/core-coin/RandomY.md), [`coreminer`](repositories/catchthatrabbit/coreminer.md), and [`pool`](repositories/catchthatrabbit/pool.md) as the task requires.
- Contracts: start with [`ylem`](repositories/core-coin/ylem.md), [`cvm`](repositories/core-coin/cvm.md), and the relevant ABI or framework reference.
- Standards and proposals: use [`cip`](repositories/core-coin/cip.md) and its compact `llms.txt` index, then inspect the individual proposal and current implementation.
- Fee-splitting contracts: inspect [`ylem-splitting`](repositories/core-laboratories/ylem-splitting.md). The user-supplied [Contract Deployer README](contract-deployer.md) describes a local deployment GUI without a repository identity.

## Repositories

### Client, protocol, and compatibility

| Repository | Platform | Research |
| --- | --- | --- |
| [core-coin/go-core](repositories/core-coin/go-core.md) | Go | Source inspected |
| [core-coin/cip](repositories/core-coin/cip.md) | TypeScript / Docusaurus | Source inspected |
| [core-coin/cvm](repositories/core-coin/cvm.md) | Rust | Source inspected |
| [core-coin/rlp](repositories/core-coin/rlp.md) | Rust | Source inspected |
| [core-coin/hive](repositories/core-coin/hive.md) | Go | Source inspected |
| [core-coin/core-diff](repositories/core-coin/core-diff.md) | Not verified | Source inspected |
| [core-coin/core-common](repositories/core-coin/core-common.md) | Rust | Source inspected |
| [core-coin/uint256](repositories/core-coin/uint256.md) | Go | Source inspected |
| [core-coin/renaming-table](repositories/core-coin/renaming-table.md) | Go | Source inspected |

### Mining and proof of work

| Repository | Platform | Research |
| --- | --- | --- |
| [core-coin/go-randomy](repositories/core-coin/go-randomy.md) | Go | Source inspected |
| [core-coin/RandomY](repositories/core-coin/RandomY.md) | C / C++ | Source inspected |
| [core-coin/randomy-rs](repositories/core-coin/randomy-rs.md) | Rust | Source inspected |
| [catchthatrabbit/coreminer](repositories/catchthatrabbit/coreminer.md) | C / C++ | Source inspected |
| [catchthatrabbit/pool](repositories/catchthatrabbit/pool.md) | Go, JavaScript / TypeScript | Source inspected |

### Cryptography, keys, and addresses

| Repository | Platform | Research |
| --- | --- | --- |
| [core-coin/go-goldilocks](repositories/core-coin/go-goldilocks.md) | Go | Source inspected |
| [core-coin/ed448-rs](repositories/core-coin/ed448-rs.md) | Rust | Source inspected |
| [core-coin/ed448](repositories/core-coin/ed448.md) | Go | Source inspected |
| [core-coin/base-rs](repositories/core-coin/base-rs.md) | Rust | Source inspected |
| [core-coin/atoms-rs](repositories/core-coin/atoms-rs.md) | Rust | Source inspected |
| [core-coin/xcb-keystore-rs](repositories/core-coin/xcb-keystore-rs.md) | Rust | Source inspected |
| [core-coin/libgoldilocks](repositories/core-coin/libgoldilocks.md) | C, Python | Source inspected |
| [core-coin/gofortuna](repositories/core-coin/gofortuna.md) | Go | Source inspected |
| [CorePass/flutter_ed448](repositories/CorePass/flutter_ed448.md) | Dart / Flutter | Source inspected |
| [bchainhub/flutter_wallet_validator](repositories/bchainhub/flutter_wallet_validator.md) | Dart / Flutter | Source inspected |
| [bchainhub/ican.js](repositories/bchainhub/ican.js.md) | JavaScript / TypeScript | Source inspected |
| [bchainhub/blo](repositories/bchainhub/blo.md) | JavaScript / TypeScript | Source inspected |

### Contracts and developer tooling

| Repository | Platform | Research |
| --- | --- | --- |
| [core-coin/ylem](repositories/core-coin/ylem.md) | C / C++ | Source inspected |
| [core-coin/corebc-rs](repositories/core-coin/corebc-rs.md) | Rust | Source inspected |
| [core-coin/geas](repositories/core-coin/geas.md) | Go | Source inspected |
| [core-coin/yvm-rs](repositories/core-coin/yvm-rs.md) | Rust | Source inspected |
| [core-coin/coreabi](repositories/core-coin/coreabi.md) | Rust | Source inspected |
| [core-coin/ylem-bins](repositories/core-coin/ylem-bins.md) | Not verified | Source inspected |
| [bchainhub/foxar](repositories/bchainhub/foxar.md) | Rust | Source inspected |
| [bchainhub/CoreOpenZeppelin](repositories/bchainhub/CoreOpenZeppelin.md) | JavaScript / TypeScript | Source inspected |
| [bchainhub/spark-std](repositories/bchainhub/spark-std.md) | JavaScript / TypeScript | Source inspected |
| [bchainhub/ds-test](repositories/bchainhub/ds-test.md) | JavaScript / TypeScript | Source inspected |
| [bchainhub/foxar-docs](repositories/bchainhub/foxar-docs.md) | JavaScript / TypeScript | Source inspected |
| [bchainhub/spark-template](repositories/bchainhub/spark-template.md) | Solidity | Source inspected |
| [core-laboratories/ylem-splitting](repositories/core-laboratories/ylem-splitting.md) | Solidity / Foxar | Source inspected; no README |
| [core-laboratories/remix](repositories/core-laboratories/remix.md) | Not verified | Inaccessible |

### Wallets, SDKs, payments, and transport

| Repository | Platform | Research |
| --- | --- | --- |
| [core-coin/core-cli](repositories/core-coin/core-cli.md) | Rust | Source inspected |
| [core-coin/pigeon](repositories/core-coin/pigeon.md) | Go | Source inspected |
| [core-coin/Xcb.Net](repositories/core-coin/Xcb.Net.md) | C# / .NET | Source inspected |
| [core-coin/wallet-generator](repositories/core-coin/wallet-generator.md) | Go | Source inspected |
| [core-coin/core-denomination](repositories/core-coin/core-denomination.md) | Not verified | Source inspected |
| [CorePass/corebc.js](repositories/CorePass/corebc.js.md) | JavaScript / TypeScript | Source inspected |
| [CorePass/core_web3dart](repositories/CorePass/core_web3dart.md) | Dart / Flutter | Source inspected |
| [bchainhub/flutter_paytorl](repositories/bchainhub/flutter_paytorl.md) | Dart / Flutter | Source inspected |
| [bchainhub/payto-rl](repositories/bchainhub/payto-rl.md) | JavaScript / TypeScript | Source inspected |
| [bchainhub/flutter_connect](repositories/bchainhub/flutter_connect.md) | Dart / Flutter | Source inspected |
| [bchainhub/better-connect](repositories/bchainhub/better-connect.md) | JavaScript / TypeScript | Source inspected |
| [bchainhub/connect.js](repositories/bchainhub/connect.js.md) | JavaScript / TypeScript | Source inspected |
| [bchainhub/flutter_txms](repositories/bchainhub/flutter_txms.md) | Dart / Flutter | Source inspected |
| [bchainhub/txms.js](repositories/bchainhub/txms.js.md) | JavaScript / TypeScript | Source inspected |
| [bchainhub/exchange-rounding](repositories/bchainhub/exchange-rounding.md) | JavaScript / TypeScript | Source inspected |
| [bchainhub/core-units](repositories/bchainhub/core-units.md) | JavaScript / TypeScript | Source inspected |
| [DataLayerHost/kamailio-txms](repositories/DataLayerHost/kamailio-txms.md) | C / C++ | Source inspected |
| [DataLayerHost/libtxms](repositories/DataLayerHost/libtxms.md) | C / C++ | Source inspected |
| [DataLayerHost/luna-sdk](repositories/DataLayerHost/luna-sdk.md) | JavaScript / TypeScript | Source inspected |
| [DataLayerHost/luna_sdk](repositories/DataLayerHost/luna_sdk.md) | Dart / Flutter | Source inspected |
| [DataLayerHost/flutter_modem](repositories/DataLayerHost/flutter_modem.md) | Dart / Flutter | Source inspected |
| [DataLayerHost/flutter_barcodetx](repositories/DataLayerHost/flutter_barcodetx.md) | Dart / Flutter | Source inspected |
| [DataLayerHost/ScanBarcode](repositories/DataLayerHost/ScanBarcode.md) | Rust / desktop | Source inspected |
| [DataLayerHost/txms-server](repositories/DataLayerHost/txms-server.md) | JavaScript / TypeScript | Source inspected |
| [DataLayerHost/bchauth](repositories/DataLayerHost/bchauth.md) | Go | Source inspected |
| [core-laboratories/payto](repositories/core-laboratories/payto.md) | JavaScript / TypeScript | Source inspected |
| [core-laboratories/compact_money](repositories/core-laboratories/compact_money.md) | Dart / Flutter | Source inspected |
| [core-laboratories/compact-money](repositories/core-laboratories/compact-money.md) | JavaScript / TypeScript | Source inspected |
| [core-laboratories/paytoonl-web](repositories/core-laboratories/paytoonl-web.md) | JavaScript / TypeScript | Source inspected |
| [core-laboratories/payto-map](repositories/core-laboratories/payto-map.md) | JavaScript / TypeScript | Source inspected |

### APIs, services, and indexing

| Repository | Platform | Research |
| --- | --- | --- |
| [core-coin/nuntiare](repositories/core-coin/nuntiare.md) | Go | Source inspected |
| [core-coin/core-etl](repositories/core-coin/core-etl.md) | Rust | Source inspected |
| [core-coin/oracle-checksum](repositories/core-coin/oracle-checksum.md) | Go | Source inspected |
| [core-coin/energy-forecast](repositories/core-coin/energy-forecast.md) | Go | Source inspected |
| [core-coin/faucet](repositories/core-coin/faucet.md) | Go, JavaScript / TypeScript | Source inspected |
| [core-coin/core-api](repositories/core-coin/core-api.md) | Not verified | Source inspected |
| [bchainhub/blockbook](repositories/bchainhub/blockbook.md) | Go | Source inspected |
| [bchainhub/well-known](repositories/bchainhub/well-known.md) | JavaScript / TypeScript | Source inspected |
| [bchainhub/gocore-mainnet-alloc-decode](repositories/bchainhub/gocore-mainnet-alloc-decode.md) | Go | Source inspected |
| [core-laboratories/oric](repositories/core-laboratories/oric.md) | Hono / JavaScript (README supplied) | README supplied; source inaccessible |

### Deployment, packaging, and distribution

| Repository | Platform | Research |
| --- | --- | --- |
| [core-coin/gocore-chocolatey](repositories/core-coin/gocore-chocolatey.md) | Not verified | Source inspected |
| [core-coin/core-playbook](repositories/core-coin/core-playbook.md) | Shell | Source inspected |
| [core-coin/homebrew-gocore](repositories/core-coin/homebrew-gocore.md) | Not verified | Source inspected |
| [core-coin/homebrew-ylem](repositories/core-coin/homebrew-ylem.md) | Not verified | Source inspected |
| [core-coin/helm-core](repositories/core-coin/helm-core.md) | Shell | Source inspected |
| [bchainhub/corecdn](repositories/bchainhub/corecdn.md) | Python, Shell | Source inspected |
| [bchainhub/core-license](repositories/bchainhub/core-license.md) | Not verified | Source inspected |
| [core-laboratories/ipfs-worker](repositories/core-laboratories/ipfs-worker.md) | Cloudflare Worker (README supplied) | README supplied; source inaccessible |
