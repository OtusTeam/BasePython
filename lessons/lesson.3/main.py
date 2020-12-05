from time import time
from functools import wraps


def lesson2():
    hello_text = "Hello world!"

    # DRY - do not repeat yourself


    x = "foo"


    def show_x(x):
        x = x * 2
        show_x = "qwe"
        print(x)
        print(show_x)


    print(x)
    show_x(x)
    print(x)



    def do_hello(name="World!"):
        # if hello_text:
        #     print(hello_text[0], hello_text[-1])
        print("Hello", name.title())


    do_hello()
    do_hello()
    do_hello()
    do_hello()
    do_hello("james brown")
    do_hello("John")
    do_hello("Ann")
    do_hello("world!")
    # do_hello(["Sam", "Nick", 1, None, 3])


    def greet_names(names):
        # never change in place!!
        # for name in names:
        #     print("Hello", name.title())
        while names:
            name = names.pop()
            print("Hello", name.title())

        # return None


    names = ["sam", "ann", "nick", "john"]
    print("names:", names)
    greet_names(names)
    print("names:", names)


    def filter_names(names, max_len=3):
        result = []
        for name in names:
            if len(name) <= max_len:
                result.append(name)
        return result


    names = ["sam", "ann", "nick", "john", "jo"]
    print(names)
    filtered_names = filter_names(names)
    print("filtered_names 3:", filtered_names)
    print(names)
    print("filtered_names 1:", filter_names(names, 1))
    print("filtered_names 2:", filter_names(names, 2))
    print("filtered_names 4:", filter_names(names, max_len=4))


    def add_default_names_to_list(names):
        names.extend(["sam", "nick"])


    print(names)
    add_default_names_to_list(names)
    print(names)

    def get_default_names():
        return ["sam", "nick"]

    print(names)
    names.extend(get_default_names())
    print(names)


    def get_new_names(base_names=None):
        # if base_names is None:
        #     base_names = []
        new_names = ["base"]
        if base_names:
            new_names.extend(base_names)
        default_names = get_default_names()
        new_names.extend(default_names)
        return new_names


    names = ["john", "sara"]

    new_names = get_new_names()
    print(new_names)
    print(names)
    print(names is new_names)

    new_names = get_new_names(names)
    print(new_names)
    print(names)
    print(names is new_names)



    """
    if hello_text:
        print(hello_text[0], hello_text[-1])
    print(hello_text)
    
    if hello_text:
        print(hello_text[0], hello_text[-1])
    print(hello_text)
    
    print(hello_text[0], hello_text[-1])
    print(hello_text)
    """

    # True values
    i = 1
    i_n = -1
    b = True
    s = "spam"
    t = ("spam", "eggs")
    l = ["foo"]

    # False values
    n = None
    b = False
    i = 0
    # print(1 == True)
    # print(0 == False)
    # print(True + False + True)
    # print(False + False)
    s = ""
    t = ()
    l = []
    d = {}
    s = set()

    foobar = None

    # d["foo"] = "bar"
    if d:
        foobar = 123

    print(foobar)
    if foobar is not None:
        print("foobar:", foobar)


    def time_call(func):
        # print("incoming func:", func)
        @wraps(func)
        def wrapper(p):
            start = time()
            res = func(p)
            end = time()
            print("res for", p, " = ", res)
            time_taken = end - start
            print(f"time taken: {time_taken:.13f}")
            return res
        # print("id   wrapper", id(wrapper))
        print(wrapper.__wrapped__)
        print(id(wrapper))
        print(id(func))
        print(id(wrapper.__wrapped__))
        return wrapper

    #

    @time_call
    def fib(pos):
        """
        1, 1, 2, 3, 5, 8
        1 = 1 + 0
        2 = 1 + 1
        3 = 2 + 1
        5 = 3 + 2  || (2 + 1) + 2
        8 = 5 + 3  || 8 = (3 + 2) + 3 || 8 = ((2 + 1) + 2) + (2 + 1)
        :param pos:
        :return:
        """
        if pos <= 1:
            return 1
        return fib(pos - 1) + fib(pos - 2)


    print(fib)
    print(fib.__wrapped__)

    fib_nums = []
    for i in range(5):
        fib_nums.append(fib(i))

    print(fib_nums)
    print([fib(i) for i in range(7)])
    # print([fib(i) for i in range(30)])


    fib_nums = []
    # for i in range(35):
    for i in range(3):
        print("pos", i)
        start = time()
        res = fib(i)
        end = time()
        fib_nums.append(res)
        print("res for", i, " = ", res)
        time_taken = end - start
        print(f"time taken: {time_taken:.13f}")


    t_call = time_call

    timed_fib = t_call(fib)
    print("id timed_fib", id(timed_fib))
    print("created new func")
    print(timed_fib(3))



    def time_call_any(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(args)
            print(kwargs)
            start = time()
            res = func(*args, **kwargs)
            end = time()
            print("res", func, " = ", res)
            time_taken = end - start
            print(f"time taken: {time_taken:.13f}")
            return res

        # wrapper.__wrapped__ = func
        # wrapper.__name__ = func.__name__
        return wrapper


    @time_call_any
    def add(a, b):
        return a + b

    add(17576547654654665, 1757654765465466517576547654654665)

    @time_call_any
    def hello_again(name="World"):
        return "Hello " + name

    print("d", hello_again())
    print("d", hello_again("John"))
    print("d", hello_again(name="Sam"))

    print("o", hello_again.__wrapped__())
    print("o", hello_again.__wrapped__("John"))
    print("o", hello_again.__wrapped__(name="Sam"))


    a = ['1', 3, True]
    for i in a:
        print(i)

    iterator = iter(a)
    print("n", next(iterator))
    print("n", next(iterator))
    print("n", next(iterator))
    # print("n", next(iterator))


def lesson3_generators():
    """
    # generators

    :return:
    """

    def pow(up_to, e=2):
        results = []
        for i in range(up_to):
            results.append(i ** e)
        return results


    print("pow up to 13", pow(13))


    def pow_gen(up_to, e=3):
        print("in pow gen")
        for i in range(up_to):
            print("process", i)
            yield i ** e
            print("continue from", i)


    print("pow_gen up to 13", list(pow_gen(13)))

    for i in pow_gen(13):
        print(i)
        if i > 100:
            print("i is gt 100")
            break


    def true_and_false(val=True):
        while True:
            yield val
            val = not val


    g = true_and_false()
    for i in range(100):
        print(next(g))


def todo():
    pass

print("wip")
