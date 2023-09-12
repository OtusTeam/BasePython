from typing import Sequence

from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from models import db, Product

products_app = Blueprint(
    "products_app",
    __name__,
    url_prefix="/products",
)


@products_app.get("/", endpoint="list")
def get_products_list():
    stmt = select(Product).order_by(Product.id)
    # products = db.session.execute(stmt).scalars()
    products: Sequence[Product] = db.session.scalars(stmt)
    return render_template(
        "products/index.html",
        products=products,
    )


@products_app.route("/add/", methods={"GET", "POST"}, endpoint="add")
def create_product():
    if request.method == "GET":
        return render_template("products/add.html")

    name = request.form.get("product-name")
    if not name:
        raise BadRequest("field `product-name` required")

    product = Product(name=name)
    db.session.add(product)

    try:
        db.session.commit()
    except IntegrityError:
        # raise BadRequest("Such product already exists!")
        flash(f"Product {name!r} already exists", category="warning")
        return redirect(request.path)

    flash(f"Product {product.name!r} created")

    # return redirect("/products/")
    # url = url_for("products_app.list")
    url = url_for("products_app.detail", product_id=product.id)
    return redirect(url)


def get_product_by_id_or_raise(product_id: int) -> Product:
    product: Product = db.get_or_404(
        Product,
        product_id,
        description=f"Product #{product_id} not found!",
    )
    return product


@products_app.get("/<int:product_id>/", endpoint="detail")
def get_product_by_id(product_id: int):
    return render_template(
        "products/detail.html",
        product=get_product_by_id_or_raise(product_id),
    )


@products_app.route(
    "/<int:product_id>/confirm-delete/",
    methods=["GET", "POST"],
    endpoint="confirm_delete",
)
def confirm_delete_product(product_id: int):
    product = get_product_by_id_or_raise(product_id)
    if request.method == "GET":
        return render_template(
            "products/confirm-delete.html",
            product=product,
        )

    name = product.name
    db.session.delete(product)
    db.session.commit()
    flash(f"Product {name!r} deleted.", category="danger")

    return redirect(url_for("products_app.list"))
