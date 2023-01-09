import requests
from bs4 import BeautifulSoup

# URL and headers for Amazon product page
url = "https://www.amazon.com/SAMSUNG-3840x2160-Computer-border-less-LU32R590CWNXZA/dp/B07L9G1BFX/ref=sr_1_3?crid=130JAPGMTJUYA&keywords=curved%2Bmonitor%2B4k&qid=1673289436&refinements=p_n_size_browse-bin%3A3547808011%2Cp_89%3ADell%7CSAMSUNG%2Cp_n_condition-type%3A2224371011&rnid=2224369011&s=pc&sprefix=curved%2Bmonitor%2B4k%2Caps%2C487&sr=1-3&th=1"
headers = {
    "User-Agent": "en-ZW,en-US;q=0.9,en;q=0.8",
    "Accept-Language": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

# Get page HTML
response = requests.get(url=url, headers=headers)

# Make soup and scrape price
soup = BeautifulSoup(response.content, "lxml")
price_tag = (soup.find("span", class_="a-offscreen").getText()).split("$")
price = float(price_tag[1])
print(price)
