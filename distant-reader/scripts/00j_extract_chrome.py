#!/usr/bin/env python3
"""00j_extract_chrome.py — process a Claude in Chrome capture into .md.

This script does NOT call Chrome MCP — the calling Claude session does that
(navigate + wait + javascript_tool to scope the capture). The session passes
the captured DOM-text body to this script.

The script synthesizes XenForo-style structural markers (# title, Thread
starter, Start date, Written by, ### [author]) around the captured body so
that downstream extractors can locate the boundaries. It then writes a .md
with extraction_method set to claude_in_chrome_dom_capture (or
claude_in_chrome_partial_capture if --partial flag is given).

Usage:
  python3 00j_extract_chrome.py CAPTURE_FILE --url URL --out-dir DIR
      --title TITLE --author AUTHOR [--date DATE] [--partial]
"""
import argparse, datetime, hashlib, pathlib, re

ap = argparse.ArgumentParser()
ap.add_argument("capture_file", type=pathlib.Path)
ap.add_argument("--url", required=True)
ap.add_argument("--out-dir", required=True, type=pathlib.Path)
ap.add_argument("--title", required=True)
ap.add_argument("--author", default="unknown")
ap.add_argument("--date")
ap.add_argument("--full-body-bytes", type=int, default=None,
                help="If known, the byte size of the full underlying body — for partial-capture front-matter")
ap.add_argument("--partial", action="store_true")
args = ap.parse_args()

body = args.capture_file.read_text(encoding="utf-8", errors="replace")
# Strip preamble if present
m = re.search(r"^---\s*$\n", body, re.MULTILINE)
if m: body = body[m.end():]
# Strip trailing "Tab Context:" block
m = re.search(r"\n\s*Tab Context:", body)
if m: body = body[:m.start()]

sha = hashlib.sha256(body.encode("utf-8")).hexdigest()
word_count = len(re.findall(r"\w+", body))

# Synthesize structural markers
date_str = args.date or datetime.date.today().isoformat()
try:
    nice = datetime.datetime.strptime(date_str, "%Y-%m-%d").strftime("%b %d, %Y")
except Exception:
    nice = date_str

forum_id_m = re.search(r"\.(\d+)/?$", args.url.rstrip("/"))
forum_id = forum_id_m.group(1) if forum_id_m else "unknown"

body_with_markers = (
    f"# {args.title}\n\n"
    f"- Thread starter [{args.author}](synthetic)\n"
    f"- Start date [{nice}](synthetic)\n\n"
    f"{body.strip()}\n\n"
    f"Written by\n\n"
    f"### [{args.author}](synthetic)\n"
)

method = "claude_in_chrome_partial_capture" if args.partial else "claude_in_chrome_dom_capture"
stem = re.sub(r"[^a-z0-9]+", "-", args.title.lower())[:60].strip("-")
out = args.out_dir / f"{stem}.md"
args.out_dir.mkdir(parents=True, exist_ok=True)

partial_note = ""
if args.partial and args.full_body_bytes:
    partial_note = f"\n  Partial capture: {len(body)} bytes of {args.full_body_bytes} total.\n  Remainder unavailable due to Chrome javascript_tool display cap (~1KB)."

fm = f"""---
source_url: "{args.url}"
forum_thread_id: {forum_id}
source_sha256: {sha}
title: "{args.title}"
extraction_method: {method}
extraction_date: {datetime.date.today()}
text_layer_present: true
ocr_used: false
body_word_count: {word_count}
language: en
extraction_rationale: |
  Captured via Claude in Chrome (mcp__claude_in_chrome__get_page_text or
  javascript_tool scoped to .message-body .bbWrapper) because WebFetch
  returned a truncated inline response or a Cloudflare challenge. XenForo
  structural markers were synthesized so downstream regexes locate the
  body, signature, and reply anchors.
notes_for_analyst: |
  Chrome-captured fetch: author_handle is synthesized because the XenForo
  signature card is not present in DOM text. inline_image_count reflects
  body-text [Image - X] placeholders only. Reactions block absent.{partial_note}
---

{body_with_markers}
"""
out.write_text(fm, encoding="utf-8")
print(f"OK: {out.name} ({word_count} words, {method})")
