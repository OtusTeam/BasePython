from pathlib import Path

from pb import address_book_pb2


ADDRESS_BOOK_FILE = Path(__file__).parent / "address-book.txt"


def write() -> None:
    person = address_book_pb2.Person()
    person.id = 42
    person.name = "John Doe"
    person.email = "jdoe@example.com"

    phone_home = person.phones.add()
    phone_home.number = "555-4321"

    phone_mobile = person.phones.add()
    phone_mobile.number = "123-4321"
    phone_mobile.type = address_book_pb2.Person.PHONE_TYPE_MOBILE

    print(person)
    print(person.SerializeToString())
    with ADDRESS_BOOK_FILE.open("wb") as f:
        f.write(person.SerializeToString())


def read() -> None:
    person = address_book_pb2.Person()
    print("person is initialized (before):", person.IsInitialized())
    with ADDRESS_BOOK_FILE.open("rb") as f:
        person.ParseFromString(f.read())
    print("person is initialized (after):", person.IsInitialized())
    print(person)


def main() -> None:
    # write()
    read()


if __name__ == "__main__":
    main()

