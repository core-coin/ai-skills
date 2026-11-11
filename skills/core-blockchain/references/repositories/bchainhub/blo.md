# bchainhub/blo

- Repository: https://github.com/bchainhub/blo
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `59981c4aabaac30cde42589a4d82af5c63f44f5f`
- Local research checkout: `/tmp/core-blockchain-research/bchainhub/blo` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/bchainhub/blo/blob/59981c4aabaac30cde42589a4d82af5c63f44f5f/README.md)

## Purpose and selection

Blockchain identicon generator.
The [`README.md`](https://github.com/bchainhub/blo/blob/59981c4aabaac30cde42589a4d82af5c63f44f5f/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src/index.ts`](https://github.com/bchainhub/blo/blob/59981c4aabaac30cde42589a4d82af5c63f44f5f/src/index.ts).
Root build or package files: [`package.json`](https://github.com/bchainhub/blo/blob/59981c4aabaac30cde42589a4d82af5c63f44f5f/package.json).
Source or project directories to inspect first: `benchmark/`, `demos/`, `src/`.

## Toolchain, setup, and validation

Detected language/platform: **JavaScript / TypeScript**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `package.json` declares engines {"node": ">=16"}.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Features`, `Library Comparison`, `Getting Started`, `React / Vue / Others`, `API`, `blo(address: Address, options?: BloOptions): string`, `bloSvg(address: Address, options?: BloOptions): string`, `bloImage(address: Address, options?: BloOptions): BloImage`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/bchainhub/blo/blob/59981c4aabaac30cde42589a4d82af5c63f44f5f/README.md), [`src/index.ts`](https://github.com/bchainhub/blo/blob/59981c4aabaac30cde42589a4d82af5c63f44f5f/src/index.ts), [`package.json`](https://github.com/bchainhub/blo/blob/59981c4aabaac30cde42589a4d82af5c63f44f5f/package.json), [`.github/workflows/publish.yml`](https://github.com/bchainhub/blo/blob/59981c4aabaac30cde42589a4d82af5c63f44f5f/.github/workflows/publish.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
