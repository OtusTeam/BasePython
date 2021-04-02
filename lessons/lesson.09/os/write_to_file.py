import os


def write_to_file():
    cwd = os.getcwd()
    file_path = os.path.join(cwd, "file.txt")
    f = open(file_path, "w")
    f.write("Hello")
    # data = f.read()
    f.close()


def with_open_file():
    cwd = os.getcwd()
    file_path = os.path.join(cwd, "file.txt")

    with open(file_path, 'r') as file:
        print(file.read())


write_to_file()
with_open_file()
