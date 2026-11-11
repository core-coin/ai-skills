# core-laboratories/payto

- Repository: https://github.com/core-laboratories/payto
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `2e5d570d189d072e4071a7a9438635e4e76a4d4c`
- Local research checkout: `/tmp/core-blockchain-research/core-laboratories/payto` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-laboratories/payto/blob/2e5d570d189d072e4071a7a9438635e4e76a4d4c/README.md)

## Purpose and selection

PayTo money transfer project.
The [`README.md`](https://github.com/core-laboratories/payto/blob/2e5d570d189d072e4071a7a9438635e4e76a4d4c/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src/i18n/index.ts`](https://github.com/core-laboratories/payto/blob/2e5d570d189d072e4071a7a9438635e4e76a4d4c/src/i18n/index.ts).
Root build or package files: [`package.json`](https://github.com/core-laboratories/payto/blob/2e5d570d189d072e4071a7a9438635e4e76a4d4c/package.json).
Source or project directories to inspect first: `src/`, `static/`, `test-results/`.
Examples or tests visible in the tree: [`src/lib/epc/payload.test.ts`](https://github.com/core-laboratories/payto/blob/2e5d570d189d072e4071a7a9438635e4e76a4d4c/src/lib/epc/payload.test.ts), [`src/lib/helpers/amount-currency.test.ts`](https://github.com/core-laboratories/payto/blob/2e5d570d189d072e4071a7a9438635e4e76a4d4c/src/lib/helpers/amount-currency.test.ts), [`src/lib/paypass/generation.test.ts`](https://github.com/core-laboratories/payto/blob/2e5d570d189d072e4071a7a9438635e4e76a4d4c/src/lib/paypass/generation.test.ts), [`src/lib/payqr/barcode.test.ts`](https://github.com/core-laboratories/payto/blob/2e5d570d189d072e4071a7a9438635e4e76a4d4c/src/lib/payqr/barcode.test.ts).

## Toolchain, setup, and validation

Detected language/platform: **JavaScript / TypeScript**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `package.json` declares engines {"node": ">=22.17"}.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `npm run build`

## Configuration, interfaces, and relationships

README sections to consult: `Technical Specifications and Organizational Notes`, `Project Initialization`, `Development`, `Building`, `Pro Features`, `Organization Plan`, `Pass Generation API`, `PayTo Libraries`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-laboratories/payto/blob/2e5d570d189d072e4071a7a9438635e4e76a4d4c/README.md), [`src/i18n/index.ts`](https://github.com/core-laboratories/payto/blob/2e5d570d189d072e4071a7a9438635e4e76a4d4c/src/i18n/index.ts), [`package.json`](https://github.com/core-laboratories/payto/blob/2e5d570d189d072e4071a7a9438635e4e76a4d4c/package.json).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
