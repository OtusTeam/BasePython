import os

def demo_os_base():
    print(os.name)
    print(os.environ)
    print(os.environ["PATH"])
    print(os.environ["HOME"])
    print(os.environ["PYTHONUNBUFFERED"])
    print(os.environ["SECRET_KEY"])
    print(os.environ.get("SECRET_KEY"))
    print(os.environ.get("SECRET_KEY_2"))

    # get current working directory
    cwd = os.getcwd()
    print(cwd)

    subdir = os.path.join(cwd, "subdir")
    print("subdir:", subdir)
    if os.path.isdir(subdir):
        print("subdir already exists")
    else:
        os.mkdir(subdir)
        print("created subdir")
        # os.makedirs()

    os.chdir(subdir)
    print(os.getcwd())


def demo_file():
    filename = "file.txt"
    with open(filename, "w"):
        pass

    print(os.listdir("."))

    # os.remove()
    os.unlink(filename)

    # res = os.system("ls -la")
    # print("res:", res)

    print(os.stat("."))


def demo_walk():
    for root, dirs, files in os.walk(".", topdown=False):
        print("root:", root)
        print("dirs:")
        for d in dirs:
            print("-", d)
        print("files:")
        for f in files:
            print("-", f)


cwd = os.getcwd()
print("cwd:", cwd)
print("base name cwd:", os.path.basename(cwd))
print("dir name cwd:", os.path.dirname(cwd))

print(os.path.exists(cwd))
file_path = os.path.join(cwd, "filename.txt")
print(os.path.split(file_path))

print("base name file_path:", os.path.basename(file_path))
print("dir name file_path:", os.path.dirname(file_path))
