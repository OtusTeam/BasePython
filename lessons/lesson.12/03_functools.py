import random
from dataclasses import dataclass
from functools import cache, wraps, partial
from timeit import default_timer as timer


def show_exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = timer()
        result = func(*args, **kwargs)
        total_time = timer() - start_time
        print(f"{func.__name__} took {total_time:.9f} seconds")
        return result

    return wrapper


@show_exec_time
@cache
def factorial(n):
    """
    Calculate the factorial of n.

    :param n:
    :return:
    """
    print(f"get factorial of {n}")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def greet(name, greeting="Hello"):
    line = f"{greeting}, {name}!"
    print(line)
    return line


@dataclass
class User:
    id: int
    name: str
    email: str
    username: str


def create_user(
    name: str,
    email: str,
    username: str,
):
    user = User(
        id=random.randint(1, 1000),
        name=name,
        email=email,
        username=username,
    )
    print(user)
    return user


def demo_factorial():

    # print("warm up cache start")
    # print(factorial(990))
    # print("warm up cache complete")
    print(factorial(2))
    print(factorial(5))
    print(factorial(10))
    print(factorial(7))
    print(factorial(100))
    print(factorial(10))
    print("---")
    print(factorial(n=100))


def demo_wraps():

    print("factorial", factorial)
    print("wrapped factorial", factorial.__wrapped__)
    print("wrapped wrapped factorial", factorial.__wrapped__.__wrapped__)
    print("help factorial:===")
    help(factorial)
    print("<<< help")
    print("doc factorial", factorial.__doc__)


def ask_for_username(create):
    username = input("username: ")
    create(username)


def main():
    # demo_factorial()
    # demo_wraps()
    greet("OTUS")
    greet("Suren")

    greet("Bob", "Hi")
    greet("Alice", greeting="Hi")

    hi = partial(greet, greeting="Hi")
    hi("john")
    hi("kyle")

    name = "Bob Smith"
    email = "bob@example.com"

    # create_user(
    #     name=name,
    #     email=email,
    #     username="bob",
    # )

    to_create = partial(create_user, name, email)
    ask_for_username(to_create)


if __name__ == "__main__":
    main()
