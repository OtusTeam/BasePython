class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other: Point) -> Point:
        # if not isinstance(other, Point):
        #     raise TypeError
        return Point(
            self.x + other.x,
            self.y + other.y,
        )

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    # def __str__(self):
    #     return f"{self.__class__.__name__}(x={self.x}, y={self.y})"
    #
    # def __repr__(self):
    #     return str(self)


p1 = Point(10, 20)
p2 = Point(3, 5)
p3 = Point(p1.x + p2.x, p1.y + p2.y)
p4 = p1 + p2

print("p1:", p1)
print("p1:", str(p1))
print("p2:", p2)
print("p3:", p3)
print("p4:", p4)

points = [p1, p2, p4]
print("points:", points)

name = "Bob"
print(str(name))
print(repr(name))
