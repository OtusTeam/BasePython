from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from werkzeug.exceptions import BadRequest

from models import db, Product


product_app = Blueprint("product_app", __name__)


@product_app.route("/")
def product_list():
    products = Product.query.filter_by(deleted=False).order_by(Product.id).all()
    return render_template("products/index.html", products=products)


@product_app.route("/<int:product_id>/", methods=['GET', 'DELETE'])
def product_detail(product_id: int):
    product = Product.query.filter_by(id=product_id).one_or_none()
    if product is None:
        raise BadRequest(f"Invalid product id #{product_id}")

    if request.method == 'DELETE':
        product.deleted = True
        db.session.commit()
        return jsonify(ok=True)

    return render_template("products/detail.html", product=product)


@product_app.route("/add/", methods=["GET", "POST"], endpoint="product_add")
def add_product():
    if request.method == "GET":
        return render_template("products/add.html")

    data = request.form
    product_name = data.get("product-name")
    if not product_name:
        raise BadRequest("product name is required")
    is_new = bool(data.get("is-new"))
    product = Product(name=product_name, is_new=is_new, deleted=False)
    db.session.add(product)
    db.session.commit()
    return redirect(url_for("product_app.product_list"))
