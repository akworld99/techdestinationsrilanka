"""Guide: how to pay employees and contractors in Sri Lanka (contracting, payroll and the regulatory framework)."""
import html

import seo_pages as SP
from seo_pages import a

e = html.escape

PATH = "guides/pay-employees-and-contractors-in-sri-lanka/"
REVIEWED = "23 October 2026"
FX = SP.FX

DESARAM = "https://www.desaram.com/a-guide-on-sri-lanka-employment-law/"
TERMINATION = "https://www.desaram.com/sri-lanka-employment-termination-redundancy-laws-2025/"
MIHCM = "https://mihcm.com/resources/guides/sri-lanka-payroll-guide"
MINWAGE = "https://conventuslaw.com/report/sri-lanka-minimum-wages-increased-2/"
TAX15 = "https://www.taxadvisor.lk/article/sei"
RELIEF = "https://adaderana.lk/news/106147/minister-issues-clarification-over-15-tax-on-digital-service-exports"
APIT = "https://taxadvisor.lk/data/uploads/notice_to_taxpayers_26_03_2025_.pdf"
FXRULES = "https://www.ft.lk/columns/Repatriation-of-export-proceeds-into-Sri-Lanka-and-conversion-A-practical-perspective/4-793764"
PDPA = "https://www.ft.lk/front-page/Data-protection-compliance-regime-takes-effect-on-1-Jan-2027/44-795776"
PLAYROLL = "https://www.playroll.com/compliance-hub/paying-employees-in-sri-lanka"
TEWA = "https://lankalaw.net/wp-content/uploads/2025/03/Termination-of-Employment-of-Workmen-Consolidated-2024.pdf"


def usd(lkr):
    return f"{round(lkr / FX / 5) * 5:,}"


GROSS = 400_000
EPF_ER, ETF, EPF_EE = round(GROSS * .12), round(GROSS * .03), round(GROSS * .08)
COST = GROSS + EPF_ER + ETF
GRAT = round(GROSS / 2)  # half a month per completed year

FAQS = [
    ("How do I pay a contractor in Sri Lanka?",
     "Sign a services agreement, have the contractor invoice you, and pay by international bank transfer to their Sri Lankan bank account or through a contractor payment platform. You can pay in US dollars, pounds or euros. The contractor declares the income and pays their own Sri Lankan tax."),
    ("Can a foreign company pay Sri Lankan employees directly without a local entity?",
     "Not as an employer in practice. Running Sri Lankan payroll means registering for the Employees' Provident Fund, the Employees' Trust Fund and income tax withholding, which needs a local employer. Without a company, use an employer of record or engage people as genuine contractors."),
    ("How are freelancers and contractors in Sri Lanka taxed?",
     "From 1 April 2025, income an individual earns from services provided abroad and paid in foreign currency is taxed at a maximum of 15% if it is remitted through a Sri Lankan bank. The first LKR 150,000 a month of income is tax free. Income kept offshore is taxed at normal rates of up to 36%."),
    ("Do I have to withhold tax when I pay a Sri Lankan contractor?",
     "A foreign company paying an independent contractor from abroad does not normally run Sri Lankan withholding. The contractor files their own return. Confirm with a tax adviser if you have any presence in Sri Lanka, because that changes the position."),
    ("What does it cost to employ someone in Sri Lanka on top of salary?",
     "15% of gross earnings in statutory employer contributions: 12% to the Employees' Provident Fund and 3% to the Employees' Trust Fund. Employers with 15 or more workers also owe gratuity of half a month's salary per year of service to anyone who leaves after five years."),
    ("Can I pay Sri Lankan employees in US dollars?",
     "Employees on local payroll are paid in Sri Lankan rupees into a local bank account. Contractors who export their services can be paid in foreign currency, and service exporters are not required to convert foreign currency proceeds into rupees."),
    ("What is the minimum wage in Sri Lanka in 2026?",
     "LKR 30,000 a month, or LKR 1,200 a day, from 1 January 2026, under the National Minimum Wage of Workers Act as amended by Act No. 11 of 2025. Technology salaries are far above it."),
    ("When is a contractor treated as an employee in Sri Lanka?",
     "When the relationship works like employment: you set the hours, they work only for you, they sit inside your team indefinitely and use your equipment. A labour tribunal looks at how the work is actually done, not the title on the contract. Misclassification can mean back payments of provident fund and trust fund contributions and termination claims."),
    ("Does Sri Lanka have a data protection law that affects employment contracts?",
     "Yes. The Personal Data Protection Act, No. 9 of 2022. Its core obligations on lawful processing, data protection officers, breach notification and cross border transfers apply from 1 January 2027. Contracts with people who handle your customer data should cover it now."),
]

LAWS = [
    ("Shop and Office Employees Act, No. 19 of 1954", "Hours (9 a day including a one hour break, 45 a week), overtime at 1.5 times, leave, and written particulars of employment.", DESARAM),
    ("Employees' Provident Fund Act, No. 15 of 1958", "Retirement fund. Employer 12%, employee 8% of total earnings, paid monthly.", MIHCM),
    ("Employees' Trust Fund Act, No. 46 of 1980", "Employer only contribution of 3% of total earnings, paid monthly.", MIHCM),
    ("Payment of Gratuity Act, No. 12 of 1983", "Half a month's salary per completed year for anyone leaving after five years, at employers with 15 or more workers.", MIHCM),
    ("Termination of Employment of Workmen (Special Provisions) Act, No. 45 of 1971", "Non disciplinary termination after 180 days needs consent or the Commissioner of Labour's approval at employers with 15 or more staff. Compensation is capped at LKR 2.5 million.", TERMINATION),
    ("Industrial Disputes Act, No. 43 of 1950", "Unfair dismissal claims before labour tribunals, which can be filed within six months.", DESARAM),
    ("National Minimum Wage of Workers Act, No. 3 of 2016, amended 2025", "LKR 30,000 a month from 1 January 2026.", MINWAGE),
    ("Minimum Retirement Age of Workers Act, No. 28 of 2021", "Probation of up to 180 days, extendable once, stated in the letter of appointment.", DESARAM),
    ("Inland Revenue Act, No. 24 of 2017, amended 2025", "Employer withholding (APIT), the LKR 150,000 monthly tax free threshold and the 15% rate on foreign currency service income.", TAX15),
    ("Foreign Exchange Act, No. 12 of 2017", "Service export proceeds must reach Sri Lanka within 180 days. Service exporters do not have to convert them into rupees.", FXRULES),
    ("Personal Data Protection Act, No. 9 of 2022", "Core obligations for anyone processing personal data apply from 1 January 2027.", PDPA),
]


def build(B, stories):
    prefix = "../../"
    faq, faq_ld = SP.faq_block(stories, FAQS)
    laws = "".join(f"<tr><td><strong>{e(n)}</strong></td><td>{e(w)} {a('Source', u)}</td></tr>" for n, w, u in LAWS)
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Guides", "../")])}
  <h1>How to pay employees and contractors in Sri Lanka</h1>
  <p class="answer">A foreign company can pay people in Sri Lanka in three ways. Contractors invoice you and you pay them abroad, in dollars if you like, and they settle their own tax at a maximum of 15%. Employees are paid in rupees through local payroll, either by an employer of record or by your own Sri Lankan company, with 15% added for provident and trust fund contributions. You cannot run Sri Lankan payroll yourself without a local entity.</p>
  <p class="reviewed">Last reviewed {REVIEWED}. Rules changed in 2025 and 2026. This is general information, not legal or tax advice. US dollar figures use LKR {FX} per dollar.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <nav class="toc" aria-label="On this page"><p><strong>On this page</strong></p><ol>
    <li><a href="#routes">The three ways to pay</a></li>
    <li><a href="#contractors">Paying contractors directly</a></li>
    <li><a href="#contract">What the contract needs</a></li>
    <li><a href="#employees">Paying employees</a></li>
    <li><a href="#cost">What an employee costs: worked example</a></li>
    <li><a href="#payroll">Running your own payroll</a></li>
    <li><a href="#laws">The regulatory framework</a></li>
    <li><a href="#mistakes">Mistakes that cost money</a></li>
  </ol></nav>

  <h2 class="h-sub mt" id="routes">The three ways to pay people in Sri Lanka</h2>
  <div class="tbl"><table>
    <thead><tr><th>Route</th><th>Who employs them</th><th>Currency</th><th>Your obligations</th><th>Best for</th></tr></thead>
    <tbody>
      <tr><td><strong>Independent contractor</strong></td><td>Nobody. They run their own business</td><td>USD, GBP, EUR or LKR</td><td>A services agreement and paying invoices on time</td><td>Specialists, projects, part time or early tests</td></tr>
      <tr><td><strong>Employer of record</strong></td><td>The provider's Sri Lankan entity</td><td>LKR payroll; you pay the provider in your currency</td><td>Salary, 15% contributions and the provider's fee</td><td>1 to 20 full time people, no entity</td></tr>
      <tr><td><strong>Your own company</strong></td><td>Your Sri Lankan subsidiary</td><td>LKR payroll</td><td>Full employer registration, monthly filings and labour law</td><td>Teams of 20 to 30 people or more</td></tr>
    </tbody>
  </table></div>
  <p class="body-l">There is a fourth option: a dedicated team employed by a Sri Lankan company that invoices you monthly. Payroll is their job. See <a href="{prefix}solutions/dedicated-development-team-sri-lanka/">dedicated development teams</a>.</p>

  <h2 class="h-sub mt" id="contractors">Paying contractors directly</h2>
  <p class="body-l">This is the simplest route and the one most foreign startups use first. The process:</p>
  <ol class="steps compact">
    <li><h3>Check it really is contracting</h3><p>Defined deliverables, their own hours and tools, freedom to work for other clients. If you need someone full time, inside your team and under your direction indefinitely, that is employment. Use an employer of record instead.</p></li>
    <li><h3>Sign a services agreement</h3><p>Before any work starts, with the clauses listed below. Sign electronically and keep the signed copy.</p></li>
    <li><h3>Agree the currency and schedule</h3><p>Most Sri Lankan contractors prefer US dollars, pounds or euros, monthly in arrears. Fix the rate in the contract so currency moves are not renegotiated every month.</p></li>
    <li><h3>Get an invoice every period</h3><p>With their name, address, the period, the work done and bank details. It is your record of a business to business payment.</p></li>
    <li><h3>Pay into their Sri Lankan bank account</h3><p>By SWIFT transfer, a money transfer service, or a contractor platform such as Deel or Remote. Paying into a Sri Lankan bank is what lets the contractor claim the 15% tax cap, so do not pay into an account abroad.</p></li>
    <li><h3>Leave the tax to them</h3><p>The contractor declares the income in Sri Lanka. As a foreign payer with no Sri Lankan presence you do not normally withhold. Take advice if you have an office, a company or staff there.</p></li>
  </ol>
  <h3 class="mt">How Sri Lankan contractors are taxed</h3>
  <ul class="ticks">
    <li>From 1 April 2025, income from services provided abroad and paid in foreign currency is taxed at a maximum of 15% when remitted through a Sri Lankan bank ({a("TaxAdvisor.lk", TAX15)}).</li>
    <li>The first LKR 150,000 a month (about USD {usd(150_000)}) is tax free, as for every individual ({a("Ada Derana", RELIEF)}).</li>
    <li>Income left offshore is taxed at the normal progressive rates of up to 36%. This is why good contractors will ask you to pay into their Sri Lankan account.</li>
    <li>Service export proceeds must reach Sri Lanka within 180 days of the service, and service exporters are not required to convert them into rupees ({a("Daily FT, June 2026", FXRULES)}). Many contractors keep a foreign currency account for exactly this.</li>
  </ul>

  <h2 class="h-sub mt" id="contract">What the contract needs</h2>
  <p class="body-l">The same list works for a contractor agreement or, with employment terms added, an offer letter through an employer of record.</p>
  <ul class="ticks">
    <li><strong>Scope and deliverables.</strong> What they deliver, not the hours they sit at a desk.</li>
    <li><strong>Fees, currency and payment terms.</strong> Rate, currency, invoice cycle, days to pay, who bears bank charges.</li>
    <li><strong>Intellectual property assignment.</strong> Everything they create for you is assigned to your company on creation, with a waiver of moral rights where possible. Never rely on default rules.</li>
    <li><strong>Confidentiality.</strong> Covering your code, customers and roadmap, surviving the end of the contract.</li>
    <li><strong>Data protection.</strong> If they touch personal data, processing terms aligned with the Personal Data Protection Act, whose core obligations apply from 1 January 2027 ({a("Daily FT", PDPA)}).</li>
    <li><strong>Independence.</strong> They control how and when they work, use their own equipment and may take other clients. Say it and mean it.</li>
    <li><strong>Termination.</strong> Notice on both sides, often 30 days, and what happens to work in progress.</li>
    <li><strong>Governing law and disputes.</strong> Your home law with arbitration is common. Labour protections under Sri Lankan law can still apply if the relationship turns out to be employment.</li>
  </ul>
  <p class="body-l">For employees, Sri Lankan law also requires written particulars: designation, hours, pay and frequency, allowances, overtime, probation, leave and holidays ({a("De Saram", DESARAM)}). Probation can run up to 180 days, extendable once.</p>

  <h2 class="h-sub mt" id="employees">Paying employees</h2>
  <p class="body-l">Employees on Sri Lankan payroll are paid monthly, in rupees, into a local bank account, with a payslip showing every deduction ({a("Playroll", PLAYROLL)}). Running that payroll needs a registered local employer, so a foreign company without an entity has two choices:</p>
  <ul class="ticks">
    <li><strong>Employer of record.</strong> The provider employs the person, runs payroll and files everything. You pay one monthly invoice in your currency. See our <a href="../employer-of-record-sri-lanka/">employer of record guide</a> for providers that cover Sri Lanka.</li>
    <li><strong>Your own company.</strong> Register a Sri Lankan company, which can be fully foreign owned, and run payroll yourself. See the <a href="../set-up-a-company-in-sri-lanka/">company setup guide</a>.</li>
  </ul>

  <h2 class="h-sub mt" id="cost">What an employee costs: a worked example</h2>
  <p class="body-l">A software engineer on LKR {GROSS:,} a month (about USD {usd(GROSS)}). See the <a href="../sri-lanka-tech-salaries/">salary guide</a> for current ranges by role.</p>
  <div class="tbl"><table>
    <thead><tr><th>Item</th><th>LKR a month</th><th>USD a month</th></tr></thead>
    <tbody>
      <tr><td>Gross salary</td><td>{GROSS:,}</td><td>{usd(GROSS)}</td></tr>
      <tr><td>Employer EPF, 12%</td><td>{EPF_ER:,}</td><td>{usd(EPF_ER)}</td></tr>
      <tr><td>Employer ETF, 3%</td><td>{ETF:,}</td><td>{usd(ETF)}</td></tr>
      <tr><td><strong>Total employer cost</strong></td><td><strong>{COST:,}</strong></td><td><strong>{usd(COST)}</strong></td></tr>
      <tr><td>Deducted from the employee: EPF 8%</td><td>{EPF_EE:,}</td><td>{usd(EPF_EE)}</td></tr>
      <tr><td>Deducted from the employee: income tax (APIT)</td><td colspan="2">On the amount above LKR 150,000, using the Inland Revenue tax table ({a("notice", APIT)})</td></tr>
    </tbody>
  </table></div>
  <ul class="ticks">
    <li><strong>Gratuity.</strong> At employers with 15 or more workers, anyone who leaves after five years gets half a month's salary per completed year. For this engineer that is LKR {GRAT:,} a year of service, so set aside about 4.2% of salary. An employer of record usually builds this into its fee or deposit.</li>
    <li><strong>Overtime.</strong> 1.5 times the hourly rate for staff covered by the Shop and Office Act. Executive grades are usually exempt.</li>
    <li><strong>Bonuses.</strong> Not required by law, but an annual bonus is common in the technology sector and expected in offers.</li>
  </ul>

  <h2 class="h-sub mt" id="payroll">Running your own payroll: the monthly cycle</h2>
  <ol class="steps compact">
    <li><h3>Register once</h3><p>As an employer with the Employees' Provident Fund (run by the Central Bank), the Employees' Trust Fund Board and the Inland Revenue Department for withholding tax.</p></li>
    <li><h3>Pay salaries monthly</h3><p>In rupees, by bank transfer, with a payslip.</p></li>
    <li><h3>Pay withholding tax by the 15th</h3><p>APIT deducted in a month is due to the Inland Revenue Department by the 15th of the next month ({a("MiHCM payroll guide", MIHCM)}).</p></li>
    <li><h3>Pay EPF and ETF by month end</h3><p>Contributions for a month are due by the last working day of the following month.</p></li>
    <li><h3>File annually</h3><p>Year end tax statements to employees, and keep a running gratuity provision.</p></li>
  </ol>
  <p class="body-l">Most new subsidiaries outsource this to a local payroll bureau or accounting firm for the first years.</p>

  <h2 class="h-sub mt" id="laws">The regulatory framework</h2>
  <p class="body-l">The laws that decide how you pay and treat people in Sri Lanka.</p>
  <div class="tbl"><table>
    <thead><tr><th>Law</th><th>What it means for you</th></tr></thead>
    <tbody>{laws}</tbody>
  </table></div>

  <h2 class="h-sub mt" id="mistakes">Mistakes that cost money</h2>
  <ul class="ticks">
    <li><strong>Calling a full time team member a contractor.</strong> If they work only for you, on your hours, inside your team, a labour tribunal can treat them as an employee, with back contributions and termination protection to follow.</li>
    <li><strong>Paying into an account abroad.</strong> It costs your contractor the 15% cap and can push them to 36%, which comes back to you as a pay rise request.</li>
    <li><strong>No IP clause.</strong> Without a written assignment, ownership of code written by a contractor is open to argument.</li>
    <li><strong>Treating termination as at will.</strong> Ending employment after probation is regulated at employers with 15 or more staff ({a("TEWA", TEWA)}). Use probation properly and take advice before letting anyone go.</li>
    <li><strong>Ignoring the data law.</strong> From 1 January 2027 Sri Lanka's data protection obligations apply. Contracts signed now will still be running then.</li>
  </ul>

  <div class="reach mt"><h2>Need the people first?</h2><p>Tell us the roles. We introduce Sri Lankan engineers and specialists, or partner teams that handle employment and payroll for you.</p>
  <div class="actions"><a class="btn" href="{prefix}talent/find/">Find talent</a><a class="btn btn-ghost" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a><a class="btn btn-ghost" href="{prefix}tools/team-cost-calculator/">Estimate team cost</a></div></div>
  {faq}
  <p class="body-l mt">Related: <a href="../how-to-hire-in-sri-lanka/">How to hire in Sri Lanka</a> · <a href="../employer-of-record-sri-lanka/">Employer of record</a> · <a href="../set-up-a-company-in-sri-lanka/">Set up a company</a> · <a href="../sri-lanka-tech-salaries/">Salary guide</a></p>
</div></section>
"""
    title = "How to pay employees and contractors in Sri Lanka"
    desc = "Pay contractors and employees in Sri Lanka: contracts, currency, the 15% tax cap, EPF and ETF, payroll deadlines, gratuity and the laws that apply. 2026 guide."
    article = SP.ld({"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
                     "datePublished": "2026-10-23", "dateModified": "2026-10-23",
                     "author": {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"},
                     "publisher": {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"},
                     "mainEntityOfPage": f"{B.SITE_URL}/{PATH}", "inLanguage": "en",
                     "about": ["Payroll in Sri Lanka", "Independent contractors in Sri Lanka", "Sri Lanka employment law"]})
    howto = SP.ld({"@context": "https://schema.org", "@type": "HowTo", "name": "How to pay a contractor in Sri Lanka",
                   "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t} for i, (n, t) in enumerate([
                       ("Check it really is contracting", "Confirm defined deliverables, the contractor's own hours and tools, and freedom to work for other clients."),
                       ("Sign a services agreement", "Include scope, fees and currency, IP assignment, confidentiality, data protection, independence, termination and governing law."),
                       ("Agree the currency and schedule", "Fix the rate and currency, usually US dollars monthly in arrears."),
                       ("Get an invoice every period", "With name, address, period, work done and bank details."),
                       ("Pay into their Sri Lankan bank account", "By SWIFT transfer or a contractor platform, so the contractor qualifies for the 15% tax cap."),
                       ("Leave the tax to them", "The contractor declares the income in Sri Lanka; a foreign payer with no local presence does not normally withhold.")])]})
    head = faq_ld + article + howto + SP.crumbs_ld(B, [("Guides", "guides/"), ("Pay employees and contractors", PATH)])
    B.write(PATH + "index.html", B.page(title, desc, body, prefix, PATH, extra_head=head, active="guides",
                                        seo_title="How to pay employees and contractors in Sri Lanka (2026)"))
    return PATH
