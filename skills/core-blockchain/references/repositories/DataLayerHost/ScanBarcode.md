# DataLayerHost/ScanBarcode

- Repository: https://github.com/DataLayerHost/ScanBarcode
- Research status: **README, manifests, CI, privacy policy, and selected source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `c7f31d5069f1104eee5926dfef5cd6f381dea64c`
- Local research checkout: `/tmp/core-blockchain-research/DataLayerHost/ScanBarcode` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/DataLayerHost/ScanBarcode/blob/c7f31d5069f1104eee5926dfef5cd6f381dea64c/README.md)

## Purpose and when to use it

ScanBarcode is a native desktop scanner for macOS, Windows, and Linux. It reads camera frames or chosen images, shows decoded results, and offers copy, save, and user-triggered actions. Use it when the receiving side of an offline QR transfer needs to reconstruct BarcodeTx data, or when a desktop app must recognize and hand off ordinary barcode content and deeplinks. It is an application, not the Dart encoding library or a transaction signer.

## Air-gapped BarcodeTx transfer

[`flutter_barcodetx`](flutter_barcodetx.md) can encode **already-signed** transaction bytes as a continuous sequence of QR frames on another device. ScanBarcode accepts raw frame bytes from its live camera or an animated GIF, tracks reconstruction progress, applies fountain decoding, checks per-frame CRC-32 and whole-batch SHA-256 integrity, and parses a batch of up to 256 transactions. It shows each result as labeled transaction hex and counts XCB entries. The inspected [decoder and batch parser](https://github.com/DataLayerHost/ScanBarcode/blob/c7f31d5069f1104eee5926dfef5cd6f381dea64c/src/main.rs#L135-L415) do not sign, validate chain semantics or signatures, or broadcast transactions. A trusted chain-specific application must review and submit the resulting signed bytes separately.

The transfer ID is derived from the first six digest bytes, so it groups frames but is not sender authentication. The parser rejects inconsistent metadata, duplicate symbols, malformed limits, bad checksums, incomplete reconstruction, and trailing batch data. For interoperability changes, compare this parser with the [BarcodeTx protocol](https://github.com/DataLayerHost/flutter_barcodetx/blob/a69741ce321eb5ae428a956a96370631af526d16/PROTOCOL.md) at the encoder's inspected revision, then check current source in both repositories.

Offline scanning is possible, but the application is not inherently isolated: direct-download builds can check GitHub for updates, and a chosen deeplink action can hand data to another application. For an air-gapped workflow, account for those behaviors and review the [privacy policy](https://github.com/DataLayerHost/ScanBarcode/blob/c7f31d5069f1104eee5926dfef5cd6f381dea64c/docs/privacy-policy.md). Scan history remains in memory unless the user copies or saves it; the clipboard or saved file can outlive the session.

## Deeplinks and other scan actions

The [README scan-action list](https://github.com/DataLayerHost/ScanBarcode/blob/c7f31d5069f1104eee5926dfef5cd6f381dea64c/README.md) and [`classify_scan`](https://github.com/DataLayerHost/ScanBarcode/blob/c7f31d5069f1104eee5926dfef5cd6f381dea64c/src/main.rs#L2748-L2850) cover `corepass:`, `tone://...`, `payto:`, `UR:`, URLs, `mailto:`, `tel:`, `sms:`, and registered custom URI schemes. They also recognize Wi-Fi, contact, calendar, payment QR, eSIM, Matter, HomeKit, OpenPGP, GS1, and other barcode formats. Recognizing a payload creates an action button; opening or executing it requires a user action. Generic URI schemes are not limited to a built-in allowlist, and the OS handler may transfer data or reach the network. Check the decoded content before choosing an action.

## Architecture, toolchain, and checks

- [`src/main.rs`](https://github.com/DataLayerHost/ScanBarcode/blob/c7f31d5069f1104eee5926dfef5cd6f381dea64c/src/main.rs) contains the scanner UI, barcode classification, BarcodeTx decoder, and action handling. [`src/update.rs`](https://github.com/DataLayerHost/ScanBarcode/blob/c7f31d5069f1104eee5926dfef5cd6f381dea64c/src/update.rs) handles updates.
- [`Cargo.toml`](https://github.com/DataLayerHost/ScanBarcode/blob/c7f31d5069f1104eee5926dfef5cd6f381dea64c/Cargo.toml) declares Rust edition 2021, package version 0.1.3, a `store` feature, and a vendored `winit` patch. [`Cargo.lock`](https://github.com/DataLayerHost/ScanBarcode/blob/c7f31d5069f1104eee5926dfef5cd6f381dea64c/Cargo.lock) pins dependencies. CI uses stable Rust; no minimum supported Rust version is declared.
- The [test workflow](https://github.com/DataLayerHost/ScanBarcode/blob/c7f31d5069f1104eee5926dfef5cd6f381dea64c/.github/workflows/test.yml) checks Ubuntu x86_64 and ARM, macOS, and Windows. Linux builds install camera, audio, and GUI development libraries. The source tree includes BarcodeTx frame fixtures under `tests/fixtures/`.
- Working directory: repository root. The README documents `cargo run` and `cargo build --release`; CI runs `cargo fmt --all -- --check`, `cargo test --all-targets`, and `cargo build --release`. These commands were **documented, not executed here**. Dependencies were not installed; build, tests, and runtime were not verified in this workspace.

## Relationships and pitfalls

[`flutter_barcodetx`](flutter_barcodetx.md) supplies the related animated QR encoder and decoder protocol; ScanBarcode is a desktop receiving implementation. [`flutter_modem`](flutter_modem.md) is a different acoustic transport, and [`core_web3dart`](../CorePass/core_web3dart.md) covers Dart Core transaction workflows. These are task relationships, not evidence that ScanBarcode directly depends on those packages. Keep transaction authenticity and broadcast checks in the signing or submission application, and preserve user consent before opening deeplinks.
