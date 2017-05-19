from flask import Flask, render_template, request
import master_parse, html
from bs4 import BeautifulSoup
from urllib.request import urlopen
app = Flask(__name__)


@app.route("/")
def index():
    company = "AAPL"
    file = urlopen("http://www.google.com/finance?q=" + company)
    text = file.read()
    soup = BeautifulSoup(text, "lxml")
    parser = soup.findAll("div", {"class" : "bld date"})
    eventDates = []

    for x in range (0 , len(parser)):
        eventDates.append(parser[x].text)

    parser = soup.findAll("div", {"class": "event"})
    subParser = []
    eventTitles = []
    masterString= ""
    for x in range (0 , len(parser)):
        subParser.append(parser[x].findAll("div" , {"class" : None}))
    string = ""
    for x in range(0 , len(subParser)):
        eventTitles.append(subParser[x][0].text.rstrip())
    for x in range(0, len(parser)):
        eventTitles[x] += eventTitles[x]+": "+eventDates[x]+"---------" 
    return render_template("docs/indexNoGraph.html", eventTitles=eventTitles)


@app.route("/<date>")
def date(date):
    
    company = "AAPL"
    file = urlopen("http://www.google.com/finance?q=" + company)
    text = file.read()
    soup = BeautifulSoup(text, "lxml")
    parser = soup.findAll("div", {"class" : "bld date"})
    eventDates = []

    for x in range (0 , len(parser)):
        eventDates.append(parser[x].text)

    parser = soup.findAll("div", {"class": "event"})
    subParser = []
    eventTitles = []
    masterString= ""
    for x in range (0 , len(parser)):
        subParser.append(parser[x].findAll("div" , {"class" : None}))
    string = ""
    for x in range(0 , len(subParser)):
        eventTitles.append(subParser[x][0].text.rstrip())
    for x in range(0, len(parser)):
        eventTitles[x] += eventTitles[x]+": "+eventDates[x]+"---------" 
    
    datef = date.split(" ")
    year = datef[3]
    day = datef[2]
    months = " JanFebMarAprMayJunJulAugSepOctNovDec"
    
    month = int(months.index(datef[1])/ 3 + 1)
    if (month<10):
    	month = "0"+str(month)
    else:
    	month = str(month)
    master_parse.main(year+"-"+month+"-"+day,"NASDAQ","AAPL")
    return render_template("docs/indexWithGraph.html", date=date, eventTitles=eventTitles)

if __name__ == "__main__":
    app.run()
