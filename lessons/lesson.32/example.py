def act(name: str):
    w = weather()
    ex = exchange_rates()
    foo = bar()
    return {
        "w": w,
    }


def main():
    act("bob")
    act("john")


if __name__ == "__main__":
    main()
