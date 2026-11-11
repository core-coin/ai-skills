# core-coin/go-core

- Repository: https://github.com/core-coin/go-core
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `a091fe2d31ea1d3926db64da7621f26ed01c92a9`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/go-core` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/README.md)

## Purpose and selection

Go client implementation used as the compatibility baseline for Core network behavior.
The [`README.md`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`cmd/cvm/main.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/cmd/cvm/main.go).
Root build or package files: [`Dockerfile`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/Dockerfile), [`Makefile`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/Makefile), [`go.mod`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/go.mod).
Source or project directories to inspect first: `accounts/`, `build/`, `cmd/`, `common/`, `consensus/`.
Examples or tests visible in the tree: [`accounts/abi/abi_test.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/accounts/abi/abi_test.go), [`accounts/abi/bind/backends/simulated_test.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/accounts/abi/bind/backends/simulated_test.go), [`accounts/abi/bind/base_test.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/accounts/abi/bind/base_test.go), [`accounts/abi/bind/bind_test.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/accounts/abi/bind/bind_test.go).

## Toolchain, setup, and validation

Detected language/platform: **Go**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `go.mod` declares Go 1.21.
The README says Go 1.14 or later for source builds, while `go.mod` declares Go 1.21. Resolve the toolchain against current CI and source before building.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `make gocore`
- `make all`

## Configuration, interfaces, and relationships

README sections to consult: `Source Building`, `To build gocore on Linux or Mac`, `To build or run on Windows`, `ICAN Network Prefixes`, `Executables`, `Full Node on the Main CORE Network`, `A Full Node on the Devín Network (PoW)`, `Configuration`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`core-coin/cvm`](cvm.md), [`core-coin/RandomY`](RandomY.md), [`core-coin/core-diff`](core-diff.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/README.md), [`cmd/cvm/main.go`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/cmd/cvm/main.go), [`Dockerfile`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/Dockerfile), [`Makefile`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/Makefile), [`go.mod`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/go.mod), [`.github/workflows/build.yml`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/.github/workflows/build.yml), [`.github/workflows/docker.yml`](https://github.com/core-coin/go-core/blob/a091fe2d31ea1d3926db64da7621f26ed01c92a9/.github/workflows/docker.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
