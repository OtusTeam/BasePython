from flask import (
    Blueprint, render_template, request, url_for,
    redirect, flash,
)
from werkzeug.exceptions import NotFound

from views.forms.products import CreateProductForm

products_app = Blueprint(
    "products_app",
    __name__,
)

PRODUCTS = {
    1: "Laptop",
    2: "Smartphone",
    3: "Tablet",
    4: "Keyboard",
    5: "Mouse",
}


@products_app.route("/", endpoint="list")
def products_list():
    return render_template(
        "products/list.html",
        products=PRODUCTS,
    )


@products_app.route("/<int:product_id>/",
                    methods=["GET", "DELETE"],
                    endpoint="details")
def get_product_by_id(product_id: int):
    product_name = PRODUCTS.get(product_id)
    if product_name is None:
        raise NotFound(f"Product #{product_id} not found!")

    if request.method == 'GET':
        return render_template(
            "products/details.html",
            product_id=product_id,
            product_name=product_name,
        )

    if request.method == 'DELETE':
        PRODUCTS.pop(product_id)
        flash(f"Deleted product {product_name}!", "warning")
        url = url_for("products_app.list")
        return {'status': 'OK', 'url': url}


@products_app.route("/add/",
                    methods=["GET", "POST"],
                    endpoint="add")
def add_product():
    form = CreateProductForm()

    if request.method == "GET":
        return render_template("products/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("products/add.html", form=form), 400

    product_name = form.name.data
    product_id = len(PRODUCTS) + 1
    PRODUCTS[product_id] = product_name

    # flash(f"Successfully added product {product_name}!")
    url = url_for("products_app.details", product_id=product_id)
    return redirect(url)
