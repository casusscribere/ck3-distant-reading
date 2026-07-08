#!/usr/bin/env python3
"""compare_corpora.py — comparative distant reading of two corpora.

Built for the dev-diary (developer voice) vs reply-thread (community voice)
comparison, but works on any two folders of provenance-tagged Markdown that
follow the corpus convention (YAML front-matter + <!-- artifact:* --> spans).

It strips front-matter and every artifact span (exactly as the distant-reader
Step 1 does), tokenizes, then computes KEYNESS with Dunning's log-likelihood
(G2): which words are statistically over-represented in corpus A vs corpus B
and vice-versa. This is the standard corpus-linguistics measure for "what does
this group talk about that the other doesn't."

USAGE
  python3 compare_corpora.py \
      --a ./ck3_reply_threads      --a-label "Community replies"  --a-glob 'rt_*.md' \
      --b ./ck3_dev_diaries        --b-label "Developer diaries"  --b-glob 'dd_*.md' \
      --min-count 5 --top 30 --out keyness.json
"""
import argparse, glob, json, math, os, re
from collections import Counter

FM_RE  = re.compile(r'^---\s*\n.*?\n---\s*\n', re.DOTALL)
ART_RE = re.compile(r'<!--\s*artifact:[a-z_]+:start\s*-->.*?<!--\s*artifact:[a-z_]+:end\s*-->', re.DOTALL)
CMT_RE = re.compile(r'<!--.*?-->', re.DOTALL)
IMG_RE = re.compile(r'!\[[^\]]*\]\([^)]*\)')
LNK_RE = re.compile(r'\[([^\]]*)\]\([^)]*\)')
TOK_RE = re.compile(r"[a-z][a-z'\-]+[a-z]")

def load(folder, pattern):
    tf = Counter(); ndoc = 0
    for path in sorted(glob.glob(os.path.join(folder, pattern))):
        if os.path.basename(path) == "MANIFEST.md": continue
        t = open(path, encoding="utf-8", errors="replace").read()
        t = FM_RE.sub('', t)
        t = ART_RE.sub(' ', t)
        t = CMT_RE.sub(' ', t)
        # Structural scaffolding present in one corpus but not the other would
        # otherwise masquerade as distinctive vocabulary. Drop ATX headings
        # (DD '# Title', reply '## Reply N — Author · date · post-id') and the
        # reply-corpus summary line so only authored body text is compared.
        t = re.sub(r'(?m)^#{1,6}\s.*$', ' ', t)
        t = re.sub(r'(?m)^\*\s*\d+\s+repl[^\n]*\*\s*$', ' ', t)
        t = IMG_RE.sub(' ', t)
        t = LNK_RE.sub(r'\1', t)
        t = re.sub(r'https?://\S+', ' ', t)
        tf.update(TOK_RE.findall(t.lower()))
        ndoc += 1
    return tf, ndoc

def g2(a, b, ta, tb):
    """Dunning log-likelihood for one term. a,b = counts; ta,tb = corpus totals."""
    if a == 0 and b == 0: return 0.0, 0.0
    Ea = ta * (a + b) / (ta + tb)
    Eb = tb * (a + b) / (ta + tb)
    ll = 0.0
    if a > 0: ll += a * math.log(a / Ea)
    if b > 0: ll += b * math.log(b / Eb)
    ll *= 2
    # relative frequency ratio (per-10k), sign: + => over-rep in A
    ra = 1e4 * a / ta; rb = 1e4 * b / tb
    return ll, (ra - rb)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True); ap.add_argument("--a-glob", default="rt_*.md")
    ap.add_argument("--a-label", default="Corpus A")
    ap.add_argument("--b", required=True); ap.add_argument("--b-glob", default="dd_*.md")
    ap.add_argument("--b-label", default="Corpus B")
    ap.add_argument("--min-count", type=int, default=5)
    ap.add_argument("--top", type=int, default=30)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    A, nA = load(args.a, args.a_glob)
    B, nB = load(args.b, args.b_glob)
    tA, tB = sum(A.values()), sum(B.values())
    vocab = set(A) | set(B)
    rows = []
    for w in vocab:
        a, b = A.get(w, 0), B.get(w, 0)
        if a + b < args.min_count: continue
        ll, diff = g2(a, b, tA, tB)
        rows.append({"term": w, "a": a, "b": b,
                     "per10k_a": round(1e4*a/tA, 2), "per10k_b": round(1e4*b/tB, 2),
                     "g2": round(ll, 2), "over": args.a_label if diff > 0 else args.b_label})
    a_key = sorted([r for r in rows if r["over"] == args.a_label], key=lambda r: -r["g2"])[:args.top]
    b_key = sorted([r for r in rows if r["over"] == args.b_label], key=lambda r: -r["g2"])[:args.top]

    print(f"{args.a_label}: {nA} docs, {tA:,} tokens, {len(A):,} types")
    print(f"{args.b_label}: {nB} docs, {tB:,} tokens, {len(B):,} types")
    print(f"\n=== Over-represented in {args.a_label.upper()} (community voice) ===")
    print(f"{'term':<16}{'A/10k':>8}{'B/10k':>8}{'G2':>9}")
    for r in a_key: print(f"{r['term']:<16}{r['per10k_a']:>8}{r['per10k_b']:>8}{r['g2']:>9}")
    print(f"\n=== Over-represented in {args.b_label.upper()} (developer voice) ===")
    print(f"{'term':<16}{'A/10k':>8}{'B/10k':>8}{'G2':>9}")
    for r in b_key: print(f"{r['term']:<16}{r['per10k_a']:>8}{r['per10k_b']:>8}{r['g2']:>9}")

    if args.out:
        json.dump({"a_label": args.a_label, "b_label": args.b_label,
                   "a_docs": nA, "b_docs": nB, "a_tokens": tA, "b_tokens": tB,
                   "over_a": a_key, "over_b": b_key}, open(args.out, "w"), indent=1)
        print(f"\nWrote {args.out}")

if __name__ == "__main__":
    main()
