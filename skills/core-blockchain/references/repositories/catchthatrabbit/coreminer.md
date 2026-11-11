# catchthatrabbit/coreminer

- Repository: https://github.com/catchthatrabbit/coreminer
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `959119a256bf9444cee4bd1c8f58d85a7d63374e`
- Local research checkout: `/tmp/core-blockchain-research/catchthatrabbit/coreminer` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/catchthatrabbit/coreminer/blob/959119a256bf9444cee4bd1c8f58d85a7d63374e/README.md)

## Purpose and selection

CPU miner with Stratum support.
The [`README.md`](https://github.com/catchthatrabbit/coreminer/blob/959119a256bf9444cee4bd1c8f58d85a7d63374e/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`coreminer/main.cpp`](https://github.com/catchthatrabbit/coreminer/blob/959119a256bf9444cee4bd1c8f58d85a7d63374e/coreminer/main.cpp).
Root build or package files: [`.gitmodules`](https://github.com/catchthatrabbit/coreminer/blob/959119a256bf9444cee4bd1c8f58d85a7d63374e/.gitmodules), [`CMakeLists.txt`](https://github.com/catchthatrabbit/coreminer/blob/959119a256bf9444cee4bd1c8f58d85a7d63374e/CMakeLists.txt), [`Dockerfile`](https://github.com/catchthatrabbit/coreminer/blob/959119a256bf9444cee4bd1c8f58d85a7d63374e/Dockerfile).
Source or project directories to inspect first: `cmake/`, `coreminer/`, `libapicore/`, `libdevcore/`, `libethash-cpu/`.

## Toolchain, setup, and validation

Detected language/platform: **C / C++**. This is based on the inspected tree and manifests, not a verified runtime environment.
Submodule configuration exists: [`.gitmodules`](https://github.com/catchthatrabbit/coreminer/blob/959119a256bf9444cee4bd1c8f58d85a7d63374e/.gitmodules); resolve submodules before a build when required.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Table of Contents`, `Install`, `Manual Installation`, `Automatic Installation`, `Cloud Deployment`, `Usage`, `How to start mining`, `Limitations`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`catchthatrabbit/pool`](pool.md), [`core-coin/RandomY`](../core-coin/RandomY.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/catchthatrabbit/coreminer/blob/959119a256bf9444cee4bd1c8f58d85a7d63374e/README.md), [`coreminer/main.cpp`](https://github.com/catchthatrabbit/coreminer/blob/959119a256bf9444cee4bd1c8f58d85a7d63374e/coreminer/main.cpp), [`.gitmodules`](https://github.com/catchthatrabbit/coreminer/blob/959119a256bf9444cee4bd1c8f58d85a7d63374e/.gitmodules), [`CMakeLists.txt`](https://github.com/catchthatrabbit/coreminer/blob/959119a256bf9444cee4bd1c8f58d85a7d63374e/CMakeLists.txt), [`Dockerfile`](https://github.com/catchthatrabbit/coreminer/blob/959119a256bf9444cee4bd1c8f58d85a7d63374e/Dockerfile), [`.github/workflows/build.yml`](https://github.com/catchthatrabbit/coreminer/blob/959119a256bf9444cee4bd1c8f58d85a7d63374e/.github/workflows/build.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
