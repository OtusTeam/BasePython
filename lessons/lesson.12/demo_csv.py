import csv

CARS_CSV_FILE = "cars.csv"
BIRTH_MONTH_CSV_FILE = "births.csv"


def read_csv_cars():
    with open(CARS_CSV_FILE) as f:
        csv_reader = csv.reader(f, delimiter=",")

        # print(dir(csv_reader))
        # print(csv_reader)
        # print(*csv_reader)
        # f.seek(0)
        for line in csv_reader:
            print(line)
            print(line[1], line[4])


def read_csv_cars_as_dict():
    with open(CARS_CSV_FILE) as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        # csv_reader = csv.DictReader(f, fieldnames=['Year', 'Make', 'Model', 'Description', 'Price'], delimiter=",", )
        print("fieldnames", csv_reader.fieldnames)

        for row in csv_reader:
            print(row)
            # print(row["Make"], row["Year"], row["Price"])


class FieldName:
    NAME = "name"
    MONTH = "month"
    DEPARTMENT = "department"


def write_csv_dict():
    fieldnames = [
        FieldName.NAME,
        FieldName.MONTH,
        FieldName.DEPARTMENT,
    ]
    with open(BIRTH_MONTH_CSV_FILE, "w") as f:
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()

        row = {
            FieldName.DEPARTMENT: "IT",
            FieldName.NAME: "John",
            FieldName.MONTH: "June",
        }
        csv_writer.writerow(row)

        row1 = {
            FieldName.MONTH: "July",
            FieldName.NAME: "Ann",
            FieldName.DEPARTMENT: "HR",
        }
        row2 = {
            FieldName.DEPARTMENT: "Accounting",
            FieldName.NAME: "Alice",
            FieldName.MONTH: "November",
        }
        csv_writer.writerows([row1, row2])


def main():
    # read_csv_cars()
    # read_csv_cars_as_dict()
    write_csv_dict()


if __name__ == "__main__":
    main()
