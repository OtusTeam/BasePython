from users import (
    USERS_MAGIC_CONST,
    create,
    update,
    delete,
)


def main():
    print("Hello main!")
    print("Users magic const:", USERS_MAGIC_CONST)
    bob = create("Bob")
    alice = create("Alice")

    update("Bob", email="bob@abc.com")

    delete("Alice")


if __name__ == "__main__":
    main()
