# core-coin/Xcb.Net

- Repository: https://github.com/core-coin/Xcb.Net
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `d9a36122c76ea55ba66f7cefcac231a2878e2ab1`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/Xcb.Net` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/Xcb.Net/blob/d9a36122c76ea55ba66f7cefcac231a2878e2ab1/README.md)

## Purpose and selection

.NET client library for keys and signed Core transactions.
The [`README.md`](https://github.com/core-coin/Xcb.Net/blob/d9a36122c76ea55ba66f7cefcac231a2878e2ab1/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`Xcb.Net/RLP/RLP.cs`](https://github.com/core-coin/Xcb.Net/blob/d9a36122c76ea55ba66f7cefcac231a2878e2ab1/Xcb.Net/RLP/RLP.cs).
Root build or package files: [`Xcb.Net.sln`](https://github.com/core-coin/Xcb.Net/blob/d9a36122c76ea55ba66f7cefcac231a2878e2ab1/Xcb.Net.sln).
Source or project directories to inspect first: `Xcb.Net.Test/`, `Xcb.Net/`.

## Toolchain, setup, and validation

Detected language/platform: **C# / .NET**. This is based on the inspected tree and manifests, not a verified runtime environment.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Usage of keys`, `Usage of transactions`, `Usage of Hierarchical Deterministic Wallet (HD-Wallet)`, `License`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/Xcb.Net/blob/d9a36122c76ea55ba66f7cefcac231a2878e2ab1/README.md), [`Xcb.Net/RLP/RLP.cs`](https://github.com/core-coin/Xcb.Net/blob/d9a36122c76ea55ba66f7cefcac231a2878e2ab1/Xcb.Net/RLP/RLP.cs), [`.github/workflows/package.yml`](https://github.com/core-coin/Xcb.Net/blob/d9a36122c76ea55ba66f7cefcac231a2878e2ab1/.github/workflows/package.yml), [`.github/workflows/test.yml`](https://github.com/core-coin/Xcb.Net/blob/d9a36122c76ea55ba66f7cefcac231a2878e2ab1/.github/workflows/test.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
