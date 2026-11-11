# CorePass/core_web3dart

- Repository: https://github.com/CorePass/core_web3dart
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `e472746ff899d92507ecbfbfc357978f7d87296a`
- Local research checkout: `/tmp/core-blockchain-research/CorePass/core_web3dart` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/CorePass/core_web3dart/blob/e472746ff899d92507ecbfbfc357978f7d87296a/README.md)

## Purpose and selection

Dart SDK for Core application and transaction workflows.
The [`README.md`](https://github.com/CorePass/core_web3dart/blob/e472746ff899d92507ecbfbfc357978f7d87296a/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`lib/cip.dart`](https://github.com/CorePass/core_web3dart/blob/e472746ff899d92507ecbfbfc357978f7d87296a/lib/cip.dart).
Root build or package files: [`pubspec.yaml`](https://github.com/CorePass/core_web3dart/blob/e472746ff899d92507ecbfbfc357978f7d87296a/pubspec.yaml).
Source or project directories to inspect first: `lib/`, `tool/`.
Examples or tests visible in the tree: [`example/core_web3dart_example.dart`](https://github.com/CorePass/core_web3dart/blob/e472746ff899d92507ecbfbfc357978f7d87296a/example/core_web3dart_example.dart), [`test/json_rpc_test.dart`](https://github.com/CorePass/core_web3dart/blob/e472746ff899d92507ecbfbfc357978f7d87296a/test/json_rpc_test.dart), [`test/mock_client.dart`](https://github.com/CorePass/core_web3dart/blob/e472746ff899d92507ecbfbfc357978f7d87296a/test/mock_client.dart).

## Toolchain, setup, and validation

Detected language/platform: **Dart / Flutter**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `pubspec.yaml` declares Dart SDK ^3.7.0.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Features`, `Requirements`, `Installation`, `Connect to Core Blockchain`, `ED448 accounts and CORE IDs`, `Sign and send a transaction`, `Encrypted wallets`, `Contract code generation`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`CorePass/flutter_ed448`](flutter_ed448.md), [`CorePass/corebc.js`](corebc.js.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/CorePass/core_web3dart/blob/e472746ff899d92507ecbfbfc357978f7d87296a/README.md), [`lib/cip.dart`](https://github.com/CorePass/core_web3dart/blob/e472746ff899d92507ecbfbfc357978f7d87296a/lib/cip.dart), [`pubspec.yaml`](https://github.com/CorePass/core_web3dart/blob/e472746ff899d92507ecbfbfc357978f7d87296a/pubspec.yaml), [`.github/workflows/publish.yml`](https://github.com/CorePass/core_web3dart/blob/e472746ff899d92507ecbfbfc357978f7d87296a/.github/workflows/publish.yml), [`.github/workflows/test.yml`](https://github.com/CorePass/core_web3dart/blob/e472746ff899d92507ecbfbfc357978f7d87296a/.github/workflows/test.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
