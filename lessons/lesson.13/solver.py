from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pprint import pprint
    pprint(1 / 0)


class Solver:
    INVALID_TYPE = "Invalid Type, expected both to be str, or numbers"
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # self.a = b
        # self.b = a

    def add(self):
        if not (
            isinstance(self.a, int | float)
            and isinstance(self.b, int | float)
            or
            isinstance(self.a, str)
            and isinstance(self.b, str)
        ):
            raise TypeError(self.INVALID_TYPE, self.a, self.b)
        # 1 // self.a
        res = self.a + self.b
        print("result:", res)
        return res

    def mul(self):
        return self.a * self.b

    def close(self):
        # удалить из базы
        # очистить кэш
        # закрыть соединение
        print("closing / clearing solver", self)
