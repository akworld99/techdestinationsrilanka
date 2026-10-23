"""Comparison pages, the team cost calculator, the employer of record guide, the answers page and the playbook download."""
import html
import json

import extra
import seo_pages as SP
from seo_pages import a

e = html.escape

EF = "https://www.ef.com/wwen/epi/"
UVIK = "https://uvik.net/blog/global-software-developer-rates-2026/"
ACC = "https://www.accelerance.com/blog/2026-outsourcing-rate-trends-asia-europe-latam"
GII = "https://www.wipo.int/edocs/gii-ranking/2025/{}.pdf"

LK = dict(name="Sri Lanka", tz="UTC+5:30, no daylight saving", ef="73rd of 123, score 486 (low band)", work="About 175,000 IT and BPM professionals (SLASSCOM, 2026)",
          rate="About USD 25 to 40 an hour (Export Development Board). Asia senior average USD 31 to 41 (Accelerance 2026)", gii="93rd of 139", kearney="23rd of 60 (2021 edition)")

OTHERS = [
    dict(slug="vietnam", name="Vietnam", cc="vn", tz="UTC+7, no daylight saving", ef="64th of 123, score 500 (moderate band)", efurl=EF + "regions/asia/vietnam/",
         work="About 530,000 programmers (TopDev, 2023)", rate="Senior USD 22 to 50 an hour (Uvik index 2026, vendor data)", gii="44th of 139", kearney="7th of 78 (2023 edition)",
         answer="Vietnam is the bigger market, with about 530,000 programmers and a top ten place in Kearney's 2023 services location index. Sri Lanka is smaller, with about 175,000 IT and business process professionals, but has a longer record of core product R&D for Western software companies: IFS, Sysco, Synopsys and the London Stock Exchange Group all build there. Choose Vietnam for scale and hardware adjacent work. Choose Sri Lanka for long running product teams, enterprise software and business in English.",
         theirs=["Scale: roughly three times the technical workforce, with more than 50,000 people entering IT study each year.", "Higher placings in Kearney's index (7th) and the Global Innovation Index (44th against 93rd).", "A large electronics and hardware industry, and new chip design centres such as Qualcomm's in Hanoi.", "Two more hours of overlap with East Asia and Australia."],
         ours=["English is the working language of the export sector, a legacy of the education system and decades serving UK, US and Nordic clients.", "Depth in enterprise software and ERP: IFS does about 60% of its global product development in Colombo.", "Product companies built and sold from Colombo, including WSO2 for USD 600 million.", "Two more hours of overlap with Europe and the Gulf.", "A strong accounting and finance talent base alongside engineering."],
         watch=[("Vietnam", "Industry reports project a shortage of 150,000 to 200,000 programmers a year, and say only about 30% of graduates meet employers' practical requirements.", "https://daibieunhandan.vn/thieu-hut-so-luong-lon-nhan-su-nganh-it-10319493.html"),
                ("Sri Lanka", "A smaller pool, so teams of several hundred take planning. The country is in an IMF programme that runs to March 2027 after its 2022 crisis.", "https://www.imf.org/en/news/articles/2026/05/27/pr26172-sri-lanka-imf-completes-combined-5th-and-6th-reviews-under-eff")]),
    dict(slug="philippines", name="the Philippines", cc="ph", tz="UTC+8, no daylight saving", ef="28th of 123, score 569 (high band)", efurl=EF + "regions/asia/philippines/",
         work="1.9 million IT and BPM workers, mostly contact centre and back office (IBPAP, 2025)", rate="Senior USD 25 to 45 an hour (Uvik index 2026, vendor data)", gii="50th of 139", kearney="12th of 78 (2023 edition)",
         answer="The Philippines is far larger in business process outsourcing, with 1.9 million workers and the best English score in Asia on the EF index. Most of that workforce is contact centre and back office. Sri Lanka is a smaller market weighted toward software engineering, product R&D and qualified finance work. Choose the Philippines for customer support and voice at scale. Choose Sri Lanka for software engineering, ERP and accounting.",
         theirs=["English: 28th in the world on the EF index, against 73rd for Sri Lanka.", "Scale in customer support, voice and back office, with USD 40 billion in sector revenue.", "Strong cultural familiarity with the US and a time zone that suits Australia.", "Higher placings in Kearney's index and the Global Innovation Index."],
         ours=["A sector built around software: IFS, Sysco, Synopsys and Zebra run engineering and R&D in Colombo.", "Product companies founded locally and acquired by global buyers, such as WSO2 and Virtusa.", "One of the largest pools of CIMA and ACCA accountants outside the UK.", "Better overlap with Europe and the Gulf: three and a half hours closer than Manila."],
         watch=[("The Philippines", "The industry body itself lists availability of employable talent and competition from other locations as constraints. One sourcing adviser describes the country as mainly call centre territory.", "https://www.philstar.com/business/2026/01/29/2504140/it-bpm-revenues-breach-40-billion-mark/amp/"),
                ("Sri Lanka", "National English scores are lower. Engineers at export companies work in English daily, so interview for it instead of assuming either way.", EF + "regions/asia/sri-lanka/")]),
    dict(slug="poland", name="Poland", cc="pl", tz="UTC+1, UTC+2 in summer", ef="15th of 123, score 600 (very high band)", efurl=EF + "regions/europe/poland/",
         work="About 554,000 ICT specialists (Eurostat, 2020)", rate="Senior USD 45 to 60 an hour (Uvik index 2026, vendor data). Europe senior average USD 64 to 76 (Accelerance 2026)", gii="39th of 139", kearney="13th of 78 (2023 edition)",
         answer="Poland is Europe's largest nearshore engineering market, inside the EU, with very high English and Google's biggest EU engineering hub. It costs roughly twice as much as Sri Lanka: senior rates of USD 45 to 60 an hour against about USD 25 to 40. Choose Poland when you need EU jurisdiction, the same time zone and short flights. Choose Sri Lanka when budget matters and four to five hours of daily overlap is enough.",
         theirs=["EU membership: data protection, contracts and travel are simpler for European buyers.", "English: 15th in the world on the EF index.", "Same working day as Western Europe.", "A workforce of more than half a million ICT specialists.", "Higher placings on every general ranking."],
         ours=["Cost: Asian senior rates average USD 31 to 41 an hour against USD 64 to 76 for Europe, according to Accelerance.", "Retention stories of 15 and 25 years with Nordic clients.", "Less competition for talent from local big tech.", "Nordic companies already here at scale, led by IFS."],
         watch=[("Poland", "Rising wage costs, difficulty accessing IT talent and a stronger currency are squeezing exporters.", "https://brandsit.pl/?p=1973350"),
                ("Sri Lanka", "Outside the EU, so check data transfer requirements. Three and a half to four and a half hours ahead of Central Europe.", "")]),
    dict(slug="ukraine", name="Ukraine", cc="ua", tz="UTC+2, UTC+3 in summer", ef="45th of 123, score 526 (moderate band)", efurl=EF + "regions/europe/ukraine/",
         work="About 303,000 IT specialists, of whom about 245,000 are in Ukraine (Lviv IT Cluster, 2025)", rate="Senior USD 35 to 55 an hour (Uvik index 2026, vendor data)", gii="66th of 139", kearney="42nd of 60 (2021 edition)",
         answer="Ukraine has a deep engineering culture and exported USD 6.45 billion of IT services in 2024, about four times Sri Lanka's total. The war is the deciding factor: 75% of Ukrainian IT companies have mobilised employees and most new sites opened in 2025 were abroad. Many buyers now add a second location. Sri Lanka offers lower rates and no conflict risk, at the cost of a wider time difference from Europe.",
         theirs=["A larger and very strong engineering workforce with a long record in product development.", "Same working day as Europe.", "Higher English and innovation rankings."],
         ours=["No war risk to people, power or continuity.", "Lower rates: about USD 25 to 40 an hour against USD 35 to 55.", "Better overlap with the Gulf, Asia and Australia.", "A stable base that global companies have used for 20 years and more."],
         watch=[("Ukraine", "75% of IT companies have mobilised staff and one in five specialists is considering emigrating, according to the 2025 Lviv IT Cluster study.", "https://scroll.media/en/?p=31670"),
                ("Sri Lanka", "An economy still in an IMF programme after the 2022 crisis. The IMF rates performance as generally strong but says debt risks remain high.", "https://www.imf.org/en/news/articles/2026/05/27/pr26172-sri-lanka-imf-completes-combined-5th-and-6th-reviews-under-eff")]),
    dict(slug="romania", name="Romania", cc="ro", tz="UTC+2, UTC+3 in summer", ef="11th of 123, score 605 (very high band)", efurl=EF + "regions/europe/romania/",
         work="195,929 IT employees (ANIS, 2024)", rate="Senior USD 40 to 55 an hour (Uvik index 2026, vendor data)", gii="49th of 139", kearney="30th of 78 (2023 edition)",
         answer="Romania combines EU membership with the best English score of any major outsourcing country, 11th in the world. Its IT workforce is about the size of Sri Lanka's and costs more: senior rates of USD 40 to 55 an hour against about USD 25 to 40. Romania removed its income tax exemption for IT workers in 2025. Choose Romania for EU jurisdiction and time zone. Choose Sri Lanka for cost and for enterprise software depth.",
         theirs=["EU membership and a European working day.", "English: 11th in the world on the EF index.", "Engineering centres for Oracle, Microsoft and Amazon."],
         ours=["Lower cost at similar workforce size.", "A 15% tax rate on exported services, against rising labour taxes in Romania.", "Core R&D for IFS, Sysco and Synopsys, and locally built companies sold to global buyers."],
         watch=[("Romania", "The IT income tax exemption ended on 1 January 2025 with no replacement, and the industry body says headcount has been flat since 2022.", "https://boundlesshq.com/blog/romania-it-tax-exemption-after-abolition/"),
                ("Sri Lanka", "Outside the EU and three and a half hours ahead of Bucharest in summer.", "")]),
    dict(slug="latin-america", name="Latin America", cc="mx", tz="Mexico UTC-6, Colombia UTC-5", ef="Mexico 103rd, Colombia 76th of 123 (very low and low bands)", efurl=EF + "regions/latin-america/mexico/",
         work="Colombia: 406,000 in software and IT (Fedesoft, 2026). Mexico: no reliable developer count", rate="Senior USD 40 to 55 an hour (Uvik index 2026, vendor data). Region senior average USD 60 to 75 (Accelerance 2026)", gii="Mexico 58th, Colombia 71st of 139", kearney="Mexico 11th, Colombia 13th of 60 (2021 edition)",
         answer="For US companies, Mexico and Colombia offer something Sri Lanka cannot: the same working day. They cost more, with senior rates of USD 40 to 55 an hour and regional averages up to USD 75, against about USD 25 to 40 for Sri Lanka. National English scores are lower in Mexico and similar in Colombia. Choose Latin America when real time collaboration all day is essential. Choose Sri Lanka when a shifted schedule or overnight progress works and cost matters.",
         theirs=["Full overlap with US working hours and short flights.", "Higher placings in Kearney's index and the Global Innovation Index.", "Large domestic technology markets."],
         ours=["Cost: roughly half the hourly rate on published figures.", "English: Sri Lanka scores above Mexico and level with Colombia on the EF index, and its export sector works in English.", "US companies already run core engineering here, including Sysco, Synopsys and Zebra.", "Work handed over at the end of the US day is ready the next morning."],
         watch=[("Latin America", "Colombia's software federation reports a gap of 83,000 professionals. A ManpowerGroup projection put Mexico's IT talent deficit at 77%.", "https://forbes.co/tecnologia/el-software-colombiano-alcanza-us1-800-millones-en-exportaciones-y-enfrenta-brecha-de-83-000-talentos"),
                ("Sri Lanka", "Nine and a half to ten and a half hours ahead of US Eastern time, so overlap needs a later shift in Colombo. About 17 hours flying time from New York.", "https://www.accelerance.com/country/sri-lanka")]),
]


def build_compare(B, stories):
    paths = []
    for o in OTHERS:
        prefix = "../../"
        N = o["name"]
        Ncap = N[0].upper() + N[1:]
        rows = "".join(f"<tr><td>{e(k)}</td><td>{e(LK[f])}</td><td>{e(o[f])}</td></tr>" for k, f in [("Time zone", "tz"), ("English, EF index 2025", "ef"), ("Workforce", "work"), ("Typical rates", "rate"), ("Global Innovation Index 2025", "gii"), ("Kearney services location index", "kearney")])
        faqs = [
            (f"Is Sri Lanka or {N} better for software outsourcing?", o["answer"]),
            (f"Is Sri Lanka cheaper than {N} for software development?", f"Published rates for Sri Lanka are about USD 25 to 40 an hour according to the Export Development Board. For {N}: {o['rate']}. The sources use different methods, so treat the comparison as indicative and ask for quotes."),
            (f"How does English in Sri Lanka compare with {N}?", f"On the EF English Proficiency Index 2025 Sri Lanka ranks 73rd of 123 countries. {Ncap}: {o['ef']}. The index tests the general adult population. Sri Lanka's export technology sector works in English."),
        ]
        faq, faq_ld = SP.faq_block(stories, faqs)
        watch = "".join(f"<li><strong>{e(w)}:</strong> {e(t)}{(' ' + a('Source', u)) if u else ''}</li>" for w, t, u in o["watch"])
        others = SP.chip_links([(f"Sri Lanka vs {x['name']}", f"../{x['slug']}/") for x in OTHERS if x is not o])
        body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Compare destinations", "../")])}
  <h1>Sri Lanka vs {e(N)} for software development and outsourcing</h1>
  <p class="answer">{e(o['answer'])}</p>
  <p class="reviewed">Last reviewed {SP.REVIEWED}. We publish from Sri Lanka, so we have tried to be hard on our own side. Every figure names its source.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <div class="tbl"><table><thead><tr><th></th><th>Sri Lanka</th><th>{e(Ncap)}</th></tr></thead><tbody>{rows}</tbody></table></div>
  <p class="cap mt-s">Sources: {a("EF English Proficiency Index 2025", o["efurl"])}, {a("Uvik rate index 2026", UVIK)}, {a("Accelerance 2026 rates guide", ACC)}, {a("WIPO Global Innovation Index 2025", GII.format(o["cc"]))}, Kearney Global Services Location Index. Workforce figures count different things in each country and are not directly comparable.</p>
  <div class="vs">
    <div><h2>Where {e(N)} is stronger</h2><ul class="ticks">{''.join(f'<li>{e(x)}</li>' for x in o['theirs'])}</ul></div>
    <div><h2>Where Sri Lanka is stronger</h2><ul class="ticks">{''.join(f'<li>{e(x)}</li>' for x in o['ours'])}</ul></div>
  </div>
  <h2 class="h-sub mt">What to watch in each</h2>
  <ul class="ticks">{watch}</ul>
  <div class="reach mt"><h2>Considering Sri Lanka alongside {e(N)}?</h2><p>Many companies run two locations. Tell us what you need and we will give you a straight view of whether Sri Lanka fits, and introduce people if it does.</p>
  <div class="actions"><a class="btn" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a><a class="btn btn-ghost" href="{prefix}talent/find/">Find talent</a><a class="btn btn-ghost" href="{prefix}tools/team-cost-calculator/">Estimate team cost</a></div></div>
  {faq}
  <h2 class="h-sub mt">Other comparisons</h2>{others}
</div></section>
"""
        path = f"compare/{o['slug']}/"
        head = faq_ld + SP.crumbs_ld(B, [("Compare destinations", "compare/"), (f"Sri Lanka vs {Ncap}", path)])
        B.write(path + "index.html", B.page(f"Sri Lanka vs {Ncap}: software outsourcing compared", f"Sri Lanka and {N} compared for offshore software development: rates, English, workforce, time zones and risks, with sources and an honest view of each.", body, prefix, path, extra_head=head, active="why"))
        paths.append(path)

    cols = [("tz", "Time zone"), ("ef", "English, EF 2025"), ("rate", "Typical rates"), ("gii", "Innovation index")]
    rows = "<tr><td><strong>Sri Lanka</strong></td>" + "".join(f"<td>{e(LK[k])}</td>" for k, _ in cols) + "</tr>"
    rows += "".join(f'<tr><td><a href="{o["slug"]}/"><strong>{e(o["name"][0].upper() + o["name"][1:])}</strong></a></td>' + "".join(f"<td>{e(o[k])}</td>" for k, _ in cols) + "</tr>" for o in OTHERS)
    faqs = [
        ("Which country is best for outsourcing software development?", "It depends on what you need. Poland and Romania suit buyers who need EU jurisdiction and a European working day. Mexico and Colombia suit US companies that need full day overlap. Vietnam and the Philippines offer scale. Sri Lanka suits long running product engineering, enterprise software and finance work at Asian rates, with an export sector that works in English."),
        ("Which offshore destinations are cheapest?", "Accelerance's 2026 guide puts senior rates in Asia at USD 31 to 41 an hour, against USD 64 to 76 in Europe and USD 60 to 75 in Latin America. Sri Lanka's Export Development Board cites about USD 25 to 40 an hour."),
        ("Is Sri Lanka a recognised outsourcing destination?", "Yes. Kearney ranked it 23rd of 60 countries in its 2021 Global Services Location Index, and the UK's National Outsourcing Association named it Outsourcing Destination of the Year in 2013."),
    ]
    faq, faq_ld = SP.faq_block(stories, faqs)
    body = f"""
<section class="page-head"><div class="wrap">
  <h1>Sri Lanka compared with other offshore development destinations</h1>
  <p class="answer">Sri Lanka is one of the lower cost offshore destinations, with rates of about USD 25 to 40 an hour, and a small but deep engineering base that runs core R&D for IFS, Sysco and Synopsys. It ranks below Eastern Europe and Southeast Asia on general English and innovation indices, and above them on cost. The pages below compare it with each alternative, including where the alternative is the better choice.</p>
</div></section>
<section class="section top-0"><div class="wrap">
  <div class="tbl"><table><thead><tr><th>Destination</th>{''.join(f'<th>{e(l)}</th>' for _, l in cols)}</tr></thead><tbody>{rows}</tbody></table></div>
  <p class="cap mt-s">Sources: EF English Proficiency Index 2025, Uvik rate index 2026 and Accelerance 2026 (both vendor data), Export Development Board of Sri Lanka, WIPO Global Innovation Index 2025.</p>
  <div class="reach mt"><h2>Want a straight answer for your case?</h2><p>Tell us the team, the stack and where you are based. If Sri Lanka is not the right fit we will say so.</p>
  <div class="actions"><a class="btn" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a><a class="btn btn-ghost" href="../tools/team-cost-calculator/">Estimate team cost</a><a class="btn btn-ghost" href="../solutions/software-outsourcing-sri-lanka/">Outsourcing to Sri Lanka</a></div></div>
  <div class="narrow-in">{faq}</div>
</div></section>
"""
    B.write("compare/index.html", B.page("Offshore development destinations compared with Sri Lanka", "Sri Lanka compared with Vietnam, the Philippines, Poland, Ukraine, Romania and Latin America for software outsourcing: rates, English, time zones and risks.", body, "../", "compare/",
                                        extra_head=faq_ld + SP.crumbs_ld(B, [("Compare destinations", "compare/")]), active="why"))
    return paths + ["compare/"]


# ------------------------------------------------------------------ calculator
def build_calculator(B, stories):
    roles = [(role, med) for _, items in SP.GLASSDOOR for role, med, _, _ in items]
    data = json.dumps({"fx": SP.FX, "roles": roles})
    f = extra.form(B, "calculator-estimate", "Get this estimate checked", "Send us your numbers and we will reply with what companies are really paying for that team, and who can build it.", [
        ("text", "name", "Your name", True, ""), ("email", "email", "Work email", True, ""), ("text", "company", "Company", False, ""),
        ("textarea", "estimate", "Your estimate", False, ""),
    ], "Send my estimate", "Sent. We will reply by email.")
    faqs = [
        ("How much does a development team in Sri Lanka cost?", f"As a guide, five software engineers and two senior engineers employed directly at median local pay cost roughly USD {round((5 * 177 + 2 * 260) * 1000 * 12 * 1.15 / SP.FX / 1000) * 1000:,} a year including statutory contributions. At the higher pay export companies report, the same team costs about 60% more. Through a partner company, budget USD 25 to 40 an hour per person."),
        ("What is included in the employer cost?", "Gross salary plus the employer's 12% provident fund and 3% trust fund contributions. It does not include office space, equipment, medical cover, gratuity provisions or an employer of record fee."),
        ("Why are there two pay levels?", "Self reported local medians are well below what export focused and dollar pegged employers pay. Good engineers cost closer to the higher level."),
    ]
    faq, faq_ld = SP.faq_block(stories, faqs)
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Guides", "../../guides/")])}
  <h1>Sri Lanka team cost calculator</h1>
  <p class="answer">Pick the roles and the team size to see what a team in Sri Lanka costs per month and per year, employed directly or through a partner company. Figures use 2026 pay data and include statutory employer contributions.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <div class="calc" id="calc" data-calc='{e(data)}'>
    <div class="calc-rows" id="calc-rows"></div>
    <button class="btn btn-ghost btn-small" type="button" id="calc-add">Add a role</button>
    <fieldset class="calc-level"><legend>Pay level</legend>
      <label class="check"><input type="radio" name="lvl" value="1" checked> Local median</label>
      <label class="check"><input type="radio" name="lvl" value="1.6"> Export company level</label>
    </fieldset>
    <dl class="facts calc-out">
      <div><dt id="c-people">0</dt><dd>people</dd></div>
      <div><dt id="c-month">0</dt><dd>USD a month, employed directly</dd></div>
      <div><dt id="c-year">0</dt><dd>USD a year, employed directly</dd></div>
      <div><dt id="c-partner">0</dt><dd>USD a year through a partner company</dd></div>
    </dl>
    <p class="cap">Direct cost is median monthly pay from self reported Glassdoor data for Colombo (2026), plus 15% statutory contributions, at LKR {SP.FX} per dollar. Export company level multiplies pay by 1.6, the gap we found between local medians and community reported pay at export employers. Partner cost assumes USD 25 to 40 an hour for 160 hours a month, per the Export Development Board. The partner figure is a billing rate: it also covers management, office, equipment, recruitment, bench time and the partner's margin, which is why it is several times the salary cost. See the <a href="../../guides/sri-lanka-tech-salaries/">salary guide</a> for sources and caveats.</p>
  </div>
  {f}
  {faq}
</div></section>
<script>
(function () {{
  var el = document.getElementById('calc'); var d = JSON.parse(el.dataset.calc); var rows = document.getElementById('calc-rows');
  function fmt(n) {{ return Math.round(n / 100) * 100 >= 1000 ? (Math.round(n / 100) * 100).toLocaleString('en-US') : String(Math.round(n)); }}
  function addRow(idx, n) {{
    var r = document.createElement('div'); r.className = 'calc-row';
    var s = document.createElement('select'); s.setAttribute('aria-label', 'Role');
    d.roles.forEach(function (x, i) {{ var o = document.createElement('option'); o.value = i; o.textContent = x[0]; s.appendChild(o); }});
    s.value = idx;
    var q = document.createElement('input'); q.type = 'number'; q.min = 0; q.max = 500; q.value = n; q.setAttribute('aria-label', 'Number of people');
    var x = document.createElement('button'); x.type = 'button'; x.className = 'calc-x'; x.textContent = 'Remove'; x.addEventListener('click', function () {{ r.remove(); calc(); }});
    r.appendChild(s); r.appendChild(q); r.appendChild(x); rows.appendChild(r);
    s.addEventListener('change', calc); q.addEventListener('input', calc);
  }}
  function calc() {{
    var lvl = parseFloat(document.querySelector('input[name=lvl]:checked').value); var people = 0, lkr = 0, lines = [];
    Array.prototype.forEach.call(rows.children, function (r) {{
      var role = d.roles[r.querySelector('select').value]; var n = Math.max(0, parseInt(r.querySelector('input').value, 10) || 0);
      people += n; lkr += n * role[1] * 1000 * lvl; if (n) lines.push(n + ' x ' + role[0]);
    }});
    var month = lkr * 1.15 / d.fx;
    document.getElementById('c-people').textContent = people;
    document.getElementById('c-month').textContent = fmt(month);
    document.getElementById('c-year').textContent = fmt(month * 12);
    document.getElementById('c-partner').textContent = fmt(people * 25 * 160 * 12) + ' to ' + fmt(people * 40 * 160 * 12);
    var t = document.querySelector('#calculator-estimate-form textarea[name=estimate]');
    if (t) t.value = lines.join(', ') + '. Pay level: ' + (lvl > 1 ? 'export company' : 'local median') + '. Direct: USD ' + fmt(month * 12) + ' a year.';
  }}
  addRow(1, 4); addRow(2, 2); addRow(6, 1);
  document.getElementById('calc-add').addEventListener('click', function () {{ addRow(1, 1); calc(); }});
  Array.prototype.forEach.call(document.querySelectorAll('input[name=lvl]'), function (i) {{ i.addEventListener('change', calc); }});
  calc();
}})();
</script>
"""
    path = "tools/team-cost-calculator/"
    head = faq_ld + SP.crumbs_ld(B, [("Guides", "guides/"), ("Team cost calculator", path)])
    B.write(path + "index.html", B.page("Sri Lanka software team cost calculator 2026", "Estimate the monthly and yearly cost of a software team in Sri Lanka by role and size, employed directly or through a partner company. 2026 data.", body, "../../", path, extra_head=head, active="guides"))
    return path


# ------------------------------------------------------------------ employer of record
def build_eor(B, stories):
    prefix = "../../"
    faqs = [
        ("What is an employer of record in Sri Lanka?", "A company with a legal entity in Sri Lanka that employs people on your behalf. It issues the local contract, runs payroll, pays provident fund and trust fund contributions and handles tax, while you manage the person's work."),
        ("Which employer of record providers cover Sri Lanka?", "Deel, Remote, G-P and Multiplier all list Sri Lanka on their own sites. Remote states that it owns a local entity."),
        ("How much does an employer of record cost in Sri Lanka?", "You pay the employee's salary, 15% in statutory contributions (12% provident fund and 3% trust fund) and the provider's monthly fee per employee, which each provider publishes or quotes."),
        ("When should I move from an employer of record to my own company?", "Usually once you pass 20 to 30 people or want local contracts, an office and a brand in the hiring market. Registration takes about two weeks."),
    ]
    faq, faq_ld = SP.faq_block(stories, faqs)
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Guides", "../")])}
  <h1>Employer of record in Sri Lanka</h1>
  <p class="answer">An employer of record lets you hire people in Sri Lanka without registering a company. The provider employs them locally, runs payroll and pays statutory contributions, and you manage their work. Deel, Remote, G-P and Multiplier all cover Sri Lanka. It is the fastest route for one to ten hires.</p>
  <p class="reviewed">Last reviewed {SP.REVIEWED}. General information, not legal advice.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <h2 class="h-sub">Providers that list Sri Lanka</h2>
  <ul class="ticks">
    <li>{a("Deel", "https://www.deel.com/hiring/employees/sri-lanka/")}</li>
    <li>{a("Remote", "https://remote.com/country-explorer/sri-lanka")}, which states it owns a local entity</li>
    <li>{a("G-P", "https://www.globalization-partners.com/globalpedia/sri-lanka-employer-of-record")}</li>
    <li>{a("Multiplier", "https://www.usemultiplier.com/srilanka/employer-of-record")}</li>
  </ul>
  <p class="body-l">We have no commercial relationship with these providers. Their own country guides disagree with each other on details such as leave and holidays, so check anything important against the <a href="../how-to-hire-in-sri-lanka/">employment rules we have sourced</a>.</p>
  <h2 class="h-sub mt">What you pay</h2>
  <ul class="ticks">
    <li>Gross salary. See the <a href="../sri-lanka-tech-salaries/">salary guide</a> for 2026 ranges by role.</li>
    <li>Employer provident fund contribution of 12% and trust fund contribution of 3%.</li>
    <li>The provider's monthly fee per employee.</li>
    <li>Any benefits you choose to add, such as medical cover.</li>
    <li>For the full cost breakdown and payroll rules, see <a href="../pay-employees-and-contractors-in-sri-lanka/">how to pay employees and contractors</a>.</li>
  </ul>
  <h2 class="h-sub mt">What an employer of record does not do</h2>
  <p class="body-l">It does not find the people. You still need to source, interview and select. That is the part we help with: tell us the roles and we introduce candidates or partner teams, and you can employ them through whichever provider you prefer.</p>
  <h2 class="h-sub mt">Know the termination rules</h2>
  <p class="body-l">Sri Lankan law restricts non disciplinary termination for employers with 15 or more staff once someone has more than 180 days of service. Your provider is the legal employer, so ask how they handle it before you sign.</p>
  <div class="reach mt"><h2>Need the people first?</h2><p>We introduce Sri Lankan engineers and specialists who fit your roles.</p>
  <div class="actions"><a class="btn" href="{prefix}talent/find/">Find talent</a><a class="btn btn-ghost" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a><a class="btn btn-ghost" href="{prefix}tools/team-cost-calculator/">Estimate team cost</a></div></div>
  {faq}
</div></section>
"""
    path = "guides/employer-of-record-sri-lanka/"
    head = faq_ld + SP.crumbs_ld(B, [("Guides", "guides/"), ("Employer of record", path)])
    B.write(path + "index.html", B.page("Employer of record in Sri Lanka: providers, costs and rules", "Hire in Sri Lanka without a local company. Which employer of record providers cover the country, what it costs and the employment rules to know.", body, prefix, path, extra_head=head, active="guides"))
    return path


# ------------------------------------------------------------------ answers
ANSWERS = [
    ("Hiring", [
        ("Can foreign companies hire employees in Sri Lanka?", "Yes. You can hire through an employer of record, contract individuals, take a dedicated team from a Sri Lankan company, or register your own company, which can be 100% foreign owned.", "guides/how-to-hire-in-sri-lanka/"),
        ("How do I find software developers in Sri Lanka?", "Tell us the roles and we introduce candidates or partner teams. You can also work with companies in our directory or recruit directly through an employer of record.", "talent/find/"),
        ("What does a senior software engineer cost in Sri Lanka?", "Roughly USD 10,800 a year at the local median and about USD 18,600 at export company pay levels, including 15% statutory contributions, on 2026 data.", "guides/sri-lanka-tech-salaries/"),
        ("Do Sri Lankan developers speak English?", "English is the working language of the export technology sector and of university level computing education. On the EF English Proficiency Index 2025 the general population ranks 73rd of 123 countries, so interview for it.", "compare/"),
        ("How do I pay a contractor in Sri Lanka?", "Sign a services agreement, take monthly invoices and pay by bank transfer into the contractor's Sri Lankan account, in dollars if you like. They pay their own tax, capped at 15% on foreign currency service income.", "guides/pay-employees-and-contractors-in-sri-lanka/"),
        ("Can I run payroll in Sri Lanka without a local company?", "No. Payroll needs a registered local employer for provident fund, trust fund and tax withholding. Use an employer of record or your own Sri Lankan company.", "guides/pay-employees-and-contractors-in-sri-lanka/"),
        ("What is the notice period in Sri Lanka?", "There is no statutory minimum. It is set in the employment contract.", "guides/how-to-hire-in-sri-lanka/"),
        ("How many public holidays does Sri Lanka have?", "The 2026 government calendar lists 26 public holidays, of which 8 are mercantile holidays that apply to most private sector offices.", "guides/sri-lanka-tech-salaries/"),
    ]),
    ("Outsourcing", [
        ("Is Sri Lanka good for IT outsourcing?", "Yes, especially for long running product engineering, enterprise software and finance operations. It exported USD 1.645 billion of IT and business process services in 2025.", "solutions/software-outsourcing-sri-lanka/"),
        ("What are typical outsourcing rates in Sri Lanka?", "About USD 25 to 40 an hour for developers through Sri Lankan companies, according to the Export Development Board.", "solutions/software-outsourcing-sri-lanka/"),
        ("What is a dedicated development team?", "Engineers employed by a partner company who work only on your product and are managed day to day by you.", "solutions/dedicated-development-team-sri-lanka/"),
        ("How does Sri Lanka compare with other outsourcing destinations?", "It is among the lower cost options, smaller than Vietnam or the Philippines, and below Eastern Europe on general English rankings, with a strong record in core product R&D.", "compare/"),
    ]),
    ("Setting up", [
        ("Can a foreigner own a company in Sri Lanka?", "Yes. IT and software companies can be 100% foreign owned, and profits can be repatriated.", "guides/set-up-a-company-in-sri-lanka/"),
        ("How long does it take to register a company in Sri Lanka?", "About 7 to 14 working days.", "guides/set-up-a-company-in-sri-lanka/"),
        ("What is the corporate tax rate for IT exports in Sri Lanka?", "15% on services exported and paid for in foreign currency, from 1 April 2025. The standard rate is 30%.", "guides/set-up-a-company-in-sri-lanka/"),
        ("What is Port City Colombo?", "A special economic zone beside Colombo's business district where licensed companies operate in foreign currency and serve overseas clients. Tax incentives there depend on a separate designation.", "guides/set-up-a-company-in-sri-lanka/"),
        ("Do I need Board of Investment approval?", "No. It is optional. Registration helps with investor approval, visas and facilitation.", "guides/set-up-a-company-in-sri-lanka/"),
        ("What is a global capability centre?", "A company's own offshore operation, staffed by its employees. IFS, Sysco, Synopsys and EY run them in Sri Lanka.", "solutions/offshore-development-center-sri-lanka/"),
    ]),
    ("The industry", [
        ("How big is Sri Lanka's IT industry?", "USD 1.645 billion in IT and business process exports in 2025 according to the Export Development Board, with roughly 150,000 to 175,000 people employed.", "guides/sri-lanka-tech-industry-facts/"),
        ("Which global tech companies are in Sri Lanka?", "IFS, Sysco, Synopsys, Zebra Technologies, Virtusa, HCLTech, EY, HSBC, WNS and Michelin all run engineering or delivery operations there.", "companies/"),
        ("What is Sri Lanka known for in tech?", "Enterprise software and ERP, capital markets technology, and product companies such as WSO2 and Virtusa. The London Stock Exchange's trading platform was built in Colombo.", "why-sri-lanka/"),
        ("What time zone is Sri Lanka in?", "UTC+5:30 all year.", "guides/sri-lanka-tech-industry-facts/"),
        ("Is Sri Lanka's economy stable enough to invest in?", "It defaulted in 2022 and entered a 48 month IMF programme in March 2023. In May 2026 the IMF completed its fifth and sixth reviews and called performance generally strong, while noting that debt risks remain high. The technology export sector kept operating throughout.", "compare/"),
    ]),
]


def build_answers(B, stories):
    blocks = ""
    for group, qs in ANSWERS:
        blocks += f'<h2 class="h-sub mt">{e(group)}</h2>' + "".join(f'<div class="fact"><h3>{e(q)}</h3><p>{e(ans)} <a href="../{u}">More</a></p></div>' for q, ans, u in qs)
    faq_ld = SP.ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for _, qs in ANSWERS for q, ans, _ in qs]})
    body = f"""
<section class="page-head"><div class="wrap narrow">
  <h1>Answers: hiring, outsourcing and setting up in Sri Lanka</h1>
  <p class="lede">Short, sourced answers to the questions founders and CTOs ask us most. Each links to the page with the detail and the sources.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">{blocks}
  <div class="reach mt"><h2>Have a different question?</h2><p>Ask us directly.</p><div class="actions"><a class="btn" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a><a class="btn btn-ghost" href="mailto:{B.EMAIL}">Email us</a></div></div>
</div></section>
"""
    B.write("answers/index.html", B.page("Hiring and outsourcing in Sri Lanka: questions answered", "Short, sourced answers on hiring developers, outsourcing software, costs, tax and company setup in Sri Lanka.", body, "../", "answers/", extra_head=faq_ld, active="guides"))
    return "answers/"


def build_playbook(B, stories):
    f = extra.form(B, "playbook", "Get the playbook", "Tell us where to send updates. The download opens as soon as you submit.", [
        ("text", "name", "Your name", True, ""), ("email", "email", "Work email", True, ""), ("text", "company", "Company", True, ""),
        ("select", "plan", "What are you considering?", True, ["Hiring a few people", "A dedicated team", "Our own centre", "Just researching"]),
    ], "Send and download", "Thank you. Your download is ready below.")
    body = f"""
<section class="page-head"><div class="wrap narrow">
  <h1>The Sri Lanka tech team playbook 2026</h1>
  <p class="answer">One document with everything a founder or CTO needs before building a team in Sri Lanka: salary ranges for 25 roles, the four hiring routes, company setup, tax, Board of Investment and Port City rules, and the industry numbers, all with sources.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <ul class="ticks">
    <li>2026 pay by role, with employer costs worked out in dollars</li>
    <li>Employer of record, contractors, partner team or own company, compared</li>
    <li>Registration, ownership, the 15% export tax and visas</li>
    <li>Employment rules foreign employers miss, including termination</li>
    <li>Exports, workforce, rankings and exits, each with its source</li>
  </ul>
  <div data-reveal="playbook">{f}</div>
  <p class="playbook-link" id="playbook-link" hidden><a class="btn btn-saffron" href="../assets/sri-lanka-tech-team-playbook-2026.pdf">Download the playbook (PDF)</a></p>
  <p class="aside">Prefer to read online? The same content is in our <a href="../guides/">guides</a>.</p>
</div></section>
"""
    B.write("playbook/index.html", B.page("Sri Lanka tech team playbook 2026: free download", "Free PDF for founders and CTOs: Sri Lanka salary ranges, hiring routes, company setup, tax rules and industry numbers, all sourced.", body, "../", "playbook/", active="guides"))
    return "playbook/"


def build_all(B, stories):
    return build_compare(B, stories) + [build_calculator(B, stories), build_eor(B, stories), build_answers(B, stories), build_playbook(B, stories)]
