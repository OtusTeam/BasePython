from http import HTTPStatus

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
)
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError

from forms import ProductForm
from models import Product
from models.database import db

products_app = Blueprint("products_app", __name__)


@products_app.get("/", endpoint="products_list")
def list_products():
    products: list[Product] = Product.query.all()
    return render_template("products/list.html", products=products)


@products_app.get("/<int:product_id>/", endpoint="product_details")
def get_product(product_id: int):
    product = Product.query.get(product_id)
    if product is None:
        raise NotFound(f"Product #{product_id} not found!")

    return render_template(
        "products/details.html",
        product=product,
    )


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    form = ProductForm()
    if request.method == "GET":
        return render_template("products/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("products/add.html", form=form), HTTPStatus.BAD_REQUEST

    product_name = form.data["name"]
    product_is_new = form.data["is_new"]
    product = Product(name=product_name, is_new=product_is_new)
    db.session.add(product)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"could not save product, probably name {product_name!r} is not unique")
    except DatabaseError:
        db.session.rollback()
        raise InternalServerError(f"could not save product, unexpected error")

    product_url = url_for("products_app.product_details", product_id=product.id)
    return redirect(product_url)
