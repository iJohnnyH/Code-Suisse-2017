from bs4 import BeautifulSoup
from urllib.request import urlopen
import html
import re

file = urlopen("http://finance.yahoo.com/quote/AAPL/options?p=AAPL&straddle=true")
text = file.read()
soup = BeautifulSoup(text, "lxml")
dateChoices = soup.find("select", {"class":"Fz(s)"})
dateChoices = soup.findAll("option")
dateID = []
for x in range (0 , len(dateChoices)):
	tag = dateChoices[x]
	dateID.append(tag['value'])
print(dateID)