from collections import namedtuple


# def get_person():
#     return "John", 42, 69, "Smith", None
#
#
# def main():
#     p = get_person()
#     print(p)
#     # name, age, weight, email = p
#     name = p[0]
#     age = p[1]
#     weight = p[2]
#     print("name:", name)
#     print("weight:", weight)
#     print("age:", age)

Person = namedtuple("Person", "age, weight")
Point = namedtuple("Point", "x, y")


def get_person():
    return Person(age=42, weight=69)


def main():
    person = get_person()
    print(person)
    # print("name:", person.name)
    print("age:", person.age)
    print("weight:", person.weight)

    print(Person.mro())
    print(person.age + 1)
#     print(person.name + 1)

    point = Point(person.age, person.weight)
    print(point)
    print("x:", point.x)
    print("y:", point.y)

    assert point == person


if __name__ == '__main__':
    main()
