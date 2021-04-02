import os


def print_os():
    print(os.name)
    print(os.environ)
    print(os.getcwd())
    # current working directory
    # os.chdir('../')
    # "C://" + "Users" + r"\\" + "admin" + "\\\\" + "Downloads"
    # "/" + "home" + "/" + "Users" + "/" + "admin" + "/" + "Downloads"
    subdir = os.path.join(os.getcwd(), "subdir")
    print(subdir)
    if os.path.isdir(subdir):
        print("Subdir exists")
    else:
        os.mkdir(subdir)
        print("Subdir is created")
    os.chdir(subdir)
    print(os.getcwd())

print_os()
