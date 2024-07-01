import users


def main():
    print("Hello!")
    print("Users magic const:", users.USERS_MAGIC_CONST)
    print("users:", users)

    users.create("Bob")
    users.create("Alice")

    users.update("Alice", email="alice@abc.com")

    users.delete("Bob")


if __name__ == "__main__":
    main()
