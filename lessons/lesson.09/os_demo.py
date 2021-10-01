import os


def demo_os_env():
    print(os.name)
    print(os.environ)
    db_conf = os.environ.get("DB_HOST"), os.environ.get("DB_PORT")
    print(db_conf)
    print("secret key:", os.environ.get("SECRET_KEY"))


def demo_os_dirs():
    cwd = os.getcwd()
    print(cwd)

    # "C://" + "Users" + r"\\" + "admin" + "\\\\" + "Downloads"
    # "/" + "home" + "/" + "user" + "/" + "Downloads"
    subdir = os.path.join(cwd, "subdir")
    print("subdir:", subdir)

    if os.path.isdir(subdir):
        print("subdir exists")
    else:
        os.mkdir(subdir)
        print("created subdir")

    os.chdir(subdir)
    print(os.getcwd())


def demo_walk():
    # for root, dirs, files in os.walk("."):
    for root, dirs, files in os.walk(".", topdown=False):
        print("-*", root)
        for dir_ in dirs:
            print("--", dir_)
        for filename in files:
            print("---", filename)


def demo_path_parts():
    cwd = os.getcwd()
    print("cwd:", cwd)
    print("current base name", os.path.basename(cwd))
    print("current dir name", os.path.dirname(cwd))
    file = os.path.join(cwd, "demo_os.py")
    print("file", file)
    print("file name", os.path.basename(file))
    print("dir", os.path.dirname(file))
    print("is it a file?", os.path.isfile(file))

    print(os.path.split(file))
    print(os.path.split(cwd))


def demo_file():
    cwd = os.getcwd()
    file_path = os.path.join(cwd, "file.txt")
    # f = open(file_path, "w")
    # b = f.write("Hello!")
    # f.close()
    # print(b)

    with open(file_path, "r") as file:
        print(file.read())


if __name__ == "__main__":
    # demo_os_env()
    # demo_os_dirs()
    demo_walk()
    # demo_path_parts()
    # demo_file()
