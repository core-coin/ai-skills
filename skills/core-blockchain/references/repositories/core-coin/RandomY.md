# core-coin/RandomY

- Repository: https://github.com/core-coin/RandomY
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `c9d185a055b7604e8d58059031e0e33dfe577cc5`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/RandomY` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/RandomY/blob/c9d185a055b7604e8d58059031e0e33dfe577cc5/README.md)

## Purpose and selection

RandomY proof-of-work implementation.
The [`README.md`](https://github.com/core-coin/RandomY/blob/c9d185a055b7604e8d58059031e0e33dfe577cc5/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src/cpu.cpp`](https://github.com/core-coin/RandomY/blob/c9d185a055b7604e8d58059031e0e33dfe577cc5/src/cpu.cpp).
Root build or package files: [`CMakeLists.txt`](https://github.com/core-coin/RandomY/blob/c9d185a055b7604e8d58059031e0e33dfe577cc5/CMakeLists.txt), [`randomy.sln`](https://github.com/core-coin/RandomY/blob/c9d185a055b7604e8d58059031e0e33dfe577cc5/randomy.sln).
Source or project directories to inspect first: `src/`, `vcxproj/`.

## Toolchain, setup, and validation

Detected language/platform: **C / C++**. This is based on the inspected tree and manifests, not a verified runtime environment.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Overview`, `Build`, `Linux`, `Windows`, `Precompiled binaries`, `Proof of work`, `CPU performance`, `Which CPU is best for mining RandomY?`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`core-coin/go-randomy`](go-randomy.md), [`core-coin/randomy-rs`](randomy-rs.md), [`catchthatrabbit/coreminer`](../catchthatrabbit/coreminer.md), [`catchthatrabbit/pool`](../catchthatrabbit/pool.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/RandomY/blob/c9d185a055b7604e8d58059031e0e33dfe577cc5/README.md), [`src/cpu.cpp`](https://github.com/core-coin/RandomY/blob/c9d185a055b7604e8d58059031e0e33dfe577cc5/src/cpu.cpp), [`CMakeLists.txt`](https://github.com/core-coin/RandomY/blob/c9d185a055b7604e8d58059031e0e33dfe577cc5/CMakeLists.txt), [`.github/workflows/pipeline.yml`](https://github.com/core-coin/RandomY/blob/c9d185a055b7604e8d58059031e0e33dfe577cc5/.github/workflows/pipeline.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
