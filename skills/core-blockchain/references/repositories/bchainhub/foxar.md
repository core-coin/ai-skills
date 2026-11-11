# bchainhub/foxar

- Repository: https://github.com/bchainhub/foxar
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `deeea38450c5c6d133c9adbbd8737730ec334cdb`
- Local research checkout: `/tmp/core-blockchain-research/bchainhub/foxar` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/README.md)

## Purpose and selection

Smart-contract development framework; inspect its README and scripts for supported workflows.
The [`README.md`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`ui/src/lib.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/ui/src/lib.rs).
Root build or package files: [`Cargo.toml`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/Cargo.toml), [`Dockerfile`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/Dockerfile).
Source or project directories to inspect first: `abi/`, `binder/`, `cli/`, `common/`, `config/`.
Examples or tests visible in the tree: [`cli/src/cmd/spark/test/filter.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/cli/src/cmd/spark/test/filter.rs), [`cli/src/cmd/spark/test/mod.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/cli/src/cmd/spark/test/mod.rs), [`pilot/tests/cache.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/pilot/tests/cache.rs).

## Toolchain, setup, and validation

Detected language/platform: **Rust**. This is based on the inspected tree and manifests, not a verified runtime environment.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Installation`, `Creation revert regression`.
Environment variable names shown in the README: `FOXAR_TEST`, `RUSTC_BOOTSTRAP`. Verify required values and scope before use.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`bchainhub/foxar-docs`](foxar-docs.md), [`bchainhub/spark-template`](spark-template.md), [`bchainhub/spark-std`](spark-std.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/README.md), [`ui/src/lib.rs`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/ui/src/lib.rs), [`Cargo.toml`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/Cargo.toml), [`Dockerfile`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/Dockerfile), [`.github/workflows/build.yml`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/.github/workflows/build.yml), [`.github/workflows/deny.yml`](https://github.com/bchainhub/foxar/blob/deeea38450c5c6d133c9adbbd8737730ec334cdb/.github/workflows/deny.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
