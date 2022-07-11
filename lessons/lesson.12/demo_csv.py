"""
CSV - comma separated values
"""

import csv

CARS_CSV_FILE = "cars.csv"
BIRTH_MONTHS_CSV_FILE = "birth_months.csv"


def read_csv_cars():
    with open(CARS_CSV_FILE) as f:
        csv_reader = csv.reader(f, delimiter=",")

        for line in csv_reader:
            print(line)
            print(line[1], line[4])


def read_csv_dict_cars():
    with open(CARS_CSV_FILE) as f:
        csv_reader = csv.DictReader(f, delimiter=",")

        print("headers:", csv_reader.fieldnames)

        for row in csv_reader:
            # print(row)
            print(row["Make"], row["Year"], row["Price"])


class FieldNames:
    NAME = "name"
    MONTH = "month"
    DEPARTMENT = "department"


def write_csv_dict():
    fieldnames = [FieldNames.NAME, FieldNames.MONTH, FieldNames.DEPARTMENT]
    with open(BIRTH_MONTHS_CSV_FILE, "w") as f:
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()

        row = {
            FieldNames.NAME: "John",
            FieldNames.DEPARTMENT: "IT",
            FieldNames.MONTH: "May",
        }
        csv_writer.writerow(row)

        row2 = {
            FieldNames.DEPARTMENT: "HelpDesk",
            FieldNames.MONTH: "March",
            FieldNames.NAME: "Sam",
        }
        row3 = {
            FieldNames.MONTH: "Feb",
            FieldNames.NAME: "Carl",
            FieldNames.DEPARTMENT: "Accounting",
        }

        rows = [row2, row3]
        csv_writer.writerows(rows)


def main():
    read_csv_cars()
    read_csv_dict_cars()
    write_csv_dict()


if __name__ == '__main__':
    main()
