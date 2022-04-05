import os


def demo_cwd():
    # current working directory
    cwd = os.getcwd()
    print("cwd", cwd)
    print(__file__)
    print(os.path.dirname(__file__))
    # os.chmod()


if __name__ == "__main__":
    demo_cwd()
