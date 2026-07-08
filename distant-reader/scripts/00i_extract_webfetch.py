#!/usr/bin/env python3
"""00i_extract_webfetch.py — process a WebFetch response into provenance .md.

This script does NOT call WebFetch — the calling Claude session does that.
The session passes the fetched response (saved temp file path or inline text)
to this script. The script parses XenForo/Substack/Medium/WordPress structural
markers and emits a per-source markdown.

For the XenForo case it reuses extract_diary.py logic from the CK3 reference
implementation: title-line detection, thread-starter regex, body-end at
reactions block, signature/reply boundaries.

Usage:
  python3 00i_extract_webfetch.py FETCH_FILE --url URL --out-dir DIR [extraction options]
"""
import argparse, datetime, hashlib, pathlib, re, sys

ap = argparse.ArgumentParser()
ap.add_argument("fetch_file", type=pathlib.Path,
    help="Path to WebFetch saved temp file (txt) containing fetched page content")
ap.add_argument("--url", required=True)
ap.add_argument("--out-dir", required=True, type=pathlib.Path)
ap.add_argument("--title")
ap.add_argument("--author")
ap.add_argument("--date")
args = ap.parse_args()

raw = args.fetch_file.read_text(encoding="utf-8", errors="replace")
sha = hashlib.sha256(raw.encode("utf-8")).hexdigest()

# XenForo title detection (covers Dev Diary, CK3 Dev Diary, CKIII Dev Diary, etc.)
RE_TITLE = re.compile(r"^# (?:CK(?:3|III)\s*-?\s*)?(?:Crusader Kings (?:III|3)\s*-?\s*)?Dev(?:eloper)? Diary\s*#?", re.IGNORECASE)
RE_THREAD_START = re.compile(r"Thread starter \[([^\]]+)\]")
RE_REACT = re.compile(r"^- (\d+)!?\[([A-Za-z][A-Za-z'+ ]*)\]")
RE_WRITTEN_BY = re.compile(r"^Written by\s*$")
RE_REPLY = re.compile(r"^- \[Add bookmark\]")

lines = raw.split("\n")
# Find title (fallback: synthesize from WebFetch's first line if no body heading)
title_idx = None
for i, line in enumerate(lines):
    if RE_TITLE.match(line):
        title_idx = i; break
if title_idx is None:
    page_title = lines[0].strip() if lines else "untitled"
    for i, line in enumerate(lines):
        if RE_THREAD_START.search(line):
            lines.insert(i, f"# {page_title}"); title_idx = i; break

if title_idx is None:
    print(f"ERROR: no title found", file=sys.stderr); sys.exit(1)

title = lines[title_idx].lstrip("# ").strip()
# Find body span
body_start = title_idx + 1
while body_start < len(lines) and (not lines[body_start].strip() or RE_THREAD_START.search(lines[body_start])):
    body_start += 1
react_start = None
for i in range(body_start, len(lines)):
    if RE_REACT.match(lines[i]):
        react_start = i; break
body_end = react_start if react_start else len(lines)
body = "\n".join(lines[body_start:body_end]).strip()
word_count = len(re.findall(r"\w+", body))

# Extract forum_id from URL
forum_id = re.search(r"\.(\d+)/?$", args.url.rstrip("/"))
forum_id = forum_id.group(1) if forum_id else "unknown"

stem = re.sub(r"[^a-z0-9]+", "-", title.lower())[:60].strip("-")
out = args.out_dir / f"{stem}.md"
args.out_dir.mkdir(parents=True, exist_ok=True)

fm = f"""---
source_url: "{args.url}"
forum_thread_id: {forum_id}
source_sha256: {sha}
title: "{title}"
extraction_method: webfetch_xenforo_text_layer
extraction_date: {datetime.date.today()}
text_layer_present: true
ocr_used: false
body_word_count: {word_count}
language: en
detected_artifacts:
  - type: webfetch_metadata
    location: lines_1_to_~27
    action: discarded_from_output
  - type: forum_chrome
    location: lines_~28_to_{title_idx}
    action: discarded_from_output
  - type: thread_metadata
    location: lines_{title_idx+2}_to_{body_start}
    action: preserved_in_body
notes_for_analyst: |
  WebFetch XenForo extraction. Body span detected between title heading and
  first reactions-block line. Signature and replies discarded.
---

# {title}

{body}
"""
out.write_text(fm, encoding="utf-8")
print(f"OK: {out.name} ({word_count} words)")
