#!/usr/bin/env python3
"""00_extract_corpus.py — Step 0 orchestrator.

Reads input from a directory (files) or a URL list (one per line, .txt),
dispatches each item to the appropriate extractor based on type and probe
results, writes provenance-tagged .md files to corpus_md/, emits MANIFEST.md.

Usage:
    python3 00_extract_corpus.py --input PATH --out-dir corpus_md/
"""
import argparse, json, pathlib, re, subprocess, sys, hashlib, datetime

URL_PATTERN = re.compile(r"^https?://", re.IGNORECASE)

def classify_source(path_or_url):
    """Return ('file', ext) or ('url', None)."""
    if URL_PATTERN.match(str(path_or_url)):
        return ("url", None)
    p = pathlib.Path(path_or_url)
    return ("file", p.suffix.lower())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Directory path OR URL-list .txt path")
    ap.add_argument("--out-dir", required=True, type=pathlib.Path)
    ap.add_argument("--mode", default="auto", choices=["auto", "files-only", "urls-only"])
    args = ap.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    scripts = pathlib.Path(__file__).parent

    # Build input list
    inputs = []
    inp = pathlib.Path(args.input)
    if inp.is_dir():
        for f in sorted(inp.iterdir()):
            if f.is_file(): inputs.append(str(f))
    elif inp.suffix.lower() == ".txt" and args.mode != "files-only":
        # Could be a URL list OR a single text file. Probe.
        with inp.open() as f:
            head = f.read(2000)
        if URL_PATTERN.search(head):
            inputs.extend([l.strip() for l in inp.read_text().splitlines() if l.strip()])
        else:
            inputs.append(str(inp))
    else:
        inputs.append(str(inp))

    print(f"Inputs to process: {len(inputs)}")
    results = []
    for inp in inputs:
        kind, ext = classify_source(inp)
        # Route to appropriate extractor
        if kind == "url":
            r = subprocess.run(["python3", str(scripts / "00h_probe_url.py"), inp],
                               capture_output=True, text=True)
            decision = r.stdout.strip()
            if decision == "server-rendered-clean":
                cmd = [str(scripts / "00i_extract_webfetch.py"), inp, "--out-dir", str(args.out_dir)]
            else:
                cmd = [str(scripts / "00j_extract_chrome.py"), inp, "--out-dir", str(args.out_dir)]
        elif ext == ".pdf":
            r = subprocess.run(["python3", str(scripts / "00a_probe_pdf.py"), inp],
                               capture_output=True, text=True)
            decision = r.stdout.strip()
            if decision == "text-layer-extraction":
                cmd = ["python3", str(scripts / "00b_extract_pdftotext.py"), inp,
                       "--out-dir", str(args.out_dir)]
            else:
                cmd = ["python3", str(scripts / "00c_extract_ocr.py"), inp,
                       "--out-dir", str(args.out_dir)]
        elif ext in (".txt", ".md"):
            cmd = ["python3", str(scripts / "00d_extract_plaintext.py"), inp,
                   "--out-dir", str(args.out_dir)]
        elif ext in (".html", ".htm", ".epub"):
            cmd = ["python3", str(scripts / "00e_extract_html_epub.py"), inp,
                   "--out-dir", str(args.out_dir)]
        else:
            print(f"  SKIP: unknown source type for {inp}")
            results.append({"input": inp, "status": "skipped_unknown_type"})
            continue
        r = subprocess.run(cmd, capture_output=True, text=True)
        status = "ok" if r.returncode == 0 else "extract_failed"
        results.append({"input": inp, "status": status, "stderr": r.stderr.strip()[:200]})
        print(f"  {status}: {inp}")

    # Annotate artifacts on each emitted .md
    annot = scripts / "00f_annotate_artifacts.py"
    if annot.exists():
        for md in args.out_dir.glob("*.md"):
            subprocess.run(["python3", str(annot), str(md)], capture_output=True)

    # Validate
    valid = scripts / "00g_validate_markdown.py"
    if valid.exists():
        r = subprocess.run(["python3", str(valid), str(args.out_dir)], capture_output=True, text=True)
        print(r.stdout)

    # Write MANIFEST.md
    manifest_lines = ["# Corpus Manifest", "", f"*Generated {datetime.date.today()}*",
                      "", f"Sources processed: {len(results)}",
                      f"Extractions succeeded: {sum(1 for r in results if r['status']=='ok')}",
                      "", "| Input | Status |", "|---|---|"]
    for r in results:
        manifest_lines.append(f"| `{pathlib.Path(r['input']).name if not r['input'].startswith('http') else r['input']}` | {r['status']} |")
    (args.out_dir / "MANIFEST.md").write_text("\n".join(manifest_lines))
    print(f"\nMANIFEST.md written to {args.out_dir}")

if __name__ == "__main__":
    main()
