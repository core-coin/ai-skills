# DataLayerHost/libtxms

- Repository: https://github.com/DataLayerHost/libtxms
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `de5f8479c4301494c6e749a1467b2564bc30ba4a`
- Local research checkout: `/tmp/core-blockchain-research/DataLayerHost/libtxms` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/DataLayerHost/libtxms/blob/de5f8479c4301494c6e749a1467b2564bc30ba4a/README.md)

## Purpose and selection

C11 implementation of the TxMS codec.
The [`README.md`](https://github.com/DataLayerHost/libtxms/blob/de5f8479c4301494c6e749a1467b2564bc30ba4a/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src/txms.c`](https://github.com/DataLayerHost/libtxms/blob/de5f8479c4301494c6e749a1467b2564bc30ba4a/src/txms.c).
Root build or package files: [`CMakeLists.txt`](https://github.com/DataLayerHost/libtxms/blob/de5f8479c4301494c6e749a1467b2564bc30ba4a/CMakeLists.txt), [`Makefile`](https://github.com/DataLayerHost/libtxms/blob/de5f8479c4301494c6e749a1467b2564bc30ba4a/Makefile).
Source or project directories to inspect first: `cmake/`, `include/`, `packaging/`, `src/`, `test_package/`.
Examples or tests visible in the tree: [`tests/flutter_compatibility.py`](https://github.com/DataLayerHost/libtxms/blob/de5f8479c4301494c6e749a1467b2564bc30ba4a/tests/flutter_compatibility.py), [`tests/test_release.py`](https://github.com/DataLayerHost/libtxms/blob/de5f8479c4301494c6e749a1467b2564bc30ba4a/tests/test_release.py).

## Toolchain, setup, and validation

Detected language/platform: **C / C++**. This is based on the inspected tree and manifests, not a verified runtime environment.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Build and test`, `API and wire behavior`, `Reference provenance and cross-language tests`, `Conan 2 packages`, `GitHub releases`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`DataLayerHost/kamailio-txms`](kamailio-txms.md), [`bchainhub/txms.js`](../bchainhub/txms.js.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/DataLayerHost/libtxms/blob/de5f8479c4301494c6e749a1467b2564bc30ba4a/README.md), [`src/txms.c`](https://github.com/DataLayerHost/libtxms/blob/de5f8479c4301494c6e749a1467b2564bc30ba4a/src/txms.c), [`CMakeLists.txt`](https://github.com/DataLayerHost/libtxms/blob/de5f8479c4301494c6e749a1467b2564bc30ba4a/CMakeLists.txt), [`Makefile`](https://github.com/DataLayerHost/libtxms/blob/de5f8479c4301494c6e749a1467b2564bc30ba4a/Makefile), [`.github/workflows/ci.yml`](https://github.com/DataLayerHost/libtxms/blob/de5f8479c4301494c6e749a1467b2564bc30ba4a/.github/workflows/ci.yml), [`.github/workflows/release.yml`](https://github.com/DataLayerHost/libtxms/blob/de5f8479c4301494c6e749a1467b2564bc30ba4a/.github/workflows/release.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
