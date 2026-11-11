# core-coin/corebc-rs

- Repository: https://github.com/core-coin/corebc-rs
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `4395f3758517c1e40fbcd4fbe5b0359416180f14`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/corebc-rs` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/corebc-rs/blob/4395f3758517c1e40fbcd4fbe5b0359416180f14/README.md)

## Purpose and selection

Rust crates for Core development; inspect individual crates for the needed API.
The [`README.md`](https://github.com/core-coin/corebc-rs/blob/4395f3758517c1e40fbcd4fbe5b0359416180f14/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`corebc/src/lib.rs`](https://github.com/core-coin/corebc-rs/blob/4395f3758517c1e40fbcd4fbe5b0359416180f14/corebc/src/lib.rs).
Root build or package files: [`Cargo.toml`](https://github.com/core-coin/corebc-rs/blob/4395f3758517c1e40fbcd4fbe5b0359416180f14/Cargo.toml).
Source or project directories to inspect first: `bin/`, `book/`, `corebc-addressbook/`, `corebc-blockindex/`, `corebc-contract/`.
Examples or tests visible in the tree: [`corebc-contract/corebc-contract-abigen/src/test/macros.rs`](https://github.com/core-coin/corebc-rs/blob/4395f3758517c1e40fbcd4fbe5b0359416180f14/corebc-contract/corebc-contract-abigen/src/test/macros.rs), [`corebc-keystore/tests/mod.rs`](https://github.com/core-coin/corebc-rs/blob/4395f3758517c1e40fbcd4fbe5b0359416180f14/corebc-keystore/tests/mod.rs), [`corebc-ylem/tests/mocked.rs`](https://github.com/core-coin/corebc-rs/blob/4395f3758517c1e40fbcd4fbe5b0359416180f14/corebc-ylem/tests/mocked.rs), [`corebc-ylem/tests/project.rs`](https://github.com/core-coin/corebc-rs/blob/4395f3758517c1e40fbcd4fbe5b0359416180f14/corebc-ylem/tests/project.rs).

## Toolchain, setup, and validation

Detected language/platform: **Rust**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `Cargo.toml` pins Rust 1.65.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/corebc-rs/blob/4395f3758517c1e40fbcd4fbe5b0359416180f14/README.md), [`corebc/src/lib.rs`](https://github.com/core-coin/corebc-rs/blob/4395f3758517c1e40fbcd4fbe5b0359416180f14/corebc/src/lib.rs), [`Cargo.toml`](https://github.com/core-coin/corebc-rs/blob/4395f3758517c1e40fbcd4fbe5b0359416180f14/Cargo.toml), [`.github/workflows/book.yml`](https://github.com/core-coin/corebc-rs/blob/4395f3758517c1e40fbcd4fbe5b0359416180f14/.github/workflows/book.yml), [`.github/workflows/ci.yml`](https://github.com/core-coin/corebc-rs/blob/4395f3758517c1e40fbcd4fbe5b0359416180f14/.github/workflows/ci.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
