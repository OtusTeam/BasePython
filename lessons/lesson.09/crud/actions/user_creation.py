from crud import users
from crud import products


def create_user(name: str, product_name: str | None):
    user = users.create(name)
    if product_name is None:
        product_name = name

    product_name = f"Product {product_name!r}"
    products.create(product_name)

    return user
