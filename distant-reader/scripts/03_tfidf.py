#!/usr/bin/env python3
"""03_tfidf.py — Steps 4+5 of Salter's methodology (themes/genre via TF-IDF).

Computes corpus-aggregated TF-IDF: for each term, (1 + log(tf)) * log(N/df).
Rewards terms that appear often within papers AND in many papers; penalizes
single-document outliers and universal function words.

Run AFTER 02_apply_stopwords.py to operate on the cleaned corpus.
"""
import argparse, collections, json, math, pathlib, re

ap = argparse.ArgumentParser()
ap.add_argument("corpus_dir", type=pathlib.Path)
ap.add_argument("--analysis-dir", type=pathlib.Path, default=pathlib.Path("analysis"))
ap.add_argument("--references-dir", type=pathlib.Path,
                default=pathlib.Path(__file__).parent.parent / "references")
ap.add_argument("--min-df", type=int, default=4)
ap.add_argument("--max-df-ratio", type=float, default=0.97)
ap.add_argument("--top", type=int, default=80)
args = ap.parse_args()

def load_stopwords(name):
    f = args.references_dir / f"stopwords-{name}.txt"
    if not f.exists(): return set()
    return set(w.strip().lower() for w in f.read_text().split() if w.strip())
ALL_STOP = load_stopwords("english") | load_stopwords("academic") | load_stopwords("artifacts")

TOKEN = re.compile(r"[A-Za-z][A-Za-z'-]+")
def clean_body(text):
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    text = re.sub(r"<!--\s*artifact:[^:]+:start\s*-->.*?<!--\s*artifact:[^:]+:end\s*-->",
                  "", text, flags=re.DOTALL)
    text = re.sub(r"<!--\s*artifact:[^>]+?\s*-->.*?<!--\s*/artifact\s*-->", "", text, flags=re.DOTALL)
    return text

doc_words = {}
for f in sorted(args.corpus_dir.glob("*.md")):
    if f.name == "MANIFEST.md": continue
    body = clean_body(f.read_text(encoding="utf-8", errors="replace")).lower()
    if not body.strip(): continue
    toks = [t for t in TOKEN.findall(body) if t not in ALL_STOP and len(t) >= 3]
    doc_words[f.stem] = collections.Counter(toks)

N = len(doc_words)
df = collections.Counter()
for d, c in doc_words.items():
    for w in c: df[w] += 1

agg = collections.Counter()
for d, c in doc_words.items():
    for w, tf in c.items():
        if df[w] < args.min_df or df[w] > N * args.max_df_ratio: continue
        idf = math.log(N / df[w])
        agg[w] += (1 + math.log(tf)) * idf

top = agg.most_common(args.top)
print(f"Top {args.top} terms by TF-IDF (min_df={args.min_df}):")
for i, (w, s) in enumerate(top, 1):
    print(f"  {i:>3}. {w:<22} score={s:>6.1f}  df={df[w]:>3}/{N}")

args.analysis_dir.mkdir(parents=True, exist_ok=True)
(args.analysis_dir / "tfidf.json").write_text(
    json.dumps([{"term": w, "score": s, "df": df[w]} for w, s in top], indent=2))
print(f"\nSaved tfidf.json")
