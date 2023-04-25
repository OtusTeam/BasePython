class Shape:

    def get_area(self):
        print("not enough data")
        # return None


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # overload - (перегрузка) не бывает в Python
    # def method(self, a):
    #     return a ** 2
    #
    # def method(self, a, b):
    #     return a ** b
    #
    # def method(self, a, b, c):
    #     return a * b * c

    # override - переопределение
    def get_area(self):
        return self.a * self.b

    def __str__(self):
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"


class Square(Rectangle):
    def __init__(self, a):
        self.a = a
        # self.b = a

    @property
    def b(self):
        return self.a

    @b.setter
    def b(self, value):
        # self.a = int(value)
        self.a = value

    def __str__(self):
        return f"{self.__class__.__name__}(a={self.a})"


shape = Shape()
print(shape)
shape.get_area()

rectangle_1 = Rectangle(2, 6)
print(rectangle_1)
rectangle_2 = Rectangle(3, 5)
print(rectangle_2)

print("r1 area:", rectangle_1.get_area())
print("r2 area:", rectangle_2.get_area())

sq1 = Square(6)
print(sq1)
print(sq1.a)
print(sq1.b)
print("sq1 square", sq1.get_area())

sq1.b = 7
print(sq1)
print(sq1.get_area())

sq1.a = 9
print(sq1)
print(sq1.get_area())
