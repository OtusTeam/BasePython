from flask import Flask, request, render_template

from views.products import products_app

app = Flask(__name__)
app.register_blueprint(products_app)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/hello/")
def hello_name_qs():
    name = request.args.get("name", "World")
    return f"Hello {name}!"


@app.route("/hello/<name>/")
def hello_name_path(name):
    return f"Hello {name}!"


# @app.route("/products/<int:product_id>/")
# def get_product_id(product_id):
#     # return jsonify({"product_id": product_id})
#     return jsonify(product_id=product_id)


# @app.route("/products/add/")
# def get_product_id(product_id):
#     # return jsonify({"product_id": product_id})
#     return jsonify(product_id=product_id)
