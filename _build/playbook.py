"""Builds the playbook PDF from the published guides. Run after build.py: python3 _build/playbook.py (needs Playwright)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ["guides/sri-lanka-tech-salaries", "guides/how-to-hire-in-sri-lanka", "guides/employer-of-record-sri-lanka", "guides/set-up-a-company-in-sri-lanka", "guides/sri-lanka-tech-industry-facts"]
SITE = "https://techdestinationsrilanka.lk"


def main():
    parts = []
    for p in PAGES:
        h = (ROOT / p / "index.html").read_text(encoding="utf-8")
        m = re.search(r'<main id="main">(.*?)</main>', h, re.S).group(1)
        m = re.sub(r"<form.*?</form>", "", m, flags=re.S)
        m = re.sub(r'<div class="reach.*?</div></div>', "", m, flags=re.S)
        m = re.sub(r'<nav class="crumbs.*?</nav>', "", m, flags=re.S)
        m = re.sub(r'href="(\.\./)+', f'href="{SITE}/', m)
        m = re.sub(r'href="\.\./', f'href="{SITE}/guides/', m)
        parts.append(f'<article class="chapter">{m}</article>')
    css = (ROOT / "assets/styles.css").read_text(encoding="utf-8").replace("url(fonts/", f"url({(ROOT / 'assets/fonts').as_uri()}/")
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>The Sri Lanka tech team playbook 2026</title><style>{css}
@page {{ size: A4; margin: 16mm 14mm; }}
body {{ font-size: 14px; background: #fff; }}
.cover {{ height: 255mm; display: flex; flex-direction: column; justify-content: center; background: #07245c; color: #fff; padding: 22mm; border-radius: 6mm; page-break-after: always; }}
.cover p.k {{ color: #f7a600; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; font-size: 13px; }}
.cover h1 {{ font-size: 46px; line-height: 1.05; margin: 14px 0 18px; color: #fff; }}
.cover p {{ font-size: 17px; max-width: 130mm; color: #dbe5fb; }}
.cover .by {{ margin-top: auto; font-size: 14px; }}
.cover a {{ color: #fff; }}
.chapter {{ page-break-before: always; }}
.chapter .page-head {{ padding: 0 0 8px; background: none; }}
.chapter .section {{ padding: 8px 0; }}
.chapter .wrap {{ max-width: none; padding: 0; }}
.chapter h1 {{ font-size: 28px; }}
.tbl {{ overflow: visible; }} table {{ font-size: 12px; }} tr, .fact, li {{ page-break-inside: avoid; }}
.cite {{ display: none; }}
.end {{ page-break-before: always; padding-top: 40mm; }}
</style></head><body>
<section class="cover"><p class="k">Tech Destination Sri Lanka</p><h1>The Sri Lanka tech team playbook 2026</h1>
<p>Salaries, hiring routes, employer of record, company setup, tax and the industry numbers. Everything a founder or CTO needs before building a team in Sri Lanka, with a source for every figure.</p>
<p class="by">Last reviewed October 2026 · <a href="{SITE}/">techdestinationsrilanka.lk</a><br>General information, not legal or tax advice.</p></section>
{''.join(parts)}
<section class="end"><h1>Ready to build your team?</h1><p class="body-l">We introduce Sri Lankan engineers, partner companies and advisers who fit what you are building.</p>
<p class="body-l"><strong>Schedule a call:</strong> <a href="https://calendly.com/digisavvyteams/30min">calendly.com/digisavvyteams/30min</a><br><strong>Email:</strong> techdestinationsrilanka@gmail.com<br><strong>Find talent:</strong> <a href="{SITE}/talent/find/">{SITE}/talent/find/</a><br><strong>Estimate a team:</strong> <a href="{SITE}/tools/team-cost-calculator/">{SITE}/tools/team-cost-calculator/</a></p></section>
</body></html>"""
    tmp = ROOT / "_build" / "_playbook.html"
    tmp.write_text(doc, encoding="utf-8")
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page()
        pg.goto(tmp.as_uri())
        pg.pdf(path=str(ROOT / "assets/sri-lanka-tech-team-playbook-2026.pdf"), format="A4", print_background=True)
        b.close()
    tmp.unlink()


if __name__ == "__main__":
    main()
