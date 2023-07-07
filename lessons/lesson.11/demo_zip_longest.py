from itertools import zip_longest


def main():
    names = [
        "John",
        "Sam",
        "Bob",
        "Nick",
        "Kyle",
    ]
    activities = [
        "wash dishes",
        "make bed",
        "watch tv",
        "play games",
    ]
    for name, activity in zip_longest(names, activities, fillvalue="rest"):
        print(name, activity)


if __name__ == '__main__':
    main()
