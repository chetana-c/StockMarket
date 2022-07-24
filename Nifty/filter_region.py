from bs4 import BeautifulSoup
import requests
import sys
from datetime import datetime, timedelta
import pandas as pd

code = "Costco" #input("Enter the NYSE stock symbol: ")

#Your Choice Stock
url = "https://finance.yahoo.com/lookup?s={}".format(code)
print(url)
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
symbol = soup.find('td', attrs={"data-reactid": "57"}) # 57+8*n
name = soup.find('td', attrs={"data-reactid": "58"}) # 58+8*n
price = soup.find('td', attrs={"data-reactid": "59"}) # 59+8*n
print(code + " stock: " + price.text)

print(pd.read_html(url))