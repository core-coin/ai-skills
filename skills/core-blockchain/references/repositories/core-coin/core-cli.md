# core-coin/core-cli

- Repository: https://github.com/core-coin/core-cli
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `b6d3a5e441639a91100831a93e27820d8ba27732`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/core-cli` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/core-cli/blob/b6d3a5e441639a91100831a93e27820d8ba27732/README.md)

## Purpose and selection

Command-line tool for accounts, transactions, and contracts.
The [`README.md`](https://github.com/core-coin/core-cli/blob/b6d3a5e441639a91100831a93e27820d8ba27732/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`crates/cli/src/lib.rs`](https://github.com/core-coin/core-cli/blob/b6d3a5e441639a91100831a93e27820d8ba27732/crates/cli/src/lib.rs).
Root build or package files: [`Cargo.toml`](https://github.com/core-coin/core-cli/blob/b6d3a5e441639a91100831a93e27820d8ba27732/Cargo.toml), [`Makefile`](https://github.com/core-coin/core-cli/blob/b6d3a5e441639a91100831a93e27820d8ba27732/Makefile).
Source or project directories to inspect first: `bin/`, `crates/`.
Examples or tests visible in the tree: [`crates/cli/tests/cli_tests.rs`](https://github.com/core-coin/core-cli/blob/b6d3a5e441639a91100831a93e27820d8ba27732/crates/cli/tests/cli_tests.rs), [`crates/cli/tests/integration_tests.rs`](https://github.com/core-coin/core-cli/blob/b6d3a5e441639a91100831a93e27820d8ba27732/crates/cli/tests/integration_tests.rs), [`crates/error/tests/unit_test.rs`](https://github.com/core-coin/core-cli/blob/b6d3a5e441639a91100831a93e27820d8ba27732/crates/error/tests/unit_test.rs), [`crates/modules/tests/xcb_tests.rs`](https://github.com/core-coin/core-cli/blob/b6d3a5e441639a91100831a93e27820d8ba27732/crates/modules/tests/xcb_tests.rs).

## Toolchain, setup, and validation

Detected language/platform: **Rust**. This is based on the inspected tree and manifests, not a verified runtime environment.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `cargo build --release`

## Configuration, interfaces, and relationships

README sections to consult: `Install Rust (Optional)`, `Installing Core CLI`, `What this does`, `Verify Installation`, `Building Core CLI from Source (Optional)`, `Getting Started with Core CLI`, `Repository and Contributions`, `License`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/core-cli/blob/b6d3a5e441639a91100831a93e27820d8ba27732/README.md), [`crates/cli/src/lib.rs`](https://github.com/core-coin/core-cli/blob/b6d3a5e441639a91100831a93e27820d8ba27732/crates/cli/src/lib.rs), [`Cargo.toml`](https://github.com/core-coin/core-cli/blob/b6d3a5e441639a91100831a93e27820d8ba27732/Cargo.toml), [`Makefile`](https://github.com/core-coin/core-cli/blob/b6d3a5e441639a91100831a93e27820d8ba27732/Makefile), [`.github/workflows/ci.yml`](https://github.com/core-coin/core-cli/blob/b6d3a5e441639a91100831a93e27820d8ba27732/.github/workflows/ci.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
