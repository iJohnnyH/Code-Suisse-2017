from bs4 import BeautifulSoup
import urllib.request
import plotly.plotly as py
import plotly.graph_objs as go
import quandl
import plotly.tools as tls
from urllib.request import urlopen
import html
import re
import datetime
from datetime import datetime, timezone
import argparse
import sys
quandl.ApiConfig.api_key = "xX7tGtBt1T4fqjsxML-H"
def DateParse(timestamp,companyid):
	file = urlopen("http://finance.yahoo.com/quote/"+companyid+"/options?p="+companyid+"&straddle=true")
	text = file.read()
	soup = BeautifulSoup(text, "lxml")
	dateChoices = soup.find("select", {"class":"Fz(s)"})
	dateChoices = soup.findAll("option")
	dateID = []
	for x in range (0 , len(dateChoices)):
		tag = dateChoices[x]
		dateID.append(tag['value'])
	i = 0
	while (timestamp >= int(dateID[i])):
		i +=1;
	return dateID[i];

def StrikeParse(dateID,currentprice,companyid):
	url = urllib.request.urlopen("http://finance.yahoo.com/quote/"+companyid+"/options?p="+companyid+"&straddle=true&date="+dateID)
	text = url.read()
	soup = BeautifulSoup(text, 'lxml')
	calls = soup.find_all("td" , {"class" : "data-col0 Ta(end) Pstart(10px)"})
	strikes = soup.find_all("td" , {"class" : "data-col5 Ta(c) Px(10px)"})
	puts = soup.find_all("td", {"class" : "data-col6 Ta(end) Pstart(10px)"})
	"""
	for x in range (0, len(strikes)):
		print (calls[x].text)
		print (strikes[x].text)
		print (puts[x].text)
		print("\n")
	"""
	lastStockPrice = currentprice;
	difference = []
	min = sys.maxsize
	index = 0;
	for x in range(0, len(strikes)):
		a = abs(lastStockPrice - (float)(strikes[x].text));
		if (a < min):
			min = a;
			index = x;

	#print(index);
	#print(calls[index].text)
	#print(strikes[index].text)
	#print(puts[index].text)
	delta = (((float)(calls[index].text) + (float)(puts[index].text))/lastStockPrice) * 100;
	#print(delta)
	return delta

def StockPricePlot(stockprice,UTC,high,low,companyid): 
	
	data = [
	    go.Scatter(
	        x=stockprice.reset_index()['Date'], # assign x as the dataframe column 'x'
	        y=stockprice['Close'],
	        name = companyid + " Stock Price"
	    ),
	    go.Scatter(
	    	x=[UTC,UTC],
	    	y=[high,low],
	    	name = 	"Predicted Range of Movement"
	    )
	]

	layout = go.Layout(
		hovermode= 'closest',
	    title=companyid+' Stockprice History',
	    yaxis=dict(title='Stockprice'),
	    xaxis=dict(title='Date', range=["2017-05-01","2017-06-31"])
	)

	fig = go.Figure(data=data, layout=layout)

	# IPython notebook
	# py.iplot(fig, filename='pandas/line-plot-title')

	url = py.plot(fig, filename='stockprice-history',auto_open = False)
	#print(tls.get_embed("https://plot.ly/~jledinh/1/apple-stockprice-history/#plot"))

def UTCtoDateTime(dateID):
	return datetime.fromtimestamp(int(dateID)+86400).strftime('%Y-%m-%d')

#Main Function
def main(n, stockindex, companyid):
#parser = argparse.ArgumentParser(description='Process ish')
#parser.add_argument('', metavar='N', type=string,)
#print(s[1][0:4]);
	year = int(n[0:4])
	month = int(n[5:7])
	day = int(n[8:10])
	d = int(datetime(year,month,day).timestamp());
	#stockindex = "NASDAQ"
	#companyid = "AAPL"
	dateID = DateParse(d,companyid);
	stockprice =  quandl.get("GOOG/"+stockindex+"_"+companyid,trim_start="2017-05-01")
	currentprice = stockprice['Close'][len(stockprice)-1]
	percent = StrikeParse(dateID,currentprice,companyid)
	high = currentprice + (currentprice * percent) / 100
	low = currentprice - (currentprice * percent) / 100
	UTC = UTCtoDateTime(dateID)
	StockPricePlot(stockprice, UTC,high,low, companyid)
	print (d)
