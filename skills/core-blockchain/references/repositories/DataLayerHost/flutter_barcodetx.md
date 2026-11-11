# DataLayerHost/flutter_barcodetx

- Repository: https://github.com/DataLayerHost/flutter_barcodetx
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `a69741ce321eb5ae428a956a96370631af526d16`
- Local research checkout: `/tmp/core-blockchain-research/DataLayerHost/flutter_barcodetx` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/DataLayerHost/flutter_barcodetx/blob/a69741ce321eb5ae428a956a96370631af526d16/README.md)

## Purpose and selection

Flutter QR transport for already-signed transactions.
The [`README.md`](https://github.com/DataLayerHost/flutter_barcodetx/blob/a69741ce321eb5ae428a956a96370631af526d16/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`tool/benchmark.dart`](https://github.com/DataLayerHost/flutter_barcodetx/blob/a69741ce321eb5ae428a956a96370631af526d16/tool/benchmark.dart).
Root build or package files: [`pubspec.yaml`](https://github.com/DataLayerHost/flutter_barcodetx/blob/a69741ce321eb5ae428a956a96370631af526d16/pubspec.yaml).
Source or project directories to inspect first: `lib/`, `tool/`.
Examples or tests visible in the tree: [`test/flutter_barcodetx_test.dart`](https://github.com/DataLayerHost/flutter_barcodetx/blob/a69741ce321eb5ae428a956a96370631af526d16/test/flutter_barcodetx_test.dart).

## Toolchain, setup, and validation

Detected language/platform: **Dart / Flutter**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `example/pubspec.yaml` declares Dart SDK >=3.7.0 <4.0.0; `pubspec.yaml` declares Dart SDK >=3.5.0 <4.0.0.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Pipeline`, `Installation`, `Encode and display`, `Decode camera output`, `Recovery and integrity`, `Documentation`, `License`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
The desktop [`ScanBarcode`](ScanBarcode.md) app implements a receiving path for BarcodeTx frames and displays reconstructed transaction hex. This is a protocol relationship, not evidence of a direct package dependency. Compare both implementations at current revisions for interoperability. Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/DataLayerHost/flutter_barcodetx/blob/a69741ce321eb5ae428a956a96370631af526d16/README.md), [`tool/benchmark.dart`](https://github.com/DataLayerHost/flutter_barcodetx/blob/a69741ce321eb5ae428a956a96370631af526d16/tool/benchmark.dart), [`pubspec.yaml`](https://github.com/DataLayerHost/flutter_barcodetx/blob/a69741ce321eb5ae428a956a96370631af526d16/pubspec.yaml), [`.github/workflows/publish.yml`](https://github.com/DataLayerHost/flutter_barcodetx/blob/a69741ce321eb5ae428a956a96370631af526d16/.github/workflows/publish.yml), [`.github/workflows/test.yml`](https://github.com/DataLayerHost/flutter_barcodetx/blob/a69741ce321eb5ae428a956a96370631af526d16/.github/workflows/test.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
