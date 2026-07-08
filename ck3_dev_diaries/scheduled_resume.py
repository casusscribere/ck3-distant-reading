#!/usr/bin/env python3
"""scheduled_resume.py — runs inside a scheduled-task session after Claude has
called mcp__workspace__web_fetch on a batch of URLs.

Auto-discovers this session's tool-results dir, matches saved fetches to
manifest entries by forum_id, runs extract_diary.py per match, updates
remaining_urls.txt. Idempotent.
"""
import json, pathlib, re, subprocess, sys

# Auto-discover workspace (Documents folder mount)
WORKSPACE = None
for sess in pathlib.Path("/sessions").iterdir():
    cand = sess / "mnt" / "26_NEH_WORKSHOP" / "Week 3" / "ck3_dev_diaries"
    if cand.exists():
        WORKSPACE = cand
        break
if not WORKSPACE:
    print("ERROR: workspace ck3_dev_diaries dir not found under /sessions/*/mnt/", file=sys.stderr)
    sys.exit(2)

# Auto-discover this session's tool-results dir
TOOL_RESULTS = None
for sess in pathlib.Path("/sessions").iterdir():
    proj_root = sess / "mnt" / ".claude" / "projects"
    if not proj_root.exists():
        continue
    for proj in proj_root.iterdir():
        tr = proj / "tool-results"
        if tr.exists() and any(tr.glob("mcp-workspace-web_fetch-*.txt")):
            TOOL_RESULTS = tr
            break
    if TOOL_RESULTS:
        break

if not TOOL_RESULTS:
    print("WARN: no tool-results directory with fetches found — nothing to extract.", file=sys.stderr)
    sys.exit(0)

print(f"Workspace: {WORKSPACE}")
print(f"Tool-results: {TOOL_RESULTS}")

# Load manifest
manifest = json.load((WORKSPACE / "manifest.json").open())
manifest_by_id = {e["forum_id"]: e for e in manifest}

# Map each saved fetch to its forum_id
fetches = {}
for f in sorted(TOOL_RESULTS.glob("mcp-workspace-web_fetch-*.txt"), key=lambda p: p.stat().st_mtime):
    try:
        head = f.read_text(encoding="utf-8", errors="replace")[:500]
        m = re.search(r"https://forum\.paradoxplaza\.com/forum/threads/\.(\d+)", head)
        if m:
            forum_id = m.group(1)
            if forum_id not in fetches or f.stat().st_size > fetches[forum_id].stat().st_size:
                fetches[forum_id] = f
    except Exception as e:
        continue

print(f"Saved fetches discovered: {len(fetches)}")

# Identify which need extracting (have fetch, no markdown yet, size > 2KB)
to_extract = []
for fid, fetch_file in fetches.items():
    if fid not in manifest_by_id:
        continue
    if fetch_file.stat().st_size < 2000:
        continue
    # Check if a markdown file already exists for this forum thread
    if any(f.read_text(encoding="utf-8", errors="replace")[:2000].find(f"forum_thread_id: {fid}") >= 0
           for f in WORKSPACE.glob("dd_*.md")):
        continue
    to_extract.append((fid, fetch_file))

print(f"To extract this run: {len(to_extract)}")

EXTRACTOR = WORKSPACE / "extract_diary.py"
ok = 0; fail = 0
for fid, fetch_file in to_extract:
    entry = manifest_by_id[fid]
    cmd = ["python3", str(EXTRACTOR), str(fetch_file),
           "--forum-id", fid, "--out-dir", str(WORKSPACE)]
    if entry["wiki_number"] is not None:
        cmd += ["--wiki-number", str(entry["wiki_number"])]
    if entry.get("expansion"):
        cmd += ["--expansion", entry["expansion"]]
    if entry.get("patch"):
        cmd += ["--patch", entry["patch"]]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode == 0:
        ok += 1
    else:
        fail += 1
        print(f"  FAIL {fid}: {r.stderr.strip()[:120]}", file=sys.stderr)

print(f"Extracted OK: {ok}   Failures: {fail}")

# Refresh remaining_urls.txt by walking corpus_md and checking what's done
done_ids = set()
for f in WORKSPACE.glob("dd_*.md"):
    text = f.read_text(encoding="utf-8", errors="replace")[:2000]
    m = re.search(r"forum_thread_id:\s*(\d+)", text)
    if m:
        done_ids.add(m.group(1))

remaining = [e for e in manifest if e["forum_id"] not in done_ids]
with (WORKSPACE / "remaining_urls.txt").open("w") as f:
    for e in remaining:
        f.write(f"https://forum.paradoxplaza.com/forum/threads/.{e['forum_id']}/\n")
print(f"Corpus now: {len(done_ids)} done, {len(remaining)} remaining")

# Refresh MANIFEST.md by invoking build_corpus_manifest.py
bcm = WORKSPACE / "build_corpus_manifest.py"
if bcm.exists():
    subprocess.run(["python3", str(bcm)], capture_output=True)

print(f"DONE_FLAG: {'YES' if len(remaining) == 0 else 'NO'}")
