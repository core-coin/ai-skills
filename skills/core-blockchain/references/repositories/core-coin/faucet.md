# core-coin/faucet

- Repository: https://github.com/core-coin/faucet
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `a85f50feba5346d428c691d225decf2c8d650eff`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/faucet` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/faucet/blob/a85f50feba5346d428c691d225decf2c8d650eff/README.md)

## Purpose and selection

Faucet application for private and test networks.
The [`README.md`](https://github.com/core-coin/faucet/blob/a85f50feba5346d428c691d225decf2c8d650eff/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`main.go`](https://github.com/core-coin/faucet/blob/a85f50feba5346d428c691d225decf2c8d650eff/main.go).
Root build or package files: [`Dockerfile`](https://github.com/core-coin/faucet/blob/a85f50feba5346d428c691d225decf2c8d650eff/Dockerfile), [`go.mod`](https://github.com/core-coin/faucet/blob/a85f50feba5346d428c691d225decf2c8d650eff/go.mod), [`package.json`](https://github.com/core-coin/faucet/blob/a85f50feba5346d428c691d225decf2c8d650eff/package.json).
Source or project directories to inspect first: `cmd/`, `internal/`, `keystore/`, `web/`.
Examples or tests visible in the tree: [`internal/chain/keystore_test.go`](https://github.com/core-coin/faucet/blob/a85f50feba5346d428c691d225decf2c8d650eff/internal/chain/keystore_test.go), [`internal/chain/util_test.go`](https://github.com/core-coin/faucet/blob/a85f50feba5346d428c691d225decf2c8d650eff/internal/chain/util_test.go).

## Toolchain, setup, and validation

Detected language/platform: **Go, JavaScript / TypeScript**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `go.mod` declares Go 1.16.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `yarn build`

## Configuration, interfaces, and relationships

README sections to consult: `Features`, `Get started`, `Prerequisites`, `Installation`, `Usage`, `Configuration`, `Docker deployment`, `Heroku deployment`.
Environment variable names shown in the README: `KEYSTORE`, `PRIVATE_KEY`, `WEB3_PROVIDER`. Verify required values and scope before use.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/faucet/blob/a85f50feba5346d428c691d225decf2c8d650eff/README.md), [`main.go`](https://github.com/core-coin/faucet/blob/a85f50feba5346d428c691d225decf2c8d650eff/main.go), [`Dockerfile`](https://github.com/core-coin/faucet/blob/a85f50feba5346d428c691d225decf2c8d650eff/Dockerfile), [`go.mod`](https://github.com/core-coin/faucet/blob/a85f50feba5346d428c691d225decf2c8d650eff/go.mod), [`package.json`](https://github.com/core-coin/faucet/blob/a85f50feba5346d428c691d225decf2c8d650eff/package.json), [`.github/workflows/build.yml`](https://github.com/core-coin/faucet/blob/a85f50feba5346d428c691d225decf2c8d650eff/.github/workflows/build.yml), [`.github/workflows/deploy_testnet.yaml`](https://github.com/core-coin/faucet/blob/a85f50feba5346d428c691d225decf2c8d650eff/.github/workflows/deploy_testnet.yaml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
