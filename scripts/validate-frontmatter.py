#!/usr/bin/env python3
"""Validate that each docs article carries required YAML frontmatter.

Scans docs/**/*.md (excluding README.md index files) and checks for a
frontmatter block delimited by --- with the required keys. Index READMEs
and meta files are skipped. Exits non-zero on the first batch of errors.
"""
from __future__ import annotations
import sys, pathlib, re

REQUIRED = {"title", "difficulty", "reading_time_min", "status"}
ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

def frontmatter(text: str):
    if not text.startswith("---"):
        return None
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return None
    keys = set()
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z0-9_-]+)\s*:", line)
        if km:
            keys.add(km.group(1))
    return keys

def main() -> int:
    errors = []
    if not DOCS.exists():
        print("no docs/ directory; nothing to validate")
        return 0
    for md in sorted(DOCS.rglob("*.md")):
        if md.name.lower() == "readme.md":
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        keys = frontmatter(text)
        rel = md.relative_to(ROOT)
        if keys is None:
            errors.append(f"{rel}: missing YAML frontmatter block")
            continue
        missing = REQUIRED - keys
        if missing:
            errors.append(f"{rel}: missing frontmatter keys: {', '.join(sorted(missing))}")
    if errors:
        print("Frontmatter validation failed:")
        for e in errors:
            print(f"  ::error file={e.split(':')[0]}::{e}")
        return 1
    print("Frontmatter OK for all articles.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
