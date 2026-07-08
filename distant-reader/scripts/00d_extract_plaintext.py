#!/usr/bin/env python3
"""00d_extract_plaintext.py — Pass through .txt/.md with annotation.

Detects Project Gutenberg header/footer markers; preserves them in the body
and flags them in detected_artifacts.
"""
import argparse, hashlib, pathlib, re, datetime

ap = argparse.ArgumentParser()
ap.add_argument("path", type=pathlib.Path)
ap.add_argument("--out-dir", required=True, type=pathlib.Path)
args = ap.parse_args()

body = args.path.read_text(encoding="utf-8", errors="replace")
sha = hashlib.sha256(body.encode("utf-8")).hexdigest()

# Detect Gutenberg
artifacts = []
g_start = re.search(r"\*\*\* START OF (THE|THIS) PROJECT GUTENBERG", body)
g_end = re.search(r"\*\*\* END OF (THE|THIS) PROJECT GUTENBERG", body)
is_gutenberg = bool(g_start and g_end)
if is_gutenberg:
    artifacts.append({"type": "gutenberg_header",
                      "location": f"lines 1-{body[:g_start.end()].count(chr(10))+1}",
                      "action": "preserved_and_flagged"})
    artifacts.append({"type": "gutenberg_footer",
                      "location": f"lines {body[:g_end.start()].count(chr(10))+1}-end",
                      "action": "preserved_and_flagged"})

word_count = len(re.findall(r"\w+", body))
stem = args.path.stem.replace(" ", "-").lower()[:80]
out = args.out_dir / f"{stem}.md"
args.out_dir.mkdir(parents=True, exist_ok=True)
method = "gutenberg_passthrough" if is_gutenberg else "plaintext_passthrough"
fm = f"""---
source_file: "{args.path.name}"
source_sha256: {sha}
extraction_method: {method}
extraction_date: {datetime.date.today()}
text_layer_present: true
ocr_used: false
body_word_count: {word_count}
language: en
detected_artifacts: {artifacts}
notes_for_analyst: |
  {'Gutenberg .txt — header and footer boilerplate flagged but preserved.' if is_gutenberg else 'Direct plaintext passthrough; no normalization applied.'}
---

{body}
"""
out.write_text(fm, encoding="utf-8")
print(f"OK: {out.name} ({word_count} words, {'Gutenberg' if is_gutenberg else 'plain'})")
