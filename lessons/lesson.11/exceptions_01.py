# foo = 100
# bar = "one"
#
# print("foo:", foo)
# print("bar:", bar)
# print("add up..")
# var = foo + bar
# print(var)
#
# name = "John"
# print(name)
from time import sleep


def fizz():
    print("running fizz")
    return {}


def buzz():
    print("running buzz")
    foo = 100
    bar = "one"
    foo + bar
    return []


def demo():
    res_fizz = fizz()
    print("res_fizz:", res_fizz)
    sleep(10)
    res_buzz = buzz()
    print("res_buzz:", res_buzz)


def main():
    demo()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("bye!")
