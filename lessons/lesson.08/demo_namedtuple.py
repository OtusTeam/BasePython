from collections import namedtuple

# Point = namedtuple("Point", "x, y")
Point = namedtuple("Point", ["x", "y", "z"])


# Person = namedtuple("Person", ["age", "weight", "fat"])


class Person(namedtuple("Person", ["age", "weight", "fat"])):
    def __eq__(self, other):
        print(super())
        print(super().__eq__)
        # return super().__eq__(other)
        return type(self) is type(other) and super().__eq__(other)

    def get_fullname(self):
        return str(self)


# class NewPerson(Person):
#     def get_fullname(self):
#         return "new" + super().get_fullname()

def get_point():
    x = 1
    y = 2
    z = 3
    return Point(x, y, z)


def get_person():
    b = 21
    c = 80
    d = 50
    p = Person(age=b, weight=c, fat=d)
    return p


def main():
    point1 = get_point()
    print(point1)
    print(point1[0])
    print(point1[1])
    # x, y = point1
    # print(x)
    # print(y)
    print(point1.x)
    print(point1.y)
    print(point1.z)
    point2 = get_point()
    print(point1)
    print(point2)
    print("p1 == p2:", point1 == point2)
    print(Point.mro())
    print(point1._asdict())
    print(point1._fields)
    p3_values = point1._asdict()
    p3_values["z"] = 4
    point3 = Point(**p3_values)
    print(point3)
    print("point1 == point3", point1 == point3)

    person = get_person()
    person2 = get_person()
    print(person)
    point = Point(21, 80, 50)
    print(point)
    print(type(point))
    print(type(person))
    print("person == point ? :", person == point)
    print("person == person2 ? :", person == person2)
    print((1, 2, 3) == (1, 2, 3) == (1, 2, 3))


if __name__ == '__main__':
    main()
