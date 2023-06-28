# from demo_named_tuple import Point

def create_class():
    class User:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return self.name

    return User


def main():
    cls = create_class()
    user = cls(name="John")
    print(cls)
    print(user.name)
    print(user)


if __name__ == "__main__":
    main()
