from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound

from my_shop.models.database import db
from my_shop.models.product import Product


product_app = Blueprint("product_app", __name__)


@product_app.route("/", endpoint="list")
def products_list():
    products = Product.query.all()
    return render_template("products/index.html", products=products)


@product_app.route("/<int:product_id>/", endpoint="details")
def product_details(product_id):
    product = Product.query.filter_by(id=product_id).one_or_none()
    if product is None:
        raise NotFound(f"Product with id {product_id} doesn't exist!")

    return render_template(
        "products/details.html",
        product=product,
    )


@product_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def product_add():
    if request.method == "GET":
        return render_template("products/add-new.html")

    product = Product(name=request.form.get("product-name"))
    db.session.add(product)
    db.session.commit()
    return redirect(url_for("product_app.list"))
