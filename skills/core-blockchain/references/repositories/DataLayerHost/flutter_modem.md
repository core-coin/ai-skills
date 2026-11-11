# DataLayerHost/flutter_modem

- Repository: https://github.com/DataLayerHost/flutter_modem
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `b0b7781dc554d6f91debb83128f818b726216eb2`
- Local research checkout: `/tmp/core-blockchain-research/DataLayerHost/flutter_modem` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/DataLayerHost/flutter_modem/blob/b0b7781dc554d6f91debb83128f818b726216eb2/README.md)

## Purpose and selection

Dart acoustic modem for transferring bytes.
The [`README.md`](https://github.com/DataLayerHost/flutter_modem/blob/b0b7781dc554d6f91debb83128f818b726216eb2/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`lib/src/modem.dart`](https://github.com/DataLayerHost/flutter_modem/blob/b0b7781dc554d6f91debb83128f818b726216eb2/lib/src/modem.dart).
Root build or package files: [`pubspec.yaml`](https://github.com/DataLayerHost/flutter_modem/blob/b0b7781dc554d6f91debb83128f818b726216eb2/pubspec.yaml).
Source or project directories to inspect first: `lib/`.
Examples or tests visible in the tree: [`example/decode_hello.dart`](https://github.com/DataLayerHost/flutter_modem/blob/b0b7781dc554d6f91debb83128f818b726216eb2/example/decode_hello.dart), [`example/encode_hello.dart`](https://github.com/DataLayerHost/flutter_modem/blob/b0b7781dc554d6f91debb83128f818b726216eb2/example/encode_hello.dart), [`example/encode_random_bytes.dart`](https://github.com/DataLayerHost/flutter_modem/blob/b0b7781dc554d6f91debb83128f818b726216eb2/example/encode_random_bytes.dart), [`example/fast_loopback.dart`](https://github.com/DataLayerHost/flutter_modem/blob/b0b7781dc554d6f91debb83128f818b726216eb2/example/fast_loopback.dart).

## Toolchain, setup, and validation

Detected language/platform: **Dart / Flutter**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `pubspec.yaml` declares Dart SDK ^3.3.0.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `dart analyze`
- `dart test`

## Configuration, interfaces, and relationships

README sections to consult: `Quick start`, `Application protocol`, `How BFSK works`, `Near-ultrasonic alternative`, `Robust low-speed mode`, `Orthogonal high-speed alternative`, `Goertzel decoding and synchronization`, `Wire and packet format`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/DataLayerHost/flutter_modem/blob/b0b7781dc554d6f91debb83128f818b726216eb2/README.md), [`lib/src/modem.dart`](https://github.com/DataLayerHost/flutter_modem/blob/b0b7781dc554d6f91debb83128f818b726216eb2/lib/src/modem.dart), [`pubspec.yaml`](https://github.com/DataLayerHost/flutter_modem/blob/b0b7781dc554d6f91debb83128f818b726216eb2/pubspec.yaml), [`.github/workflows/ci.yml`](https://github.com/DataLayerHost/flutter_modem/blob/b0b7781dc554d6f91debb83128f818b726216eb2/.github/workflows/ci.yml), [`.github/workflows/publish.yml`](https://github.com/DataLayerHost/flutter_modem/blob/b0b7781dc554d6f91debb83128f818b726216eb2/.github/workflows/publish.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
