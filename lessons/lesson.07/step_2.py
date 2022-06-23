class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str([self.x, self.y])

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def add(self, p):
        # p = Point(x=1, y=2)
        # return p
        return self.__class__(x=self.x + p.x, y=self.y + p.y)

    def __add__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


def add_points(point_1, point_2):
    print("point_1", point_1, point_1.x, point_1.y)
    print("point_2", point_2, point_2.x, point_2.y)


p1 = Point(2, 3)
p2 = Point(5, 7)
p3 = Point(1, 9)

print(p1)
print(p2)
print([p1, p2, p3])

p4 = p1 + p2
print(p4)

# p5 = p4 + p3
p5 = p4.add(p3)
print([p4, p3, p5])

p6 = p1 + p2 + p3
print([p1, p2, p3, p6])

p7 = p1.add(p2).add(p3)
print([p1, p2, p3, p7])

add_points(p4, p5)
add_points(p6, p7)

print([p1, p2, p3])

print(p3, id(p3))
p3.x = p1.x + p2.x
p3.y = p1.y + p2.y
print(p3, id(p3))

p3.x = p3.x + p2.x
p3.y = p3.y + p2.y
print(p3, id(p3))

p3 += p2
print(p3, id(p3))

p4 = p3 + p2
print(p4)

ZERO_POINT = Point(10, 10)


def new_point(a, b):
    p = ZERO_POINT + Point(a, b)
    return p


p5 = new_point(1, 2)
print([p5])
ZERO_POINT.x = 20
p6 = new_point(1, 2)
print([p6])
