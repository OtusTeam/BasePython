class Solver:

    EXC_PARAMS_SHOULD_BE_NUMS = "a and b should be nums"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        res = self.a + self.b
        print("res:", res)
        return res

    def mul(self):
        if not (
            isinstance(self.a, (int, float))
            and isinstance(self.b, (int, float))
        ):
            raise TypeError(self.EXC_PARAMS_SHOULD_BE_NUMS)
        return self.a * self.b


def div(a, b):
    return a / b
