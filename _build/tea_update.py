#!/usr/bin/env python3
"""Fetch the latest Colombo tea auction figures and add new sales to _build/tea/weekly.csv.

Run from the repo root:   python3 _build/tea_update.py
Needs network access and pdfplumber (pip install pdfplumber). The GitHub Action in .github/workflows/tea-prices.yml runs
it every week, rebuilds the site when a sale is added, and commits the result.

Where the figures come from: Forbes & Walker Tea Brokers publish "Weekly Tea Auction Quantities & Averages <year>" as a
PDF and as a table on their statistics site, and upload a fresh copy (with a new file name) as the year goes on. This
script reads the statistics listing to find the newest copies, falls back to the plain file name, parses every copy it
finds, and keeps only rows that pass tea_data.check(). Nothing is deleted: a sale already stored stays unless the broker
publishes a different figure for the same date, which replaces it.
"""
import html
import io
import json
import re
import sys
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import tea_data as T  # noqa: E402

UA = "Mozilla/5.0 (compatible; TechDestinationSriLanka/1.0; +https://techdestinationsrilanka.lk/source/ceylon-tea/auction-prices/)"
STATUS = HERE / "tea" / "last_update.json"


def get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read(), r.headers.get("Content-Type", "")


def quote_url(url, keep="/&"):
    p = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((p.scheme, p.netloc, urllib.parse.quote(urllib.parse.unquote(p.path), safe=keep), p.query, ""))


def fetch(url):
    """Get a page or file, trying the browser's spelling of the path first and the fully encoded one second."""
    last = None
    for keep in ("/&", "/"):
        try:
            return get(quote_url(url, keep))
        except Exception as ex:  # noqa: BLE001
            last = ex
    raise last


def to_text(body, ctype, url):
    if body[:5] == b"%PDF-" or "pdf" in ctype.lower() or url.lower().endswith(".pdf"):
        import pdfplumber
        try:
            with pdfplumber.open(io.BytesIO(body)) as pdf:
                return "\n".join((p.extract_text() or "") for p in pdf.pages)
        except Exception as ex:  # noqa: BLE001  a page served under a .pdf name that is not a PDF
            print(f"    not a readable PDF ({ex}); reading it as text")
    t = body.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", t)
    return html.unescape(re.sub(r"<[^>]+>", " ", t))


def links(page_url, body):
    t = body.decode("utf-8", "replace")
    for href in re.findall(r'href\s*=\s*["\']([^"\']+)["\']', t, flags=re.I):
        yield urllib.parse.urljoin(page_url, html.unescape(href))


def _is_weekly_file(u):
    low = urllib.parse.unquote(u).lower().replace("&amp;", "&")
    return ("quantities" in low and "averages" in low) or "weekly-tea-auction-quantities-averages/" in low


def _is_pdf(u):
    return urllib.parse.urlsplit(u).path.lower().endswith(".pdf")


def _norm(u):
    return urllib.parse.urldefrag(u)[0]


def _stamp(u):
    m = re.search(r"_(\d{9,})\.pdf", urllib.parse.unquote(u))
    return int(m.group(1)) if m else 0


def crawl(years, max_fetches=24):
    """Read the broker's listing pages, then every page or PDF that looks like the weekly quantities and averages,
    one level deep. Returns (url, text) for everything read, and logs what each page offered."""
    queue = [(u, 0) for u in (T.FW_REPORTS, T.FW_STATS, T.FW_HOME)]
    queue += [(f"https://www.forbestea.com/pdf/Weekly Tea Auction Quantities & Averages {y}.pdf", 2) for y in years]
    seen, out, fetches = set(), [], 0
    while queue and fetches < max_fetches:
        url, depth = queue.pop(0)
        url = _norm(url)
        if url in seen:
            continue
        seen.add(url)
        fetches += 1
        try:
            body, ctype = fetch(url)
        except Exception as ex:  # noqa: BLE001
            print(f"  not reachable: {urllib.parse.unquote(url)} ({ex})")
            continue
        text = to_text(body, ctype, url)
        out.append((url, text))
        if _is_pdf(url) or body[:5] == b"%PDF-":
            continue
        found = [_norm(u) for u in links(url, body)]
        nxt = [u for u in dict.fromkeys(found) if u not in seen and (_is_weekly_file(u) or (_is_pdf(u) and any(str(y) in urllib.parse.unquote(u) for y in years)
                                                                                           and re.search(r"quantit|averag", urllib.parse.unquote(u), re.I)))]
        nxt.sort(key=lambda u: (_is_pdf(u), any(str(y) in urllib.parse.unquote(u) for y in years), _stamp(u)), reverse=True)
        pdfs = [u for u in dict.fromkeys(found) if _is_pdf(u)]
        sample = re.sub(r"\s+", " ", text)[:240]
        print(f"  page {urllib.parse.unquote(url)}: {len(pdfs)} PDF links, {len(nxt)} to follow. Text starts: {sample}")
        for u in pdfs[:25]:
            print(f"    pdf: {urllib.parse.unquote(u)}")
        if depth < 2:
            queue += [(u, depth + 1) for u in nxt[:10]]
    return out


def main():
    today = date.today()
    years = [today.year] + ([today.year - 1] if today.month <= 2 else [])
    old = T.load()
    fresh, report = [], {"run": datetime.now(timezone.utc).isoformat(timespec="seconds"), "sources": []}
    for url, text in crawl(years):
        rows, rejected = T.parse_text(text, url)
        rows = [r for r in rows if r["sale_date"].year >= today.year - 1]
        latest = max((r["sale_date"] for r in rows), default=None)
        report["sources"].append({"url": url, "rows": len(rows), "rejected": [r["sale_date"].isoformat() for r in rejected],
                                  "latest": latest.isoformat() if latest else None})
        if rows or rejected:
            print(f"  rows from {urllib.parse.unquote(url)}: {len(rows)}, latest {latest}, rejected {len(rejected)}")
        fresh += rows
    # Several copies of the same file: for each date keep the row from the copy that runs furthest into the year.
    reach = {s["url"]: s.get("latest") or "" for s in report["sources"]}
    best = {}
    for r in sorted(fresh, key=lambda r: reach.get(r["source"], "")):
        best[r["sale_date"]] = r
    fresh = [best[d] for d in sorted(best)]
    rows, added, changed = T.merge(old, fresh)
    report.update(parsed=len(fresh), added=[r["sale_date"].isoformat() for r in added], changed=[r["sale_date"].isoformat() for r in changed],
                  latest_sale=rows[-1]["sale_date"].isoformat(), total_sales=len(rows))
    if added or changed:
        T.save(rows)
    STATUS.write_text(json.dumps(report, indent=1) + "\n")
    print(f"Parsed {len(fresh)} rows. Added {len(added)}, changed {len(changed)}. Latest sale {rows[-1]['sale_date']}.")
    if not fresh:
        print("No rows could be read from any source. The pages and PDF links listed above show what the broker's site offered.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
