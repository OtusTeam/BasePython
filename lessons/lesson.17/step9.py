from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    context = {

    }
    return render_template("index.html", name='Bob')


@app.route("/hello")
def hello():
    return "Helllo!"


if __name__ == "__main__":
    app.run(debug=True)