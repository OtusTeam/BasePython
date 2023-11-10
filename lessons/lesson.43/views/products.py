from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import render_template
from flask import flash

from models import db, Product
from .forms.products import ProductForm


products_app = Blueprint(
    "products_app",
    __name__,
    url_prefix="/products",
)


@products_app.get("/", endpoint="list")
def get_products_list():
    products: list[Product] = Product.query.order_by(Product.id).all()
    return render_template("products/list.html", products=products)


def get_product_by_id(product_id: int) -> Product:
    return Product.query.get_or_404(
        product_id,
        description=f"Product #{product_id} not found!",
    )


@products_app.get("/<int:product_id>/", endpoint="details")
def get_product_details(product_id: int):
    product = get_product_by_id(product_id=product_id)
    return render_template("products/details.html", product=product)


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def create_new_product():
    form = ProductForm()
    if request.method == "GET":
        return render_template("products/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("products/add.html", form=form), 400

    product = Product(name=form.data["name"])
    db.session.add(product)
    db.session.commit()
    url = url_for("products_app.details", product_id=product.id)
    flash(f"Created product {product.name!r}", category="primary")
    return redirect(url)


@products_app.route(
    "/<int:product_id>/confirm-delete/",
    methods=["GET", "POST"],
    endpoint="confirm-delete",
)
def confirm_delete_product(product_id: int):
    product = get_product_by_id(product_id=product_id)
    if request.method == "GET":
        return render_template("products/confirm-delete.html", product=product)

    product_name = product.name
    db.session.delete(product)
    db.session.commit()
    flash(f"Deleted product {product_name!r}", category="warning")
    url = url_for("products_app.list")
    return redirect(url)
