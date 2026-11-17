"""Colombo tea auction data: weekly quantities and average prices by elevation.

The figures come from Forbes & Walker Tea Brokers' "Weekly Tea Auction Quantities & Averages" file, one per year.
_build/tea/weekly.csv holds every sale we have; _build/tea_update.py adds new sales each week and the page builder
(_build/seo_tea.py) reads from here. Every row is checked before it is stored: the three elevations must add up to the
total quantity, and their quantity weighted average must match the total average.
"""
import csv
import re
from collections import OrderedDict
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSV = HERE / "tea" / "weekly.csv"
FIELDS = ["sale_date", "qty_high", "qty_medium", "qty_low", "qty_total", "avg_high", "avg_medium", "avg_low", "avg_total", "source"]
ELEV = [("high", "High Grown"), ("medium", "Medium Grown"), ("low", "Low Grown")]

FW_HOME = "https://www.forbestea.com/"
FW_REPORTS = "https://www.forbestea.com/statistics-tea-market-reports"
FW_STATS = "https://web.forbestea.com/statistics/sri-lankan-statistics/90-weekly-tea-auction-quantities-averages"
TRI_FORMULA = "https://dl.nsf.gov.lk/bitstreams/c8413e7e-337e-408d-839e-6ce5c0073cf0/download"
TEA_BOARD = "https://www.srilankateaboard.lk/"

MONTHS = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "MAT": 5, "JUN": 6, "JUNE": 6, "JUL": 7, "JULY": 7, "AUG": 8,
          "SEP": 9, "SEPT": 9, "OCT": 10, "NOV": 11, "DEC": 12}
MONTH_NAMES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# A sale row as printed in the broker's file, in PDF text or in the HTML table once tags are stripped:
# 07-JAN-2026 843 810 3,099 4,752 1145.14 994.84 1243.94 1183.95
ROW_RE = re.compile(
    r"(\d{1,2})\s*-\s*([A-Za-z]{3,5})\s*-\s*(\d{4})"
    r"\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)"
    r"\s+([\d,]+\.\d+)\s+([\d,]+\.\d+)\s+([\d,]+\.\d+)\s+([\d,]+\.\d+)")


def _num(s):
    return float(s.replace(",", ""))


def check(r):
    """True when a row is internally consistent. Quantities are in thousands of kg, rounded, so allow a little slack."""
    q = [r["qty_high"], r["qty_medium"], r["qty_low"]]
    a = [r["avg_high"], r["avg_medium"], r["avg_low"]]
    if not (500 <= r["qty_total"] <= 15000) or not all(200 <= x <= 5000 for x in a + [r["avg_total"]]):
        return False
    if abs(sum(q) - r["qty_total"]) > 2:
        return False
    weighted = sum(x * y for x, y in zip(q, a)) / r["qty_total"]
    return abs(weighted - r["avg_total"]) <= 1.0


def parse_text(text, source, year=None):
    """Find sale rows in text extracted from the broker's PDF or HTML page. Each file covers one year, so the year
    most rows print is the file's year, and a row printing a neighbouring year is a typo: the broker printed
    01-JUL-2027 in the 2026 file. Pass `year` to force the file's year when it is known."""
    found = []
    for m in ROW_RE.finditer(text):
        mon = m.group(2).upper()
        if mon in MONTHS:
            found.append((int(m.group(1)), MONTHS[mon], int(m.group(3)), m))
    if not found:
        return [], []
    if year is None:
        years = [y for _, _, y, _ in found]
        year = max(set(years), key=years.count)
    rows, rejected = [], []
    for d, mon, y, m in found:
        if abs(y - year) > 1:
            continue
        try:
            sale = date(year, mon, d)
        except ValueError:
            continue
        r = {"sale_date": sale, "qty_high": _num(m.group(4)), "qty_medium": _num(m.group(5)), "qty_low": _num(m.group(6)),
             "qty_total": _num(m.group(7)), "avg_high": _num(m.group(8)), "avg_medium": _num(m.group(9)), "avg_low": _num(m.group(10)),
             "avg_total": _num(m.group(11)), "source": source}
        (rows if check(r) else rejected).append(r)
    return rows, rejected


def load():
    rows = []
    with open(CSV, newline="", encoding="utf-8") as f:
        for x in csv.DictReader(f):
            r = {k: (float(v) if k not in ("sale_date", "source") else v) for k, v in x.items()}
            r["sale_date"] = date.fromisoformat(x["sale_date"])
            rows.append(r)
    rows.sort(key=lambda r: r["sale_date"])
    return rows


def save(rows):
    rows = sorted(rows, key=lambda r: r["sale_date"])
    with open(CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(FIELDS)
        for r in rows:
            w.writerow([r["sale_date"].isoformat()] + [int(r[k]) for k in FIELDS[1:5]] + [f"{r[k]:.2f}" for k in FIELDS[5:9]] + [r["source"]])


def merge(old, new, keep_existing=False):
    """Add sales we do not have yet. A stored sale that differs in the new data is listed in `changed`, and replaced
    only when keep_existing is False: reading a PDF can shift figures onto the wrong date while every row still adds
    up, so the updater keeps stored sales and leaves revisions for a person to check. Returns rows, added, changed."""
    by_date = OrderedDict((r["sale_date"], r) for r in old)
    added, changed = [], []
    for r in new:
        prev = by_date.get(r["sale_date"])
        if prev is None:
            added.append(r)
        elif any(abs(prev[k] - r[k]) > 0.005 for k in FIELDS[1:9]):
            changed.append(r)
            if keep_existing:
                continue
        else:
            continue
        by_date[r["sale_date"]] = r
    return list(by_date.values()), added, changed


def misaligned(rows):
    """Dates whose figures repeat another date's exactly: a sign the PDF's date column and number columns were read
    out of line. Two real sales never match on all eight figures."""
    seen, dupes = {}, []
    for r in rows:
        key = tuple(r[k] for k in FIELDS[1:9])
        if key in seen and seen[key] != r["sale_date"]:
            dupes.append(r["sale_date"])
        seen.setdefault(key, r["sale_date"])
    return dupes


# ------------------------------------------------------------------ summaries for the pages
def wavg(rows, k):
    q = sum(r[f"qty_{k}"] for r in rows)
    return sum(r[f"qty_{k}"] * r[f"avg_{k}"] for r in rows) / q if q else None


def monthly(rows):
    """Quantity weighted average per elevation for each month's sales, keyed (year, month)."""
    out = OrderedDict()
    for r in rows:
        out.setdefault((r["sale_date"].year, r["sale_date"].month), []).append(r)
    return OrderedDict((k, {"sales": len(v), "qty": sum(r["qty_total"] for r in v), **{e: wavg(v, e) for e in ("high", "medium", "low", "total")}})
                       for k, v in out.items())


def year_to_date(rows, year, until):
    """Weighted averages for a year's sales up to the same day and month as `until`."""
    sel = [r for r in rows if r["sale_date"].year == year and (r["sale_date"].month, r["sale_date"].day) <= (until.month, until.day)]
    return {e: wavg(sel, e) for e in ("high", "medium", "low", "total")} | {"sales": len(sel), "qty": sum(r["qty_total"] for r in sel)}


def pct(a, b):
    return (a / b - 1) * 100 if a and b else None


def summary(rows):
    last, prev = rows[-1], rows[-2]
    y = last["sale_date"].year
    ytd, ytd_prev = year_to_date(rows, y, last["sale_date"]), year_to_date(rows, y - 1, last["sale_date"])
    this_year = [r for r in rows if r["sale_date"].year == y]
    low_share = sum(r["qty_low"] for r in this_year) / sum(r["qty_total"] for r in this_year) * 100
    return {"last": last, "prev": prev, "year": y, "ytd": ytd, "ytd_prev": ytd_prev, "low_share": low_share,
            "top": max(ELEV, key=lambda x: last[f"avg_{x[0]}"]), "bottom": min(ELEV, key=lambda x: last[f"avg_{x[0]}"]),
            "chg_prev": pct(last["avg_total"], prev["avg_total"]), "chg_ytd": pct(ytd["total"], ytd_prev["total"])}


def fdate(d):
    return f"{d.day} {MONTH_NAMES[d.month - 1]} {d.year}"


def rs(v, dp=2):
    return f"Rs {v:,.{dp}f}"


def signed(v, dp=1, unit="%"):
    if v is None:
        return "–"
    s = f"{abs(v):.{dp}f}{unit}"
    return ("+" if v > 0 else "−" if v < 0 else "") + s


# ------------------------------------------------------------------ more summaries for the month, year and elevation pages
LEAF_SHARE, LEAF_EXCESS, OUTTURN = 0.68, 0.50, 0.2222   # green leaf formula as documented by the Tea Research Institute (2003)


def leaf_rate(nsa, ea=None):
    """Green leaf rate per kg of leaf for a factory net sale average `nsa`, against elevation average `ea` (defaults to nsa)."""
    ea = nsa if ea is None else ea
    made = LEAF_SHARE * nsa if nsa <= ea else LEAF_SHARE * ea + LEAF_EXCESS * (nsa - ea)
    return made * OUTTURN


def month_slug(y, m):
    return f"{MONTH_NAMES[m - 1].lower()}-{y}"


def range_52w(rows, k):
    """Highest and lowest weekly average for elevation k over the 52 weeks to the latest sale: (hi, hi_date, lo, lo_date)."""
    last = rows[-1]["sale_date"]
    sel = [r for r in rows if (last - r["sale_date"]).days < 364]
    hi = max(sel, key=lambda r: r[f"avg_{k}"])
    lo = min(sel, key=lambda r: r[f"avg_{k}"])
    return hi[f"avg_{k}"], hi["sale_date"], lo[f"avg_{k}"], lo["sale_date"]


def years(rows):
    return sorted({r["sale_date"].year for r in rows})
