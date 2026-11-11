# bchainhub/payto-rl

- Repository: https://github.com/bchainhub/payto-rl
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `5c751e1f4df86b00f99051987cb4a6fceda5d1b0`
- Local research checkout: `/tmp/core-blockchain-research/bchainhub/payto-rl` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/bchainhub/payto-rl/blob/5c751e1f4df86b00f99051987cb4a6fceda5d1b0/README.md)

## Purpose and selection

TypeScript parser and formatter for Payto Resource Locators.
The [`README.md`](https://github.com/bchainhub/payto-rl/blob/5c751e1f4df86b00f99051987cb4a6fceda5d1b0/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src/index.ts`](https://github.com/bchainhub/payto-rl/blob/5c751e1f4df86b00f99051987cb4a6fceda5d1b0/src/index.ts).
Root build or package files: [`package.json`](https://github.com/bchainhub/payto-rl/blob/5c751e1f4df86b00f99051987cb4a6fceda5d1b0/package.json).
Source or project directories to inspect first: `src/`.
Examples or tests visible in the tree: [`test/btcPrecision.test.ts`](https://github.com/bchainhub/payto-rl/blob/5c751e1f4df86b00f99051987cb4a6fceda5d1b0/test/btcPrecision.test.ts), [`test/emv.test.ts`](https://github.com/bchainhub/payto-rl/blob/5c751e1f4df86b00f99051987cb4a6fceda5d1b0/test/emv.test.ts), [`test/formats.test.ts`](https://github.com/bchainhub/payto-rl/blob/5c751e1f4df86b00f99051987cb4a6fceda5d1b0/test/formats.test.ts), [`test/payqr.test.ts`](https://github.com/bchainhub/payto-rl/blob/5c751e1f4df86b00f99051987cb4a6fceda5d1b0/test/payqr.test.ts).

## Toolchain, setup, and validation

Detected language/platform: **JavaScript / TypeScript**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `package.json` declares engines {"node": ">=16"}.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Features`, `Installation`, `Usage`, `API Reference`, `Constructor`, `Properties`, `Methods`, `Type Safety`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`bchainhub/flutter_paytorl`](flutter_paytorl.md), [`core-laboratories/payto`](../core-laboratories/payto.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/bchainhub/payto-rl/blob/5c751e1f4df86b00f99051987cb4a6fceda5d1b0/README.md), [`src/index.ts`](https://github.com/bchainhub/payto-rl/blob/5c751e1f4df86b00f99051987cb4a6fceda5d1b0/src/index.ts), [`package.json`](https://github.com/bchainhub/payto-rl/blob/5c751e1f4df86b00f99051987cb4a6fceda5d1b0/package.json), [`.github/workflows/publish.yml`](https://github.com/bchainhub/payto-rl/blob/5c751e1f4df86b00f99051987cb4a6fceda5d1b0/.github/workflows/publish.yml), [`.github/workflows/test.yml`](https://github.com/bchainhub/payto-rl/blob/5c751e1f4df86b00f99051987cb4a6fceda5d1b0/.github/workflows/test.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
