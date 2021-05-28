from flask import Blueprint, request, jsonify, render_template, url_for, redirect
from werkzeug.exceptions import NotFound, BadRequest


products_app = Blueprint("products_app", __name__, url_prefix="/products")

PRODUCTS = {
    1: "Laptop",
    2: "Smartphone",
    3: "Tablet",
}


@products_app.route("/", endpoint="list")
def list_products():
    return render_template("products/index.html", products=PRODUCTS)


@products_app.route("/<int:product_id>/", endpoint="details")
def get_product(product_id):
    product_name = PRODUCTS.get(product_id)
    if product_name is None:
        raise NotFound(f"Product #{product_id} doesn't exist.")
    # return jsonify(product_id=product_id, name=product_name)
    return render_template(
        "products/details.html",
        product_id=product_id,
        product_name=product_name,
    )


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def product_add():
    if request.method == "GET":
        return render_template("products/add.html")

    product_name = request.form.get("product-name")
    if not product_name:
        raise BadRequest("Field product-name is required!")

    new_product_id = len(PRODUCTS) + 1
    PRODUCTS[new_product_id] = product_name
    url = url_for("products_app.details", product_id=new_product_id)
    return redirect(url)
