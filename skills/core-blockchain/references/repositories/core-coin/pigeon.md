# core-coin/pigeon

- Repository: https://github.com/core-coin/pigeon
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `ee0250ca8c9e995e4f3c7b55116977adc7ee8999`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/pigeon` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/pigeon/blob/ee0250ca8c9e995e4f3c7b55116977adc7ee8999/README.md)

## Purpose and selection

Tooling to sign and transmit transactions.
The [`README.md`](https://github.com/core-coin/pigeon/blob/ee0250ca8c9e995e4f3c7b55116977adc7ee8999/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`main.go`](https://github.com/core-coin/pigeon/blob/ee0250ca8c9e995e4f3c7b55116977adc7ee8999/main.go).
Root build or package files: [`go.mod`](https://github.com/core-coin/pigeon/blob/ee0250ca8c9e995e4f3c7b55116977adc7ee8999/go.mod).
Source or project directories to inspect first: `cmd/`, `domain/`, `infrastructure/`, `logger/`, `pkg/`.

## Toolchain, setup, and validation

Detected language/platform: **Go**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `go.mod` declares Go 1.19.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Start the application`, `Flags`, `Example runs`, `Liability`, `File with transactions scheme :`, `License`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/pigeon/blob/ee0250ca8c9e995e4f3c7b55116977adc7ee8999/README.md), [`main.go`](https://github.com/core-coin/pigeon/blob/ee0250ca8c9e995e4f3c7b55116977adc7ee8999/main.go), [`go.mod`](https://github.com/core-coin/pigeon/blob/ee0250ca8c9e995e4f3c7b55116977adc7ee8999/go.mod), [`.github/workflows/build.yml`](https://github.com/core-coin/pigeon/blob/ee0250ca8c9e995e4f3c7b55116977adc7ee8999/.github/workflows/build.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
