from http import HTTPStatus

from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
)
from werkzeug.exceptions import (
    NotFound,
)

from views.forms import ProductForm
from models import Product
from .crud import products_storage as storage

products_app = Blueprint("products_app", __name__, url_prefix="/products")


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
    form = ProductForm()
    if request.method == "GET":
        return render_template(
            "products/add.html",
            form=form,
        )

    if not form.validate_on_submit():
        return (
            render_template(
                "products/add.html",
                form=form,
            ),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )

    product_name = form.name.data
    product_price = form.price.data
    product = storage.create(name=product_name, price=product_price)
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


@products_app.route(
    "/<int:product_id>/confirm-delete/",
    methods=["GET", "POST"],
    endpoint="delete",
)
def delete_product(product_id: int):
    product = Product.query.get_or_404(
        ident=product_id,
        description=f"Product with id #{product_id} not found!",
    )
    if request.method == "GET":
        return render_template(
            "products/confirm-delete.html",
            product=product,
        )

    storage.delete(product)
    return redirect(url_for("products_app.list"))
