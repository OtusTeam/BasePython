from products import *
from users import *


def main():
    print("Hello main!")
    print("Users magic const:", USERS_MAGIC_CONST)
    bob = create("Bob")
    alice = create("Alice")

    update("Bob", email="bob@abc.com")

    delete("Alice")

    create("Smartphone")
    create("Laptop")
    update("Laptop", description="Lightest Laptop")


if __name__ == "__main__":
    main()
