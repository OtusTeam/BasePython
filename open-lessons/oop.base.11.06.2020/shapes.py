class BaseShape:
    def area(self):
        raise NotImplementedError


class Rectangle(BaseShape):
    def __init__(self, length: int, width: int, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self) -> int:
        return self.length * self.width

    def perimeter(self) -> int:
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length: int, **kwargs):
        super().__init__(length, length, **kwargs)


class Triangle(BaseShape):
    def __init__(self, base: int, height: int, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self) -> float:
        return 0.5 * self.base * self.height


class RightPyramid(Square, Triangle):
    def __init__(self, base: int, slant_height: int):
        super().__init__(base=base, height=slant_height, length=base)
        self.base = base
        self.slant_height = slant_height

    def pyramid_area(self):
        base_area = self.area()
        side_area = self.tri_area()
        return side_area * 4 + base_area


if __name__ == '__main__':
    rectangle = Rectangle(2, 4)
    print("Rectangle:", rectangle.length, rectangle.width)
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())

    square = Square(5)
    print("Square:", square.length)
    print("Area:", square.area())
    print("Perimeter:", square.perimeter())

    triangle = Triangle(4, 6)
    print("triangle area:", triangle.tri_area())

    pyramid = RightPyramid(10, 12)
    print(RightPyramid.__mro__)
    print("pyramid area", pyramid.pyramid_area())
