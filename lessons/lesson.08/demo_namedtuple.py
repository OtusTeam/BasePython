from collections import namedtuple


# Point = namedtuple("Point", ["x", "y"])
# Point = namedtuple("Point", "x, y")
# print(Point)

class Point(namedtuple("Point", "x, y")):
    def add(self, other: "Point"):
        return Point(self.x + other.x, self.y + other.y)


FriendPair = namedtuple("FriendPair", ["user_id", "friend_id"])


def demo_point_values():
    x = 1
    y = 2
    return x, y


def demo_point_nt() -> Point:
    p = Point(3, 4)
    return p


def main():
    point1 = demo_point_values()
    point2 = demo_point_nt()
    print(point1)
    print(point2)
    x, y = point2
    print(x, y)
    x = point2.x
    y = point2.y
    print(x, y)
    print(point2[0], point2[1])
    print(point2._asdict())
    point3 = Point(1, 2)
    point4 = point2.add(point3)
    print(point4)
    # point3.x = 3

    friend_pair = FriendPair(4, 6)
    print(friend_pair)

    print("point4 == friend_pair", point4 == friend_pair)
    print(tuple(point4), tuple(friend_pair))
    print(friend_pair.friend_id, friend_pair.user_id)
    # point4.add(friend_pair)


if __name__ == '__main__':
    main()
