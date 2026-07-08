#!/usr/bin/env python3
"""02_apply_stopwords.py — Step 2 of Salter's methodology.

Applies three default passes of stopwords (English basic, academic discourse,
publisher/citation artifacts). Each pass surfaces the top 60 surviving terms.
Iterate further by editing the references/stopwords-*.txt files.
"""
import argparse, collections, json, pathlib, re

ap = argparse.ArgumentParser()
ap.add_argument("corpus_dir", type=pathlib.Path)
ap.add_argument("--analysis-dir", type=pathlib.Path, default=pathlib.Path("analysis"))
ap.add_argument("--references-dir", type=pathlib.Path,
                default=pathlib.Path(__file__).parent.parent / "references")
ap.add_argument("--include-artifacts", default="")
args = ap.parse_args()
args.analysis_dir.mkdir(parents=True, exist_ok=True)
include_set = set(args.include_artifacts.split(",")) if args.include_artifacts else set()

TOKEN = re.compile(r"[A-Za-z][A-Za-z'-]+")

def load_stopwords(name):
    f = args.references_dir / f"stopwords-{name}.txt"
    if not f.exists(): return set()
    return set(w.strip().lower() for w in f.read_text().split() if w.strip())

basic = load_stopwords("english")
academic = load_stopwords("academic")
artifacts = load_stopwords("artifacts")
ALL_STOP = basic | academic | artifacts
print(f"Stopwords loaded: {len(basic)} basic + {len(academic)} academic + {len(artifacts)} artifacts = {len(ALL_STOP)} total")

def clean_body(text):
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    def strip_or_keep(m):
        t = m.group(1)
        return m.group(0) if t in include_set else ""
    text = re.sub(r"<!--\s*artifact:([^:]+):start\s*-->.*?<!--\s*artifact:[^:]+:end\s*-->",
                  strip_or_keep, text, flags=re.DOTALL)
    text = re.sub(r"<!--\s*artifact:([^>]+?)\s*-->[^<]*?<!--\s*/artifact\s*-->",
                  strip_or_keep, text, flags=re.DOTALL)
    return text

counts = collections.Counter()
doc_freq = collections.Counter()
total = 0
for f in sorted(args.corpus_dir.glob("*.md")):
    if f.name == "MANIFEST.md": continue
    body = clean_body(f.read_text(encoding="utf-8", errors="replace")).lower()
    if not body.strip(): continue
    toks = [t for t in TOKEN.findall(body) if t not in ALL_STOP and len(t) >= 3]
    total += len(toks)
    counts.update(toks)
    for w in set(toks): doc_freq[w] += 1

print(f"\nAfter stopwording: {total:,} content tokens, {len(counts):,} unique")
print(f"\nTop 60 content words:")
top = counts.most_common(60)
for i, (w, c) in enumerate(top, 1):
    bar = "█" * int(c/top[0][1]*30)
    print(f"  {i:>3}  {w:<18}{c:>6,}  {doc_freq[w]:>3}docs  {bar}")

(args.analysis_dir / "bag_clean.json").write_text(json.dumps(counts.most_common(2000)))
(args.analysis_dir / "doc_freq_clean.json").write_text(json.dumps(dict(doc_freq.most_common(2000))))
print(f"\nSaved bag_clean.json and doc_freq_clean.json")
