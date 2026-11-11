# core-coin/base-rs

- Repository: https://github.com/core-coin/base-rs
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `c4db05f2e108b426d543e245c8ac829e500f6043`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/base-rs` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/base-rs/blob/c4db05f2e108b426d543e245c8ac829e500f6043/README.md)

## Purpose and selection

Foundational Rust libraries for Core projects.
The [`README.md`](https://github.com/core-coin/base-rs/blob/c4db05f2e108b426d543e245c8ac829e500f6043/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`crates/core/src/lib.rs`](https://github.com/core-coin/base-rs/blob/c4db05f2e108b426d543e245c8ac829e500f6043/crates/core/src/lib.rs).
Root build or package files: [`Cargo.toml`](https://github.com/core-coin/base-rs/blob/c4db05f2e108b426d543e245c8ac829e500f6043/Cargo.toml).
Source or project directories to inspect first: `crates/`, `scripts/`.
Examples or tests visible in the tree: [`crates/core/tests/sol.rs`](https://github.com/core-coin/base-rs/blob/c4db05f2e108b426d543e245c8ac829e500f6043/crates/core/tests/sol.rs), [`crates/json-abi/tests/abi.rs`](https://github.com/core-coin/base-rs/blob/c4db05f2e108b426d543e245c8ac829e500f6043/crates/json-abi/tests/abi.rs), [`crates/syn-ylem/tests/contracts.rs`](https://github.com/core-coin/base-rs/blob/c4db05f2e108b426d543e245c8ac829e500f6043/crates/syn-ylem/tests/contracts.rs), [`crates/ylm-types/tests/compiletest.rs`](https://github.com/core-coin/base-rs/blob/c4db05f2e108b426d543e245c8ac829e500f6043/crates/ylm-types/tests/compiletest.rs).

## Toolchain, setup, and validation

Detected language/platform: **Rust**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `Cargo.toml` pins Rust 1.65.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Overview`, `Supported Rust Versions`, `Contributing`, `WASM support`, `Note on nostd`, `Credits`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/base-rs/blob/c4db05f2e108b426d543e245c8ac829e500f6043/README.md), [`crates/core/src/lib.rs`](https://github.com/core-coin/base-rs/blob/c4db05f2e108b426d543e245c8ac829e500f6043/crates/core/src/lib.rs), [`Cargo.toml`](https://github.com/core-coin/base-rs/blob/c4db05f2e108b426d543e245c8ac829e500f6043/Cargo.toml), [`.github/workflows/ci.yml`](https://github.com/core-coin/base-rs/blob/c4db05f2e108b426d543e245c8ac829e500f6043/.github/workflows/ci.yml), [`.github/workflows/deps.yml`](https://github.com/core-coin/base-rs/blob/c4db05f2e108b426d543e245c8ac829e500f6043/.github/workflows/deps.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
