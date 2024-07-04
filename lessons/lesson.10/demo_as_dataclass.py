from typing import TypeGuard, Any, Self

from dataclasses import dataclass, field


# @dataclass(frozen=True)
# @dataclass(slots=True)
@dataclass
class Point:
    x: int
    y: int

    @classmethod
    def validate_other(cls, other: Any) -> TypeGuard["Point"]:
        if not isinstance(other, Point):
            raise TypeError(f"Cannot add {type(other)} to {cls}")
        return True

    def __add__(self, other: "Point") -> "Point":
        self.validate_other(other)
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: "Point") -> Self:
        self.validate_other(other)
        self.x += other.x
        self.y += other.y
        return self

    def copy(self) -> "Point":
        return Point(self.x, self.y)


@dataclass
class Person:
    name: str
    age: int
    email: str

    def increase_age(self):
        self.age += 1


def default_food_tags():
    return ["sale"]


@dataclass
class Food:
    name: str
    tags: list[str] = field(default_factory=default_food_tags)


def get_person() -> Person:
    return Person(
        "John",
        age=25,
        email="john@example.com",
    )


def main():
    print(Point.mro())
    person = get_person()
    print(person)
    print("name:", person.name)
    print("age:", person.age)
    print("email:", person.email)

    person.increase_age()
    print("age:", person.age)

    print("---")
    p1 = Point(1, 2)
    p1_2 = p1
    p1_copy = p1.copy()
    print("p1_copy == p1:", p1_copy == p1)
    print("p1_copy is p1:", p1_copy is p1)

    p1.x += 1
    print("p1:", p1)
    p2 = Point(3, 4)
    print(p2)
    p3 = p1 + p2
    print(p3)
    p1 += p3
    print(p1)
    print("p1_2:", p1_2)
    print("p1_2 is p1:", p1_2 is p1)
    print("p1_copy:", p1_copy)
    print("p1_copy is p1:", p1_copy is p1)

    p = Point("one", "qwerty")
    print(p)
    # print(p.x + 1)
    # print(p.__slots__)
    print(p.__dict__)
    p.z = 42
    print(p.z)
    print(p.__dict__)

    print("---")
    bread = Food("Bread")
    print(bread)
    milk = Food("Milk", tags=["milk"])
    print(milk)
    bread.tags.append("sale")
    print(milk)
    print(bread)


if __name__ == "__main__":
    main()
