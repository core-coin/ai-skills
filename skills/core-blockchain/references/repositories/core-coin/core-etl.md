# core-coin/core-etl

- Repository: https://github.com/core-coin/core-etl
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `8395ea26a7e952331732cd93b5258e61379ccd30`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/core-etl` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/core-etl/blob/8395ea26a7e952331732cd93b5258e61379ccd30/README.md)

## Purpose and selection

Extraction and transformation of Core chain data.
The [`README.md`](https://github.com/core-coin/core-etl/blob/8395ea26a7e952331732cd93b5258e61379ccd30/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`crates/etl/src/lib.rs`](https://github.com/core-coin/core-etl/blob/8395ea26a7e952331732cd93b5258e61379ccd30/crates/etl/src/lib.rs).
Root build or package files: [`Cargo.toml`](https://github.com/core-coin/core-etl/blob/8395ea26a7e952331732cd93b5258e61379ccd30/Cargo.toml), [`Dockerfile`](https://github.com/core-coin/core-etl/blob/8395ea26a7e952331732cd93b5258e61379ccd30/Dockerfile), [`Makefile`](https://github.com/core-coin/core-etl/blob/8395ea26a7e952331732cd93b5258e61379ccd30/Makefile).
Source or project directories to inspect first: `bin/`, `crates/`, `docker-compose/`.

## Toolchain, setup, and validation

Detected language/platform: **Rust**. This is based on the inspected tree and manifests, not a verified runtime environment.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `cargo build --release`
- `make build-postgres`
- `make build-libsql`

## Configuration, interfaces, and relationships

README sections to consult: `Table of Contents`, `Introduction`, `Installation`, `Usage`, `Commands`, `Flags`, `Makefile`, `Docker`.
Environment variable names shown in the README: `MODULES`, `NETWORK`, `SQLITE3_PATH`, `STORAGE`, `TABLES_PREFIX`. Verify required values and scope before use.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/core-etl/blob/8395ea26a7e952331732cd93b5258e61379ccd30/README.md), [`crates/etl/src/lib.rs`](https://github.com/core-coin/core-etl/blob/8395ea26a7e952331732cd93b5258e61379ccd30/crates/etl/src/lib.rs), [`Cargo.toml`](https://github.com/core-coin/core-etl/blob/8395ea26a7e952331732cd93b5258e61379ccd30/Cargo.toml), [`Dockerfile`](https://github.com/core-coin/core-etl/blob/8395ea26a7e952331732cd93b5258e61379ccd30/Dockerfile), [`Makefile`](https://github.com/core-coin/core-etl/blob/8395ea26a7e952331732cd93b5258e61379ccd30/Makefile), [`.github/workflows/ci.yml`](https://github.com/core-coin/core-etl/blob/8395ea26a7e952331732cd93b5258e61379ccd30/.github/workflows/ci.yml), [`.github/workflows/docker.yml`](https://github.com/core-coin/core-etl/blob/8395ea26a7e952331732cd93b5258e61379ccd30/.github/workflows/docker.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
