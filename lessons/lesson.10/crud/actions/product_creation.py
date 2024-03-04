from crud.users import USER_MAGIC_ID
from crud.products import create as create_product


def product_creation(name):
    p = create_product(name)
    if USER_MAGIC_ID:
        print("User magic id", USER_MAGIC_ID, "for name", name)
    return p
