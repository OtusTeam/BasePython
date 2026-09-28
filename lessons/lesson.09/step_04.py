import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @property
    @abstractmethod
    def area(self):
        raise NotImplementedError


# class Shape:
#
#     def area(self):
#         raise NotImplementedError


#
#
# shape = Shape()


class Circle(Shape):

    def __init__(self, r) -> None:
        self.r = r

    @property
    def area(self):
        return math.pi * self.r**2


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b


class RightTriangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return (self.a * self.b) / 2


# Плохо! Нарушение open-closed principle.
# def total_area(shapes: list[Shape]):
#     total = 0
#     for shape in shapes:
#         if isinstance(shape, Circle):
#             total += math.pi * shape.r**2
#         elif isinstance(shape, Rectangle):
#             total += shape.a * shape.b
#         elif isinstance(shape, RightTriangle):
#             total += (shape.a * shape.b) / 2
#         else:
#             raise ...
#     return total


def total_area(shapes: list[Shape]):
    return sum(s.area for s in shapes)


circle = Circle(8)
rect = Rectangle(5, 10)
triangle = RightTriangle(6, 7)
my_shapes = [circle, rect, triangle]
result = total_area(my_shapes)
print(result)
print([s.area for s in my_shapes])
