class InvalidOperandError(ValueError):
    pass


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
        if not isinstance(p, self.__class__):
            raise InvalidOperandError(f"Should be Point, got {type(p)}")
        return self.__class__(x=self.x + p.x, y=self.y + p.y)

    def __add__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


p1 = Point(1, 2)
p2 = Point(3, 4)
print([p1, p2])
p3 = p1 + p2
print([p3])
p4 = p3.add(p2)
print([p4])

p1 + 3


