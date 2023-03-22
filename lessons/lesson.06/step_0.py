class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # return f"x={self.x}, y={self.y}"
        return repr(self)

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        # instance = экземпляр
        if not isinstance(other, self.__class__):
            return False

        return self.x == other.x and self.y == other.y

    def add(self, point):
        return self.__class__(x=self.x + point.x, y=self.y + point.y)

    def __add__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        """
        in-place add
        :param other:
        :return:
        """
        # return self.add(other)

        # self.x = self.x + other.x
        self.x += other.x
        self.y += other.y

        return self


# double underscore
# underscore = "_"
# double underscore -> d_under
# double underscore -> dunder

if __name__ == "__main__":

    print(Point.mro())

    p1 = Point(1, 2)
    p2 = Point(3, y=4)
    p3 = Point(x=5, y=6)
    p3_swap = Point(x=6, y=5)
    p4 = Point(y=8, x=7)
    p5 = Point(y=2, x=1)


    print("p1", p1)
    print("p2", p2)
    p7 = p1.add(p2)
    print("p7", p7)
    p7 = p2.add(p1)
    print("p7", p7)
    # print(2 + "2")
    p8 = p1 + p2
    print("p8", p7)
    print("p7 == p8", p7 == p8)
    print("p7 is p8", p7 is p8)

    print("p1 == p2?", p1 == p2)
    print("p3 == p3_swap?", p3, p3_swap, p3 == p3_swap)
    print("p1 == p5?",  p1, p5, p1 == p5)
    print("p1 is p5?",  p1, p5, p1 is p5)

    p6 = p5
    print("p6 == p5?",  p6, p5, p6 == p5)
    print("p6 is p5?",  p6, p5, p6 is p5)

    print(id(p5))
    print(id(p6))
    p5 += p1

    print("after iadd")
    print(id(p5))
    print(id(p6))

    print("p6 == p5?",  p6, p5, p6 == p5)
    print("p6 is p5?",  p6, p5, p6 is p5)

    s = str
    assert s is str

    p5.y = 20
    p6.y *= 2
    p6.x = 10
    print("p6", p6)
    print("p5", p5)


    a = 42
    b = "012"
    c = str(b)
    d = str(a)
    print(a)
    print(b)
    print(c)
    print(d)
    print(d + b)

    p1_str = str(p1)
    print(p1_str)
    print(p1)
    print(p2)
    print(p3)
    print(p4)

    items = [a, b, c, d]
    print(str(c))
    print(repr(c))
    print(items)
    print(repr(items))
    print(str(items))
    assert str(p1) == p1.__str__()

    print(repr(p1))

    print([p1, p2, p3])
    print({"abc": p1})


    a = [1, 2]
    b = [3, 4]
    d = a

    c = a + b
    print(a)
    print(d)
    print(b)
    print(c)

    a += b
    print(a)
    print(d)
    print("a is d", a is d)
    print(id(a))
    print(id(d))

