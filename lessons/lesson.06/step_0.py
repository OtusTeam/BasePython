class Point:
    # ABC = "QWERTY"

    def __init__(self, x, y):
        # print(self.ABC)
        self.x = x
        self.y = y

    def __str__(self):
        return repr(self)
        # return str([self.x, self.y])

    def __repr__(self):
        cls = type(self)
        # cls == self.__class__
        return f"{cls.__name__}(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.equals(other)

    def equals(self, other):
        # if not isinstance(other, Point):
        if not isinstance(other, self.__class__):
            return False

        return self.x == other.x and self.y == other.y

    # @classmethod
    # def equal_points(cls, point_a, point_b):
    #     return cls.equals(point_a, point_b)

    def add(self, point: "Point"):
        return self.__class__(x=self.x + point.x, y=self.y + point.y)
        # return Point(x=self.x + point.x, y=self.y + point.y)

    def __add__(self, other: "Point") -> "Point":
        return self.add(other)

    def __iadd__(self, other):
        # self += other !!!!!
        self.x += other.x
        self.y += other.y
        # self.x = self.x + other.x
        # self.y = self.y + other.y
        return self


class Point2D(Point):
    pass


p1 = Point(2, 3)
print("p1", p1.x, p1.y)

print("p1:", p1)
print("p1:", repr(p1))

p2 = Point(x=2, y=3)
assert p2.__class__ is Point
print("p2:", repr(p2))


print("p1 == p2", p1 == p2)
p3 = p1

print("p1 == p3", p1 == p3)

p2.x = 4
print("p1:", repr(p1))
print("p2:", repr(p2))
print("p1 == p2", p1 == p2)

print("p1 == p2", p1.__eq__(p2))


p4 = p1.add(p2)
print("p1:", p1)
print("p2:", p2)
print("p4:", p4)

print("p1.__class__", p1.__class__)
print("type(p1)", type(p1))
print("Point", Point)

print("p1.__class__ is type(p1)", p1.__class__ is type(p1))
print("Point(1, 2) == p1.__class__(1, 2)", Point(1, 2) == p1.__class__(1, 2))


p2d_1 = Point2D(4, 5)
p2d_2 = Point2D(7, 9)
assert p2d_2.__class__ is Point2D
assert type(p2d_2) is Point2D


p2d_3 = p2d_1.add(p2d_2)
p2d_4 = p2d_1 + p2d_2

print(p2d_1)
print(p2d_2)
print(p2d_3)
print(p2d_4)

p5 = p1 + p2
print("p1:", p1)
print("p2:", p2)
print("p5:", p5)
print("p4:", p4)


words = ["fall", "winter"]
w2 = words
print(words)
print(w2)
print(id(words))
print("w2 is words", w2 is words)
words += ["foo", "bar"]
print(words)
print(w2)
print(id(words))
print("w2 is words", w2 is words)

print()

p5_2 = p5
print("p5", p5)
print("p5_2", p5_2)
print("id(p5)", id(p5))
print("p5 is p5_2", p5 is p5_2)
p5 += p2
print("p5", p5)
print("p5_2", p5_2)
print("id(p5)", id(p5))
print("p5 is p5_2", p5 is p5_2)
