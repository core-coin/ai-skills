# core-coin/cip

- Repository: https://github.com/core-coin/cip
- Research status: **README, source tree, and selected files inspected**
- Inspection date: 2026-11-11
- Inspected branch: `master`
- Inspected commit: `0c2e54bbebebd506bb5d11a452e2d2f7a3cf3e51`
- Local research checkout: `/tmp/core-blockchain-research/core-coin/cip` (research only)
- README: [`README.md`](https://github.com/core-coin/cip/blob/0c2e54bbebebd506bb5d11a452e2d2f7a3cf3e51/README.md)

## Purpose and when to use it

Core Improvement Proposals document proposed and adopted Core protocol, networking, interface, CBC contract, informational, and process standards. Start here for normative standards questions, then read the specific proposal and its status. A `Final` proposal and a live network activation are different facts; verify implementation and activation in the relevant client source.

## Find the right proposal

Use [`static/llms.txt`](https://github.com/core-coin/cip/blob/0c2e54bbebebd506bb5d11a452e2d2f7a3cf3e51/static/llms.txt) as the compact machine-readable index, then open the individual linked proposal. The user has asked that the larger corpus no longer be used because it will be discontinued. The index says it includes final proposals and general documentation. For drafts and complete status tracking, inspect the source files under [`cip/`](https://github.com/core-coin/cip/tree/0c2e54bbebebd506bb5d11a452e2d2f7a3cf3e51/cip) and the [workflow guide](https://github.com/core-coin/cip/blob/0c2e54bbebebd506bb5d11a452e2d2f7a3cf3e51/docs/cip-workflow.md). Preserve normative words such as MUST and SHOULD when summarizing requirements.

The source tree contains `cip/core/`, `cip/networking/`, `cip/interface/`, `cip/cbc/`, `cip/informational/`, and `cip/meta/`. For example, [`cip/core/cip-98.md`](https://github.com/core-coin/cip/blob/0c2e54bbebebd506bb5d11a452e2d2f7a3cf3e51/cip/core/cip-98.md) declares `status: final` and specifies a Core cryptography scheme. Read proposal metadata and text at the same revision.

## Toolchain and validation

[`package.json`](https://github.com/core-coin/cip/blob/0c2e54bbebebd506bb5d11a452e2d2f7a3cf3e51/package.json) declares Node.js >=20 and Docusaurus 3.10.2. It defines `npm run build`, `npm run typecheck`, `npm run generate:llms`, and `npm run validate:llms` from the repository root. The [generation workflow](https://github.com/core-coin/cip/blob/0c2e54bbebebd506bb5d11a452e2d2f7a3cf3e51/.github/workflows/generate-llms.yml) and [`scripts/validate_llms.mjs`](https://github.com/core-coin/cip/blob/0c2e54bbebebd506bb5d11a452e2d2f7a3cf3e51/scripts/validate_llms.mjs) govern generated machine-readable files. These commands are **documented, not executed here**. Dependencies were not installed; build, tests, and runtime were not verified.

## Relationships

Use CIPs with [`go-core`](go-core.md) for client behavior, [`cvm`](cvm.md) for execution, and contract or wallet references for interface implementations. A proposal is evidence for a standard; confirm the implementation and activation state in current source before changing protocol behavior.
