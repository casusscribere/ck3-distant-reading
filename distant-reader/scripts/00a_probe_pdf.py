#!/usr/bin/env python3
"""00a_probe_pdf.py — Detect whether a PDF has a usable text layer.

Runs pdftotext on the first 2 pages, checks word count, Latin-character ratio,
and garbage indicators. Prints routing decision to stdout:
  text-layer-extraction | ocr-required | mixed
"""
import subprocess, sys, re, tempfile, pathlib

if len(sys.argv) < 2:
    print("usage: 00a_probe_pdf.py <pdf-path>", file=sys.stderr); sys.exit(1)
pdf = sys.argv[1]

with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as f:
    tmp = f.name
subprocess.run(["pdftotext", "-f", "1", "-l", "2", "-enc", "UTF-8", pdf, tmp],
               capture_output=True)
text = pathlib.Path(tmp).read_text(encoding="utf-8", errors="replace")
pathlib.Path(tmp).unlink()

words = re.findall(r"\w+", text)
n_words = len(words)
latin_chars = sum(1 for c in text if c.isalpha() and ord(c) < 128)
total_chars = sum(1 for c in text if c.isalpha()) or 1
ratio = latin_chars / total_chars

# Single-character-line clusters indicate OCR-style fragmentation
single_char_lines = sum(1 for line in text.splitlines() if len(line.strip()) == 1)

if n_words < 50:
    print("ocr-required")  # Empty text layer = image-only
elif ratio < 0.7 and n_words < 200:
    print("ocr-required")  # Garbage encoding
elif single_char_lines > 20:
    print("ocr-required")  # OCR-fragmented existing layer
else:
    print("text-layer-extraction")
