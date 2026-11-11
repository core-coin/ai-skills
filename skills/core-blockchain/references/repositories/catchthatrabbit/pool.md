# catchthatrabbit/pool

- Repository: https://github.com/catchthatrabbit/pool
- Research status: **source inspected via GitHub connector**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `2fe84056362bd65fdff341b776984db79be3a479`
- Local research checkout: none; connected GitHub source used
- README: [`README.md`](https://github.com/catchthatrabbit/pool/blob/2fe84056362bd65fdff341b776984db79be3a479/README.md)

## Purpose and selection

Core mining pool service with HTTP and Stratum interfaces.
The [`README.md`](https://github.com/catchthatrabbit/pool/blob/2fe84056362bd65fdff341b776984db79be3a479/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`main.go`](https://github.com/catchthatrabbit/pool/blob/2fe84056362bd65fdff341b776984db79be3a479/main.go).
Root build or package files: [`Dockerfile`](https://github.com/catchthatrabbit/pool/blob/2fe84056362bd65fdff341b776984db79be3a479/Dockerfile), [`Makefile`](https://github.com/catchthatrabbit/pool/blob/2fe84056362bd65fdff341b776984db79be3a479/Makefile), [`go.mod`](https://github.com/catchthatrabbit/pool/blob/2fe84056362bd65fdff341b776984db79be3a479/go.mod).
Source or project directories to inspect first: `accs/`, `api/`, `build/`, `misc/`, `payouts/`.
Examples or tests visible in the tree: [`payouts/unlocker_test.go`](https://github.com/catchthatrabbit/pool/blob/2fe84056362bd65fdff341b776984db79be3a479/payouts/unlocker_test.go), [`storage/redis_test.go`](https://github.com/catchthatrabbit/pool/blob/2fe84056362bd65fdff341b776984db79be3a479/storage/redis_test.go), [`www/tests/test-helper.js`](https://github.com/catchthatrabbit/pool/blob/2fe84056362bd65fdff341b776984db79be3a479/www/tests/test-helper.js).

## Toolchain, setup, and validation

Detected language/platform: **Go, JavaScript / TypeScript**. This is based on the inspected tree and manifests, not a verified runtime environment.
The README mentions ECIP-1017 reward calculation and Parity RPC failover. Verify those assumptions against the current Core network and client before deployment.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Open Source Core Mining Pool`, `Features`, `Community / Support`, `Building on Linux`, `Running Pool`, `Building Frontend`, `Configuration`, `Notes`.
Example configuration files: [`config.example.json`](https://github.com/catchthatrabbit/pool/blob/2fe84056362bd65fdff341b776984db79be3a479/config.example.json). Do not copy example secrets into production.
Related references by task (not verified direct dependencies): [`catchthatrabbit/coreminer`](coreminer.md), [`core-coin/RandomY`](../core-coin/RandomY.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/catchthatrabbit/pool/blob/2fe84056362bd65fdff341b776984db79be3a479/README.md), [`main.go`](https://github.com/catchthatrabbit/pool/blob/2fe84056362bd65fdff341b776984db79be3a479/main.go), [`.github/workflows/build.yml`](https://github.com/catchthatrabbit/pool/blob/2fe84056362bd65fdff341b776984db79be3a479/.github/workflows/build.yml), [`.github/workflows/deploy_brts_public.yaml`](https://github.com/catchthatrabbit/pool/blob/2fe84056362bd65fdff341b776984db79be3a479/.github/workflows/deploy_brts_public.yaml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
