from functools import wraps
from typing import TypeVar, reveal_type, Sized, Callable, ParamSpec

IntOrFloat = TypeVar("IntOrFloat", float, int)

ReturnType = TypeVar("ReturnType")
P = ParamSpec("P")


def announced(func: Callable[P, ReturnType]) -> Callable[P, ReturnType]:
    print("creating announced function", func)

    @wraps(func)
    def new_announced(*args: P.args, **kwargs: P.kwargs) -> ReturnType:
        print("run function", func, "args:", args, "kwargs:", kwargs)
        result = func(*args, **kwargs)
        print("done function", func, "res:", result)
        return result

    print("successfully created announced func for", func, "announced:", new_announced)
    return new_announced


@announced
def cube(num: IntOrFloat) -> IntOrFloat:
    return num ** 3


@announced
def power(num: IntOrFloat, exponent: int) -> IntOrFloat:
    val: IntOrFloat = num ** exponent
    return val


@announced
def many_str(line: str, times: int) -> str:
    return line * times


@announced
def get_size(obj: Sized) -> int:
    return len(obj)


def main() -> None:
    c1 = cube(5)
    reveal_type(c1)
    print("print:", c1)

    c2 = cube(2.5)
    reveal_type(c2)
    print("print:", c2)
    #
    p = power(2, 10)
    reveal_type(p)
    print("print:", p)
    p2 = power(num=3, exponent=5)
    reveal_type(p2)
    print("print:", p2)
    line = many_str("foobar", 3)
    reveal_type(line)
    print("print:", line)
    size = get_size({"spam", "eggs"})
    reveal_type(size)
    print("print:", size)


if __name__ == '__main__':
    main()
