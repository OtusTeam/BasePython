class Box:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def __len__(self):
        return self.x2 - self.x1


box = Box(1, 10)

print(len(box))
# print(box.__len__())