#!/usr/bin/env python3
"""Offline checks for the public skill package; no host configuration or API access."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
NAMES = {
    "job-search-brief", "linkedin-search-plan", "job-research",
    "fit-review", "company-brief", "shortlist-review",
}
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def local_links(path: Path, boundary: Path) -> list[str]:
    errors = []
    for target in LINK.findall(path.read_text(encoding="utf-8")):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
            continue
        relative = target.split("#", 1)[0]
        resolved = (path.parent / relative).resolve()
        if not resolved.is_relative_to(boundary.resolve()):
            errors.append(f"{path.relative_to(ROOT)}: link escapes its package: {target}")
        elif not resolved.is_file():
            errors.append(f"{path.relative_to(ROOT)}: missing link target: {target}")
    return errors


def validate() -> list[str]:
    errors = []
    folders = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    if folders != NAMES:
        errors.append(f"Expected the six named skills; got {sorted(folders)}")
    for name in sorted(NAMES):
        folder = ROOT / "skills" / name
        entry = folder / "SKILL.md"
        if not entry.is_file():
            errors.append(f"Missing {name}/SKILL.md")
            continue
        text = entry.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not match:
            errors.append(f"{name}: malformed YAML frontmatter")
            continue
        try:
            metadata = yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            errors.append(f"{name}: frontmatter is not valid YAML")
            continue
        if not isinstance(metadata, dict):
            errors.append(f"{name}: frontmatter must be a mapping")
            continue
        if metadata.get("name") != name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(f"{name}: skill name must match its folder")
        description = metadata.get("description")
        if not isinstance(description, str) or not description.strip() or len(description) > 1024:
            errors.append(f"{name}: description must be a nonempty string of at most 1024 characters")
        body = text[match.end():].strip()
        if not body or "[TODO:" in body:
            errors.append(f"{name}: missing or unfinished instructions")
        for page in folder.rglob("*.md"):
            errors.extend(local_links(page, folder))
        for path in folder.rglob("*"):
            if path.is_symlink():
                errors.append(f"{name}: symlink is not independently portable: {path.name}")

    for directory in (ROOT, ROOT / "docs", ROOT / "checks", ROOT / "examples"):
        for page in directory.glob("*.md"):
            errors.extend(local_links(page, ROOT))
    for path in (ROOT / "examples").glob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeError):
            errors.append(f"Invalid example JSON: {path.name}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Validated 6 independently portable skills, package links and example JSON (offline).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
