from inspect import getfullargspec

from dataclasses import dataclass, asdict


# @dataclass(frozen=True)
@dataclass
class Point:
    x: int
    y: int

    def incr_both(self, value: int):
        """
        increase `x` and `y` by value
        :param value:
        :return:
        """
        self.x += value
        self.y += value


def demo_point():
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = Point("foo", "bar")
    print(p1)
    print(p2)
    print(p3)
    print("asdict(p3):", asdict(p3))
    p3.x = p1.x
    p3.y = p1.y
    print(p3)
    print("asdict(p3):", asdict(p3))

    print("p1 == p2", p1 == p2)
    print("p1 == p3", p1 == p3)
    print("p1 is p3", p1 is p3)

    p4 = Point(x=123, y=456)
    print("p4:", p4)
    p4.incr_both(25)
    print(p4)

    print(Point.__init__)
    print(help(Point.__init__))
    print(getfullargspec(Point.__init__))


def main():
    demo_point()


if __name__ == '__main__':
    main()
