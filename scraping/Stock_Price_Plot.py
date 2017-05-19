import plotly.plotly as py
import plotly.graph_objs as go
import quandl
import plotly.tools as tls
stockprice =  quandl.get("GOOG/NASDAQ_AAPL",trim_start="2017-01-01")
currentprice = stockprice['Close'][len(stockprice)-1]
data = [
    go.Scatter(
        x=stockprice.reset_index()['Date'], # assign x as the dataframe column 'x'
        y=stockprice['Close']
    )
]

layout = go.Layout(
    title='Apple Stockprice History',
    yaxis=dict(title='Stockprice'),
    xaxis=dict(title='Date', range=["2017-01-01","2017-06-31"])
)

fig = go.Figure(data=data, layout=layout)

# IPython notebook
# py.iplot(fig, filename='pandas/line-plot-title')

url = py.plot(fig, filename='line-plot-title')
print(tls.get_embed("https://plot.ly/~jledinh/1/apple-stockprice-history/#plot"))