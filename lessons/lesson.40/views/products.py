import logging

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import DatabaseError, IntegrityError
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

from models import db, Product
from views.forms.products import ProductForm

products_app = Blueprint("products_app", __name__)


@products_app.route("/", endpoint="list")
def list_products():
    products = Product.query.order_by(Product.id).all()
    return render_template(
        "products/list.html",
        products=products,
    )


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

    form = ProductForm()
    if request.method == "GET" or not form.validate_on_submit():
        return render_template(
            "products/details.html",
            product=product,
            form=form,
        )

    product_name = form.data["name"]
    if product.name == product_name:
        raise BadRequest(f"this product is already named {product_name}")
    if Product.query.filter_by(name=product_name).count():
        raise BadRequest(f"product with name {product_name!r} already exists!")

    product.name = product_name
    product.is_new = form.data["is_new"]

    save_product(product_name)
    # return render_template(
    #     "products/details.html",
    #     product=product,
    # )
    return redirect(url_for("products_app.details", product_id=product.id))


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    form = ProductForm()
    if request.method == "GET":
        return render_template("products/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("products/add.html", form=form), 400

    product = Product(name=form.data["name"], is_new=form.data["is_new"])
    db.session.add(product)
    save_product(product.name)
    return redirect(url_for("products_app.details", product_id=product.id))


@products_app.route("/reset/", methods=["POST"], endpoint="reset")
def reset_products():
    # PRODUCTS.clear()
    # PRODUCTS.update(get_default_products())
    # return {"message": "ok"}
    return {"ok": True}
