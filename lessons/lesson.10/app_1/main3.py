from users import create, delete as delete_user


def main():
    print("Hello main!")

    create("Nick")
    create("Bob")

    # update("Nick", age=20, city="New York")
    # update("Bob", email="bob@example.com", job="Software Engineering")

    delete_user("Nick")


if __name__ == "__main__":
    main()
