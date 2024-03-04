# users actions
USER_MAGIC_ID = 42


def create(name):
    print(f"Created user {name=}")
    return ...


def update(name, **kwargs):
    print(f"Updated user {name=} with {kwargs=}")


def delete(name):
    print(f"Deleted user {name=}")


# print(__file__)
# print(__name__)

def main():
    create("John")
    create("Sam")

    update("John", age=20, city="New York")
    update("Sam", email="sam@example.com", job="Software Engineering")

    delete("Sam")

    # very slow function:
    # find_pi_1000000_fraction()

    print("END of users")


if __name__ == "__main__":
    main()
