from flask import Flask, request, render_template

from views.products import products_app

app = Flask(__name__)


app.config.update(
    ENV="development",
    SECRET_KEY="sdkjnslkdfgnajrsgoiqejrogj3qo4itgj",
)

app.register_blueprint(products_app, url_prefix="/products")


@app.route("/")
def hello_world():
    print_request()
    # return "<h1>Hello, World!</h1>"
    return render_template("index.html")
    # return render_template("base.html")


def print_request():
    print("request:", request)
    print("request.method", request.method)
    print("request.path", request.path)


@app.route("/hello/")
@app.route("/hello/<name>/")
def hello_view(name: str = None):
    print_request()
    if name is None:
        name = request.args.get("name", "")
    name = name.strip()
    if not name:
        name = "World"
    # names = request.args.getlist("name")
    # print(request.args)
    # return {"message": "Hello!", "name": name, "names": names}
    return {"message": f"Hello {name}!"}


@app.route("/items/<int:item_id>/")
def get_item(item_id: int):
    return {
        "item": {"id": item_id},
    }


@app.route("/items/<item_id>/")
def get_item_string(item_id: str):
    return {
        "item_id": item_id.upper(),
    }


# @app.route("/hello/<name>/")
# def hello_name(name: str):
#     return {"message": f"Hello {name}!"}


if __name__ == "__main__":
    app.run(debug=True)

