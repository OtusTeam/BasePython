from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
)
from werkzeug.exceptions import BadRequest, NotFound

products_app = Blueprint("products_app", __name__)

PRODUCTS = {
    1: "Laptop",
    2: "Desktop",
    3: "Smartphone",
}


@products_app.route("/", endpoint="list")
def products_list():
    return render_template(
        "products/list.html",
        products=list(PRODUCTS.items()),
    )


@products_app.route("/<int:product_id>/", endpoint="details")
def get_product(product_id: int):
    product_name = PRODUCTS.get(product_id)
    if product_name is None:
        raise NotFound(f"product #{product_id} doesn't exist!")
    return render_template(
        "products/details.html",
        product_id=product_id,
        product_name=product_name,
    )


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    if request.method == "GET":
        return render_template("products/add.html")

    # if request.method == "POST":
    #     pass

    product_name = request.form.get("product-name")
    if not product_name:
        raise BadRequest("Field `product-name` required!")

    product_id = len(PRODUCTS) + 1
    PRODUCTS[product_id] = product_name
    url = url_for("products_app.details", product_id=product_id)
    return redirect(url)
