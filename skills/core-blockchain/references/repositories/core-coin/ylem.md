# core-coin/ylem

- Repository: https://github.com/core-coin/ylem
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `afc75eef761bb0128fb528d7998a8db16347d13a`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/ylem` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/ylem/blob/afc75eef761bb0128fb528d7998a8db16347d13a/README.md)

## Purpose and selection

High-level contract language and compiler for Core contracts.
The [`README.md`](https://github.com/core-coin/ylem/blob/afc75eef761bb0128fb528d7998a8db16347d13a/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`solc/main.cpp`](https://github.com/core-coin/ylem/blob/afc75eef761bb0128fb528d7998a8db16347d13a/solc/main.cpp).
Root build or package files: [`CMakeLists.txt`](https://github.com/core-coin/ylem/blob/afc75eef761bb0128fb528d7998a8db16347d13a/CMakeLists.txt).
Source or project directories to inspect first: `cmake/`, `libevmasm/`, `liblangutil/`, `libsmtutil/`, `libsolc/`.
Examples or tests visible in the tree: [`test/buglistTests.js`](https://github.com/core-coin/ylem/blob/afc75eef761bb0128fb528d7998a8db16347d13a/test/buglistTests.js), [`test/pyscriptTests.py`](https://github.com/core-coin/ylem/blob/afc75eef761bb0128fb528d7998a8db16347d13a/test/pyscriptTests.py).

## Toolchain, setup, and validation

Detected language/platform: **C / C++**. This is based on the inspected tree and manifests, not a verified runtime environment.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Table of Contents`, `Background`, `Build and Install`, `Example`, `Documentation`, `Development`, `Maintainers`, `License`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`core-coin/yvm-rs`](yvm-rs.md), [`core-coin/ylem-bins`](ylem-bins.md), [`core-coin/cvm`](cvm.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/ylem/blob/afc75eef761bb0128fb528d7998a8db16347d13a/README.md), [`solc/main.cpp`](https://github.com/core-coin/ylem/blob/afc75eef761bb0128fb528d7998a8db16347d13a/solc/main.cpp), [`CMakeLists.txt`](https://github.com/core-coin/ylem/blob/afc75eef761bb0128fb528d7998a8db16347d13a/CMakeLists.txt), [`.github/workflows/build.yml`](https://github.com/core-coin/ylem/blob/afc75eef761bb0128fb528d7998a8db16347d13a/.github/workflows/build.yml), [`.github/workflows/buildpack-deps.yml`](https://github.com/core-coin/ylem/blob/afc75eef761bb0128fb528d7998a8db16347d13a/.github/workflows/buildpack-deps.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
