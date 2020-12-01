from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest

product_app = Blueprint("product_app", __name__)


def get_default_products():
    return {
        1: 'Smartphone',
        2: 'Tablet',
        3: 'Laptop',
    }


PRODUCTS = get_default_products()


@product_app.route("/")
def product_list():
    return render_template("products/index.html", products=PRODUCTS)


@product_app.route("/<int:product_id>/", methods=['GET', 'DELETE'])
def product_detail(product_id: int):
    try:
        product_name = PRODUCTS[product_id]
    except KeyError:
        raise BadRequest(f"Invalid product id #{product_id}")

    if request.method == 'DELETE':
        PRODUCTS.pop(product_id)
        return jsonify(ok=True)

    return render_template(
        "products/detail.html",
        product_id=product_id,
        product_name=product_name,
    )


@product_app.route("/recover/", methods=["POST"])
def recover_products():
    PRODUCTS.update(get_default_products())
    return jsonify(ok=True)
