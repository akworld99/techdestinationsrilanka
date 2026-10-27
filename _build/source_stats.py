"""Sri Lanka export statistics: 2025 and 2026 to date, by month, product and country.
All figures are US$ million from Export Development Board releases. Services values are EDB estimates; all figures are provisional.

MONTHLY UPDATE: this is the only file to edit when the EDB publishes a new month. Update the LATEST block, append the month to
MONTHLY, refresh TOTALS, SECTORS, SERVICES, LINES and MARKETS to the new year-to-date release, and rewrite DESC, ANSWER, STATS,
SHIFTS and FAQS. The hub, homepage, answers page, bar chart and llms.txt read their figures from here."""
from source_cats import M, EDB25, EDB9M, EDB9M_EDB

# ---------------------------------------------------------------- latest year-to-date release
PERIOD = "January to September 2026"          # the period the year-to-date columns cover
PERIOD_SHORT = "Jan to Sep 2026"
PERIOD_END = "2026-09-30"
YTD_URL = EDB9M_EDB                            # EDB release for that period
YTD_NEWS = EDB9M                               # a news report of the same release
YTD_NEWS_NAME = "Newswire"
YTD_PUBLISHED = "26 October 2026"
REVIEWED = "27 October 2026"                   # date of the last update to this page
MODIFIED = "2026-10-27"

# month, total, change, goods, change, services, change, source URL, note. As first published in each monthly release.
EDB_NEWS = "https://www.srilankabusiness.com/news/"
MONTHLY = [
    ("January 2026", 1532.60, "+13.71%", 1165.02, "+10.66%", 367.55, "+24.59%", EDB_NEWS + "robust-export-performance-signals-positive-outlook-for-2026.html", ""),
    ("February 2026", 1401.78, "+4.22%", 1066.88, "+1.32%", 334.90, "+14.68%", EDB_NEWS + "sri-lankas-exports-record-steady-growth-in-february-2026.html", ""),
    ("March 2026", 1467.31, f"{M}5.20%", 1180.39, f"{M}4.94%", 286.92, f"{M}6.26%", EDB_NEWS + "sri-lankas-export-performance-remains-steady-with-strong-q1-2026-growth.html", ""),
    ("April 2026", 1380.93, "+6%", 1063.77, "+9.87%", 317.16, None, EDB_NEWS + "sri-lankas-exports-surpass-us-5-7-billion-in-first-four-months-of-2026-despite-the-challenging-global-economic-conditions.html", ""),
    ("May 2026", 1570.64, "+18.34%", 1223.49, "+18.25%", 347.15, "+18.67%", EDB_NEWS + "sri-lankas-exports-exceeds-usd-7.3-billion-in-first-five-months-of-2026-signaling-strong-external-sector-recovery.html", ""),
    ("June 2026", 1658.62, "+12.53%", 1314.10, "+15.09%", 344.52, "+3.75%", EDB_NEWS + "sri-lanka-s-exports-cross-us-9-billion-milestone-in-the-first-half-of-2026-reflecting-sustained-growth-momentum.html", ""),
    ("July 2026", 1637.26, "+2.63%", 1285.31, f"{M}1.30%", 351.92, "+3.75%", EDB_NEWS + "sri-lankas-exports-surpass-us-10-billion-in-first-seven-months-of-2026-maintaining-positive-growth-momentum.html", ""),
    ("August 2026", 1601.36, "+1.77%", 1269.49, f"{M}1.00%", 331.87, "+13.97%", EDB_NEWS + "sri-lankas-exports-surpass-us-12-bn-in-first-eight-months-of-2026.html", ""),
    ("September 2026", 1690.00, "+17.23%", 1390.00, "+21.66%", 306.17, "+0.67%", EDB9M_EDB, "total and goods rounded to US$10 million in the release"),
]

GEMS_URL = "https://www.srilankabusiness.com/gem-diamond-and-jewellery/"

TITLE = "Sri Lanka exports 2026: by month, product and country"
H1 = "Sri Lanka export statistics: 2025 and 2026, by month, product and country"
DESC = ("Sri Lanka exported US$17.25B in 2025 and US$13.61B in January to September 2026. Exports by month, product and country, "
        "with sources and a CSV.")
ANSWER = ("Sri Lanka exported US$17.25 billion of goods and services in 2025, up 5.6%: US$13.58 billion of goods and US$3.67 billion of services. "
          "From January to September 2026 exports reached US$13.61 billion, up 5.04%, with goods at US$10.76 billion, up 5.35%. "
          "The largest export is apparel and textiles, at US$4.91 billion in 2025, followed by tea, coconut products and rubber products. "
          "The fastest growing in 2026 are electrical and electronic components, up 61%, and spices and essential oils, up 30.5%. "
          "The United States is the largest market, taking more than a fifth of goods exports, followed by India and the United Kingdom.")

STATS = [("US$17.25B", "total exports in 2025, up 5.6%"), ("US$13.61B", "January to September 2026, up 5.04%"),
         ("US$4.91B", "apparel and textiles, the largest export, 2025"), ("+61%", "electrical and electronic components, January to September 2026")]

# label, 2025 value, 2025 change, Jan to Sep 2026 value, Jan to Sep 2026 change
TOTALS = [
    ("Total exports, goods and services", 17252.15, "+5.60%", 13612.55, "+5.04%"),
    ("Merchandise (goods)", 13579.38, "+6.32%", 10761.92, "+5.35%"),
    ("Services (EDB estimate)", 3672.77, "+2.79%", 2850.63, "+3.88%"),
]

# label, link inside /source/ (or a root path starting with ../), 2025 value, 2025 change, Jan to Sep 2026 value, Jan to Sep 2026 change
SECTORS = [
    ("Apparel and textiles", "apparel-manufacturing/", 4909.05, "+5.34%", 3783.76, f"{M}5.68%"),
    ("Tea", "ceylon-tea/", 1507.19, "+4.97%", 1083.58, f"{M}6.83%"),
    ("Coconut and coconut based products", "coconut-products/", 1233.01, "+42.66%", 942.50, "+3.68%"),
    ("Rubber and rubber products", "industrial-tyres/", 945.73, f"{M}5.56%", 773.88, "+8.44%"),
    ("Food and beverages", "processed-food-beverages/", 583.89, "+24.23%", 526.31, "+20.90%"),
    ("Electrical and electronic components", "electrical-cables-transformers/", 438.49, "+3.91%", 508.86, "+61.05%"),
    ("Spices, essential oils and oleoresins", "spices-essential-oils/", 449.90, f"{M}2.59%", 430.53, "+30.53%"),
    ("Gems, diamonds and jewellery", "gems-jewellery/", 334.13, None, None, None),
    ("Seafood", "seafood/", 240.19, "+3.09%", 180.81, f"{M}2.03%"),
    ("Ornamental fish", "ornamental-fish/", 22.60, f"{M}7.60%", None, f"{M}26.71%"),
]
SERVICES = [
    ("Logistics and transport services", None, 1851.58, "+3.22%", None, None),
    ("ICT and BPM services", "../offshoring/", 1644.83, "+8.81%", 1240.67, "+3.69%"),
]

# product line, link, Jan to Sep 2026 value (or None), Jan to Sep 2026 change
LINES = [
    ("Boilers, piston engines, pumps and vacuum pumps", "light-engineering/", None, "+508.71%"),
    ("Coconut husk chips", "coco-peat-coir/", None, "+334.15%"),
    ("Telephone sets and audio and video equipment", "electrical-cables-transformers/", None, "+234.82%"),
    ("Insulated wires and cables", "electrical-cables-transformers/", None, "+82.59%"),
    ("Pepper", "spices-essential-oils/", 136.26, "+61.45%"),
    ("Tea bags", "ceylon-tea/", None, "+53.39%"),
    ("Non-alcoholic beverages", "processed-food-beverages/", None, "+46.78%"),
    ("Coconut shell based products", "activated-carbon/", None, "+45.91%"),
    ("Activated carbon", "activated-carbon/", None, "+37.79%"),
    ("Processed food", "processed-food-beverages/", 243.28, "+34.19%"),
    ("Electrical transformers", "electrical-cables-transformers/", None, "+33.46%"),
    ("Switches, boards and panels", "electrical-cables-transformers/", None, "+31.49%"),
    ("Cinnamon", "ceylon-cinnamon/", 221.56, "+31.03%"),
    ("Oleoresins", "spices-essential-oils/", None, "+30.09%"),
    ("Gaskets, washers and seals", "rubber-gloves/", None, "+27.78%"),
    ("Essential oils", "spices-essential-oils/", None, "+22.17%"),
    ("Animal feed", "processed-food-beverages/", None, "+13.69%"),
    ("Instant tea", "ceylon-tea/", None, "+9.85%"),
    ("Industrial and surgical gloves", "rubber-gloves/", None, "+7.58%"),
    ("Apparel", "apparel-manufacturing/", 3513.37, f"{M}5.36%"),
    ("Bulk tea", "ceylon-tea/", None, f"{M}11.13%"),
]

# market, 2025 value, 2025 change, Jan to Sep 2026 value, Jan to Sep 2026 change
MARKETS = [
    ("United States", 2999.15, "+3.06%", 2252.99, "+0.05%"),
    ("India", 1035.72, "+17.21%", 889.84, "+12.30%"),
    ("United Kingdom", 929.03, "+2.80%", 654.36, f"{M}9.33%"),
    ("Italy", 679.77, "+14.16%", 514.28, "+1.48%"),
    ("Germany", 706.49, "+12.45%", 513.08, f"{M}4.27%"),
    ("Netherlands", 474.80, "+20.63%", 328.12, f"{M}5.35%"),
    ("China", None, None, 234.39, "+16.46%"),
    ("United Arab Emirates", 341.06, None, 232.06, f"{M}10.50%"),
    ("Türkiye", None, None, 218.24, "+94.01%"),
    ("France", 277.18, "+5.09%", 198.77, f"{M}6.54%"),
    ("Belgium", 254.44, "+6.42%", 193.42, "+3.16%"),
    ("Australia", 262.00, None, None, None),
    ("Pakistan", None, f"{M}2.03%", 74.73, "+33.59%"),
    ("European Union, all members", None, "+13.41%", None, f"{M}0.15%"),
]

SHIFTS = [
    ("Electrical and electronic components rose 61.05% to US$508.86 million, led by insulated wires and cables, up 82.59%, and transformers, up 33.46%.", "EDB, January to September 2026", EDB9M),
    ("Spices and essential oils rose 30.53%: pepper up 61.45% to US$136.26 million and cinnamon up 31.03% to US$221.56 million.", "EDB, January to September 2026", EDB9M),
    ("Food and beverages rose 20.90%, with processed food up 34.19% and non-alcoholic beverages up 46.78%.", "EDB, January to September 2026", EDB9M),
    ("Tea fell 6.83% overall, but tea bags rose 53.39% and tea exports to Türkiye rose 126.51%.", "EDB, January to September 2026", EDB9M),
    ("Activated carbon exports to China rose 78.33%.", "EDB, January to September 2026", EDB9M),
    ("Apparel and textiles fell 5.68%, and apparel alone 5.36%, with apparel to the US down 3.83%, the EU down 5.54% and the UK down 10.41%.", "EDB, January to September 2026", EDB9M),
    ("September 2026 alone was strong: goods exports rose 21.66% to US$1.39 billion.", "EDB, September 2026", EDB9M),
]

SRC = (f'Source: Export Development Board, <a href="{EDB25}" rel="noopener">2025 export performance</a> (published January 2026) and '
       f'<a href="{YTD_URL}" rel="noopener">{PERIOD}</a> (also reported by <a href="{YTD_NEWS}" rel="noopener">{YTD_NEWS_NAME}</a>, {YTD_PUBLISHED}); '
       f'gems 2025 value from the <a href="{GEMS_URL}" rel="noopener">EDB gem sector page</a>; 2025 values for Australia and the UAE from the EDB market briefs on '
       f'<a href="https://www.srilankabusiness.com/pdfs/market-profiles/2026/australia-2026.pdf" rel="noopener">Australia</a> and <a href="https://www.srilankabusiness.com/pdfs/market-profiles/2026/uae-2026.pdf" rel="noopener">the UAE</a>. Provisional figures; services are EDB estimates. '
       "A dash means the release did not give that figure.")

FAQS = [
    ("What are Sri Lanka's main exports?",
     "Apparel and textiles (US$4.91 billion in 2025), tea (US$1.51 billion), coconut products (US$1.23 billion), rubber products (US$946 million), "
     "food and beverages (US$584 million), spices and essential oils (US$450 million), electrical and electronic components (US$438 million), "
     "gems and jewellery and seafood. In services, logistics brought in US$1.85 billion and IT and business process services US$1.64 billion."),
    ("What is Sri Lanka's most famous export?",
     "Tea, sold as Ceylon tea, which earned US$1.51 billion in 2025. By value apparel and textiles earn more, at US$4.91 billion. "
     "Sri Lanka is also known for Ceylon cinnamon, blue sapphires and coconut products."),
    ("How much did Sri Lanka export in 2025?",
     "US$17.25 billion of goods and services, up 5.6% on 2024. Goods were US$13.58 billion, up 6.32%, and services US$3.67 billion, up 2.79%, according to the Export Development Board."),
    ("What is Sri Lanka's export income in 2026?",
     "From January to September 2026 Sri Lanka earned US$13.61 billion from exports, up 5.04% on the same months of 2025. Goods were US$10.76 billion, up 5.35%, and services an estimated US$2.85 billion, up 3.88%."),
    ("Which countries buy the most from Sri Lanka?",
     "The United States, at US$3.0 billion in 2025 and more than a fifth of goods exports, then India (US$1.04 billion), the United Kingdom (US$929 million), Germany, Italy and the Netherlands. "
     "In January to September 2026 China, the UAE and Türkiye each took more than US$200 million, and Türkiye grew fastest, up 94%."),
    ("Which Sri Lankan exports are growing fastest?",
     "In January to September 2026: electrical and electronic components, up 61.05%, spices and essential oils, up 30.53%, and food and beverages, up 20.90%. "
     "Within those, pepper rose 61%, insulated cables 83% and processed food 34%."),
    ("Where do these figures come from?",
     "From the Export Development Board's monthly export releases, linked on this page. They are provisional and can be revised, and the services figures are estimates."),
]


def csv_rows():
    """Rows for data/sri-lanka-exports-2025-2026.csv."""
    out = [("table", "item", "value_2025_usd_m", "change_2025", "value_2026_ytd_usd_m", "change_2026_ytd", "source", "ytd_period")]
    fmt = lambda v: "" if v is None else f"{v:.2f}"
    ch = lambda c: "" if c is None else c.replace(M, "-")
    for lbl, v1, c1, v2, c2 in TOTALS:
        out.append(("total", lbl, fmt(v1), ch(c1), fmt(v2), ch(c2), "EDB", PERIOD))
    for lbl, _, v1, c1, v2, c2 in SECTORS + SERVICES:
        out.append(("sector", lbl, fmt(v1), ch(c1), fmt(v2), ch(c2), "EDB" + (" gem sector page" if lbl.startswith("Gems") else ""), PERIOD))
    for lbl, _, v2, c2 in LINES:
        out.append(("product_line", lbl, "", "", fmt(v2), ch(c2), "EDB", PERIOD))
    for lbl, v1, c1, v2, c2 in MARKETS:
        out.append(("market", lbl, fmt(v1), ch(c1), fmt(v2), ch(c2), "EDB", PERIOD))
    for mo, t, tc, g, gc, sv, sc, _, _ in MONTHLY:
        out.append(("month_total", mo, "", "", fmt(t), ch(tc), "EDB monthly release", mo))
        out.append(("month_goods", mo, "", "", fmt(g), ch(gc), "EDB monthly release", mo))
        out.append(("month_services", mo, "", "", fmt(sv), ch(sc), "EDB monthly release", mo))
    return out


# ---------------------------------------------------------------- derived figures used across the site
def _num(c):
    return float(c.replace(M, "-").rstrip("%")) if c else None


def pct(c):
    """'+61.05%' -> '61%', '+30.53%' -> '30.5%' (magnitude only)."""
    v = abs(_num(c))
    return (f"{v:.0f}" if v >= 50 else f"{v:.1f}".rstrip("0").rstrip(".")) + "%"


def updown(c):
    return ("up " if _num(c) >= 0 else "down ") + c.lstrip("+").lstrip(M)


SHORT = {"Spices, essential oils and oleoresins": "spices and essential oils", "Coconut and coconut based products": "coconut products"}


def lc(label):
    return SHORT.get(label, label[0].lower() + label[1:])


def leaders(n=2):
    rows = sorted([r for r in SECTORS if r[5]], key=lambda r: _num(r[5]), reverse=True)[:n]
    return rows


def leaders_text(n=2):
    rows = leaders(n)
    parts = [f"{lc(r[0])}, up {pct(r[5])}" for r in rows]
    return ", ".join(parts[:-1]) + ", and " + parts[-1]


def goods_ytd():
    return TOTALS[1][3], TOTALS[1][4]


def total_ytd():
    return TOTALS[0][3], TOTALS[0][4]


def line(label):
    return next((r for r in LINES if r[0] == label), None)


def bn(v):
    return f"US${v / 1000:.2f}B"


def latest_month():
    return MONTHLY[-1]
