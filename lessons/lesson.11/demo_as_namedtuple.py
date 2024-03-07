from collections import namedtuple

Person = namedtuple("Person", "name, age, rating, email")


Point = namedtuple("Point", "x, y")
PersonCharacteristics = namedtuple("PersonCharacteristics", "height, weight")


def get_person_as_tuple():
    name = "John Smith"
    age = 42
    rating = 7
    email = None
    return name, age, rating, email


def get_person_as_namedtuple():
    name = "John Smith"
    age = 42
    rating = 7
    email = None
    return Person(name, age, rating, email)


def example():
    p1 = Point(y=10, x=20)
    print(p1)
    p2 = Point(20, y=10)
    print(p2)
    print("p1 == p2:", p1 == p2)
    # p1.x = 123
    x, y = p1
    print(f"{x=} {y=}")
    x = 150
    y = 40
    p3 = Point(x, y)
    print(p3)

    p_chars = PersonCharacteristics(height=150, weight=40)
    print(p_chars)

    print("p_chars == p3:", p_chars == p3)
    print(type(p3))
    print(type(p3).mro())
    print(type(p_chars))
    print(type(p_chars).mro())


def main():
    person = get_person_as_tuple()
    print(person)
    print("name:", person[0])
    print("age:", person[1])
    print("email:", person[2])

    p2 = get_person_as_namedtuple()
    print(p2)
    print(type(p2))
    print(type(p2).mro())
    print("name:", p2.name)
    print("age:", p2.age)
    print("email:", p2.email)

    print()
    example()


if __name__ == "__main__":
    main()
