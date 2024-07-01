import os
import crud
from crud.actions import create_user
from crud.actions import create_product as create_p

from core.models import Article, Post


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
    print("Post:", Post)

    print()
    create_user("Bob", product_name="Smartphone")
    print()
    create_p("Laptop")


if __name__ == "__main__":
    main()
