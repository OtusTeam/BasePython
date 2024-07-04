from typing import NamedTuple
from collections import namedtuple


PersonCharacteristics = namedtuple(
    "PersonCharacteristics",
    ["age", "height"],
)


class Point(NamedTuple):
    x: int
    y: int

    def add(self, other: "Point") -> "Point":
        return Point(x=self.x + other.x, y=self.y + other.y)


class Person(NamedTuple):
    name: str
    age: int
    email: str


# Person = namedtuple(
#     "Person",
#     "name, age, email",
# )


def get_person() -> Person:
    # return Person("John", 30, "john@example.com")
    return Person("John", age=30, email="john@example.com")


def main():
    print("Hello!")
    print(Person.mro())
    person = get_person()
    print(person)
    print("name:", person.name)
    print("age:", person.age)
    print("email:", person.email)
    # print("email:", person.email + 1)

    print("---")
    name, age, email = person
    # name, *_ = person
    # name, age, *_ = person
    # name = person.name
    # age = person.age
    print("name:", name)
    print("age:", age)
    print("email:", email)
    # person.email = person.email.lower()
    print(person.age)
    print("---")

    point = Point(40, 180)
    print(point)
    p_chars = PersonCharacteristics(age=40, height=180)
    print(p_chars)

    print("point == p_chars:", point == p_chars)
    print("tuple(point) == tuple(p_chars):", tuple(point) == tuple(p_chars))
    print(tuple(point), tuple(p_chars))

    point_2 = Point(20, 40)

    print(point_2)
    print(point.add(point_2))


if __name__ == "__main__":
    main()
