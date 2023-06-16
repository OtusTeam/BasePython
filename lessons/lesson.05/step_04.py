class Shape:
    def get_area(self):
        print("Not implemented")


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        # return "rect: " + str([self.a, self.b])
        return repr(self)

    def __repr__(self):
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"

    def get_area(self):
        return self.a * self.b


class Square(Rectangle):

    def __init__(self, a):
        # super().__init__(a, a)
        self.a = a

    @property
    def b(self):
        return self.a

    @b.setter
    def b(self, value):
        self.a = value

    def __repr__(self):
        return f"{self.__class__.__name__}(a={self.a})"

    # def get_area(self):
    #     return self.a * self.a


print(Rectangle.mro())

rect_1 = Rectangle(2, 3)
print(rect_1)
print(rect_1.a)
print(rect_1.b)

rect_2 = Rectangle(5, 6)
print(rect_2)

print(repr(rect_1))
print(repr(rect_2))

print([1, "1"])
print(1)
print("1")
print(repr("1"))
print([rect_1, rect_2])

print(rect_1, "area", rect_1.get_area())
rect_1.a = 7
print(rect_1, "area", rect_1.get_area())
print(rect_2, "area", rect_2.get_area())


sq1 = Square(5)
print(sq1)
print(sq1, "area", sq1.get_area())
sq1.a = 6
print(sq1, "area", sq1.get_area())
sq1.b = 7
print(sq1, "area", sq1.get_area())


# print(str(sq1))
# str(sq1) == sq1.__str__()

