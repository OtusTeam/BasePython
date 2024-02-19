fruits = ["apple", "banana", "peach", "grape", "orange"]


def combine_fruits():
    for f1 in fruits:
        for f2 in fruits:
            print("-- generate pair", f1, f2)
            yield f1, f2


# def combine_fruits():
#     result = []
#     for f1 in fruits:
#         for f2 in fruits:
#             result.append((f1, f2))
#     return result


def main():
    # print(combine_fruits())
    for f1, f2 in combine_fruits():
        if "an" in f1 and "g" in f2:
            print("found!", f1, f2)
            # break


if __name__ == "__main__":
    main()
