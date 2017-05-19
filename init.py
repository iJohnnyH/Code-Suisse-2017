from flask import Flask, render_template, request
import master_parse

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("docs/indexNoGraph.html")
    
@app.route("/<date>")
def date(date):
    print(date)
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
    return render_template("docs/indexWithGraph.html", date=date)

if __name__ == "__main__":
    app.run()
