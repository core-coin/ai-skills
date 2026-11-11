# core-coin/helm-core

- Repository: https://github.com/core-coin/helm-core
- Research status: **source inspected via GitHub connector**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `718a05843682c8391ea55426da2e9a8c9b75d0c4`
- Local research checkout: none; connected GitHub source used
- README: [`README.md`](https://github.com/core-coin/helm-core/blob/718a05843682c8391ea55426da2e9a8c9b75d0c4/README.md)

## Purpose and selection

Helm chart for Core deployments.
The [`README.md`](https://github.com/core-coin/helm-core/blob/718a05843682c8391ea55426da2e9a8c9b75d0c4/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Source or project directories to inspect first: `ci/`, `scripts/`, `templates/`.

## Toolchain, setup, and validation

Detected language/platform: **Shell**. This is based on the inspected tree and manifests, not a verified runtime environment.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `TL;DR;`, `Introduction`, `Prerequisites`, `Installing the Chart`, `Uninstalling the Chart`, `Configuration`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`core-coin/core-playbook`](core-playbook.md), [`core-coin/go-core`](go-core.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/helm-core/blob/718a05843682c8391ea55426da2e9a8c9b75d0c4/README.md), [`.github/workflows/release.yaml`](https://github.com/core-coin/helm-core/blob/718a05843682c8391ea55426da2e9a8c9b75d0c4/.github/workflows/release.yaml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
