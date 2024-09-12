from http import HTTPStatus

from flask import Blueprint
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

# from flask import Response

# from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import NotFound

from .crud import storage
from .models import ProductCreate

products_app = Blueprint(
    "products_app",
    __name__,
    url_prefix="/products",
)


@products_app.route("/", endpoint="index")
def get_products_list():
    return render_template(
        "products/index.html",
        products=storage.get(),
    )


@products_app.route(
    "/add/",
    methods=["GET", "POST"],
    endpoint="add",
)
def add_product():  # pylint:disable=missing-function-docstring
    if request.method != "POST":
        return render_template("products/add.html")

    product_name = request.form.get("product-name") or "Default"
    product_price = request.form.get("product-price") or 0


    product = storage.create(
        product_create=ProductCreate(
            name=product_name,
            price=product_price,
        ),
    )
    new_url = url_for("products_app.details", product_id=product.id)
    return redirect(new_url, code=HTTPStatus.SEE_OTHER)


@products_app.route("/<int:product_id>/", endpoint="details")
def get_product_by_id(product_id: int):
    """
    Get product by id
    :param product_id:
    :return:
    """
    product = storage.get_by_id(product_id)
    if not product:
        # response = Response(render_template("error.html"), status=404)
        # raise HTTPException(response=response)
        raise NotFound(f"Product #{product_id} not found")
    return render_template(
        "products/details.html",
        product=product,
    )
