from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    url_for,
)
from werkzeug.exceptions import BadRequest, NotFound

from . import crud

products_app = Blueprint(
    "products_app",
    __name__,
    url_prefix="/products",
)


@products_app.get(
    "/",
    endpoint="list",
)
def get_products():
    return render_template(
        "products/list.html",
        products=crud.storage.get_products(),
    )


@products_app.route(
    "/add/",
    endpoint="add",
    methods=["GET", "POST"],
)
def create_product():
    if request.method == "GET":
        return render_template("products/add.html")

    product_name = request.form.get("product-name", "")
    product_name = product_name.strip()
    if not product_name:
        raise BadRequest("product-name is required!")

    product = crud.storage.create_product(
        name=product_name,
    )

    url = url_for(
        "products_app.details",
        product_id=product.id,
    )
    return redirect(url)


@products_app.get(
    "/<int:product_id>/",
    endpoint="details",
)
def get_product_details(product_id: int):
    product: crud.Product | None = crud.storage.get_product(
        product_id=product_id,
    )
    if product is None:
        raise NotFound(
            description=f"Product #{product_id} not found!",
        )

    return render_template(
        "products/details.html",
        product=product,
    )
