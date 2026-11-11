# Core Blockchain Ecosystem Skills

Reusable coding-agent guidance for the Core Blockchain ecosystem.

## Available skill

| Skill | Use it for |
| --- | --- |
| [core-blockchain](skills/core-blockchain/SKILL.md) | Core protocol, clients, mining, CVM contracts, cryptography, SDKs, wallets, APIs, and operations. |

The skill routes agents to [88 repository references](skills/core-blockchain/references/index.md) and cross-cutting compatibility notes. Each reference records its inspected source revision and what was actually validated. Research notes do not assert that every project is maintained or production ready.

## Install

Install [Node.js 22.20 or later](https://nodejs.org/en/download) first. It includes `npm` and `npx`. Check the version in your terminal:

```sh
node --version
```

The [Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) runs through `npx`, so it does not need a separate installation. To download the CLI and check that it works:

```sh
npx skills --help
```

Then install this repository's skill in the current project:

```sh
npx skills add core-coin/ai-skills --skill core-blockchain
```

To make it available to Codex across projects, use:

```sh
npx skills add core-coin/ai-skills --skill core-blockchain -g -a codex
```

These commands install the skill from GitHub. They do not publish the repository to a registry.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for evidence and validation requirements.

## Security

Report vulnerabilities as described in [SECURITY.md](SECURITY.md).

## License

This repository uses the [CORE License](LICENSE).
