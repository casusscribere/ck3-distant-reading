#!/usr/bin/env python3
"""01_bag_of_words.py — Step 1 of Salter's methodology.

Reads every .md in corpus_md/, strips YAML front-matter and artifact-flagged
comment blocks, tokenizes, computes corpus-wide frequency distribution.
Outputs bag_raw.json (top 5000 terms with frequencies and document-frequencies).

Print the top 40 raw tokens so the reader can see function-word dominance,
which motivates Step 2's stopword application.
"""
import argparse, collections, json, pathlib, re

ap = argparse.ArgumentParser()
ap.add_argument("corpus_dir", type=pathlib.Path)
ap.add_argument("--out-dir", type=pathlib.Path, default=pathlib.Path("analysis"))
ap.add_argument("--include-artifacts", default="",
                help="Comma-separated artifact types to INCLUDE rather than strip (e.g., references_section)")
args = ap.parse_args()
args.out_dir.mkdir(parents=True, exist_ok=True)
include_set = set(args.include_artifacts.split(",")) if args.include_artifacts else set()

TOKEN = re.compile(r"[A-Za-z][A-Za-z'-]+")

def clean_body(text, include_artifacts):
    """Strip front-matter and artifact-flagged blocks."""
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    # Strip artifact blocks NOT in include_artifacts
    def strip_or_keep(m):
        t = m.group(1)
        return m.group(0) if t in include_artifacts else ""
    text = re.sub(r"<!--\s*artifact:([^:]+):start\s*-->.*?<!--\s*artifact:[^:]+:end\s*-->",
                  strip_or_keep, text, flags=re.DOTALL)
    text = re.sub(r"<!--\s*artifact:([^>]+?)\s*-->[^<]*?<!--\s*/artifact\s*-->",
                  strip_or_keep, text, flags=re.DOTALL)
    return text

counts = collections.Counter()
doc_freq = collections.Counter()
total_tokens = 0; n_docs = 0; skipped_artifacts = collections.Counter()

for f in sorted(args.corpus_dir.glob("*.md")):
    if f.name == "MANIFEST.md": continue
    text = f.read_text(encoding="utf-8", errors="replace")
    # Log artifact types present
    for at in re.findall(r"<!--\s*artifact:([^:>]+)", text):
        if at not in include_set:
            skipped_artifacts[at] += 1
    body = clean_body(text, include_set).lower()
    if not body.strip(): continue
    n_docs += 1
    toks = TOKEN.findall(body)
    total_tokens += len(toks)
    counts.update(toks)
    for w in set(toks): doc_freq[w] += 1

print(f"Documents:         {n_docs}")
print(f"Total tokens:      {total_tokens:,}")
print(f"Unique types:      {len(counts):,}")
print(f"Artifacts skipped: {dict(skipped_artifacts)}")
print(f"\nTop 40 raw (no stopwords yet):")
print(f"{'rank':>4}  {'token':<15}{'count':>8}  {'docs':>6}")
for i, (w, c) in enumerate(counts.most_common(40), 1):
    print(f"{i:>4}  {w:<15}{c:>8,}  {doc_freq[w]:>6}")

(args.out_dir / "bag_raw.json").write_text(json.dumps(counts.most_common(5000)))
(args.out_dir / "doc_freq.json").write_text(json.dumps(dict(doc_freq.most_common(5000))))
print(f"\nSaved bag_raw.json and doc_freq.json to {args.out_dir}")
