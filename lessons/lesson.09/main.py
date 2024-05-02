import os

from core.models import Article
import crud


def main():
    # get current working directory
    print("workdir:", os.getcwd())
    print("current file:", __file__)
    print("Article:", Article)
    print(crud)
    print(crud.users)
    print(crud.products)

    print()
    print(crud.actions.create_product("Laptop"))
    print()
    print(crud.actions.create_user("Bob", default_product_name="PC"))


if __name__ == "__main__":
    main()
