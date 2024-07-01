from crud.products import create as create_p
from crud.users import USERS_MAGIC_CONST


def create_product(name: str):
    product = create_p(name)

    if USERS_MAGIC_CONST:
        print("magic const:", USERS_MAGIC_CONST)

    return product
