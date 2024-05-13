from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
)
from werkzeug.exceptions import (
    NotFound,
    BadRequest,
)

from .crud import products_storage as storage

products_app = Blueprint(
    "products_app",
    __name__,
    url_prefix="/products"
)


@products_app.get("/", endpoint="list")
def get_products():
    # products = Product.query.all()
    # products = storage.get()
    return render_template(
        "products/list.html",
        # products=products,
        products=storage.get(),
    )


@products_app.route("/add/", endpoint="add", methods=["GET", "POST"])
def add_product():
    if request.method == "GET":
        return render_template("products/add.html")

    product_name = request.form.get("product-name", "")
    product_name = product_name.strip()
    if not product_name:
        raise BadRequest("product-name is required")
    product = storage.create(name=product_name)
    url = url_for("products_app.details", product_id=product.id)
    return redirect(url)


@products_app.get("/<int:product_id>/", endpoint="details")
def get_product(product_id: int):
    product = storage.get_by_id(product_id)
    if product is None:
        raise NotFound(f"Product with id #{product_id} not found!")

    return render_template(
        "products/details.html",
        product=product,
    )
