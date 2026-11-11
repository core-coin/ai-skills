# Contract Deployer: user-supplied README

The user supplied a Contract Deployer README without a repository URL, branch, or commit. This page records its described workflow and design constraints; its code, dependencies, and runtime were not inspected. Locate the actual checkout and verify the README against source before implementation.

## When to consult it

The described tool is a local TypeScript web GUI for compiling, deploying, and interacting with contracts on Core and several EVM chains. Core Devin is the default network; mainnets are opt-in. Use this guide for tasks involving its local GUI, compiler or artifact paths, fee review, signing, contract interactions, token transfers, or Core Safe integration. It is separate from the [`ylem`](repositories/core-coin/ylem.md) compiler and [`foxar`](repositories/bchainhub/foxar.md) framework.

## Reported workflow and boundaries

- The README documents `npm install`, `npm run ylem:install`, and `npm start` from the project root. It says the Ylem install checks a SHA-256 digest and the server binds `127.0.0.1:4848`. These commands were **not executed** in this workspace.
- `src/server/` owns keys, compilation, signing, chain calls, and local data. `src/client/` is the React UI; `src/shared/` contains shared validation and types.
- The README says secrets stay server-side, the server binds loopback, POST routes retain Host/Origin/content-type checks, and signing requires a user-approved quote. Changes to sending must preserve transaction locking and the `send.ts` path.
- Core and EVM chains have separate compiler artifacts and per-network data. RPC URLs may contain API keys and must not enter logs or documentation. Mainnet transactions and deployments require task-specific authorization.
- The README documents `npm run typecheck && npm test` after installing the Ylem binary for server tests. Those checks were **not run** here.

The pasted README describes optional local Deploy wizard source that is absent from Git. Do not assume it exists in a normal checkout. The README also states workarounds for a particular `corebc` version; verify dependency versions and actual behavior before changing them.
