# bchainhub/flutter_wallet_validator

- Repository: https://github.com/bchainhub/flutter_wallet_validator
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `6bb14dbf680e076f125c3171ce3dc546430afdf7`
- Local research checkout: `/tmp/core-blockchain-research/bchainhub/flutter_wallet_validator` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/bchainhub/flutter_wallet_validator/blob/6bb14dbf680e076f125c3171ce3dc546430afdf7/README.md)

## Purpose and selection

Flutter validation library for wallet identifiers.
The [`README.md`](https://github.com/bchainhub/flutter_wallet_validator/blob/6bb14dbf680e076f125c3171ce3dc546430afdf7/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`lib/src/validator.dart`](https://github.com/bchainhub/flutter_wallet_validator/blob/6bb14dbf680e076f125c3171ce3dc546430afdf7/lib/src/validator.dart).
Root build or package files: [`pubspec.yaml`](https://github.com/bchainhub/flutter_wallet_validator/blob/6bb14dbf680e076f125c3171ce3dc546430afdf7/pubspec.yaml).
Source or project directories to inspect first: `lib/`.
Examples or tests visible in the tree: [`example/flutter_wallet_validator_example.dart`](https://github.com/bchainhub/flutter_wallet_validator/blob/6bb14dbf680e076f125c3171ce3dc546430afdf7/example/flutter_wallet_validator_example.dart), [`test/base58_check_test.dart`](https://github.com/bchainhub/flutter_wallet_validator/blob/6bb14dbf680e076f125c3171ce3dc546430afdf7/test/base58_check_test.dart), [`test/flutter_wallet_validator_test.dart`](https://github.com/bchainhub/flutter_wallet_validator/blob/6bb14dbf680e076f125c3171ce3dc546430afdf7/test/flutter_wallet_validator_test.dart).

## Toolchain, setup, and validation

Detected language/platform: **Dart / Flutter**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `pubspec.yaml` declares Dart SDK >=3.5.0 <4.0.0.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Features`, `Installation`, `Usage`, `Basic Example`, `With Options`, `Strict EVM checksum validation`, `Validation coverage`, `Flutter Widget Example`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/bchainhub/flutter_wallet_validator/blob/6bb14dbf680e076f125c3171ce3dc546430afdf7/README.md), [`lib/src/validator.dart`](https://github.com/bchainhub/flutter_wallet_validator/blob/6bb14dbf680e076f125c3171ce3dc546430afdf7/lib/src/validator.dart), [`pubspec.yaml`](https://github.com/bchainhub/flutter_wallet_validator/blob/6bb14dbf680e076f125c3171ce3dc546430afdf7/pubspec.yaml), [`.github/workflows/publish.yml`](https://github.com/bchainhub/flutter_wallet_validator/blob/6bb14dbf680e076f125c3171ce3dc546430afdf7/.github/workflows/publish.yml), [`.github/workflows/test.yml`](https://github.com/bchainhub/flutter_wallet_validator/blob/6bb14dbf680e076f125c3171ce3dc546430afdf7/.github/workflows/test.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
