class Line:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    @property
    def length(self):
        return abs(self.x2 - self.x1)

    def __len__(self):
        return self.length

    def __eq__(self, other: Line) -> bool:
        if not isinstance(other, Line):
            raise TypeError
        return self.x1 == other.x1 and self.x2 == other.x2


line = Line(13, 5)
print("length:", line.length)

line2 = Line(7, 2)
print("length2:", len(line2))

print("line == line2:", line == line2)

line3 = Line(line2.x1, line2.x2)
print("line2 == line3:", line2 == line3)
