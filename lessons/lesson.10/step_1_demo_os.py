import os

BASE_DIR = os.path.dirname(__file__)
# IS_WINDOWS = 'nt' in os.name
IS_WINDOWS = os.name == "nt"


def demo_paths():
    print("__file__", __file__)
    print(BASE_DIR)
    print("IS_WINDOWS", IS_WINDOWS)
    print("os.path.sep:", os.path.sep)
    # os.chdir("./venv")

    filename = "cats.jpg"
    folder_name = "pictures"

    # os.path.sep.join((filename, folder_name))
    # path = os.path.join(folder_name, filename)
    path = os.path.join(BASE_DIR, folder_name, filename)
    print(path)


def demo_cwd():
    cwd = os.getcwd()
    print("cwd:", cwd)
    print(os.listdir("."))

    # NEVER PLEASE
    os.chdir("./venv")
    # !!!!!

    cwd = os.getcwd()
    print("cwd:", cwd)
    print(os.listdir("."))

    #
    print(os.listdir(BASE_DIR))


def demo_listdir():

    if os.path.isfile(__file__):
        print("current file exists")

    filename = "file.txt"
    if os.path.isfile(filename):
        print("delete file", filename)
        os.unlink(filename)

    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, "w") as f:
        f.write("Hello\n")
        # f.write(str((0.5).as_integer_ratio()))
        # f.write(0.5)
        f.writelines(["spam\n", "eggs\n"])

    with open(filepath, "wb") as f:
        f.write(b"Hello world!\n")

    with open(filepath, "a") as f:
        f.writelines(["spam\n", "eggs\n"])

    # with open(filepath, "r")
    with open(filepath) as f:
        print(f.readlines())

    with open(filepath) as f:
        print(repr(f.read()))

    with open(filepath) as f:
        for line in f:
            print("line:", repr(line))
            # if i > 10:
            #     break
            break

        print(repr(next(f)))
        f.seek(0)
        print(repr(next(f)))

    with open(filepath) as f:
        lines = list(filter(lambda s: ('a' in s or 'l' in s), f))
        print(lines)


if __name__ == "__main__":
    # demo_paths()
    # demo_cwd()
    demo_listdir()
