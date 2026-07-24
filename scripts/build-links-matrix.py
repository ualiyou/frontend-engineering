#!/usr/bin/env python3
"""Generate INTERNAL_LINKS.md — a human-readable view of all five relations
for every article, grouped by Part and Domain. Derived from the extended
graph.json files; regenerate whenever the graphs change."""
import os, glob, json, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = sorted(glob.glob(os.path.join(ROOT, "docs", "*", "*", "graph.json")))

def cell(items):
    return "; ".join(items) if items else "—"

def mistakes_cell(items):
    out = []
    for m in items:
        if m.startswith("anti-patterns/"):
            out.append(f"[domain pitfalls]({m})")
        elif m == "#common-mistakes":
            out.append("in-article")
        else:
            out.append(m)
    return "; ".join(out) if out else "—"

total = 0
parts = {}   # part -> list of (doc, file)
for f in files:
    doc = json.load(open(f))
    parts.setdefault(doc["part"], []).append((doc, f))

lines = []
lines.append("# Internal Links — Per-Article Matrix")
lines.append("")
lines.append("> The five internal-linking relations for **every** article, generated from each domain's "
             "`graph.json`. This is the human-readable companion to the machine-readable graph; the model and "
             "rules are defined in [`INTERNAL_LINKING.md`](INTERNAL_LINKING.md). Do not edit by hand — run "
             "`scripts/build-links-matrix.py`.")
lines.append("")
lines.append("**Columns:** *Prerequisites* (read before) · *Next* (read after, ≤5) · *Related* (see-also) · "
             "*Alternatives* (substitutes) · *Common Mistakes* (links into the "
             "[anti-pattern catalog](anti-patterns/README.md) + the article's own section). "
             "A reference is `Title` when globally unique, else `Title · Domain`.")

for part in sorted(parts):
    lines.extend(["", f"## {part}", ""])
    for index, (doc, f) in enumerate(sorted(parts[part], key=lambda x: x[0]["nodes"][0]["order"] if x[0]["nodes"] else 0)):
        dom = doc["domain"]
        if index:
            lines.append("")
        lines.extend([f"### {dom}  ({doc.get('node_count', len(doc['nodes']))} articles)", ""])
        lines.append("| # | Article | Prerequisites | Next | Related | Alternatives | Common Mistakes |")
        lines.append("| --- | --- | --- | --- | --- | --- | --- |")
        for n in sorted(doc["nodes"], key=lambda n: n.get("order", 0)):
            total += 1
            lines.append("| {order} | {title} | {pre} | {nxt} | {rel} | {alt} | {mis} |".format(
                order=n.get("order", ""),
                title=n["title"].replace("|", "\\|"),
                pre=cell(n.get("prerequisites", [])).replace("|", "\\|"),
                nxt=cell(n.get("next", [])).replace("|", "\\|"),
                rel=cell(n.get("related", [])).replace("|", "\\|"),
                alt=cell(n.get("alternatives", [])).replace("|", "\\|"),
                mis=mistakes_cell(n.get("common_mistakes", [])).replace("|", "\\|"),
            ))

open(os.path.join(ROOT, "INTERNAL_LINKS.md"), "w").write("\n".join(lines) + "\n")
print(f"wrote INTERNAL_LINKS.md — {total} articles across {len(files)} domains")
