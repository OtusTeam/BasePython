from auth_storage import AuthStorage

# import importlib

# hello_world = importlib.import_module("hello-world")
# print(hello_world)
# print(hello_world.HELLO_WORLD)
#
# one_two_three = importlib.import_module("123")
# print(one_two_three)
# print(one_two_three.NUMBERS)


def main():
    auth_storage = AuthStorage()
    auth_storage.register_user("bob", "qwerty")
    kyle = auth_storage.register_user("kyle", "foobar")
    # auth_storage.register_user("bob", "qwerty")
    print(auth_storage)
    user_bob = auth_storage.login_user("bob", "qwerty")
    # print(user_bob)
    # user_bob = auth_storage.login_user("bob", "qwerty123")
    # post = user_bob.add_post("foo", "foo-bar")
    # post.add_user(kyle)


if __name__ == "__main__":
    main()
