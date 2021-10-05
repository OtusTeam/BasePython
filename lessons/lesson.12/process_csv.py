import csv


def read_csv_cars():
    with open("cars.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")
        # for row in csv_reader:
        #     print(row)
        for line, row in enumerate(csv_reader):
            if line == 0:
                print("Columns:", " | ".join(row))
            else:
                print(
                    "Car by {vendor} name {name!r} for {price}".format(
                        vendor=row[1],
                        name=row[2],
                        price=row[4],
                    )
                )


def read_csv_cars_as_dict():
    with open("cars.csv") as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        print("Columns:", " | ".join(csv_reader.fieldnames))
        for row in csv_reader:
            # print(row)
            print(
                "Car by {vendor} name {name!r} for {price}".format(
                    vendor=row["Make"],
                    name=row["Model"],
                    price=row["Price"],
                )
            )


def write_csv_dict():
    FIELD_NAME = "name"
    FIELD_DEPARTMENT = "department"
    FIELD_MONTH = "month"

    fieldnames = [
        FIELD_NAME,
        FIELD_DEPARTMENT,
        FIELD_MONTH,
    ]
    with open("emoloyees_birth_months.csv", "w") as f:
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()

        csv_writer.writerow({
            FIELD_MONTH: "May",
            FIELD_DEPARTMENT: "IT",
            FIELD_NAME: "John Smith",
        })

        csv_writer.writerow({
            FIELD_NAME: "Sam White",
            FIELD_DEPARTMENT: "Helpdesk",
            FIELD_MONTH: "November",
        })

        # csv_writer.writerows()


def main():
    # read_csv_cars()
    # read_csv_cars_as_dict()
    write_csv_dict()


if __name__ == '__main__':
    main()
