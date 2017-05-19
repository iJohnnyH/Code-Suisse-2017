from flask import Flask, render_template, request
import scraping/master_parse

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("docs/indexNoGraph.html")


@app.route("/<date>")
def date(date):
    print(date)
    return render_template("docs/indexWithGraph.html", date=date)

if __name__ == "__main__":
    app.run()

@app.route('/newCompany', methods = ['POST'])
def newCompany():
    company = request.form['companyName']
    print(company)
    return render_template('docs/indexWithGraph.html')