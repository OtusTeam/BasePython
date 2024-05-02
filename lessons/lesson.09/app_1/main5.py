import users as users_crud
import products

# from abc import utils as utils_abc
# from qwe import utils as utils_qwe


def main():
    print("Hello world!")
    print()

    print(users_crud)

    users_crud.create("John")
    users_crud.create("Bob")

    users_crud.update("Bob", friend="Alice")

    users_crud.delete("Sam")

    print()
    products.create("Laptop")
    products.create("PC")

    products.update("PC", cpu="ABC")


if __name__ == "__main__":
    main()
