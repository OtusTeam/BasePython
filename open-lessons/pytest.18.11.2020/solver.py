
class Solver:

    @classmethod
    def add(cls, a, b):
        res = a + b
        print("result a + b", res)
        return res


def mul(a, b):
    return a * b


SUB_ERROR_TEXT = "All arguments have to be of type int or float"


def sub(a, b):
    if not all(
        map(
            lambda x: isinstance(x, (int, float)),
            (a, b),
        )
    ):
        raise TypeError(SUB_ERROR_TEXT)
    return a - b


if __name__ == '__main__':
    res = Solver.add(1, 2)
    print("expected 3, got", res)
