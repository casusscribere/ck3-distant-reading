#!/usr/bin/env python3
"""00k_chrome_capture_adapter.py — minimal shim equivalent to the CK3
chrome_fetch_to_file.py: take URL + page title + body via stdin, write a file
shaped like a WebFetch saved temp file so 00i_extract_webfetch.py can process it.

Use when you want to leverage the WebFetch-based extractor path against a
Chrome-captured body. Most users should prefer 00j_extract_chrome.py which
goes straight to the final .md.
"""
import sys, pathlib, time, re

if len(sys.argv) < 4:
    print("usage: 00k_chrome_capture_adapter.py URL TITLE OUT_DIR", file=sys.stderr); sys.exit(1)
url, title, out_dir = sys.argv[1], sys.argv[2], pathlib.Path(sys.argv[3])
body = sys.stdin.read()
m = re.search(r"\.(\d+)/?$", url.rstrip("/"))
fid = m.group(1) if m else "x"
out_dir.mkdir(parents=True, exist_ok=True)
out = out_dir / f"chrome-fetch-{fid}-{int(time.time())}.txt"
out.write_text(f"{title}\nhttps://www.example.com/.{fid}\n→ {url}\n"
               f"Content-Type: text/html; charset=utf-8\n\n{body}\n",
               encoding="utf-8")
print(out)
