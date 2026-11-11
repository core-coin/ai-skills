# bchainhub/blockbook

- Repository: https://github.com/bchainhub/blockbook
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `c3dcac935459689c0770e2274e6af924251d4f62`
- Local research checkout: `/tmp/core-blockchain-research/bchainhub/blockbook` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/bchainhub/blockbook/blob/c3dcac935459689c0770e2274e6af924251d4f62/README.md)

## Purpose and selection

Blockchain indexing backend used by wallet applications.
The [`README.md`](https://github.com/bchainhub/blockbook/blob/c3dcac935459689c0770e2274e6af924251d4f62/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`static/js/main.js`](https://github.com/bchainhub/blockbook/blob/c3dcac935459689c0770e2274e6af924251d4f62/static/js/main.js).
Root build or package files: [`Makefile`](https://github.com/bchainhub/blockbook/blob/c3dcac935459689c0770e2274e6af924251d4f62/Makefile), [`go.mod`](https://github.com/bchainhub/blockbook/blob/c3dcac935459689c0770e2274e6af924251d4f62/go.mod).
Source or project directories to inspect first: `api/`, `bchain/`, `build/`, `common/`, `configs/`.
Examples or tests visible in the tree: [`api/types_test.go`](https://github.com/bchainhub/blockbook/blob/c3dcac935459689c0770e2274e6af924251d4f62/api/types_test.go), [`bchain/baseparser_test.go`](https://github.com/bchainhub/blockbook/blob/c3dcac935459689c0770e2274e6af924251d4f62/bchain/baseparser_test.go), [`bchain/coins/bch/bcashparser_test.go`](https://github.com/bchainhub/blockbook/blob/c3dcac935459689c0770e2274e6af924251d4f62/bchain/coins/bch/bcashparser_test.go), [`bchain/coins/bellcoin/bellcoinparser_test.go`](https://github.com/bchainhub/blockbook/blob/c3dcac935459689c0770e2274e6af924251d4f62/bchain/coins/bellcoin/bellcoinparser_test.go).

## Toolchain, setup, and validation

Detected language/platform: **Go**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `go.mod` declares Go 1.21.1.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Build and installation instructions`, `Implemented coins`, `Common issues when running Blockbook or implementing additional coins`, `Data storage in RocksDB`, `API`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/bchainhub/blockbook/blob/c3dcac935459689c0770e2274e6af924251d4f62/README.md), [`static/js/main.js`](https://github.com/bchainhub/blockbook/blob/c3dcac935459689c0770e2274e6af924251d4f62/static/js/main.js), [`Makefile`](https://github.com/bchainhub/blockbook/blob/c3dcac935459689c0770e2274e6af924251d4f62/Makefile), [`go.mod`](https://github.com/bchainhub/blockbook/blob/c3dcac935459689c0770e2274e6af924251d4f62/go.mod).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
