#!/usr/bin/env python3
"""05_phrases.py — Step 7 of Salter's methodology (bigrams + trigrams).

Filters phrases by document frequency >= 5 and a DRM-token blocklist so that
per-page publisher boilerplate doesn't dominate the top trigrams (the
Bloomsbury / ProQuest gotcha from the Week 3 run).
"""
import argparse, collections, json, pathlib, re

ap = argparse.ArgumentParser()
ap.add_argument("corpus_dir", type=pathlib.Path)
ap.add_argument("--analysis-dir", type=pathlib.Path, default=pathlib.Path("analysis"))
ap.add_argument("--references-dir", type=pathlib.Path,
                default=pathlib.Path(__file__).parent.parent / "references")
ap.add_argument("--min-df", type=int, default=5)
args = ap.parse_args()

DRM_TOKENS = {"bloomsbury","proquest","ebookcentral","ucf","docid","copyright",
              "reserved","http","www","com","lib","ebook","central","academic",
              "professional","accessed","retrieved","jstor"}

TOKEN = re.compile(r"[A-Za-z][A-Za-z'-]+")
def clean_body(text):
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    text = re.sub(r"<!--\s*artifact:[^:]+:start\s*-->.*?<!--\s*artifact:[^:]+:end\s*-->",
                  "", text, flags=re.DOTALL)
    return text

def load_stopwords(name):
    f = args.references_dir / f"stopwords-{name}.txt"
    if not f.exists(): return set()
    return set(w.strip().lower() for w in f.read_text().split() if w.strip())
ALL_STOP = load_stopwords("english") | load_stopwords("academic") | load_stopwords("artifacts")

def is_stop(w): return w in ALL_STOP or len(w) < 3

bi_total = collections.Counter(); bi_docs = collections.Counter()
tri_total = collections.Counter(); tri_docs = collections.Counter()
for f in sorted(args.corpus_dir.glob("*.md")):
    if f.name == "MANIFEST.md": continue
    body = clean_body(f.read_text(encoding="utf-8", errors="replace")).lower()
    toks = TOKEN.findall(body)
    doc_bi = set(); doc_tri = set()
    for i in range(len(toks)-1):
        a, b = toks[i], toks[i+1]
        if is_stop(a) and is_stop(b): continue
        bg = f"{a} {b}"; bi_total[bg] += 1; doc_bi.add(bg)
    for i in range(len(toks)-2):
        a, b, c = toks[i], toks[i+1], toks[i+2]
        if sum(1 for x in (a,b,c) if not is_stop(x)) < 2: continue
        tg = f"{a} {b} {c}"; tri_total[tg] += 1; doc_tri.add(tg)
    for b in doc_bi: bi_docs[b] += 1
    for t in doc_tri: tri_docs[t] += 1

def has_drm(p): return any(t in DRM_TOKENS for t in p.split())

bi = [(p,c) for p,c in bi_total.items() if bi_docs[p] >= args.min_df and not has_drm(p)]
tri = [(p,c) for p,c in tri_total.items() if tri_docs[p] >= args.min_df and not has_drm(p)]
bi.sort(key=lambda x: -x[1]); tri.sort(key=lambda x: -x[1])

print(f"Top 25 bigrams (df>={args.min_df}, DRM filtered):")
for i, (p, c) in enumerate(bi[:25], 1):
    print(f"  {i:>2}. {p:<35} {c:>5}  df={bi_docs[p]:>2}")
print(f"\nTop 25 trigrams:")
for i, (p, c) in enumerate(tri[:25], 1):
    print(f"  {i:>2}. {p:<45} {c:>5}  df={tri_docs[p]:>2}")

args.analysis_dir.mkdir(parents=True, exist_ok=True)
(args.analysis_dir / "bigrams.json").write_text(
    json.dumps([{"phrase":p,"count":c,"df":bi_docs[p]} for p,c in bi[:50]], indent=2))
(args.analysis_dir / "trigrams.json").write_text(
    json.dumps([{"phrase":p,"count":c,"df":tri_docs[p]} for p,c in tri[:50]], indent=2))
print(f"\nSaved bigrams.json, trigrams.json")
