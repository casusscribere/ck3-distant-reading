#!/usr/bin/env python3
"""00f_annotate_artifacts.py — wrap Salter-style extraneous content in HTML
comments without removing it.

Scans the body of each .md and injects <!-- artifact:TYPE:start --> /
<!-- artifact:TYPE:end --> markers around detected artifacts. The downstream
analysis can strip these comment blocks; a human reader still sees the source.

Detected artifact types from artifact-taxonomy.md:
  bare_page_number, running_header, jstor_cover_page, drm_footer,
  publisher_boilerplate, references_section.
"""
import argparse, pathlib, re

ap = argparse.ArgumentParser()
ap.add_argument("md", type=pathlib.Path)
args = ap.parse_args()

text = args.md.read_text(encoding="utf-8")
# Split frontmatter from body
m = re.match(r"^(---\n.*?\n---\n)(.*)$", text, re.DOTALL)
if not m:
    print(f"  skip: no front-matter in {args.md.name}"); raise SystemExit(0)
fm, body = m.group(1), m.group(2)

# JSTOR cover sheet — appears at top, has stable URL + accessed-date + REFERENCES line
jstor_re = re.search(r"^(Society for[^\n]+\n.*?REFERENCES\n.*?(?=\n\n))", body, re.DOTALL | re.MULTILINE)
if jstor_re:
    body = body.replace(jstor_re.group(1),
        f"<!-- artifact:jstor_cover_page:start -->\n{jstor_re.group(1)}\n<!-- artifact:jstor_cover_page:end -->")

# Bare page numbers — standalone lines of just 1-4 digits
body = re.sub(r"(?m)^(\s*\d{1,4}\s*)$",
              r"<!-- artifact:bare_page_number -->\1<!-- /artifact -->", body)

# Reference section heading — flag from heading to end if in last 40% of body
refs_re = re.compile(r"(?m)^\s*(References|Bibliography|Works Cited)\s*$")
matches = [m for m in refs_re.finditer(body) if m.start() >= len(body) * 0.6]
if matches:
    last = matches[-1]
    body = body[:last.start()] + \
           "<!-- artifact:references_section:start -->\n" + \
           body[last.start():] + \
           "\n<!-- artifact:references_section:end -->"

# DRM footer — Bloomsbury / ProQuest e-book per-page boilerplate
body = re.sub(r"(Copyright (Bloomsbury|Routledge|Palgrave)[^\n]*\n)",
              r"<!-- artifact:drm_footer -->\1<!-- /artifact -->\n", body)
body = re.sub(r"(ebookcentral\.proquest\.com[^\n]*\n)",
              r"<!-- artifact:drm_footer -->\1<!-- /artifact -->\n", body)

args.md.write_text(fm + body, encoding="utf-8")
print(f"  annotated: {args.md.name}")
