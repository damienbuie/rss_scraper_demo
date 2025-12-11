"""
Configuration for news sources and areas of interest
"""
from typing import List, Dict

# Areas of interest - customize these based on your needs
AREAS_OF_INTEREST = [
    "cybersecurity",
    "threat intelligence",
    "disinformation",
    "foreign interference",
    "information warfare",
    "national security",
    "intelligence",
    "defense",
    "strategic communications",
    "digital forensics",
    "hybrid threats",
    "influence operations",
    "data privacy",
    "artificial intelligence security",
    "counter-terrorism",
    "international relations",
    "conflict analysis"
]

# News sources configuration
# Format: {"name": "Site Name", "url": "https://example.com", "is_rss": True/False, "selectors": {...}}
# Total: 232 sources
NEWS_SOURCES = [
    {
        "name": "Africa Center for Strategic Studies",
        "url": "https://africacenter.org/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Institute for Security Studies (ISS)",
        "url": "https://issafrica.org/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Science Feedback",
        "url": "https://science.feedback.org/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "American Enterprise Institute (AEI) - Critical Threats",
        "url": "https://www.criticalthreats.org/feed",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Armed Conflict Location & Event Data Project (ACLED)",
        "url": "https://acleddata.com/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "International Crisis Group",
        "url": "https://www.crisisgroup.org/rss.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Journal of Cybersecurity",
        "url": "https://academic.oup.com/rss/site_5188/3053.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Citizen Lab",
        "url": "https://citizenlab.ca/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Google Cloud Threat Intelligence Reports",
        "url": "https://feeds.feedburner.com/threatintelligence/pvexyqv7v0v",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Google Threat Analysis Group (TAG) Bulletins & Reports",
        "url": "https://blog.google/threat-analysis-group/rss/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "National Cyber Security Centre (NCSC) - Blog Posts",
        "url": "https://www.ncsc.gov.uk/api/1/services/v1/blog-post-rss-feed.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "National Cyber Security Centre (NCSC) - Threat Reports",
        "url": "https://www.ncsc.gov.uk/api/1/services/v1/report-rss-feed.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Record",
        "url": "https://therecord.media/feed",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Contemporary Security Policy",
        "url": "https://www.tandfonline.com/feed/rss/fcsp20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Critical Studies on Security",
        "url": "https://www.tandfonline.com/feed/rss/rcss20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Defence & Security Analysis",
        "url": "https://www.tandfonline.com/feed/rss/cdan20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Defence Studies",
        "url": "https://www.tandfonline.com/feed/rss/fdef20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "European Journal of International Security (EJIS)",
        "url": "https://www.cambridge.org/core/rss/product/id/E5D7515F8CBF4E7BFAB89AB5AA5D091C",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "European Security",
        "url": "https://www.tandfonline.com/feed/rss/feus20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Journal of Gloabl Security Studies",
        "url": "https://academic.oup.com/rss/site_5401/3262.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Journal of Strategic Studies",
        "url": "https://www.tandfonline.com/feed/rss/fjss20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Problems of Post Communism",
        "url": "https://www.tandfonline.com/feed/rss/mppc20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Small Wars Journal (SWJ)",
        "url": "https://smallwarsjournal.com/rss.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Studies in Conflict & Terrorism",
        "url": "https://www.tandfonline.com/feed/rss/uter20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Washington Quarterly",
        "url": "https://www.tandfonline.com/feed/rss/rwaq20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Lawfare",
        "url": "https://www.lawfaremedia.org/rss.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "War On The Rocks",
        "url": "https://warontherocks.com/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Globesec",
        "url": "https://www.globsec.org/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "International Institute for Strategic Studies (IISS)",
        "url": "https://www.iiss.org/rss/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "RAND Corporation - Articles",
        "url": "https://www.rand.org/pubs/articles.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "RAND Corporation - Commentary",
        "url": "https://www.rand.org/pubs/commentary.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "RAND Corporation - Research",
        "url": "https://www.rand.org/pubs/new.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Royal United Services Institute (RUSI)",
        "url": "https://www.rusi.org/rss/latest-publications.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "International Affairs (Chatham House)",
        "url": "https://academic.oup.com/ia/rss",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Foreign Policy",
        "url": "https://foreignpolicy.com/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Chatham House",
        "url": "https://www.chathamhouse.org/path/news-releases.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Hope Not Hate",
        "url": "https://hopenothate.org.uk/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Dialogues on Digital Society",
        "url": "https://journals.sagepub.com/action/showFeed?ui=0&mi=ehikzz&ai=2b4&jc=dds&type=etoc&feed=rss",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "International Journal of Communication",
        "url": "https://ijoc.org/index.php/ijoc/gateway/plugin/WebFeedGatewayPlugin/rss2",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "International Journal of Press/Politics (IJPP)",
        "url": "https://journals.sagepub.com/action/showFeed?ui=0&mi=ehikzz&ai=2b4&jc=hij&type=etoc&feed=rss",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "International Journal of Strategic Communication",
        "url": "https://www.tandfonline.com/feed/rss/hstc20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Media, War & Conflict",
        "url": "https://journals.sagepub.com/action/showFeed?ui=0&mi=ehikzz&ai=2b4&jc=mwc&type=etoc&feed=rss",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Political Communication",
        "url": "https://www.tandfonline.com/feed/rss/upcp20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Atlantic Council - Digital Forensics Research Lab (DFRLab)",
        "url": "https://dfrlab.org/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Debunk.org Disinformation Analysis Center",
        "url": "https://www.debunk.org/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "DoubleThink Lab",
        "url": "https://doublethinklab.org/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Doublethink Lab (Medium)",
        "url": "https://medium.com/feed/doublethinklab",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "EU Disinfo Lab",
        "url": "https://www.disinfo.eu/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "European Centre for Excellence for Countering Hybrid Threats (Hybrid COE)",
        "url": "https://www.hybridcoe.fi/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Foundation for Defense of Democracies (FDD)",
        "url": "https://www.fdd.org/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "German Marshall Fund of the United States (GMF) Alliance for Securing Democracy",
        "url": "https://securingdemocracy.gmfus.org/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Institute for Strategic Dialogue (ISD)",
        "url": "https://www.isdglobal.org/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "MAP!NFLUENCE",
        "url": "https://mapinfluence.eu/en/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Tactical Tech",
        "url": "https://tacticaltech.org/rss.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Gloabl Disinformation Index (GDI)",
        "url": "https://www.disinformationindex.org/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "European Digital Media Observatory (EDMO)",
        "url": "https://edmo.eu/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "EUvsDisinfo",
        "url": "https://euvsdisinfo.eu/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Dysinfluence",
        "url": "https://marcowenjones.substack.com/feed",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Memetic Warfare",
        "url": "https://substack.com/@memeticwarfareweekly/feed",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Newsguard\'s Reality Check",
        "url": "https://www.newsguardrealitycheck.com/feed",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Lvivski Substack",
        "url": "https://adamure.substack.com/feed",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Australian Strategic Policy Institute (ASPI)",
        "url": "https://www.aspi.org.au/feed",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Recorded Future",
        "url": "https://www.recordedfuture.com/feed",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Intelligence and National Security",
        "url": "https://www.tandfonline.com/feed/rss/fint20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "International Journal of Intelligence and Counterintelligence",
        "url": "https://www.tandfonline.com/feed/rss/ujic20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "International Journal of Intelligence, Security and Public Affairs",
        "url": "https://www.tandfonline.com/feed/rss/usip20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Journal of Intelligence History",
        "url": "https://www.tandfonline.com/feed/rss/rjih20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Journal of Policing, Intelligence and Counter Terrorism (JPICT)",
        "url": "https://www.tandfonline.com/feed/rss/rpic20",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "International Consortium of Investigative Journalists (ICIJ)",
        "url": "https://www.icij.org/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Lighthouse Reports",
        "url": "https://www.lighthousereports.com/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Insider",
        "url": "https://theins.ru/api/rss/en/default",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Intercept",
        "url": "https://theintercept.com/feed/?rss",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Conversation",
        "url": "https://theconversation.com/uk/articles.atom",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "African Arguments",
        "url": "https://africanarguments.org/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Continent",
        "url": "https://continent.substack.com/feed",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Diplomat",
        "url": "https://thediplomat.com/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "404 Media",
        "url": "https://www.404media.co/rss/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "BleepingComputer",
        "url": "https://www.bleepingcomputer.com/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Dark Reading",
        "url": "https://www.darkreading.com/rss.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Eurasianet",
        "url": "https://eurasianet.org/rss",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Politico Europe - Brussels Playbook",
        "url": "https://www.politico.eu/newsletter/brussels-playbook/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Politico Europe - Cyber Security and Data Protection",
        "url": "https://www.politico.eu/section/cybersecurity/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Politico Europe - Defense",
        "url": "https://www.politico.eu/section/defense/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Politico Europe - EU Influence",
        "url": "https://www.politico.eu/newsletter/politico-eu-influence/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Politico Europe - Global Security",
        "url": "https://www.politico.eu/newsletter/global-security/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Politico Europe - London Influence",
        "url": "https://www.politico.eu/newsletter/politico-london-influence/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Politico Europe - London Playbook",
        "url": "https://www.politico.eu/newsletter/london-playbook/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Politico Europe - Technology",
        "url": "https://www.politico.eu/section/technology/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Financial Times - Emerging Markets",
        "url": "https://www.ft.com/emerging-markets?format=rss",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Financial Times - World",
        "url": "https://www.ft.com/world?format=rss",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "The Wall Street Journal - Politics",
        "url": "https://feeds.content.dowjones.io/public/rss/socialpoliticsfeed",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Wall Street Journal - Technology: What\'s News",
        "url": "https://feeds.content.dowjones.io/public/rss/RSSWSJD",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Wall Street Journal - World",
        "url": "http://feeds.content.dowjones.io/public/rss/RSSWorldNews",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Le Monde",
        "url": "https://www.lemonde.fr/en/rss/une.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Spigel International",
        "url": "http://www.spiegel.de/schlagzeilen/rss/0,5291,676,00.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The New Humanitarian",
        "url": "https://www.thenewhumanitarian.org/rss/all.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Middle East Eye",
        "url": "https://www.middleeasteye.net/rss",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Middle East Monitor",
        "url": "https://www.middleeastmonitor.com/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Al Jazeera",
        "url": "https://www.aljazeera.com/xml/rss/all.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "BBC News - Science & Enviroment",
        "url": "https://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "BBC News - Technology",
        "url": "https://feeds.bbci.co.uk/news/technology/rss.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "BBC News - UK",
        "url": "https://feeds.bbci.co.uk/news/uk/rss.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "BBC News - World",
        "url": "https://feeds.bbci.co.uk/news/world/rss.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Sky News - Politics",
        "url": "https://feeds.skynews.com/feeds/rss/politics.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Sky News - Technology",
        "url": "https://feeds.skynews.com/feeds/rss/technology.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Sky News - UK",
        "url": "https://feeds.skynews.com/feeds/rss/uk.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Sky News - World",
        "url": "https://feeds.skynews.com/feeds/rss/world.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Daily Telegraph",
        "url": "https://www.telegraph.co.uk/rss.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Guardian - Global Development",
        "url": "https://www.theguardian.com/global-development/rss",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Guardian - Technology",
        "url": "https://www.theguardian.com/uk/technology/rss",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Guardian - UK",
        "url": "https://www.theguardian.com/uk-news/rss",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Guardian - World",
        "url": "https://www.theguardian.com/world/rss",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Axios",
        "url": "https://api.axios.com/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "CNN",
        "url": "http://rss.cnn.com/rss/edition_world.rss",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Politico - Defense",
        "url": "https://rss.politico.com/defense.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Politico - Influence",
        "url": "https://rss.politico.com/politicoinfluence.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Politico - Morning Cybersecurity",
        "url": "https://rss.politico.com/morningcybersecurity.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Politico - Politics",
        "url": "https://rss.politico.com/politics-news.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The New York Times - Technology",
        "url": "http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The New York Times - World",
        "url": "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Washington Post - Technology",
        "url": "https://feeds.washingtonpost.com/rss/business/technology",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "The Washington Post - World",
        "url": "https://feeds.washingtonpost.com/rss/world",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "bellingcat",
        "url": "https://www.bellingcat.com/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Foundation for Defense of Democracies (FDD) Long War Journal",
        "url": "https://feeds.feedburner.com/LongWarJournal",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "ADWEEK",
        "url": "https://www.adweek.com/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Intelligence Online",
        "url": "https://feeds.feedburner.com/IntelligenceOnline",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "PR Week",
        "url": "https://feeds.feedburner.com/PrweekUsNews",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Civil Service World",
        "url": "https://www.civilserviceworld.com/nocache/rss/articles",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Ministry of Defence (MOD)",
        "url": "https://www.gov.uk/government/organisations/ministry-of-defence.atom",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Foreign, Commonwealth & Development Office (FCDO)",
        "url": "https://blogs.fcdo.gov.uk/feed/",
        "is_rss": True,
        "selectors": {}
    },
    {
        "name": "Anthropic Threat Intelligence",
        "url": "https://www.anthropic.com/news",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "OpenAI Disrupting Malicious Uses of AI Reports",
        "url": "https://openai.com/news/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "The Uppsala Conflict Data Program (UCDP)",
        "url": "https://www.uu.se/en/department/peace-and-conflict-research/research/ucdp",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "United Nations Security Council Monitoring Team Reports",
        "url": "https://main.un.org/securitycouncil/en/sanctions/1267/monitoring-team/reports",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Microsoft Threat Analysis Center (MTAC) Reports",
        "url": "https://www.microsoft.com/en-us/corporate-responsibility/customer-security-trust/microsoft-threat-analysis-center",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Clearsky Cyber Security",
        "url": "https://www.clearskysec.com/category/disinformation/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Intel471",
        "url": "https://www.intel471.com/resources/whitepapers",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Cornell Studies in Security Affairs",
        "url": "https://www.cornellpress.cornell.edu/series/cornell-studies-in-security-affairs/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Defence Committee",
        "url": "https://committees.parliament.uk/committee/24/defence-committee/publications/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "International Relations & Defence Committee",
        "url": "https://committees.parliament.uk/committee/360/international-relations-and-defence-committee/publications/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "National Security Strategy (Joint Committee)",
        "url": "https://committees.parliament.uk/committee/111/national-security-strategy-joint-committee/publications/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Democracy Reporting International (DRI)",
        "url": "https://democracy-reporting.org/en/office/global",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "European External Action Service (EEAS)",
        "url": "https://www.eeas.europa.eu/eeas/information-integrity-and-countering-foreign-information-manipulation-interference-fimi_en",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Foreign Affairs Committee",
        "url": "https://committees.parliament.uk/committee/78/foreign-affairs-committee/publications/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "HKS (Harvard Kennedy School) Misinformation Review",
        "url": "https://misinforeview.hks.harvard.edu/explore/research-article/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Place Branding and Public Diplomacy",
        "url": "https://link.springer.com/journal/41254",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Attribution Data Analysis Countermeasures Interoperability (ADAC.iO)",
        "url": "http://adacio.eu/publications",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Cardiff University Disinformation, Strategic Communications and Open Source Research Programme (DISCOS)",
        "url": "https://www.cardiff.ac.uk/security-crime-intelligence-innovation-institute/research/groups/disinformation-strategic-communications-and-open-source-research-programme",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Clemson University Media Forensic Hub",
        "url": "https://www.clemson.edu/centers-institutes/watt/hub/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "King\'s EVIDENCE Network (Ensuring Validation & Investigation of Deceptive Narratives on CBRN Events)",
        "url": "https://www.evidencenetwork.co.uk/blog",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Lund University Psychological Defence Research Institute",
        "url": "https://www.psychologicaldefence.lu.se/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "UCL Digital Speech Lab",
        "url": "https://www.digitalspeechlab.com/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "University of Nottingham Centre for the Study of Subversion, Unconventional Interventions and Terrorism (SUIT)",
        "url": "https://www.nottingham.ac.uk/suit/projects/index.aspx",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "University of Oxford Oxford Internet Institute (OII) Programme on Democracy & Technology",
        "url": "https://demtech.oii.ox.ac.uk/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Global Transformation in Media & Communication Research",
        "url": "https://link.springer.com/series/15018/books",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "AI Forensics",
        "url": "https://aiforensics.org/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Alliance4Europe",
        "url": "https://alliance4europe.eu/reports",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "CheckFirst",
        "url": "https://checkfirst.network/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Cyfluence Research Center (CRC)",
        "url": "https://www.cyfluence-research.org/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Foreign Information Manipulation and Interference Information Sharing and Analysis Centre (FIMI-ISAC)",
        "url": "https://fimi-isac.org/index.html",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "German Marshall Fund of the United States (GMF)",
        "url": "https://www.gmfus.org/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Global Influence Operations Report (GIOR)",
        "url": "https://www.global-influence-ops.com/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Intenational Panel on the Information Enviroment (IPIE)",
        "url": "https://www.ipie.info/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Qurium Media Foundation - Digital Forensics",
        "url": "https://www.qurium.org/alerts/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Tech Against Terrorism",
        "url": "https://techagainstterrorism.org/home",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Tech Policy .Press",
        "url": "https://www.techpolicy.press/category/disinformation/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "The Alan Turing Institute - Centre for Emerging Technology and Security (CETaS)",
        "url": "https://cetas.turing.ac.uk/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Watchdog MD",
        "url": "https://watchdog.md/en/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Microsoft, Security Insider, Cyber Influence Operations",
        "url": "https://www.microsoft.com/en-gb/security/security-insider/browse-by-topic/cyber-influence-operations",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Journal of Information Warfare",
        "url": "https://www.jinfowar.com/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "NATO Strateigc Communications Centre of Excellence",
        "url": "https://stratcomcoe.org/publications",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "BBC Monitoring Disinformation Watch",
        "url": "https://monitoring.bbc.co.uk/inside-bbcm/33",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Indicator",
        "url": "https://indicator.media/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Vatnik Soup",
        "url": "https://vatniksoup.com/en/articles/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Counter WMD Disinformation Initiative (GP WMD Counter Disinfo)",
        "url": "https://www.gpwmd.com/countering-wmd-cbrn-disinformation",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "G7 Rapid Response Mechanism (G7 RRM)",
        "url": "https://www.international.gc.ca/transparency-transparence/rapid-response-mechanism-mecanisme-reponse-rapide/index.aspx?lang=eng#a2",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Center for Countering Disinformation (CCD)",
        "url": "https://cpd.gov.ua/en/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Office of the Director National Intelligence (ODNI) Foreign Malign Influence Center (FMIC)",
        "url": "https://www.dni.gov/index.php/nctc-home",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Psychological Defence Agency",
        "url": "https://mpf.se/psychological-defence-agency/publications",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "US State Department Global Engagement Center (GEC)",
        "url": "https://2021-2025.state.gov/bureaus-offices/under-secretary-for-public-diplomacy-and-public-affairs/global-engagement-center/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Vigilance and Protection Against Foreign Interference (VIGINUM)",
        "url": "https://www.diplomatie.gouv.fr/en/french-foreign-policy/digital-diplomacy/news/article/foreign-digital-interference-publication-of-the-viginum-report-on-information",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Integrity Institute",
        "url": "https://www.integrityinstitute.org/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Carnegie Endowment for International Peace - Partnership for Countering Influence Operations",
        "url": "https://carnegieendowment.org/projects/partnership-for-countering-influence-operations?lang=en",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Communication & Digital Committee",
        "url": "https://committees.parliament.uk/committee/170/communications-and-digital-committee/publications/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Culture, Media & Sport Sub-committee on Online Harms & Disinformation",
        "url": "https://committees.parliament.uk/committee/438/culture-media-and-sport-subcommittee-on-online-harms-and-disinformation/publications/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "ActiveFence",
        "url": "https://www.activefence.com/research/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Alethea",
        "url": "https://alethea.com/insights?category=case-study",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Blackbird.AI RAV3N Intelligence Team",
        "url": "https://blackbird.ai/rav3n-blog/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Cyabra",
        "url": "https://cyabra.com/reports/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Graphika",
        "url": "https://www.graphika.com/reports",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Logically.",
        "url": "https://logically.ai/research",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "OpenMinds",
        "url": "https://www.openminds.ltd/reports",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "OpenMinds Cognitive Defence Monitor",
        "url": "https://surf-jonquil-8b7.notion.site/1e07b10a66328195a9a3dd593c3c9fcc?v=1e07b10a663281b4ad41000cf6237cbc",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Osavul",
        "url": "https://www.osavul.cloud/cases",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Intelligence & Security Committee of Parliament (ISC)",
        "url": "https://isc.independent.gov.uk/reports/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Journal of Applied Operational Intelligence",
        "url": "https://www.ubplj.org/index.php/jaoi",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Journal of European and American Intelligence Studies (JEAIS)",
        "url": "https://rieas.gr/intelligence-journal",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Concise Histories of Intelligence",
        "url": "https://press.georgetown.edu/Series-List/category/Concise-Histories-of-Intelligence",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Georgetown Studies in Intelligence History",
        "url": "https://press.georgetown.edu/Series-List/category/Georgetown-Studies-in-Intelligence-History",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Intelligence, Surveillance and Secret Warfare",
        "url": "https://edinburghuniversitypress.com/series-intelligence-surveillance-and-secret-warfare/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "New Intelligence Studies",
        "url": "https://www.routledge.com/Routledge-New-Intelligence-Studies/book-series/RNIS",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Security and Professional Intelligence Education Series (SPIES)",
        "url": "https://www.bloomsbury.com/us/series/security-and-professional-intelligence-education-series/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Studies in Espionage and Culture",
        "url": "https://www.routledge.com/Routledge-Studies-in-Espionage-and-Culture/book-series/RSIEAC",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Studies in Intelligence",
        "url": "https://www.routledge.com/Studies-in-Intelligence/book-series/SE0788",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "International Development Committee",
        "url": "https://committees.parliament.uk/committee/98/international-development-committee/publications/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "International Development Sub-Committee on the Work of the Independent Commission for Aid Impact (ICAI)",
        "url": "https://committees.parliament.uk/committee/347/international-development-subcommittee-on-the-work-of-the-independent-commission-for-aid-impact",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Reporters Without Borders (RSF)",
        "url": "https://rsf.org/en/subject/disinformation-and-propaganda",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "The Buearu of Investigative Journalism (TBIJ)",
        "url": "https://www.thebureauinvestigates.com/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "South China Morning Post (SCMP)",
        "url": "https://www.scmp.com/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Atlas News",
        "url": "https://theatlasnews.co/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Cyber Security Intelligence",
        "url": "https://www.cybersecurityintelligence.com/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Cybernews",
        "url": "https://cybernews.com/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "The Hacker News",
        "url": "https://thehackernews.com/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Reuters",
        "url": "https://www.reuters.com/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "The Finanical Times",
        "url": "https://www.ft.com/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "The Times",
        "url": "https://www.thetimes.co.uk/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "AP News",
        "url": "https://apnews.com/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Semafor",
        "url": "https://www.semafor.com/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Journal of Illicit Economies and Development",
        "url": "https://jied.lse.ac.uk/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Organized Crime and Corruption Reporting Project (OCCRP)",
        "url": "https://www.occrp.org/en",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Centre for Information Resilience (CIR)",
        "url": "https://www.info-res.org/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Forensic Architecture",
        "url": "https://forensic-architecture.org/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Advanced Sciences and Technologies for Security Applications",
        "url": "https://link.springer.com/series/5540",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Bluesky Moderation Reports",
        "url": "https://bsky.social/about/blog",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Meta\'s Threat Disruptions",
        "url": "https://transparency.meta.com/en-gb/metasecurity/threat-reporting/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "TikTok Covert Influence Operations",
        "url": "https://www.tiktok.com/transparency/en-us/covert-influence-operations",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "X Transparency Center",
        "url": "https://transparency.x.com/en",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Pool Re",
        "url": "https://www.poolre.co.uk/reports/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Commission for Countering Extremism (CCE)",
        "url": "https://www.gov.uk/government/organisations/commission-for-countering-extremism",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "The Brooking\'s Institute",
        "url": "https://www.brookings.edu/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Drop Site News",
        "url": "https://www.dropsitenews.com/",
        "is_rss": False,
        "selectors": {}
    },
    {
        "name": "Center for Countering Digital Hate (CCDH)",
        "url": "https://counterhate.com/research/",
        "is_rss": False,
        "selectors": {}
    },
]

# Common selectors for sites that follow similar patterns
COMMON_SELECTORS = {
    "article_links": "article a, .article a, .post a, .news-item a",
    "title": "h1, .article-title, .post-title, .headline",
    "content": "article, .article-content, .post-content, .entry-content, main",
    "date": "time, .date, .published-date, .article-date"
}

# Scraper settings
SCRAPER_CONFIG = {
    "max_articles_per_site": 50,  # Limit articles per site per run
    "request_delay": 1.0,  # Seconds between requests
    "timeout": 30,  # Request timeout in seconds
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "concurrent_sources": 10,  # Number of sources to scrape concurrently
    "batch_delay": 5.0,  # Delay between batches of concurrent requests
    "max_sources": 20,  # Set to an integer to limit how many sources to process (None = all)
}

# Agent settings
AGENT_CONFIG = {
    "model": "gpt-4o-mini",  # Use gpt-4o for better analysis, gpt-4o-mini for cost efficiency
    "relevance_threshold": 0.5,  # Minimum relevance score to consider article relevant
    "max_content_length": 5000,  # Maximum characters to send to agent for analysis
}


