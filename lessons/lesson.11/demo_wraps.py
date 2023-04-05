from functools import wraps


def show_args(func):

    @wraps(func)
    def wrapper(*a):
        args_str = ", ".join(map(str, a))
        print("process func",
              func.__name__,
              "with args", args_str)
        result = func(*a)
        print("result =", result)
        return result

    return wrapper


@show_args
def sum_nums(*nums):
    return sum(nums)


def main():
    print(sum_nums)
    print(sum_nums.__name__)
    # print(sum_nums.__wrapped__)
    res = sum_nums()
    print(res)


if __name__ == "__main__":
    main()
