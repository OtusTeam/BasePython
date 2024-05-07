import collections
from collections import namedtuple
from typing import NamedTuple

Person = namedtuple("Person", "name, age, level, email")
PersonCharacteristics = namedtuple(
    "PersonCharacteristics", "age, height"
)


class Point(NamedTuple):
    x: int
    y: int


def get_point():
    return Point(x=3, y=5)


def get_person():
    return Person("John", 42, 3, "john@example.com")


def get_person_characteristics():
    return PersonCharacteristics(age=42, height=180)


def main():
    person = get_person()
    print(person)
    # name, age, email = person
    # print("name:", name)
    # print("age:", age)
    # print("email:", email)

    print("name:", person.name)
    print("age:", person.age)
    print("email:", person.email)
    print("level:", person.level)
    # person.age += 1

    point = get_point()
    print(point)
    print(Point(x="three", y="5"))
    print("x:", point.x)

    p_char = get_person_characteristics()
    print(p_char)

    point_a = Point(x=42, y=180)

    print(point_a)

    print("p_char == point_a", p_char == point_a)


if __name__ == "__main__":
    main()

    print(help(collections))
    print(dir(collections))
