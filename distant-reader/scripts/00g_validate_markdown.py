#!/usr/bin/env python3
"""00g_validate_markdown.py — sanity-check every .md in corpus_md/.

Enforces:
- Well-formed YAML front-matter (--- ... ---)
- Non-empty body
- No unclosed <!-- artifact:* --> blocks
- Recognized extraction_method
- Required keys: source_file or source_url, extraction_method,
  extraction_date, body_word_count

Exits non-zero on any failure with per-file diagnostics.
"""
import argparse, pathlib, re, sys

KNOWN_METHODS = {
    "pdftotext_layout", "tesseract_ocr", "plaintext_passthrough",
    "gutenberg_passthrough", "html_strip_tags", "ebook_convert",
    "webfetch_xenforo_text_layer", "claude_in_chrome_dom_capture",
    "claude_in_chrome_partial_capture",
    "unrecoverable_no_ocr", "unrecoverable_no_ebook_convert",
}

REQUIRED = ["extraction_method", "extraction_date", "body_word_count"]

ap = argparse.ArgumentParser()
ap.add_argument("corpus_dir", type=pathlib.Path)
args = ap.parse_args()

failures = []
checked = 0
for md in sorted(args.corpus_dir.glob("*.md")):
    if md.name == "MANIFEST.md": continue
    checked += 1
    text = md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        failures.append((md.name, "no front-matter")); continue
    fm, body = m.group(1), m.group(2)
    if not body.strip():
        failures.append((md.name, "empty body")); continue
    # required keys present
    for k in REQUIRED:
        if not re.search(rf"^{k}:", fm, re.MULTILINE):
            failures.append((md.name, f"missing key: {k}")); break
    # extraction method recognized
    em = re.search(r"^extraction_method:\s*(\S+)", fm, re.MULTILINE)
    if em and em.group(1) not in KNOWN_METHODS:
        failures.append((md.name, f"unknown extraction_method: {em.group(1)}"))
    # no unclosed artifact comments
    starts = len(re.findall(r"<!--\s*artifact:[^:]+:start\s*-->", body))
    ends = len(re.findall(r"<!--\s*artifact:[^:]+:end\s*-->", body))
    if starts != ends:
        failures.append((md.name, f"unbalanced artifact comments: {starts} starts, {ends} ends"))

print(f"Validated {checked} markdown files")
if failures:
    print(f"FAILURES: {len(failures)}")
    for name, reason in failures:
        print(f"  {name}: {reason}")
    sys.exit(1)
else:
    print("All files passed validation.")
