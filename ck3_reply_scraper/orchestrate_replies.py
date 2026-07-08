#!/usr/bin/env python3
"""orchestrate_replies.py — resume-safe driver for the reply-thread scraper.

Mirrors orchestrate.py, but each thread has MULTIPLE page dumps (one per
forum page) that must be fed to extract_replies.py together.

It scans a directory of saved page dumps (WebFetch tool-results or
Claude-in-Chrome captures), groups them by forum thread id, orders them by
page number, and runs extract_replies.py once per thread. Threads whose
output already exists are skipped (resume-safe), so a long scrape can be
interrupted and continued.

USAGE
  python3 orchestrate_replies.py \
      --dumps-dir   ./reply_page_dumps \
      --manifest    ./manifest.json \
      --out-dir     ./ck3_reply_threads \
      --extractor   ./extract_replies.py
"""
import argparse, json, pathlib, re, subprocess, sys

RE_THREAD = re.compile(r"https://forum\.paradoxplaza\.com/forum/threads/\.(\d+)")
RE_PAGE   = re.compile(r"/page-(\d+)")

def scan_dumps(dumps_dir):
    """Return {forum_id: [(page_no, path), ...]} grouped & page-ordered."""
    groups = {}
    for f in sorted(pathlib.Path(dumps_dir).glob("*.txt")):
        head = f.read_text(encoding="utf-8", errors="replace")[:600]
        m = RE_THREAD.search(head)
        if not m:
            continue
        fid = m.group(1)
        pm = RE_PAGE.search(head)
        page = int(pm.group(1)) if pm else 1
        groups.setdefault(fid, []).append((page, f))
    for fid in groups:
        # de-dupe pages keeping the largest dump per page, then order
        best = {}
        for page, f in groups[fid]:
            if page not in best or f.stat().st_size > best[page].stat().st_size:
                best[page] = f
        groups[fid] = [best[p] for p in sorted(best)]
    return groups

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dumps-dir", required=True, type=pathlib.Path)
    ap.add_argument("--manifest", required=True, type=pathlib.Path)
    ap.add_argument("--out-dir", required=True, type=pathlib.Path)
    ap.add_argument("--extractor", default=pathlib.Path(__file__).parent / "extract_replies.py", type=pathlib.Path)
    ap.add_argument("--method", default="webfetch_xenforo_text_layer")
    ap.add_argument("--dd-corpus", default=None, type=pathlib.Path, help="dev-diary corpus dir; links each reply thread to its dd_*.md")
    ap.add_argument("--force", action="store_true", help="re-extract even if output exists")
    args = ap.parse_args()

    manifest = json.load(args.manifest.open())
    by_id = {e["forum_id"]: e for e in manifest}
    groups = scan_dumps(args.dumps_dir)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    existing = {p.name for p in args.out_dir.glob("rt_*.md")}
    dd_by_key = {}   # (wiki_number, date) -> filename  (date disambiguates DD#N reused across expansions)
    if args.dd_corpus and args.dd_corpus.exists():
        for p in args.dd_corpus.glob("dd_*.md"):
            mm = re.match(r"dd_(\d{3}|xxx)_(\d{4}-\d{2}-\d{2})_", p.name)
            if mm:
                wn = None if mm.group(1) == "xxx" else int(mm.group(1))
                dd_by_key[(wn, mm.group(2))] = p.name

    print(f"Manifest threads: {len(manifest)} | dumps found for {len(groups)} threads")
    results = []
    for fid, pages in groups.items():
        e = by_id.get(fid, {})
        wnum = e.get("wiki_number")
        date = e.get("date")
        title = e.get("title", f"Thread {fid}")
        # predicted output name (for resume skip)
        slug = re.sub(r"[^a-z0-9]+", "-", re.sub(r"^(?:ck3|crusader kings (?:iii|3))\s*-?\s*", "",
                      re.sub(r"^dev(?:eloper)? diary\s*#?\s*\d*\s*[-—]?\s*", "", title.lower()))).strip("-")[:40].strip("-")
        wf = (str(wnum).zfill(3) if wnum not in (None, "-", "") else "xxx")
        predicted = f"rt_{wf}_{date or 'unknown-date'}_{slug}__replies.md"
        if not args.force and predicted in existing:
            results.append({"forum_id": fid, "status": "skipped_exists", "pages": len(pages)})
            continue
        cmd = ["python3", str(args.extractor)] + [str(p) for p in pages] + [
            "--forum-id", fid, "--out-dir", str(args.out_dir), "--method", args.method,
            "--title", title]
        if date: cmd += ["--date", date]
        if wnum not in (None, "-", ""): cmd += ["--wiki-number", str(wnum)]
        if e.get("expansion"): cmd += ["--expansion", e["expansion"]]
        if e.get("patch"): cmd += ["--patch", e["patch"]]
        wn_key = int(wnum) if str(wnum).isdigit() else None
        parent = dd_by_key.get((wn_key, date))
        if parent:
            cmd += ["--parent-dd", parent]
        # parent dd file (best-effort match in sibling corpus, optional)
        r = subprocess.run(cmd, capture_output=True, text=True)
        status = "ok" if r.returncode == 0 else "extract_failed"
        results.append({"forum_id": fid, "status": status, "pages": len(pages),
                        "stdout": r.stdout.strip()[-400:], "stderr": r.stderr.strip()[:200]})
        print(f"  [{status}] {fid} ({len(pages)}p) {title!r}")

    (args.out_dir / "reply_run_results.json").write_text(json.dumps(results, indent=2, ensure_ascii=False))
    ok = sum(1 for r in results if r["status"] == "ok")
    sk = sum(1 for r in results if r["status"] == "skipped_exists")
    fa = sum(1 for r in results if r["status"] == "extract_failed")
    miss = [e["forum_id"] for e in manifest if e["forum_id"] not in groups]
    print(f"\nOK: {ok} | skipped(existing): {sk} | extract-failed: {fa} | no-dumps: {len(miss)}")
    if miss:
        print("Threads still needing page dumps:", ", ".join(miss[:15]), ("…" if len(miss) > 15 else ""))

if __name__ == "__main__":
    main()
