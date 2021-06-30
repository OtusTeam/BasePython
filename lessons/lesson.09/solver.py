def from_dict2(data_dict: dict):
    s = Solver2D(data_dict["a"], data_dict["b"])
    return s


class Solver2D:
    EXC_VALUES_HAVE_TO_BE_NUMS = "all values have to be nums"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def from_dict(cls, data_dict: dict):
        s = cls(data_dict["a"], data_dict["b"])
        return s

    @staticmethod
    def from_dict2(data_dict: dict):
        s = Solver2D(data_dict["a"], data_dict["b"])
        return s

    def add(self):
        if not all(map(
            lambda v: isinstance(v, (int, float)),
            (self.a, self.b),
        )):
            raise TypeError(self.EXC_VALUES_HAVE_TO_BE_NUMS)

        result = self.a + self.b

        print("a =", self.a, "b =", self.b, ". a + b =", result)
        return result

    def mul(self):
        return self.a * self.b


class Solver3D(Solver2D):
    def __init__(self, a, b, c=0):
        super().__init__(a, b)
        self.c = c

    def add(self):
        # return super().add() + self.c
        return self.a + self.b + self.c


def main():
    s1 = Solver2D(1, 2)
    s2 = Solver2D(5, 7)

    print("s1 add:", s1.add())
    print("s2 add:", s2.add())

    s3 = Solver3D.from_dict({"a": 4, "b": 6})
    print("s3", s3)
    s3_2 = Solver3D.from_dict2({"a": 4, "b": 6})
    print("s3_2", s3_2)
    s3_3 = from_dict2({"a": 4, "b": 6})
    print("s3_3", s3_3)


if __name__ == '__main__':
    main()
