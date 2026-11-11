#!/usr/bin/env python3
"""Check GitHub workflow and issue form YAML and required fields."""

from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
GITHUB = ROOT / ".github"


class UniqueKeyLoader(yaml.BaseLoader):
	def construct_mapping(self, node, deep=False):
		mapping = {}
		for key_node, value_node in node.value:
			key = self.construct_object(key_node, deep=deep)
			if key in mapping:
				raise yaml.constructor.ConstructorError(None, None, f"duplicate key: {key}", key_node.start_mark)
			mapping[key] = self.construct_object(value_node, deep=deep)
		return mapping


def read_yaml(path):
	with path.open(encoding="utf-8") as handle:
		return yaml.load(handle, Loader=UniqueKeyLoader)


def main() -> int:
	errors = []
	paths = sorted(GITHUB.rglob("*.yml"))
	parsed = {}
	for path in paths:
		try:
			data = read_yaml(path)
			if not isinstance(data, dict):
				errors.append(f"{path.relative_to(ROOT)}: expected a mapping")
			else:
				parsed[path.relative_to(GITHUB).as_posix()] = data
		except yaml.YAMLError as error:
			errors.append(f"{path.relative_to(ROOT)}: {error}")
	workflow = parsed.get("workflows/validate.yml", {})
	if not {"push", "pull_request"}.issubset(workflow.get("on", {})):
		errors.append("validation workflow must run on pushes and pull requests")
	if workflow.get("permissions", {}).get("contents") != "read":
		errors.append("validation workflow needs read-only contents permission")
	if not workflow.get("jobs", {}).get("validate", {}).get("steps"):
		errors.append("validation workflow has no steps")
	config = parsed.get("ISSUE_TEMPLATE/config.yml", {})
	if config.get("blank_issues_enabled") != "false":
		errors.append("blank issues must be disabled")
	for name in ("bug", "feature"):
		form = parsed.get(f"ISSUE_TEMPLATE/{name}.yml", {})
		body = form.get("body", [])
		if not form.get("name") or not isinstance(body, list) or not body:
			errors.append(f"{name} issue form needs a name and fields")
			continue
		if not all(field.get("validations", {}).get("required") == "true" for field in body):
			errors.append(f"{name} issue form has an optional field")
	if errors:
		print("\n".join(errors), file=sys.stderr)
		return 1
	print(f"Validated {len(paths)} GitHub YAML files and required issue fields.")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
