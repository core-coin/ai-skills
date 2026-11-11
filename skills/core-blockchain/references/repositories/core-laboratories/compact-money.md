# core-laboratories/compact-money

- Repository: https://github.com/core-laboratories/compact-money
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `3cd3083ce5b8aed31b58ae9ff84ab7d8b3a0d15c`
- Local research checkout: `/tmp/core-blockchain-research/core-laboratories/compact-money` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-laboratories/compact-money/blob/3cd3083ce5b8aed31b58ae9ff84ab7d8b3a0d15c/README.md)

## Purpose and selection

Compact money data representation; compare its API with compact_money.
The [`README.md`](https://github.com/core-laboratories/compact-money/blob/3cd3083ce5b8aed31b58ae9ff84ab7d8b3a0d15c/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src/index.ts`](https://github.com/core-laboratories/compact-money/blob/3cd3083ce5b8aed31b58ae9ff84ab7d8b3a0d15c/src/index.ts).
Root build or package files: [`package.json`](https://github.com/core-laboratories/compact-money/blob/3cd3083ce5b8aed31b58ae9ff84ab7d8b3a0d15c/package.json).
Source or project directories to inspect first: `scripts/`, `src/`.
Examples or tests visible in the tree: [`tests/compact.test.ts`](https://github.com/core-laboratories/compact-money/blob/3cd3083ce5b8aed31b58ae9ff84ab7d8b3a0d15c/tests/compact.test.ts), [`tests/rounding.test.ts`](https://github.com/core-laboratories/compact-money/blob/3cd3083ce5b8aed31b58ae9ff84ab7d8b3a0d15c/tests/rounding.test.ts).

## Toolchain, setup, and validation

Detected language/platform: **JavaScript / TypeScript**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `package.json` declares engines {"node": ">=22"}.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `npm run test:package`

## Configuration, interfaces, and relationships

README sections to consult: `Installation`, `Usage`, `API`, `Units and rounding`, `Decimal places without rounding`, `Currency and presentation`, `Numeric precision`, `Development and releases`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`core-laboratories/compact_money`](compact_money.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-laboratories/compact-money/blob/3cd3083ce5b8aed31b58ae9ff84ab7d8b3a0d15c/README.md), [`src/index.ts`](https://github.com/core-laboratories/compact-money/blob/3cd3083ce5b8aed31b58ae9ff84ab7d8b3a0d15c/src/index.ts), [`package.json`](https://github.com/core-laboratories/compact-money/blob/3cd3083ce5b8aed31b58ae9ff84ab7d8b3a0d15c/package.json), [`.github/workflows/release.yml`](https://github.com/core-laboratories/compact-money/blob/3cd3083ce5b8aed31b58ae9ff84ab7d8b3a0d15c/.github/workflows/release.yml), [`.github/workflows/test.yml`](https://github.com/core-laboratories/compact-money/blob/3cd3083ce5b8aed31b58ae9ff84ab7d8b3a0d15c/.github/workflows/test.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
