import logging

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import NotFound, InternalServerError

from views.forms import ProductForm
from models import Product
from models.database import db

log = logging.getLogger(__name__)

products_app = Blueprint("products_app", __name__)


@products_app.get("/", endpoint="list")
def get_products_list():
    # body, status, headers
    # return {"products": ["P1", "P2", "..."]}
    # return jsonify(["P1", "P2", "..."])

    products = Product.query.all()
    return render_template(
        "products/list.html",
        products=products,
    )


@products_app.route("/<int:product_id>/", methods=["GET", "DELETE"], endpoint="details")
def get_product_by_id(product_id: int):
    product = Product.query.get(product_id)
    if product is None:
        # abort(404, f"Product #{product_id} not found!")
        # abort()
        raise NotFound(f"Product #{product_id} not found!")

    if request.method == "GET":
        return render_template(
            "products/details.html",
            product=product,
        )

    product_name = product.name
    db.session.delete(product)
    db.session.commit()
    flash(f"Deleted product #{product_id} {product_name!r}", "warning")
    url = url_for("products_app.list")
    return {"ok": True, "url": url}
    # return redirect(url)


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    form = ProductForm()
    if request.method == "GET":
        return render_template("products/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("products/add.html", form=form), 400

    # product_name = request.form.get("product-name")
    # if not product_name:
    #     raise BadRequest("Field `product-name` is required!")

    product_name = form.name.data
    is_new = form.is_new.data

    product = Product(name=product_name, is_new=is_new)
    db.session.add(product)
    try:
        db.session.commit()
    except IntegrityError:
        error_text = f"Could not save product {product_name!r}, probably name is not unique!"
        form.form_errors.append(error_text)
        return render_template("products/add.html", form=form), 400

        # raise BadRequest(error_text)
    except DatabaseError:
        log.exception("could not save product %r", product_name)
        raise InternalServerError(f"could not save product {product_name!r}")

    flash(f"Created new product: {product.name}", "success")
    url = url_for("products_app.details", product_id=product.id)
    return redirect(url)
