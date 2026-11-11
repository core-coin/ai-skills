# core-laboratories/ylem-splitting

- Repository: https://github.com/core-laboratories/ylem-splitting
- Research status: **source inspected; no README found**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `6f810556e8e04b14fff3511c381f9b053664479a`
- Local research checkout: `/tmp/core-blockchain-research/core-laboratories/ylem-splitting` (research only)
- README: none in the inspected tree

## Purpose and when to use it

The source contains a `DistributeWithFee` contract for splitting native currency or CRC20 token transfers between a recipient and a treasury. Use it when working on that fee-splitting contract or its Foxar tests. There is no README to establish intended deployment status or broader product scope.

## Architecture and interfaces

[`src/DistributeWithFee.sol`](https://github.com/core-laboratories/ylem-splitting/blob/6f810556e8e04b14fff3511c381f9b053664479a/src/DistributeWithFee.sol) defines `transfer`, owner-only `setTreasury` and `setFee`, and owner-only `rescue`. Fees are basis points capped at 10,000. Native transfers require `msg.value == amount`; token transfers use CRC20 safe transfer helpers and check the received amount. The contract rejects zero-value transfers and invalid treasury or recipient addresses. Review external call and token behavior before production use.

[`test/DistributeWithFee.t.sol`](https://github.com/core-laboratories/ylem-splitting/blob/6f810556e8e04b14fff3511c381f9b053664479a/test/DistributeWithFee.t.sol) covers native and token splits, fee extremes, owner restrictions, invalid inputs, failed native sends, and taxed-token behavior. This is source inspection, not a test result.

## Toolchain and workflow

[`foxar.toml`](https://github.com/core-laboratories/ylem-splitting/blob/6f810556e8e04b14fff3511c381f9b053664479a/foxar.toml) configures `src`, `out`, and `lib` paths. [`.gitmodules`](https://github.com/core-laboratories/ylem-splitting/blob/6f810556e8e04b14fff3511c381f9b053664479a/.gitmodules) declares `spark-std` and `openzeppelin-contracts` submodules. [CI](https://github.com/core-laboratories/ylem-splitting/blob/6f810556e8e04b14fff3511c381f9b053664479a/.github/workflows/test.yml) checks out submodules, installs a Foxar nightly toolchain, and runs `spark build --sizes` and `spark test -vvv` from the repository root. These are **documented in CI, not executed here**. No lockfile or exact nightly revision was identified in the inspected tree.

## Relationships and validation

See [`ylem`](../core-coin/ylem.md), [`foxar`](../bchainhub/foxar.md), and [`spark-std`](../bchainhub/spark-std.md) for related tasks. The submodule declarations are direct repository relationships; the other links are task routing. Dependencies were not installed, and build, tests, and runtime were not executed during this pass.
