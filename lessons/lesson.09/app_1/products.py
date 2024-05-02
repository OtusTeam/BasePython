def create(name):
    print("create product", name)
    return {"product": name}


def update(name, **params):
    print("update product", name, "params", params)
    return {"product": name, "params": params}


def main():
    create("Tablet")
    create("Laptop")

    update("Laptop", description="Gaming Laptop")


with open("/dev/random", "rb") as f:
    product_key_id = f.read(10)


if __name__ == "__main__":
    main()
