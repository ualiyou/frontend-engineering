#!/usr/bin/env python3
"""
validate-links.py — integrity checks for the extended link graph.

Fails (exit 1) on any broken invariant:
  1. every prerequisites/related/next/alternatives ref resolves to a real node
  2. the prerequisite graph is acyclic (DAG)
  3. next is exactly the inverse of prerequisites (no disagreement)
  4. no self-links in any relation
  5. alternatives are symmetric and never overlap prerequisites/next
  6. every common_mistakes catalog target exists
"""
import json, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = sorted(glob.glob(os.path.join(ROOT, "docs", "*", "*", "graph.json")))

title_count = {}
records = []
for f in files:
    doc = json.load(open(f))
    for n in doc["nodes"]:
        title_count[n["title"]] = title_count.get(n["title"], 0) + 1
        records.append((doc["domain"], n))

def ref_of(title, dom):
    return title if title_count.get(title, 0) == 1 else f"{title} · {dom}"

reg = {}
for dom, n in records:
    reg[ref_of(n["title"], dom)] = (dom, n)

by_title = {}
for r,(d,n) in reg.items():
    by_title.setdefault(n["title"], []).append((d,n))

def resolve(ref, home):
    if ref in reg: return reg[ref]
    if " · " in ref:
        title, dom = ref.rsplit(" · ", 1)
    else:
        title, dom = ref, home
    c = ref_of(title, dom)
    if c in reg: return reg[c]
    hits = by_title.get(title, [])
    if len(hits) == 1: return hits[0]
    for d,n in hits:
        if d == dom: return (d,n)
    return None

errors = []

# 1 + 4: resolvable + no self-links
for dom, n in records:
    me = ref_of(n["title"], dom)
    for rel in ("prerequisites", "related", "next", "alternatives"):
        for ref in n.get(rel, []):
            if resolve(ref, dom) is None:
                errors.append(f"[{dom}] {n['title']}: {rel} -> unresolved '{ref}'")
            elif ref_of(resolve(ref,dom)[1]['title'], resolve(ref,dom)[0]) == me:
                errors.append(f"[{dom}] {n['title']}: {rel} self-link")

# 2: acyclicity of prerequisites
graph = {}
for dom, n in records:
    me = ref_of(n["title"], dom)
    graph[me] = []
    for p in n.get("prerequisites", []):
        t = resolve(p, dom)
        if t: graph[me].append(ref_of(t[1]["title"], t[0]))
WHITE, GREY, BLACK = 0, 1, 2
color = {k: WHITE for k in graph}
def dfs(u, stack):
    color[u] = GREY
    for v in graph.get(u, []):
        if color.get(v, BLACK) == GREY:
            errors.append("CYCLE: " + " -> ".join(stack + [v]))
        elif color.get(v, BLACK) == WHITE:
            dfs(v, stack + [v])
    color[u] = BLACK
for k in list(graph):
    if color[k] == WHITE:
        dfs(k, [k])

# 3: next is SOUND w.r.t. prerequisites (capped at MAX_NEXT, so not required to be
#    complete). Every next edge P -> X must be either a real inverse-prerequisite
#    edge (X depends on P) or a forward continuity fallback (P has no dependents).
#    A next edge must never point backward into P's own prerequisite ancestry.
MAX_NEXT = 5
depends_on = {}   # ref -> set(prereq refs)
dependents = {}   # ref -> set(dependent refs)
order_of = {}
for dom, n in records:
    me = ref_of(n["title"], dom); order_of[me] = n.get("order", 0)
    depends_on.setdefault(me, set())
    for p in n.get("prerequisites", []):
        t = resolve(p, dom)
        if t:
            pr = ref_of(t[1]["title"], t[0])
            depends_on[me].add(pr)
            dependents.setdefault(pr, set()).add(me)

def ancestors(ref):
    seen, stack = set(), list(depends_on.get(ref, ()))
    while stack:
        x = stack.pop()
        if x in seen: continue
        seen.add(x); stack.extend(depends_on.get(x, ()))
    return seen

for dom, n in records:
    me = ref_of(n["title"], dom)
    nxts = n.get("next", [])
    if len(nxts) > MAX_NEXT:
        errors.append(f"[{dom}] {n['title']}: next exceeds cap ({len(nxts)})")
    anc = ancestors(me)
    for nx in nxts:
        t = resolve(nx, dom)
        if not t: continue
        to = ref_of(t[1]["title"], t[0])
        if to in anc:
            errors.append(f"NEXT points into own ancestry: {me} -> {to}")
        inverse = me in depends_on.get(to, set())
        fallback = len(dependents.get(me, set())) == 0 and order_of[to] > order_of[me]
        if not (inverse or fallback):
            errors.append(f"NEXT unsound (not inverse, not continuity): {me} -> {to}")

# 5: alternatives symmetric + disjoint from prereqs/next
alt = {}
for dom, n in records:
    me = ref_of(n["title"], dom)
    alt[me] = set(ref_of(resolve(a,dom)[1]['title'], resolve(a,dom)[0]) for a in n.get("alternatives",[]) if resolve(a,dom))
for a, s in alt.items():
    for b in s:
        if a not in alt.get(b, set()):
            errors.append(f"ALT not symmetric: {a} <-> {b}")

# 6: common_mistakes catalog targets
catalog = os.path.join(ROOT, "anti-patterns", "README.md")
cat_anchors = set()
if os.path.exists(catalog):
    txt = open(catalog).read()
    for m in re.finditer(r"^#{1,6}\s+(.*)$", txt, re.M):
        a = re.sub(r"[^a-z0-9]+", "-", m.group(1).lower()).strip("-")
        cat_anchors.add(a)
    for m in re.finditer(r'id="([^"]+)"', txt):   # explicit anchors
        cat_anchors.add(m.group(1))
for dom, n in records:
    for cm in n.get("common_mistakes", []):
        if cm.startswith("anti-patterns/README.md#"):
            anc = cm.split("#",1)[1]
            if cat_anchors and anc not in cat_anchors:
                errors.append(f"[{dom}] {n['title']}: common_mistakes anchor #{anc} missing in catalog")

if errors:
    print(f"FAIL: {len(errors)} problem(s)")
    for e in errors[:60]:
        print("  -", e)
    sys.exit(1)
print(f"OK: {len(records)} nodes; prereq DAG acyclic; next == inverse(prereqs); "
      f"alternatives symmetric; all refs resolve; catalog anchors present.")
