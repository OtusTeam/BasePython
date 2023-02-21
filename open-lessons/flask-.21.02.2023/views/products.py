from dataclasses import dataclass

from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import BadRequest, NotFound


products_app = Blueprint(
    "products_app",
    __name__,
    url_prefix="/products",
)


@dataclass(frozen=True, slots=True)
class Product:
    id: int
    name: str


@dataclass(slots=True)
class ProductsStorage:
    products: dict[int, Product]
    last_index: int = 0

    @property
    def next_index(self):
        self.last_index += 1
        return self.last_index

    def create(self, name: str):
        product = Product(id=self.next_index, name=name)
        self.products[product.id] = product
        return product


storage = ProductsStorage(products={})
storage.create("Laptop")
storage.create("Desktop")
storage.create("Smartphone")


@products_app.route("/", endpoint="list")
def get_products_list():
    products = list(storage.products.values())
    return render_template("products/list.html", products=products)


@products_app.route("/<int:product_id>/", endpoint="details")
def get_product_by_id(product_id):
    product = storage.products.get(product_id)
    if product is None:
        raise NotFound(f"Product #{product_id} not found!")
    return render_template("products/details.html", product=product)


@products_app.route("/create/", methods=["GET", "POST"], endpoint="create")
def create_product():
    if request.method == "GET":
        return render_template("products/create.html")

    product_name = request.form.get("product-name") or ""
    product_name = product_name.strip()
    if not product_name:
        raise BadRequest("Field `product-name` is required!")

    product = storage.create(name=product_name)
    url = url_for('products_app.details', product_id=product.id)
    return redirect(url)
