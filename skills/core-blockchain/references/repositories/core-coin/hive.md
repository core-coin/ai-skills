# core-coin/hive

- Repository: https://github.com/core-coin/hive
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `7abf3138375dda9162dce43d50a9fb5ce06e4188`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/hive` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/hive/blob/7abf3138375dda9162dce43d50a9fb5ce06e4188/README.md)

## Purpose and selection

Integration test harness for Core clients.
The [`README.md`](https://github.com/core-coin/hive/blob/7abf3138375dda9162dce43d50a9fb5ce06e4188/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`cmd/hiveview/main.go`](https://github.com/core-coin/hive/blob/7abf3138375dda9162dce43d50a9fb5ce06e4188/cmd/hiveview/main.go).
Root build or package files: [`go.mod`](https://github.com/core-coin/hive/blob/7abf3138375dda9162dce43d50a9fb5ce06e4188/go.mod).
Source or project directories to inspect first: `clients/`, `cmd/`, `configs/`, `hiveproxy/`, `hivesim/`.
Examples or tests visible in the tree: [`cmd/hivechain/generate_test.go`](https://github.com/core-coin/hive/blob/7abf3138375dda9162dce43d50a9fb5ce06e4188/cmd/hivechain/generate_test.go), [`cmd/hiveview/deploy_test.go`](https://github.com/core-coin/hive/blob/7abf3138375dda9162dce43d50a9fb5ce06e4188/cmd/hiveview/deploy_test.go), [`hiveproxy/proxy_test.go`](https://github.com/core-coin/hive/blob/7abf3138375dda9162dce43d50a9fb5ce06e4188/hiveproxy/proxy_test.go), [`hivesim/docs_test.go`](https://github.com/core-coin/hive/blob/7abf3138375dda9162dce43d50a9fb5ce06e4188/hivesim/docs_test.go).

## Toolchain, setup, and validation

Detected language/platform: **Go**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `go.mod` declares Go 1.21; `hiveproxy/go.mod` declares Go 1.21.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Contributions`, `License`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/hive/blob/7abf3138375dda9162dce43d50a9fb5ce06e4188/README.md), [`cmd/hiveview/main.go`](https://github.com/core-coin/hive/blob/7abf3138375dda9162dce43d50a9fb5ce06e4188/cmd/hiveview/main.go), [`go.mod`](https://github.com/core-coin/hive/blob/7abf3138375dda9162dce43d50a9fb5ce06e4188/go.mod).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
