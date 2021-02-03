class Solver:
    @classmethod
    def add(cls, a, b):
        res = a + b
        return res


def mul(a, b):
    return a * b


class MyCls:
    def __init__(self, a):
        self.a = a

    def get_copy(self):
        self.a += 1
        return self.create_copy(self)
        # return MyCls(self.a)

    @classmethod
    def create_copy(cls, item: "MyCls"):
        # self.a
        item.a += 1
        return cls(item.a)


m = MyCls(42)
m2 = m.get_copy()
m3 = MyCls.create_copy(m2)
m.create_copy(m)

MyCls.get_copy(m)
m.get_copy()
