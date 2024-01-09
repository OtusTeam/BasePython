import os
from pprint import pprint

IS_WINDOWS: bool = "nt" in os.name

print("os.name:", os.name)
print("IS WINDOWS? ", IS_WINDOWS)

BASE_DIR = os.path.dirname(__file__)


def demo_dirs():
    print("Base dir:", BASE_DIR)
    print("path separator:", os.path.sep)
    print(r"C:\\Users\Suren\Desktop\pic.img")
    # print("path:", os.path.sep.join(("Desktop", "pic.img")))
    print("os path join:", os.path.join("Desktop", "pic.img"))

    print(os.listdir("."))
    print(os.listdir(BASE_DIR))
    venv_dir = os.path.join(BASE_DIR, "venv")
    print(os.listdir(venv_dir))
    # print(os.listdir("~"))

    print("cwd:", os.getcwd())
    # print(os.listdir("./venv"))
    print(os.listdir(venv_dir))
    os.chdir("venv")
    print("cwd:", os.getcwd())
    print(os.listdir(venv_dir))

    print()
    print(os.path.expanduser('~'))


def demo_files():
    filename = "file.txt"
    filepath = os.path.join(BASE_DIR, filename)
    print("filepath:", filepath)
    print("fp exists?", os.path.exists(filepath))
    print("venv exists?", os.path.exists("venv"))
    print("qwerty exists?", os.path.exists("qwerty"))
    print("current file exists?", os.path.exists(__file__))
    print("fp is file?", os.path.isfile(filepath))
    print("venv is file?", os.path.isfile("venv"))
    print("qwerty is file?", os.path.isfile("qwerty"))
    print("venv is dir?", os.path.isdir("venv"))

    # file = open(filepath, "w")
    # file.write("qwerty")
    # file.close()
    with open(filepath, "w") as file:
        file.write("Hello\n")
        file.write("Hello to you too!\n")

    if os.path.isfile(filepath):
        print("delete file")
        # os.remove(filepath)
        os.unlink(filepath)

    with open(filepath, "w") as file:
        res = file.write("abc\n")
        print(res)

    with open(filepath, "a") as file:
        res = file.write("qwerty\n")
        print(res)
        file.writelines([
            "John\n",
            "Sam\n",
        ])
        file.writelines([
            "foo\n",
            "bar\n",
        ])

    # with open(filepath, "r") as file:
    with open(filepath) as file:
        # print(repr(file.read()))
        # # print(file.read())
        # file.seek(0)
        # print(file.readlines())
        # for line in file.readlines():
        #     pass
        for line in file:
            print(repr(line))
            if "J" in line:
                print("oh no, J!")
                break

        # print("ok, again")
        # file.seek(0)
        next_line = next(file)
        print("line:", repr(next_line))
        print("ok, next")
        for line in file:
            print(repr(line))


def demo_environ():
    print(os.environ)


def main():
    demo_dirs()
    demo_files()
    pprint(dict(os.environ))
    print(os.environ.get("SECRET_KEY"))
    print(os.getenv("SECRET_KEY"))


if __name__ == "__main__":
    main()
