#!/usr/bin/env python3
"""00b_extract_pdftotext.py — Extract a text-layer PDF to provenance-tagged .md.

Uses pdftotext -layout, then writes a .md with full YAML front-matter recording
the extraction method, command, page count, word count, and detected artifacts.
"""
import argparse, hashlib, pathlib, re, subprocess, datetime

ap = argparse.ArgumentParser()
ap.add_argument("pdf", type=pathlib.Path)
ap.add_argument("--out-dir", required=True, type=pathlib.Path)
args = ap.parse_args()

# Compute SHA-256
sha = hashlib.sha256(args.pdf.read_bytes()).hexdigest()

# Get page count via pdfinfo
try:
    info = subprocess.check_output(["pdfinfo", str(args.pdf)], text=True)
    m = re.search(r"^Pages:\s*(\d+)$", info, re.MULTILINE)
    pages = int(m.group(1)) if m else 0
except Exception:
    pages = 0

# Extract
result = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8",
                        str(args.pdf), "-"], capture_output=True, text=True)
body = result.stdout

# Normalize ligatures and smart quotes
LIGATURES = {"ﬁ":"fi","ﬂ":"fl","ﬀ":"ff","ﬃ":"ffi","ﬄ":"ffl",
             """:'"',""":'"',"'":"'","'":"'","–":"-","—":"-","…":"..."}
for k, v in LIGATURES.items(): body = body.replace(k, v)

# De-hyphenate line breaks
body = re.sub(r"(\w+)-\n(\w+)", r"\1\2", body)

word_count = len(re.findall(r"\w+", body))
stem = args.pdf.stem.replace(" ", "-").lower()[:80]
out = args.out_dir / f"{stem}.md"
args.out_dir.mkdir(parents=True, exist_ok=True)

frontmatter = f"""---
source_file: "{args.pdf.name}"
source_sha256: {sha}
extraction_method: pdftotext_layout
extraction_command: "pdftotext -layout -enc UTF-8 INPUT -"
extraction_date: {datetime.date.today()}
text_layer_present: true
ocr_used: false
page_count: {pages}
body_word_count: {word_count}
language: en
detected_artifacts: []
notes_for_analyst: |
  Clean text-layer extraction via pdftotext. Run 00f_annotate_artifacts.py
  on this file to detect and flag page numbers, running headers, JSTOR
  cover sheets, DRM footers, and reference sections.
---

{body}
"""
out.write_text(frontmatter, encoding="utf-8")
print(f"OK: {out.name} ({word_count} words)")
