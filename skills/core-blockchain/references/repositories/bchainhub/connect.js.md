# bchainhub/connect.js

- Repository: https://github.com/bchainhub/connect.js
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `e4cd8930b2babf283463054b3932036495d20504`
- Local research checkout: `/tmp/core-blockchain-research/bchainhub/connect.js` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/bchainhub/connect.js/blob/e4cd8930b2babf283463054b3932036495d20504/README.md)

## Purpose and selection

Browser-side Connect v1 authentication adapters.
The [`README.md`](https://github.com/bchainhub/connect.js/blob/e4cd8930b2babf283463054b3932036495d20504/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src/index.ts`](https://github.com/bchainhub/connect.js/blob/e4cd8930b2babf283463054b3932036495d20504/src/index.ts).
Root build or package files: [`package.json`](https://github.com/bchainhub/connect.js/blob/e4cd8930b2babf283463054b3932036495d20504/package.json).
Source or project directories to inspect first: `scripts/`, `src/`.

## Toolchain, setup, and validation

Detected language/platform: **JavaScript / TypeScript**. This is based on the inspected tree and manifests, not a verified runtime environment.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `npm test`
- `npm run test:browser`
- `npm run test:package`

## Configuration, interfaces, and relationships

README sections to consult: `Nearby wallet apps`, `Wallet address validation`, `Blockchain providers and discovery`, `Native universal wallet API`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`bchainhub/better-connect`](better-connect.md), [`bchainhub/flutter_connect`](flutter_connect.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/bchainhub/connect.js/blob/e4cd8930b2babf283463054b3932036495d20504/README.md), [`src/index.ts`](https://github.com/bchainhub/connect.js/blob/e4cd8930b2babf283463054b3932036495d20504/src/index.ts), [`package.json`](https://github.com/bchainhub/connect.js/blob/e4cd8930b2babf283463054b3932036495d20504/package.json), [`.github/workflows/ci.yml`](https://github.com/bchainhub/connect.js/blob/e4cd8930b2babf283463054b3932036495d20504/.github/workflows/ci.yml), [`.github/workflows/release.yml`](https://github.com/bchainhub/connect.js/blob/e4cd8930b2babf283463054b3932036495d20504/.github/workflows/release.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
