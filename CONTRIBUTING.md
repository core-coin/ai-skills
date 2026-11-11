# Contributing

Thanks for improving Core Blockchain agent guidance.

## Before opening a pull request

1. Check existing issues and the [reference index](skills/core-blockchain/references/index.md) for related work.
2. Keep changes scoped to this repository. Do not include source checkouts, generated build output, credentials, or private keys.
3. For repository references, read the actual README and relevant manifests, build files, workflows, and source. Record the branch, full commit SHA, inspection date, and files supporting important claims. Use commit-pinned links where possible.
4. Separate documented commands from commands you ran. Record the working directory, prerequisites, and actual result for each executed check.
5. Update the index and research status when adding or revising references. Keep protocol claims distinct from proposals and owner-stated goals.
6. Run `python3 scripts/validate_skill.py` and `python3 scripts/check_format.py`. Install `requirements-ci.txt` in a virtual environment to run `python3 scripts/validate_github_config.py`. Include the results in the pull request.

Use focused pull requests with a clear explanation of what changed and why. Do not post vulnerabilities or secrets in public issues or pull requests; follow [SECURITY.md](SECURITY.md).

Contributions are provided under the repository's [CORE License](LICENSE).
