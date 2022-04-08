import csv


CARS_CSV_FILE_NAME = "cars.csv"


def read_csv_cars():
    with open(CARS_CSV_FILE_NAME) as f:
        # for line in f:
        #     print(repr(line))
        csv_reader = csv.reader(f, delimiter=",")
        # for row in csv_reader:
            # print(row)
        for index, row in enumerate(csv_reader):
            if index == 0:
                print("Headers:", " | ".join(row))
            else:
                print("Car by {vendor}, model {model!r}, for {price}".format(
                    vendor=row[1],
                    model=row[2],
                    price=row[4],
                ))


def read_csv_as_dict():
    with open(CARS_CSV_FILE_NAME) as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        print("Headers:", " | ".join(csv_reader.fieldnames))
        for row in csv_reader:
            # print(row)
            print("Car by {vendor}, model {model!r}, for {price}".format(
                vendor=row["Make"],
                model=row["Model"],
                price=row["Price"],
            ))


class FieldNames:
    NAME = "name"
    DEPARTMENT = "department"
    MONTH = "month"


def write_csv_dict():
    fieldnames = [
        FieldNames.NAME,
        FieldNames.DEPARTMENT,
        FieldNames.MONTH,
    ]
    # "/home/suren/Documents/file.csv"
    with open("employees_bd_months.csv", "w") as f:
        csv_writer = csv.DictWriter(f, fieldnames)
        csv_writer.writeheader()

        row = {
            FieldNames.NAME: "John",
            FieldNames.DEPARTMENT: "IT",
            FieldNames.MONTH: "March",
        }
        csv_writer.writerow(row)

        row2 = {
            FieldNames.NAME: "Sam",
            FieldNames.MONTH: "June",
            FieldNames.DEPARTMENT: "HelpDesk"
        }
        row3 = {
            FieldNames.DEPARTMENT: "Accounting",
            FieldNames.MONTH: "February",
            FieldNames.NAME: "Ann",
        }
        rows = [
            row2,
            row3,
        ]
        csv_writer.writerows(rows)


def main():
    # read_csv_cars()
    # read_csv_as_dict()
    write_csv_dict()


if __name__ == "__main__":
    main()
