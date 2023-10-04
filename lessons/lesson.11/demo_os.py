import os
import sys
# import argparse
# from pprint import pprint
# from collections import Iterator

# print("__file__:")
# print(__file__)
BASE_DIR = os.path.dirname(__file__)
# print(BASE_DIR)


def demo_env():

    APP_STATE = os.getenv("APP_STATE")
    OTUS_COURSE = os.getenv("OTUS_COURSE", "otus")

    print("APP_STATE:", repr(APP_STATE))
    print("OTUS_COURSE:", repr(OTUS_COURSE))

    # print(os.environ.get("OTUS_COURSE"))
    # pprint(dict(os.environ))


def demo_sys_size():
    data = {}
    print(data)

    print(sys.argv)
    print(sys.getsizeof(data))
    data["foo"] = "bar"
    print(sys.getsizeof(data))
    data["spam"] = "eggs"
    print(sys.getsizeof(data))
    data["fizzbuzz"] = "qwerty"
    print(sys.getsizeof(data))
    data["abc"] = "qwerty" * 100
    print(sys.getsizeof(data))

    for i in range(10):
        data[i] = i ** 2

    print(sys.getsizeof(data))
    print(sys.getrefcount(data))


def demo_show_dir():
    print(os.path.sep)
    print(os.getcwd())
    print(os.listdir())
    print(os.listdir("lc-venv"))
    print(os.path.isdir("lc-venv/bin"))
    print(os.listdir("lc-venv/bin"))
    # os.mkdir("/abc/qwe")


def demo_change_dir():
    print(os.getcwd())
    print(os.listdir())
    idea_path = os.path.join(BASE_DIR, ".idea")
    print(os.listdir(idea_path))
    os.chdir("lc-venv")
    print(os.getcwd())
    print(os.listdir())
    print(os.listdir(idea_path))
    print(idea_path)
    cats_pics_path = os.path.join(BASE_DIR, "pics", "cats")
    print(cats_pics_path)
    my_cat_pic_path = os.path.join(cats_pics_path, "my-cat.jpg")
    print(my_cat_pic_path)


def demo_files():
    filename = "plan.txt"
    filepath = os.path.join(BASE_DIR, filename)
    print(filepath)
    print("exists?", os.path.exists(filepath))
    print("isfile?", os.path.isfile(filepath))
    print("isdir?", os.path.isdir(filepath))
    # print("BASE_DIR isdir?", os.path.isdir(BASE_DIR))
    # print("BASE_DIR isfile?", os.path.isfile(BASE_DIR))

    with open(filepath, "w") as file:
        file.write("Hello\n")

    if os.path.isfile(filepath):
        print("delete file")
        # os.remove()
        os.unlink(filepath)

    with open(filepath, "w") as file:
        file.write("Hello there!\n")

    with open(filepath, "a") as file:
        file.write("qwerty\n")
        file.writelines(["foo\n", "bar\n"])
        file.writelines(["\tspam\n", "\teggs\n"])
        # for

    # file = open(filepath, "a")
    # file.write("end\n")
    # 1/0
    # file.close()

    # with open(filepath, "r")
    with open(filepath) as file:
        # print(file.read())
        # print(repr(file.read()))
        # print(file.readlines())
        for line in file:
            # print(line)
            # print(line, end="")
            print(repr(line))
            if "foo" in line:
                break

        print("ok, now continue")

        for line in file:
            print(repr(line))
            if "spam" in line:
                break
        print("ok, now what?")
        # print(next(file))
        file.seek(0)
        for line in file:
            print(line, end="")

        print()


class Count:
    def __init__(self, start=0):
        self._count = start
        self._start = start

    def __iter__(self):
        self._count = self._start
        return self

    def __next__(self):
        self._count += 1
        return self._count


def demo_count():
    c = Count()
    for cnt, value in zip(c, range(10, 20, 2)):
        print(cnt, value)

    for cnt, value in zip(c, range(15, 30, 3)):
        print(cnt, value)


if __name__ == "__main__":
    # demo_env()
    # demo_sys_size()
    # demo_show_dir()
    # demo_change_dir()
    # print(demo_files.__doc__)
    # demo_files()
    pass
