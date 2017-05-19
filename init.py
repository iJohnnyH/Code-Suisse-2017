from flask import Flask, render_template, request
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
