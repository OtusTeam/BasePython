import csv

CARS_FILE = "cars.csv"
USERS_FILE = "users.csv"


def demo_read_csv():
    with open(CARS_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            print(row[0], row[1], "price:", row[4])
            # print(row[3].replace("\n", " + "))
            print(row[3])
            print()


def demo_read_csv_dict():
    with open(CARS_FILE, "r") as file:
        reader = csv.DictReader(file)
        print("field names:", reader.fieldnames)
        for row in reader:  # type: dict
            print(row)  
            print(row["Year"], row["Make"], "Price:", row["Price"])
            print(row["Description"])
            print()

            # print(row[0], row[1], "price:", row[4])
            # # print(row[3].replace("\n", " + "))
            # print(row[3])
            # print()


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
            FieldNames.USERNAME: "john",
            FieldNames.EMAIL: "john@example.com",
            FieldNames.PHONE: "999",
        })

        user_sam = {
            FieldNames.PHONE: "333",
            FieldNames.USERNAME: "sam",
            FieldNames.EMAIL: "sam@yahoo.com",
        }
        user_nick = {
            FieldNames.EMAIL: "nick@ya.ru",
            FieldNames.PHONE: "555",
            FieldNames.USERNAME: "nick",
        }
        users = [user_sam, user_nick]
        writer.writerows(users)


def main():
    # demo_read_csv()
    # demo_read_csv_dict()
    demo_write_csv()


if __name__ == "__main__":
    main()

