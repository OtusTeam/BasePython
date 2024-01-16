import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent
CARS_FILE = BASE_DIR / "cars.csv"
USERS_FILE = BASE_DIR / "users.csv"


def read_cars_csv():
    with open(CARS_FILE, "r") as file:
        for row in file:
            # print(row, end="|")
            print(repr(row))

        file.seek(0)
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
            # print("year:", row[0], 'make:', row[1], "model", row[2], "price:", row[4])
            print(row[0], row[1], row[2], "price:", row[4])


def read_cars_csv_dict():
    with open(CARS_FILE, "r") as file:
        # reader = csv.DictReader(file, delimiter=",")
        reader = csv.DictReader(file)
        print("headers:", reader.fieldnames)
        for row in reader:
            print(row)
            print(row["Year"], row["Make"], row["Model"], "price:", row["Price"])
            print(row["Description"])


class FieldNames:
    FULL_NAME = "full name"
    EMAIL = "email"
    PHONE = "phone"


def write_csv_dict():
    fieldnames = [
        FieldNames.FULL_NAME,
        FieldNames.EMAIL,
        FieldNames.PHONE,
    ]
    with open(USERS_FILE, "w") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        row = {
            FieldNames.FULL_NAME: "John Smith",
            FieldNames.EMAIL: "john@example.com",
            FieldNames.PHONE: "1234",
        }
        writer.writerow(row)
        writer.writerows([
            {
                FieldNames.PHONE: "23412",
                FieldNames.FULL_NAME: "Sam White",
                FieldNames.EMAIL: "sam@example.com",
            },
            {
                FieldNames.EMAIL: "bob@example.com",
                FieldNames.PHONE: "5342",
                FieldNames.FULL_NAME: "Bob Black, Dr.",
            },
        ])


def main():
    # read_cars_csv()
    # read_cars_csv_dict()
    write_csv_dict()


if __name__ == "__main__":
    main()
