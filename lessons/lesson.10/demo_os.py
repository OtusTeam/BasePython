import os

BASE_DIR = os.path.dirname(__file__)


def demo_os_main():
    cwd = os.getcwd()
    print("cwd:", cwd)

    print("BASE_DIR:", BASE_DIR)
    print("sep:", os.path.sep)


def demo_os_file():
    filename = "file.txt"

    with open("filename", "w"):
        pass

    names = os.listdir(BASE_DIR)
    print("BASE_DIR contains:", names)

    for name in names:
        full_path = os.path.join(BASE_DIR, name)
        if os.path.isdir(full_path):
            print(repr(name), "is dir")
        elif os.path.isfile(full_path):
            print(repr(name), "is file")
        else:
            print(repr(name), "is not a file or dir, what is it?")

    filepath = os.path.join(BASE_DIR, filename)

    if not os.path.exists(filepath):
        print("create file", filepath)
        with open(filepath, "a") as f:
            f.write("Hello file\n")

    print("stat", os.stat(filepath))


def demo_walk():

    for root, dirs, files in os.walk(BASE_DIR):
        print("***root", root)
        print("*dirs:")
        for dir_ in dirs:
            print("-", dir_)
        print("%files:")
        for filename in files:
            print("-", filename)


if __name__ == '__main__':
    # demo_os_main()
    # demo_os_file()
    demo_walk()
