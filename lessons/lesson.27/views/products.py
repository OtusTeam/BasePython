import logging
from http import HTTPStatus

from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError
from sqlalchemy.exc import IntegrityError, DatabaseError

from models import Product
from models.database import db

log = logging.getLogger(__name__)

products_app = Blueprint("products_app", __name__)


PRODUCTS_DATA = {
    1: "Laptop",
    2: "Smartphone",
    3: "Tablet",
}


@products_app.route("/", endpoint="list")
def get_products_list():
    products = Product.query.all()
    return render_template("products/list.html", products=products)


@products_app.route("/<int:product_id>/", methods=["GET", "DELETE"], endpoint="detail")
def get_product(product_id: int):
    product = Product.query.filter_by(id=product_id).one_or_none()
    if product is None:
        raise NotFound(f"No product for id {product_id}")

    if request.method == "GET":
        return render_template(
            "products/detail.html",
            product=product,
        )

    # if DELETE:
    db.session.delete(product)
    try:
        db.session.commit()
    except DatabaseError:
        log.exception("Could not delete product %, got database error", product)
        db.session.rollback()
        raise InternalServerError("Error deleting product")
    return "", HTTPStatus.NO_CONTENT


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def create_product():
    if request.method == "GET":
        return render_template("products/add.html")

    product_name = request.form.get("product-name")
    if not product_name:
        raise BadRequest("Please provide product name!")

    product = Product(name=product_name)
    db.session.add(product)
    try:
        db.session.commit()
    except IntegrityError:
        log.exception("Could not add product, got integrity error")
        db.session.rollback()
        raise BadRequest("Error adding new product, probably the name is not unique")
    except DatabaseError:
        log.exception("Could not add product, got database error")
        db.session.rollback()
        raise InternalServerError("Error adding new product")

    return redirect(url_for("products_app.detail", product_id=product.id))
