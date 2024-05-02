from users import create, update, delete

# import products
from products import (
    create as create_product,
    update as update_product,
)
# from products import create


def main():
    print("Hello world!")
    print()

    create("John")
    create("Bob")

    update("Bob", friend="Alice")

    delete("Sam")

    print()
    create_product("Laptop")
    create_product("PC")

    update_product("PC", cpu="ABC")


if __name__ == "__main__":
    main()
