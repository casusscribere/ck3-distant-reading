#!/usr/bin/env python3
"""render_wordcloud.py — generate SVG word cloud from bag_clean.json."""
import argparse, json, pathlib

ap = argparse.ArgumentParser()
ap.add_argument("--analysis-dir", type=pathlib.Path, default=pathlib.Path("analysis"))
ap.add_argument("--out", type=pathlib.Path, default=pathlib.Path("analysis/wordcloud.html"))
args = ap.parse_args()

bag = json.loads((args.analysis_dir / "bag_clean.json").read_text())[:60]
data_js = json.dumps([{"word": w, "count": c} for w, c in bag])

html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Word Cloud</title>
<style>body{{font-family:Inter,system-ui,sans-serif;margin:24px}}#wc{{width:680px;height:480px}}</style>
</head><body>
<h2>Top 60 content words</h2>
<div id="wc"></div>
<script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
<script src="https://cdn.jsdelivr.net/npm/d3-cloud@1.2.7/build/d3.layout.cloud.min.js"></script>
<script>
const data = {data_js};
const W=680,H=480,max=data[0].count,min=data[data.length-1].count;
const scale=d3.scaleSqrt().domain([min,max]).range([12,64]);
const layout=d3.layout.cloud().size([W,H])
  .words(data.map(d=>({{text:d.word,size:scale(d.count)}})))
  .padding(3).rotate(()=>Math.random()<0.3?90:0)
  .font("Inter, sans-serif").fontSize(d=>d.size).on("end",draw);
layout.start();
function draw(words){{
  d3.select("#wc").append("svg").attr("viewBox",`0 0 ${{W}} ${{H}}`).attr("width","100%")
    .append("g").attr("transform",`translate(${{W/2}},${{H/2}})`)
    .selectAll("text").data(words).join("text")
    .style("font-family","Inter, sans-serif").style("font-weight",500)
    .style("fill",(d,i)=>d3.schemeCategory10[i%10])
    .attr("text-anchor","middle").attr("font-size",d=>d.size+"px")
    .attr("transform",d=>`translate(${{d.x}},${{d.y}})rotate(${{d.rotate}})`)
    .text(d=>d.text);
}}
</script></body></html>
"""
args.out.parent.mkdir(parents=True, exist_ok=True)
args.out.write_text(html, encoding="utf-8")
print(f"Wrote {args.out}")
