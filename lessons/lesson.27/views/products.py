from flask import Blueprint, render_template, request, url_for, redirect, flash

from models import db, Product
from views.forms.products import CreateProductForm

products_app = Blueprint("products_app", __name__)


@products_app.route("/", endpoint="list")
def get_products():
    products = Product.query.order_by(Product.id).all()
    return render_template("products/list.html", products=products)


@products_app.route(
    "/<int:product_id>/confirm-delete/",
    methods=["GET", "POST"],
    endpoint="confirm-delete",
)
@products_app.route(
    "/<int:product_id>/",
    methods=["GET", "DELETE"],
    endpoint="details",
)
def get_product_by_id(product_id: int):
    # product = db.session.get(Product, product_id)
    # if product is None:
    #     raise NotFound(f"Product #{product_id} not found!")
    product: Product = Product.query.get_or_404(
        product_id,
        f"Product #{product_id} not found!",
    )

    confirm_delete = request.endpoint == "products_app.confirm-delete"
    if request.method == "GET":
        return render_template(
            "products/confirm-delete.html" if confirm_delete else "products/details.html",
            product=product,
        )

    db.session.delete(product)
    db.session.commit()

    flash(f"Deleted product {product.name}!", "warning")
    url = url_for("products_app.list")
    if confirm_delete:
        return redirect(url)

    return {"ok": True, "url": url}


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    form = CreateProductForm()

    if request.method == "GET":
        return render_template("products/add.html", form=form)

    # if form.validate()
    if not form.validate_on_submit():
        return render_template("products/add.html", form=form), 400

    # product_name = request.form.get("product-name", "")
    # product_name = product_name.strip()
    # if not product_name:
    #     raise BadRequest("Field `product-name` is required!")

    product_name = form.name.data
    is_new = form.is_new.data

    product = Product(name=product_name, is_new=is_new)
    db.session.add(product)
    db.session.commit()

    flash(f"Successfully added product {product.name}!")
    url = url_for("products_app.details", product_id=product.id)
    return redirect(url)
