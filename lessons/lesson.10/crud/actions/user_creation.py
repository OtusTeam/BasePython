from crud.users.create import create as create_user
from crud.products.create import create as create_product


def user_create(name):
    u = create_user(name)
    create_product(f"Default {name} product")
    return u
