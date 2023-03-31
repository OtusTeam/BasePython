from http import HTTPStatus

from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import or_
from werkzeug.exceptions import NotFound

from .forms import ProductForm
from models import db, Product

products_app = Blueprint(
    "products_app",
    __name__,
    url_prefix="/products",
)

# short_description = f"Product #{product.id} ({product.name}) short description"


@products_app.get("/", endpoint="list")
def get_products():
    # products = db.session.query(Product).all()
    search = request.args.get("search") or ""
    query = Product.query
    if search:
        query = query.filter(
            or_(
                Product.name.ilike(f"%{search}%"),
                Product.short_description.ilike(f"%{search}%"),
            ),
        )
    products = query.order_by(Product.id).all()

    return render_template(
        "products/list.html",
        products=products,
        search=search,
    )


def get_product_or_raise(product_id: int) -> Product:
    return Product.query.filter_by(id=product_id).one_or_404(
        description=f"Product #{product_id} not found!",
    )


@products_app.get("/<int:product_id>/", endpoint="details")
def get_product_details(product_id: int):
    product = get_product_or_raise(product_id)
    return render_template("products/details.html", product=product)


@products_app.route(
    "/<int:product_id>/update/",
    methods=["GET", "POST"],
    endpoint="update",
)
def update_product_details(product_id: int):
    product = get_product_or_raise(product_id)
    form = ProductForm()
    if request.method == "GET":
        return render_template(
            "products/update.html",
            form=form,
            product=product,
        )

    if not form.validate_on_submit():
        return (
            render_template(
                "products/update.html",
                form=form,
                product=product,
            ),
            HTTPStatus.BAD_REQUEST,
        )

    # Product.query.filter_by(id=product_id).update(
    #     {
    #         "name": form.data["name"],
    #         "short_description": form.data["short_description"],
    #     }
    # )
    product.name = form.data["name"]
    product.short_description = form.data["short_description"]
    db.session.add(product)
    db.session.commit()
    flash(f"Product #{product.id} was updated!", category="info")
    url = url_for("products_app.details", product_id=product.id)
    return redirect(url)


@products_app.route(
    "/<int:product_id>/delete/",
    methods=["GET", "POST"],
    endpoint="delete",
)
def delete_product(product_id: int):
    product = get_product_or_raise(product_id)

    if request.method == "GET":
        return render_template("products/delete.html", product=product)

    product_name = product.name
    db.session.delete(product)
    db.session.commit()
    flash(f"Deleted product {product_name}!", category="warning")
    url = url_for("products_app.list")
    return redirect(url)


@products_app.route("/create/", methods=["GET", "POST"], endpoint="create")
def create_product():
    form = ProductForm()
    if request.method == "GET":
        return render_template("products/create.html", form=form)

    if not form.validate_on_submit():
        return (
            render_template("products/create.html", form=form),
            HTTPStatus.BAD_REQUEST,
        )

    product = Product(
        name=form.data["name"],
        short_description=form.data["short_description"],
    )
    db.session.add(product)
    db.session.commit()
    flash(f"Product {product.name} was created!", category="success")
    url = url_for("products_app.details", product_id=product.id)
    return redirect(url)
