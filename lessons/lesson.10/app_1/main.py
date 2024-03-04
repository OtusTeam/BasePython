import users
import products

# import by real name
import items_processor


def main():
    print("Hello main!")

    users.create("Nick")
    users.create("Bob")

    users.update("Nick", age=20, city="New York")
    users.update("Bob", email="bob@example.com", job="Software Engineering")

    products.create("Laptop")
    products.create("Tablet")

    print(items_processor)
    print(items_processor.ItemsProcessor)
    print(items_processor.ItemsProcessor())


if __name__ == "__main__":
    main()
