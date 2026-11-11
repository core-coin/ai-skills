# core-laboratories/oric

- Repository: https://github.com/core-laboratories/oric
- Research status: **README supplied by the user; repository source inaccessible**
- Inspection date: 2026-11-11
- Inspected branch and commit: unavailable
- Local research checkout: unavailable
- README path: reported as `README.md`; its content was supplied in this conversation, not verified in GitHub

## Purpose and when to use it

The supplied README describes a Hono API for validating, decomposing, storing, and looking up ORIC codes. Use it for ORIC API integration or service behavior, then verify the current source before relying on endpoint contracts or deployment configuration.

## Documented API

The README lists health endpoints `GET /ping`, `GET /time`, and `GET /health`. ORIC operations include `GET /` for KV keys, `GET /test/:code` for validation, `GET /list/:code` for prefix lookup, `GET /:code` for an exact lookup, `GET /analyze/:code` for decomposition, and `GET /verify/:code/:address` for matching a stored address case-insensitively. Specific response codes described include `400.01` (invalid format), `404.01` (missing result), `422.01` (address mismatch), and `500.01` (server error). Check route ordering in source because the general `/:code` route overlaps named paths.

The supplied README describes versioned `oric-v1.payto.onl` and latest `oric.payto.onl` hostnames. It links a Postman collection at https://www.postman.com/core-labs/payto. These are documented interfaces, not live endpoints verified during this research pass.

## Configuration and local workflow

The README names `ORIC_KV_STAGING_ID` and `ORIC_KV_PRODUCTION_ID` for environment-specific KV namespaces. It says `*.payto.onl` hosts use production and other hosts use staging. Verify this host selection and KV binding behavior in source before deployment.

Working directory: repository root. The supplied README lists `npm install` and `npm run dev`; `npm run deploy` changes remote infrastructure and requires task-specific authorization. These commands are **documented, not executed**. No test command or version pin was supplied.

## Evidence and limits

This page summarizes the README text provided by the user. GitHub REST and the connected GitHub tool returned 404 during the source research pass. No commit, source file, manifest, dependency installation, build, test, or runtime behavior was verified.
