from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.exceptions import NotFound, BadRequest

products_app = Blueprint("products_app", __name__)


PRODUCTS_DATA = {
    1: "Laptop",
    2: "Smartphone",
    3: "Tablet",
}


@products_app.route("/", endpoint="list")
def get_products_list():
    return render_template("products/list.html", products=PRODUCTS_DATA)


@products_app.route("/<int:product_id>/", endpoint="detail")
def get_product(product_id: int):
    product_name = PRODUCTS_DATA.get(product_id)
    if product_name is None:
        raise NotFound(f"No product for id {product_id}")
    return render_template(
        "products/detail.html",
        product_id=product_id,
        product_name=product_name,
    )


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def create_product():
    if request.method == "GET":
        return render_template("products/add.html")

    product_name = request.form.get("product-name")
    if not product_name:
        raise BadRequest("Please provide product name!")

    product_id = len(PRODUCTS_DATA) + 1
    PRODUCTS_DATA[product_id] = product_name
    return redirect(url_for("products_app.detail", product_id=product_id))
