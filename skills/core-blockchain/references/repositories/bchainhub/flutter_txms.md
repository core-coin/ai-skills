# bchainhub/flutter_txms

- Repository: https://github.com/bchainhub/flutter_txms
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `3a593f0c3021007ee21b74932d2d640bc6fff2a3`
- Local research checkout: `/tmp/core-blockchain-research/bchainhub/flutter_txms` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/bchainhub/flutter_txms/blob/3a593f0c3021007ee21b74932d2d640bc6fff2a3/README.md)

## Purpose and selection

Flutter codec for hex-encoded TxMS messages.
The [`README.md`](https://github.com/bchainhub/flutter_txms/blob/3a593f0c3021007ee21b74932d2d640bc6fff2a3/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`lib/src/routing.dart`](https://github.com/bchainhub/flutter_txms/blob/3a593f0c3021007ee21b74932d2d640bc6fff2a3/lib/src/routing.dart).
Root build or package files: [`pubspec.yaml`](https://github.com/bchainhub/flutter_txms/blob/3a593f0c3021007ee21b74932d2d640bc6fff2a3/pubspec.yaml).
Source or project directories to inspect first: `lib/`.
Examples or tests visible in the tree: [`test/txms_test.dart`](https://github.com/bchainhub/flutter_txms/blob/3a593f0c3021007ee21b74932d2d640bc6fff2a3/test/txms_test.dart).

## Toolchain, setup, and validation

Detected language/platform: **Dart / Flutter**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `pubspec.yaml` declares Dart SDK >=3.5.0 <4.0.0.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Features`, `Getting Started`, `Usage`, `Parse transaction receipt SMS`, `Basic Example`, `SMS Generation and Opening`, `File Operations`, `Message Counting`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`bchainhub/txms.js`](txms.js.md), [`DataLayerHost/libtxms`](../DataLayerHost/libtxms.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/bchainhub/flutter_txms/blob/3a593f0c3021007ee21b74932d2d640bc6fff2a3/README.md), [`lib/src/routing.dart`](https://github.com/bchainhub/flutter_txms/blob/3a593f0c3021007ee21b74932d2d640bc6fff2a3/lib/src/routing.dart), [`pubspec.yaml`](https://github.com/bchainhub/flutter_txms/blob/3a593f0c3021007ee21b74932d2d640bc6fff2a3/pubspec.yaml), [`.github/workflows/publish.yml`](https://github.com/bchainhub/flutter_txms/blob/3a593f0c3021007ee21b74932d2d640bc6fff2a3/.github/workflows/publish.yml), [`.github/workflows/test.yml`](https://github.com/bchainhub/flutter_txms/blob/3a593f0c3021007ee21b74932d2d640bc6fff2a3/.github/workflows/test.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
