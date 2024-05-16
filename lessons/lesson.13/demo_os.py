import os

from pprint import pprint

print(__file__)
BASE_DIR = os.path.dirname(__file__)


def check_win():
    is_windows = os.name == "nt"
    print("is windows?", is_windows)


def demo_dirs():
    print("BASE_DIR:", BASE_DIR)
    print("sep:", os.path.sep)
    filepath = os.path.join(BASE_DIR, "file.txt")
    print("filepath:", filepath)
    print("isfile filepath?", os.path.isfile(filepath))
    print("isdir filepath?", os.path.isdir(filepath))

    images_path = os.path.join(BASE_DIR, "images")
    print("exists images_path?", os.path.exists(images_path))
    print("isdir images_path?", os.path.isdir(images_path))

    if not os.path.exists(images_path):
        print("create dir")
        os.mkdir(images_path)
    print("exists images_path?", os.path.exists(images_path))
    print("isdir images_path?", os.path.isdir(images_path))

    # print("working directory", os.getcwd())
    # os.chdir(images_path)
    # # os.chdir("images")
    # print("new working directory", os.getcwd())

    print("current dir contents:", os.listdir(BASE_DIR))
    print("'.idea' dir contents:", os.listdir(os.path.join(BASE_DIR,'.idea')))

    home_dir = os.path.expanduser("~")
    print("home_dir:", home_dir)
    print("home dir contents:", os.listdir(home_dir))


def demo_files():
    filepath = os.path.join(BASE_DIR, "file.txt")

    print("isfile filepath?", os.path.isfile(filepath))

    # file = open(filepath, "w")
    # file.write("Hello World!")
    # file.close()

    with open(filepath, "w") as file:
        file.write("hello world")
        file.write(os.linesep)
        file.write("Path separator: ")
        file.write(os.path.sep)
        file.write(os.linesep)
        # file.write("Hello again!\n")
        file.write("Hello again!")
        file.write(os.linesep)

    if os.path.isfile(filepath):
        print("file exists, deleting")
        os.remove(filepath)
        # os.unlink(filepath)

    with open(filepath, "w") as file:
        total = file.write("First line\n")
        print("Wrote bytes", total)

    with open(filepath, "a") as file:
        file.write("Second line\n")
        file.write("Another line\n")

        file.writelines([
            "John\n",
            "Sam\n",
        ])

        file.writelines([
            "foo",
            "bar",
        ])

        file.write(os.linesep)

    with open(filepath, "ab") as file:
        file.write(b"Hi bytes!")
        file.write(b"\n")
        file.write(bytes([97]))
        file.write(bytes([10, 97, 97, 97, 10]))

    print()
    print()
    print()

    with open(filepath) as f:
        file_contents = f.read()
    print(file_contents)
    print("len:", len(file_contents))

    with open(filepath) as f:
        file_lines = f.readlines()

    print(file_lines)
    print("file_lines len:", len(file_lines))

    # print("stat:", os.stat(filepath))

    with open(filepath) as f:
        for idx, line in enumerate(f, start=1):
            print(repr(line))
            if "Sam" in line:
                print("Found 'Sam' on line", idx)
                break

        print("---")
        print(repr(next(f)))
        print(repr(next(f)))
        print("continue cycle to the end")

        for line in f:
            print(repr(line))

        f.seek(0)
        print()
        print(repr(next(f)))


def main():
    # check_win()
    # demo_dirs()
    demo_files()
    # print(os.environ)
    pprint(dict(os.environ))
    foobar = os.getenv("FOOBAR")
    print("foobar:", foobar)


if __name__ == "__main__":
    main()
