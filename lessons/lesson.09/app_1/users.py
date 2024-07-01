USERS_MAGIC_CONST = 42

print("users module, name:", repr(__name__))


def create(name: str):
    print("creating user", name)
    return {"name": name, "details": ...}


def update(name: str, **kwargs):
    # d = {}
    # for i in range(7000):
    #     d[i] = i**i
    print("updating user", name, "with", kwargs)
    return {"name": name, "details": kwargs}


def delete(name: str):
    print("deleting user", name)


def main():
    print("Hello users module!")
    print("Magic const:", USERS_MAGIC_CONST)
    print()
    create("Nick")
    create("John")
    print()
    update("John", email="john@example.com")
    print()
    delete("Nick")


if __name__ == "__main__":
    main()
