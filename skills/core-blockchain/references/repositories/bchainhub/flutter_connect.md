# bchainhub/flutter_connect

- Repository: https://github.com/bchainhub/flutter_connect
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `9579fe3a8236fadf6570888c2c98ee995426bd36`
- Local research checkout: `/tmp/core-blockchain-research/bchainhub/flutter_connect` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/bchainhub/flutter_connect/blob/9579fe3a8236fadf6570888c2c98ee995426bd36/README.md)

## Purpose and selection

Flutter wallet support for Connect v1 links and approvals.
The [`README.md`](https://github.com/bchainhub/flutter_connect/blob/9579fe3a8236fadf6570888c2c98ee995426bd36/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`lib/src/links.dart`](https://github.com/bchainhub/flutter_connect/blob/9579fe3a8236fadf6570888c2c98ee995426bd36/lib/src/links.dart).
Root build or package files: [`pubspec.yaml`](https://github.com/bchainhub/flutter_connect/blob/9579fe3a8236fadf6570888c2c98ee995426bd36/pubspec.yaml).
Source or project directories to inspect first: `doc/`, `lib/`.
Examples or tests visible in the tree: [`example/test/operations_test.dart`](https://github.com/bchainhub/flutter_connect/blob/9579fe3a8236fadf6570888c2c98ee995426bd36/example/test/operations_test.dart), [`example/test/widget_test.dart`](https://github.com/bchainhub/flutter_connect/blob/9579fe3a8236fadf6570888c2c98ee995426bd36/example/test/widget_test.dart), [`test/bluetooth_test.dart`](https://github.com/bchainhub/flutter_connect/blob/9579fe3a8236fadf6570888c2c98ee995426bd36/test/bluetooth_test.dart), [`test/chains_test.dart`](https://github.com/bchainhub/flutter_connect/blob/9579fe3a8236fadf6570888c2c98ee995426bd36/test/chains_test.dart).

## Toolchain, setup, and validation

Detected language/platform: **Dart / Flutter**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `example/pubspec.yaml` declares Dart SDK >=3.12.0 <4.0.0; `pubspec.yaml` declares Dart SDK >=3.12.0 <4.0.0.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `flutter analyze`
- `flutter test`

## Configuration, interfaces, and relationships

README sections to consult: `Wallet address validation`, `Universal operations and browser provider discovery`, `Native universal wallet API`, `Native WebViews`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`bchainhub/connect.js`](connect.js.md), [`bchainhub/better-connect`](better-connect.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/bchainhub/flutter_connect/blob/9579fe3a8236fadf6570888c2c98ee995426bd36/README.md), [`lib/src/links.dart`](https://github.com/bchainhub/flutter_connect/blob/9579fe3a8236fadf6570888c2c98ee995426bd36/lib/src/links.dart), [`pubspec.yaml`](https://github.com/bchainhub/flutter_connect/blob/9579fe3a8236fadf6570888c2c98ee995426bd36/pubspec.yaml), [`.github/workflows/ci.yml`](https://github.com/bchainhub/flutter_connect/blob/9579fe3a8236fadf6570888c2c98ee995426bd36/.github/workflows/ci.yml), [`.github/workflows/release.yml`](https://github.com/bchainhub/flutter_connect/blob/9579fe3a8236fadf6570888c2c98ee995426bd36/.github/workflows/release.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
