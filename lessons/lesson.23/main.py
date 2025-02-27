from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/about")
def hello():
    return "О нас!!!!!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")