# core-coin/randomy-rs

- Repository: https://github.com/core-coin/randomy-rs
- Research status: **source inspected via GitHub connector**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `ea1e46ea5885b4a34695da0afd1cccd7db783c2a`
- Local research checkout: none; connected GitHub source used
- README: [`README.md`](https://github.com/core-coin/randomy-rs/blob/ea1e46ea5885b4a34695da0afd1cccd7db783c2a/README.md)

## Purpose and selection

Rust binding to proof-of-work code; compare its manifest and README before assuming algorithm compatibility.
The [`README.md`](https://github.com/core-coin/randomy-rs/blob/ea1e46ea5885b4a34695da0afd1cccd7db783c2a/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src/lib.rs`](https://github.com/core-coin/randomy-rs/blob/ea1e46ea5885b4a34695da0afd1cccd7db783c2a/src/lib.rs).
Root build or package files: [`.gitmodules`](https://github.com/core-coin/randomy-rs/blob/ea1e46ea5885b4a34695da0afd1cccd7db783c2a/.gitmodules), [`Cargo.toml`](https://github.com/core-coin/randomy-rs/blob/ea1e46ea5885b4a34695da0afd1cccd7db783c2a/Cargo.toml).
Source or project directories to inspect first: `src/`.

## Toolchain, setup, and validation

Detected language/platform: **Rust**. This is based on the inspected tree and manifests, not a verified runtime environment.
The README calls this project RandomX-rs despite the repository name. Verify the actual algorithm and compatibility before using it for RandomY work.
Submodule configuration exists: [`.gitmodules`](https://github.com/core-coin/randomy-rs/blob/ea1e46ea5885b4a34695da0afd1cccd7db783c2a/.gitmodules); resolve submodules before a build when required.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Build Dependencies`, `Mac`, `Linux`, `Windows`, `MacOs`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Related references by task (not verified direct dependencies): [`core-coin/RandomY`](RandomY.md), [`core-coin/go-randomy`](go-randomy.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/randomy-rs/blob/ea1e46ea5885b4a34695da0afd1cccd7db783c2a/README.md), [`src/lib.rs`](https://github.com/core-coin/randomy-rs/blob/ea1e46ea5885b4a34695da0afd1cccd7db783c2a/src/lib.rs), [`.gitmodules`](https://github.com/core-coin/randomy-rs/blob/ea1e46ea5885b4a34695da0afd1cccd7db783c2a/.gitmodules), [`Cargo.toml`](https://github.com/core-coin/randomy-rs/blob/ea1e46ea5885b4a34695da0afd1cccd7db783c2a/Cargo.toml), [`.github/workflows/audit.yml`](https://github.com/core-coin/randomy-rs/blob/ea1e46ea5885b4a34695da0afd1cccd7db783c2a/.github/workflows/audit.yml), [`.github/workflows/ci.yml`](https://github.com/core-coin/randomy-rs/blob/ea1e46ea5885b4a34695da0afd1cccd7db783c2a/.github/workflows/ci.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
