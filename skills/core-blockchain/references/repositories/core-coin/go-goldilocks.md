# core-coin/go-goldilocks

- Repository: https://github.com/core-coin/go-goldilocks
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `c399187e68d118fa77495c09bfbea3d75449f598`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/go-goldilocks` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/go-goldilocks/blob/c399187e68d118fa77495c09bfbea3d75449f598/README.md)

## Purpose and selection

Go bindings for Ed448 Goldilocks cryptography.
The [`README.md`](https://github.com/core-coin/go-goldilocks/blob/c399187e68d118fa77495c09bfbea3d75449f598/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`goldilocks.go`](https://github.com/core-coin/go-goldilocks/blob/c399187e68d118fa77495c09bfbea3d75449f598/goldilocks.go).
Root build or package files: [`go.mod`](https://github.com/core-coin/go-goldilocks/blob/c399187e68d118fa77495c09bfbea3d75449f598/go.mod).
Source or project directories to inspect first: `build/`.
Examples or tests visible in the tree: [`goldilocks_test.go`](https://github.com/core-coin/go-goldilocks/blob/c399187e68d118fa77495c09bfbea3d75449f598/goldilocks_test.go).

## Toolchain, setup, and validation

Detected language/platform: **Go**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `go.mod` declares Go 1.21.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Golang Ed448-Goldilocks bindings`, `How to use`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`core-coin/libgoldilocks`](libgoldilocks.md), [`core-coin/ed448`](ed448.md), [`core-coin/ed448-rs`](ed448-rs.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/go-goldilocks/blob/c399187e68d118fa77495c09bfbea3d75449f598/README.md), [`goldilocks.go`](https://github.com/core-coin/go-goldilocks/blob/c399187e68d118fa77495c09bfbea3d75449f598/goldilocks.go), [`go.mod`](https://github.com/core-coin/go-goldilocks/blob/c399187e68d118fa77495c09bfbea3d75449f598/go.mod), [`.github/workflows/build.yml`](https://github.com/core-coin/go-goldilocks/blob/c399187e68d118fa77495c09bfbea3d75449f598/.github/workflows/build.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
