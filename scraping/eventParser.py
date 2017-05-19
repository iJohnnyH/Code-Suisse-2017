from bs4 import BeautifulSoup
from urllib.request import urlopen
import html

company = "AAPL"
file = urlopen("http://www.google.com/finance?q=" + company)
text = file.read()
soup = BeautifulSoup(text, "lxml")
parser = soup.findAll("div", {"class" : "bld date"})
eventDates = []
for x in range (0 , len(parser)):
	eventDates.append(parser[x].text)
print (eventDates)

print("\n")

parser = soup.findAll("div", {"class": "event"})
subParser = []
eventTitles = []
for x in range (0 , len(parser)):
	subParser.append(parser[x].findAll("div" , {"class" : None}))

string = ""
for x in range(0 , len(subParser)):
	eventTitles.append(subParser[x][0].text.rstrip())
print(eventTitles)