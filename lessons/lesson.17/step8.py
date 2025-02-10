from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():

    return """<h1>Главная!</h1>
    <p>http://127.0.0.1:5000<p>
    <p>http://127.0.0.1:5000<p>
    <p>http://127.0.0.1:5000<p>
    """

@app.route("/hello")
def hello():
    return "Helllo!"

if __name__ == "__main__":
    app.run(debug=True)