"""The startup ecosystem guide."""
import html

import seo_pages as SP
from seo_pages import a

e = html.escape

FT24 = "https://www.ft.lk/TOP-STORY/Boost-for-Sri-Lanka-from-Global-Startup-Ecosystem-Report-2024/26-762923"
ADA25 = "https://bizenglish.adaderana.lk/sri-lankas-startup-ecosystem-scales-new-heights-with-global-validation-and-charts-bold-future-post-disrupt-asia/"
WIPO = "https://www.wipo.int/edocs/gii-ranking/2025/lk.pdf"
ECHELON = "https://echelon.lk/startups-in-sri-lanka-unravelling-the-innovation-puzzle/"
BOI = "https://investsrilanka.com/wp-content/uploads/2025/09/IT-SECTOR-3-2.pdf"
FT26 = "https://www.ft.lk/front-page/Govt-lines-up-policy-changes-to-support-5-b-digital-exports/44-795438"


def build(B, stories):
    prefix = "../../"
    faqs = [
        ("How many startups are there in Sri Lanka?", "Between about 750 and 1,000, depending on who is counting. Startup Genome's 2024 report counted 872, Echelon reported 748 operating in 2024, and the Board of Investment cites about 1,000."),
        ("How does Sri Lanka's startup ecosystem rank globally?", "StartupBlink ranks Sri Lanka 69th in the world in its 2026 index. Startup Genome has placed it in the global top five for affordable talent."),
        ("What are the biggest Sri Lankan startup exits?", "WSO2 was acquired by EQT in 2024 in a deal valued at more than USD 600 million. WealthOS was acquired by J.P. Morgan in 2026. PickMe, hSenid Business Solutions and Kapruka have all listed on the Colombo Stock Exchange."),
        ("Is there venture capital in Sri Lanka?", "Yes, but it is limited. Startup Genome recorded USD 104 million of venture funding over 2019 to 2023, with a median seed round of USD 80,000. Active investors include the Lankan Angel Network, BOV Capital and nVentures. A USD 50 million government backed fund of funds was announced in 2025."),
        ("Can a foreigner invest in or start a startup in Sri Lanka?", "Yes. IT companies can be 100% foreign owned and capital can be repatriated, according to the Board of Investment. Income from exported services is taxed at 15%."),
    ]
    faq, faq_ld = SP.faq_block(stories, faqs)
    li = lambda items: '<ul class="ticks">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Guides", "../")])}
  <h1>Sri Lanka's startup ecosystem</h1>
  <p class="answer">Sri Lanka has roughly 750 to 1,000 startups, most of them in Colombo. StartupBlink ranks the country 69th in the world in 2026, and Startup Genome has placed it in the global top five for affordable talent. Sri Lankan founders have produced an exit of more than USD 600 million, a J.P. Morgan acquisition and three stock market listings. Funding is the weak point: rounds are small and late stage capital is scarce.</p>
  <p class="reviewed">Last reviewed {SP.REVIEWED}. Every figure names its source.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  {SP.stats_strip([("69th", "in the world, StartupBlink 2026"), ("750 to 1,000", "startups, depending on the source"), ("USD 600M+", "largest exit: WSO2, acquired by EQT in 2024"), ("USD 50M", "government backed fund of funds announced in 2025")])}

  <h2 class="h-sub mt">The numbers</h2>
  {li([
      f"Ranked 69th globally by StartupBlink in 2026, up from 76th in 2024. Colombo ranks 230th among cities ({a('StartupBlink', 'https://www.startupblink.com/startup-ecosystem/sri-lanka')}).",
      f"Startup count: 872 in Startup Genome's 2024 report ({a('Daily FT', FT24)}), 748 operating according to {a('Echelon', ECHELON)}, about 1,000 according to the {a('Board of Investment', BOI)}.",
      f"Ecosystem value of USD 821 million created between July 2022 and December 2024, roughly three times the 2021 figure, according to coverage of Startup Genome's 2025 report ({a('Ada Derana', ADA25)}).",
      f"Top five in the world for affordable talent, on the same report ({a('Ada Derana', ADA25)}).",
      f"USD 104 million in venture funding over 2019 to 2023 ({a('Daily FT', FT24)}).",
  ])}

  <h2 class="h-sub mt">What Sri Lankan founders have built</h2>
  {li([
      f"<strong>WSO2.</strong> API and identity software founded in Colombo in 2005. EQT agreed to acquire it in 2024 at a value of more than USD 600 million ({a('TechCrunch', 'https://techcrunch.com/2024/05/03/eqt-snaps-up-enterprise-software-company-wso2-for-more-than-600m')}).",
      f"<strong>WealthOS.</strong> Wealth infrastructure founded in 2019 by two Sri Lankans, with engineering in Sri Lanka. J.P. Morgan agreed to acquire it in 2026 ({a('Fintech Futures', 'https://www.fintechfutures.com/m-a/jp-morgan-acquires-wealthos')}).",
      f"<strong>PickMe.</strong> Ride hailing and delivery. Listed on the Colombo Stock Exchange in 2024 after an LKR 1.56 billion offer ({a('Daily FT', 'https://www.ft.lk/Front-Page/PickMe-says-Rs-1-56-b-IPO-pivotal-step-in-its-journey/44-766365')}).",
      f"<strong>hSenid Business Solutions.</strong> HR software. Its 2021 listing was the first by an IT company on the Colombo exchange and was 13.5 times oversubscribed ({a('Daily FT', 'https://www.ft.lk/Front-Page/hSenid-s-Rs-619-m-IPO-notches-record-oversubscription-of-over-13-times/44-727526')}).",
      f"<strong>Kapruka.</strong> Ecommerce. Listed in 2021 ({a('Daily FT', 'https://www.ft.lk/Front-Page/Kapruka-IPO-snapped-up-even-before-official-opening/44-728032')}).",
      f"<strong>Surge Global and Calcey.</strong> Combined in a USD 40 million transaction in 2025 ({a('Sunday Times', 'https://www.sundaytimes.lk/250803/education/hnb-backs-40m-surge-calcey-merger-to-launch-short-circuit-607178.html')}).",
      f"<strong>Logical.</strong> An AI startup reported as the first all Sri Lankan team in Y Combinator, with a seed round of more than LKR 150 million in 2026 ({a('Dealroom', 'https://dealroom.co/news/138988-logical-raises-rs-150m-seed-becomes-first-all-sri-lankan-team-in-y-combi/')}).",
  ])}
  <p class="aside">This is not the full list. We are reporting on more Sri Lankan startups. <a href="{prefix}get-featured/">Tell us about one</a>.</p>

  <h2 class="h-sub mt">Who supports startups</h2>
  {li([
      f"{a('Hatch', 'https://hatch.lk')}: coworking, startup programmes and demo days in Colombo.",
      f"{a('Spiralation', 'https://icta.lk/projects/digital-industry/spiralation')}: the state incubator run by ICTA since 2010, which has supported 130+ tech startups.",
      f"{a('Lankan Angel Network', 'https://www.lankanangelnetwork.com')}: the main angel investor network.",
      f"{a('BOV Capital', 'https://www.bovcapital.com')}: early stage venture capital.",
      f"nVentures: more than USD 1.5 million invested in Sri Lankan startups in three years ({a('Daily Mirror', 'https://www.dailymirror.lk/print/business-news/nVentures-invests-over-US-1-5mn-in-SL-start-ups/273-315782')}).",
      f"{a('John Keells X', 'https://www.johnkeellsx.com')}: the corporate accelerator of John Keells Holdings.",
      f"{a('Startup SL', 'https://startupsl.lk')}: the national startup registry.",
      f"Disrupt Asia: the national startup conference. The 2025 edition drew 5,000+ participants and 100+ investors ({a('LMD', 'https://lmd.lk/disrupt-asia-2025/')}).",
  ])}

  <h2 class="h-sub mt">Policy and incentives</h2>
  {li([
      f"100% foreign ownership and full capital repatriation for IT companies ({a('Board of Investment', BOI)}).",
      f"15% tax on income from exported services, against a 30% standard rate, from 1 April 2025 ({a('TaxAdvisor', 'https://www.taxadvisor.lk/article/sei')}).",
      f"A USD 50 million fund of funds, with USD 5 million of government seed money, was announced in September 2025 ({a('Ada Derana', ADA25)}). As of mid 2026 it was not yet operating ({a('Daily FT', FT26)}).",
      f"Budget 2026 set aside LKR 1.5 billion for a startup ecosystem fund ({a('Daily FT', 'https://www.ft.lk/front-page/Biggest-boost-to-unleash-digital-economy/44-784067')}).",
      f"A digital nomad visa has been issued since February 2026 ({a('Daily FT', 'https://www.ft.lk/front-page/Sri-Lanka-issues-first-Digital-Nomad-Visa/44-788961')}).",
      f"The government's stated target is USD 5 billion in digital exports by 2030 ({a('Daily FT', FT26)}).",
  ])}

  <h2 class="h-sub mt">The weak points</h2>
  {li([
      f"Rounds are small. The median seed round was USD 80,000 and the median Series A USD 200,000 in Startup Genome's 2024 report ({a('Daily FT', FT24)}).",
      f"Late stage capital is scarce. The Global Innovation Index 2025 ranks Sri Lanka 111th of 139 for venture capital received ({a('WIPO', WIPO)}).",
      f"Talent left after the 2022 crisis. One report put departures at about 25,000 IT and BPM professionals from 2022 ({a('AsiaNews', 'https://www.asianews.it/news-en/Laws-and-red-tape-limit-the-growth-of-Sri-Lanka%27s-IT-industry-58441.html')}).",
      "The home market is small, so startups that grow have to sell abroad early.",
  ])}

  <h2 class="h-sub mt">What this means if you are building a company abroad</h2>
  <p class="body-l">The startup scene is where many of Sri Lanka's product engineers learn to ship with small teams and tight budgets. Foreign startups use that in three ways: they <a href="{prefix}solutions/sri-lanka-for-startups/">build their engineering team here</a>, they <a href="{prefix}solutions/staff-augmentation-sri-lanka/">add individual specialists</a>, or they partner with a Sri Lankan company that has built a similar product.</p>
  <div class="reach mt"><h2>Building a team, or looking for a startup to work with?</h2><p>Tell us what you are building. We will introduce the people who fit.</p>
  <div class="actions"><a class="btn" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a><a class="btn btn-ghost" href="{prefix}talent/find/">Find talent</a><a class="btn btn-ghost" href="{prefix}tools/team-cost-calculator/">Estimate team cost</a></div></div>
  {faq}
</div></section>
"""
    path = "guides/sri-lanka-startup-ecosystem/"
    head = faq_ld + SP.crumbs_ld(B, [("Guides", "guides/"), ("Startup ecosystem", path)])
    B.write(path + "index.html", B.page("Sri Lanka startup ecosystem 2026: numbers, exits, investors", "How big Sri Lanka's startup ecosystem is, how it ranks, what founders have built, who funds them and where it is weak. Every figure sourced.", body, prefix, path, extra_head=head, active="guides"))
    return [path]
