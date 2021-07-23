from flask import Blueprint, request, jsonify, render_template, url_for, redirect
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError

from web_app.models import db
from web_app.models import Product

products_app = Blueprint("products_app", __name__, url_prefix="/products")


@products_app.route("/", endpoint="list")
def list_products():
    products = Product.query.all()
    return render_template("products/index.html", products=products)


@products_app.route("/<int:product_id>/", endpoint="details")
def get_product(product_id):
    product = Product.query.filter_by(id=product_id).one_or_none()
    if product is None:
        raise NotFound(f"Product #{product_id} doesn't exist.")
    # return jsonify(product_id=product_id, name=product_name)
    return render_template(
        "products/details.html",
        product=product,
    )


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def product_add():
    if request.method == "GET":
        return render_template("products/add.html")

    product_name = request.form.get("product-name")
    if not product_name:
        raise BadRequest("Field product-name is required!")

    product = Product(name=product_name)
    db.session.add(product)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise InternalServerError(f"Could not save product with name {product_name!r}")

    url = url_for("products_app.details", product_id=product.id)
    return redirect(url)
