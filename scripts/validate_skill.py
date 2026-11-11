#!/usr/bin/env python3
"""Validate local skill structure and repository reference links without dependencies."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/core-blockchain"
REFS = SKILL / "references"
REPOS = REFS / "repositories"
EXPECTED = 88


def main() -> int:
	errors = []
	entry = (SKILL / "SKILL.md").read_text()
	if not re.match(r"\A---\nname: core-blockchain\ndescription: .+\n---\n", entry):
		errors.append("SKILL.md needs name and description frontmatter")
	pages = sorted(REPOS.glob("*/*.md"))
	if len(pages) != EXPECTED:
		errors.append(f"expected {EXPECTED} repository pages, found {len(pages)}")
	index = (REFS / "index.md").read_text()
	for page in pages:
		rel = page.relative_to(REFS).as_posix()
		if f"({rel})" not in index:
			errors.append(f"index does not link {rel}")
		body = page.read_text()
		sha = re.search(r"^- Inspected commit: `([a-f0-9]{40})`$", body, re.M)
		for url in re.findall(r"https://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/([^\s)]+)", body):
			owner, repo, commit, _ = url
			target = REPOS / owner / f"{repo}.md"
			target_body = target.read_text() if target.exists() else ""
			target_sha = re.search(r"^- Inspected commit: `([a-f0-9]{40})`$", target_body, re.M)
			if not target_sha or commit != target_sha.group(1):
				errors.append(f"source evidence mismatch in {rel}")
		if "source inspected" in body and not sha:
			errors.append(f"missing commit in {rel}")
	for page in [ROOT / "README.md", SKILL / "SKILL.md", *REFS.rglob("*.md")]:
		body = page.read_text()
		for dest in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", body):
			if re.match(r"[a-z]+://", dest):
				continue
			if not (page.parent / dest).exists():
				errors.append(f"broken local link in {page.relative_to(ROOT)}: {dest}")
	if errors:
		for error in errors:
			print(f"ERROR: {error}", file=sys.stderr)
		return 1
	print(f"Validated {len(pages)} repository pages, index coverage, frontmatter, and links.")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
