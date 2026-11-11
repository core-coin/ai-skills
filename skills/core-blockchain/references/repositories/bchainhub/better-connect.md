# bchainhub/better-connect

- Repository: https://github.com/bchainhub/better-connect
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `eea920ea38513181527fc5dca0c7a706d8318fea`
- Local research checkout: `/tmp/core-blockchain-research/bchainhub/better-connect` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/bchainhub/better-connect/blob/eea920ea38513181527fc5dca0c7a706d8318fea/README.md)

## Purpose and selection

Backend authentication service for Connect v1.
The [`README.md`](https://github.com/bchainhub/better-connect/blob/eea920ea38513181527fc5dca0c7a706d8318fea/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src/index.ts`](https://github.com/bchainhub/better-connect/blob/eea920ea38513181527fc5dca0c7a706d8318fea/src/index.ts).
Root build or package files: [`package.json`](https://github.com/bchainhub/better-connect/blob/eea920ea38513181527fc5dca0c7a706d8318fea/package.json).
Source or project directories to inspect first: `scripts/`, `src/`.
Examples or tests visible in the tree: [`test/client-types.ts`](https://github.com/bchainhub/better-connect/blob/eea920ea38513181527fc5dca0c7a706d8318fea/test/client-types.ts).

## Toolchain, setup, and validation

Detected language/platform: **JavaScript / TypeScript**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `package.json` declares engines {"node": ">=22"}.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `npm test`
- `npm run test:package`

## Configuration, interfaces, and relationships

README sections to consult: `Wallet address validation`, `License`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`bchainhub/connect.js`](connect.js.md), [`bchainhub/flutter_connect`](flutter_connect.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/bchainhub/better-connect/blob/eea920ea38513181527fc5dca0c7a706d8318fea/README.md), [`src/index.ts`](https://github.com/bchainhub/better-connect/blob/eea920ea38513181527fc5dca0c7a706d8318fea/src/index.ts), [`package.json`](https://github.com/bchainhub/better-connect/blob/eea920ea38513181527fc5dca0c7a706d8318fea/package.json), [`.github/workflows/ci.yml`](https://github.com/bchainhub/better-connect/blob/eea920ea38513181527fc5dca0c7a706d8318fea/.github/workflows/ci.yml), [`.github/workflows/interop.yml`](https://github.com/bchainhub/better-connect/blob/eea920ea38513181527fc5dca0c7a706d8318fea/.github/workflows/interop.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
