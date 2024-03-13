from functools import cache, partial


@cache
def factorial(n):
    print("get factorial for n", n)
    if n < 2:
        return n
    return n * factorial(n - 1)


def say_hi(name, greeting="Hi"):
    msg = f"{greeting}, {name}!"
    print(msg)
    return msg


def main_factorial():
    print(factorial(3))
    print(factorial(4))
    print(factorial(5))
    print(factorial(6))


def main_partial():
    say_hi("Otus")
    say_hi("John")
    say_hi("King", greeting="Hello")
    say_hi("Queen", greeting="Hello")

    hello = partial(say_hi, greeting="Hello")
    hello("King")
    hello("Queen")
    hello(name="Bob")



def main():
    # main_factorial()
    main_partial()


if __name__ == "__main__":
    main()
