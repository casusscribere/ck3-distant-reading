#!/usr/bin/env python3
"""render_phrases.py — Chart.js horizontal-bar chart of top bigrams and trigrams."""
import argparse, json, pathlib

ap = argparse.ArgumentParser()
ap.add_argument("--analysis-dir", type=pathlib.Path, default=pathlib.Path("analysis"))
ap.add_argument("--out", type=pathlib.Path, default=pathlib.Path("analysis/phrases.html"))
args = ap.parse_args()

bi = json.loads((args.analysis_dir / "bigrams.json").read_text())[:18]
tri = json.loads((args.analysis_dir / "trigrams.json").read_text())[:15]
html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>Frequent Phrases</title>
<style>body{{font-family:Inter,system-ui,sans-serif;margin:24px}}.chart{{width:100%;height:480px;position:relative}}</style>
</head><body>
<h2>Most frequent bigrams</h2>
<div class="chart"><canvas id="bi"></canvas></div>
<h2>Most frequent trigrams</h2>
<div class="chart"><canvas id="tri"></canvas></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<script>
const bi={json.dumps(bi)}, tri={json.dumps(tri)};
function chart(id,data){{
  new Chart(document.getElementById(id),{{type:"bar",data:{{labels:data.map(d=>d.phrase),
    datasets:[{{label:"count",data:data.map(d=>d.count),backgroundColor:"#534AB7",borderRadius:3}}]}},
    options:{{indexAxis:"y",responsive:true,maintainAspectRatio:false,plugins:{{legend:{{display:false}}}}}}}});
}}
chart("bi",bi); chart("tri",tri);
</script></body></html>"""
args.out.parent.mkdir(parents=True, exist_ok=True)
args.out.write_text(html, encoding="utf-8")
print(f"Wrote {args.out}")
