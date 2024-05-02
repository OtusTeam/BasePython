USERS_MAGIC_VARIABLE = 42

print("users module, name:", repr(__name__))


def create(name):
    print("creating user", name)
    return {"name": name, "details": ...}


def update(name, **kwargs):
    print("updating user", name, "with", kwargs)
    return {"name": name, "details": kwargs}


def delete(name):
    print("deleting user", name)


def run_demo_users():
    print("hello users!")
    print("magic variable:", USERS_MAGIC_VARIABLE)
    print()
    create("Nick")
    create("Alex")

    update("Nick", email="nick@example.com")

    delete("Alex")
    print()


if __name__ == "__main__":
    run_demo_users()
