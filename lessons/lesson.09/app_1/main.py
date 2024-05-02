import users
import products


def main():
    print("Hello world!")
    print()

    users.create("John")
    users.create("Bob")

    users.update("Bob", friend="Alice")

    users.delete("Sam")

    print()
    products.create("Laptop")
    products.create("PC")

    products.update("PC", cpu="ABC")


if __name__ == "__main__":
    main()
