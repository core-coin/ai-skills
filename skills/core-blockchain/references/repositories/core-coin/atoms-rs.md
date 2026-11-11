# core-coin/atoms-rs

- Repository: https://github.com/core-coin/atoms-rs
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `dc67b3d6206976e14ddbcb8fd6fdafc14eb8c52c`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/atoms-rs` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/atoms-rs/blob/dc67b3d6206976e14ddbcb8fd6fdafc14eb8c52c/README.md)

## Purpose and selection

Rust atom-related component; its README points to a parent file, so inspect package metadata.
The [`README.md`](https://github.com/core-coin/atoms-rs/blob/dc67b3d6206976e14ddbcb8fd6fdafc14eb8c52c/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`crates/eips/src/lib.rs`](https://github.com/core-coin/atoms-rs/blob/dc67b3d6206976e14ddbcb8fd6fdafc14eb8c52c/crates/eips/src/lib.rs).
Root build or package files: [`Cargo.toml`](https://github.com/core-coin/atoms-rs/blob/dc67b3d6206976e14ddbcb8fd6fdafc14eb8c52c/Cargo.toml).
Source or project directories to inspect first: `crates/`, `scripts/`.

## Toolchain, setup, and validation

Detected language/platform: **Rust**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `Cargo.toml` pins Rust 1.76.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/atoms-rs/blob/dc67b3d6206976e14ddbcb8fd6fdafc14eb8c52c/README.md), [`crates/eips/src/lib.rs`](https://github.com/core-coin/atoms-rs/blob/dc67b3d6206976e14ddbcb8fd6fdafc14eb8c52c/crates/eips/src/lib.rs), [`Cargo.toml`](https://github.com/core-coin/atoms-rs/blob/dc67b3d6206976e14ddbcb8fd6fdafc14eb8c52c/Cargo.toml), [`.github/workflows/ci.yml`](https://github.com/core-coin/atoms-rs/blob/dc67b3d6206976e14ddbcb8fd6fdafc14eb8c52c/.github/workflows/ci.yml), [`.github/workflows/deps.yml`](https://github.com/core-coin/atoms-rs/blob/dc67b3d6206976e14ddbcb8fd6fdafc14eb8c52c/.github/workflows/deps.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
