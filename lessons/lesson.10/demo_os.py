import os


BASE_DIR = os.path.dirname(__file__)

IS_WINDOWS = "nt" in os.name


def demo_paths():
    print(__file__)
    print(BASE_DIR)
    print(os.name)
    print("is Windows?", IS_WINDOWS)
    print("os path sep:", os.path.sep)

    print()

    folder_name = "pictures"
    file_name = "cat.jpg"

    # filepath = folder_name + os.path.sep + file_name
    print("".join((BASE_DIR, os.path.sep, folder_name, os.path.sep, file_name)))
    print(os.path.sep.join((BASE_DIR, folder_name, file_name)))

    print(os.path.join(BASE_DIR, folder_name, file_name))


def demo_cwd():
    # current working directory
    cwd = os.getcwd()
    print("cwd", cwd)
    print("cwd repr:", repr(cwd))
    print("B D", BASE_DIR)


def demo_files():
    print(os.listdir("."))
    filename = "file.txt"
    # if os.path.exists(filename) and os.path.isfile(filename):
    if os.path.isfile(filename):
        os.unlink(filename)
        print("deleted file")

    with open(filename, "w") as f:
        f.write("hello\n")

    print(os.listdir("."))

    with open(filename) as f:
        print(f.readlines())

    # f = open(filename)
    # f.read()
    # # error occurs
    # f.close()  # this line doesn't get executed


def main():
    # demo_paths()
    # demo_cwd()
    # print(os.stat(__file__))
    demo_files()


if __name__ == "__main__":
    main()


