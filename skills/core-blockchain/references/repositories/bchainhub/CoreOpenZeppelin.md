# bchainhub/CoreOpenZeppelin

- Repository: https://github.com/bchainhub/CoreOpenZeppelin
- Research status: **source inspected via GitHub connector**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `4e35b0b4078bc0aa532c740e58f30dddd6b17574`
- Local research checkout: none; connected GitHub source used
- README: [`README.md`](https://github.com/bchainhub/CoreOpenZeppelin/blob/4e35b0b4078bc0aa532c740e58f30dddd6b17574/README.md)

## Purpose and selection

Smart-contract library fork; inspect compatibility with Core tooling before reuse.
The [`README.md`](https://github.com/bchainhub/CoreOpenZeppelin/blob/4e35b0b4078bc0aa532c740e58f30dddd6b17574/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`scripts/solhint-custom/index.js`](https://github.com/bchainhub/CoreOpenZeppelin/blob/4e35b0b4078bc0aa532c740e58f30dddd6b17574/scripts/solhint-custom/index.js).
Root build or package files: [`.gitmodules`](https://github.com/bchainhub/CoreOpenZeppelin/blob/4e35b0b4078bc0aa532c740e58f30dddd6b17574/.gitmodules), [`package.json`](https://github.com/bchainhub/CoreOpenZeppelin/blob/4e35b0b4078bc0aa532c740e58f30dddd6b17574/package.json).
Source or project directories to inspect first: `audits/`, `certora/`, `contracts/`, `hardhat/`, `scripts/`.
Examples or tests visible in the tree: [`test/access/AccessControl.test.js`](https://github.com/bchainhub/CoreOpenZeppelin/blob/4e35b0b4078bc0aa532c740e58f30dddd6b17574/test/access/AccessControl.test.js), [`test/access/Ownable.test.js`](https://github.com/bchainhub/CoreOpenZeppelin/blob/4e35b0b4078bc0aa532c740e58f30dddd6b17574/test/access/Ownable.test.js), [`test/access/Ownable2Step.test.js`](https://github.com/bchainhub/CoreOpenZeppelin/blob/4e35b0b4078bc0aa532c740e58f30dddd6b17574/test/access/Ownable2Step.test.js), [`test/access/extensions/AccessControlDefaultAdminRules.test.js`](https://github.com/bchainhub/CoreOpenZeppelin/blob/4e35b0b4078bc0aa532c740e58f30dddd6b17574/test/access/extensions/AccessControlDefaultAdminRules.test.js).

## Toolchain, setup, and validation

Detected language/platform: **JavaScript / TypeScript**. This is based on the inspected tree and manifests, not a verified runtime environment.
Submodule configuration exists: [`.gitmodules`](https://github.com/bchainhub/CoreOpenZeppelin/blob/4e35b0b4078bc0aa532c740e58f30dddd6b17574/.gitmodules); resolve submodules before a build when required.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Overview`, `Installation`, `Usage`, `Learn More`, `Security`, `Contribute`, `License`, `Legal`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/bchainhub/CoreOpenZeppelin/blob/4e35b0b4078bc0aa532c740e58f30dddd6b17574/README.md), [`scripts/solhint-custom/index.js`](https://github.com/bchainhub/CoreOpenZeppelin/blob/4e35b0b4078bc0aa532c740e58f30dddd6b17574/scripts/solhint-custom/index.js), [`.gitmodules`](https://github.com/bchainhub/CoreOpenZeppelin/blob/4e35b0b4078bc0aa532c740e58f30dddd6b17574/.gitmodules), [`.github/workflows/actionlint.yml`](https://github.com/bchainhub/CoreOpenZeppelin/blob/4e35b0b4078bc0aa532c740e58f30dddd6b17574/.github/workflows/actionlint.yml), [`.github/workflows/changeset.yml`](https://github.com/bchainhub/CoreOpenZeppelin/blob/4e35b0b4078bc0aa532c740e58f30dddd6b17574/.github/workflows/changeset.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
