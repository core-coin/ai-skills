# DataLayerHost/kamailio-txms

- Repository: https://github.com/DataLayerHost/kamailio-txms
- Research status: **source inspected**
- Inspection date: 2026-11-11
- Inspected branch: `main`
- Inspected commit: `8a93383ee09b774b4570677d624ceccacf61e6fb`
- Local research checkout: `/tmp/core-blockchain-research/DataLayerHost/kamailio-txms` (research only; not required to use this skill)
- README: [`README.md`](https://github.com/DataLayerHost/kamailio-txms/blob/8a93383ee09b774b4570677d624ceccacf61e6fb/README.md)

## Purpose and selection

Kamailio module that receives TxMS messages and queues transactions.
The [`README.md`](https://github.com/DataLayerHost/kamailio-txms/blob/8a93383ee09b774b4570677d624ceccacf61e6fb/README.md) is the starting evidence for this role. Use this repository for tasks involving its documented interface; inspect the current source before choosing it over similarly named projects.

## Architecture and source entry points

Inspected source entry point: [`src/rpc.c`](https://github.com/DataLayerHost/kamailio-txms/blob/8a93383ee09b774b4570677d624ceccacf61e6fb/src/rpc.c).
Root build or package files: [`CMakeLists.txt`](https://github.com/DataLayerHost/kamailio-txms/blob/8a93383ee09b774b4570677d624ceccacf61e6fb/CMakeLists.txt), [`Makefile`](https://github.com/DataLayerHost/kamailio-txms/blob/8a93383ee09b774b4570677d624ceccacf61e6fb/Makefile).
Source or project directories to inspect first: `fuzz/`, `include/`, `module/`, `src/`, `tools/`.
Examples or tests visible in the tree: [`tests/rpc_server.py`](https://github.com/DataLayerHost/kamailio-txms/blob/8a93383ee09b774b4570677d624ceccacf61e6fb/tests/rpc_server.py), [`tests/sip_integration.py`](https://github.com/DataLayerHost/kamailio-txms/blob/8a93383ee09b774b4570677d624ceccacf61e6fb/tests/sip_integration.py), [`tests/test_release.py`](https://github.com/DataLayerHost/kamailio-txms/blob/8a93383ee09b774b4570677d624ceccacf61e6fb/tests/test_release.py).

## Toolchain, setup, and validation

Detected language/platform: **C / C++**. This is based on the inspected tree and manifests, not a verified runtime environment.

Repository-documented commands (working directory: repository root; **documented, not executed here**; install dependencies and review prerequisites in the README first):

- `make test`

## Configuration, interfaces, and relationships

README sections to consult: `Architecture`, `Build and install`, `Configuration and routing`, `Gateway formats and SMS`, `Multipart concurrency and limits`, `MMS support and limitations`, `Core RPC and recovery`, `Tests and troubleshooting`.
Example configuration files: [`.env.example`](https://github.com/DataLayerHost/kamailio-txms/blob/8a93383ee09b774b4570677d624ceccacf61e6fb/.env.example). Do not copy example secrets into production.
Related references by task (not verified direct dependencies): [`DataLayerHost/libtxms`](libtxms.md), [`DataLayerHost/txms-server`](txms-server.md).
Similar naming or a sibling checkout does not establish a direct dependency; verify imports and manifest versions before linking projects.

## Compatibility and evidence

Primary evidence: [`README.md`](https://github.com/DataLayerHost/kamailio-txms/blob/8a93383ee09b774b4570677d624ceccacf61e6fb/README.md), [`src/rpc.c`](https://github.com/DataLayerHost/kamailio-txms/blob/8a93383ee09b774b4570677d624ceccacf61e6fb/src/rpc.c), [`CMakeLists.txt`](https://github.com/DataLayerHost/kamailio-txms/blob/8a93383ee09b774b4570677d624ceccacf61e6fb/CMakeLists.txt), [`Makefile`](https://github.com/DataLayerHost/kamailio-txms/blob/8a93383ee09b774b4570677d624ceccacf61e6fb/Makefile), [`.github/workflows/ci.yml`](https://github.com/DataLayerHost/kamailio-txms/blob/8a93383ee09b774b4570677d624ceccacf61e6fb/.github/workflows/ci.yml), [`.github/workflows/release.yml`](https://github.com/DataLayerHost/kamailio-txms/blob/8a93383ee09b774b4570677d624ceccacf61e6fb/.github/workflows/release.yml).
The source tree and listed text files were inspected at the commit above. Dependencies were **not installed**; build, tests, and runtime were **not executed**. Confirm protocol, encoding, cryptographic, and version behavior in current code before implementation. README instructions may differ from newer manifests or CI.
