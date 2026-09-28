class Line:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    @property
    def length(self):
        return abs(self.x2 - self.x1)

    def __len__(self):
        return self.length


line = Line(13, 5)
print("length:", line.length)

line2 = Line(7, 2)
print("length2:", len(line2))
