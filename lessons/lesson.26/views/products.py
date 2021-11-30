import logging

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import DatabaseError, IntegrityError
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

from models import db, Product

products_app = Blueprint("products_app", __name__)


@products_app.route("/", endpoint="list")
def list_products():
    products = Product.query.order_by(Product.id).all()
    return render_template(
        "products/list.html",
        products=products,
    )


def get_product_name_from_form():
    product_name = request.form.get("product-name")
    if name := (product_name and product_name.strip()):
        return name

    raise BadRequest("field product-name is required!")


def get_product_is_new_from_form():
    is_new = request.form.get("is-new")
    return bool(is_new)


def save_product(product_name):
    try:
        db.session.commit()
    except IntegrityError as ex:
        logging.warning("got integrity error with text %s", ex)
        raise BadRequest(f"Could not save product {product_name}, probably name is not unique")
    except DatabaseError:
        db.session.rollback()
        logging.exception("got db error!")
        raise InternalServerError(f"could not save product with name {product_name}!")


@products_app.route("/<int:product_id>/", methods=["GET", "POST"], endpoint="details")
def get_product_by_id(product_id: int):
    product = Product.query.get(product_id)
    if product is None:
        raise NotFound(f"Product with id #{product_id} not found!")

    if request.method == "GET":
        return render_template(
            "products/details.html",
            product=product,
        )

    product_name = get_product_name_from_form()
    if product.name == product_name:
        raise BadRequest(f"this product is already named {product_name}")
    if Product.query.filter_by(name=product_name).count():
        raise BadRequest(f"product with name {product_name!r} already exists!")

    product.name = product_name
    product.is_new = get_product_is_new_from_form()

    save_product(product_name)
    # return render_template(
    #     "products/details.html",
    #     product=product,
    # )
    return redirect(url_for("products_app.details", product_id=product.id))


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    if request.method == "GET":
        return render_template("products/add.html")

    product_name = get_product_name_from_form()
    is_new = get_product_is_new_from_form()
    product = Product(name=product_name, is_new=is_new)
    db.session.add(product)
    save_product(product_name)
    return redirect(url_for("products_app.details", product_id=product.id))
