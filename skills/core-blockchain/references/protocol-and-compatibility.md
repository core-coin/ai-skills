# Protocol and compatibility

## Planning context

The following are project-owner goals supplied with this skill request. They are planning context, not verified claims about every repository. The intended client modernization should preserve the existing Core network and current proof-of-work behavior. The existing `core-coin/go-core` client is the behavioral reference. The owner describes Core as derived from pre-Merge Ethereum with modifications; inspect actual sources before documenting differences.

A future client should be able to run alongside `go-core`. Compare historical block validation, block hashes, state roots, receipts, energy accounting, rewards, fork choice, reorganizations, networking, and RPC behavior. Compare the same block hash, not just the latest height. Concurrent clients need separate data directories and ports.

Future desired features include reward halving, nonce-related changes, JSON-RPC and gRPC, and multiple smart-contract source languages. A faster nonce-search strategy does not itself change consensus nonce-validity rules. Multiple source languages targeting CVM do not necessarily require another VM. WASM smart contracts differ from executing a node runtime via WASM; adding WASM contract execution needs deterministic execution, resource metering, state and rollback rules, interfaces, and coordinated activation.

Polkadot SDK and Reth are architectural candidates to investigate, not selected or validated foundations. Polkadot SDK does not automatically provide Core-compatible blocks, transactions, state commitments, CVM execution, peer protocols, or RandomY. CometBFT is not a drop-in replacement for current PoW consensus. Check specific releases and authoritative documentation before claiming framework PoW support or maintenance status.

## Working rule

Use the [go-core reference](repositories/core-coin/go-core.md) and its inspected source as the starting point for compatibility questions. Consult the [CIP registry](repositories/core-coin/cip.md) for relevant specifications, checking each proposal's status and the client's actual implementation and activation. Reinspect the current checkout before proposing protocol changes.
