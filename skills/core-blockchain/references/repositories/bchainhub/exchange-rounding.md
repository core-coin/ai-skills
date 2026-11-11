# bchainhub/exchange-rounding

- Repository: https://github.com/bchainhub/exchange-rounding
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `f5c74f8aa723cfd8191d959220de40862fd9a55c`
- Local research checkout: `/tmp/core-blockchain-research/bchainhub/exchange-rounding` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/bchainhub/exchange-rounding/blob/f5c74f8aa723cfd8191d959220de40862fd9a55c/README.md)

## Purpose and selection

Number formatting for exchange-facing financial values.
The [`README.md`](https://github.com/bchainhub/exchange-rounding/blob/f5c74f8aa723cfd8191d959220de40862fd9a55c/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src/index.ts`](https://github.com/bchainhub/exchange-rounding/blob/f5c74f8aa723cfd8191d959220de40862fd9a55c/src/index.ts).
Root build or package files: [`package.json`](https://github.com/bchainhub/exchange-rounding/blob/f5c74f8aa723cfd8191d959220de40862fd9a55c/package.json).
Source or project directories to inspect first: `src/`, `types/`.
Examples or tests visible in the tree: [`test/index.test.ts`](https://github.com/bchainhub/exchange-rounding/blob/f5c74f8aa723cfd8191d959220de40862fd9a55c/test/index.test.ts).

## Toolchain, setup, and validation

Detected language/platform: **JavaScript / TypeScript**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `package.json` declares engines {"node": ">=13.2.0"}.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Features`, `Installation`, `Usage`, `Basic Usage`, `Advanced Usage with Custom Currencies`, `API Reference`, `new ExchNumberFormat(locales, options)`, `Rounding Modes`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/bchainhub/exchange-rounding/blob/f5c74f8aa723cfd8191d959220de40862fd9a55c/README.md), [`src/index.ts`](https://github.com/bchainhub/exchange-rounding/blob/f5c74f8aa723cfd8191d959220de40862fd9a55c/src/index.ts), [`package.json`](https://github.com/bchainhub/exchange-rounding/blob/f5c74f8aa723cfd8191d959220de40862fd9a55c/package.json), [`.github/workflows/publish.yml`](https://github.com/bchainhub/exchange-rounding/blob/f5c74f8aa723cfd8191d959220de40862fd9a55c/.github/workflows/publish.yml), [`.github/workflows/test.yml`](https://github.com/bchainhub/exchange-rounding/blob/f5c74f8aa723cfd8191d959220de40862fd9a55c/.github/workflows/test.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
