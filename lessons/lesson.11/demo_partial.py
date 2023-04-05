from functools import partial


def say_hi(name, greeting="Hi"):
    msg = f"{greeting}, {name}!"
    print(msg)
    return msg


def main():
    say_hi("Otus")
    say_hi("John")
    # say_hi("King", greeting="Hello")
    # say_hi("Queen", greeting="Hello")

    hello = partial(say_hi, greeting="Hello")

    # print(hello)
    hello("King")
    hello("Queen")
    hello(name="Bob")


if __name__ == "__main__":
    main()
