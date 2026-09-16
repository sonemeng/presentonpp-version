#!/usr/bin/env python3
"""Validate a template metadata JSON file without external dependencies."""

import json
import re
import sys
from pathlib import Path

IDENTIFIER = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_TEMPLATE_FIELDS = ("id", "name", "description", "layouts")
REQUIRED_LAYOUT_FIELDS = ("id", "name", "purpose")


def is_nonempty_string(value):
    return isinstance(value, str) and bool(value.strip())


def validate(document):
    errors = []
    if not isinstance(document, dict):
        return ["Root value must be an object."]

    for field in REQUIRED_TEMPLATE_FIELDS:
        if field not in document:
            errors.append(f"Missing required field: {field}.")

    template_id = document.get("id")
    if not is_nonempty_string(template_id) or not IDENTIFIER.fullmatch(template_id):
        errors.append("id must use lowercase kebab-case.")

    for field in ("name", "description"):
        if not is_nonempty_string(document.get(field)):
            errors.append(f"{field} must be a non-empty string.")

    tags = document.get("tags", [])
    if not isinstance(tags, list) or any(not is_nonempty_string(tag) for tag in tags):
        errors.append("tags must be an array of non-empty strings when present.")
    elif len(tags) != len(set(tags)):
        errors.append("tags must not contain duplicate values.")

    layouts = document.get("layouts")
    if not isinstance(layouts, list) or not layouts:
        errors.append("layouts must be a non-empty array.")
        return errors

    seen_layout_ids = set()
    for index, layout in enumerate(layouts):
        prefix = f"layouts[{index}]"
        if not isinstance(layout, dict):
            errors.append(f"{prefix} must be an object.")
            continue
        for field in REQUIRED_LAYOUT_FIELDS:
            if field not in layout:
                errors.append(f"{prefix} is missing required field: {field}.")
        layout_id = layout.get("id")
        if not is_nonempty_string(layout_id) or not IDENTIFIER.fullmatch(layout_id):
            errors.append(f"{prefix}.id must use lowercase kebab-case.")
        elif layout_id in seen_layout_ids:
            errors.append(f"{prefix}.id duplicates {layout_id!r}.")
        else:
            seen_layout_ids.add(layout_id)
        for field in ("name", "purpose"):
            if not is_nonempty_string(layout.get(field)):
                errors.append(f"{prefix}.{field} must be a non-empty string.")
    return errors


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_template.py <template.json>", file=sys.stderr)
        return 2
    try:
        document = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Cannot read template metadata: {exc}", file=sys.stderr)
        return 2

    errors = validate(document)
    if errors:
        print("Template metadata is invalid:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("Template metadata is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
