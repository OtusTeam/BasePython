import os

# print("__file__", __file__)
BASE_DIR = os.path.dirname(__file__)
print(BASE_DIR)


def demo_dir():
    """
    get cwd
    get current working directory
    :return:
    """
    print(os.getcwd())
    print(os.listdir("."))
    print(os.listdir())
    os.chdir("./venv")
    print(os.getcwd())
    print(os.listdir("."))
    print(os.listdir(BASE_DIR))
    print(os.listdir())


def demo_build_path():
    print(BASE_DIR)
    print(os.path.sep)
    # base_dir = BASE_DIR + "/"
    # print(base_dir)
    venv_dir = os.path.join(BASE_DIR, "venv")
    print(venv_dir)


def demo_file():
    filename = "text.txt"
    filepath = os.path.join(BASE_DIR, filename)
    print(filename)
    print(filepath)
    print("exists?", os.path.exists(filepath))
    print("isfile?", os.path.isfile(filepath))
    print("isdir?", os.path.isdir(filepath))

    # file = open(filepath)
    # file.read()
    # # file.write()
    # 1/0
    # file.close()
    with open(filepath, "w") as file:
        file.write("Hello\n")

    if os.path.isfile(filepath):
        stat = os.stat(filepath)
        print(stat)
        print("file is", stat.st_size, "bytes")
        # os.remove()
        os.unlink(filepath)
        print("deleted file")

    with open(filepath, "a") as file:
        file.write("fizz\n\n")
        file.writelines(["foo\n", "bar\n"])
        nums = [1, 2, 3]
        last_elem_idx = len(nums) - 1
        for idx, num in enumerate(nums):
            if idx == 0:
                file.write("[")
            file.write(str(num))
            if idx == last_elem_idx:
                file.write("]")
            else:
                file.write(",\n")
        file.write("\n")

    with open(filepath, "r") as file:
        for line in file:
            # print(repr(line))
            # print(line, end=";")
            # print(line, end="")
            # print(repr(line.strip()))
            print(line.strip())
            if "foo" in line:
                break

        print("ok====")
        print(repr(next(file)))
        print(repr(next(file)))
        print(repr(next(file)))
        file.seek(0)
        print(repr(next(file)))


def main():
    # demo_dir()
    # demo_build_path()
    demo_file()


if __name__ == '__main__':
    main()
