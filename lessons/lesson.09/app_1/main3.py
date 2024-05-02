from products import *
from users import *


def main():
    print("Hello world!")
    print()

    create("John")
    create("Bob")

    update("Bob", friend="Alice")

    delete("Sam")

    print()
    create("Laptop")
    create("PC")

    update("PC", cpu="ABC")


if __name__ == "__main__":
    main()
