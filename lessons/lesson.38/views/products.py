from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash,
)
from sqlalchemy.exc import IntegrityError

# from werkzeug.exceptions import NotFound
from werkzeug.exceptions import BadRequest

from models import db, Product
from views.forms.products import ProductForm

products_app = Blueprint(
    "products_app",
    __name__,
)


@products_app.route("/", endpoint="list")
def products_list():
    products = Product.query.all()
    return render_template(
        "products/list.html",
        products=products,
    )


@products_app.route(
    "/<int:product_id>/",
    methods=["GET", "DELETE"],
    endpoint="details",
)
def get_product_by_id(product_id: int):
    product = Product.query.get_or_404(
        product_id,
        description=f"Product #{product_id} not found!",
    )
    # Product.query.filter(Product.name.ilike('')).one_or_404()
    # Product.query.filter(Product.name.ilike('')).first_or_404()

    if request.method == "GET":
        return render_template(
            "products/details.html",
            product=product,
        )

    product_name = product.name
    db.session.delete(product)
    db.session.commit()
    flash(f"Deleted product {product_name}!", "warning")
    url = url_for("products_app.list")
    return {"status": "OK", "url": url}


@products_app.route(
    "/<int:product_id>/update/",
    methods=["GET", "POST"],
    endpoint="update",
)
def update_product(product_id: int):
    product = Product.query.get_or_404(
        product_id,
        description=f"Product #{product_id} not found!",
    )

    if request.method == "GET":
        form = ProductForm(name=product.name, description=product.description)
        return render_template("products/add.html", form=form, product=product)

    form = ProductForm()
    if not form.validate_on_submit():
        return render_template("products/add.html", form=form, product=product), 400

    product.name = form.name.data
    product.description = form.description.data

    db.session.commit()

    flash(f"Successfully updated product {product.name}!")
    url = url_for("products_app.details", product_id=product.id)
    return redirect(url)


@products_app.route(
    "/add/",
    methods=["GET", "POST"],
    endpoint="add",
)
def add_product():
    form = ProductForm()

    if request.method == "GET":
        return render_template("products/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("products/add.html", form=form), 400

    product_name = form.name.data
    product_description = form.description.data
    product = Product(name=product_name, description=product_description)
    db.session.add(product)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"Could not create product {product_name!r},"
                         f" probably such product already exists.")

    flash(f"Successfully added product {product_name}!")
    url = url_for("products_app.details", product_id=product.id)
    return redirect(url)
