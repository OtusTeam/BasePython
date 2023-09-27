from collections import namedtuple


# def get_person():
#     return "John", 42, "Smith", "john@example.com"

# def main():
#     person = get_person()
#     print(person)
#     name = person[0]
#     age = person[1]
#     email = person[3]
#     # name, age = person
#     # name, age, lastname = person
#     # name, age, lastname, email = person
#     print("name:", name)
#     print("age:", age)
#     print("email:", email)
#
#     print("name:", person[0])
#     print("age:", person[1])
#     print("email:", person[3])


# def get_person():
#     # age, weight
#     return 70, 75


Person = namedtuple("Person", "age, weight")
Point = namedtuple("Point", "x, y")


def get_person():
    # person = Person(40, 50)
    # person = Person(40, weight=50)
    person = Person(age=40, weight=50)
    return person


def get_point():
    return Point(7, 10)


def main():
    person = get_person()
    print(person)
    age = person[0]
    weight = person[1]

    print("age:", person.age)
    print("weight:", person.weight)

    print("age:", age)
    print("weight:", weight)

    age, weight = person

    print("age:", age)
    print("weight:", weight)

    # person.age = 44
    print(person.__class__.mro())
    # person_2 = Person(*person)

    point = get_point()
    print("point:", point)
    print("p.x", point.x)
    print("p.y", point.y)

    point_1 = Point(40, 50)
    print(person)
    print(point_1)
    print("person == point_1:", person == point_1)
    print(tuple(person) == tuple(point_1))
    print(tuple(person))
    print(tuple(point_1))
    # person.age == point_1.x


if __name__ == "__main__":
    main()
