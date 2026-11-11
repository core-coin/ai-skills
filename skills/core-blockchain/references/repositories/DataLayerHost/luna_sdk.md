# DataLayerHost/luna_sdk

- Repository: https://github.com/DataLayerHost/luna_sdk
- Research status: **source inspected via GitHub connector**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `33bf2250d839f249702b06a7557a23e0b953994c`
- Local research checkout: none; connected GitHub source used
- README: [`README.md`](https://github.com/DataLayerHost/luna_sdk/blob/33bf2250d839f249702b06a7557a23e0b953994c/README.md)

## Purpose and selection

Flutter and Dart SDK for the Luna communication layer.
The [`README.md`](https://github.com/DataLayerHost/luna_sdk/blob/33bf2250d839f249702b06a7557a23e0b953994c/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`lib/luna_sdk.dart`](https://github.com/DataLayerHost/luna_sdk/blob/33bf2250d839f249702b06a7557a23e0b953994c/lib/luna_sdk.dart).
Root build or package files: [`pubspec.yaml`](https://github.com/DataLayerHost/luna_sdk/blob/33bf2250d839f249702b06a7557a23e0b953994c/pubspec.yaml).
Source or project directories to inspect first: `doc/`, `lib/`, `test-vectors/`, `tool/`.
Examples or tests visible in the tree: [`example/test/widget_test.dart`](https://github.com/DataLayerHost/luna_sdk/blob/33bf2250d839f249702b06a7557a23e0b953994c/example/test/widget_test.dart), [`test/ble_test.dart`](https://github.com/DataLayerHost/luna_sdk/blob/33bf2250d839f249702b06a7557a23e0b953994c/test/ble_test.dart), [`test/edge_cases_test.dart`](https://github.com/DataLayerHost/luna_sdk/blob/33bf2250d839f249702b06a7557a23e0b953994c/test/edge_cases_test.dart), [`test/peer_test.dart`](https://github.com/DataLayerHost/luna_sdk/blob/33bf2250d839f249702b06a7557a23e0b953994c/test/peer_test.dart).

## Toolchain, setup, and validation

Detected language/platform: **Dart / Flutter**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `example/pubspec.yaml` declares Dart SDK >=3.9.2 <4.0.0; `pubspec.yaml` declares Dart SDK >=3.9.2 <4.0.0.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `flutter analyze`
- `flutter test`

## Configuration, interfaces, and relationships

README sections to consult: `Quick start`, `Functionality and boundaries`, `Development`, `License`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`DataLayerHost/luna-sdk`](luna-sdk.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/DataLayerHost/luna_sdk/blob/33bf2250d839f249702b06a7557a23e0b953994c/README.md), [`lib/luna_sdk.dart`](https://github.com/DataLayerHost/luna_sdk/blob/33bf2250d839f249702b06a7557a23e0b953994c/lib/luna_sdk.dart), [`pubspec.yaml`](https://github.com/DataLayerHost/luna_sdk/blob/33bf2250d839f249702b06a7557a23e0b953994c/pubspec.yaml), [`.github/workflows/release.yml`](https://github.com/DataLayerHost/luna_sdk/blob/33bf2250d839f249702b06a7557a23e0b953994c/.github/workflows/release.yml), [`.github/workflows/tests.yml`](https://github.com/DataLayerHost/luna_sdk/blob/33bf2250d839f249702b06a7557a23e0b953994c/.github/workflows/tests.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
