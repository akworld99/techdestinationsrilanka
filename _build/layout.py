"""Turns the narrow, blog-like inner page markup into the wide page layout.

Every generator writes the same simple markup (a .page-head section, then
sections wrapped in .wrap.narrow). page() runs upgrade() on the body, so the
whole site moves to the new layout without touching each generator:

  page-head  ->  navy hero, title on the left, short answer on the right
  narrow     ->  sidebar (contents + contact card) beside a wide main column
"""
import html
import re

HEAD_OPEN = '<section class="page-head"><div class="wrap narrow">'


def _slug(text):
    t = re.sub(r"<[^>]+>", "", text)
    t = re.sub(r"[^a-z0-9]+", "-", html.unescape(t).lower()).strip("-")
    return t[:60] or "section"


def _close_of(body, start, tag="section"):
    """Index just past the </tag> that closes the <tag> opened at start."""
    depth, i = 0, start
    pat = re.compile(rf"<(/?){tag}\b[^>]*>")
    for m in pat.finditer(body, start):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return m.end()
    return -1


def _first_unbalanced_close(html_text):
    depth = 0
    for m in re.finditer(r"<(/?)div\b[^>]*>", html_text):
        depth += -1 if m.group(1) else 1
        if depth < 0:
            return m.start()
    return -1


def _narrow_to_doc(tail):
    """Inside a tail, turn any top-level wrap.narrow block into an aligned doc block."""
    out, pos = "", 0
    opener = '<div class="wrap narrow">'
    while True:
        i = tail.find(opener, pos)
        if i < 0:
            return out + tail[pos:]
        depth, end = 0, -1
        for m in re.finditer(r"<(/?)div\b[^>]*>", tail[i:]):
            depth += -1 if m.group(1) else 1
            if depth == 0:
                end = i + m.start()
                close_end = i + m.end()
                break
        if end < 0:
            return out + tail[pos:]
        out += tail[pos:i] + '<div class="wrap doc"><aside class="doc-side"></aside><div class="doc-main">' + tail[i + len(opener):end] + "</div></div>"
        pos = close_end


def _hero(inner):
    m = re.search(r"</h1>", inner)
    if not m:
        return f'<section class="ph"><div class="wrap ph-grid one"><div class="ph-title">{inner}</div></div><div class="ph-flag" aria-hidden="true"><i></i><i></i><i></i><i></i></div></section>'
    left, right = inner[:m.end()], inner[m.end():].strip()
    grid = "ph-grid" if right else "ph-grid one"
    right_html = f'<div class="ph-answer">{right}</div>' if right else ""
    return (f'<section class="ph"><div class="wrap {grid}"><div class="ph-title">{left}</div>{right_html}</div>'
            f'<div class="ph-flag" aria-hidden="true"><i></i><i></i><i></i><i></i></div></section>')


def _card_for(path, prefix):
    if path.startswith("source/"):
        return ("Buying from Sri Lanka?", "Tell us the product and volumes. We connect you with exporters who can supply it.", "Request a quote", f"{prefix}source/request-a-quote/")
    if path.startswith("offshoring/"):
        return ("Outsourcing to Sri Lanka?", "Tell us the work you want to move. We introduce teams that already do it for clients abroad.", "Tell us what you need", f"{prefix}contact/")
    return ("Building a team in Sri Lanka?", "Tell us what you need. We introduce companies and people who have done it before.", "Find talent", f"{prefix}talent/find/")


def _side(toc, prefix, booking, path=""):
    nav = ""
    if len(toc) >= 2:
        items = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
        nav = f'<nav class="side-toc" aria-label="On this page"><p class="side-h">On this page</p><ol>{items}</ol></nav>'
    h, t, label, href = _card_for(path, prefix)
    card = (f'<div class="side-card"><p class="side-card-h">{h}</p>'
            f'<p>{t}</p>'
            f'<a class="btn btn-saffron btn-small" href="{href}">{label}</a>'
            f'<a class="side-link" href="{booking}" rel="noopener">Schedule a call</a></div>')
    return f'<aside class="doc-side">{nav}{card}</aside>'


def upgrade(body, prefix, booking, path=""):
    body = re.sub(r'<section class="page-head(?: has-img)?">\s*<div class="wrap(?: narrow)?">', HEAD_OPEN, body)
    if HEAD_OPEN not in body:
        return body
    body = re.sub(r'(<section class="(?!page-head")[^"]*">)\s*<div class="wrap narrow([^"]*)">', r'\1<div class="wrap narrow" data-x="\2">', body)
    # 1. hero
    s = body.index(HEAD_OPEN)
    e = _close_of(body, s)
    inner = body[s + len(HEAD_OPEN):e]
    inner = inner[: inner.rfind("</div>")]  # drop the wrap's closing div and </section>
    body = body[:s] + _hero(inner.strip()) + body[e:]

    # 2. every narrow section after the hero becomes a doc layout
    first = True
    pos = 0
    used = set()
    while True:
        m = re.search(r'<section class="([^"]*)"><div class="wrap narrow"(?: data-x="([^"]*)")?>', body[pos:])
        if not m:
            break
        s = pos + m.start()
        e = _close_of(body, s)
        if e < 0:
            break
        sec = body[s:e]
        open_tag = f'<section class="{m.group(1)} doc-sec">'
        content = sec[len(m.group(0)):]
        content = content[: content.rfind("</section>")]
        content = content[: content.rfind("</div>")]

        def add_id(h):
            attrs, text = h.group(1), h.group(2)
            if "id=" in attrs:
                used.add(re.search(r'id="([^"]+)"', attrs).group(1))
                return h.group(0)
            hid = _slug(text)
            while hid in used:
                hid += "-2"
            used.add(hid)
            return f'<h2{attrs} id="{hid}">{text}</h2>'
        content = re.sub(r"<h2([^>]*)>(.*?)</h2>", add_id, content, flags=re.S)
        toc = []
        for h in re.finditer(r'<h2[^>]*id="([^"]+)"[^>]*>(.*?)</h2>', content, flags=re.S):
            text = re.sub(r"<[^>]+>", "", h.group(2)).strip()
            if text and text.lower() not in ("on this page",):
                toc.append((h.group(1), html.escape(html.unescape(text))))
        side = _side(toc, prefix, booking, path) if first else '<aside class="doc-side"></aside>'
        cut = _first_unbalanced_close(content)
        tail = ""
        if cut >= 0:
            tail = _narrow_to_doc(content[cut + 6:] + "</div>")
            content = content[:cut]
        extra = (m.group(2) or "").strip()
        new = f'{open_tag}<div class="wrap doc">{side}<div class="doc-main{(" " + extra) if extra else ""}">{content}</div></div>{tail}</section>'
        body = body[:s] + new + body[e:]
        pos = s + len(new)
        first = False
    return re.sub(r'<div class="wrap narrow" data-x="([^"]*)">', r'<div class="wrap narrow\1">', body)
