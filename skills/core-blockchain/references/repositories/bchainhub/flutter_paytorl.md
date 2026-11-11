# bchainhub/flutter_paytorl

- Repository: https://github.com/bchainhub/flutter_paytorl
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `c562180960aa1e5c4e627b6518c9649a4c2d6161`
- Local research checkout: `/tmp/core-blockchain-research/bchainhub/flutter_paytorl` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/bchainhub/flutter_paytorl/blob/c562180960aa1e5c4e627b6518c9649a4c2d6161/README.md)

## Purpose and selection

Flutter parser and formatter for Payto Resource Locators.
The [`README.md`](https://github.com/bchainhub/flutter_paytorl/blob/c562180960aa1e5c4e627b6518c9649a4c2d6161/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`lib/src/payqr.dart`](https://github.com/bchainhub/flutter_paytorl/blob/c562180960aa1e5c4e627b6518c9649a4c2d6161/lib/src/payqr.dart).
Root build or package files: [`pubspec.yaml`](https://github.com/bchainhub/flutter_paytorl/blob/c562180960aa1e5c4e627b6518c9649a4c2d6161/pubspec.yaml).
Source or project directories to inspect first: `doc/`, `lib/`.
Examples or tests visible in the tree: [`test/btc_precision_test.dart`](https://github.com/bchainhub/flutter_paytorl/blob/c562180960aa1e5c4e627b6518c9649a4c2d6161/test/btc_precision_test.dart), [`test/emv_mpm_test.dart`](https://github.com/bchainhub/flutter_paytorl/blob/c562180960aa1e5c4e627b6518c9649a4c2d6161/test/emv_mpm_test.dart), [`test/formats_test.dart`](https://github.com/bchainhub/flutter_paytorl/blob/c562180960aa1e5c4e627b6518c9649a4c2d6161/test/formats_test.dart), [`test/payqr_contract.dart`](https://github.com/bchainhub/flutter_paytorl/blob/c562180960aa1e5c4e627b6518c9649a4c2d6161/test/payqr_contract.dart).

## Toolchain, setup, and validation

Detected language/platform: **Dart / Flutter**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `pubspec.yaml` declares Dart SDK >=3.8.0 <4.0.0.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Features`, `Installation`, `Usage`, `API Reference`, `Constructor`, `Properties`, `Methods`, `BIC Payments`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`bchainhub/payto-rl`](payto-rl.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/bchainhub/flutter_paytorl/blob/c562180960aa1e5c4e627b6518c9649a4c2d6161/README.md), [`lib/src/payqr.dart`](https://github.com/bchainhub/flutter_paytorl/blob/c562180960aa1e5c4e627b6518c9649a4c2d6161/lib/src/payqr.dart), [`pubspec.yaml`](https://github.com/bchainhub/flutter_paytorl/blob/c562180960aa1e5c4e627b6518c9649a4c2d6161/pubspec.yaml), [`.github/workflows/publish.yml`](https://github.com/bchainhub/flutter_paytorl/blob/c562180960aa1e5c4e627b6518c9649a4c2d6161/.github/workflows/publish.yml), [`.github/workflows/test.yml`](https://github.com/bchainhub/flutter_paytorl/blob/c562180960aa1e5c4e627b6518c9649a4c2d6161/.github/workflows/test.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
