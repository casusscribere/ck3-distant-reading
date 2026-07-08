#!/usr/bin/env python3
"""chrome_fetch_to_file.py — adapter for Claude in Chrome capture.

Writes Chrome-captured page text to a file in the format orchestrate.py and
extract_diary.py expect. Output goes to /tmp/chrome_fetches/ (writable from
the sandbox); orchestrate.py is patched to scan this directory alongside
the standard tool-results dir.
"""
import sys, pathlib, time, re

if len(sys.argv) < 3:
    print("usage: chrome_fetch_to_file.py <url> <page-title>", file=sys.stderr)
    sys.exit(1)

url = sys.argv[1]
page_title = sys.argv[2]
text = sys.stdin.read()

m = re.search(r"\.(\d+)/?$", url.rstrip("/"))
if not m:
    print(f"ERROR: could not parse forum_id from URL: {url}", file=sys.stderr)
    sys.exit(1)
forum_id = m.group(1)

out_dir = pathlib.Path("/sessions/eager-zealous-hawking/mnt/outputs/ck3_extractor/chrome_fetches")
out_dir.mkdir(parents=True, exist_ok=True)
out = out_dir / f"chrome-fetch-{forum_id}-{int(time.time())}.txt"

out.write_text(
    f"{page_title}\n"
    f"https://forum.paradoxplaza.com/forum/threads/.{forum_id}\n"
    f"→ {url}\n"
    f"Content-Type: text/html; charset=utf-8\n"
    f"\n"
    f"{text}\n",
    encoding="utf-8"
)
print(out)
