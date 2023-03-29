from collections import namedtuple

# Point = namedtuple("Point", "x, y")
Point = namedtuple("Point", ["x", "y"])

# Person = namedtuple("Person", "age, weight, email")
Person = namedtuple("Person", "age, weight")


# class Person:
#     def __init__(self, age, weight):
#         self.age = age
#         self.weight = weight


def get_point():
    """

    :return: x, y
    """
    # return (1, 2)
    return Point(20, 80)


def get_person():
    """

    :return: age, weight
    """
    return Person(20, weight=80)


def main():
    p1 = get_point()
    print(p1)
    person_1 = get_person()
    # person_1 = (10, 30)
    print(person_1)
    print("p.x", p1.x)
    print("p.y", p1.y)

    print("person age", person_1.age)
    print("person weight", person_1.weight)
    print(p1[0])
    print(p1[1])

    print("person [1]", person_1[1])
    age, weight = person_1
    print("age", age, "weight", weight)

    person_2 = Person(person_1.age + 1, person_1.weight - 5)
    print(person_1)
    print(person_2)
    person_3 = Person(*person_1)
    print(person_3)

    print("person_1 == person_2:", person_1 == person_2)
    print("person_1 == person_3:", person_1 == person_3)
    print(p1)
    print("person_1 == p1:", person_1 == p1)
    print(Person.mro())


if __name__ == "__main__":
    main()
