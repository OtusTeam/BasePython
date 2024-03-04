import users as users_crud
import products as products_crud

import items_processor as ip


def users():
    return ["users"]


def main():
    print("Hello main!")

    print(users())

    users_crud.create("Nick")
    users_crud.create("Bob")

    users_crud.update("Nick", age=20, city="New York")
    users_crud.update("Bob", email="bob@example.com", job="Software Engineering")

    products_crud.create("Laptop")
    products_crud.create("Tablet")

    print(ip)
    print(ip.ItemsProcessor)


if __name__ == "__main__":
    main()
