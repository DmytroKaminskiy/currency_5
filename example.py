import requests
from bs4 import BeautifulSoup

currency_url = 'https://alfabank.ua/ru'

response = requests.get(currency_url)

response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

usd_buy = soup.find("span", {"data-currency": "USD_BUY"}).text.strip()
usd_sale = soup.find("span", {"data-currency": "USD_SALE"}).text.strip()
