from src.func import x


def print_hi(name):
    # from src.func import x

    print(f'Hi, {name}, {x=}')  # Press Ctrl+F8 to toggle the breakpoint.
    from src.func import x
    print(f'Hi, {name}, {x=}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
