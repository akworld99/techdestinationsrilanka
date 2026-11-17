"""Ceylon tea data pages: Colombo tea auction prices (weekly averages by elevation, monthly averages, CSV) and a green
leaf price calculator for bought-leaf factories. Figures come from tea_data.py, which _build/tea_update.py keeps current."""
import html
import json

import seo_pages as SP
import seo_source as SS
import tea_data as T
from og_source import ROOT
from seo_pages import a

e = html.escape
PRICES = "source/ceylon-tea/auction-prices/"
CALC = "source/ceylon-tea/green-leaf-price-calculator/"
CSV_NAME = "colombo-tea-auction-weekly-prices.csv"
CSV_PATH = "../../../data/" + CSV_NAME   # from the prices page; other pages add their own prefix in front of PRICES
LATEST_JSON = "colombo-tea-auction-latest.json"
OG_PRICES = "assets/og/source-tea-auction-prices.jpg"
OG_CALC = "assets/og/source-green-leaf-price-calculator.jpg"
COLORS = {"high": "#3a6fd8", "medium": "#d17a00", "low": "#11865f"}   # checked for colour blind separation
STUDY = "https://huggingface.co/papers/2608.24894"
SHORT = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def _og(path):
    """The share image when it has been rendered (python3 _build/og_source.py), else the site default."""
    import os
    return path if os.path.exists(os.path.join(ROOT, path)) else None


def _sd(d):
    return f"{d.day} {SHORT[d.month - 1]} {d.year}"


def _src_line(prefix=""):
    return (f'Source: Forbes &amp; Walker Tea Brokers, {a("weekly tea auction quantities and averages", T.FW_STATS)}. '
            "Averages in Sri Lankan rupees per kilo of made tea, quantities sold in each sale.")


# ------------------------------------------------------------------ chart
def chart(rows, elev=None, title="Colombo tea auction: weekly average price by elevation"):
    """Weekly average price per elevation as an inline SVG line chart, with a hover layer driven by the data attribute.
    `elev` picks the elevations to draw, as (key, name) pairs; one elevation draws without a legend."""
    elev = elev or T.ELEV
    W, H, L, R, TOP, BOT = 680, 330, 52, 128, 14, 34
    d0, d1 = rows[0]["sale_date"].toordinal(), rows[-1]["sale_date"].toordinal()
    vals = [r[f"avg_{k}"] for r in rows for k, _ in elev]
    lo, hi = int(min(vals) // 100 * 100), int(-(-max(vals) // 100) * 100)
    X = lambda d: L + (d.toordinal() - d0) / (d1 - d0) * (W - L - R)  # noqa: E731
    Y = lambda v: TOP + (hi - v) / (hi - lo) * (H - TOP - BOT)  # noqa: E731
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="tea-ct tea-cd" class="tea-svg">',
           f'<title id="tea-ct">{e(title)}</title>',
           f'<desc id="tea-cd">Average price in rupees per kilo at each Colombo sale from {_sd(rows[0]["sale_date"])} to {_sd(rows[-1]["sale_date"])}, '
           f'for {", ".join(n for _, n in elev)} teas. The same figures are in the tables below and the CSV.</desc>']
    for v in range(lo, hi + 1, 100):
        out.append(f'<line x1="{L}" x2="{W - R}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="#e6eaf1" stroke-width="1"/>'
                   f'<text x="{L - 8}" y="{Y(v) + 4:.1f}" text-anchor="end" class="ax">{v:,}</text>')
    from datetime import date
    y0, y1 = rows[0]["sale_date"].year, rows[-1]["sale_date"].year
    labelled = set()
    for yr in range(y0, y1 + 1):
        for m in (1, 4, 7, 10):
            t = date(yr, m, 1)
            if d0 <= t.toordinal() <= d1:
                lab = f"{SHORT[m - 1]} {yr}" if m == 1 or yr not in labelled else SHORT[m - 1]
                labelled.add(yr)
                out.append(f'<line x1="{X(t):.1f}" x2="{X(t):.1f}" y1="{H - BOT}" y2="{H - BOT + 5}" stroke="#c9d1de"/>'
                           f'<text x="{X(t):.1f}" y="{H - BOT + 20}" text-anchor="middle" class="ax">{lab}</text>')
    out.append(f'<line x1="{L}" x2="{W - R}" y1="{H - BOT}" y2="{H - BOT}" stroke="#c9d1de"/>')
    ends = []
    for k, name in elev:
        pts = " ".join(f"{X(r['sale_date']):.1f},{Y(r[f'avg_{k}']):.1f}" for r in rows)
        out.append(f'<polyline points="{pts}" fill="none" stroke="{COLORS[k]}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
        ends.append([Y(rows[-1][f"avg_{k}"]), k, name])
    ends.sort()
    for i in range(1, len(ends)):   # keep end labels at least 30 units apart
        ends[i][0] = max(ends[i][0], ends[i - 1][0] + 30)
    xe = X(rows[-1]["sale_date"])
    for ly, k, name in ends:
        yv = Y(rows[-1][f"avg_{k}"])
        out.append(f'<circle cx="{xe:.1f}" cy="{yv:.1f}" r="4" fill="{COLORS[k]}" stroke="#fff" stroke-width="2"/>'
                   f'<text x="{xe + 10:.1f}" y="{ly - 2:.1f}" class="lab">{name}</text>'
                   f'<text x="{xe + 10:.1f}" y="{ly + 13:.1f}" class="val">{rows[-1][f"avg_{k}"]:,.0f}</text>')
    out.append(f'<g class="tea-hover" style="display:none"><line y1="{TOP}" y2="{H - BOT}" stroke="#8a94a8" stroke-width="1"/>'
               + "".join(f'<circle r="4.5" fill="{COLORS[k]}" stroke="#fff" stroke-width="2" data-k="{k}"/>' for k, _ in elev) + "</g>")
    out.append(f'<rect class="tea-hit" x="{L}" y="{TOP}" width="{W - L - R}" height="{H - TOP - BOT}" fill="transparent"/></svg>')
    data = {"x": [round(X(r["sale_date"]), 1) for r in rows], "d": [_sd(r["sale_date"]) for r in rows], "q": [round(r["qty_total"] / 1000, 2) for r in rows],
            "t": [r["avg_total"] for r in rows], "y": {k: [round(Y(r[f"avg_{k}"]), 1) for r in rows] for k, _ in elev},
            "v": {k: [r[f"avg_{k}"] for r in rows] for k, _ in elev}, "w": W}
    legend = "".join(f'<span><i style="background:{COLORS[k]}"></i>{n}</span>' for k, n in elev) if len(elev) > 1 else ""
    return ((f'<div class="tea-legend" aria-hidden="true">{legend}</div>' if legend else "")
            + f'<div class="tea-chart" data-chart=\'{e(json.dumps(data))}\'><div class="tea-scroll">{"".join(out)}</div><div class="tea-tip" role="status"></div></div>')


CHART_JS = """<script>
(function () {
  var box = document.querySelector('.tea-chart'); if (!box) return;
  var d = JSON.parse(box.dataset.chart), svg = box.querySelector('svg'), g = svg.querySelector('.tea-hover'), tip = box.querySelector('.tea-tip');
  var names = {high: 'High Grown', medium: 'Medium Grown', low: 'Low Grown'}, colors = {high: '#3a6fd8', medium: '#d17a00', low: '#11865f'};
  function fmt(v) { return v.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2}); }
  function show(ev) {
    var pt = svg.createSVGPoint(); pt.x = ev.clientX; pt.y = ev.clientY; var p = pt.matrixTransform(svg.getScreenCTM().inverse());
    var i = 0; for (var j = 1; j < d.x.length; j++) if (Math.abs(d.x[j] - p.x) < Math.abs(d.x[i] - p.x)) i = j;
    g.style.display = ''; var ln = g.querySelector('line'); ln.setAttribute('x1', d.x[i]); ln.setAttribute('x2', d.x[i]);
    Array.prototype.forEach.call(g.querySelectorAll('circle'), function (c) { c.setAttribute('cx', d.x[i]); c.setAttribute('cy', d.y[c.dataset.k][i]); });
    var h = '<b>Sale of ' + d.d[i] + '</b>';
    ['low', 'high', 'medium'].filter(function (k) { return k in d.v; }).forEach(function (k) { h += '<br><i style="background:' + colors[k] + '"></i>' + names[k] + ': Rs ' + fmt(d.v[k][i]); });
    h += '<br>All teas: Rs ' + fmt(d.t[i]) + '<br>' + d.q[i] + ' million kg sold';
    tip.innerHTML = h; tip.style.display = 'block';
    var r = box.getBoundingClientRect(), sr = svg.getBoundingClientRect(), x = sr.left - r.left + d.x[i] / d.w * sr.width;
    var tw = tip.offsetWidth; tip.style.left = (x + 16 + tw <= r.width ? x + 16 : Math.max(x - 16 - tw, 0)) + 'px';
  }
  var sc = box.querySelector('.tea-scroll'); if (sc) sc.scrollLeft = sc.scrollWidth;
  var hit = svg.querySelector('.tea-hit');
  hit.addEventListener('mousemove', show); hit.addEventListener('touchstart', function (ev) { show(ev.touches[0]); }, {passive: true});
  hit.addEventListener('mouseleave', function () { g.style.display = 'none'; tip.style.display = 'none'; });
})();
</script>"""


# ------------------------------------------------------------------ tables
def _latest_table(rows, n=10):
    body = []
    recent = rows[-(n + 1):]
    for i in range(len(recent) - 1, 0, -1):
        r, p = recent[i], recent[i - 1]
        c = T.pct(r["avg_total"], p["avg_total"])
        cls = "up" if c > 0 else "down" if c < 0 else ""
        body.append(f"<tr><td class=\"nw\">{_sd(r['sale_date'])}</td>" + "".join(f"<td>{r[f'avg_{k}']:,.2f}</td>" for k, _ in T.ELEV)
                    + f"<td><strong>{r['avg_total']:,.2f}</strong></td><td>{r['qty_total'] / 1000:.2f}</td><td class=\"{cls}\">{T.signed(c)}</td></tr>")
    head = "".join(f"<th>{h}</th>" for h in ["Sale", "High Grown, Rs", "Medium Grown, Rs", "Low Grown, Rs", "All teas, Rs", "Sold, million kg", "All teas, change on previous sale"])
    return f'<div class="tbl"><table><thead><tr>{head}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'


def _monthly_table(rows):
    m = T.monthly(rows)
    last = rows[-1]["sale_date"]
    year = last.year
    partial = last.day < 24   # the month of the latest sale may have more sales to come
    body = []
    for (y, mo), v in reversed(list(m.items())):
        if y != year:
            continue
        prev = m.get((y - 1, mo))
        if partial and (y, mo) == (last.year, last.month):   # compare with the same days a year earlier, not the whole month
            same = [r for r in rows if (r["sale_date"].year, r["sale_date"].month) == (y - 1, mo) and r["sale_date"].day <= last.day]
            prev = {"total": T.wavg(same, "total")} if same else None
        c = T.pct(v["total"], prev["total"]) if prev else None
        cls = "up" if c and c > 0 else "down" if c and c < 0 else ""
        n = f"{v['sales']} sale{'s' if v['sales'] != 1 else ''}"
        note = f"<br><span class=\"cap\">{n}, to {last.day} {SHORT[mo - 1]}</span>" if partial and (y, mo) == (last.year, last.month) else f"<br><span class=\"cap\">{n}</span>"
        before = f"{prev['total']:,.2f}" if prev else "–"
        body.append(f"<tr><td>{T.MONTH_NAMES[mo - 1]} {y}{note}</td>" + "".join(f"<td>{v[k]:,.2f}</td>" for k, _ in T.ELEV)
                    + f"<td><strong>{v['total']:,.2f}</strong></td><td>{before}</td><td class=\"{cls}\">{T.signed(c)}</td></tr>")
    head = "".join(f"<th>{h}</th>" for h in ["Month", "High Grown, Rs", "Medium Grown, Rs", "Low Grown, Rs", "All teas, Rs", f"All teas, {year - 1}, Rs", "Change"])
    return f'<div class="tbl"><table><thead><tr>{head}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'


def _csv(B, rows):
    lines = ["sale_date,high_grown_qty_000kg,medium_grown_qty_000kg,low_grown_qty_000kg,total_qty_000kg,high_grown_avg_lkr,medium_grown_avg_lkr,low_grown_avg_lkr,all_teas_avg_lkr"]
    lines += [",".join([r["sale_date"].isoformat()] + [str(int(r[k])) for k in T.FIELDS[1:5]] + [f"{r[k]:.2f}" for k in T.FIELDS[5:9]]) for r in rows]
    B.write("data/" + CSV_NAME, "\n".join(lines) + "\n")


# ------------------------------------------------------------------ copy that reads from the data
def answer(rows):
    s = T.summary(rows)
    r = s["last"]
    ytd = s["ytd"]
    c = s["chg_ytd"]
    compare = f", {'up' if c > 0 else 'down'} {abs(c):.1f}% on the same period of {s['year'] - 1}" if c is not None else ""
    return (f"The average price at the Colombo tea auction sale of {T.fdate(r['sale_date'])} was {T.rs(r['avg_total'])} a kilo, across {r['qty_total'] / 1000:.2f} million kg. "
            f"Low Grown teas averaged {T.rs(r['avg_low'])}, High Grown {T.rs(r['avg_high'])} and Medium Grown {T.rs(r['avg_medium'])}. "
            f"Across the {ytd['sales']} sale{'s' if ytd['sales'] != 1 else ''} of {s['year']} to that date the average was {T.rs(ytd['total'])}{compare}.")


def faqs_prices(rows):
    s = T.summary(rows)
    return [
        ("What is the average price at the Colombo tea auction?", answer(rows)),
        ("When is the Colombo tea auction held?", "Every week, usually over two days on Tuesday and Wednesday, with occasional one day or rescheduled sales around holidays. "
         "Each sale offers around 5 to 6 million kg of tea in catalogues from the licensed brokers."),
        ("What are High, Medium and Low Grown teas?", "Ceylon tea is grouped by the elevation of the estate where it is grown. The three groups sell at different prices: "
         f"at the latest sale Low Grown teas averaged {T.rs(s['last']['avg_low'], 0)} a kilo against {T.rs(s['last']['avg_medium'], 0)} for Medium Grown. "
         f"Low Grown teas were {s['low_share']:.0f}% of the quantity sold at auction in {s['year']}."),
        ("Where do these figures come from?", "From the weekly tea auction quantities and averages that Forbes & Walker Tea Brokers publish. We check that every sale adds up "
         "before we store it and add each new sale when the broker publishes it. Monthly averages are our calculation, weighted by the quantity sold at each sale. "
         "The Sri Lanka Tea Board publishes the official monthly national sale average, which is calculated differently and can differ by up to about 2%."),
        ("What is the Ceylon tea price per kg?", f"At the Colombo auction sale of {T.fdate(s['last']['sale_date'])} the average was {T.rs(s['last']['avg_total'])} a kilo of made tea "
         f"across all elevations, ranging from {T.rs(s['last']['avg_' + s['bottom'][0]])} for {s['bottom'][1]} to {T.rs(s['last']['avg_' + s['top'][0]])} for {s['top'][1]} teas. "
         "These are auction averages in Sri Lankan rupees; individual lots and grades sell well above and below them."),
        (f"What was the highest Colombo tea auction average in {s['year']}?", _year_high(rows, s["year"])),
        ("What is the national sale average (NSA)?", "The average price per kilo that tea fetched at the Colombo auction over a month. The Sri Lanka Tea Board publishes it each month for all teas and "
         "by elevation, and each bought-leaf factory has its own NSA, which sets the green leaf price it pays its suppliers."),
        ("Do you forecast tea prices?", "We are testing forecasts of the next four to eight weeks by elevation, and will publish them only once they beat a simple "
         "benchmark: assuming the next sale repeats the last one. Leave your details on this page to get them first."),
    ]


def _year_high(rows, y):
    sel = [r for r in rows if r["sale_date"].year == y]
    hi = max(sel, key=lambda r: r["avg_total"])
    return f"{T.rs(hi['avg_total'])} a kilo for all teas, at the sale of {T.fdate(hi['sale_date'])}, to the latest sale of {T.fdate(sel[-1]['sale_date'])}."


# ------------------------------------------------------------------ pages
def build_prices(B, stories, rows):
    prefix = "../../../"
    s = T.summary(rows)
    r = s["last"]
    _csv(B, rows)
    faq, faq_ld = SP.faq_block(stories, faqs_prices(rows))
    form = SS._form(B, "tea-prices", "Get Colombo price alerts and forecasts",
                    "We are testing forecasts of auction prices by elevation, four to eight weeks ahead. Leave your details for weekly price emails, "
                    "alerts on WhatsApp when prices move, and the first forecasts once they pass our accuracy tests.", [
                        ("text", "name", "Your name", True, ""), ("email", "email", "Work email", True, ""), ("text", "company", "Company", False, ""),
                        ("text", "country", "Country", False, ""),
                        ("select", "role", "You are", True, ["Importer or packer", "Sri Lankan exporter", "Broker or trader", "Tea factory or plantation", "Analyst or lender", "Other"]),
                        ("checks", "wants", "What you want", False, ["Weekly price email", "Price alerts on WhatsApp", "Forecasts by elevation", "Data feed or API"]),
                        ("tel", "whatsapp", "WhatsApp number", False, "+94 ..."),
                    ], "Keep me posted", "Thanks. We will be in touch by email.")
    stats = [(T.rs(r["avg_total"], 0), f"average a kilo at the sale of {_sd(r['sale_date'])}"),
             (T.signed(s["chg_ytd"]), f"{s['year']} average to date against the same period of {s['year'] - 1}"),
             (f"{s['low_share']:.0f}%", f"of {s['year']} auction quantity was Low Grown tea"),
             (f"{r['qty_total'] / 1000:.2f}M kg", "sold at the latest sale")]
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Source from Sri Lanka", "../../"), ("Ceylon tea", "../")])}
  <h1>Colombo tea auction prices: weekly averages by elevation</h1>
  <p class="answer">{e(answer(rows))}</p>
  <p class="reviewed">Figures to the sale of {T.fdate(r['sale_date'])}, from Forbes &amp; Walker Tea Brokers, linked under each table. We add each sale when the broker publishes it.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  {SP.stats_strip(stats)}
  <h2 class="h-sub mt">Key figures by elevation</h2>
  {key_figures(rows, prefix)}
  <p class="cap">{_src_line()} Highs, lows and comparisons are our calculation.</p>
  <h2 class="h-sub mt">Weekly average price by elevation, {rows[0]['sale_date'].year} to {r['sale_date'].year}</h2>
  <p class="body-l">Rupees per kilo at each sale. Hover or tap the chart to read a sale.</p>
  {chart(rows)}
  <p class="cap">{_src_line()}</p>
  <h2 class="h-sub mt">Latest sales</h2>
  {_latest_table(rows)}
  <p class="cap">{_src_line()} Change is our calculation.</p>
  <h2 class="h-sub mt">Monthly averages, {s['year']} against {s['year'] - 1}</h2>
  {_monthly_table(rows)}
  <p class="cap">Our calculation from the weekly figures, weighted by quantity sold. A month still in progress is compared with the same days a year earlier. The Sri Lanka Tea Board's official monthly national sale average is calculated differently and can differ by up to about 2%.</p>
  <h2 class="h-sub mt">What moves Colombo prices</h2>
  <p class="body-l">A study of 105 weekly broker reports from November 2023 to March 2026 found market and structural factors, such as grade and catalogue, drive prices far more than weather. Weather is a secondary, lagged signal: Low Grown prices responded to rain and sunshine one to three weeks earlier, while High Grown prices showed no lasting weather effect ({a("study, August 2026", STUDY)}).</p>
  <div class="cite"><strong>Use this data.</strong> <a href="{prefix}data/{CSV_NAME}" download>Download every sale as CSV</a> or the <a href="{prefix}data/{LATEST_JSON}">latest figures as JSON</a>. The weekly figures are Forbes &amp; Walker Tea Brokers'; credit them as the source, and link to this page if you use our charts or monthly averages.<br><span>Suggested credit: Forbes &amp; Walker Tea Brokers, compiled by Tech Destination Sri Lanka, {B.SITE_URL}/{PRICES}</span></div>
  {form}
  <h2 class="h-sub mt">Run a bought-leaf tea factory?</h2>
  <p class="body-l">See the green leaf rate your net sale average supports, and what happens to it if prices move: <a href="../green-leaf-price-calculator/">green leaf price calculator</a>.</p>
  <h2 class="h-sub mt">Buying Ceylon tea?</h2>
  <p class="body-l">Grades, the Lion logo, certificates and how to buy from Sri Lankan exporters: <a href="../">Ceylon tea suppliers and exporters</a>. Or <a href="../../request-a-quote/?product=ceylon-tea">request a quote</a> and we will introduce exporters who ship to your market.</p>
  {browse(rows, prefix)}
  {faq}
</div></section>
{CHART_JS}
"""
    org = {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"}
    ds = SP.ld({"@context": "https://schema.org", "@type": "Dataset", "name": "Colombo tea auction weekly average prices and quantities by elevation",
                "description": "Average price in Sri Lankan rupees per kilo and quantity sold at each Colombo tea auction sale, for High, Medium and Low Grown teas, "
                               "compiled from Forbes & Walker Tea Brokers' weekly tea auction quantities and averages.",
                "url": f"{B.SITE_URL}/{PRICES}", "creator": org, "publisher": org, "isAccessibleForFree": True, "isBasedOn": T.FW_STATS,
                "temporalCoverage": f"{rows[0]['sale_date'].isoformat()}/{r['sale_date'].isoformat()}", "spatialCoverage": {"@type": "Place", "name": "Colombo, Sri Lanka"},
                "dateModified": r["sale_date"].isoformat(), "keywords": ["Colombo tea auction prices", "Ceylon tea price", "tea auction average", "Sri Lanka tea prices", "Low Grown tea price"],
                "variableMeasured": ["Average price (LKR per kg)", "Quantity sold (thousand kg)"],
                "distribution": [{"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": f"{B.SITE_URL}/data/{CSV_NAME}"}]})
    head = faq_ld + ds + SP.crumbs_ld(B, [("Source from Sri Lanka", "source/"), ("Ceylon tea", "source/ceylon-tea/"), ("Auction prices", PRICES)])
    desc = (f"Colombo tea auction prices: {T.rs(r['avg_total'], 0)} a kilo at the sale of {_sd(r['sale_date'])}. Weekly Ceylon tea averages by elevation, "
            "monthly averages and a CSV, updated every week.")
    B.write(PRICES + "index.html", B.page("Colombo tea auction prices: weekly averages by elevation", desc, body, prefix, PRICES, extra_head=head,
                                          active="source", seo_title="Colombo tea auction prices this week: Ceylon tea", image=_og(OG_PRICES)))
    return PRICES


def build_calculator(B, stories, rows):
    prefix = "../../../"
    m = T.monthly(rows)
    (y, mo), last = list(m.items())[-1]
    if last["sales"] < 3 and len(m) > 1:   # a month with one or two sales is too thin to stand for the month
        (y, mo), last = list(m.items())[-2]
    ea = {k: round(last[k], 2) for k, _ in T.ELEV}
    month = f"{T.MONTH_NAMES[mo - 1]} {y}"
    data = json.dumps({"ea": ea})
    faqs = [
        ("How is the green leaf price calculated in Sri Lanka?", "Bought-leaf factories pay for green leaf under a statutory formula tied to the factory's net sale average at auction. "
         "As documented by the Tea Research Institute, the supplier receives 68% of the net sale average when it is at or below the elevation average, or 68% of the "
         "elevation average plus 50% of the excess when it is above, converted at a fixed out-turn of 22.22 kg of made tea per 100 kg of green leaf."),
        ("What is a factory's net sale average?", "The average price per kilo that a factory's made tea fetched at the Colombo auction over the month."),
        ("Why does the elevation average matter?", "Above the elevation average the supplier's share of the extra drops from 68% to 50%, so a factory that sells "
         "above its elevation's average keeps more of that premium."),
        ("Is this the official green leaf price?", "No. It is an estimate from the formula as last documented. The Tea Commissioner's Division of the Sri Lanka Tea Board "
         "sets and enforces the rules, so confirm current parameters with it before you rely on a figure."),
        ("What is the green leaf price this month?", f"It depends on each factory's net sale average. As an estimate at the {month} elevation averages, the formula gives about "
         + ", ".join(f"{T.rs(T.leaf_rate(last[k]), 0)} for {n}" for k, n in sorted(T.ELEV, key=lambda x: -last[x[0]])) + " a kilo of green leaf."),
        ("What is dalu mila?", "Dalu mila (දළු මිල in Sinhala) is the price a factory pays for green tea leaf, the same green leaf rate this calculator works out. In Tamil it is "
         "கொழுந்து விலை (kolunthu vilai)."),
    ]
    leaf_rows = ""
    for (yy, mm), v in list(reversed(list(m.items())))[:12]:
        note = " <span class=\"cap\">(so far)</span>" if (yy, mm) == (rows[-1]["sale_date"].year, rows[-1]["sale_date"].month) and rows[-1]["sale_date"].day < 24 else ""
        leaf_rows += (f'<tr><td><a href="../auction-prices/{T.month_slug(yy, mm)}/">{T.MONTH_NAMES[mm - 1]} {yy}</a>{note}</td>'
                      + "".join(f"<td>{T.leaf_rate(v[k]):,.2f}</td>" for k in ("low", "high", "medium")) + "</tr>")
    leaf_head = "".join(f"<th>{h}</th>" for h in ["Month", "Low Grown, Rs per kg of leaf", "High Grown, Rs per kg of leaf", "Medium Grown, Rs per kg of leaf"])
    faq, faq_ld = SP.faq_block(stories, faqs)
    form = SS._form(B, "tea-factory", "Get next month's leaf rate outlook for your factory",
                    "We are piloting a monthly outlook for bought-leaf factories: where next month's auction prices and leaf rate are likely to land, and a WhatsApp "
                    "message to your leaf suppliers in Sinhala and Tamil, in your factory's name.", [
                        ("text", "name", "Your name", True, ""), ("text", "factory", "Factory name", True, ""), ("text", "district", "District", True, ""),
                        ("tel", "whatsapp", "WhatsApp number", True, "+94 ..."), ("email", "email", "Email", False, ""),
                        ("select", "suppliers", "Leaf suppliers", False, ["Not sure", "Under 500", "500 to 2,000", "2,000 to 5,000", "Over 5,000"]),
                        ("checks", "wants", "What you want", False, ["Next month's leaf rate outlook", "Supplier messages on WhatsApp", "Factory price dashboard"]),
                    ], "Join the pilot", "Thanks. We will contact you on WhatsApp.")
    opts = "".join(f'<option value="{k}"{" selected" if k == "low" else ""}>{n}</option>' for k, n in T.ELEV)
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Source from Sri Lanka", "../../"), ("Ceylon tea", "../")])}
  <h1>Green leaf price calculator for Sri Lankan tea factories</h1>
  <p class="answer">Bought-leaf factories pay their suppliers for green leaf under a statutory formula tied to what the factory's tea fetches at auction. Enter your factory's net sale average and the elevation average for the month to see the leaf rate it implies, and how that rate moves if auction prices change.</p>
  <p class="reviewed">Formula as documented by the Tea Research Institute ({a("2003 study", T.TRI_FORMULA)}). An estimate, not the official rate: confirm current parameters with the Tea Commissioner's Division.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <div class="calc" id="leaf" data-calc='{e(data)}'>
    <div class="tea-fields">
      <label><span>Elevation</span><select id="lf-elev">{opts}</select></label>
      <label><span>Elevation average, Rs per kg</span><input id="lf-ea" type="number" min="0" step="0.01" inputmode="decimal"></label>
      <label><span>Your factory's net sale average, Rs per kg</span><input id="lf-nsa" type="number" min="0" step="0.01" inputmode="decimal"></label>
    </div>
    <details class="tea-adv"><summary>Formula settings</summary>
      <div class="tea-fields">
        <label><span>Supplier share up to the elevation average, %</span><input id="lf-share" type="number" value="68" step="0.1"></label>
        <label><span>Supplier share of the excess above it, %</span><input id="lf-excess" type="number" value="50" step="0.1"></label>
        <label><span>Made tea per 100 kg of green leaf, kg</span><input id="lf-out" type="number" value="22.22" step="0.01"></label>
      </div>
    </details>
    <dl class="facts calc-out">
      <div><dt id="lf-rate">0</dt><dd>green leaf rate, Rs per kg of leaf</dd></div>
      <div><dt id="lf-mt">0</dt><dd>supplier's share, Rs per kg of made tea</dd></div>
      <div><dt id="lf-pct">0</dt><dd>supplier's share of the net sale average</dd></div>
    </dl>
    <h3 class="h-sub">If auction prices move</h3>
    <div class="tbl slim"><table><thead><tr><th>Net sale average changes by</th><th>Net sale average, Rs</th><th>Leaf rate, Rs per kg</th><th>Change in leaf rate, Rs</th></tr></thead><tbody id="lf-rows"></tbody></table></div>
    <p class="cap">The elevation average is filled in with our {e(month)} Colombo auction average for that elevation, weighted by quantity sold, from Forbes &amp; Walker Tea Brokers' weekly figures (<a href="../auction-prices/">see the prices</a>). Use the Tea Board's official figure for the month if you have it; it can differ by up to about 2%. The scenarios hold the elevation average fixed.</p>
  </div>
  <h2 class="h-sub mt">The formula</h2>
  <p class="body-l">As documented by the Tea Research Institute in 2003, with NSA the factory's net sale average and EA the elevation average:</p>
  <ul class="ticks"><li>If NSA is at or below EA: leaf rate = out-turn × 68% × NSA</li><li>If NSA is above EA: leaf rate = out-turn × (68% × EA + 50% × (NSA − EA))</li><li>Out-turn: 22.22 kg of made tea from 100 kg of green leaf</li></ul>
  <p class="body-l">Change the settings above if the Tea Commissioner's Division has revised any of these.</p>
  <h2 class="h-sub mt">Green leaf rate by month, at the elevation average</h2>
  <p class="body-l">What the formula gives when a factory's net sale average equals its elevation's average for the month. Factories that sell above or below the average pay more or less.</p>
  <div class="tbl"><table><thead><tr>{leaf_head}</tr></thead><tbody>{leaf_rows}</tbody></table></div>
  <p class="cap">Our estimate: the formula above applied to each month's Colombo auction average by elevation, weighted by quantity, from Forbes &amp; Walker Tea Brokers' weekly figures. Not the official rate.</p>
  <h2 class="h-sub mt">In Sinhala and Tamil</h2>
  <p class="body-l" lang="si">තේ දළු මිල ගණකය: ඔබේ කර්මාන්තශාලාවේ මාසික ශුද්ධ විකුණුම් සාමාන්‍යය (NSA) සහ උන්නතාංශ සාමාන්‍යය ඇතුළත් කර, කිලෝවක දළු මිල ගණනය කරන්න. මෙය ඇස්තමේන්තුවකි; නිල මිල තේ කොමසාරිස් කොට්ඨාසයෙන් තහවුරු කරගන්න.</p>
  <p class="body-l" lang="ta">தேயிலை பச்சைக் கொழுந்து விலை கணிப்பான்: உங்கள் தொழிற்சாலையின் மாதாந்த நிகர விற்பனை சராசரி (NSA) மற்றும் உயர சராசரியை உள்ளிட்டு, ஒரு கிலோ கொழுந்தின் விலையைக் கணக்கிடுங்கள். இது ஒரு மதிப்பீடு மட்டுமே; உத்தியோகபூர்வ விலையை தேயிலை ஆணையாளர் பிரிவிடம் உறுதிப்படுத்துங்கள்.</p>
  {form}
  <div class="actions"><a class="btn btn-wa" href="{SS.wa("Hi, I run a tea factory and want the monthly leaf rate outlook.")}" rel="noopener">WhatsApp us</a></div>
  {faq}
  <p class="body-l mt">See also: <a href="../auction-prices/">Colombo tea auction prices</a> · <a href="../">Ceylon tea from Sri Lanka</a> · <a href="../../tender-radar/">Tender Radar for exporters</a></p>
</div></section>
<script>
(function () {{
  var d = JSON.parse(document.getElementById('leaf').dataset.calc);
  function $(id) {{ return document.getElementById(id); }}
  function num(id) {{ return parseFloat($(id).value) || 0; }}
  function rs(v) {{ return 'Rs ' + v.toLocaleString('en-US', {{minimumFractionDigits: 2, maximumFractionDigits: 2}}); }}
  function rate(nsa, ea) {{
    var s = num('lf-share') / 100, x = num('lf-excess') / 100, o = num('lf-out') / 100;
    var mt = nsa <= ea ? s * nsa : s * ea + x * (nsa - ea); return {{mt: mt, leaf: mt * o}};
  }}
  function calc() {{
    var ea = num('lf-ea'), nsa = num('lf-nsa'), r = rate(nsa, ea);
    $('lf-rate').textContent = rs(r.leaf); $('lf-mt').textContent = rs(r.mt); $('lf-pct').textContent = nsa ? (r.mt / nsa * 100).toFixed(1) + '%' : '0%';
    var rows = '';
    [-10, -5, 0, 5, 10].forEach(function (p) {{
      var n = nsa * (1 + p / 100), q = rate(n, ea), dlt = q.leaf - r.leaf;
      rows += '<tr><td>' + (p > 0 ? '+' : p < 0 ? '\\u2212' : '') + Math.abs(p) + '%</td><td>' + n.toLocaleString('en-US', {{minimumFractionDigits: 2, maximumFractionDigits: 2}}) + '</td><td><strong>' + q.leaf.toFixed(2) + '</strong></td><td>' + (p ? (dlt > 0 ? '+' : '\\u2212') + Math.abs(dlt).toFixed(2) : '') + '</td></tr>';
    }});
    $('lf-rows').innerHTML = rows;
  }}
  function setElev() {{ var v = d.ea[$('lf-elev').value]; $('lf-ea').value = v; $('lf-nsa').value = v; calc(); }}
  $('lf-elev').addEventListener('change', setElev);
  ['lf-ea', 'lf-nsa', 'lf-share', 'lf-excess', 'lf-out'].forEach(function (id) {{ $(id).addEventListener('input', calc); }});
  setElev();
}})();
</script>
"""
    app = SP.ld({"@context": "https://schema.org", "@type": "WebApplication", "name": "Green leaf price calculator for Sri Lankan tea factories",
                 "url": f"{B.SITE_URL}/{CALC}", "applicationCategory": "BusinessApplication", "operatingSystem": "Any", "inLanguage": ["en", "si", "ta"],
                 "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
                 "description": "Works out the green leaf rate a bought-leaf tea factory pays under Sri Lanka's price formula, from its net sale average and the elevation average.",
                 "publisher": {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"}})
    head = faq_ld + app + SP.crumbs_ld(B, [("Source from Sri Lanka", "source/"), ("Ceylon tea", "source/ceylon-tea/"), ("Green leaf price calculator", CALC)])
    B.write(CALC + "index.html", B.page("Green leaf price calculator for Sri Lankan tea factories",
                                        f"Green leaf price (dalu mila) calculator for Sri Lankan tea factories. At the {month} Low Grown average the formula gives about {T.rs(T.leaf_rate(last['low']), 0)} a kilo of leaf. Work out yours.",
                                        body, prefix, CALC, extra_head=head, active="source", seo_title="Tea green leaf price calculator: Sri Lanka dalu mila", image=_og(OG_CALC)))
    return CALC


# ------------------------------------------------------------------ pieces used on other pages
def category_box():
    """Latest prices on the Ceylon tea sourcing page (source/ceylon-tea/)."""
    rows = T.load()
    r = rows[-1]
    cells = "".join(f"<tr><td>{n}</td><td>{r[f'avg_{k}']:,.2f}</td></tr>" for k, n in T.ELEV) + f"<tr><td><strong>All teas</strong></td><td><strong>{r['avg_total']:,.2f}</strong></td></tr>"
    return f"""<h2 class="h-sub mt">Colombo auction prices</h2>
  <p class="body-l">Average price at the sale of {T.fdate(r['sale_date'])}, rupees per kilo, with {r['qty_total'] / 1000:.2f} million kg sold:</p>
  <div class="tbl slim"><table><thead><tr><th>Elevation</th><th>Average, Rs per kg</th></tr></thead><tbody>{cells}</tbody></table></div>
  <p class="cap">{_src_line()}</p>
  <p class="body-l"><a href="auction-prices/">Every sale since {rows[0]['sale_date'].year}, monthly averages and a CSV</a> · <a href="green-leaf-price-calculator/">Green leaf price calculator for factories</a></p>
  <p class="body-l">By elevation: <a href="auction-prices/low-grown/">Low Grown</a> · <a href="auction-prices/high-grown/">High Grown</a> · <a href="auction-prices/medium-grown/">Medium Grown</a></p>"""


def llms_lines(B):
    rows = T.load()
    y, m = rows[-1]["sale_date"].year, rows[-1]["sale_date"].month
    lines = ["", "## Ceylon tea prices",
             f"- [Colombo tea auction prices: weekly averages by elevation]({B.SITE_URL}/{PRICES}): {answer(rows)} CSV: {B.SITE_URL}/data/{CSV_NAME}. Latest figures as JSON: {B.SITE_URL}/data/{LATEST_JSON}",
             f"- [Green leaf price calculator for Sri Lankan tea factories]({B.SITE_URL}/{CALC}): The green leaf rate (dalu mila) a bought-leaf factory pays under Sri Lanka's price formula, from its net sale average and the elevation average, with monthly estimates."]
    lines += [f"- [{n} tea prices at the Colombo auction]({B.SITE_URL}/{PRICES}{ELEV_SLUG[k]}/): {elevation_answer(rows, k, n)}" for k, n in T.ELEV]
    lines += [f"- [Colombo tea auction prices {yy}]({B.SITE_URL}/{PRICES}{yy}/): {year_answer(rows, yy)[0]}" for yy in reversed(T.years(rows))]
    lines.append(f"- [Colombo tea auction prices, {_mname(y, m)}]({B.SITE_URL}/{PRICES}{T.month_slug(y, m)}/): {month_answer(rows, y, m)} Every month since {_mname(rows[0]['sale_date'].year, rows[0]['sale_date'].month)} has its own page.")
    return lines


def build(B, stories):
    rows = T.load()
    out = [build_prices(B, stories, rows), build_calculator(B, stories, rows)]
    nav = [(y, m) for y, m, _ in _months(rows)]
    out += [build_month(B, stories, rows, y, m, nav) for y, m in nav]
    out += [build_year(B, stories, rows, y) for y in T.years(rows)]
    out += [build_elevation(B, stories, rows, k, n) for k, n in T.ELEV]
    latest_json(B, rows)
    return out


# ================================================================== search pages: month, year, elevation
GROWING = "https://teasrilanka.org/growing-regions"
EDB_TEA = "https://www.srilankabusiness.com/ebooks/tea---industry-capability-report----december-2019.pdf"
ELEV_SLUG = {"high": "high-grown", "medium": "medium-grown", "low": "low-grown"}
ELEV_INFO = {   # sourced: Tea Exporters Association (elevations) and Export Development Board (main markets)
    "high": ("grown above 1,200 m", None),
    "medium": ("grown between 600 m and 1,200 m", "Medium grown teas are popular in Australia, Europe, Japan and North America"),
    "low": ("grown from sea level to 600 m", "Low grown teas are mainly popular in Western Asia and the Middle East"),
}


def _months(rows):
    """[(year, month, rows)] in date order."""
    out = {}
    for r in rows:
        out.setdefault((r["sale_date"].year, r["sale_date"].month), []).append(r)
    return [(y, m, v) for (y, m), v in sorted(out.items())]


def _mname(y, m):
    return f"{T.MONTH_NAMES[m - 1]} {y}"


def _chg(a, b):
    c = T.pct(a, b)
    if c is None:
        return "–", ""
    return T.signed(c), "up" if c > 0 else "down" if c < 0 else ""


def _updown(c):
    return f"up {abs(c):.1f}%" if c > 0 else f"down {abs(c):.1f}%" if c < 0 else "unchanged"


def _partial(rows, y, m):
    last = rows[-1]["sale_date"]
    return (y, m) == (last.year, last.month) and last.day < 24


def _same_days(rows, y, m, day):
    return [r for r in rows if (r["sale_date"].year, r["sale_date"].month) == (y, m) and r["sale_date"].day <= day]


def _month_url(prefix, y, m):
    return f"{prefix}{PRICES}{T.month_slug(y, m)}/"


def browse(rows, prefix):
    """Links to every elevation, year and month page, for the main page and the pages themselves."""
    el = SP.chip_links([(f"{n} tea prices", f"{prefix}{PRICES}{ELEV_SLUG[k]}/") for k, n in T.ELEV])
    yr = SP.chip_links([(f"Tea auction prices {y}", f"{prefix}{PRICES}{y}/") for y in reversed(T.years(rows))])
    mo = SP.chip_links([(_mname(y, m), _month_url(prefix, y, m)) for y, m, _ in reversed(_months(rows))])
    return f"""<h2 class="h-sub mt">Browse Colombo tea prices</h2>
  <p class="body-l"><strong>By elevation</strong></p>{el}
  <p class="body-l"><strong>By year</strong></p>{yr}
  <p class="body-l"><strong>By month</strong></p>{mo}"""


def key_figures(rows, prefix):
    s = T.summary(rows)
    y = s["year"]
    cut = s["last"]["sale_date"]
    cur, prev = [r for r in rows if r["sale_date"].year == y], T.year_to_date(rows, y - 1, cut)
    body = ""
    for k, n in T.ELEV:
        hi, hid, lo, lod = T.range_52w(rows, k)
        ytd = T.wavg(cur, k)
        c, cls = _chg(ytd, prev[k])
        body += (f'<tr><td><a href="{prefix}{PRICES}{ELEV_SLUG[k]}/">{n}</a></td><td>{s["last"][f"avg_{k}"]:,.2f}</td>'
                 f'<td>{hi:,.2f}<br><span class="cap">{_sd(hid)}</span></td><td>{lo:,.2f}<br><span class="cap">{_sd(lod)}</span></td>'
                 f'<td>{ytd:,.2f}</td><td>{prev[k]:,.2f}</td><td class="{cls}">{c}</td></tr>')
    head = "".join(f"<th>{h}</th>" for h in ["Elevation", f"Sale of {_sd(cut)}, Rs", "52-week high, Rs", "52-week low, Rs", f"{y} to date, Rs", f"Same period {y - 1}, Rs", "Change"])
    return f'<div class="tbl"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def _page_head(trail, h1, answer_text, reviewed):
    return f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html(trail)}
  <h1>{e(h1)}</h1>
  <p class="answer">{e(answer_text)}</p>
  <p class="reviewed">{reviewed}</p>
</div></section>"""


def _crumbs(B, last_name, path):
    return SP.crumbs_ld(B, [("Source from Sri Lanka", "source/"), ("Ceylon tea", "source/ceylon-tea/"), ("Auction prices", PRICES), (last_name, path)])


# ------------------------------------------------------------------ month pages
def month_stats(rows, y, m):
    sel = [r for r in rows if (r["sale_date"].year, r["sale_date"].month) == (y, m)]
    v = {k: T.wavg(sel, k) for k in ("high", "medium", "low", "total")} | {"sales": len(sel), "qty": sum(r["qty_total"] for r in sel), "rows": sel}
    if _partial(rows, y, m):
        same = _same_days(rows, y - 1, m, rows[-1]["sale_date"].day)
    else:
        same = [r for r in rows if (r["sale_date"].year, r["sale_date"].month) == (y - 1, m)]
    v["ly"] = {k: T.wavg(same, k) for k in ("high", "medium", "low", "total")} if same else None
    pm = (y, m - 1) if m > 1 else (y - 1, 12)
    psel = [r for r in rows if (r["sale_date"].year, r["sale_date"].month) == pm]
    v["pm"] = {k: T.wavg(psel, k) for k in ("high", "medium", "low", "total")} if psel else None
    v["pm_key"] = pm
    return v


def month_answer(rows, y, m):
    v = month_stats(rows, y, m)
    part = _partial(rows, y, m)
    when = f"So far in {_mname(y, m)}, to the sale of {_sd(rows[-1]['sale_date'])}," if part else f"In {_mname(y, m)}"
    sales = f"{v['sales']} sale{'s' if v['sales'] != 1 else ''}"
    txt = (f"{when} the Colombo tea auction held {sales} and sold {v['qty'] / 1000:.2f} million kg at an average of {T.rs(v['total'])} a kilo, weighted by quantity. ")
    if v["ly"]:
        txt += f"That is {_updown(T.pct(v['total'], v['ly']['total']))} on {'the same days of ' if part else ''}{_mname(y - 1, m)} ({T.rs(v['ly']['total'])}). "
    txt += f"Low Grown teas averaged {T.rs(v['low'])}, High Grown {T.rs(v['high'])} and Medium Grown {T.rs(v['medium'])}."
    return txt


def build_month(B, stories, rows, y, m, nav):
    path = f"{PRICES}{T.month_slug(y, m)}/"
    prefix = "../../../../"
    v = month_stats(rows, y, m)
    part = _partial(rows, y, m)
    name = _mname(y, m)
    best = max(v["rows"], key=lambda r: r["avg_total"])
    stats = [(T.rs(v["total"], 0), f"average a kilo, {name}{' so far' if part else ''}"),
             (T.signed(T.pct(v["total"], v["ly"]["total"])) if v["ly"] else "–", f"against {'the same days of ' if part else ''}{_mname(y - 1, m)}"),
             (f"{v['qty'] / 1000:.2f}M kg", f"sold at {v['sales']} sale{'s' if v['sales'] != 1 else ''}"),
             (T.rs(best["avg_total"], 0), f"highest sale average, {_sd(best['sale_date'])}")]
    sales_rows = "".join(f"<tr><td class=\"nw\">{_sd(r['sale_date'])}</td>" + "".join(f"<td>{r[f'avg_{k}']:,.2f}</td>" for k, _ in T.ELEV)
                         + f"<td><strong>{r['avg_total']:,.2f}</strong></td><td>{r['qty_total'] / 1000:.2f}</td></tr>" for r in reversed(v["rows"]))
    sales_head = "".join(f"<th>{h}</th>" for h in ["Sale", "High Grown, Rs", "Medium Grown, Rs", "Low Grown, Rs", "All teas, Rs", "Sold, million kg"])
    pm_name = _mname(*v["pm_key"])
    comp = ""
    for k, n in T.ELEV + [("total", "All teas")]:
        c1, k1 = _chg(v[k], v["pm"][k]) if v["pm"] else ("–", "")
        c2, k2 = _chg(v[k], v["ly"][k]) if v["ly"] else ("–", "")
        cell = f'<a href="{prefix}{PRICES}{ELEV_SLUG[k]}/">{n}</a>' if k in ELEV_SLUG else f"<strong>{n}</strong>"
        comp += (f"<tr><td>{cell}</td><td>{v[k]:,.2f}</td><td>{v['pm'][k]:,.2f}</td><td class=\"{k1}\">{c1}</td>" if v["pm"] else f"<tr><td>{cell}</td><td>{v[k]:,.2f}</td><td>–</td><td></td>")
        comp += (f"<td>{v['ly'][k]:,.2f}</td><td class=\"{k2}\">{c2}</td></tr>" if v["ly"] else "<td>–</td><td></td></tr>")
    comp_head = "".join(f"<th>{h}</th>" for h in ["Elevation", f"{name}, Rs", f"{pm_name}, Rs", "Change", f"{_mname(y - 1, m)}{' (same days)' if part else ''}, Rs", "Change"])
    leaf = ", ".join(f"{n} {T.rs(T.leaf_rate(v[k]), 0)}" for k, n in sorted(T.ELEV, key=lambda x: -v[x[0]]))
    prev_link = next_link = ""
    i = nav.index((y, m))
    if i > 0:
        prev_link = f'<a href="{_month_url(prefix, *nav[i - 1])}">&larr; {_mname(*nav[i - 1])}</a>'
    if i < len(nav) - 1:
        next_link = f'<a href="{_month_url(prefix, *nav[i + 1])}">{_mname(*nav[i + 1])} &rarr;</a>'
    faqs = [(f"What was the average Colombo tea auction price in {name}?", month_answer(rows, y, m))]
    if v["ly"]:
        faqs.append((f"How did tea prices in {name} compare with {_mname(y - 1, m)}?",
                     f"The all teas average was {T.rs(v['total'])} a kilo against {T.rs(v['ly']['total'])}{' over the same days' if part else ''}, {_updown(T.pct(v['total'], v['ly']['total']))}. "
                     + " ".join(f"{n} teas were {_updown(T.pct(v[k], v['ly'][k]))}." for k, n in T.ELEV)))
    faqs.append((f"What was the green leaf price in {name}?", f"The rate each factory pays depends on its own net sale average. As an estimate at the elevation average, the formula gives about {leaf} a kilo of green leaf. "
                 "Check the rate your factory announces, or work it out for your factory with the green leaf price calculator."))
    faq, faq_ld = SP.faq_block(stories, faqs)
    reviewed = f"{'Figures to the sale of ' + T.fdate(rows[-1]['sale_date']) + '. ' if part else ''}From Forbes &amp; Walker Tea Brokers' weekly figures; monthly averages are our calculation, weighted by quantity sold."
    body = _page_head([("Source from Sri Lanka", "../../../"), ("Ceylon tea", "../../"), ("Auction prices", "../")], f"Colombo tea auction prices, {name}", month_answer(rows, y, m), reviewed) + f"""
<section class="section top-0"><div class="wrap narrow">
  {SP.stats_strip(stats)}
  <h2 class="h-sub mt">Sales in {name}</h2>
  <div class="tbl"><table><thead><tr>{sales_head}</tr></thead><tbody>{sales_rows}</tbody></table></div>
  <p class="cap">{_src_line()}</p>
  <h2 class="h-sub mt">{name} against {pm_name} and {_mname(y - 1, m)}</h2>
  <div class="tbl"><table><thead><tr>{comp_head}</tr></thead><tbody>{comp}</tbody></table></div>
  <p class="cap">Monthly averages are our calculation from the weekly figures, weighted by quantity sold. The Sri Lanka Tea Board's official monthly national sale average is calculated differently and can differ by up to about 2%.</p>
  <h2 class="h-sub mt">Green leaf rate in {name}</h2>
  <p class="body-l">At the elevation average, the green leaf formula gives about {leaf} a kilo of leaf. Your factory's rate depends on its own net sale average: <a href="{prefix}{CALC}">work it out with the green leaf price calculator</a>.</p>
  <p class="body-l">{prev_link}{' · ' if prev_link and next_link else ''}{next_link}</p>
  <p class="body-l"><a href="../">Latest Colombo tea auction prices</a> · <a href="../{y}/">All of {y}</a> · <a href="{prefix}data/{CSV_NAME}" download>Every sale as CSV</a></p>
  {faq}
</div></section>
"""
    head = faq_ld + _crumbs(B, name, path)
    title = f"Colombo tea auction prices, {name}"
    B.write(path + "index.html", B.page(title, month_answer(rows, y, m), body, prefix, path, extra_head=head, active="source",
                                        seo_title=f"Tea auction prices {name}: Colombo averages", image=_og(OG_PRICES)))
    return path


# ------------------------------------------------------------------ year pages
def year_answer(rows, y):
    sel = [r for r in rows if r["sale_date"].year == y]
    last = sel[-1]["sale_date"]
    current = last.year == rows[-1]["sale_date"].year
    avg = {k: T.wavg(sel, k) for k in ("high", "medium", "low", "total")}
    prev = T.year_to_date(rows, y - 1, last) if current else {k: T.wavg([r for r in rows if r["sale_date"].year == y - 1], k) for k in ("high", "medium", "low", "total")}
    txt = (f"The Colombo tea auction averaged {T.rs(avg['total'])} a kilo across {len(sel)} sales in {y}{' to ' + _sd(last) if current else ''}, "
           f"selling {sum(r['qty_total'] for r in sel) / 1000:.1f} million kg. ")
    if prev.get("total"):
        txt += f"That is {_updown(T.pct(avg['total'], prev['total']))} on {'the same period of ' if current else ''}{y - 1}. "
    txt += f"By elevation: Low Grown {T.rs(avg['low'])}, High Grown {T.rs(avg['high'])}, Medium Grown {T.rs(avg['medium'])}."
    return txt, avg, prev, sel, current


def build_year(B, stories, rows, y):
    path = f"{PRICES}{y}/"
    prefix = "../../../../"
    txt, avg, prev, sel, current = year_answer(rows, y)
    mrows = ""
    by_total = []
    for yy, m, v in reversed(_months(sel)):
        t = T.wavg(v, "total")
        by_total.append((t, m))
        mrows += (f'<tr><td><a href="{_month_url(prefix, yy, m)}">{T.MONTH_NAMES[m - 1]}</a></td>' + "".join(f"<td>{T.wavg(v, k):,.2f}</td>" for k, _ in T.ELEV)
                  + f"<td><strong>{t:,.2f}</strong></td><td>{len(v)}</td><td>{sum(r['qty_total'] for r in v) / 1000:.2f}</td></tr>")
    mhead = "".join(f"<th>{h}</th>" for h in ["Month", "High Grown, Rs", "Medium Grown, Rs", "Low Grown, Rs", "All teas, Rs", "Sales", "Sold, million kg"])
    erows = ""
    for k, n in T.ELEV + [("total", "All teas")]:
        hi = max(sel, key=lambda r: r[f"avg_{k}"])
        lo = min(sel, key=lambda r: r[f"avg_{k}"])
        c, cls = _chg(avg[k], prev.get(k))
        cell = f'<a href="../{ELEV_SLUG[k]}/">{n}</a>' if k in ELEV_SLUG else f"<strong>{n}</strong>"
        erows += (f"<tr><td>{cell}</td><td>{avg[k]:,.2f}</td><td>{prev[k]:,.2f}</td><td class=\"{cls}\">{c}</td>" if prev.get(k) else f"<tr><td>{cell}</td><td>{avg[k]:,.2f}</td><td>–</td><td></td>")
        erows += f"<td>{hi[f'avg_{k}']:,.2f}<br><span class=\"cap\">{_sd(hi['sale_date'])}</span></td><td>{lo[f'avg_{k}']:,.2f}<br><span class=\"cap\">{_sd(lo['sale_date'])}</span></td></tr>"
    ehead = "".join(f"<th>{h}</th>" for h in ["Elevation", f"{y}{' to date' if current else ''}, Rs", f"{y - 1}{' same period' if current else ''}, Rs", "Change", "Highest sale, Rs", "Lowest sale, Rs"])
    top_t, top_m = max(by_total)
    faqs = [(f"What was the average Colombo tea auction price in {y}?", txt),
            (f"Which month of {y} had the highest Colombo tea auction prices?", f"{T.MONTH_NAMES[top_m - 1]}, at an all teas average of {T.rs(top_t)} a kilo, weighted by quantity sold{' (to ' + _sd(sel[-1]['sale_date']) + ')' if current else ''}.")]
    hi_all = max(sel, key=lambda r: r["avg_total"])
    faqs.append((f"What was the highest Colombo tea auction average in {y}?", f"{T.rs(hi_all['avg_total'])} a kilo for all teas at the sale of {T.fdate(hi_all['sale_date'])}. "
                 f"The highest elevation average was {T.rs(max(r['avg_low'] for r in sel))} for Low Grown teas."
                 if max(r["avg_low"] for r in sel) >= max(max(r["avg_high"] for r in sel), max(r["avg_medium"] for r in sel)) else
                 f"{T.rs(hi_all['avg_total'])} a kilo for all teas at the sale of {T.fdate(hi_all['sale_date'])}."))
    faq, faq_ld = SP.faq_block(stories, faqs)
    other = " · ".join(f'<a href="../{yy}/">Tea auction prices {yy}</a>' for yy in T.years(rows) if yy != y)
    body = _page_head([("Source from Sri Lanka", "../../../"), ("Ceylon tea", "../../"), ("Auction prices", "../")], f"Colombo tea auction prices {y}", txt,
                      "From Forbes &amp; Walker Tea Brokers' weekly figures; annual and monthly averages are our calculation, weighted by quantity sold.") + f"""
<section class="section top-0"><div class="wrap narrow">
  <h2 class="h-sub">{y} by elevation</h2>
  <div class="tbl"><table><thead><tr>{ehead}</tr></thead><tbody>{erows}</tbody></table></div>
  <p class="cap">{_src_line()}</p>
  <h2 class="h-sub mt">{y} by month</h2>
  <div class="tbl"><table><thead><tr>{mhead}</tr></thead><tbody>{mrows}</tbody></table></div>
  <p class="cap">Monthly averages weighted by quantity sold; the Sri Lanka Tea Board's official monthly national sale average can differ by up to about 2%.</p>
  <p class="body-l"><a href="../">Latest Colombo tea auction prices</a>{' · ' + other if other else ''} · <a href="{prefix}data/{CSV_NAME}" download>Every sale as CSV</a></p>
  {faq}
</div></section>
"""
    B.write(path + "index.html", B.page(f"Colombo tea auction prices {y}", txt, body, prefix, path, extra_head=faq_ld + _crumbs(B, str(y), path),
                                        active="source", seo_title=f"Colombo tea auction prices {y}: monthly averages", image=_og(OG_PRICES)))
    return path


# ------------------------------------------------------------------ elevation pages
def elevation_answer(rows, k, n):
    s = T.summary(rows)
    y, last = s["year"], s["last"]
    hi, hid, lo, lod = T.range_52w(rows, k)
    cur = [r for r in rows if r["sale_date"].year == y]
    ytd, prev = T.wavg(cur, k), T.year_to_date(rows, y - 1, last["sale_date"])[k]
    share = sum(r[f"qty_{k}"] for r in cur) / sum(r["qty_total"] for r in cur) * 100
    return (f"{n} teas averaged {T.rs(last[f'avg_{k}'])} a kilo at the Colombo tea auction sale of {T.fdate(last['sale_date'])}. "
            f"Over the past 52 weeks the weekly {n} average ranged from {T.rs(lo)} ({_sd(lod)}) to {T.rs(hi)} ({_sd(hid)}). "
            f"In {y} to date {n} teas averaged {T.rs(ytd)}, {_updown(T.pct(ytd, prev))} on the same period of {y - 1}, and made up {share:.0f}% of the quantity sold.")


def build_elevation(B, stories, rows, k, n):
    path = f"{PRICES}{ELEV_SLUG[k]}/"
    prefix = "../../../../"
    s = T.summary(rows)
    y = s["year"]
    txt = elevation_answer(rows, k, n)
    grown, market = ELEV_INFO[k]
    mrows = ""
    for yy, m, v in reversed([x for x in _months(rows) if x[0] == y]):
        ly = [r for r in rows if (r["sale_date"].year, r["sale_date"].month) == (yy - 1, m)]
        if _partial(rows, yy, m):
            ly = _same_days(rows, yy - 1, m, rows[-1]["sale_date"].day)
        a1, a0 = T.wavg(v, k), (T.wavg(ly, k) if ly else None)
        c, cls = _chg(a1, a0)
        mrows += (f'<tr><td><a href="{_month_url(prefix, yy, m)}">{_mname(yy, m)}</a></td><td><strong>{a1:,.2f}</strong></td><td>{f"{a0:,.2f}" if a0 else "–"}</td>'
                  f'<td class="{cls}">{c}</td><td>{sum(r[f"qty_{k}"] for r in v) / 1000:.2f}</td></tr>')
    mhead = "".join(f"<th>{h}</th>" for h in ["Month", f"{n}, Rs", f"Same month {y - 1}, Rs", "Change", f"{n} sold, million kg"])
    m_all = T.monthly(rows)
    (ly_, lm_), lv = list(m_all.items())[-1]
    if lv["sales"] < 3 and len(m_all) > 1:
        (ly_, lm_), lv = list(m_all.items())[-2]
    leaf = T.leaf_rate(lv[k])
    hi, hid, lo, lod = T.range_52w(rows, k)
    cur = [r for r in rows if r["sale_date"].year == y]
    share = sum(r[f"qty_{k}"] for r in cur) / sum(r["qty_total"] for r in cur) * 100
    faqs = [(f"What is the {n} tea price at the Colombo auction?", txt),
            (f"What was the highest {n} tea price in the past year?", f"The highest weekly {n} average in the 52 weeks to {_sd(s['last']['sale_date'])} was {T.rs(hi)} a kilo, at the sale of {T.fdate(hid)}. The lowest was {T.rs(lo)}, on {T.fdate(lod)}."),
            (f"What are {n} teas?", f"Ceylon teas {grown}, as the Tea Exporters Association defines the three elevations. {(market + ', according to the Export Development Board.') if market else ''}".strip()),
            (f"How much of the Colombo auction is {n} tea?", f"{share:.0f}% of the quantity sold in {y} to date.")]
    faq, faq_ld = SP.faq_block(stories, faqs)
    others = " · ".join(f'<a href="../{ELEV_SLUG[kk]}/">{nn} tea prices</a>' for kk, nn in T.ELEV if kk != k)
    body = _page_head([("Source from Sri Lanka", "../../../"), ("Ceylon tea", "../../"), ("Auction prices", "../")], f"{n} tea prices at the Colombo auction", txt,
                      f"Figures to the sale of {T.fdate(s['last']['sale_date'])}, from Forbes &amp; Walker Tea Brokers. We add each sale when the broker publishes it.") + f"""
<section class="section top-0"><div class="wrap narrow">
  {SP.stats_strip([(T.rs(s['last'][f'avg_{k}'], 0), f"{n} average a kilo, sale of {_sd(s['last']['sale_date'])}"), (T.rs(hi, 0), f"52-week high, {_sd(hid)}"), (T.rs(lo, 0), f"52-week low, {_sd(lod)}"), (f"{share:.0f}%", f"of {y} auction quantity")])}
  <h2 class="h-sub mt">Weekly {n} average price, {rows[0]['sale_date'].year} to {y}</h2>
  {chart(rows, [(k, n)], f"Colombo tea auction: weekly {n} average price")}
  <p class="cap">{_src_line()}</p>
  <h2 class="h-sub mt">{n} by month, {y} against {y - 1}</h2>
  <div class="tbl"><table><thead><tr>{mhead}</tr></thead><tbody>{mrows}</tbody></table></div>
  <p class="cap">Our calculation from the weekly figures, weighted by quantity sold. A month still in progress is compared with the same days a year earlier.</p>
  <h2 class="h-sub mt">What {n} teas are</h2>
  <p class="body-l">Ceylon teas {grown} ({a("Tea Exporters Association", GROWING)}).{(' ' + market + ' (' + a('Export Development Board', EDB_TEA) + ').') if market else ''}</p>
  <h2 class="h-sub mt">Green leaf rate at the {n} average</h2>
  <p class="body-l">At the {_mname(ly_, lm_)} {n} average of {T.rs(lv[k])}, the green leaf formula gives about {T.rs(leaf)} a kilo of leaf. Your factory's rate depends on its own net sale average: <a href="{prefix}{CALC}">green leaf price calculator</a>.</p>
  <p class="body-l"><a href="../">All elevations</a> · {others}</p>
  {faq}
</div></section>
{CHART_JS}
"""
    B.write(path + "index.html", B.page(f"{n} tea prices at the Colombo auction", txt, body, prefix, path, extra_head=faq_ld + _crumbs(B, f"{n} tea prices", path),
                                        active="source", seo_title=f"{n} tea prices: Colombo auction averages", image=_og(OG_PRICES)))
    return path


# ------------------------------------------------------------------ machine readable latest figures, answers page
def latest_json(B, rows):
    s = T.summary(rows)
    r = s["last"]
    m = T.monthly(rows)
    data = {
        "name": "Colombo tea auction prices", "url": f"{B.SITE_URL}/{PRICES}", "csv": f"{B.SITE_URL}/data/{CSV_NAME}",
        "source": "Forbes & Walker Tea Brokers, weekly tea auction quantities and averages", "source_url": T.FW_STATS,
        "units": {"price": "LKR per kg of made tea", "quantity": "thousand kg"},
        "latest_sale": {"date": r["sale_date"].isoformat(), **{f"avg_{k}": r[f"avg_{k}"] for k in ("high", "medium", "low", "total")},
                        "qty_total": r["qty_total"]},
        "year_to_date": {"year": s["year"], "sales": s["ytd"]["sales"], **{f"avg_{k}": round(s["ytd"][k], 2) for k in ("high", "medium", "low", "total")},
                         "change_vs_same_period_last_year_pct": round(s["chg_ytd"], 2) if s["chg_ytd"] is not None else None},
        "months": [{"month": f"{y}-{mo:02d}", "sales": v["sales"], **{f"avg_{k}": round(v[k], 2) for k in ("high", "medium", "low", "total")}}
                   for (y, mo), v in m.items()],
        "note": "Monthly figures are quantity weighted averages of each month's sales, calculated by Tech Destination Sri Lanka.",
    }
    B.write("data/" + LATEST_JSON, json.dumps(data, indent=1) + "\n")


def _answers():
    rows = T.load()
    s = T.summary(rows)
    m = T.monthly(rows)
    (y, mo), v = list(m.items())[-1]
    if v["sales"] < 3 and len(m) > 1:
        (y, mo), v = list(m.items())[-2]
    leaf = ", ".join(f"{n} about {T.rs(T.leaf_rate(v[k]), 0)}" for k, n in sorted(T.ELEV, key=lambda x: -v[x[0]]))
    top, bottom = s["last"]["avg_" + s["top"][0]], s["last"]["avg_" + s["bottom"][0]]
    return [
        ("What is the Colombo tea auction price this week?", answer(rows), PRICES),
        ("What is the green leaf price in Sri Lanka?", f"Each bought-leaf factory pays a rate set by a statutory formula from its own net sale average. At the {_mname(y, mo)} elevation averages the formula gives {leaf} a kilo of leaf.", CALC),
        ("Which Ceylon tea elevation sells for the most at auction?", f"{s['top'][1]} teas, at {T.rs(top)} a kilo at the sale of {T.fdate(s['last']['sale_date'])}, against {T.rs(bottom)} for {s['bottom'][1]}.", PRICES + ELEV_SLUG[s["top"][0]] + "/"),
    ]


ANSWERS = _answers()
