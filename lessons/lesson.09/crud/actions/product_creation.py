from crud import products
from crud import users


def create_product(name):
    p = products.create(name)
    if users.USERS_MAGIC_VARIABLE:
        print("users magic variable:", users.USERS_MAGIC_VARIABLE)

    return p
