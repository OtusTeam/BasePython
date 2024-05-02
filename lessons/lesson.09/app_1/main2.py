from users import create, update, delete

from products import create, update
# from products import create


def main():
    print("Hello world!")
    print()

    create("John")
    create("Bob")

    update("Bob", friend="Alice")

    delete("Sam")


if __name__ == "__main__":
    main()
