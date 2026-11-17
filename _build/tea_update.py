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


def quote_url(url):
    p = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((p.scheme, p.netloc, urllib.parse.quote(urllib.parse.unquote(p.path), safe="/"), p.query, ""))


def to_text(body, ctype, url):
    if body[:5] == b"%PDF-" or "pdf" in ctype.lower() or url.lower().endswith(".pdf"):
        import pdfplumber
        with pdfplumber.open(io.BytesIO(body)) as pdf:
            return "\n".join((p.extract_text() or "") for p in pdf.pages)
    t = body.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", t)
    return html.unescape(re.sub(r"<[^>]+>", " ", t))


def links(page_url, body):
    t = body.decode("utf-8", "replace")
    for href in re.findall(r'href\s*=\s*["\']([^"\']+)["\']', t, flags=re.I):
        yield urllib.parse.urljoin(page_url, html.unescape(href))


def candidates(year):
    """Every place the year's file might be, newest copies first where we can tell."""
    found = []
    for listing in (T.FW_STATS, T.FW_HOME + "statistics"):
        try:
            body, _ = get(listing)
        except Exception as ex:  # noqa: BLE001
            print(f"  listing not reachable: {listing} ({ex})")
            continue
        for u in links(listing, body):
            low = urllib.parse.unquote(u).lower()
            if str(year) in low and ("weekly tea auction quantities" in low or "weekly-tea-auction-quantities" in low):
                found.append(u)
    stamp = lambda u: int((re.search(r"_(\d{9,})\.pdf", urllib.parse.unquote(u)) or [0, 0])[1])  # noqa: E731
    found = sorted(set(found), key=stamp, reverse=True)
    found.append(f"https://www.forbestea.com/pdf/Weekly Tea Auction Quantities & Averages {year}.pdf")
    return list(dict.fromkeys(found))


def main():
    today = date.today()
    years = [today.year] + ([today.year - 1] if today.month <= 2 else [])
    old = T.load()
    fresh, report = [], {"run": datetime.now(timezone.utc).isoformat(timespec="seconds"), "sources": []}
    for year in years:
        for url in candidates(year):
            entry = {"url": url, "year": year}
            try:
                body, ctype = get(quote_url(url))
                rows, rejected = T.parse_text(to_text(body, ctype, url), year, url)
                entry.update(rows=len(rows), rejected=[r["sale_date"].isoformat() for r in rejected],
                             latest=max((r["sale_date"] for r in rows), default=None))
                fresh += rows
            except Exception as ex:  # noqa: BLE001
                entry["error"] = str(ex)[:200]
            if entry.get("latest"):
                entry["latest"] = entry["latest"].isoformat()
            report["sources"].append(entry)
            print(f"  {url}: {entry.get('rows', 0)} rows, latest {entry.get('latest')}, rejected {len(entry.get('rejected', []))} {entry.get('error', '')}")
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
        print("No rows could be read from any source. Check the broker's file names and formats.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
