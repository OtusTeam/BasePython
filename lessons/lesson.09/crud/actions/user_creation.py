from crud import users
from crud import products


def create_user(name, default_product_name=None):
    u = users.create(name)
    if not default_product_name:
        default_product_name = name

    new_product_name = f"Product {default_product_name} for user {name}"
    products.create(new_product_name)

    return u
