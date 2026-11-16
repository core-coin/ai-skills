# Research status

Repository survey dated **2026-11-11**. A successful clone or source read is not a configured development environment. No dependencies were installed, builds or tests executed, or runtimes verified during this pass. Public repositories were read from partial Git checkouts; accessible private repositories were read through the connected GitHub tool. The user supplied READMEs for two repositories whose source remained inaccessible. A third new repository remained inaccessible without a supplied README. The Contract Deployer note is based on an attached README without a repository identity and is tracked separately. The table below records the latest inspected revisions, including the dated follow-ups.

On **2026-11-15**, the [Core protocol reference](core-protocol.md) was added and expanded with addresses, hashing, signatures and typed data, transaction encoding and replay protection, CVM rules, precompile behavior, and consensus selected from the developer's `go-core` guidance. The fork origin and these implementation details were checked in local `go-core` source and history at commit `a091fe2d31ea1d3926db64da7621f26ed01c92a9` (local branch `audit`). The reference distinguishes transaction wire order from signing-hash order, pool admission policy from consensus, and the implemented difficulty formula from the stated block-time target. Ylem's `ecrecover` declaration and call generation were separately inspected at commit `eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7` (local branch `fix/version`); the later Ylem follow-up below expands that inspection and updates the card's source revision. The new reference links the files supporting each section. Routing across the skill was reviewed, and relevant repository pages link to the applicable sections. No client or compiler builds, tests, or runtime checks were performed in that protocol follow-up.

On **2026-11-15**, the [Foxar card](repositories/bchainhub/foxar.md) gained practical development workflows selected from the developer's local skill. Commands, network selection, price options, and typed-data support were checked against a detached checkout of the already surveyed Foxar commit `deeea38450c5c6d133c9adbbd8737730ec334cdb`. Signature helper declarations were checked in the local Spark standard-library checkout at its already surveyed commit `e3212df3fe6568c2f24981d042ba83843410c069`. Installed tool version and help commands succeeded; their versions, working directory, and scope are recorded in the card. This was CLI inspection only: no builds, contract tests, node execution, RPC calls, signing, or broadcasts were performed. Source build and contract-runtime verification remained unperformed.

On **2026-11-15**, the [Ylem card](repositories/core-coin/ylem.md) was expanded using local branch `fix/version` at `eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7`: compiler use, address/ABI/storage representation, builtin names, target selection, source entry points, and build/test targets. The installed Ylem `1.1.2+commit.cb4b093a.Linux.g++` was separately queried for version and help; its output and exit statuses are recorded in the card. No source build or compiler/contract test was run.

On **2026-11-15**, the developer identified `bchainhub/openzeppelin-contracts` and `bchainhub/openzeppelin-contracts-upgradeable` as the current public CoreOZ libraries and requested one shared card. The [CoreOZ card](repositories/bchainhub/CoreOpenZeppelin.md) now covers both; this supersedes the earlier `bchainhub/CoreOpenZeppelin` survey at `4e35b0b4078bc0aa532c740e58f30dddd6b17574` for current development guidance without assuming the repositories are aliases. Public `main` heads were checked with `git ls-remote --symref` and matched the local source commits below. Source, project instructions, configuration, CI, and relevant tests were read; no root README exists at either revision. No dependencies were installed, library builds/tests run, or deployments performed. The developer also confirmed `EIP712Domain` as the correct Core typed-data domain name and `CIP712Domain` as an implementation error; the protocol reference and Foxar fixture note distinguish that requirement from current code. Coverage is now 89 repository identities in 88 cards.

On **2026-11-15**, [HD wallet derivation](core-protocol.md#hd-wallet-derivation) was added under addresses: Core coin type 654, the root and base address paths, relative-path parsing, and account-index iteration were checked in `accounts/hd.go` and `accounts/hd_test.go` at the recorded go-core commit `a091fe2d31ea1d3926db64da7621f26ed01c92a9` (local branch `audit`). Plain-keystore limitations were checked in `accounts/keystore/wallet.go`. Wallet and signer cards now route to this section without asserting HD support for every implementation. The [SLIP-0044 registry](https://github.com/satoshilabs/slips/blob/7a2abdd1e823f5180e0997434250eda88b57cb75/slip-0044.md), branch `master` at commit `7a2abdd1e823f5180e0997434250eda88b57cb75`, lists 654 as USDG; the reference therefore documents Core's implemented convention without repeating the client's registration claim. This was source inspection only; no wallet creation, mnemonic recovery, key derivation, or backend tests were performed.

| Repository | Commit | Source tree | README | Dependencies installed | Build | Tests | Runtime |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [core-coin/go-core](repositories/core-coin/go-core.md) | `a091fe2d31ea` | Yes | Yes | No | No | No | No |
| [core-coin/cip](repositories/core-coin/cip.md) | `0c2e54bbebeb` | Yes | Yes | No | No | No | No |
| [core-coin/cvm](repositories/core-coin/cvm.md) | `cf0f8737c713` | Yes | Yes | No | No | No | No |
| [core-coin/gocore-chocolatey](repositories/core-coin/gocore-chocolatey.md) | `976d06a82779` | Yes | Yes | No | No | No | No |
| [core-coin/go-goldilocks](repositories/core-coin/go-goldilocks.md) | `c399187e68d1` | Yes | Yes | No | No | No | No |
| [core-coin/ed448-rs](repositories/core-coin/ed448-rs.md) | `dc58d0c73d1f` | Yes | No README | No | No | No | No |
| [core-coin/ed448](repositories/core-coin/ed448.md) | `2f430f1307c8` | Yes | Yes | No | No | No | No |
| [core-coin/ylem](repositories/core-coin/ylem.md) | `eaf05fdd802ff` | Yes | Yes | No | No | No | CLI version/help only |
| [core-coin/nuntiare](repositories/core-coin/nuntiare.md) | `87aad6715f02` | Yes | Yes | No | No | No | No |
| [core-coin/go-randomy](repositories/core-coin/go-randomy.md) | `d2b7cb34e082` | Yes | Yes | No | No | No | No |
| [core-coin/core-cli](repositories/core-coin/core-cli.md) | `b6d3a5e44163` | Yes | Yes | No | No | No | No |
| [core-coin/core-etl](repositories/core-coin/core-etl.md) | `8395ea26a7e9` | Yes | Yes | No | No | No | No |
| [core-coin/base-rs](repositories/core-coin/base-rs.md) | `c4db05f2e108` | Yes | Yes | No | No | No | No |
| [core-coin/atoms-rs](repositories/core-coin/atoms-rs.md) | `dc67b3d62069` | Yes | Yes | No | No | No | No |
| [core-coin/xcb-keystore-rs](repositories/core-coin/xcb-keystore-rs.md) | `12b01647134e` | Yes | Yes | No | No | No | No |
| [core-coin/libgoldilocks](repositories/core-coin/libgoldilocks.md) | `f9177d5efcad` | Yes | Yes | No | No | No | No |
| [core-coin/RandomY](repositories/core-coin/RandomY.md) | `c9d185a055b7` | Yes | Yes | No | No | No | No |
| [core-coin/randomy-rs](repositories/core-coin/randomy-rs.md) | `ea1e46ea5885` | Yes | Yes | No | No | No | No |
| [core-coin/core-playbook](repositories/core-coin/core-playbook.md) | `682ccedf2ae2` | Yes | Yes | No | No | No | No |
| [core-coin/rlp](repositories/core-coin/rlp.md) | `9e108a2367bf` | Yes | Yes | No | No | No | No |
| [core-coin/hive](repositories/core-coin/hive.md) | `7abf3138375d` | Yes | Yes | No | No | No | No |
| [core-coin/corebc-rs](repositories/core-coin/corebc-rs.md) | `4395f3758517` | Yes | Yes | No | No | No | No |
| [core-coin/geas](repositories/core-coin/geas.md) | `7e40470f64bd` | Yes | Yes | No | No | No | No |
| [core-coin/yvm-rs](repositories/core-coin/yvm-rs.md) | `5cc860059ef0` | Yes | Yes | No | No | No | No |
| [core-coin/coreabi](repositories/core-coin/coreabi.md) | `ff9eab39a6a6` | Yes | Yes | No | No | No | No |
| [core-coin/core-diff](repositories/core-coin/core-diff.md) | `d6c22c36697e` | Yes | Yes | No | No | No | No |
| [core-coin/core-common](repositories/core-coin/core-common.md) | `6887ba42dc17` | Yes | Yes | No | No | No | No |
| [core-coin/oracle-checksum](repositories/core-coin/oracle-checksum.md) | `7892e500db17` | Yes | Yes | No | No | No | No |
| [core-coin/energy-forecast](repositories/core-coin/energy-forecast.md) | `ec89e7464981` | Yes | Yes | No | No | No | No |
| [core-coin/pigeon](repositories/core-coin/pigeon.md) | `ee0250ca8c9e` | Yes | Yes | No | No | No | No |
| [core-coin/Xcb.Net](repositories/core-coin/Xcb.Net.md) | `d9a36122c76e` | Yes | Yes | No | No | No | No |
| [core-coin/wallet-generator](repositories/core-coin/wallet-generator.md) | `3353936feffb` | Yes | Yes | No | No | No | No |
| [core-coin/ylem-bins](repositories/core-coin/ylem-bins.md) | `eee8f71eb684` | Yes | No README | No | No | No | No |
| [core-coin/faucet](repositories/core-coin/faucet.md) | `a85f50feba53` | Yes | Yes | No | No | No | No |
| [core-coin/uint256](repositories/core-coin/uint256.md) | `5e95ed0e0ff6` | Yes | Yes | No | No | No | No |
| [core-coin/homebrew-gocore](repositories/core-coin/homebrew-gocore.md) | `998f146958a5` | Yes | Yes | No | No | No | No |
| [core-coin/homebrew-ylem](repositories/core-coin/homebrew-ylem.md) | `5b375f184b97` | Yes | Yes | No | No | No | No |
| [core-coin/core-denomination](repositories/core-coin/core-denomination.md) | `f996c53649c3` | Yes | Yes | No | No | No | No |
| [core-coin/core-api](repositories/core-coin/core-api.md) | `71a3ea86e3f2` | Yes | No README | No | No | No | No |
| [core-coin/gofortuna](repositories/core-coin/gofortuna.md) | `8d9eed96287e` | Yes | Yes | No | No | No | No |
| [core-coin/renaming-table](repositories/core-coin/renaming-table.md) | `b25eb3e92d40` | Yes | Yes | No | No | No | No |
| [core-coin/helm-core](repositories/core-coin/helm-core.md) | `718a05843682` | Yes | Yes | No | No | No | No |
| [catchthatrabbit/coreminer](repositories/catchthatrabbit/coreminer.md) | `959119a256bf` | Yes | Yes | No | No | No | No |
| [catchthatrabbit/pool](repositories/catchthatrabbit/pool.md) | `2fe84056362b` | Yes | Yes | No | No | No | No |
| [CorePass/corebc.js](repositories/CorePass/corebc.js.md) | `caedc524ad4a` | Yes | Yes | No | No | No | No |
| [CorePass/flutter_ed448](repositories/CorePass/flutter_ed448.md) | `99861de215d5` | Yes | Yes | No | No | No | No |
| [CorePass/core_web3dart](repositories/CorePass/core_web3dart.md) | `e472746ff899` | Yes | Yes | No | No | No | No |
| [bchainhub/foxar](repositories/bchainhub/foxar.md) | `deeea38450c5` | Yes | Yes | No | No | No | No |
| [bchainhub/blockbook](repositories/bchainhub/blockbook.md) | `c3dcac935459` | Yes | Yes | No | No | No | No |
| [bchainhub/corecdn](repositories/bchainhub/corecdn.md) | `55965a02661e` | Yes | Yes | No | No | No | No |
| [bchainhub/flutter_paytorl](repositories/bchainhub/flutter_paytorl.md) | `c562180960aa` | Yes | Yes | No | No | No | No |
| [bchainhub/payto-rl](repositories/bchainhub/payto-rl.md) | `5c751e1f4df8` | Yes | Yes | No | No | No | No |
| [bchainhub/flutter_connect](repositories/bchainhub/flutter_connect.md) | `9579fe3a8236` | Yes | Yes | No | No | No | No |
| [bchainhub/better-connect](repositories/bchainhub/better-connect.md) | `eea920ea3851` | Yes | Yes | No | No | No | No |
| [bchainhub/connect.js](repositories/bchainhub/connect.js.md) | `e4cd8930b2ba` | Yes | Yes | No | No | No | No |
| [bchainhub/flutter_wallet_validator](repositories/bchainhub/flutter_wallet_validator.md) | `6bb14dbf680e` | Yes | Yes | No | No | No | No |
| [bchainhub/flutter_txms](repositories/bchainhub/flutter_txms.md) | `3a593f0c3021` | Yes | Yes | No | No | No | No |
| [bchainhub/txms.js](repositories/bchainhub/txms.js.md) | `53de2be00f10` | Yes | Yes | No | No | No | No |
| [bchainhub/well-known](repositories/bchainhub/well-known.md) | `6ec20da05db3` | Yes | Yes | No | No | No | No |
| [bchainhub/ican.js](repositories/bchainhub/ican.js.md) | `4cfc33f95188` | Yes | Yes | No | No | No | No |
| [bchainhub/exchange-rounding](repositories/bchainhub/exchange-rounding.md) | `f5c74f8aa723` | Yes | Yes | No | No | No | No |
| [bchainhub/openzeppelin-contracts](repositories/bchainhub/CoreOpenZeppelin.md#standard-contracts) | `672b803bebe6` | Yes | No root README | No | No | No | No |
| [bchainhub/openzeppelin-contracts-upgradeable](repositories/bchainhub/CoreOpenZeppelin.md#upgradeable-contracts) | `42f9882a4e98` | Yes | No root README | No | No | No | No |
| [bchainhub/core-license](repositories/bchainhub/core-license.md) | `f402289cb519` | Yes | Yes | No | No | No | No |
| [bchainhub/blo](repositories/bchainhub/blo.md) | `59981c4aabaa` | Yes | Yes | No | No | No | No |
| [bchainhub/spark-std](repositories/bchainhub/spark-std.md) | `e3212df3fe65` | Yes | Yes | No | No | No | No |
| [bchainhub/ds-test](repositories/bchainhub/ds-test.md) | `728395453b4e` | Yes | No README | No | No | No | No |
| [bchainhub/foxar-docs](repositories/bchainhub/foxar-docs.md) | `b4619e7dff80` | Yes | Yes | No | No | No | No |
| [bchainhub/spark-template](repositories/bchainhub/spark-template.md) | `4c4ba9c74044` | Yes | Yes | No | No | No | No |
| [bchainhub/gocore-mainnet-alloc-decode](repositories/bchainhub/gocore-mainnet-alloc-decode.md) | `657209c7d415` | Yes | Yes | No | No | No | No |
| [bchainhub/core-units](repositories/bchainhub/core-units.md) | `ee1566465b32` | Yes | Yes | No | No | No | No |
| [DataLayerHost/kamailio-txms](repositories/DataLayerHost/kamailio-txms.md) | `8a93383ee09b` | Yes | Yes | No | No | No | No |
| [DataLayerHost/libtxms](repositories/DataLayerHost/libtxms.md) | `de5f8479c430` | Yes | Yes | No | No | No | No |
| [DataLayerHost/luna-sdk](repositories/DataLayerHost/luna-sdk.md) | `4b0dee01ff72` | Yes | Yes | No | No | No | No |
| [DataLayerHost/luna_sdk](repositories/DataLayerHost/luna_sdk.md) | `33bf2250d839` | Yes | Yes | No | No | No | No |
| [DataLayerHost/flutter_modem](repositories/DataLayerHost/flutter_modem.md) | `b0b7781dc554` | Yes | Yes | No | No | No | No |
| [DataLayerHost/flutter_barcodetx](repositories/DataLayerHost/flutter_barcodetx.md) | `a69741ce321e` | Yes | Yes | No | No | No | No |
| [DataLayerHost/ScanBarcode](repositories/DataLayerHost/ScanBarcode.md) | `c7f31d5069f1` | Yes | Yes | No | No | No | No |
| [DataLayerHost/txms-server](repositories/DataLayerHost/txms-server.md) | `91372add3457` | Yes | Yes | No | No | No | No |
| [DataLayerHost/bchauth](repositories/DataLayerHost/bchauth.md) | `b17a1761655f` | Yes | Yes | No | No | No | No |
| [core-laboratories/payto](repositories/core-laboratories/payto.md) | `2e5d570d189d` | Yes | Yes | No | No | No | No |
| [core-laboratories/compact_money](repositories/core-laboratories/compact_money.md) | `3c9ef0558b89` | Yes | Yes | No | No | No | No |
| [core-laboratories/compact-money](repositories/core-laboratories/compact-money.md) | `3cd3083ce5b8` | Yes | Yes | No | No | No | No |
| [core-laboratories/paytoonl-web](repositories/core-laboratories/paytoonl-web.md) | `cdf950bf4581` | Yes | Yes | No | No | No | No |
| [core-laboratories/ipfs-worker](repositories/core-laboratories/ipfs-worker.md) | `unavailable` | No (404) | User supplied | No | No | No | No |
| [core-laboratories/oric](repositories/core-laboratories/oric.md) | `unavailable` | No (404) | User supplied | No | No | No | No |
| [core-laboratories/payto-map](repositories/core-laboratories/payto-map.md) | `11b4966e5cb9` | Yes | Yes | No | No | No | No |
| [core-laboratories/ylem-splitting](repositories/core-laboratories/ylem-splitting.md) | `6f810556e8e0` | Yes | No README | No | No | No | No |
| [core-laboratories/remix](repositories/core-laboratories/remix.md) | `unavailable` | No (404) | No | No | No | No | No |

## Access failures

- `core-laboratories/ipfs-worker`: unauthenticated GitHub REST returned HTTP 404; connected GitHub `get_repo` returned `NOT_FOUND`; Git clone could not obtain a checkout.
- `core-laboratories/oric`: unauthenticated GitHub REST returned HTTP 404; connected GitHub `get_repo` returned `NOT_FOUND`; Git clone could not obtain a checkout.
- `core-laboratories/remix`: connected GitHub `get_repo` and the public page returned HTTP 404; unauthenticated shallow clone timed out.

A 404 does not establish whether a repository was removed or is private. The user-supplied IPFS Worker and ORIC README content is available, but source and commits remain unverified. Remix content and commit remain unverified. Earlier build and runtime results supplied in the request came from another environment and are not checks performed here.
