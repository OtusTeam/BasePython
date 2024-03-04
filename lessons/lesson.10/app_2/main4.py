# from users import *
from users import create, update_user, delete
# from users import delete


def main():
    print("Hello main!")

    create("Nick")
    create("Bob")

    update_user("Nick", age=20, city="New York")
    update_user("Bob", email="bob@example.com", job="Software Engineering")

    delete("Nick")
    # products.create("Laptop")
    # products.create("Tablet")
    #
    # print(items_processor)
    # print(items_processor.ItemsProcessor)
    # print(items_processor.ItemsProcessor())


if __name__ == "__main__":
    main()
