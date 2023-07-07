from functools import partial


def say_hi(name, greeting="Hi"):
    msg = f"{greeting}, {name}!"
    print(msg)
    return msg


def main():
    say_hi("Bob")
    say_hi("Alice")
    say_hi("John", "Hello")
    say_hi("Sam", greeting="Hello")

    hello = partial(say_hi, greeting="Hello")
    print(hello)
    hello("Kate")

    greet_bob = partial(say_hi, "Bob")
    print(greet_bob)
    greet_bob("Hello")
    greet_bob("How are you")
    greet_bob(greeting="What's up")


if __name__ == '__main__':
    main()
