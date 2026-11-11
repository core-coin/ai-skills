# DataLayerHost/bchauth

- Repository: https://github.com/DataLayerHost/bchauth
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `b17a1761655f7c3207b6f849bc195d99046ed710`
- Local research checkout: `/tmp/core-blockchain-research/DataLayerHost/bchauth` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/DataLayerHost/bchauth/blob/b17a1761655f7c3207b6f849bc195d99046ed710/README.md)

## Purpose and selection

Caddy middleware that checks Core transaction-based access.
The [`README.md`](https://github.com/DataLayerHost/bchauth/blob/b17a1761655f7c3207b6f849bc195d99046ed710/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`bchauth.go`](https://github.com/DataLayerHost/bchauth/blob/b17a1761655f7c3207b6f849bc195d99046ed710/bchauth.go).
Root build or package files: [`go.mod`](https://github.com/DataLayerHost/bchauth/blob/b17a1761655f7c3207b6f849bc195d99046ed710/go.mod).

## Toolchain, setup, and validation

Detected language/platform: **Go**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `go.mod` declares Go 1.22.0.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Features`, `Installation`, `Configuration`, `Example Caddyfile`, `Parameters`, `Read-only Mode`, `License`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/DataLayerHost/bchauth/blob/b17a1761655f7c3207b6f849bc195d99046ed710/README.md), [`bchauth.go`](https://github.com/DataLayerHost/bchauth/blob/b17a1761655f7c3207b6f849bc195d99046ed710/bchauth.go), [`go.mod`](https://github.com/DataLayerHost/bchauth/blob/b17a1761655f7c3207b6f849bc195d99046ed710/go.mod).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
