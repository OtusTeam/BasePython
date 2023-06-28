from collections import namedtuple

# Point = namedtuple("Point", ["x", "y"])
# Point = namedtuple("Point", "x, y")
Point = namedtuple("Point", "x, y")

Person = namedtuple("Person", "age, weight")
NewPerson = namedtuple("NewPerson", "name, age")

print(NewPerson)

# class NewPoint(Point):
#     def add(self):
# class NewPoint(namedtuple("Point", "x, y")):
#     pass


def get_point():
    # x, y
    # тюпл (от tuple)
    # он же кортеж
    # return (42, 50)
    return Point(42, 50)


def get_person():
    return Person(age=42, weight=50)


def get_new_person():
    return NewPerson(name="John", age=42)


def main():
    p1 = get_point()
    print(p1)
    print("p1.x:", p1.x)
    print("p1.y:", p1.y)

    person = get_person()
    print(person)
    print("age", person.age)
    print("weight", person.weight)

    print("p1 == person:", p1 == person)
    print(p1 == (42, 50))
    print(person == (42, 50))

    new_person = get_new_person()
    print(new_person)
    print("person == new_person", person == new_person)
    print("eq tuple", new_person == ("John", 42))
    # (42, 50) == (42, 50)

    # p2 = get_point()
    # print(p1)
    # print(p2)
    # print(p1 == p2)
    # # x, y = p1
    # # print("x:", x)
    # # print("y:", y)
    #
    # x = p1.x
    # print("x:", x)
    # print("p1.x:", p1.x)
    # print("p1.y:", p1.y)
    #
    # p3 = Point(x=10, y=20)
    # print(p3)
    print(Point.mro())
    print(isinstance(p1, tuple))
    print(Person.mro())
    print(isinstance(person, tuple))


if __name__ == "__main__":
    main()
