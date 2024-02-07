from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import BadRequest, NotFound

from .crud import storage, Product

products_app = Blueprint(
    "products_app",
    __name__,
    url_prefix="/products"
)


@products_app.get("/", endpoint="list")
def get_products_list():
    return render_template(
        "products/index.html",
        products=storage.get_products_list(),
    )


def get_product_by_id_or_raise_helper(product_id: int) -> Product:
    product = storage.get_product_by_id(product_id)
    if product is None:
        raise NotFound(f"product #{product_id} not found")

    return product


@products_app.get("/<int:product_id>/", endpoint="details")
def get_product_by_id_or_raise(product_id: int):
    product = get_product_by_id_or_raise_helper(product_id)

    return render_template(
        "products/details.html",
        product=product,
    )


@products_app.route("/create/", endpoint="create", methods=["GET", "POST"])
def create_new_product():
    if request.method == "GET":
        return render_template("products/create.html")

    product_name = request.form.get("product_name", "")
    product_name = product_name.strip()
    if not product_name:
        raise BadRequest("`product_name` field required")

    product = storage.create_product(name=product_name)
    # url = url_for("products_app.list")
    url = url_for("products_app.details", product_id=product.id)
    return redirect(url)


@products_app.route(
    "/<int:product_id>/confirm-delete/",
    endpoint="delete",
    methods=["GET", "POST"],
)
def delete_product(product_id: int):
    product = get_product_by_id_or_raise_helper(product_id)
    if request.method == "GET":
        return render_template(
            "products/confirm-delete.html",
            product=product
        )

    storage.delete_product(product_id)
    url = url_for("products_app.list")
    return redirect(url)
