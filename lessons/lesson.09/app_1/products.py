def create(name: str):
    print("creating product", name)
    return {"name": name, "params": ...}


def update(name: str, **kwargs):
    print("updating product", name, "with params", kwargs)
    return {"name": name, "params": kwargs}


def main():
    create("Tablet")
    create("Desktop")

    update("Desktop", description="Gaming PC")


if __name__ == "__main__":
    main()
