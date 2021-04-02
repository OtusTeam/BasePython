import os


def walk_through_files():
    # for item in os.walk("."):
    #     print(item)
    # current dir, nested dirs, files
    for root, dirs, files in os.walk(".."
                                     # , topdown=False
                                     ):
        print("-*", root)
        for dir_ in dirs:
            print("--", dir)
            for filename in files:
                print("---", filename)


walk_through_files()
