from bs4 import BeautifulSoup as BS4
import requests

URL = "https://www.investing.com/stock-screener/?sp=country::5|sector::a|industry::a|equityType::a|price2bk_us::0.1,0.9|peexclxor_us::0,10<eq_market_cap;1"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.111"}

page = requests.get(URL, headers=headers)

soup = BS4(page.content, "html.parser")

# print(soup.prettify())

TABLE = soup.find(id="resultsTable")
THEAD = TABLE.findNext()
TBODY = THEAD.findNextSibling()
rows = TBODY.findAllNext()

print(rows[3])
