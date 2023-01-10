import os

dir_path = '.'
for root, dirs, files in os.walk(dir_path):
    # for el in dirs:
    #     _dir_path = os.path.abspath(os.path.join(root, el))
    #     print(_dir_path, os.path.isdir(_dir_path))
    for el in files:
        f_path = os.path.join(root, el)
        print(f_path)



