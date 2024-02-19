def rnd_numbers_generator():
    print("Generating random numbers...")
    # rolled a dice
    yield 6
    print("Also, there's another random number")
    # rolled a dice
    yield 5
    # return "done"
    yield
    yield 4


print("")

# def rnd_numbers_generator():
#     return 1
#     print("Generating random numbers...")
#     # rolled a dice
#     if False:
#         yield 6


def main():
    rnd_g = rnd_numbers_generator()
    for n in rnd_g:
        print("got:", n)

    print("One more time")
    rnd_g = rnd_numbers_generator()

    print(rnd_g)
    print(next(rnd_g))
    print("pause...")
    print(next(rnd_g))
    print("another pause...")
    print(next(rnd_g))
    print("try again!")
    print(next(rnd_g))


if __name__ == "__main__":
    main()
