from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Docker1235679101112!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)