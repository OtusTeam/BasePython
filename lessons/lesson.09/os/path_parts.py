import os


def path_parts():
    cwd = os.getcwd()
    print(cwd)
    print(os.path.basename(cwd))
    print(os.path.dirname(cwd))
    file = os.path.join(cwd, "os.py")
    print(os.path.isfile(file))
    print(os.path.split(file))
    print(os.path.split(cwd))


path_parts()
