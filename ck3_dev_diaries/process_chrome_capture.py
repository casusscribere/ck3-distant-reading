#!/usr/bin/env python3
"""process_chrome_capture.py — Chrome→adapter→extractor in one call."""
import argparse, datetime, json, pathlib, re, subprocess, sys, time

ap = argparse.ArgumentParser()
ap.add_argument("chrome_file", type=pathlib.Path)
ap.add_argument("url")
ap.add_argument("forum_id")
ap.add_argument("--wiki-number", default=None)
ap.add_argument("--expansion", default=None)
ap.add_argument("--patch", default=None)
ap.add_argument("--title", default=None)
ap.add_argument("--author", default="Paradox Dev")
ap.add_argument("--date", default=None)
args = ap.parse_args()

raw = args.chrome_file.read_text(encoding="utf-8")
m = re.search(r"^---\s*$\n", raw, re.MULTILINE)
body = raw[m.end():] if m else raw
m = re.search(r"\n\s*Tab Context:", body)
if m: body = body[:m.start()]

page_title = args.title
if not page_title:
    m = re.search(r"^Title:\s*(.+?)(?:\s*\|\s*Paradox Interactive Forums)?$", raw, re.MULTILINE)
    page_title = m.group(1).strip() if m else f"Forum Thread {args.forum_id}"
page_title = re.sub(r"\s*\|\s*Paradox Interactive Forums\s*$", "", page_title)

date_str = args.date
if not date_str:
    for entry in json.load(open("/sessions/eager-zealous-hawking/mnt/outputs/ck3_extractor/manifest.json")):
        if entry["forum_id"] == args.forum_id:
            date_str = entry["date"]; break
if not date_str: date_str = datetime.date.today().isoformat()
try: nice_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").strftime("%b %d, %Y")
except: nice_date = date_str

body_with_markers = (
    f"# {page_title}\n\n"
    f"- Thread starter [{args.author}](https://forum.paradoxplaza.com/forum/members/synthetic.0/)\n"
    f"- Start date [{nice_date}](https://forum.paradoxplaza.com/forum/threads/.{args.forum_id}/)\n\n"
    f"{body.strip()}\n\nWritten by\n\n"
    f"### [{args.author}](https://forum.paradoxplaza.com/forum/members/synthetic.0/)\n\nParadox Staff\n"
)
out_dir = pathlib.Path("/sessions/eager-zealous-hawking/mnt/outputs/ck3_extractor/chrome_fetches")
out_dir.mkdir(parents=True, exist_ok=True)
fetch_file = out_dir / f"chrome-fetch-{args.forum_id}-{int(time.time())}.txt"
fetch_file.write_text(
    f"{page_title}\nhttps://forum.paradoxplaza.com/forum/threads/.{args.forum_id}\n→ {args.url}\n"
    f"Content-Type: text/html; charset=utf-8\n\n{body_with_markers}\n", encoding="utf-8")
print(f"Fetch file: {fetch_file.name} ({fetch_file.stat().st_size} bytes)")

workspace = pathlib.Path("/sessions/eager-zealous-hawking/mnt/26_NEH_WORKSHOP/Week 3/ck3_dev_diaries")
cmd = ["python3", str(workspace / "extract_diary.py"), str(fetch_file),
       "--forum-id", args.forum_id, "--out-dir", str(workspace)]
if args.wiki_number: cmd += ["--wiki-number", args.wiki_number]
if args.expansion:   cmd += ["--expansion", args.expansion]
if args.patch:       cmd += ["--patch", args.patch]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.stdout)
if r.returncode != 0:
    print(f"EXTRACT FAILED: {r.stderr}", file=sys.stderr); sys.exit(r.returncode)

# Post-edit: fix extraction_method and add Chrome provenance
wnum = int(args.wiki_number) if args.wiki_number else None
candidates = list(workspace.glob("dd_*.md"))
if wnum is not None:
    candidates = [m for m in candidates if m.name.startswith(f"dd_{wnum:03d}_")]
if candidates:
    md = max(candidates, key=lambda p: p.stat().st_mtime)
    text = md.read_text(encoding="utf-8")
    text = text.replace("extraction_method: webfetch_xenforo_text_layer",
                        "extraction_method: claude_in_chrome_dom_capture")
    text = re.sub(
        r"extraction_rationale: \|\n(?:  .+\n)+",
        "extraction_rationale: |\n"
        "  Captured via Claude in Chrome (get_page_text) because WebFetch returned\n"
        "  a truncated inline response or a Cloudflare challenge. XenForo structural\n"
        "  markers were synthesized by process_chrome_capture.py so extract_diary.py's\n"
        "  boundary regexes can locate the body, reactions, and signature anchors.\n",
        text, count=1)
    text = re.sub(
        r"notes_for_analyst: \|\n((?:  .+\n)+)",
        lambda m: "notes_for_analyst: |\n" + m.group(1).rstrip() +
                  "\n  Chrome-captured fetch: author_handle is synthesized because the\n"
                  "  XenForo signature card is not present in DOM text. inline_image_count\n"
                  "  reflects body-text image references only. Reactions block absent.\n",
        text, count=1)
    md.write_text(text, encoding="utf-8")
    print(f"Post-edited: {md.name}")
print("OK")
