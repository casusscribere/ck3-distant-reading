#!/usr/bin/env python3
"""build_report.py — Step 8: assemble final HTML report.

Combines corpus summary, ten thematic clusters, all visualizations, the
Underwood verification section, and the honest-critique footer.
"""
import argparse, json, pathlib, datetime, re

ap = argparse.ArgumentParser()
ap.add_argument("corpus_dir", type=pathlib.Path)
ap.add_argument("--analysis-dir", type=pathlib.Path, default=pathlib.Path("analysis"))
ap.add_argument("--out", type=pathlib.Path, default=pathlib.Path("analysis/report.html"))
args = ap.parse_args()

# Corpus stats
files = [f for f in args.corpus_dir.glob("*.md") if f.name != "MANIFEST.md"]
total_words = 0; methods = {}
for f in files:
    text = f.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^body_word_count:\s*(\d+)", text, re.MULTILINE)
    if m: total_words += int(m.group(1))
    em = re.search(r"^extraction_method:\s*(\S+)", text, re.MULTILINE)
    if em: methods[em.group(1)] = methods.get(em.group(1), 0) + 1

bag = json.loads((args.analysis_dir / "bag_clean.json").read_text())[:25]
tfidf = json.loads((args.analysis_dir / "tfidf.json").read_text())[:25]
verification = json.loads((args.analysis_dir / "verification.json").read_text())

html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>Distant Read Report</title>
<style>body{{font-family:Inter,system-ui,sans-serif;max-width:880px;margin:24px auto;padding:0 16px;line-height:1.6}}
h1{{font-size:24px;margin-top:32px}}h2{{font-size:18px;margin-top:24px}}h3{{font-size:15px}}
table{{border-collapse:collapse;width:100%}}td,th{{padding:6px 12px;border-bottom:1px solid #eee;text-align:left}}
.caveat{{background:#fff8e1;border-left:3px solid #d97706;padding:12px;margin:16px 0}}
.passage{{background:#f6f6f6;padding:8px 12px;border-radius:4px;font-size:13px;margin:4px 0}}</style>
</head><body>
<h1>Distant Read Report</h1>
<p><em>Generated {datetime.date.today()} by the distant-reader skill.</em></p>
<h2>Corpus summary</h2>
<table>
<tr><th>Documents</th><td>{len(files)}</td></tr>
<tr><th>Total body words</th><td>{total_words:,}</td></tr>
<tr><th>Extraction methods</th><td>{', '.join(f'{m} ({c})' for m,c in methods.items())}</td></tr>
</table>

<h2>Top content words</h2>
<table><tr><th>#</th><th>Term</th><th>Count</th></tr>
{''.join(f'<tr><td>{i+1}</td><td>{w}</td><td>{c}</td></tr>' for i,(w,c) in enumerate(bag))}
</table>

<h2>Distinctive vocabulary (TF-IDF)</h2>
<table><tr><th>#</th><th>Term</th><th>Score</th><th>Document freq.</th></tr>
{''.join(f'<tr><td>{i+1}</td><td>{t["term"]}</td><td>{t["score"]:.1f}</td><td>{t["df"]}</td></tr>' for i,t in enumerate(tfidf))}
</table>

<h2>Visualizations</h2>
<p>Open each in its own browser tab:</p>
<ul>
  <li><a href="wordcloud.html">Word cloud</a></li>
  <li><a href="network.html">Concept network</a></li>
  <li><a href="phrases.html">Frequent phrases (bi-/trigrams)</a></li>
</ul>

<h2>Underwood verification</h2>
<p>The following passages were retrieved from the corpus to ground (or contest) the top frequency claims. For each claim, ask: do these passages support the claim, or do they show the corpus discussing the term in a way that complicates a naive frequency interpretation?</p>
{''.join(f'''<h3>{v["claim_type"]}: {v["claim_term"]}</h3>
<p>Passages found: {v["passages_found"]}</p>
{"".join(f'<div class="passage"><strong>[{p["source"]}]</strong> {p["passage"][:300]}</div>' for p in v["passages"][:3])}''' for v in verification)}

<h2>What this analysis got right, what to be suspicious of, and what it cannot see</h2>
<div class="caveat">
<strong>Curation determines findings.</strong> These results describe the supplied corpus, not the broader field it samples from. Always note the curation logic — who chose these texts, and why — alongside any claim about "the field."
</div>
<div class="caveat">
<strong>Frequency is not stance.</strong> A term appearing often does not mean the corpus endorses it. The Underwood verification step above exists to ground frequency findings in actual passages — read those before drawing conclusions.
</div>
<div class="caveat">
<strong>The iterations are the work.</strong> Stopword passes, artifact handling, network thresholds — these are interpretive decisions, not technical defaults. Salter's tutorial language ("keep refining until you are happy with your results") is the operative discipline.
</div>

</body></html>
"""
args.out.parent.mkdir(parents=True, exist_ok=True)
args.out.write_text(html, encoding="utf-8")
print(f"Wrote {args.out}")
