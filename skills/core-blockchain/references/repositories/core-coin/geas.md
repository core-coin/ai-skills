# core-coin/geas

- Repository: https://github.com/core-coin/geas
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `7e40470f64bd2f0ef2c3159b02ac4ecfb4a49646`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/geas` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/core-coin/geas/blob/7e40470f64bd2f0ef2c3159b02ac4ecfb4a49646/README.md)

## Purpose and selection

Macro assembler for EVM bytecode.
The [`README.md`](https://github.com/core-coin/geas/blob/7e40470f64bd2f0ef2c3159b02ac4ecfb4a49646/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`asm/ast.go`](https://github.com/core-coin/geas/blob/7e40470f64bd2f0ef2c3159b02ac4ecfb4a49646/asm/ast.go).
Root build or package files: [`go.mod`](https://github.com/core-coin/geas/blob/7e40470f64bd2f0ef2c3159b02ac4ecfb4a49646/go.mod).
Source or project directories to inspect first: `asm/`, `assets/`, `cmd/`, `internal/`.
Examples or tests visible in the tree: [`asm/compiler_test.go`](https://github.com/core-coin/geas/blob/7e40470f64bd2f0ef2c3159b02ac4ecfb4a49646/asm/compiler_test.go), [`asm/eval_test.go`](https://github.com/core-coin/geas/blob/7e40470f64bd2f0ef2c3159b02ac4ecfb4a49646/asm/eval_test.go), [`asm/lexer_test.go`](https://github.com/core-coin/geas/blob/7e40470f64bd2f0ef2c3159b02ac4ecfb4a49646/asm/lexer_test.go).

## Toolchain, setup, and validation

Detected language/platform: **Go**. This is based on the inspected tree and manifests, not a verified runtime environment.
Version evidence: `go.mod` declares Go 1.21.

No safe root-level build or test command was extracted from the README. Consult the README, scripts, and CI before running commands. No dependencies were installed, build executed, tests run, or runtime verified during this documentation pass.

## Configuration, interfaces, and relationships

README sections to consult: `Installation and Usage`, `Editor Support`, `Use as a Go Library`, `Language`, `Jump`, `Push`, `Expression Macros`, `Builtin Macros`.
No conventional example configuration file was identified in the inspected tree; read the README and target source for required settings and public interfaces.
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/core-coin/geas/blob/7e40470f64bd2f0ef2c3159b02ac4ecfb4a49646/README.md), [`asm/ast.go`](https://github.com/core-coin/geas/blob/7e40470f64bd2f0ef2c3159b02ac4ecfb4a49646/asm/ast.go), [`go.mod`](https://github.com/core-coin/geas/blob/7e40470f64bd2f0ef2c3159b02ac4ecfb4a49646/go.mod), [`.github/workflows/go.yml`](https://github.com/core-coin/geas/blob/7e40470f64bd2f0ef2c3159b02ac4ecfb4a49646/.github/workflows/go.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
