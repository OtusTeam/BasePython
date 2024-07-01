import products as p
import users as u


def main():
    print("Hello main!")
    print("Users magic const:", u.USERS_MAGIC_CONST)
    bob = u.create("Bob")
    alice = u.create("Alice")

    u.update("Bob", email="bob@abc.com")

    u.delete("Alice")

    p.create("Smartphone")
    p.create("Laptop")
    p.update("Laptop", description="Lightest Laptop")


if __name__ == "__main__":
    main()
