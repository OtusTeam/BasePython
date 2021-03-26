class Quadrilateral:
    def __init__(self, length, height, **kwargs):
        super().__init__(**kwargs)
        self.length = length
        self.height = height

    def area(self):
        print("generic area call")
        return self.length * self.height


class Rectangle(Quadrilateral):
    def __init__(self, length, height, **kwargs):
        super().__init__(length, height, **kwargs)


class Square(Rectangle):  # inherits from quadri
    def __init__(self, side, **kwargs):
        super().__init__(side, side, **kwargs)  # create Quadrilateral
        self.side = side

    def area(self):
        return super().area()  # the Quadrilateral method


class xxx():
    def __init__(self, dim1, dim2, dim3, **kwargs):
        self.dim1 = dim1
        self.dim2 = dim2
        self.dim3 = dim3
        super().__init__(**kwargs)

    def volume(self):
        # print("dim1=",self.dim1)
        rez = self.dim1 * self.dim2 * self.dim3
        print("rezult is ", rez)
        return rez


class Cube(Square, xxx):
    def __init__(self, base, c_height, **kwargs):
        self.base = base
        self.c_height = c_height
        kwargs["dim1"] = base
        kwargs["dim2"] = base
        kwargs["dim3"] = c_height
        # kwargs["lenght"] = base
        # kwargs["height"] = base
        super().__init__(base, **kwargs)  # square method

    def one_side_area(self):
        return super().area()

    def volume(self):
        return super().volume()


class Triangle():
    def __init__(self, base_tri, height_tri, **kwargs):
        self.base_tri = base_tri
        self.height_tri = height_tri
        super().__init__(**kwargs)

    def TriArea(self):
        print("area trinagle method")
        return 0.5 * (self.height_tri * self.base_tri)


class RightPhyramid(Square, Triangle):
    def __init__(self, base, height, sides=4, **kwargs):
        self.base = base
        self.height = height
        self.sides = sides
        kwargs["base_tri"] = base
        kwargs["height_tri"] = height
        super().__init__(base, **kwargs)  # square

    def area(self):
        base_area = super().area()
        sides_area = self.sides * super().TriArea()
        return base_area + sides_area


# sq0 = Square(5)
# sq0.area()
# c1 = Cube(5,10)
# print(c1.one_side_area())
# print(c1.volume())
# tri = Triangle(10, 15)
# print(tri.area())
Rp0 = RightPhyramid(10, 15)
print(Rp0.area())
print(Rp0.__dict__)
