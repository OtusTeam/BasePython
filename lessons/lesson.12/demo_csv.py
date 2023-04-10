import csv

FILENAME = "cars.csv"
USERS_FILE = "users.csv"


def demo_read_csv():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for not_first, row in enumerate(reader):
            if not_first:
                # print(row)
                print(row[1], row[2], row[0], "y.")
            else:
                print("row headers:", row)


def demo_read_csv_dict():
    with open(FILENAME, "r") as file:
        csv_reader = csv.DictReader(file, delimiter=",")

        print("headers:", csv_reader.fieldnames)
        for row in csv_reader:
            # print(row)
            print(row["Make"], row["Model"], row["Year"], "y.")


class FieldNames:
    USERNAME = "username"
    EMAIL = "email"
    REG_DATE = "date registered"


def write_csv():
    fieldnames = [
        FieldNames.USERNAME,
        FieldNames.EMAIL,
        FieldNames.REG_DATE,
    ]

    # file = open(USERS_FILE, "w")
    # file.write()
    # 1/0
    # file.close()
    with open(USERS_FILE, "w") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        user_info = {
            FieldNames.USERNAME: "john",
            FieldNames.EMAIL: "john@example.com",
            FieldNames.REG_DATE: "2023-11-30",
        }
        writer.writerow(user_info)

        users_info = [
            {
                FieldNames.REG_DATE: "2023-10-20",
                FieldNames.EMAIL: "sam@example.com",
                FieldNames.USERNAME: "sam",
            },
            {
                FieldNames.EMAIL: "kate@example.com",
                FieldNames.REG_DATE: "2023-09-10",
                FieldNames.USERNAME: "kate",
            },
        ]
        writer.writerows(users_info)


def main():
    # demo_read_csv()
    # demo_read_csv_dict()
    write_csv()


if __name__ == '__main__':
    main()
