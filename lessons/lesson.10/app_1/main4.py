# from users import create, delete, update

# NEVER DO THIS!
from users import *
from products import *


def main():
    print("Hello main!")

    create("Nick")
    create("Bob")

    update("Nick", age=20, city="New York")
    update("Bob", email="bob@example.com", job="Software Engineering")

    delete("Nick")


if __name__ == "__main__":
    main()
