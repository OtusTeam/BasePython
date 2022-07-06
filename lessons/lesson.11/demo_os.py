import os

BASE_DIR = os.path.dirname(__file__)
IS_WINDOWS = 'nt' in os.name


def demo_paths():
    print("__file__:", __file__)
    print(os.name)
    print("IS_WINDOWS:", IS_WINDOWS)
    print("BASE_DIR:", BASE_DIR)
    print("sep:", os.path.sep)

    print()

    filename = "cats.jpg"
    foldername = "pictures"

    # BASE_DIR + "/"
    # path = BASE_DIR + os.path.sep + foldername + os.path.sep + filename
    # path = f"{BASE_DIR}{os.path.sep}"
    # path = "{base}{sep}{folder}{sep}{file}".format(
    #     sep=os.path.sep,
    #     base=BASE_DIR,
    #     file=filename,
    #     folder=foldername,
    # )

    # path = "|".join(("spam", "eggs"))
    # print(path)
    # path = os.path.sep.join((BASE_DIR, foldername, filename))
    # print(path)

    path = os.path.join(BASE_DIR, foldername, filename)
    print(path)


def demo_cwd():
    # current working directory
    cwd = os.getcwd()
    print("cwd:", cwd)

    # NEVER PLEASE
    os.chdir("./venv")

    cwd = os.getcwd()
    print("cwd:", cwd)


def demo_list_dir():
    print(os.listdir("."))
    print(os.listdir("./venv"))

    if os.path.isdir(".idea"):
        print(".idea folder exists")

    if os.path.isdir("qwerty"):
        print("qwerty folder exists")
    else:
        print("qwerty folder doesn't exist")

    # if os.path.isfile("demo_os.py")
    if os.path.isfile(__file__):
        print("this file exists")

    filename = "file.txt"
    if os.path.isfile(filename):
        # os.remove(filename)
        os.unlink(filename)
        print("deleted file", filename)

    with open(filename, "w") as f:
        f.write("hello\n")
        f.writelines(["spam\n", "eggs\n"])

    with open(filename) as f:
        print(f.readlines())

    with open(filename) as f:
        print([f.read()])

    with open(filename) as f:
        for line in f:
            print("line:", repr(line))
            break


def main():
    # demo_paths()
    # demo_cwd()
    # print(os.listdir(BASE_DIR))
    demo_list_dir()


if __name__ == '__main__':
    main()
