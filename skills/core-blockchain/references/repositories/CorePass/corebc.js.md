# CorePass/corebc.js

- Repository: https://github.com/CorePass/corebc.js
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `caedc524ad4a77d35474dbeebd66fe6332ba667c`
- Local research checkout: `/tmp/core-blockchain-research/CorePass/corebc.js` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/CorePass/corebc.js/blob/caedc524ad4a77d35474dbeebd66fe6332ba667c/README.md)

## Purpose and selection

JavaScript and TypeScript tools for Core wallets and signing.
The [`README.md`](https://github.com/CorePass/corebc.js/blob/caedc524ad4a77d35474dbeebd66fe6332ba667c/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src.ts/index.ts`](https://github.com/CorePass/corebc.js/blob/caedc524ad4a77d35474dbeebd66fe6332ba667c/src.ts/index.ts).
Root build or package files: [`package.json`](https://github.com/CorePass/corebc.js/blob/caedc524ad4a77d35474dbeebd66fe6332ba667c/package.json).
Source or project directories to inspect first: `scripts/`, `src.ts/`, `testcases/`.

## Toolchain, setup, and validation

Detected language/platform: **JavaScript / TypeScript**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `package.json` declares engines {"node": ">=22.12.0"}.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Install`, `Wallets and contracts`, `CIP metadata`, `IPFS and custom units`, `Browser bundles`, `Development`, `License`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`CorePass/core_web3dart`](core_web3dart.md), [`core-coin/corebc-rs`](../core-coin/corebc-rs.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/CorePass/corebc.js/blob/caedc524ad4a77d35474dbeebd66fe6332ba667c/README.md), [`src.ts/index.ts`](https://github.com/CorePass/corebc.js/blob/caedc524ad4a77d35474dbeebd66fe6332ba667c/src.ts/index.ts), [`package.json`](https://github.com/CorePass/corebc.js/blob/caedc524ad4a77d35474dbeebd66fe6332ba667c/package.json), [`.github/workflows/nodejs.yml`](https://github.com/CorePass/corebc.js/blob/caedc524ad4a77d35474dbeebd66fe6332ba667c/.github/workflows/nodejs.yml), [`.github/workflows/publish-npm.yml`](https://github.com/CorePass/corebc.js/blob/caedc524ad4a77d35474dbeebd66fe6332ba667c/.github/workflows/publish-npm.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
