# core-coin/libgoldilocks

- Repository: https://github.com/core-coin/libgoldilocks
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `f9177d5efcade6254711d20262805e000896a0e7`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/libgoldilocks` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/libgoldilocks/blob/f9177d5efcade6254711d20262805e000896a0e7/README.md)

## Purpose and selection

Native Ed448 Goldilocks cryptography library.
The [`README.md`](https://github.com/core-coin/libgoldilocks/blob/f9177d5efcade6254711d20262805e000896a0e7/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src/eddsa.c`](https://github.com/core-coin/libgoldilocks/blob/f9177d5efcade6254711d20262805e000896a0e7/src/eddsa.c).
Source or project directories to inspect first: `m4/`, `pkgconfig/`, `python/`, `src/`.

## Toolchain, setup, and validation

Detected language/platform: **C, Python**. This is based on the inspected tree and manifests, not a verified runtime environment.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `make test`

## Configuration, interfaces, and relationships

README sections to consult: `Building the library`, `Using the library`, `General elliptic curve operations.`, `CFRG cryptosystems.`, `Symmetric crypto and hashing`, `Internals`, `Licensing`, `Caveats`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`core-coin/go-goldilocks`](go-goldilocks.md), [`core-coin/ed448`](ed448.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/libgoldilocks/blob/f9177d5efcade6254711d20262805e000896a0e7/README.md), [`src/eddsa.c`](https://github.com/core-coin/libgoldilocks/blob/f9177d5efcade6254711d20262805e000896a0e7/src/eddsa.c), [`.github/workflows/build.yml`](https://github.com/core-coin/libgoldilocks/blob/f9177d5efcade6254711d20262805e000896a0e7/.github/workflows/build.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
