class Point:
    IS_2D = True
    all_instances = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = None
        self.all_instances.append(self)

    def __str__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def __repr__(self):
        return str(self)

    def move_up(self):
        self.y += 1

    # @classmethod
    # def copy(cls, from_point):
    #     return cls(from_point.x, from_point.y)

    def copy_me(self):
        # return self.copy(self)
        return self.__class__(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z


class AnotherPoint(Point):
    all_instances = []



print(Point.all_instances)
p = Point(4, 5)
print("point z", p.z)

# Point.__init__(p, 6, 7)
print(p, "is 2d?", p.IS_2D)
print("Point is 2D?", Point.IS_2D)
print("move up")
print(p.move_up(), p)
print(Point.move_up(p), p)

p2 = p
print(p, p2)
p.x += 1
p2.y -= 1
print(p, p2, p is p2)

# p3 = Point.copy(p)
p3 = p.copy_me()
print(p3, p2, p3 is p2, p3 is p)
print("p3 == p", p3 == p)
print("p3 == (5, 6)", p3 == (5, 6))

p3.move_up()
p.x += 3
p4 = p3 + p
print(p3, p)
print(p4)


print()
print()


print(Point.all_instances)
Point(1, 2)

print(Point.all_instances)
print("another", AnotherPoint.all_instances)

print()
print()
print()
print("types")
print(type(p))
print(type(Point))
print(Point.__mro__)

print(type(type))

def my_func():
    pass

print(type(my_func))
print(type(Point.__init__))
print(type(lambda x: x))

f_type = type(my_func)
print(f_type)
# p.x = 2
# p.y = 1
print(p)
# p2 = Point()
# print(p2, p2.x, p2.y)

print(isinstance(type, object))
print(isinstance(1, object))
print(isinstance(isinstance, object))
print(isinstance(print, object))
