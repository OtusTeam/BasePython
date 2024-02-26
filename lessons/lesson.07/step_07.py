class Polygon:
    @property
    def area(self):
        return

    @property
    def perimeter(self):
        return


class Rectangle(Polygon):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)


class Square(Rectangle):
    def __init__(self, a):
        self.a = a

    @property
    def b(self):
        return self.a

    @b.setter
    def b(self, value):
        self.a = value


rectangle = Rectangle(2, 3)
print(rectangle.area)
rectangle.a = 4
print(rectangle.area)
rectangle.b = 5
print(rectangle.area)
print(rectangle.perimeter)

print("my room")
my_room = Rectangle(4, 3)
print(my_room.area)
print(my_room.perimeter)

square = Square(3)
print(square.area)
square.b = 5
print(square.area)
print(square.perimeter)
