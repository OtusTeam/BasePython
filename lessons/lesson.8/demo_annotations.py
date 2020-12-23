from typing import Optional


def demo_annotations():
    # my_str: str
    # my_str = "foobar"
    my_str: str = "FooBar"
    print(my_str.lower())
    # my_str = {}

    data = {"username": "spameggs"}
    username: Optional[str] = None
    if "username" in data:
        username = data["username"]

    print("username:", username and username.lower())


if __name__ == '__main__':
    demo_annotations()
