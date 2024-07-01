import os
import crud

from core.models import Article



def main():
    print("Hello!")
    print("Users magic const:", crud.users.USERS_MAGIC_CONST)
    print("current working directory:", os.getcwd())
    print("current file:", __file__)
    print("os:", os)
    print("crud:", crud)
    print("users:", crud.users)
    print("crud.users.create:", crud.users.create)
    print("Article:", Article)

    print()
    crud.actions.create_user("Bob", product_name="Smartphone")
    print()
    crud.actions.create_product("Laptop")


if __name__ == "__main__":
    main()
