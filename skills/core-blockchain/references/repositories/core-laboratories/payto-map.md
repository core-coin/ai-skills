# core-laboratories/payto-map

- Repository: https://github.com/core-laboratories/payto-map
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `11b4966e5cb9ab0cc2fcdb0375a3bf66a25153e4`
- Local research checkout: `/tmp/core-blockchain-research/core-laboratories/payto-map` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-laboratories/payto-map/blob/11b4966e5cb9ab0cc2fcdb0375a3bf66a25153e4/README.md)

## Purpose and selection

Cloudflare Worker API for PayTo map locations.
The [`README.md`](https://github.com/core-laboratories/payto-map/blob/11b4966e5cb9ab0cc2fcdb0375a3bf66a25153e4/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src/index.ts`](https://github.com/core-laboratories/payto-map/blob/11b4966e5cb9ab0cc2fcdb0375a3bf66a25153e4/src/index.ts).
Root build or package files: [`package.json`](https://github.com/core-laboratories/payto-map/blob/11b4966e5cb9ab0cc2fcdb0375a3bf66a25153e4/package.json).
Source or project directories to inspect first: `db/`, `src/`.
Examples or tests visible in the tree: [`examples/fetch-locations.ts`](https://github.com/core-laboratories/payto-map/blob/11b4966e5cb9ab0cc2fcdb0375a3bf66a25153e4/examples/fetch-locations.ts).

## Toolchain, setup, and validation

Detected language/platform: **JavaScript / TypeScript**. This is based on the inspected tree and manifests, not a verified runtime environment.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Project purpose`, `Setup commands`, `Production D1 commands`, `DNS / route setup`, `Integration possibilities`, `A. Direct frontend fetch from PayToonl /map`, `B. MapLibre GeoJSON source`, `C. Filtered API`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-laboratories/payto-map/blob/11b4966e5cb9ab0cc2fcdb0375a3bf66a25153e4/README.md), [`src/index.ts`](https://github.com/core-laboratories/payto-map/blob/11b4966e5cb9ab0cc2fcdb0375a3bf66a25153e4/src/index.ts), [`package.json`](https://github.com/core-laboratories/payto-map/blob/11b4966e5cb9ab0cc2fcdb0375a3bf66a25153e4/package.json).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
