import csv

CARS_CSV = "cars.csv"
USERS_CSV_FILE = "users.csv"


def demo_read_csv_cars():
    with open(CARS_CSV) as f:
        csv_reader = csv.reader(f)
        # for row in csv_reader:
        #     print(row)
        print(next(csv_reader))

        for car in csv_reader:
            print(
                "<<",
                car[1],
                car[2],
                ">>",
                "year:",
                car[0],
                "price:",
                car[4],
            )


def demo_read_csv_cars_dict():
    with open(CARS_CSV) as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        for car in csv_reader:  # type: dict
            print(car)
            print(
                "<<",
                car["Make"],
                car["Model"],
                ">>",
                "year:",
                car["Year"],
                "price:",
                car["Price"],
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
    with open(USERS_CSV_FILE, "w") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        writer.writerow(
            {
                FieldName.username: "john",
                FieldName.email: "john@example.com",
                FieldName.phone: "+1-999,123",
            },
        )
        user_sam = {
            FieldName.username: "sam",
            FieldName.email: "sam@example.com",
            FieldName.phone: "111",
        }
        user_nick = {
            FieldName.username: "nick",
            FieldName.email: "nick@example.com",
            FieldName.phone: "333",
        }
        writer.writerows([user_sam, user_nick])


def main():
    # demo_read_csv_cars()
    # demo_read_csv_cars_dict()
    demo_write_csv()


if __name__ == "__main__":
    main()
