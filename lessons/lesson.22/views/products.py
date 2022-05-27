from flask import (
    Blueprint,
    jsonify,
    render_template,
    abort,
    request,
    redirect,
    url_for,
    flash,
)
from werkzeug.exceptions import BadRequest, NotFound

from views.forms import ProductForm

products_app = Blueprint("products_app", __name__)

PRODUCTS = {
    1: "Tablet",
    2: "Smartphone",
    3: "Laptop",
}


@products_app.get("/", endpoint="list")
def get_products_list():
    # body, status, headers
    # return {"products": ["P1", "P2", "..."]}
    # return jsonify(["P1", "P2", "..."])
    return render_template(
        "products/list.html",
        products=list(PRODUCTS.items()),
    )


@products_app.get("/<int:product_id>/", endpoint="details")
def get_product_by_id(product_id: int):
    product_name = PRODUCTS.get(product_id)
    if product_name is None:
        # abort(404, f"Product #{product_id} not found!")
        # abort()
        raise NotFound(f"Product #{product_id} not found!")

    return render_template(
        "products/details.html",
        product_id=product_id,
        product_name=product_name,
    )


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

    product_id = len(PRODUCTS) + 1
    PRODUCTS[product_id] = product_name

    flash(f"Created new product: {product_name}")
    url = url_for("products_app.details", product_id=product_id)
    return redirect(url)
