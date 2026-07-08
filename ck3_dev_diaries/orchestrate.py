#!/usr/bin/env python3
"""orchestrate.py — Match saved WebFetch tool-results to manifest entries,
run the extractor on each, and write to corpus directory."""
import json, pathlib, re, subprocess, sys, datetime

TOOL_RESULTS = pathlib.Path("/sessions/eager-zealous-hawking/mnt/.claude/projects/C--Users-kirkl-AppData-Roaming-Claude-local-agent-mode-sessions-0cc742ec-186e-4ed9-8c21-0ef78972fd96-aa9eec76-9566-42c2-a94d-f9b130ab7646-local-785f3833-b385-44ae-a6cf-32f1c1d839b1-outputs/0429b5a9-2d6f-4046-a212-43a7501b3fa3/tool-results")
EXTRACT_SCRIPT = pathlib.Path("/sessions/eager-zealous-hawking/mnt/outputs/ck3_extractor/extract_diary.py")
MANIFEST = pathlib.Path("/sessions/eager-zealous-hawking/mnt/outputs/ck3_extractor/manifest.json")
CORPUS_DIR = pathlib.Path("/sessions/eager-zealous-hawking/mnt/26_NEH_WORKSHOP/Week 3/ck3_dev_diaries")

def map_fetches_to_forum_ids():
    """Walk tool-results dir + chrome_fetches/, identify which forum thread each file is for."""
    mapping = {}
    chrome_dir = pathlib.Path("/sessions/eager-zealous-hawking/mnt/outputs/ck3_extractor/chrome_fetches")
    all_fetches = sorted(TOOL_RESULTS.glob("mcp-workspace-web_fetch-*.txt"), key=lambda p: p.stat().st_mtime)
    if chrome_dir.exists():
        all_fetches += sorted(chrome_dir.glob("chrome-fetch-*.txt"), key=lambda p: p.stat().st_mtime)
    for f in all_fetches:
        try:
            head = f.read_text(encoding="utf-8", errors="replace")[:500]
            m = re.search(r"https://forum\.paradoxplaza\.com/forum/threads/\.(\d+)", head)
            if m:
                forum_id = m.group(1)
                # Keep the largest (most-complete) fetch for each forum_id
                if forum_id not in mapping or f.stat().st_size > mapping[forum_id].stat().st_size:
                    mapping[forum_id] = f
        except Exception as e:
            print(f"WARN: could not parse {f.name}: {e}", file=sys.stderr)
    return mapping

def run_extractor(fetch_file, entry):
    """Invoke extract_diary.py for one entry."""
    cmd = [
        "python3", str(EXTRACT_SCRIPT),
        str(fetch_file),
        "--forum-id", entry["forum_id"],
        "--out-dir", str(CORPUS_DIR),
    ]
    if entry["wiki_number"] is not None:
        cmd += ["--wiki-number", str(entry["wiki_number"])]
    if entry["expansion"]:
        cmd += ["--expansion", entry["expansion"]]
    if entry["patch"]:
        cmd += ["--patch", entry["patch"]]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr

def main():
    manifest = json.load(MANIFEST.open())
    fetches = map_fetches_to_forum_ids()
    print(f"Manifest entries: {len(manifest)}")
    print(f"Fetched: {len(fetches)}")
    print(f"Missing: {len(manifest) - sum(1 for e in manifest if e['forum_id'] in fetches)}")
    print()

    CORPUS_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    for entry in manifest:
        fid = entry["forum_id"]
        if fid not in fetches:
            results.append({"forum_id": fid, "wiki_number": entry["wiki_number"],
                            "title": entry["title"], "date": entry["date"],
                            "expansion": entry["expansion"], "status": "fetch_failed",
                            "size_bytes": 0})
            continue
        fetch_file = fetches[fid]
        size = fetch_file.stat().st_size
        # If the fetch is implausibly small (<2KB), the page was empty or errored
        if size < 2000:
            results.append({"forum_id": fid, "wiki_number": entry["wiki_number"],
                            "title": entry["title"], "date": entry["date"],
                            "expansion": entry["expansion"], "status": "fetch_too_small",
                            "size_bytes": size})
            continue
        rc, out, err = run_extractor(fetch_file, entry)
        if rc != 0:
            results.append({"forum_id": fid, "wiki_number": entry["wiki_number"],
                            "title": entry["title"], "date": entry["date"],
                            "expansion": entry["expansion"], "status": "extract_failed",
                            "size_bytes": size, "error": err.strip()[:200]})
        else:
            results.append({"forum_id": fid, "wiki_number": entry["wiki_number"],
                            "title": entry["title"], "date": entry["date"],
                            "expansion": entry["expansion"], "status": "ok",
                            "size_bytes": size, "extractor_output": out.strip()[-500:]})

    # Save run report
    pathlib.Path("/sessions/eager-zealous-hawking/mnt/outputs/ck3_extractor/run_results.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False))
    # Summary
    ok = sum(1 for r in results if r["status"] == "ok")
    failed_fetch = sum(1 for r in results if r["status"] == "fetch_failed")
    too_small = sum(1 for r in results if r["status"] == "fetch_too_small")
    extract_failed = sum(1 for r in results if r["status"] == "extract_failed")
    print(f"  OK:            {ok}")
    print(f"  Fetch failed:  {failed_fetch}")
    print(f"  Too small:     {too_small}")
    print(f"  Extract fail:  {extract_failed}")
    if extract_failed:
        print("\n=== Extraction failures ===")
        for r in results:
            if r["status"] == "extract_failed":
                print(f"  {r['forum_id']}  {r['title']}: {r.get('error','?')[:120]}")
    if failed_fetch or too_small:
        print("\n=== Fetch problems (would benefit from re-fetch) ===")
        for r in results:
            if r["status"] in ("fetch_failed", "fetch_too_small"):
                print(f"  {r['forum_id']}  ({r['date']})  {r['title']!r}  [{r['status']}, {r['size_bytes']} bytes]")

if __name__ == "__main__":
    main()
