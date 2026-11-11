# CorePass/flutter_ed448

- Repository: https://github.com/CorePass/flutter_ed448
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `99861de215d513afb2a69da20b81d72539d2694a`
- Local research checkout: `/tmp/core-blockchain-research/CorePass/flutter_ed448` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/CorePass/flutter_ed448/blob/99861de215d513afb2a69da20b81d72539d2694a/README.md)

## Purpose and selection

Flutter and Dart Ed448 cryptography package.
The [`README.md`](https://github.com/CorePass/flutter_ed448/blob/99861de215d513afb2a69da20b81d72539d2694a/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`js/main.dart`](https://github.com/CorePass/flutter_ed448/blob/99861de215d513afb2a69da20b81d72539d2694a/js/main.dart).
Root build or package files: [`pubspec.yaml`](https://github.com/CorePass/flutter_ed448/blob/99861de215d513afb2a69da20b81d72539d2694a/pubspec.yaml).
Source or project directories to inspect first: `bin/`, `js/`, `lib/`, `tool/`.
Examples or tests visible in the tree: [`example/flutter_ed448_example.dart`](https://github.com/CorePass/flutter_ed448/blob/99861de215d513afb2a69da20b81d72539d2694a/example/flutter_ed448_example.dart), [`test/all.dart`](https://github.com/CorePass/flutter_ed448/blob/99861de215d513afb2a69da20b81d72539d2694a/test/all.dart), [`test/flutter_ed448_test.dart`](https://github.com/CorePass/flutter_ed448/blob/99861de215d513afb2a69da20b81d72539d2694a/test/flutter_ed448_test.dart), [`test/test_blake3.dart`](https://github.com/CorePass/flutter_ed448/blob/99861de215d513afb2a69da20b81d72539d2694a/test/test_blake3.dart).

## Toolchain, setup, and validation

Detected language/platform: **Dart / Flutter**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `pubspec.yaml` declares Dart SDK >=3.0.0 <4.0.0.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `dart test`
- `dart analyze`

## Configuration, interfaces, and relationships

README sections to consult: `Installation`, `Quick Start`, `Running Tests`, `Release Process`, `Licensing`, `Contributing`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/CorePass/flutter_ed448/blob/99861de215d513afb2a69da20b81d72539d2694a/README.md), [`js/main.dart`](https://github.com/CorePass/flutter_ed448/blob/99861de215d513afb2a69da20b81d72539d2694a/js/main.dart), [`pubspec.yaml`](https://github.com/CorePass/flutter_ed448/blob/99861de215d513afb2a69da20b81d72539d2694a/pubspec.yaml), [`.github/workflows/ci.yml`](https://github.com/CorePass/flutter_ed448/blob/99861de215d513afb2a69da20b81d72539d2694a/.github/workflows/ci.yml), [`.github/workflows/publish.yml`](https://github.com/CorePass/flutter_ed448/blob/99861de215d513afb2a69da20b81d72539d2694a/.github/workflows/publish.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
