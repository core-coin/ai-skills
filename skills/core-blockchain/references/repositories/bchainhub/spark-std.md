# bchainhub/spark-std

- Repository: https://github.com/bchainhub/spark-std
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `e3212df3fe6568c2f24981d042ba83843410c069`
- Local research checkout: `/tmp/core-blockchain-research/bchainhub/spark-std` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/README.md)

## Purpose and selection

Standard library for the Spark contract toolchain.
The [`README.md`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src/Vm.sol`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/src/Vm.sol).
Root build or package files: [`.gitmodules`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/.gitmodules), [`package.json`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/package.json).
Source or project directories to inspect first: `lib/`, `src/`.
Examples or tests visible in the tree: [`test/StdAssertions.t.sol`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/test/StdAssertions.t.sol), [`test/StdChains.t.sol`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/test/StdChains.t.sol), [`test/StdCheats.t.sol`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/test/StdCheats.t.sol), [`test/StdError.t.sol`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/test/StdError.t.sol).

## Toolchain, setup, and validation

Detected language/platform: **JavaScript / TypeScript**. This is based on the inspected tree and manifests, not a verified runtime environment.
Submodule configuration exists: [`.gitmodules`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/.gitmodules); resolve submodules before a build when required.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Install`, `Contracts`, `stdError`, `stdStorage`, `stdCheats`, `Std Assertions`, `console.log`, `License`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/README.md), [`src/Vm.sol`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/src/Vm.sol), [`.gitmodules`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/.gitmodules), [`package.json`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/package.json), [`.github/workflows/ci.yml`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/.github/workflows/ci.yml), [`.github/workflows/sync.yml`](https://github.com/bchainhub/spark-std/blob/e3212df3fe6568c2f24981d042ba83843410c069/.github/workflows/sync.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
