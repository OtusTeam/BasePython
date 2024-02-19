def main():
    line = "Hello World!"
    print(line)
    print(list(line))
    for char in line:
        if char.isupper():
            print(char)

    print(str.isupper("H"))
    print(str.isupper("h"))
    print(list(map(str.isupper, line)))
    print(list(filter(str.isupper, line)))


if __name__ == "__main__":
    main()
