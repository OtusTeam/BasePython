class Shape:

    def get_area(self):
        print("not enough data")


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = self.prepare_value(a)
        self.b = self.prepare_value(b)
        # print("initialized r with p", self.get_p())

    @classmethod
    def prepare_value(cls, value):
        # cls(value, value)
        # cls.
        # print(cls)
        if value > 0:
            return value
        # return -value
        return value * -1

    def get_area(self):
        return self.a * self.b

    def get_p(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        # return "abc"
        # return "abc" + "foobar"
        # return "abc" + str(1) + "qwerty"
        # return f"abc{1}qwerty{sum(1,2,3)}"
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"

    def __len__(self):
        return self.get_p()


class Square(Rectangle):
    def __init__(self, a):
        # super().__init__(a, a)
        # Rectangle.__init__(self, a, a)
        self.a = self.prepare_value(a)
        # self.b = a

    @property
    def b(self):
        return self.a

    @b.setter
    def b(self, value):
        self.a = self.prepare_value(value)

    # def __getattribute__(self, item):
    #     if item == "get_p"..
    # def get_p(self):
    #     pass
    #     # return None
    #     raise Exception

# print(Square.b)
# print(Square.b())
# print(Square.__init__)

# var1 = None
# var_ = None
# var_name = None
# var_1_name = None
# _var = None
# _var_ = None
# __var = None
# __var__ = None

rectangle1 = Rectangle(3, 5)

print(rectangle1)
# print(rectangle1.__str__())
# print(str(rectangle1))
print("p:", len(rectangle1))
print("p:", rectangle1.__len__())
print("p:", rectangle1.get_p())
print(rectangle1.get_area())


# s1 = Square(5, 5)
s1 = Square(6)
print(s1)
print("P", s1.get_p())
print("Sq", s1.get_area())

s1.a = 7
s1.a
# s1.get_area

print(s1)
print(s1.a, s1.b)
print("P", s1.get_p())
print("Sq", s1.get_area())

s1.b = 8
print(s1)
print(s1.a, s1.b)
print("P", s1.get_p())
print("Sq", s1.get_area())


s1.b = -10
print(s1)
print("P", s1.get_p())
print("Sq", s1.get_area())

print(Rectangle.prepare_value(-10))
print(Rectangle.prepare_value(11))
