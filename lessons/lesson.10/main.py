# from crud import users
# from crud.users import create
from crud.users import update
from crud import actions


# from crud.users import update_user
# from users.update import update_user as update
# from users import update


def main():
    print("Hello main!")

    actions.user_create("Nick")
    actions.user_create("Bob")

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
