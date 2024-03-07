# from __future__ import annotations

# from typing import Union, Optional
from dataclasses import dataclass, field, asdict


# @dataclass(slots=True)
@dataclass()
class Person:
    name: str
    age: int
    email: str | None = None
    # email: Union[str, None]
    # email: Optional[str]

    def increase_age(self):
        self.age += 1


def create_new_empty_list():
    return []


def create_default_food_tags_list():
    # return ["sale"]
    tags_list = create_new_empty_list()
    tags_list.append("sale")
    return tags_list


# def power(x, y):
#     return x**y
#
# map(power, [1, 2, 3], [3, 4, 5])
# map(lambda x, y: x**y, [1, 2, 3], [3, 4, 5])
# map(pow, [1, 2, 3], [3, 4, 5])

@dataclass(frozen=True)
class Food:
    name: str
    weight: int = field(default=100)
    # tags: list[str] = []
    # tags: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=create_default_food_tags_list)


class MyPerson:
    def __init__(self, name: str, age: int, email: str | None = None):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return (f"{self.__class__.__name__}("
                f"name={self.name!r},"
                f" age={self.age}, "
                f"email={self.email!r})")

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return False


def get_person() -> Person:
    p = Person("John Smith", age=42)
    return p


def main():
    p = get_person()
    p2 = Person("Sam Black", age="abc", email="sam@example.com")
    print(p)
    print(type(p))
    print(type(p).mro())
    print([p, p2])
    p3 = MyPerson("Kate White", 42, email="kate@example.com")
    p4 = MyPerson("Kyle Gray", 22, email="kyle@example.com")
    # p3.name.
    print(p3)
    print([p3, p4])

    milk = Food(name="Milk", weight=1000)
    print(milk)
    bread = Food(name="Bread", weight=500, tags=["wheat"])
    print(bread)
    # milk.weight = 900
    # print(milk)

    print(p2)
    # p2.is_superuser = True
    # print(p2)
    # print(p2.is_superuser)
    # print(p.is_superuser)
    # print(p.__slots__)
    print(p.__dict__)
    print(p)
    print(p.age)
    p.increase_age()
    print(p.age)
    print()
    print(asdict(p))
    print(asdict(p2))


if __name__ == "__main__":
    main()
