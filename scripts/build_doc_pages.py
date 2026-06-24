#!/usr/bin/env python3
"""Render the engagement's Markdown docs into brand-styled HTML pages.

The command-center site (docs/index.html) is hand-built HTML with no Jekyll, so a
link to a raw ".md" serves an unstyled markdown download instead of a page. This
script renders every doc Markdown file to a sibling ".html" in the Top Spirit brand
(deep navy ground, gold accent, Inter + Playfair), and rewrites internal ".md"
links to ".html" so the whole doc set is browsable as real pages. The ".md" sources
are kept (this is additive). Idempotent: safe to re-run after any content change.

Usage:
    python scripts/build_doc_pages.py            # build
    python scripts/build_doc_pages.py --check    # fail if any output is stale
"""
import glob
import html
import os
import re
import sys

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_REL = "docs/index.html"

CSS = """
:root{
  --deep:#07111F; --surface:#101B2A; --line:#1d2c40; --border:#2a3a4f;
  --gold:#D6A94A; --teal:#0D9488; --cream:#F6F1E8; --paper:#FBF8F1;
  --ink:#10243a; --muted:#5b6b7d; --clay:#B45309;
}
*{box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{
  margin:0; font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  color:var(--ink); background:linear-gradient(160deg,var(--deep) 0%,var(--surface) 100%);
  background-attachment:fixed; line-height:1.65;
}
.topbar{
  position:sticky; top:0; z-index:10; display:flex; align-items:center; justify-content:space-between;
  gap:18px; padding:14px 28px; background:rgba(7,17,31,.92); backdrop-filter:blur(8px);
  border-bottom:1px solid var(--border);
}
.brand{display:flex; flex-direction:column; line-height:1.2;}
.brand .name{color:#fff; font-weight:800; letter-spacing:-.01em; font-size:15px;}
.brand .sub{color:var(--gold); font-size:11px; text-transform:uppercase; letter-spacing:.14em;}
.back{
  color:#cdd8e6; text-decoration:none; font-size:14px; font-weight:600; white-space:nowrap;
  border:1px solid var(--border); padding:8px 14px; border-radius:9px; transition:all .15s;
}
.back:hover{color:#fff; border-color:var(--gold); background:rgba(214,169,74,.12);}
.wrap{max-width:880px; margin:34px auto 60px; padding:0 22px;}
.doc{
  background:var(--paper); border-radius:16px; padding:54px 56px;
  box-shadow:0 24px 60px rgba(0,0,0,.35); border:1px solid rgba(255,255,255,.06);
}
.doc h1,.doc h2,.doc h3,.doc h4{font-family:"Playfair Display",Georgia,serif; color:var(--deep); line-height:1.18; letter-spacing:-.01em;}
.doc h1{font-size:34px; margin:0 0 8px; padding-bottom:16px; border-bottom:3px solid var(--gold);}
.doc h2{font-size:25px; margin:38px 0 12px;}
.doc h3{font-size:19px; margin:28px 0 8px;}
.doc h4{font-size:16px; margin:22px 0 6px; font-family:Inter,sans-serif; font-weight:700;}
.doc p{margin:12px 0;}
.doc a{color:var(--teal); text-decoration:none; border-bottom:1px solid rgba(13,148,136,.3);}
.doc a:hover{color:var(--clay); border-bottom-color:var(--clay);}
.doc ul,.doc ol{padding-left:24px; margin:12px 0;}
.doc li{margin:5px 0;}
.doc strong{color:var(--deep);}
.doc blockquote{
  margin:18px 0; padding:12px 20px; border-left:4px solid var(--gold);
  background:rgba(214,169,74,.08); color:var(--ink); border-radius:0 8px 8px 0;
}
.doc blockquote p{margin:6px 0;}
.doc code{
  font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace; font-size:.88em;
  background:#eee6d6; color:#7a4d12; padding:2px 6px; border-radius:5px;
}
.doc pre{
  background:var(--deep); color:#e6edf6; padding:18px 20px; border-radius:11px;
  overflow:auto; font-size:13px; line-height:1.55; border:1px solid var(--border);
}
.doc pre code{background:none; color:inherit; padding:0;}
.doc table{border-collapse:collapse; width:100%; margin:20px 0; font-size:14.5px; overflow:hidden; border-radius:10px;}
.doc thead th{background:var(--deep); color:#fff; text-align:left; padding:11px 14px; font-weight:600;}
.doc tbody td{padding:10px 14px; border-bottom:1px solid #e6ddca; vertical-align:top;}
.doc tbody tr:nth-child(even){background:rgba(16,36,58,.035);}
.doc tbody tr:last-child td{border-bottom:none;}
.doc hr{border:none; border-top:1px solid #e0d6c0; margin:30px 0;}
.doc img{max-width:100%; border-radius:10px;}
.footer{max-width:880px; margin:0 auto 50px; padding:0 22px; color:#8ea2b8; font-size:12.5px; text-align:center;}
.footer a{color:#bcd0e6;}
@media (max-width:640px){.doc{padding:32px 22px;} .wrap{margin-top:20px;} .doc h1{font-size:27px;}}
"""

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__ — Top Spirit Command Center</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap" rel="stylesheet">
<style>__CSS__</style>
</head>
<body>
<header class="topbar">
  <div class="brand"><span class="name">Top Spirit Command Center</span><span class="sub">Angel Software Solutions</span></div>
  <a class="back" href="__BACK__">Back to command center</a>
</header>
<div class="wrap">
  <article class="doc">
__BODY__
  </article>
</div>
<footer class="footer">
  <p>Private pre-call draft for Top Spirit (Marussia) and Angel Software Solutions. Demo values are illustrative; starter data is synthetic; client evidence gates remain explicit.</p>
</footer>
</body>
</html>
"""

MD_EXT = ["tables", "fenced_code", "sane_lists", "toc", "attr_list", "md_in_html"]
_MD_HREF = re.compile(r'(href=")([^"]+?)\.md(#[^"]*)?(")')


def collect():
    """Doc Markdown to render: the whole docs/ tree plus any docs under assets/
    (mockups, pitch decks, presentation set). The mirror site keeps some linked docs
    under assets/pitch, so globbing both layouts keeps one converter working for both
    repos. Internal brand-review docs (assets/brand/*) are not client-facing pages."""
    files = set(glob.glob(os.path.join(ROOT, "docs", "**", "*.md"), recursive=True))
    for p in glob.glob(os.path.join(ROOT, "assets", "**", "*.md"), recursive=True):
        if "/assets/brand/" in p.replace(os.sep, "/"):
            continue
        files.add(p)
    return sorted(files)


def title_from(text, fallback):
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s[2:].strip()
    return fallback


def rewrite_md_links(body):
    # Internal links to other docs become .html so the set browses as real pages.
    return _MD_HREF.sub(lambda m: m.group(1) + m.group(2) + ".html" + (m.group(3) or "") + m.group(4), body)


def back_link(out_path):
    rel = os.path.relpath(os.path.join(ROOT, INDEX_REL), os.path.dirname(out_path))
    return rel.replace(os.sep, "/")


def render(src):
    text = open(src, encoding="utf-8").read()
    title = title_from(text, os.path.splitext(os.path.basename(src))[0])
    body = markdown.markdown(text, extensions=MD_EXT)
    body = rewrite_md_links(body)
    page = (TEMPLATE
            .replace("__TITLE__", html.escape(title))
            .replace("__CSS__", CSS)
            .replace("__BACK__", back_link(os.path.splitext(src)[0] + ".html"))
            .replace("__BODY__", body))
    return page


def main():
    check = "--check" in sys.argv
    srcs = collect()
    built = 0
    stale = []
    for src in srcs:
        out = os.path.splitext(src)[0] + ".html"
        try:
            page = render(src)
        except Exception as exc:
            print(f"  skip unreadable {os.path.relpath(src, ROOT)}: {type(exc).__name__}")
            continue
        if check:
            existing = open(out, encoding="utf-8").read() if os.path.exists(out) else None
            if existing != page:
                stale.append(os.path.relpath(out, ROOT))
            continue
        with open(out, "w", encoding="utf-8") as f:
            f.write(page)
        built += 1
    if check:
        if stale:
            print("doc-pages STALE (run build_doc_pages.py):")
            for s in stale:
                print("  " + s)
            sys.exit(1)
        print(f"doc-pages=ok ({len(srcs)} pages current)")
        return
    print(f"doc-pages built {built} HTML pages from Markdown")


if __name__ == "__main__":
    main()
