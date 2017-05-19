from bs4 import BeautifulSoup
import urllib.request

url = urllib.request.urlopen("http://finance.yahoo.com/quote/AAPL/options?p=AAPL&straddle=true&date=1496361600")
text = url.read()
soup = BeautifulSoup(text, 'lxml')
calls = soup.find_all("td" , {"class" : "data-col0 Ta(end) Pstart(10px)"})
strikes = soup.find_all("td" , {"class" : "data-col5 Ta(c) Px(10px)"})
puts = soup.find_all("td", {"class" : "data-col6 Ta(end) Pstart(10px)"})

for x in range (0, len(strikes)):
	print (calls[x].text)
	print (strikes[x].text)
	print (puts[x].text)
	print("\n")

lastStockPrice = 152.54;
difference = []
min = 20000
index = 0;
for x in range(0, len(strikes)):
	a = abs(lastStockPrice - (float)(strikes[x].text));
	if (a < min):
		min = a;
		index = x;

print(index);
print(calls[index].text)
print(strikes[index].text)
print(puts[index].text)
delta = (((float)(calls[index].text) + (float)(puts[index].text))/lastStockPrice) * 100;
print(delta)


