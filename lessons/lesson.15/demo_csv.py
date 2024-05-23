import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

CARS_FILE = BASE_DIR / "cars.csv"
USERS_FILE = BASE_DIR / "users.csv"


def demo_read_csv_cars():
    with CARS_FILE.open() as f:
        csv_reader = csv.reader(f)
        print(next(csv_reader))
        for car in csv_reader:
            print(
                "<<", car[1], car[2], ">>",
                "year:", car[0],
                "price:", car[4],
            )


def demo_read_csv_cars_as_dict():
    with CARS_FILE.open() as f:
        # , fieldnames=("name", "year", "price")
        csv_reader = csv.DictReader(f, delimiter=",")
        for car in csv_reader:  # type: dict
            print(
                "<<", car["Make"], car["Model"], ">>",
                "year:", car["Year"],
                "price:", car["Price"],
            )


class FieldName:
    username = "username"
    email = "email"
    phone = "phone"


def demo_write_csv():
    fieldnames = [
        FieldName.username,
        FieldName.email,
        FieldName.phone,
    ]
    # print("fieldnames", fieldnames)
    with USERS_FILE.open("w") as f:
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()

        csv_writer.writerow({
            FieldName.username: "bob",
            FieldName.email: "bob@example.com",
            FieldName.phone: "555-555-5555",
        })

        user_sam = {
            FieldName.email: "sam@example.com",
            FieldName.phone: "333-333-5555",
            FieldName.username: "sam",
        }
        user_alice = {
            FieldName.phone: "777-777-5555",
            FieldName.username: "alice",
            FieldName.email: "alice@example.com",
        }
        csv_writer.writerows([user_sam, user_alice])


def main():
    demo_read_csv_cars()
    demo_read_csv_cars_as_dict()
    demo_write_csv()


if __name__ == "__main__":
    main()
