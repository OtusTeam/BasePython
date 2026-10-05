from typing import Self

# file = open("pyproject.toml", "r")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print()
# file.close()

with open("pyproject.toml", "r") as file:
    print(file.readline(), end="")
    print(file.readline(), end="")
    print(file.readline(), end="")
print()


class Session:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__is_open = False

    def write(self, value):
        if not self.is_open:
            raise ValueError("Should be open")
        print("write", value)

    @property
    def is_open(self) -> bool:
        return self.__is_open

    def __enter__(self) -> Self:
        self.__is_open = True
        print("[debug]: open", self.name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__is_open = False
        print("[debug]: close", self.name)
        if isinstance(exc_val, ZeroDivisionError):
            return True

        return False


# session = Session("foobar")
#
# with session:
#     session.write("hi")


print("before ctx")
with Session("foobar") as session:
    print("in ctx")
    session.write("hi")
    # 1 / 0
    # 1 + ""
    session.write("bye")
print("after ctx")
