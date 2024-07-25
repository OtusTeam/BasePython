from flask import Flask
from flask import request
from flask import render_template

from views.products import products_app

app = Flask(__name__)
app.register_blueprint(products_app)


@app.route("/", endpoint="index")
def hello():
    return render_template("index.html")


@app.route("/hello/")
def hello_optional_name():
    name = request.args.get("name") or ""
    # return f"<h1>Hello {name}</h1>"
    name = name.strip()
    if not name:
        name = "World"
    return {
        "name": name,
        "ids": request.args.getlist("id"),
    }


@app.route("/hello/<name>/")
def hello_name(name):
    # return f"<h1>Hello {name}</h1>"
    name = name.strip()
    return render_template(
        "hello.html",
        name=name,
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5050,
    )
