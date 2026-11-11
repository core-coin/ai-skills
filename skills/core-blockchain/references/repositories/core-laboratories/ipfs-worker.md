# core-laboratories/ipfs-worker

- Repository: https://github.com/core-laboratories/ipfs-worker
- Research status: **README supplied by the user; repository source inaccessible**
- Inspection date: 2026-11-11
- Inspected branch and commit: unavailable
- Local research checkout: unavailable
- README path: reported as `README.md`; its content was supplied in this conversation, not verified in GitHub

## Purpose and when to use it

The supplied README describes a Cloudflare Worker that proxies IPFS and IPNS requests through configured public gateways. Use this reference for gateway routing, private access, bans, and error behavior. The source, package manifest, tests, and current deployment state remain unverified.

## Routes and behavior described by the README

- Subdomain forms: `{CID}.ipfs.ipf.sk/path` and `{label}.ipns.ipf.sk/path`.
- Path forms: `ipf.sk/ipfs/{CID}/path` and `ipf.sk/ipns/{label}/path`.
- Apex shortcut: `ipf.sk/{CID}/path`, for IPFS CIDs only. The README says CID v0 and v1 are supported and shortcut CIDs are validated.
- IPNS subdomain labels encode `.` as `-` and `-` as `--`.
- Providers are requested in parallel; the first successful response wins and slower requests are aborted. If all fail, the README specifies a 502 response. Image requests receive an SVG placeholder on error.

## Configuration and access control

`BANS` is a required Cloudflare KV binding. `REGISTRY` is an optional KV binding and is required when `PRIVATE=true`. `GATEWAY_PROVIDERS` is a required Wrangler secret containing provider URLs as a JSON array or comma/newline-separated list. The README documents `npx wrangler secret put GATEWAY_PROVIDERS` from the repository root; it changes remote configuration and was **not executed**. The README says `storry.tv` is ignored even if configured. Ban and registry records may contain an ISO `expiration`; expired entries are ignored, and bans take precedence over allow-list entries. Invalid JSON in a ban record is described as a permanent ban.

The README points to `wrangler.jsonc` for KV bindings, variables, and domain settings. Verify its actual contents before changing deployment configuration. Avoid embedding gateway credentials in this reference.

## Documented local workflow

Working directory: repository root. The supplied README lists `npm install`, `npm run dev`, and `npm test` after Node.js, Wrangler, and Cloudflare account setup. It also lists `npm run deploy`, which changes remote infrastructure and requires task-specific authorization. These commands are **documented, not executed**; script definitions and versions were not available to check.

## Evidence and limits

This page summarizes the README text provided by the user. GitHub REST and the connected GitHub tool returned 404 during the source research pass. No commit, source file, manifest, dependency installation, build, test, or runtime behavior was verified. Check repository access and current source before implementation or operations.
