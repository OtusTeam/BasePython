from flask import Flask, request, render_template

from views.products import products_app

app = Flask(__name__)
app.register_blueprint(products_app)


@app.route("/")
def index_view():
    return render_template("index.html")


@app.route("/hello/")
@app.route("/hello/<string:name>/")
def get_hello(name=None):
    if name is None:
        name = request.args.get("name") or ""
    if not name:
        name = "World"
    # return f"<h1>Hello {name}!</h1>"
    return render_template("hello.html", name=name)


@app.route("/items/<int:item_id>/")
def get_item_by_id(item_id):
    return {
        "data": {
            "id": item_id,
            "name": f"Name_{item_id}"
        }
    }


if __name__ == "__main__":
    app.run(debug=True)
