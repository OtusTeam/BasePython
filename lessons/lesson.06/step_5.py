class Shape:
    def get_area(self):
        """
        :return:
        """
        print("нет данных для вычисления площади")
        # return 0
        # return None

    @property
    def area(self):
        return self.get_area()


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = self.validate_value(a)
        self.b = self.validate_value(b)

    # @classmethod
    # @staticmethod
    # def validate_value(value):
    @classmethod
    def validate_value(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"value should be int or float, got {type(value)}")
        return value

    def get_area(self):
        return self.a * self.b

    # @property
    # def area(self):
    #     # return 2 * 3
    #     return self.a * self.b

    def __str__(self):
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"


class Square(Rectangle):
    # def __init__(self, a):
    #     super().__init__(a, a)

    def __init__(self, a):
        self.a = self.validate_value(a)

    @property
    def b(self):
        return self.a

    @b.setter
    def b(self, value):
        # if not isinstance(value, (int, float)):
        #     raise TypeError("value should be int or float")
        # self.a = value
        self.a = self.validate_value(value)


shape1 = Shape()
result = shape1.get_area()
# print("result:", None)

rect1 = Rectangle(3, 5)
# print(rect1, "area:", rect1.get_area())

rect2 = Rectangle(7, 12)
# print(rect2, "area:", rect2.get_area())

rect1.a = 7
# print(rect1, "area:", rect1.get_area())

if isinstance(rect1, Shape):
    pass
    # print("obj", rect1, "area", rect1.get_area())


# print("class rect", rect1.__class__)
square1 = Square(5)
# print(square1, "area:", square1.get_area())
# print("class square", square1.__class__)

square1.a = 6
# print(square1, "area:", square1.get_area())


square1.b = 7
# print(square1, "area:", square1.area)


rect1.b = 4
# print(rect1, "area:", rect1.area)

square2 = Square(123)
print(square2, "area:", square2.area)

# square2.b = "321"
square2.b = 321
print(square2, "area:", square2.area)
