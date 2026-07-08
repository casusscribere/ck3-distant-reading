#!/usr/bin/env python3
"""render_network.py — force-directed concept network from network.json."""
import argparse, json, pathlib

ap = argparse.ArgumentParser()
ap.add_argument("--analysis-dir", type=pathlib.Path, default=pathlib.Path("analysis"))
ap.add_argument("--out", type=pathlib.Path, default=pathlib.Path("analysis/network.html"))
args = ap.parse_args()

data_js = (args.analysis_dir / "network.json").read_text()
html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>Concept Network</title>
<style>body{{font-family:Inter,system-ui,sans-serif;margin:24px}}#net{{width:680px;height:560px}}</style>
</head><body><h2>Concept co-occurrence network</h2><div id="net"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
<script>
const data={data_js};
const W=680,H=560;
const svg=d3.select("#net").append("svg").attr("viewBox",`0 0 ${{W}} ${{H}}`).attr("width","100%");
const r=d3.scaleSqrt().domain([d3.min(data.nodes,n=>n.count),d3.max(data.nodes,n=>n.count)]).range([6,26]);
const ew=d3.scaleLinear().domain([d3.min(data.edges,e=>e.pmi),d3.max(data.edges,e=>e.pmi)]).range([0.6,4]);
const sim=d3.forceSimulation(data.nodes)
  .force("link",d3.forceLink(data.edges).id(d=>d.id).distance(e=>100-e.pmi*25))
  .force("charge",d3.forceManyBody().strength(-220))
  .force("center",d3.forceCenter(W/2,H/2));
const link=svg.append("g").selectAll("line").data(data.edges).join("line")
  .attr("stroke","#999").attr("stroke-opacity",0.5).attr("stroke-width",e=>ew(e.pmi));
const node=svg.append("g").selectAll("g").data(data.nodes).join("g");
node.append("circle").attr("r",d=>r(d.count)).attr("fill","#534AB7").attr("stroke","#fff").attr("stroke-width",1.5);
node.append("text").text(d=>d.id).attr("font-size",12).attr("text-anchor","middle").attr("dy",d=>-r(d.count)-4);
sim.on("tick",()=>{{
  link.attr("x1",d=>d.source.x).attr("y1",d=>d.source.y).attr("x2",d=>d.target.x).attr("y2",d=>d.target.y);
  node.attr("transform",d=>`translate(${{d.x}},${{d.y}})`);
}});
</script></body></html>"""
args.out.parent.mkdir(parents=True, exist_ok=True)
args.out.write_text(html, encoding="utf-8")
print(f"Wrote {args.out}")
