"""Share images (1200 x 630) for the Source from Sri Lanka pages.

Run after the art exists:  python3 _build/og_source.py
Writes assets/og/source-<name>.jpg. The build links each page to its image when the file is there.
"""
import base64
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import source_data as D  # noqa: E402

OUT = os.path.join(ROOT, "assets", "og")


def og_path(name):
    """Site-relative path of a page's share image, or None when it has not been rendered."""
    rel = f"assets/og/source-{name}.jpg"
    return rel if os.path.exists(os.path.join(ROOT, rel)) else None


def pages():
    """(name, kicker, title, stat value, stat label, art) for every Source page."""
    out = []
    for c in D.CATS:
        title = c["h1"].split(":")[0]
        v, l = c["stats"][0]
        out.append((c["slug"], "Source from Sri Lanka", title, v, l, c["art"]))
    s0 = D.HUB_STATS[0]
    out += [
        ("hub", "Source from Sri Lanka", "Sri Lankan exporters and export products", s0[0], s0[1], "s-exporters"),
        ("request-a-quote", "Source from Sri Lanka", "Request a quote from Sri Lankan exporters", "2 days", "to a reply with matched exporters", "s-rfq"),
        ("tender-radar", "For Sri Lankan exporters", "Tender Radar: international tenders on WhatsApp", "UN, World Bank", "and utility tenders matched to what you make", "s-radar"),
        ("bid-support", "For Sri Lankan exporters", "Tender bid support and export consultancy", "Go or no go", "then a compliant, complete bid", "s-bid"),
        ("for-exporters", "For Sri Lankan exporters", "Buyer requests, tenders and bids for exporters", "One desk", "for buyers, tenders and bids", "s-exporters"),
        ("how-to-import-from-sri-lanka", "Buyer's guide 2026", "How to import from Sri Lanka", "UK, EU, US", "duty access, documents, shipping and payment", "s-import"),
        ("sri-lanka-export-statistics", "Export statistics 2026", "Sri Lanka exports by product and by country", "US$17.25B", "exported in 2025, goods and services, up 5.6%", "s-stats"),
    ]
    extra = getattr(D, "OG_EXTRA", [])
    return out + list(extra)


def _b64(path, mime):
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()


def card(kicker, title, value, label, art):
    e = html.escape
    font = _b64(os.path.join(ROOT, "assets", "fonts", "manrope.woff2"), "font/woff2")
    logo = _b64(os.path.join(ROOT, "assets", "logo.png"), "image/png")
    svg = _b64(os.path.join(ROOT, "assets", "art", f"{art}.svg"), "image/svg+xml")
    size = 54 if len(title) <= 44 else 48 if len(title) <= 58 else 42
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: Manrope; src: url({font}) format("woff2"); font-weight: 200 800; }}
* {{ box-sizing: border-box; margin: 0; }}
body {{ width: 1200px; height: 630px; font-family: Manrope, sans-serif; background: #fff; position: relative; overflow: hidden; }}
.l {{ position: absolute; left: 0; top: 0; width: 660px; height: 616px; padding: 56px 52px 0 64px; display: flex; flex-direction: column; }}
.k {{ color: #b46f00; font-weight: 800; font-size: 20px; letter-spacing: .14em; text-transform: uppercase; }}
h1 {{ color: #0f1b33; font-weight: 800; font-size: {size}px; line-height: 1.08; letter-spacing: -.02em; margin-top: 22px; }}
.s {{ margin-top: 30px; padding-left: 18px; border-left: 5px solid #f7a600; display: flex; flex-direction: column; gap: 4px; }}
.v {{ color: #0b3c91; font-weight: 800; font-size: 40px; letter-spacing: -.01em; white-space: nowrap; }}
.sl {{ color: #36415a; font-size: 21px; font-weight: 600; line-height: 1.3; max-width: 520px; }}
.f {{ margin-top: auto; padding-bottom: 34px; display: flex; align-items: center; gap: 20px; }}
.f img {{ height: 64px; }}
.f span {{ color: #5d6880; font-size: 18px; font-weight: 700; }}
.r {{ position: absolute; right: 0; top: 0; width: 540px; height: 616px; background: url({svg}) center / cover no-repeat; }}
.bar {{ position: absolute; left: 0; bottom: 0; width: 1200px; height: 14px; background: #f7a600; }}
</style></head><body>
<div class="l"><div class="k">{e(kicker)}</div><h1>{e(title)}</h1>
<div class="s"><span class="v">{e(value)}</span><span class="sl">{e(label)}</span></div>
<div class="f"><img src="{logo}" alt=""><span>techdestinationsrilanka.lk/source</span></div></div>
<div class="r"></div><div class="bar"></div></body></html>"""


def main(only=None):
    from playwright.sync_api import sync_playwright
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        for name, kicker, title, value, label, art in pages():
            if only and name not in only:
                continue
            pg.set_content(card(kicker, title, value, label, art), wait_until="load")
            pg.wait_for_timeout(120)
            pg.screenshot(path=os.path.join(OUT, f"source-{name}.jpg"), type="jpeg", quality=84)
            print("og", name)
        b.close()


if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
