from dataclasses import (
    dataclass,
    field,
    asdict,
    astuple,
)


@dataclass
class Point:
    x: int
    y: int


@dataclass(frozen=True, slots=True)
class Person:
    # __slots__ = ("name", "age", "email")
    name: str
    age: int
    email: str | None = None

    # def __init__(self, name: str, age: int, email: str | None = None):
    #     self.name = name
    #     self.age = age
    #     self.email = email
    #
    # def __str__(self):
    #     return f"{self.__class__.__name__}(name={self.name!r}, age={self.age})"
    #
    # def __repr__(self):
    #     return str(self)
    #
    # def __eq__(self, other):
    #     if not isinstance(other, self.__class__):
    #         return False
    #     return self.name == other.name and self.age == other.age and self.email == other.email

    def increase_age(self):
        self.age += 1


def create_default_tags_list():
    return ["sale"]


@dataclass(frozen=True)
class Grocery:
    name: str
    weight: int
    tags: list[str] = field(default_factory=create_default_tags_list)


def get_person():
    return Person("John", age=42, email="john@example.com")


def main():
    p1 = get_person()
    print("p1:", p1)
    p2 = get_person()
    print("p2:", p2)

    print("p1 is p2", p1 is p2)
    print("p1 == p2", p1 == p2)
    # p2.increase_age()
    print("p2:", p2)
    print("p1 == p2", p1 == p2)

    # p1.abc = "qwe"
    # print(p1.__slots__)
    # print(p1.__dict__)
    print(Person.mro())
    print(dir(Person))

    p1 = Point(1, 2)
    p2 = Point(1, 3)
    print("p1:", p1)
    print("p2:", p2)

    p3 = Point(x="abc", y="foobar")
    print(p3)

    bread = Grocery(name="Bread", weight=200)
    milk = Grocery(name="Milk", weight=930)
    choco = Grocery(name="Choco", weight=100, tags=["sugar"])
    print(bread)
    print(milk)
    print(choco)
    bread.tags.append("wheat")
    milk.tags.append("whole")
    print(bread)
    print(milk)

    print(choco)
    print(astuple(choco))
    print(asdict(choco))


if __name__ == "__main__":
    main()
