# DataLayerHost/luna-sdk

- Repository: https://github.com/DataLayerHost/luna-sdk
- Research status: **source inspected via GitHub connector**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `4b0dee01ff729282c865998601244597d5bd16dd`
- Local research checkout: none; connected GitHub source used
- README: [`README.md`](https://github.com/DataLayerHost/luna-sdk/blob/4b0dee01ff729282c865998601244597d5bd16dd/README.md)

## Purpose and selection

TypeScript SDK for the Luna transport-independent communication layer.
The [`README.md`](https://github.com/DataLayerHost/luna-sdk/blob/4b0dee01ff729282c865998601244597d5bd16dd/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src/index.ts`](https://github.com/DataLayerHost/luna-sdk/blob/4b0dee01ff729282c865998601244597d5bd16dd/src/index.ts).
Root build or package files: [`package.json`](https://github.com/DataLayerHost/luna-sdk/blob/4b0dee01ff729282c865998601244597d5bd16dd/package.json).
Source or project directories to inspect first: `scripts/`, `src/`, `test-vectors/`.

## Toolchain, setup, and validation

Detected language/platform: **JavaScript / TypeScript**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `package.json` declares engines {"node": ">=22"}.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `npm test`
- `npm run build`

## Configuration, interfaces, and relationships

README sections to consult: `Use`, `Included`, `Development`, `License`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`DataLayerHost/luna_sdk`](luna_sdk.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/DataLayerHost/luna-sdk/blob/4b0dee01ff729282c865998601244597d5bd16dd/README.md), [`src/index.ts`](https://github.com/DataLayerHost/luna-sdk/blob/4b0dee01ff729282c865998601244597d5bd16dd/src/index.ts), [`package.json`](https://github.com/DataLayerHost/luna-sdk/blob/4b0dee01ff729282c865998601244597d5bd16dd/package.json), [`.github/workflows/release.yml`](https://github.com/DataLayerHost/luna-sdk/blob/4b0dee01ff729282c865998601244597d5bd16dd/.github/workflows/release.yml), [`.github/workflows/tests.yml`](https://github.com/DataLayerHost/luna-sdk/blob/4b0dee01ff729282c865998601244597d5bd16dd/.github/workflows/tests.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
