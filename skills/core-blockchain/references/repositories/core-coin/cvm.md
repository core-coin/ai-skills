# core-coin/cvm

- Repository: https://github.com/core-coin/cvm
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `cf0f8737c7139720e390d83ce940b846cc78dd1b`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/cvm` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/cvm/blob/cf0f8737c7139720e390d83ce940b846cc78dd1b/README.md)

## Purpose and selection

Rust virtual machine fork adapting execution to Core address widths.
The [`README.md`](https://github.com/core-coin/cvm/blob/cf0f8737c7139720e390d83ce940b846cc78dd1b/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`bins/revme/src/lib.rs`](https://github.com/core-coin/cvm/blob/cf0f8737c7139720e390d83ce940b846cc78dd1b/bins/revme/src/lib.rs).
Root build or package files: [`Cargo.toml`](https://github.com/core-coin/cvm/blob/cf0f8737c7139720e390d83ce940b846cc78dd1b/Cargo.toml).
Source or project directories to inspect first: `bins/`, `crates/`.
Examples or tests visible in the tree: [`bins/revme/tests/ican_deploy_contract_test.rs`](https://github.com/core-coin/cvm/blob/cf0f8737c7139720e390d83ce940b846cc78dd1b/bins/revme/tests/ican_deploy_contract_test.rs), [`bins/revme/tests/ican_send_eth_test.rs`](https://github.com/core-coin/cvm/blob/cf0f8737c7139720e390d83ce940b846cc78dd1b/bins/revme/tests/ican_send_eth_test.rs), [`crates/revm/tests/code_rollback.rs`](https://github.com/core-coin/cvm/blob/cf0f8737c7139720e390d83ce940b846cc78dd1b/crates/revm/tests/code_rollback.rs).

## Toolchain, setup, and validation

Detected language/platform: **Rust**. This is based on the inspected tree and manifests, not a verified runtime environment.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `cargo test --all --all-features`

## Configuration, interfaces, and relationships

README sections to consult: `Tests`, `Benchmark Tests`, `Disclaimer`, `Contributing`, `TODO`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`core-coin/ylem`](ylem.md), [`core-coin/coreabi`](coreabi.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/cvm/blob/cf0f8737c7139720e390d83ce940b846cc78dd1b/README.md), [`bins/revme/src/lib.rs`](https://github.com/core-coin/cvm/blob/cf0f8737c7139720e390d83ce940b846cc78dd1b/bins/revme/src/lib.rs), [`Cargo.toml`](https://github.com/core-coin/cvm/blob/cf0f8737c7139720e390d83ce940b846cc78dd1b/Cargo.toml), [`.github/workflows/ci.yml`](https://github.com/core-coin/cvm/blob/cf0f8737c7139720e390d83ce940b846cc78dd1b/.github/workflows/ci.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
