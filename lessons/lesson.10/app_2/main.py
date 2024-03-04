from users.create import create
# from users.update import update_user as update
from users import update


def main():
    print("Hello main!")

    create("Nick")
    create("Bob")

    update.update_user("Nick", age=20, city="New York")
    update.update_user("Bob", email="bob@example.com", job="Software Engineering")

    # products.create("Laptop")
    # products.create("Tablet")
    #
    # print(items_processor)
    # print(items_processor.ItemsProcessor)
    # print(items_processor.ItemsProcessor())


if __name__ == "__main__":
    main()
