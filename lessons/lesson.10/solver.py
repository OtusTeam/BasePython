class InvalidOperandTypeError(Exception):
    pass


class Solver:

    EXC_TYPE_ERROR_TEXT = "a and b have to be int or float"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        res = self.a + self.b
        print(res)
        return res

    def mul(self):
        if not (
            isinstance(self.a, (int, float))
            and isinstance(self.b, (int, float))
        ):
            raise TypeError(self.EXC_TYPE_ERROR_TEXT)
            # raise InvalidOperandTypeError

        # print("mul", self.a, "and", self.b)
        return self.a * self.b


def abc():
    return 123


def main():
    s = Solver(2, 3)
    print(s, s.add())
    s = Solver(3, 1)
    s.mul()
    print("ok")
    s.add()


if __name__ == '__main__':
    main()
