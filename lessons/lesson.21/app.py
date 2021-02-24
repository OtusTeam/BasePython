from flask import Flask, request

from views.products import product_app


app = Flask(__name__)

app.register_blueprint(product_app, url_prefix="/products")


@app.route("/", methods=["GET", "POST"])
def hello_world():
    print(request.environ)
    if request.method == "GET":
        return "Hello, World!"

    # print("data:", request.form)
    # print("name:", request.form.get("name"))
    # print("name list:", request.form.getlist("name"))

    name = request.form.get("name")
    return f"Hello {name}!"


@app.route("/hello/")
@app.route("/hello/<name>/")
def hello(name="World"):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5000,
        debug=True,
    )
