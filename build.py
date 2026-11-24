"""Builds the public pages from the Markdown sources.

Run after editing a .md file:  python build.py

Why plain HTML: the default GitHub Pages theme loaded a script from a
third-party CDN on every visit, which sends the visitor's IP address to
another company. These pages load nothing from other servers. The
.nojekyll file turns the theme off, so GitHub serves the files as they are.

Supported Markdown: '# ' and '## ' headings, paragraphs, '• ' bullets,
two trailing spaces as a line break, **bold** and [text](link).
"""
import html
import re
from pathlib import Path

PAGES = {
    "privacy-policy.md": "en",
    "terms-of-use.md": "en",
    "kvkk-aydinlatma.md": "tr",
    "kullanim-sartlari.md": "tr",
}

STYLE = """
  :root { color-scheme: light dark; }
  body { margin: 0 auto; max-width: 760px; padding: 24px 16px 48px;
         font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
         line-height: 1.6; color: #1f2933; background: #ffffff; }
  h1 { font-size: 1.7rem; line-height: 1.25; }
  h2 { font-size: 1.2rem; margin-top: 2rem; }
  a { color: #0f766e; }
  ul { padding-left: 1.2rem; }
  li { margin: 0.3rem 0; }
  @media (prefers-color-scheme: dark) {
    body { color: #e5e7eb; background: #111827; }
    a { color: #5eead4; }
  }
"""


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    return text


def convert(md):
    out, para, bullets = [], [], []

    def flush():
        if para:
            out.append("<p>" + "".join(para) + "</p>")
            para.clear()
        if bullets:
            out.append("<ul>\n" + "\n".join(f"<li>{b}</li>" for b in bullets) + "\n</ul>")
            bullets.clear()

    title = ""
    for raw in md.splitlines():
        line = raw.rstrip("\n")
        stripped = line.strip()
        if not stripped:
            flush()
        elif stripped.startswith("# "):
            flush()
            title = stripped[2:]
            out.append(f"<h1>{inline(title)}</h1>")
        elif stripped.startswith("## "):
            flush()
            out.append(f"<h2>{inline(stripped[3:])}</h2>")
        elif stripped.startswith("• "):
            if para:
                flush()
            bullets.append(inline(stripped[2:]))
        else:
            if bullets:
                flush()
            br = "<br>\n" if line.endswith("  ") else " "
            para.append(inline(stripped) + br)
    flush()
    return title, "\n".join(out)


for name, lang in PAGES.items():
    src = Path(name)
    title, body = convert(src.read_text(encoding="utf-8"))
    page = (
        "<!DOCTYPE html>\n"
        f'<html lang="{lang}">\n<head>\n<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f"<title>{html.escape(title)}</title>\n<style>{STYLE}</style>\n</head>\n<body>\n"
        f"{body}\n</body>\n</html>\n"
    )
    src.with_suffix(".html").write_text(page, encoding="utf-8", newline="\n")
    print("built", src.with_suffix(".html"))
