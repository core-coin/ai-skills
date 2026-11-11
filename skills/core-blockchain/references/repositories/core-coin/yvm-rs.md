# core-coin/yvm-rs

- Repository: https://github.com/core-coin/yvm-rs
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `5cc860059ef04436af71f8e8fd8d965483bb21a8`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/yvm-rs` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/yvm-rs/blob/5cc860059ef04436af71f8e8fd8d965483bb21a8/README.md)

## Purpose and selection

Version manager for the Ylem compiler.
The [`README.md`](https://github.com/core-coin/yvm-rs/blob/5cc860059ef04436af71f8e8fd8d965483bb21a8/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`crates/yvm-rs/src/lib.rs`](https://github.com/core-coin/yvm-rs/blob/5cc860059ef04436af71f8e8fd8d965483bb21a8/crates/yvm-rs/src/lib.rs).
Root build or package files: [`Cargo.toml`](https://github.com/core-coin/yvm-rs/blob/5cc860059ef04436af71f8e8fd8d965483bb21a8/Cargo.toml).
Source or project directories to inspect first: `crates/`.

## Toolchain, setup, and validation

Detected language/platform: **Rust**. This is based on the inspected tree and manifests, not a verified runtime environment.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Install`, `Usage`, `TODO`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`core-coin/ylem`](ylem.md), [`core-coin/ylem-bins`](ylem-bins.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/yvm-rs/blob/5cc860059ef04436af71f8e8fd8d965483bb21a8/README.md), [`crates/yvm-rs/src/lib.rs`](https://github.com/core-coin/yvm-rs/blob/5cc860059ef04436af71f8e8fd8d965483bb21a8/crates/yvm-rs/src/lib.rs), [`Cargo.toml`](https://github.com/core-coin/yvm-rs/blob/5cc860059ef04436af71f8e8fd8d965483bb21a8/Cargo.toml), [`.github/workflows/ci.yml`](https://github.com/core-coin/yvm-rs/blob/5cc860059ef04436af71f8e8fd8d965483bb21a8/.github/workflows/ci.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
