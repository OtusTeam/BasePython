from dataclasses import dataclass, field

from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import BadRequest, NotFound

products_app = Blueprint(
    "products_app",
    __name__,
    url_prefix="/products",
)


@dataclass(slots=True)
class Product:
    id: int
    name: str


@dataclass
class ProductsStorage:
    last_id: int = 0
    products: dict[int, Product] = field(default_factory=dict)

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def add_product(self, name: str) -> Product:
        product = Product(id=self.next_id, name=name)
        self.products[product.id] = product
        return product

    def get_all_products(self) -> list[Product]:
        return list(self.products.values())

    def get_product_by_id(self, product_id: int) -> Product | None:
        return self.products.get(product_id)


storage = ProductsStorage()
storage.add_product("Table")
storage.add_product("Laptop")
# storage.add_product("Smartphone")


@products_app.get("/", endpoint="list")
def get_products_list():
    return render_template(
        "products/index.html",
        products=storage.get_all_products(),
    )


@products_app.route("/add/", methods={"GET", "POST"}, endpoint="add")
def create_product():
    if request.method == "GET":
        return render_template("products/add.html")

    name = request.form.get("product-name")
    if not name:
        raise BadRequest("field `product-name` required")

    product = storage.add_product(name)
    # return redirect("/products/")
    # url = url_for("products_app.list")
    url = url_for("products_app.detail", product_id=product.id)
    return redirect(url)


@products_app.get("/<int:product_id>/", endpoint="detail")
def get_product_by_id(product_id: int):
    product = storage.get_product_by_id(product_id)
    if product is None:
        raise NotFound(f"Product #{product_id} not found!")

    return render_template(
        "products/detail.html",
        product=product,
    )
