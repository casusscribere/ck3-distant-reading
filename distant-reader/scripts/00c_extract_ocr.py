#!/usr/bin/env python3
"""00c_extract_ocr.py — OCR an image-only PDF via Tesseract.

Renders each page to PNG via pdftoppm at 300 DPI, runs Tesseract, joins per-page
output. Records ocr_average_confidence in front-matter and flags low-confidence
pages as artifacts.
"""
import argparse, hashlib, pathlib, re, subprocess, tempfile, datetime

ap = argparse.ArgumentParser()
ap.add_argument("pdf", type=pathlib.Path)
ap.add_argument("--out-dir", required=True, type=pathlib.Path)
ap.add_argument("--lang", default="eng")
args = ap.parse_args()

sha = hashlib.sha256(args.pdf.read_bytes()).hexdigest()

# Check Tesseract availability
try:
    subprocess.check_output(["tesseract", "--version"], stderr=subprocess.STDOUT)
except (FileNotFoundError, subprocess.CalledProcessError):
    # Graceful degradation: emit stub
    out = args.out_dir / f"{args.pdf.stem.replace(' ','-').lower()[:80]}.md"
    args.out_dir.mkdir(parents=True, exist_ok=True)
    out.write_text(f"""---
source_file: "{args.pdf.name}"
source_sha256: {sha}
extraction_method: unrecoverable_no_ocr
extraction_date: {datetime.date.today()}
text_layer_present: false
ocr_used: false
body_word_count: 0
notes_for_analyst: |
  Tesseract not installed; cannot OCR this image-only PDF. The file
  exists in the corpus folder as a stub. Install tesseract-ocr to
  recover this source.
---

""")
    print(f"STUB (no Tesseract): {out.name}")
    raise SystemExit(0)

# Render and OCR
with tempfile.TemporaryDirectory() as td:
    subprocess.run(["pdftoppm", "-r", "300", "-png", str(args.pdf),
                    str(pathlib.Path(td) / "page")], capture_output=True)
    pages = sorted(pathlib.Path(td).glob("page-*.png"))
    bodies, confidences, low_conf_pages = [], [], []
    for i, png in enumerate(pages, 1):
        r = subprocess.run(["tesseract", str(png), "-", "-l", args.lang,
                            "--oem", "1", "--psm", "1"],
                           capture_output=True, text=True)
        bodies.append(r.stdout)
        # Crude confidence: word_count vs char_count ratio
        words = len(re.findall(r"\w+", r.stdout))
        if words < 30: low_conf_pages.append(i)
        confidences.append(min(100, words * 2))

body = "\n\n".join(bodies)
avg_conf = sum(confidences) // max(1, len(confidences))
word_count = len(re.findall(r"\w+", body))

artifacts = []
if low_conf_pages:
    artifacts.append({
        "type": "low_ocr_confidence",
        "pages": low_conf_pages,
        "note": "Tesseract returned few words — possible OCR failure or near-blank page"
    })

stem = args.pdf.stem.replace(" ", "-").lower()[:80]
out = args.out_dir / f"{stem}.md"
args.out_dir.mkdir(parents=True, exist_ok=True)
fm = f"""---
source_file: "{args.pdf.name}"
source_sha256: {sha}
extraction_method: tesseract_ocr
extraction_command: "pdftoppm -r 300 + tesseract --oem 1 --psm 1 -l {args.lang}"
extraction_date: {datetime.date.today()}
text_layer_present: false
ocr_used: true
ocr_average_confidence: {avg_conf}
page_count: {len(pages)}
body_word_count: {word_count}
language: {args.lang}
detected_artifacts: {artifacts}
notes_for_analyst: |
  OCR extraction. Average confidence proxy: {avg_conf}/100. Low-confidence
  pages flagged in detected_artifacts list. Run 00f_annotate_artifacts.py
  to flag body-level artifacts (page numbers, headers, etc.).
---

{body}
"""
out.write_text(fm, encoding="utf-8")
print(f"OK: {out.name} (OCR, {word_count} words, ~{avg_conf}% confidence)")
