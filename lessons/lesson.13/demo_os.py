import os
from pprint import pprint

IS_WINDOWS = os.name == "nt"

BASE_DIR = os.path.dirname(__file__)

print("OS name:", os.name)
print("IS_WINDOWS:", IS_WINDOWS)


# print(__file__)
# print(os.path.dirname(__file__))
# print(str(__file__).rsplit(os.path.sep)[0])


def demo_dirs():
    print("BASE_DIR:", BASE_DIR)
    # print("local files:", os.listdir("."))
    print("local files:", os.listdir(BASE_DIR))
    print("os.path.sep:", os.path.sep)
    images_path = os.path.join("Desktop", "images", "cat.jpg")
    print("joined desktop path:", images_path)
    print("images path exists?", os.path.exists(images_path))
    print("images path is file?", os.path.isfile(images_path))

    print("BASE_DIR exists?", os.path.exists(BASE_DIR))
    print("is base dir a dir?", os.path.isdir(BASE_DIR))
    print("is base dir a file?", os.path.isfile(BASE_DIR))
    current_file = __file__
    print("is current file a dir?", os.path.isdir(current_file))
    print("is current file a file?", os.path.isfile(current_file))

    print("current working directory:", os.getcwd())
    venv_path = os.path.join(BASE_DIR, ".venv")
    print("venv path:", venv_path)
    print("is .venv path a dir?", os.path.isdir(venv_path))
    print("is .venv path a file?", os.path.isfile(venv_path))

    # PLEASE NEVER CHANGE DIR
    os.chdir(".venv")
    print("current working directory:", os.getcwd())
    print("is .venv path a dir?", os.path.isdir(venv_path))
    print("is .venv path a file?", os.path.isfile(venv_path))
    home_dir = os.path.expanduser("~")
    print(home_dir)
    print("is home_dir a dir?", os.path.isdir(home_dir))

    # my_app_cache_dir = os.path.join(home_dir, ".cache/my-app")
    #


def demo_files():
    filename = "file.txt"
    filepath = os.path.join(BASE_DIR, filename)
    print("filepath:", filepath)
    print("filepath type:", type(filepath))
    print("fp exists?", os.path.exists(filepath))
    print("fp is file?", os.path.isfile(filepath))

    # file = open(filepath, "w")
    # file.write("Hello!")
    # file.close()
    with open(filepath, "w") as f:
        f.write("hello world!")
        f.write(os.linesep)
        f.write("Hello again!\n")

    if os.path.isfile(filepath):
        print("delete file")
        # os.remove(filepath)
        os.unlink(filepath)

    with open(filepath, "w") as f:
        res = f.write("First line!\n")
        print("Wrote bytes:", res)

    with open(filepath, "a") as f:
        f.write("Second line!\n")
        f.write("Qwerty\n")

        f.writelines([
            "John\n",
            "Sam\n",
        ])
        f.writelines([
            "foo\n",
            "bar\n",
        ])

    with open(filepath, "ab") as f:
        f.write(b"Hi there!")
        f.write(bytes([10, 97]))
        f.write(bytes([10]))

    print()
    print()
    print()
    # with open(filepath, "r") as f:
    with open(filepath) as f:
        file_data = f.read()
    print(file_data)
    print(repr(file_data))

    print()
    print()
    with open(filepath) as f:
        file_lines = f.readlines()
    print(file_lines)
    for line in file_lines:
        print(line, end="")

    print()
    print()
    with open(filepath) as f:
        for line in f:
            # print(line, end="")
            print(repr(line))
            if "Qwerty" in line:
                print("met Qwerty")
                break

        print(repr(next(f)))
        print(repr(next(f)))

        print("continue cycle")
        for line in f:
            print(repr(line))
            if "bar" in line:
                print("stop on bar")
                break

        f.seek(0)
        # f.seek(3)
        print(repr(next(f)))


def main():
    # os.chdir(".idea")
    # print("current working directory:", os.getcwd())
    # os.chdir("..")
    demo_dirs()
    demo_files()
    print(os.environ)
    pprint(dict(os.environ))
    print("secret key", os.environ.get("MY_SECRET_KEY"))
    print("secret key", os.getenv("MY_SECRET_KEY"))


if __name__ == "__main__":
    main()
