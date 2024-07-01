from users import (
    USERS_MAGIC_CONST,
    create,
    update,
    delete,
)

import products


def main():
    print("Hello main!")
    print("Users magic const:", USERS_MAGIC_CONST)
    bob = create("Bob")
    alice = create("Alice")

    update("Bob", email="bob@abc.com")

    delete("Alice")

    products.create("Smartphone")
    products.create("Laptop")
    products.update("Laptop", description="Lightest Laptop")


if __name__ == "__main__":
    main()
