import users


def main():
    print("Hello main!")

    print(users)
    print(users.create)
    users.create("Nick")
    users.create("Bob")

    users.update_user("Nick", age=20, city="New York")
    users.update_user("Bob", email="bob@example.com", job="Software Engineering")

    # products.create("Laptop")
    # products.create("Tablet")
    #
    # print(items_processor)
    # print(items_processor.ItemsProcessor)
    # print(items_processor.ItemsProcessor())


if __name__ == "__main__":
    main()
