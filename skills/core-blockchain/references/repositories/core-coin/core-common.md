# core-coin/core-common

- Repository: https://github.com/core-coin/core-common
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `6887ba42dc17baaa96bd75b1e88d9c6db0789abe`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/core-common` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/core-common/blob/6887ba42dc17baaa96bd75b1e88d9c6db0789abe/README.md)

## Purpose and selection

Shared Rust crates for Core applications.
The [`README.md`](https://github.com/core-coin/core-common/blob/6887ba42dc17baaa96bd75b1e88d9c6db0789abe/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`rlp/src/lib.rs`](https://github.com/core-coin/core-common/blob/6887ba42dc17baaa96bd75b1e88d9c6db0789abe/rlp/src/lib.rs).
Root build or package files: [`Cargo.toml`](https://github.com/core-coin/core-common/blob/6887ba42dc17baaa96bd75b1e88d9c6db0789abe/Cargo.toml).
Source or project directories to inspect first: `bounded-collections/`, `ethbloom/`, `ethereum-types/`, `fixed-hash/`, `keccak-hash/`.
Examples or tests visible in the tree: [`ethereum-types/tests/serde.rs`](https://github.com/core-coin/core-common/blob/6887ba42dc17baaa96bd75b1e88d9c6db0789abe/ethereum-types/tests/serde.rs), [`kvdb-rocksdb/examples/memtest.rs`](https://github.com/core-coin/core-common/blob/6887ba42dc17baaa96bd75b1e88d9c6db0789abe/kvdb-rocksdb/examples/memtest.rs), [`primitive-types/tests/fp_conversion.rs`](https://github.com/core-coin/core-common/blob/6887ba42dc17baaa96bd75b1e88d9c6db0789abe/primitive-types/tests/fp_conversion.rs), [`primitive-types/tests/num_traits.rs`](https://github.com/core-coin/core-common/blob/6887ba42dc17baaa96bd75b1e88d9c6db0789abe/primitive-types/tests/num_traits.rs).

## Toolchain, setup, and validation

Detected language/platform: **Rust**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `bounded-collections/Cargo.toml` pins Rust 1.60.0; `ethbloom/Cargo.toml` pins Rust 1.56.1; `ethereum-types/Cargo.toml` pins Rust 1.60.0.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/core-common/blob/6887ba42dc17baaa96bd75b1e88d9c6db0789abe/README.md), [`rlp/src/lib.rs`](https://github.com/core-coin/core-common/blob/6887ba42dc17baaa96bd75b1e88d9c6db0789abe/rlp/src/lib.rs), [`Cargo.toml`](https://github.com/core-coin/core-common/blob/6887ba42dc17baaa96bd75b1e88d9c6db0789abe/Cargo.toml), [`.github/workflows/ci.yml`](https://github.com/core-coin/core-common/blob/6887ba42dc17baaa96bd75b1e88d9c6db0789abe/.github/workflows/ci.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
