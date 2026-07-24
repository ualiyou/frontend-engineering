#!/usr/bin/env python3
"""
build-links.py — Internal-linking generator for the Frontend Engineering wiki.

Reads every domain `graph.json`, then derives and writes back three new
relation arrays per article node, additive to the existing
`prerequisites` and `related`:

  - next            forward learning path (inverse of prerequisites)
  - alternatives    parallel/substitute approaches to the same problem
  - common_mistakes links into the anti-pattern catalog

The prerequisite DAG is the source of truth; `next` is its exact inverse,
so the two never disagree. All derivations are deterministic and idempotent:
re-running reproduces byte-identical output. This is a v1 *baseline* — authors
refine per-article edges as articles are written (same policy the repo already
applies to prerequisites/related).

Reference convention (unchanged from the existing data):
  a link target is written as the bare "Title" when that title is globally
  unique, otherwise as "Title · Domain".
"""
import json, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRAPH_FILES = sorted(glob.glob(os.path.join(ROOT, "docs", "*", "*", "graph.json")))

MAX_NEXT = 5
MAX_ALTERNATIVES = 4

# ---------------------------------------------------------------- load
graphs = {}          # path -> parsed doc
nodes_by_ref = {}    # canonical ref -> node record
title_count = {}     # title -> how many domains define it

def domain_slug(dom):
    return re.sub(r"[^a-z0-9]+", "-", dom.lower()).strip("-")

records = []  # flat list of (path, domain, node)
for f in GRAPH_FILES:
    doc = json.load(open(f))
    graphs[f] = doc
    dom = doc["domain"]
    for node in doc["nodes"]:
        title_count[node["title"]] = title_count.get(node["title"], 0) + 1
        records.append((f, dom, node))

def ref_of(title, domain):
    """Canonical reference string for a node."""
    return title if title_count.get(title, 0) == 1 else f"{title} · {domain}"

# Build the canonical registry.
for f, dom, node in records:
    node["_domain"] = dom
    node["_ref"] = ref_of(node["title"], dom)
    nodes_by_ref[node["_ref"]] = node

by_title = {}
for n in nodes_by_ref.values():
    by_title.setdefault(n["title"], []).append(n)

def resolve(ref, home_domain):
    """Resolve a prerequisite/related string to a node record, or None.
    Handles bare titles and the explicit 'Title · Domain' cross-domain form,
    even when the title is globally unique (canonical ref is then the bare title)."""
    if ref in nodes_by_ref:
        return nodes_by_ref[ref]
    if " · " in ref:
        title, dom = ref.rsplit(" · ", 1)
    else:
        title, dom = ref, home_domain
    cand = ref_of(title, dom)
    if cand in nodes_by_ref:
        return nodes_by_ref[cand]
    hits = by_title.get(title, [])
    if len(hits) == 1:
        return hits[0]
    for h in hits:
        if h["_domain"] == dom:
            return h
    return None

# ---------------------------------------------------------------- next (inverse prereqs)
# For every prerequisite edge P -> X (X depends on P), record X as a "next" of P.
for f, dom, node in records:
    for p in node.get("prerequisites", []):
        target = resolve(p, dom)
        if target is None:
            continue
        target.setdefault("_next_set", [])
        if node["_ref"] not in target["_next_set"]:
            target["_next_set"].append(node["_ref"])

# ---------------------------------------------------------------- alternatives
# Same subcategory + identical prerequisite set + no dependency either way.
# Identical starting point = genuine parallel options branching from the same base.
def norm_prereqs(node, dom):
    s = set()
    for p in node.get("prerequisites", []):
        t = resolve(p, dom)
        if t is not None:
            s.add(t["_ref"])
    return frozenset(s)

# index by (domain, subcategory)
by_subcat = {}
for f, dom, node in records:
    by_subcat.setdefault((dom, node.get("subcategory")), []).append((node, dom))

for (dom, sub), members in by_subcat.items():
    for node, d in members:
        mine = norm_prereqs(node, d)
        alts = []
        for other, od in members:
            if other is node:
                continue
            if norm_prereqs(other, od) == mine and other["_ref"] not in mine \
               and node["_ref"] not in norm_prereqs(other, od):
                alts.append(other)
        alts.sort(key=lambda n: n.get("order", 0))
        node["_alts"] = [a["_ref"] for a in alts[:MAX_ALTERNATIVES]]

# ---------------------------------------------------------------- common_mistakes
# Internal links into the anti-pattern catalog: every article points at its
# domain's signature-pitfalls entry plus its own in-article section.
for f, dom, node in records:
    slug = domain_slug(dom)
    node["_mistakes"] = [
        f"anti-patterns/README.md#{slug}",   # domain-level pitfalls catalog
        f"#common-mistakes",                  # this article's own section
    ]

# ---------------------------------------------------------------- finalize next
_dep_cache = {}
def _direct_prereq_refs(node, dom):
    out = []
    for p in node.get("prerequisites", []):
        t = resolve(p, dom)
        if t is not None:
            out.append(t["_ref"])
    return out

def _ancestors(ref):
    if ref in _dep_cache:
        return _dep_cache[ref]
    seen, stack = set(), list(_direct_prereq_refs(nodes_by_ref[ref], nodes_by_ref[ref]["_domain"]))
    while stack:
        x = stack.pop()
        if x in seen:
            continue
        seen.add(x)
        stack.extend(_direct_prereq_refs(nodes_by_ref[x], nodes_by_ref[x]["_domain"]))
    _dep_cache[ref] = seen
    return seen

for f, dom, node in records:
    nxt = node.get("_next_set", [])
    # order by global reading order of the target
    nxt_sorted = sorted(nxt, key=lambda r: nodes_by_ref[r].get("order", 0))
    if not nxt_sorted:
        # fallback: next article by order within the same subcategory, else domain
        same_sub = sorted(
            [n for (df, dd, n) in records
             if dd == dom and n.get("subcategory") == node.get("subcategory")
             and n.get("order", 0) > node.get("order", 0)],
            key=lambda n: n.get("order", 0))
        pool = same_sub or sorted(
            [n for (df, dd, n) in records
             if dd == dom and n.get("order", 0) > node.get("order", 0)],
            key=lambda n: n.get("order", 0))
        if pool:
            nxt_sorted = [pool[0]["_ref"]]
        else:
            # domain terminal: continue into the globally next article by order
            # that is NOT already an ancestor (prerequisite) of this node.
            anc = _ancestors(node["_ref"])
            later = sorted(
                [n for (df, dd, n) in records
                 if n.get("order", 0) > node.get("order", 0) and n["_ref"] not in anc],
                key=lambda n: n.get("order", 0))
            nxt_sorted = [later[0]["_ref"]] if later else []
    node["_next"] = nxt_sorted[:MAX_NEXT]

# ---------------------------------------------------------------- write back
# Insert the new arrays right after `related`, preserving field order.
def rebuild(node):
    out = {}
    for k, v in node.items():
        if k.startswith("_"):
            continue
        out[k] = v
        if k == "related":
            out["next"] = node["_next"]
            out["alternatives"] = node["_alts"]
            out["common_mistakes"] = node["_mistakes"]
    # if a node had no `related` key, append at end
    if "next" not in out:
        out["next"] = node["_next"]
        out["alternatives"] = node["_alts"]
        out["common_mistakes"] = node["_mistakes"]
    return out

for f, doc in graphs.items():
    doc["nodes"] = [rebuild(n) for n in doc["nodes"]]
    with open(f, "w") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

print(f"Extended {len(graphs)} graph.json files, {len(records)} nodes.")

# quick stats
import statistics
nexts = [len(n["_next"]) for _, _, n in records]
alts  = [len(n["_alts"]) for _, _, n in records]
print(f"next:  min {min(nexts)} max {max(nexts)} mean {statistics.mean(nexts):.2f} | zero: {sum(1 for x in nexts if x==0)}")
print(f"alts:  min {min(alts)} max {max(alts)} mean {statistics.mean(alts):.2f} | zero: {sum(1 for x in alts if x==0)}")
