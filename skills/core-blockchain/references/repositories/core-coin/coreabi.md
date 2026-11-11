# core-coin/coreabi

- Repository: https://github.com/core-coin/coreabi
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `ff9eab39a6a6e407a550e8c49b28ceb415aafcf2`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/coreabi` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/coreabi/blob/ff9eab39a6a6e407a550e8c49b28ceb415aafcf2/README.md)

## Purpose and selection

ABI crate adapted for Core.
The [`README.md`](https://github.com/core-coin/coreabi/blob/ff9eab39a6a6e407a550e8c49b28ceb415aafcf2/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`cli/src/main.rs`](https://github.com/core-coin/coreabi/blob/ff9eab39a6a6e407a550e8c49b28ceb415aafcf2/cli/src/main.rs).
Root build or package files: [`Cargo.toml`](https://github.com/core-coin/coreabi/blob/ff9eab39a6a6e407a550e8c49b28ceb415aafcf2/Cargo.toml).
Source or project directories to inspect first: `cli/`, `contract/`, `derive/`, `ethabi/`, `res/`.

## Toolchain, setup, and validation

Detected language/platform: **Rust**. This is based on the inspected tree and manifests, not a verified runtime environment.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/coreabi/blob/ff9eab39a6a6e407a550e8c49b28ceb415aafcf2/README.md), [`cli/src/main.rs`](https://github.com/core-coin/coreabi/blob/ff9eab39a6a6e407a550e8c49b28ceb415aafcf2/cli/src/main.rs), [`Cargo.toml`](https://github.com/core-coin/coreabi/blob/ff9eab39a6a6e407a550e8c49b28ceb415aafcf2/Cargo.toml), [`.github/workflows/main.yml`](https://github.com/core-coin/coreabi/blob/ff9eab39a6a6e407a550e8c49b28ceb415aafcf2/.github/workflows/main.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
