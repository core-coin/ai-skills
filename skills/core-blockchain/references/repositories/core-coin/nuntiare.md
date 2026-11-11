# core-coin/nuntiare

- Repository: https://github.com/core-coin/nuntiare
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `87aad6715f02a7495410966364b787b531690387`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/nuntiare` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/nuntiare/blob/87aad6715f02a7495410966364b787b531690387/README.md)

## Purpose and selection

Service that watches Core events and sends notifications.
The [`README.md`](https://github.com/core-coin/nuntiare/blob/87aad6715f02a7495410966364b787b531690387/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`cmd/nuntiare/main.go`](https://github.com/core-coin/nuntiare/blob/87aad6715f02a7495410966364b787b531690387/cmd/nuntiare/main.go).
Root build or package files: [`Dockerfile`](https://github.com/core-coin/nuntiare/blob/87aad6715f02a7495410966364b787b531690387/Dockerfile), [`Makefile`](https://github.com/core-coin/nuntiare/blob/87aad6715f02a7495410966364b787b531690387/Makefile), [`go.mod`](https://github.com/core-coin/nuntiare/blob/87aad6715f02a7495410966364b787b531690387/go.mod).
Source or project directories to inspect first: `cmd/`, `conf/`, `internal/`, `pkg/`.

## Toolchain, setup, and validation

Detected language/platform: **Go**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `go.mod` declares Go 1.22.0.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Features`, `Prerequisites`, `Quick Start (local Go environment)`, `Running with Docker Compose`, `Configuration`, `HTTP API`, `POST /subscription - Register Wallet`, `GET /issubscribed - Check Subscription Status`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/nuntiare/blob/87aad6715f02a7495410966364b787b531690387/README.md), [`cmd/nuntiare/main.go`](https://github.com/core-coin/nuntiare/blob/87aad6715f02a7495410966364b787b531690387/cmd/nuntiare/main.go), [`Dockerfile`](https://github.com/core-coin/nuntiare/blob/87aad6715f02a7495410966364b787b531690387/Dockerfile), [`Makefile`](https://github.com/core-coin/nuntiare/blob/87aad6715f02a7495410966364b787b531690387/Makefile), [`go.mod`](https://github.com/core-coin/nuntiare/blob/87aad6715f02a7495410966364b787b531690387/go.mod).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
