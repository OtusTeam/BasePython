from __future__ import annotations

from dataclasses import dataclass, field, asdict


# @dataclass(frozen=True)
# @dataclass(slots=True)
@dataclass()
class Point:
    x: int
    y: int
    # z: int = 1


@dataclass
class Person:
    name: str
    age: int
    email: str | None = None
    # father: Person | None = None
    friends: list[Person] = field(default_factory=list)

    def increase_age(self):
        self.age += 1

    # def __str__(self):
    #     return f"p {self.name}"


@dataclass
class Grocery:
    weight: int
    price: int


def get_point():
    return Point(7, y=10)


def get_person():
    return Person("John", 42)


def main():
    point = get_point()
    print(point)
    point.x = 42
    print(point)
    point.z = 3
    print(point.z)
    print("abc")
    print(["abc"])
    print(point)
    print([point])

    person = get_person()
    print(person)

    bread = Grocery(500, 50)
    point_1 = Point(500, 50)
    print(bread)
    print(point_1)
    print("bread == point_1:", bread == point_1)

    person_2 = Person(
        "Sam",
        "twenty two",
    )
    print(person_2)
    print(person.age)
    person.increase_age()
    print(person.age)
    # person_2.increase_age()
    print(person.age + 10)
    # print(person_2.age + 10)
    # print(person_2.name + 10)
    person.friends.append(person_2)
    print(person)
    print(asdict(person))


if __name__ == "__main__":
    main()
