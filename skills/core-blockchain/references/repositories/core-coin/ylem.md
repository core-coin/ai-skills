# core-coin/ylem

- Repository: https://github.com/core-coin/ylem
- Research status: **source inspected**
- Inspection date: 2026-11-15 (expanded from the 2026-11-11 survey)
- Inspected branch: `fix/version`
- Inspected commit: `eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7`
- Local research checkout: developer checkout, read only; not required to use this skill
- README: [`README.md`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/README.md)

## Purpose and selection

Ylem is the contract language and compiler used for Core CVM contracts. Use this card for compiler selection, ABI and storage assumptions, code generation, and compiler development. For project builds, contract tests, simulation, and deployment, follow the [Foxar workflow](../bchainhub/foxar.md#contract-project-workflow). For reusable contract modules, read [CoreOZ](../bchainhub/CoreOpenZeppelin.md).

## Contract compilation

Use the project's selected Ylem version and import constraints. Ylem retains `pragma solidity`; a contract targeting the 1.1.2 family can declare:

```solidity
pragma solidity ^1.1.2;
```

This is a Ylem version constraint, not a request for an Ethereum Solidity compiler. Existing dependencies may pin an exact version, so do not rewrite their pragmas merely to match this example. The inspected README contains an inherited 0.x pragma example; select the version from the actual project and compiler, not that example.

The following commands assume the selected Ylem executable is available as `ylem` and run from the contract project root:

```bash
ylem --version
ylem --evm-version istanbul --abi --bin src/Example.sol
ylem --evm-version istanbul --hashes --storage-layout src/Example.sol
ylem --standard-json < compiler-input.json > compiler-output.json
```

Replace the input path and supply the project's import remappings and base path. `--abi` emits the ABI, `--bin` emits creation bytecode, `--bin-runtime` emits runtime bytecode, `--hashes` reports function selectors, and `--storage-layout` reports slots, offsets, and types. Standard JSON takes compiler settings from its input; check its returned `errors` diagnostics, not just the process exit status.

For Spark projects, use `spark build --use 1.1.2` when that is the required version; retain the project's compiler constraints and configuration. See [Foxar compiler selection](../bchainhub/foxar.md#toolchain-setup-and-validation) and [YVM](yvm-rs.md) for tool-specific version management.

The inspected source and installed 1.1.2 binary default to `istanbul`; the CLI also accepts `berlin`. An accepted compiler target does not establish network activation. Choose targets against the [CVM execution rules](../../core-protocol.md#cvm-execution), rather than inferring Core compatibility from a target's name.

Sources: [`solc/CommandLineInterface.cpp`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/solc/CommandLineInterface.cpp), [`libsolidity/interface/StandardCompiler.cpp`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/libsolidity/interface/StandardCompiler.cpp), [`liblangutil/EVMVersion.h`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/liblangutil/EVMVersion.h), and [`README.md`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/README.md). CLI options were also checked against the installed binary recorded below.

## Language, ABI, and storage

| Surface | Core behavior and development consequence |
| --- | --- |
| `address` and contract types | Full 22-byte values. Address-to-integer conversions use `uint176`; treating an address as `uint160` loses its prefix and checksum. |
| Ordinary ABI encoding | A static address occupies a 32-byte word containing the full 22-byte address, left-padded with zeros. |
| Packed encoding and storage | A scalar address occupies 22 bytes. Check assembly masks, packed messages, field offsets, and storage packing instead of carrying over 20-byte assumptions. |
| `keccak256` | The language name remains; Core uses NIST SHA3-256. Use the [hashing reference](../../core-protocol.md#hashing) for selectors, event IDs, and hash-derived values. |
| `block.chainid` | The language member remains `chainid` and compiles to opcode `0x46`, which Core executes as `NETWORKID`. Do not rename the member to `block.networkId`. |
| `ecrecover` | The builtin is `ecrecover(bytes32 hash, bytes memory signature) returns (address)`. Read the [signature format](../../core-protocol.md#signatures-and-address-derivation) and [failure behavior](../../core-protocol.md#ecrecover). |

Address representation does not mean every value is an ordinary ICAN account: preserve the [precompile address rules](../../core-protocol.md#precompile-addresses). For contract upgrades, compare Ylem-produced storage layouts of the exact old and new implementations.

Sources: `AddressType` and `ContractType` in [`libsolidity/ast/Types.h`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/libsolidity/ast/Types.h), conversions and `block` members in [`libsolidity/ast/Types.cpp`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/libsolidity/ast/Types.cpp), [`libsolidity/codegen/ABIFunctions.cpp`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/libsolidity/codegen/ABIFunctions.cpp), builtins in [`libsolidity/analysis/GlobalContext.cpp`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/libsolidity/analysis/GlobalContext.cpp), [`libsolidity/codegen/ExpressionCompiler.cpp`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/libsolidity/codegen/ExpressionCompiler.cpp), and [`libsolutil/Keccak256.cpp`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/libsolutil/Keccak256.cpp).

## Compiler source map

| Task | Entry points |
| --- | --- |
| CLI arguments and compilation flow | [`solc/main.cpp`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/solc/main.cpp), [`solc/CommandLineInterface.cpp`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/solc/CommandLineInterface.cpp) |
| Standard JSON and compiler orchestration | [`libsolidity/interface/StandardCompiler.cpp`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/libsolidity/interface/StandardCompiler.cpp), [`libsolidity/interface/CompilerStack.cpp`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/libsolidity/interface/CompilerStack.cpp) |
| Types and builtin declarations | `libsolidity/ast/`, `libsolidity/analysis/`; start with `Types.h`, `Types.cpp`, and `GlobalContext.cpp` linked above |
| ABI, bytecode, and IR generation | `libsolidity/codegen/`, [`libsolidity/codegen/ir/IRGenerator.cpp`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/libsolidity/codegen/ir/IRGenerator.cpp), `libyul/`, `libevmasm/` |
| Diagnostics and execution expectations | `test/libsolidity/syntaxTests/`, `test/libsolidity/semanticTests/`, [`test/libsolidity/SemanticTest.cpp`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/test/libsolidity/SemanticTest.cpp); use `test/libyul/` for Yul changes |

## Compiler build and validation

For changes to Ylem itself, use the CMake build. The inspected source requires CMake 3.13 or newer, a supported C/C++ toolchain, and its declared dependencies, including Boost 1.65 or newer. Check [`cmake/EthDependencies.cmake`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/cmake/EthDependencies.cmake), [`cmake/EthCompilerSettings.cmake`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/cmake/EthCompilerSettings.cmake), and [`.github/workflows/build.yml`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/.github/workflows/build.yml) for platform setup and optional SMT support.

From the Ylem repository root, after satisfying those prerequisites:

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DTESTS=ON
cmake --build build --target ylem
cmake --build build --target soltest
```

The compiler target is `ylem`, with the Unix executable at `build/solc/ylem`; the compiler test executable is `build/test/soltest`. [`scripts/tests.sh`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/scripts/tests.sh) shows the test runner's `--testpath`, target, and optimizer options. Select tests for the changed compiler component and check execution-test prerequisites before running the wider matrix.

Sources: [`CMakeLists.txt`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/CMakeLists.txt), [`solc/CMakeLists.txt`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/solc/CMakeLists.txt), [`test/CMakeLists.txt`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/test/CMakeLists.txt), and [`scripts/tests.sh`](https://github.com/core-coin/ylem/blob/eaf05fdd802ffe3a3e56b140f2174b7e0b4500f7/scripts/tests.sh). Release CI supplies a version from its tag; the source snapshot and an installed release binary must be identified separately.

## Inspection scope

Source was read at the commit above, including the committed CMake file rather than local uncommitted changes. No compiler build or compiler/contract test was run, and no dependencies were installed.

Executed CLI checks from the local Ylem checkout, using an already installed YVM-managed executable: `--version` exited 0 and reported `1.1.2+commit.cb4b093a.Linux.g++`; `--help` printed the documented options and exited 1. This verifies the binary's reported interface, not compilation or CVM execution. The compilation and build commands above are documented guidance, not executed checks.

Related distribution references: [Ylem binaries](ylem-bins.md) and [YVM](yvm-rs.md).
