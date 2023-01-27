"""
Main
"""
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from werkzeug.exceptions import NotFound

from views.products import products_app

app = Flask(__name__)
app.register_blueprint(products_app, url_prefix="/products")


def print_request():
    """
    print_request
    :return:
    """
    print("request:", request)
    print("headers", request.headers)


@app.get("/")
def get_root():
    """
    get root
    :return:
    """
    # print_request()
    print(request.args)
    # return {
    #     "request.args": request.args,
    #     "request.args['foo']": request.args["foo"],
    #     "request.args.get('foo')": request.args.get("foo"),
    #     "request.args.getlist('foo')": request.args.getlist("foo"),
    #     "request.args.getlist('spam')": request.args.getlist("spam"),
    #     "request.args.to_dict()": request.args.to_dict(),
    #     "request.args.to_dict(flat=False)": request.args.to_dict(flat=False),
    #     "message": "Hello!",
    # }
    return render_template("index.html")


@app.route("/hello/")
@app.route("/hello/<name>/")
def hello_world(name: str = None):
    """
    hello_world
    :param name:
    :return:
    """
    # print_request()
    if name is None:
        name = request.args.get("name", "world")
    return f"<h2>Hello {name}!</h2>"


@app.get("/items/")
def get_items():
    """
    get_items
    :return:
    """
    return jsonify(
        {
            "items": [
                {"id": 1},
                {"id": 2},
            ],
        },
        # spam="eggs",
    )


@app.get("/items/<int:item_id>/")
def get_item(item_id: int):
    """
    get_item
    :param item_id:
    :return:
    """
    return {"item": {"id": item_id}}


@app.get("/items/<item_id>/")
def get_item_as_string(item_id: str):
    """
    get_item_as_string
    :param item_id:
    :return:
    """
    return {"item_id": item_id.upper()}


@app.errorhandler(404)
def handle_404(error):
    """
    handle_404
    :param error:
    :return:
    """
    if isinstance(error, NotFound) and error.description != NotFound.description:
        return error
    return f"<h1>eroror: {error}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
