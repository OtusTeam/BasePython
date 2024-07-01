import users


def main():
    print("Hello main!")
    print("Users magic const:", users.USERS_MAGIC_CONST)
    bob = users.create("Bob")
    alice = users.create("Alice")

    users.update("Bob", email="bob@abc.com")

    users.delete("Alice")


if __name__ == "__main__":
    main()
