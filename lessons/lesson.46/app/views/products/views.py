from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    url_for,
    flash,
)
from werkzeug.exceptions import BadRequest, NotFound

from models import Product, db
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
        products=crud.get_products(),
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

    product = crud.create_product(
        name=product_name,
    )

    flash(f"Created product {product_name!r}!", category="success")
    # return {"product": product.name, "id": product.id}
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
    product: Product = Product.query.get_or_404(
        product_id,
        description=f"Product #{product_id} not found!",
    )
    return render_template(
        "products/details.html",
        product=product,
    )


@products_app.route(
    "/<int:product_id>/confirm-delete/",
    endpoint="delete",
    methods=["GET", "POST"],
)
def delete_product(product_id: int):
    product: Product = Product.query.get_or_404(
        product_id,
        description=f"Product #{product_id} not found!",
    )
    if request.method == "GET":
        return render_template(
            "products/delete.html",
            product=product,
        )

    product_name = product.name
    db.session.delete(product)
    db.session.commit()

    flash(f"Deleted {product_name!r} successfully!", category="warning")
    url = url_for("products_app.list")
    return redirect(url)
