#!/usr/bin/env python3
"""00e_extract_html_epub.py — Convert .html/.epub to plaintext markdown.

For .html: strip tags via regex (good enough for most cases; for cleaner
extraction the user can install python-readability).
For .epub: requires ebook-convert (Calibre); falls back to stub if unavailable.
"""
import argparse, hashlib, pathlib, re, subprocess, tempfile, datetime

ap = argparse.ArgumentParser()
ap.add_argument("path", type=pathlib.Path)
ap.add_argument("--out-dir", required=True, type=pathlib.Path)
args = ap.parse_args()

raw = args.path.read_bytes()
sha = hashlib.sha256(raw).hexdigest()
ext = args.path.suffix.lower()

if ext == ".epub":
    try:
        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as f:
            tmp = f.name
        subprocess.run(["ebook-convert", str(args.path), tmp],
                       capture_output=True, check=True)
        body = pathlib.Path(tmp).read_text(encoding="utf-8", errors="replace")
        pathlib.Path(tmp).unlink()
        method = "ebook_convert"
    except (FileNotFoundError, subprocess.CalledProcessError):
        body = ""
        method = "unrecoverable_no_ebook_convert"
else:
    text = raw.decode("utf-8", errors="replace")
    body = re.sub(r"<script[\s\S]*?</script>", "", text, flags=re.IGNORECASE)
    body = re.sub(r"<style[\s\S]*?</style>", "", body, flags=re.IGNORECASE)
    body = re.sub(r"<[^>]+>", " ", body)
    body = re.sub(r"&nbsp;", " ", body)
    body = re.sub(r"&amp;", "&", body)
    body = re.sub(r"&lt;", "<", body)
    body = re.sub(r"&gt;", ">", body)
    body = re.sub(r"&quot;", '"', body)
    body = re.sub(r"\s+\n", "\n", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    method = "html_strip_tags"

word_count = len(re.findall(r"\w+", body))
stem = args.path.stem.replace(" ", "-").lower()[:80]
out = args.out_dir / f"{stem}.md"
args.out_dir.mkdir(parents=True, exist_ok=True)
fm = f"""---
source_file: "{args.path.name}"
source_sha256: {sha}
extraction_method: {method}
extraction_date: {datetime.date.today()}
text_layer_present: {str(method != 'unrecoverable_no_ebook_convert').lower()}
ocr_used: false
body_word_count: {word_count}
language: en
detected_artifacts: []
notes_for_analyst: |
  {'HTML stripped via tag regex; for cleaner extraction install python-readability.' if ext != '.epub' else 'EPUB converted via Calibre ebook-convert.'}
---

{body}
"""
out.write_text(fm, encoding="utf-8")
print(f"OK: {out.name} ({word_count} words, {method})")
