import os
# from pprint import pprint
# import asyncio

BASE_DIR = os.path.dirname(__file__)
# BASE_DIR.rstrip("/")
# IS_WIDOWS = "nt" in os.name
IS_WIDOWS = os.name == "nt"


def show_env():
    print(os.getenv("SECRET_KEY", "super-secret"))
    print(os.environ.get("APP_DEBUG", "1"))
    # pprint(dict(os.environ))


def demo_build_path():
    print(BASE_DIR)
    venv_dir = os.path.join(BASE_DIR, "venv")
    print(os.path.sep)
    print(venv_dir)


def demo_file():
    filename = "text.txt"
    filepath = os.path.join(BASE_DIR, filename)
    print(filepath)
    print("exists", os.path.exists(filepath))
    print("isfile", os.path.isfile(filepath))
    print("isdir", os.path.isdir(filepath))

    if os.path.isfile(filepath):
        os.unlink(filepath)
        print("deleted exising file", filename)

    # file = open(filepath)
    # file.read()
    # file.write()
    # file.close()
    with open(filepath, "w") as file:
        file.write("Hello\n")

    with open(filepath, "a") as file:
        file.write("fizz\n")
        file.writelines(["foo \n", "bar\n"])

    with open(filepath, "r") as file:
        for line in file:
            print(repr(line))
            print(repr(line.strip()))
            break

        print(repr(next(file)))
        file.seek(0)
        print(repr(next(file)))


def demo_cwd():
    cwd = os.getcwd()
    print(cwd)
    print(os.listdir("."))
    # NEVER CHANGE DIR!
    # os.chdir("./venv")
    # cwd = os.getcwd()
    # print(cwd)
    # print(os.listdir("."))
    os.listdir(BASE_DIR)


def main():
    # if IS_WIDOWS:
    #     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # print("base dir", BASE_DIR)
    # demo_cwd()
    # demo_build_path()
    # demo_file()
    show_env()


if __name__ == "__main__":
    main()
