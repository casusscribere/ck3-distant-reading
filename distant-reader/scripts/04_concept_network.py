#!/usr/bin/env python3
"""04_concept_network.py — Step 6 of Salter's methodology.

Sentence-level co-occurrence network weighted by Pointwise Mutual Information.
Nodes are key terms (from TF-IDF top list or a user-supplied list); edges
connect terms that co-occur more than chance.

For fiction corpora: use character names. For academic corpora: use concept
keywords. For mixed: let user decide via --nodes flag.
"""
import argparse, collections, json, math, pathlib, re

ap = argparse.ArgumentParser()
ap.add_argument("corpus_dir", type=pathlib.Path)
ap.add_argument("--analysis-dir", type=pathlib.Path, default=pathlib.Path("analysis"))
ap.add_argument("--nodes", help="Comma-separated list of node terms; defaults to top TF-IDF terms")
ap.add_argument("--min-co", type=int, default=10, help="Minimum co-occurrence count")
ap.add_argument("--min-pmi", type=float, default=0.4, help="Minimum PMI to keep edge")
ap.add_argument("--max-edges", type=int, default=70)
args = ap.parse_args()

if args.nodes:
    NODES = set(w.strip().lower() for w in args.nodes.split(","))
else:
    tfidf = json.loads((args.analysis_dir / "tfidf.json").read_text())
    NODES = set(e["term"] for e in tfidf[:40])

SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")
TOKEN = re.compile(r"[A-Za-z][A-Za-z'-]+")
def clean_body(text):
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    text = re.sub(r"<!--\s*artifact:[^:]+:start\s*-->.*?<!--\s*artifact:[^:]+:end\s*-->",
                  "", text, flags=re.DOTALL)
    return text

node_count = collections.Counter(); pair_count = collections.Counter()
n_sentences = 0
for f in sorted(args.corpus_dir.glob("*.md")):
    if f.name == "MANIFEST.md": continue
    body = clean_body(f.read_text(encoding="utf-8", errors="replace"))
    for sent in SENT.split(body):
        present = set(t.lower() for t in TOKEN.findall(sent)) & NODES
        if not present: continue
        n_sentences += 1
        for w in present: node_count[w] += 1
        plist = sorted(present)
        for i in range(len(plist)):
            for j in range(i+1, len(plist)):
                pair_count[(plist[i], plist[j])] += 1

edges = []
for (a, b), c in pair_count.items():
    if c < args.min_co: continue
    pa = node_count[a] / n_sentences; pb = node_count[b] / n_sentences
    pab = c / n_sentences
    if pa * pb == 0: continue
    pmi = math.log(pab / (pa * pb))
    if pmi < args.min_pmi: continue
    edges.append({"source": a, "target": b, "weight": c, "pmi": round(pmi, 3)})

edges.sort(key=lambda e: -e["pmi"] * math.log(e["weight"]))
edges = edges[:args.max_edges]

print(f"Sentences scanned: {n_sentences:,}")
print(f"Nodes:             {len(node_count)}")
print(f"Edges:             {len(edges)}")
print(f"\nTop 15 strongest links:")
for e in edges[:15]:
    print(f"  {e['source']:>14} -- {e['target']:<14}  co={e['weight']:>4}  PMI={e['pmi']:.2f}")

args.analysis_dir.mkdir(parents=True, exist_ok=True)
nodes_out = [{"id": w, "count": node_count[w]} for w in NODES if node_count[w] > 0]
(args.analysis_dir / "network.json").write_text(
    json.dumps({"nodes": nodes_out, "edges": edges}, indent=2))
print(f"\nSaved network.json")
