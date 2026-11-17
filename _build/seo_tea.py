"""Ceylon tea data pages: Colombo tea auction prices (weekly averages by elevation, monthly averages, CSV) and a green
leaf price calculator for bought-leaf factories. Figures come from tea_data.py, which _build/tea_update.py keeps current."""
import html
import json

import seo_pages as SP
import seo_source as SS
import tea_data as T
from seo_pages import a

e = html.escape
PRICES = "source/ceylon-tea/auction-prices/"
CALC = "source/ceylon-tea/green-leaf-price-calculator/"
CSV_NAME = "colombo-tea-auction-weekly-prices.csv"
COLORS = {"high": "#3a6fd8", "medium": "#d17a00", "low": "#11865f"}   # checked for colour blind separation
STUDY = "https://huggingface.co/papers/2608.24894"
SHORT = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def _sd(d):
    return f"{d.day} {SHORT[d.month - 1]} {d.year}"


def _src_line(prefix=""):
    return (f'Source: Forbes &amp; Walker Tea Brokers, {a("weekly tea auction quantities and averages", T.FW_STATS)}. '
            "Averages in Sri Lankan rupees per kilo of made tea, quantities sold in each sale.")


# ------------------------------------------------------------------ chart
def chart(rows):
    """Weekly average price per elevation as an inline SVG line chart, with a hover layer driven by the data attribute."""
    W, H, L, R, TOP, BOT = 680, 330, 52, 128, 14, 34
    d0, d1 = rows[0]["sale_date"].toordinal(), rows[-1]["sale_date"].toordinal()
    vals = [r[f"avg_{k}"] for r in rows for k, _ in T.ELEV]
    lo, hi = int(min(vals) // 100 * 100), int(-(-max(vals) // 100) * 100)
    X = lambda d: L + (d.toordinal() - d0) / (d1 - d0) * (W - L - R)  # noqa: E731
    Y = lambda v: TOP + (hi - v) / (hi - lo) * (H - TOP - BOT)  # noqa: E731
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="tea-ct tea-cd" class="tea-svg">',
           '<title id="tea-ct">Colombo tea auction: weekly average price by elevation</title>',
           f'<desc id="tea-cd">Average price in rupees per kilo at each Colombo sale from {_sd(rows[0]["sale_date"])} to {_sd(rows[-1]["sale_date"])}, '
           f'for High, Medium and Low Grown teas. The same figures are in the tables below and the CSV.</desc>']
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
    for k, name in T.ELEV:
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
               + "".join(f'<circle r="4.5" fill="{COLORS[k]}" stroke="#fff" stroke-width="2" data-k="{k}"/>' for k, _ in T.ELEV) + "</g>")
    out.append(f'<rect class="tea-hit" x="{L}" y="{TOP}" width="{W - L - R}" height="{H - TOP - BOT}" fill="transparent"/></svg>')
    data = {"x": [round(X(r["sale_date"]), 1) for r in rows], "d": [_sd(r["sale_date"]) for r in rows], "q": [round(r["qty_total"] / 1000, 2) for r in rows],
            "t": [r["avg_total"] for r in rows], "y": {k: [round(Y(r[f"avg_{k}"]), 1) for r in rows] for k, _ in T.ELEV},
            "v": {k: [r[f"avg_{k}"] for r in rows] for k, _ in T.ELEV}, "w": W}
    legend = "".join(f'<span><i style="background:{COLORS[k]}"></i>{n}</span>' for k, n in T.ELEV)
    return (f'<div class="tea-legend" aria-hidden="true">{legend}</div>'
            f'<div class="tea-chart" data-chart=\'{e(json.dumps(data))}\'><div class="tea-scroll">{"".join(out)}</div><div class="tea-tip" role="status"></div></div>')


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
    ['low', 'high', 'medium'].forEach(function (k) { h += '<br><i style="background:' + colors[k] + '"></i>' + names[k] + ': Rs ' + fmt(d.v[k][i]); });
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
         "The Sri Lanka Tea Board publishes the official monthly national sale average, which is calculated differently and can differ by 1 to 2%."),
        ("Do you forecast tea prices?", "We are testing forecasts of the next four to eight weeks by elevation, and will publish them only once they beat a simple "
         "benchmark: assuming the next sale repeats the last one. Leave your details on this page to get them first."),
    ]


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
  <h2 class="h-sub mt">Weekly average price by elevation, {rows[0]['sale_date'].year} to {r['sale_date'].year}</h2>
  <p class="body-l">Rupees per kilo at each sale. Hover or tap the chart to read a sale.</p>
  {chart(rows)}
  <p class="cap">{_src_line()}</p>
  <h2 class="h-sub mt">Latest sales</h2>
  {_latest_table(rows)}
  <p class="cap">{_src_line()} Change is our calculation.</p>
  <h2 class="h-sub mt">Monthly averages, {s['year']} against {s['year'] - 1}</h2>
  {_monthly_table(rows)}
  <p class="cap">Our calculation from the weekly figures, weighted by quantity sold. A month still in progress is compared with the same days a year earlier. The Sri Lanka Tea Board's official monthly national sale average is calculated differently and can differ by 1 to 2%.</p>
  <h2 class="h-sub mt">What moves Colombo prices</h2>
  <p class="body-l">A study of 105 weekly broker reports from November 2023 to March 2026 found market and structural factors, such as grade and catalogue, drive prices far more than weather. Weather is a secondary, lagged signal: Low Grown prices responded to rain and sunshine one to three weeks earlier, while High Grown prices showed no lasting weather effect ({a("study, August 2026", STUDY)}).</p>
  <div class="cite"><strong>Use this data.</strong> <a href="{prefix}data/{CSV_NAME}" download>Download every sale as CSV</a>. The weekly figures are Forbes &amp; Walker Tea Brokers'; credit them as the source, and link to this page if you use our charts or monthly averages.<br><span>Suggested credit: Forbes &amp; Walker Tea Brokers, compiled by Tech Destination Sri Lanka, {B.SITE_URL}/{PRICES}</span></div>
  {form}
  <h2 class="h-sub mt">Run a bought-leaf tea factory?</h2>
  <p class="body-l">See the green leaf rate your net sale average supports, and what happens to it if prices move: <a href="../green-leaf-price-calculator/">green leaf price calculator</a>.</p>
  <h2 class="h-sub mt">Buying Ceylon tea?</h2>
  <p class="body-l">Grades, the Lion logo, certificates and how to buy from Sri Lankan exporters: <a href="../">Ceylon tea suppliers and exporters</a>. Or <a href="../../request-a-quote/?product=ceylon-tea">request a quote</a> and we will introduce exporters who ship to your market.</p>
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
    desc = (f"Average prices at every Colombo tea auction sale since {rows[0]['sale_date'].year} for High, Medium and Low Grown teas, "
            "with monthly averages, quantities sold and a CSV download. Updated weekly.")
    B.write(PRICES + "index.html", B.page("Colombo tea auction prices: weekly averages by elevation", desc, body, prefix, PRICES, extra_head=head,
                                          active="source", seo_title="Colombo tea auction prices: weekly averages"))
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
    ]
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
    <p class="cap">The elevation average is filled in with our {e(month)} Colombo auction average for that elevation, weighted by quantity sold, from Forbes &amp; Walker Tea Brokers' weekly figures (<a href="../auction-prices/">see the prices</a>). Use the Tea Board's official figure for the month if you have it; it can differ by 1 to 2%. The scenarios hold the elevation average fixed.</p>
  </div>
  <h2 class="h-sub mt">The formula</h2>
  <p class="body-l">As documented by the Tea Research Institute in 2003, with NSA the factory's net sale average and EA the elevation average:</p>
  <ul class="ticks"><li>If NSA is at or below EA: leaf rate = out-turn × 68% × NSA</li><li>If NSA is above EA: leaf rate = out-turn × (68% × EA + 50% × (NSA − EA))</li><li>Out-turn: 22.22 kg of made tea from 100 kg of green leaf</li></ul>
  <p class="body-l">Change the settings above if the Tea Commissioner's Division has revised any of these.</p>
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
    head = faq_ld + SP.crumbs_ld(B, [("Source from Sri Lanka", "source/"), ("Ceylon tea", "source/ceylon-tea/"), ("Green leaf price calculator", CALC)])
    B.write(CALC + "index.html", B.page("Green leaf price calculator for Sri Lankan tea factories",
                                        "Work out the green leaf rate a bought-leaf tea factory pays under Sri Lanka's price formula, from its net sale average and the elevation average, with what-if scenarios.",
                                        body, prefix, CALC, extra_head=head, active="source", seo_title="Green leaf price calculator: Sri Lanka tea leaf rate"))
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
  <p class="body-l"><a href="auction-prices/">Every sale since {rows[0]['sale_date'].year}, monthly averages and a CSV</a> · <a href="green-leaf-price-calculator/">Green leaf price calculator for factories</a></p>"""


def llms_lines(B):
    rows = T.load()
    return ["", "## Ceylon tea prices",
            f"- [Colombo tea auction prices: weekly averages by elevation]({B.SITE_URL}/{PRICES}): {answer(rows)} CSV: {B.SITE_URL}/data/{CSV_NAME}",
            f"- [Green leaf price calculator for Sri Lankan tea factories]({B.SITE_URL}/{CALC}): The green leaf rate a bought-leaf factory pays under Sri Lanka's price formula, from its net sale average and the elevation average."]


def build(B, stories):
    rows = T.load()
    return [build_prices(B, stories, rows), build_calculator(B, stories, rows)]
