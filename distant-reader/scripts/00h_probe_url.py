#!/usr/bin/env python3
"""00h_probe_url.py — classify a URL's response shape.

NOTE: Unlike the file-based probes, this script CANNOT make the WebFetch call
itself (WebFetch is a Cowork tool, not invokable from Python). The probe is
performed by the calling Claude session, which then passes the response shape
to this script as an argument, OR the script returns a default routing
recommendation based on URL pattern matching.

Default policy: route XenForo, Cloudflare-fronted, and major news sites that
historically truncate to Chrome; everything else to WebFetch.
"""
import sys, re

if len(sys.argv) < 2:
    print("usage: 00h_probe_url.py <url>", file=sys.stderr); sys.exit(1)
url = sys.argv[1]

# Heuristic routing decisions based on URL patterns observed in the CK3 run
# and known Cloudflare-fronted publishers. Claude can override based on actual
# probe results.
CHROME_PREFERRED_DOMAINS = [
    "forum.paradoxplaza.com",  # XenForo with truncation risk for long OPs
]
KNOWN_CLOUDFLARE = [
    "paradoxwikis.com",
]
WEBFETCH_PREFERRED_DOMAINS = [
    "gutenberg.org",
    "wikipedia.org",
    "wikisource.org",
    "github.com",
    "anthropic.com",
]

for d in CHROME_PREFERRED_DOMAINS:
    if d in url:
        print("chrome-preferred"); sys.exit(0)
for d in KNOWN_CLOUDFLARE:
    if d in url:
        print("chrome-required"); sys.exit(0)
for d in WEBFETCH_PREFERRED_DOMAINS:
    if d in url:
        print("server-rendered-clean"); sys.exit(0)
# Default: try WebFetch first; downgrade to Chrome on truncation
print("server-rendered-clean")
