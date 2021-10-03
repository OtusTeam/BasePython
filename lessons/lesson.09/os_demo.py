import os


def demo_os_env():
    print(os.name)
    print(os.environ)
    print(os.environ.get("DB_HOST"))
    print(os.environ.get("DB_PORT"))
    print(os.environ.get("KEY"))
    db_conf = os.environ.get("DB_HOST"), os.environ.get("DB_PORT")
    print(db_conf)
    # print("secret key:", os.environ.get("SECRET_KEY"))


def demo_os_dirs():
    cwd = os.getcwd()
    print(cwd)

    # "C://" + "Users" + r"\\" + "admin" + "\\\\" + "Downloads"
    # "/" + "home" + "/" + "user" + "/" + "Downloads"
    subdir = os.path.join(cwd, "subdir")
    print(type(subdir))
    print("subdir:", subdir)
    print(os.path.isdir(subdir))

    # if os.path.isdir(subdir):
    #     print("subdir exists")
    # else:
    #     # print("subdir does not exist")
    #     os.mkdir(subdir)
    #     print("created subdir")
    print("before : ", os.getcwd())
    os.chdir(subdir)
    # os.chdir(subdir + "/test")
    print("after : ", os.getcwd())


def demo_walk():
    # for item in os.walk("."):
    #     print(item)
    # for root, dirs, files in os.walk("."):
    #     print(root)
    #     print(dirs)
    #     print(files)
    # print(os.getcwd())
    # downloads_path = os.path.join('/Users/nigar/', 'Downloads')
    # print(os.path.isdir(downloads_path))
    for root, dirs, files in os.walk(".", topdown=True):
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
    file = os.path.join(cwd, "os_demo.py")
    print("file", file)
    print("file name", os.path.basename(file))
    print("dir", os.path.dirname(file))
    print("is it a file?", os.path.isfile(file))

    subdir = os.path.join(cwd, "subdir")
    print("is it a file? ", os.path.isfile(subdir))

    print(os.path.split(file))
    print(os.path.split(cwd))
    print(os.path.split(subdir))


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
    # demo_walk()
    demo_path_parts()
    # demo_file()
