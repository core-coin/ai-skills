# bchainhub/foxar

- Repository: https://github.com/bchainhub/foxar
- Research status: **source inspected**
- Inspection dates: 2026-11-11 (survey), 2026-11-15 (workflow and CLI follow-up)
- Inspected branch: `master` in the survey; the follow-up used a detached checkout of the same commit
- Inspected commit: `deeea38450c5c6d133c9adbbd8737730ec334cdb`
- Local research checkout: temporary checkout at the inspected commit (research only; not required to use this skill)
- README: [`README.md`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/README.md)

## Purpose and selection

Core smart-contract development framework for compilation, tests, scripting, deployment, account operations, and local execution.
The [`README.md`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

| Tool | Role |
| --- | --- |
| `spark` | Build and test contract projects, run scripts, and deploy contracts |
| `probe` | Encode and inspect contract data, call RPC methods, manage signing, and send transactions |
| `shuttle` | Run a local development node |
| `pilot` | Evaluate contract-language expressions interactively |
| `foxarup` | Install or update Foxar binaries; supports selecting a release or branch |

For a contract project, start with the workflows below. For changes to Foxar itself, inspect the Rust workspace and its CI.

## Architecture and source entry points

Inspected source entry point: [`ui/src/lib.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/ui/src/lib.rs).
Root build or package files: [`Cargo.toml`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/Cargo.toml), [`Dockerfile`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/Dockerfile).
Source or project directories to inspect first: `abi/`, `binder/`, `cli/`, `common/`, `config/`.
Examples or tests visible in the tree: [`cli/src/cmd/spark/test/filter.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/cli/src/cmd/spark/test/filter.rs), [`cli/src/cmd/spark/test/mod.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/cli/src/cmd/spark/test/mod.rs), [`pilot/tests/cache.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/pilot/tests/cache.rs).

## Toolchain, setup, and validation

Detected language/platform: **Rust**. This is based on the inspected tree and manifests, not a verified runtime environment.

For work on Foxar itself, the README documents Rust 1.87.0 and Ylem 1.1.2 for its focused creation-revert regression. Its Spark binary build command, run from the Foxar repository root, is `RUSTC_BOOTSTRAP=1 cargo build --locked -p foxar-cli --bin spark`. Consult the README for that regression's test command and prerequisites. These source-build commands were not executed during this inspection.

For contract projects, use the project's `foxar.toml`, dependencies, and selected Ylem version. Check `spark --version`, `probe --version`, and the relevant subcommand's `--help` before applying version-specific options. Use `--use <YLEM_VERSION>` when an explicit compiler selection is needed; retain the project's compiler constraints.

## Contract project workflow

Run from the contract project's root, with Foxar, the selected Ylem compiler, and project dependencies available:

```bash
spark build
spark test
```

The network examples below use user-provided variables: `RPC_URL` for the endpoint, `WALLET_NETWORK` for `mainnet` or `devin`, `NETWORK_ID` for the corresponding numeric ID, `SENDER` for the full Core sender address, and `ENERGY_PRICE` for the chosen transaction price. Obtain the private key through the project's existing signing setup; `PRIVATE_KEY` below represents that input. Network IDs and address rules are in [Core protocol](../../core-protocol.md#transactions).

### Network selection

Keep the endpoint, wallet network, numeric network ID, and ordinary account prefixes consistent. For prefix errors during script simulation, inspect the selected network and explicitly set `--sender "$SENDER" --tx-origin "$SENDER"` where needed. Preserve [precompile address exceptions](../../core-protocol.md#precompile-addresses).

At the inspected revision, `probe send` chooses its network from Foxar configuration. The default configuration contains `Private(1337)`, so `--wallet-network` alone does not replace the configured transaction network. Set `FOXAR_NETWORK_ID="$WALLET_NETWORK"` for the invocation, or configure the equivalent `network_id` in the project's selected profile.

`spark script` accepts `--network-id`. `spark create` obtains the numeric network ID from its provider and has **no `--network-id` option** at this revision; it accepts `--wallet-network`. Check the provider's network before deployment.

Sources: [`config/src/lib.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/config/src/lib.rs), [`cli/src/utils.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/cli/src/utils.rs), [`cli/src/cmd/probe/send.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/cli/src/cmd/probe/send.rs), [`cli/src/opts/wallet/mod.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/cli/src/opts/wallet/mod.rs), and [`cli/src/cmd/spark/create.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/cli/src/cmd/spark/create.rs).

### Script simulation and deployment

Simulate a script without broadcasting transactions:

```bash
spark script script/Deploy.s.sol:Deploy --rpc-url "$RPC_URL" --network-id "$NETWORK_ID" --sender "$SENDER" --tx-origin "$SENDER"
```

This executes the script using state fetched from the selected endpoint. Use the actual script path and contract name from the project.

For an authorized deployment, choose either a script broadcast or direct contract creation. A script must collect the intended transactions using its broadcast helpers:

```bash
spark script script/Deploy.s.sol:Deploy --rpc-url "$RPC_URL" --network-id "$NETWORK_ID" --wallet-network "$WALLET_NETWORK" --private-key "$PRIVATE_KEY" --sender "$SENDER" --tx-origin "$SENDER" --with-energy-price "$ENERGY_PRICE" --broadcast
```

Direct creation submits the deployment without a separate `--broadcast` flag:

```bash
spark create src/Example.sol:Example --rpc-url "$RPC_URL" --wallet-network "$WALLET_NETWORK" --private-key "$PRIVATE_KEY" --energy-price "$ENERGY_PRICE"
```

Add the project's constructor arguments when required. For an authorized contract write through Probe:

```bash
FOXAR_NETWORK_ID="$WALLET_NETWORK" probe send "$TO" "$METHOD_SIGNATURE" "$ARG" --rpc-url "$RPC_URL" --wallet-network "$WALLET_NETWORK" --private-key "$PRIVATE_KEY" --energy-price "$ENERGY_PRICE"
```

Adapt the argument list to the method. Retrieve a price quote, when needed, with `probe rpc --rpc-url "$RPC_URL" xcb_energyPrice`. For script transactions, `--with-energy-price` sets the broadcast price; `spark script --energy-price` configures the execution environment. Direct creation and `probe send` use `--energy-price`.

The inspected `spark script --help` documents `--code-size-limit` with a 50,000-byte default. Compare actual enforcement with the [network's runtime code limit](../../core-protocol.md#cvm-execution); a local override does not change network rules.

Sources: [`cli/src/cmd/spark/script/mod.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/cli/src/cmd/spark/script/mod.rs), [`cli/src/cmd/spark/script/broadcast.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/cli/src/cmd/spark/script/broadcast.rs), [`cli/src/cmd/spark/create.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/cli/src/cmd/spark/create.rs), [`cli/src/cmd/probe/send.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/cli/src/cmd/probe/send.rs), and [`evm/src/executor/opts.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/evm/src/executor/opts.rs).

### Signature tests and typed data

Use [`spark-std`](spark-std.md) test helpers for a matched address/key pair. At its inspected revision, the private key is a hex **string** representing 57 bytes, and `vm.sign` returns a **bytes** signature. Inside a test inheriting `Test`, after constructing the intended `bytes32 digest`:

```solidity
(address signer, string memory privateKey) = makeAddrAndKey("signer");
bytes memory signature = vm.sign(privateKey, digest);
assertEq(ecrecover(digest, signature), signer);
```

`vm.addr(privateKey)` derives an address from an existing key; `vm.rememberKey(privateKey)` also makes that key available for broadcasting. `vm.sign` signs the supplied digest directly and produces the [Core signature blob](../../core-protocol.md#signatures-and-address-derivation). Construct the [message or typed-data digest](../../core-protocol.md#message-and-typed-data-signing) explicitly; do not assume a separate `signTypedData` cheatcode.

Probe supports typed-data JSON supplied inline with `--data`, or from a file with `--data --from-file`:

```bash
probe wallet sign --data --from-file typed-data.json --wallet-network "$WALLET_NETWORK" --private-key "$PRIVATE_KEY"
```

The inspected CLI fixture uses `CIP712Domain` with `networkId`. The developer confirmed that the correct name is `EIP712Domain`; the fixture's domain name is erroneous. Do not copy it into new payloads. Match the complete domain type and encoded fields to the verifying contract, and check the signing implementation's domain hashing before relying on this CLI path. See the [typed-data compatibility note](CoreOpenZeppelin.md#typed-data-compatibility); the two names yield different hashes. At this revision, Shuttle implements `xcb_signTypedData_v4`; `xcb_signTypedData` and `xcb_signTypedData_v3` return an unimplemented error. This describes Shuttle, not every Core RPC server.

Sources: Spark standard-library [`src/StdCheats.sol`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/src/StdCheats.sol) and [`src/Vm.sol`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/src/Vm.sol); Foxar [`evm/src/executor/inspector/cheatcodes/util.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/evm/src/executor/inspector/cheatcodes/util.rs), [`cli/src/cmd/probe/wallet/mod.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/cli/src/cmd/probe/wallet/mod.rs), [`cli/tests/fixtures/sign_typed_data.json`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/cli/tests/fixtures/sign_typed_data.json), [`shuttle/core/src/eth/mod.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/shuttle/core/src/eth/mod.rs), and [`shuttle/src/eth/api.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/shuttle/src/eth/api.rs).

## Configuration, interfaces, and relationships

README sections to consult: `Installation`, `Creation revert regression`.
Environment variable names shown in the README: `FOXAR_TEST`, `RUSTC_BOOTSTRAP`. Verify required values and scope before use.
Contract project settings are loaded from `foxar.toml`; `FOXAR_CONFIG` selects another config file and `FOXAR_PROFILE` selects a profile. `FOXAR_` environment variables override corresponding configuration fields. Inspect the project's settings before relying on defaults.
Related references by task (not verified direct dependencies): [`bchainhub/foxar-docs`](foxar-docs.md), [`bchainhub/spark-template`](spark-template.md), [`bchainhub/spark-std`](spark-std.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

For mnemonic imports and derived-account selection in Probe or Spark, consult [Core HD derivation](../../core-protocol.md#hd-wallet-derivation). Check the wallet backend's full path and account index; network selection alone does not choose a derivation path.

For compiler targets, execution tests, and native calls, compare behavior with the [CVM baseline](../../core-protocol.md#cvm-execution) and [precompile rules](../../core-protocol.md#precompile-addresses). For wallet signing and broadcasts, consult [message and typed-data digests](../../core-protocol.md#message-and-typed-data-signing) and [transaction rules](../../core-protocol.md#transactions), then verify the specific tool's implementation.

Primary evidence: [`README.md`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/README.md), [`ui/src/lib.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/ui/src/lib.rs), [`Cargo.toml`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/Cargo.toml), [`Dockerfile`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/Dockerfile), [`.github/workflows/build.yml`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/.github/workflows/build.yml), [`.github/workflows/deny.yml`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/.github/workflows/deny.yml).
The source tree and listed text files were inspected at the commit above. Tool roles were also checked in [`cli/Cargo.toml`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/cli/Cargo.toml), [`pilot/src/bin/pilot.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/pilot/src/bin/pilot.rs), and [`foxarup/README.md`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/foxarup/README.md). The workflow follow-up on **2026-11-15** compared the developer's local guidance with a detached checkout of this same revision and Spark standard-library commit `e3212df3fe6568c2f24981d042ba83843410c069`.

Executed checks, from the skill repository root with the installed Foxar binaries on `PATH`: `--version` for `spark`, `probe`, `shuttle`, and `pilot`, and `--help` for `spark build`, `spark test`, `spark create`, `spark script`, `probe send`, `probe rpc`, `probe wallet sign`, `shuttle`, and `pilot`. All exited successfully. Spark and Probe reported `0.2.0`, Shuttle `0.1.0`, and Pilot `0.1.1`, all with commit prefix `deeea38`. No dependencies were installed, source builds or contract tests run, nodes started, RPC methods called, or transactions signed or broadcast. The examples above are source- and help-checked guidance, not end-to-end validation.
