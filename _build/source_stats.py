"""Sri Lanka export statistics: 2025 and 2026 to date, by month, product and country.
All figures are US$ million from Export Development Board releases. Services values are EDB estimates; all figures are provisional.

MONTHLY UPDATE: this is the only file to edit when the EDB publishes a new month. Update the LATEST block, append the month to
MONTHLY, refresh TOTALS, SECTORS, SERVICES, LINES and MARKETS to the new year-to-date release, and rewrite DESC, ANSWER, STATS,
SHIFTS and FAQS. The hub, homepage, answers page, bar chart and llms.txt read their figures from here."""
from source_cats import M, EDB25, EDB9M, EDB9M_EDB

# ---------------------------------------------------------------- latest year-to-date release
PERIOD = "January to October 2026"          # the period the year-to-date columns cover
PERIOD_SHORT = "Jan to Oct 2026"
PERIOD_END = "2026-10-31"
YTD_URL = ("https://www.srilankabusiness.com/news/"
           "sri-lankas-export-momentum-strengthens-reaching-us-15-3-bn-with-6-growth.html")  # EDB release for that period
YTD_NEWS = ("https://www.newswire.lk/2026/11/25/"
            "sri-lankas-export-earnings-rise-6-03-to-us-15-28-billion-in-first-10-months-of-2026/")  # a news report of the same release
YTD_NEWS_NAME = "Newswire"
YTD_PUBLISHED = "25 November 2026"
REVIEWED = "27 November 2026"                  # date of the last update to this page
MODIFIED = "2026-11-27"

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
    ("October 2026", 1620.00, "+11.57%", 1260.00, "+9.65%", 360.21, "+18.87%", YTD_URL, "total and goods rounded to US$10 million in the release"),
]

GEMS_URL = "https://www.srilankabusiness.com/gem-diamond-and-jewellery/"

TITLE = "Sri Lanka exports 2026: by month, product and country"
H1 = "Sri Lanka export statistics: 2025 and 2026, by month, product and country"
DESC = ("Sri Lanka exported US$17.25B in 2025 and US$15.28B in January to October 2026. Exports by month, product and country, "
        "with sources and a CSV.")
ANSWER = ("Sri Lanka exported US$17.25 billion of goods and services in 2025, up 5.6%: US$13.58 billion of goods and US$3.67 billion of services. "
          "From January to October 2026 exports reached US$15.28 billion, up 6.03%, with goods at US$12.01 billion, up 5.72%. "
          "The largest export is apparel and textiles, at US$4.91 billion in 2025, followed by tea, coconut products and rubber products. "
          "The fastest growing in 2026 are electrical and electronic components, up 59.6%, and spices and essential oils, up 35.4%. "
          "The United States is the largest market, taking more than a fifth of goods exports, followed by India and the United Kingdom.")

STATS = [("US$17.25B", "total exports in 2025, up 5.6%"), ("US$15.28B", "January to October 2026, up 6.03%"),
         ("US$4.91B", "apparel and textiles, the largest export, 2025"), ("+59.6%", "electrical and electronic components, January to October 2026")]

# label, 2025 value, 2025 change, Jan to Oct 2026 value, Jan to Oct 2026 change
TOTALS = [
    ("Total exports, goods and services", 17252.15, "+5.60%", 15281.57, "+6.03%"),
    ("Merchandise (goods)", 13579.38, "+6.32%", 12014.99, "+5.72%"),
    ("Services (EDB estimate)", 3672.77, "+2.79%", 3266.58, "+7.20%"),
]

# label, link inside /source/ (or a root path starting with ../), 2025 value, 2025 change, Jan to Oct 2026 value, Jan to Oct 2026 change
SECTORS = [
    ("Apparel and textiles", "apparel-manufacturing/", 4909.05, "+5.34%", 4196.56, f"{M}5.50%"),
    ("Tea", "ceylon-tea/", 1507.19, "+4.97%", 1202.26, f"{M}6.77%"),
    ("Coconut and coconut based products", "coconut-products/", 1233.01, "+42.66%", 1054.43, "+2.07%"),
    ("Rubber and rubber products", "industrial-tyres/", 945.73, f"{M}5.56%", 873.85, "+10.10%"),
    ("Food and beverages", "processed-food-beverages/", 583.89, "+24.23%", 594.52, "+18.93%"),
    ("Electrical and electronic components", "electrical-cables-transformers/", 438.49, "+3.91%", 566.14, "+59.60%"),
    ("Spices, essential oils and oleoresins", "spices-essential-oils/", 449.90, f"{M}2.59%", 498.43, "+35.35%"),
    ("Gems, diamonds and jewellery", "gems-jewellery/", 334.13, None, None, None),
    ("Seafood", "seafood/", 240.19, "+3.09%", 199.34, f"{M}0.29%"),
    ("Ornamental fish", "ornamental-fish/", 22.60, f"{M}7.60%", None, None),
]
SERVICES = [
    ("Logistics and transport services", None, 1851.58, "+3.22%", None, None),
    ("ICT and BPM services", "../offshoring/", 1644.83, "+8.81%", 1415.37, "+6.37%"),
]

# product line, link, Jan to Oct 2026 value (or None), Jan to Oct 2026 change
LINES = [
    ("Boilers, piston engines, pumps and vacuum pumps", "light-engineering/", None, "+520.54%"),
    ("Coconut husk chips", "coco-peat-coir/", 39.41, "+317.92%"),
    ("Telephone sets and audio and video equipment", "electrical-cables-transformers/", None, "+205.54%"),
    ("Meat, fish and dairy preparations", "processed-food-beverages/", 95.98, "+121.41%"),
    ("Insulated wires and cables", "electrical-cables-transformers/", None, "+82.65%"),
    ("Pepper", "spices-essential-oils/", 157.30, "+75.25%"),
    ("Tea bags", "ceylon-tea/", None, "+49.54%"),
    ("Non-alcoholic beverages", "processed-food-beverages/", None, None),
    ("Coconut shell based products", "activated-carbon/", 249.50, "+43.88%"),
    ("Activated carbon", "activated-carbon/", 223.08, "+36.38%"),
    ("Processed food", "processed-food-beverages/", 319.40, "+24.81%"),
    ("Electrical transformers", "electrical-cables-transformers/", None, "+36.19%"),
    ("Switches, boards and panels", "electrical-cables-transformers/", None, "+33.05%"),
    ("Cinnamon", "ceylon-cinnamon/", 256.64, "+31.57%"),
    ("Oleoresins", "spices-essential-oils/", None, "+52.79%"),
    ("Gaskets, washers and seals", "rubber-gloves/", 55.14, "+26.18%"),
    ("Essential oils", "spices-essential-oils/", None, "+23.95%"),
    ("Animal feed", "processed-food-beverages/", None, None),
    ("Instant tea", "ceylon-tea/", None, "+15.30%"),
    ("Pneumatic and retreaded tyres and tubes", "industrial-tyres/", 483.39, "+10.0%"),
    ("Industrial and surgical gloves", "rubber-gloves/", 266.59, "+8.70%"),
    ("Coconut fibre based products", "coco-peat-coir/", 267.08, "+6.11%"),
    ("Tea packets", "ceylon-tea/", None, f"{M}5.18%"),
    ("Apparel", "apparel-manufacturing/", 3897.30, f"{M}5.16%"),
    ("Textiles", "apparel-manufacturing/", 299.26, f"{M}9.70%"),
    ("Bulk tea", "ceylon-tea/", None, f"{M}10.37%"),
]

# market, 2025 value, 2025 change, Jan to Oct 2026 value, Jan to Oct 2026 change
MARKETS = [
    ("United States", 2999.15, "+3.06%", 2518.31, "+0.81%"),
    ("India", 1035.72, "+17.21%", 989.66, "+14.16%"),
    ("United Kingdom", 929.03, "+2.80%", 723.40, f"{M}8.67%"),
    ("Italy", 679.77, "+14.16%", 573.18, "+0.05%"),
    ("Germany", 706.49, "+12.45%", 565.95, f"{M}5.32%"),
    ("Netherlands", 474.80, "+20.63%", 364.43, f"{M}6.72%"),
    ("China", None, None, 261.31, "+16.24%"),
    ("United Arab Emirates", 341.06, None, 252.35, f"{M}13.02%"),
    ("Türkiye", None, None, 239.30, "+84.93%"),
    ("France", 277.18, "+5.09%", 219.76, f"{M}7.09%"),
    ("Belgium", 254.44, "+6.42%", 217.15, "+3.25%"),
    ("Australia", 262.00, None, None, None),
    ("Pakistan", None, f"{M}2.03%", 88.13, "+38.83%"),
    ("European Union, all members", None, "+13.41%", 2591.36, f"{M}0.85%"),
]

SHIFTS = [
    ("Electrical and electronic components rose 59.60% to US$566.14 million, led by insulated wires and cables, up 82.65%, and transformers, up 36.19%.", "EDB, January to October 2026", YTD_URL),
    ("Spices and concentrates rose 35.35% to US$498.43 million: pepper up 75.25% to US$157.30 million and cinnamon up 31.57% to US$256.64 million.", "EDB, January to October 2026", YTD_URL),
    ("Food and beverages rose 18.93%, with processed food up 24.81% and meat, fish and dairy preparations up 121.41% to US$95.98 million.", "EDB, January to October 2026", YTD_URL),
    ("Rubber products rose 10.10% to US$873.85 million, with tyres and tubes up 10.0% and gloves up 8.70%.", "EDB, January to October 2026", YTD_URL),
    ("Tea fell 6.77% overall, with bulk tea down 10.37% and tea to the Middle East down 33.50%, while tea bags rose 49.54%.", "EDB, January to October 2026", YTD_URL),
    ("Apparel and textiles fell 5.50%, and apparel alone 5.16%, with apparel to the US down 3.99%, the EU down 9.67% and the UK down 5.64%.", "EDB, January to October 2026", YTD_URL),
    ("October 2026 alone rose 11.57% to US$1.62 billion, with services up 18.87% on transport and logistics, and spices up 76.90% in the month.", "EDB, October 2026", YTD_URL),
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
     "From January to October 2026 Sri Lanka earned US$15.28 billion from exports, up 6.03% on the same months of 2025. Goods were US$12.01 billion, up 5.72%, and services an estimated US$3.27 billion, up 7.20%."),
    ("Which countries buy the most from Sri Lanka?",
     "The United States, at US$3.0 billion in 2025 and more than a fifth of goods exports, then India (US$1.04 billion), the United Kingdom (US$929 million), Germany, Italy and the Netherlands. "
     "In January to October 2026 India grew 14.16% to US$990 million, China, the UAE and Türkiye each took more than US$230 million, and Türkiye grew fastest, up 85%."),
    ("Which Sri Lankan exports are growing fastest?",
     "In January to October 2026: electrical and electronic components, up 59.60%, spices and essential oils, up 35.35%, and food and beverages, up 18.93%. "
     "Within those, pepper rose 75%, insulated cables 83% and processed food 25%."),
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
