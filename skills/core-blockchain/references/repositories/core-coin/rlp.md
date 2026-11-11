# core-coin/rlp

- Repository: https://github.com/core-coin/rlp
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `9e108a2367bfc52d3149e2b624a0c62d7d23a0bd`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/rlp` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/rlp/blob/9e108a2367bfc52d3149e2b624a0c62d7d23a0bd/README.md)

## Purpose and selection

Rust RLP serialization library.
The [`README.md`](https://github.com/core-coin/rlp/blob/9e108a2367bfc52d3149e2b624a0c62d7d23a0bd/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`crates/rlp/src/lib.rs`](https://github.com/core-coin/rlp/blob/9e108a2367bfc52d3149e2b624a0c62d7d23a0bd/crates/rlp/src/lib.rs).
Root build or package files: [`Cargo.toml`](https://github.com/core-coin/rlp/blob/9e108a2367bfc52d3149e2b624a0c62d7d23a0bd/Cargo.toml).
Source or project directories to inspect first: `crates/`.
Examples or tests visible in the tree: [`crates/rlp/tests/derive.rs`](https://github.com/core-coin/rlp/blob/9e108a2367bfc52d3149e2b624a0c62d7d23a0bd/crates/rlp/tests/derive.rs), [`examples/enum.rs`](https://github.com/core-coin/rlp/blob/9e108a2367bfc52d3149e2b624a0c62d7d23a0bd/examples/enum.rs).

## Toolchain, setup, and validation

Detected language/platform: **Rust**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `Cargo.toml` pins Rust 1.64.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Supported Rust Versions`, `Contributing`, `Provenance note`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/rlp/blob/9e108a2367bfc52d3149e2b624a0c62d7d23a0bd/README.md), [`crates/rlp/src/lib.rs`](https://github.com/core-coin/rlp/blob/9e108a2367bfc52d3149e2b624a0c62d7d23a0bd/crates/rlp/src/lib.rs), [`Cargo.toml`](https://github.com/core-coin/rlp/blob/9e108a2367bfc52d3149e2b624a0c62d7d23a0bd/Cargo.toml), [`.github/workflows/ci.yml`](https://github.com/core-coin/rlp/blob/9e108a2367bfc52d3149e2b624a0c62d7d23a0bd/.github/workflows/ci.yml), [`.github/workflows/deps.yml`](https://github.com/core-coin/rlp/blob/9e108a2367bfc52d3149e2b624a0c62d7d23a0bd/.github/workflows/deps.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
