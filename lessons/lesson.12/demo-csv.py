import csv

CARS_FILE = "cars.csv"
USERS_FILE = "users.csv"


def demo_read_csv():
    with open(CARS_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            print(row[1], row[2], "for", row[4])


def demo_read_csv_as_dict():
    # , encoding="windows-1251"
    with open(CARS_FILE, "r") as file:
        csv_reader = csv.DictReader(file)
        print("fieldnames:", csv_reader.fieldnames)
        for row in csv_reader:
            # print(row)
            print(row["Make"], row["Model"], "for", row["Price"])


class FieldNames:
    USERNAME = "username"
    EMAIL = "email"
    PHONE = "phone"


def demo_write_csv():
    field_names = [
        FieldNames.USERNAME,
        FieldNames.EMAIL,
        FieldNames.PHONE,
    ]
    with open(USERS_FILE, "w") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()

        writer.writerow({
            FieldNames.PHONE: "995123",
            FieldNames.EMAIL: "sam@example.com",
            FieldNames.USERNAME: "sam",
        })

        users_info = [
            {
                FieldNames.EMAIL: "john+abc@google.com",
                FieldNames.USERNAME: "john",
                FieldNames.PHONE: "+99 99, 123",
            },
            {
                FieldNames.USERNAME: "kate",
                FieldNames.PHONE: "+098765",
                FieldNames.EMAIL: "kate@yahoo.com",
            },
        ]
        writer.writerows(users_info)


def main():
    # demo_read_csv()
    # demo_read_csv_as_dict()
    demo_write_csv()


if __name__ == "__main__":
    main()
