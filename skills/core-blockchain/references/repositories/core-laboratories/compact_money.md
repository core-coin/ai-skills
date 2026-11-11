# core-laboratories/compact_money

- Repository: https://github.com/core-laboratories/compact_money
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `3c9ef0558b893c7980cef81e68fa89b7f8e67998`
- Local research checkout: `/tmp/core-blockchain-research/core-laboratories/compact_money` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-laboratories/compact_money/blob/3c9ef0558b893c7980cef81e68fa89b7f8e67998/README.md)

## Purpose and selection

Compact money data representation; compare its API with compact-money.
The [`README.md`](https://github.com/core-laboratories/compact_money/blob/3c9ef0558b893c7980cef81e68fa89b7f8e67998/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`lib/src/units.dart`](https://github.com/core-laboratories/compact_money/blob/3c9ef0558b893c7980cef81e68fa89b7f8e67998/lib/src/units.dart).
Root build or package files: [`pubspec.yaml`](https://github.com/core-laboratories/compact_money/blob/3c9ef0558b893c7980cef81e68fa89b7f8e67998/pubspec.yaml).
Source or project directories to inspect first: `lib/`, `tool/`.
Examples or tests visible in the tree: [`example/compact_money_example.dart`](https://github.com/core-laboratories/compact_money/blob/3c9ef0558b893c7980cef81e68fa89b7f8e67998/example/compact_money_example.dart), [`test/compact_test.dart`](https://github.com/core-laboratories/compact_money/blob/3c9ef0558b893c7980cef81e68fa89b7f8e67998/test/compact_test.dart), [`test/compact_unit_test.dart`](https://github.com/core-laboratories/compact_money/blob/3c9ef0558b893c7980cef81e68fa89b7f8e67998/test/compact_unit_test.dart), [`test/precision_test.dart`](https://github.com/core-laboratories/compact_money/blob/3c9ef0558b893c7980cef81e68fa89b7f8e67998/test/precision_test.dart).

## Toolchain, setup, and validation

Detected language/platform: **Dart / Flutter**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `pubspec.yaml` declares Dart SDK >=3.10.0 <4.0.0.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `dart analyze --fatal-infos`
- `dart test`

## Configuration, interfaces, and relationships

README sections to consult: `Installation`, `Usage`, `API`, `Units and rounding`, `Decimal places without rounding`, `Currency and presentation`, `Numeric precision`, `Development and releases`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`core-laboratories/compact-money`](compact-money.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-laboratories/compact_money/blob/3c9ef0558b893c7980cef81e68fa89b7f8e67998/README.md), [`lib/src/units.dart`](https://github.com/core-laboratories/compact_money/blob/3c9ef0558b893c7980cef81e68fa89b7f8e67998/lib/src/units.dart), [`pubspec.yaml`](https://github.com/core-laboratories/compact_money/blob/3c9ef0558b893c7980cef81e68fa89b7f8e67998/pubspec.yaml), [`.github/workflows/release.yml`](https://github.com/core-laboratories/compact_money/blob/3c9ef0558b893c7980cef81e68fa89b7f8e67998/.github/workflows/release.yml), [`.github/workflows/test.yml`](https://github.com/core-laboratories/compact_money/blob/3c9ef0558b893c7980cef81e68fa89b7f8e67998/.github/workflows/test.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
