#!/usr/bin/env python3
"""06_underwood_verify.py — Step 8 of Salter's methodology, made non-optional.

For each top claim (top-3 cleaned tokens, top-3 concept-network edges, top-3
trigrams), retrieve representative passages from the corpus. Surface the
passages alongside the claims so the analyst can check whether the corpus
actually supports the claim or merely names the term.

See references/underwood-critique.md for the methodology.
"""
import argparse, collections, json, pathlib, re

ap = argparse.ArgumentParser()
ap.add_argument("corpus_dir", type=pathlib.Path)
ap.add_argument("--analysis-dir", type=pathlib.Path, default=pathlib.Path("analysis"))
ap.add_argument("--passages-per-claim", type=int, default=4)
args = ap.parse_args()

# Load claims
bag = json.loads((args.analysis_dir / "bag_clean.json").read_text())
network = json.loads((args.analysis_dir / "network.json").read_text())
trigrams = json.loads((args.analysis_dir / "trigrams.json").read_text())

claims = []
for term, count in bag[:3]:
    claims.append({"type": "frequency", "term": term, "count": count,
                   "pattern": re.compile(rf"\b{re.escape(term)}\b", re.IGNORECASE)})
for edge in network["edges"][:3]:
    a, b = edge["source"], edge["target"]
    claims.append({"type": "co-occurrence", "term": f"{a} ↔ {b}", "pmi": edge["pmi"],
                   "pattern": re.compile(rf"\b{re.escape(a)}\b.*?\b{re.escape(b)}\b|\b{re.escape(b)}\b.*?\b{re.escape(a)}\b",
                                         re.IGNORECASE)})
for tg in trigrams[:3]:
    claims.append({"type": "trigram", "term": tg["phrase"], "count": tg["count"],
                   "pattern": re.compile(re.escape(tg["phrase"]), re.IGNORECASE)})

# Gather passages
verification = []
for claim in claims:
    passages = []
    for f in sorted(args.corpus_dir.glob("*.md")):
        if f.name == "MANIFEST.md": continue
        text = f.read_text(encoding="utf-8", errors="replace")
        text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
        for m in claim["pattern"].finditer(text):
            start = max(0, m.start() - 120)
            end = min(len(text), m.end() + 120)
            passage = text[start:end].replace("\n", " ")
            passages.append({"source": f.stem, "passage": "..." + passage + "..."})
            if len(passages) >= args.passages_per_claim: break
        if len(passages) >= args.passages_per_claim: break
    verification.append({
        "claim_type": claim["type"], "claim_term": claim["term"],
        "passages_found": len(passages),
        "passages": passages,
    })

print(f"Verifying {len(claims)} claims against {len(list(args.corpus_dir.glob('*.md')))} corpus files:\n")
for v in verification:
    print(f"CLAIM: {v['claim_type']} — {v['claim_term']!r}")
    print(f"  Passages found: {v['passages_found']}")
    for p in v["passages"][:2]:
        print(f"  · [{p['source']}] {p['passage'][:200]}")
    print()

args.analysis_dir.mkdir(parents=True, exist_ok=True)
(args.analysis_dir / "verification.json").write_text(json.dumps(verification, indent=2))
print(f"Saved verification.json — use these passages to ground or contest each claim.")
