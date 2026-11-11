#!/usr/bin/env python3
"""Check text formatting without rewriting project files."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
FILES = [
	ROOT / ".gitignore",
	ROOT / "LICENSE",
	ROOT / "README.md",
	ROOT / "CONTRIBUTING.md",
	ROOT / "SECURITY.md",
	ROOT / "requirements-ci.txt",
	*ROOT.joinpath("skills").rglob("*.md"),
	*ROOT.joinpath("scripts").glob("*.py"),
	*ROOT.joinpath(".github").rglob("*.yml"),
]


def main() -> int:
	errors = []
	for path in FILES:
		if not path.is_file():
			errors.append(f"missing file: {path.relative_to(ROOT)}")
			continue
		data = path.read_bytes()
		relative = path.relative_to(ROOT)
		if b"\r" in data:
			errors.append(f"{relative}: use LF line endings")
		if data and not data.endswith(b"\n"):
			errors.append(f"{relative}: add a final newline")
		for number, line in enumerate(data.splitlines(), 1):
			if line.rstrip(b" \t") != line:
				errors.append(f"{relative}:{number}: trailing whitespace")
			if path.suffix in {".yml", ".yaml"} and b"\t" in line:
				errors.append(f"{relative}:{number}: YAML cannot use tabs for indentation")
	if errors:
		print("\n".join(errors), file=sys.stderr)
		return 1
	print(f"Checked formatting of {len(FILES)} text files.")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
