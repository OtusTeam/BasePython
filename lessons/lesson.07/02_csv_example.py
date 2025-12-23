import csv
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
csv_dir = CURRENT_DIR / "csv-files"

print(csv_dir, "is dir", csv_dir.is_dir())

cars_csv = csv_dir / "cars.csv"
birthdays_csv = csv_dir / "birthdays.csv"

# with cars_csv.open() as file:
#     for line in file:
#         print(f"current line: {line!r}")


def demo_csv_read_cars():
    with cars_csv.open() as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # print(row)
            print(
                "<<",
                row[1],
                row[2],
                ">> (",
                row[0],
                ")",
                repr(row[3]),
                "for only",
                row[4],
            )


def demo_csv_read_cars_as_dict():
    with cars_csv.open() as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # print(row)
            print(
                "<<",
                row["Make"],
                row["Model"],
                ">> (",
                row["Year"],
                ")",
                repr(row["Description"]),
                "for only",
                row["Price"],
            )


class FieldsNames:
    NAME = "Full name"
    DEPARTMENT = "Department"
    BIRTH_DATE = "Birth Date"


def demo_write_csv():
    fieldnames = [
        FieldsNames.NAME,
        FieldsNames.DEPARTMENT,
        FieldsNames.BIRTH_DATE,
    ]
    with birthdays_csv.open("w") as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()

        csv_writer.writerow(
            {
                FieldsNames.NAME: "John Smith",
                FieldsNames.DEPARTMENT: "IT",
                FieldsNames.BIRTH_DATE: "1990-01-01",
            }
        )

        csv_writer.writerows(
            [
                {
                    FieldsNames.DEPARTMENT: "Helpdesk",
                    FieldsNames.NAME: "Bob Black",
                    FieldsNames.BIRTH_DATE: "1985-11-21",
                },
                {
                    FieldsNames.BIRTH_DATE: "1991-12-25",
                    FieldsNames.DEPARTMENT: "Accounting",
                    FieldsNames.NAME: "Alice White",
                },
            ]
        )


# demo_csv_read_cars()
# demo_csv_read_cars_as_dict()
demo_write_csv()
