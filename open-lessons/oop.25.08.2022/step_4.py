from typing import Union


class InvalidOperandError(TypeError):
    pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str([self.x, self.y])

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               f"x={self.x}, y={self.y})"

    # def add(self, other: list | tuple | "Point"):
    def add(self, other: Union["Point", list, tuple]):
        # if not isinstance(point, self.__class__):
        #     raise InvalidOperandError(
        #         f"Should be {self.__class__}, not"
        #         f" {type(point)}")
        if isinstance(other, self.__class__):
            return self.__class__(
                x=self.x + other.x,
                y=self.y + other.y,
            )

        if (
            isinstance(other, (tuple, list))
            and len(other) == 2
        ):
            x, y = other
            return self.__class__(
                x=self.x + x,
                y=self.y + y,
            )

        raise InvalidOperandError(
            f"Should be {self.__class__}, not"
            f" {type(other)}")

    def __add__(self, other):
        return self.add(other)

    # def __radd__(self, other: "Point"):
    def __radd__(self, other):
        return self.add(other)

    def __iadd__(self, point: "Point"):
        if not isinstance(point, self.__class__):
            raise InvalidOperandError(
                f"Should be {self.__class__}, not"
                f" {type(point)}")
        self.x += point.x
        self.y += point.y
        return self


p1 = Point(1, 2)
p2 = Point(x=3, y=4)

print(p1)
print(p2)
print([p1, p2])

p3 = p1 + p2
print(p3)

p4 = p3.add(p2)
print(p4)

res = (5, 7) + p1
print(res)

print([res, p1 + [1, 2]])

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("id l1", id(list1))

list3 = list1 + list2
print(list1)
print("id l1", id(list1))

print(list2)
print(list3)

list1 += list2
print(list1)
print("id l1", id(list1))
print(list2)

list1.append(7)
print(list1)
print("id l1", id(list1))


print([p1, p2])
print("id p1", id(p1))
p1 += p2
print("id p1", id(p1))
print([p1, p2])

