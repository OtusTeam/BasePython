import csv


def read_csv_cars():
    with open("cars.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")
        print(csv_reader)
        lines_count = 0
        for row in csv_reader:
            # print(row)
            # continue
            if lines_count == 0:
                print("Columns:", " | ".join(row))
            else:
                # print(*row)
                print(f"Car by {row[1]} ({row[0]}) {row[2]!r} for {row[4]}")

            lines_count += 1
            # print(row)
        print("rows count:", lines_count)


def read_csv_cars_as_dict():
    with open("cars.csv") as f:
        csv_reader = csv.DictReader(f)
        print(csv_reader)
        lines_count = 0
        for row in csv_reader:
            # print(row)
            if lines_count == 0:
                print("Columns:", " | ".join(row))
            print(f"Car by {row['vendor']} ({row['year']})"
                  f" {row['name']!r} for {row['price']}")
            lines_count += 1

        print("rows count:", lines_count)


def write_csv_dict():
    FIELD_NAME = "name"
    FIELD_DEPARTMENT = "department"
    FIELD_MONTH = "birth month"

    fieldnames = [
        FIELD_NAME,
        FIELD_DEPARTMENT,
        FIELD_MONTH,
    ]
    with open("employee_birth_months.csv", "w") as f:
        csv_writer = csv.DictWriter(
            f,
            fieldnames=fieldnames,
            # delimiter=",",
            # quotechar='"',
            # quoting=csv.QUOTE_MINIMAL,
        )

        csv_writer.writeheader()

        csv_writer.writerow({
            FIELD_NAME: "Sam White",
            FIELD_DEPARTMENT: "Helpdesk",
            FIELD_MONTH: "7",
        })
        csv_writer.writerow({
            FIELD_NAME: "John Smith",
            FIELD_DEPARTMENT: "IT",
            FIELD_MONTH: "1",
        })
        csv_writer.writerow({
            FIELD_NAME: "Ann Black",
            FIELD_DEPARTMENT: "Accountant, Manager",
            FIELD_MONTH: "12",
        })


def read_csv_birth_months_as_dict():
    with open("employee_birth_months.csv") as f:
        csv_reader = csv.DictReader(f)
        # print(csv_reader)
        for row in csv_reader:
            print(row)


def main():
    # read_csv_cars()
    # read_csv_cars_as_dict()
    # write_csv_dict()
    read_csv_birth_months_as_dict()


if __name__ == '__main__':
    main()
