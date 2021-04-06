import csv
from contextlib import contextmanager


def read_csv_cars():
    with open("cars.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")
        print(csv_reader)
        # line = 0
        for line, row in enumerate(csv_reader):
            # print(line, row)
            if line == 0:
                print("Columns:", " | ".join(row))
            else:
                print("Car {vendor} {name} ({year} y) ${price}".format(
                    vendor=row[1],
                    name=row[2],
                    year=row[0],
                    price=row[4],
                ))
            # line += 1


@contextmanager
def open_with_close(filename):
    f = open(filename)
    print("Opened file", filename)
    try:
        print("yielded file", filename)
        yield f
        print("successfully finished working with", filename)
    finally:
        f.close()
        print("closed", filename)


def read_csv_cars_as_dict():
    with open_with_close("cars.csv") as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        print(csv_reader)
        print("Columns:", " | ".join(csv_reader.fieldnames))
        for row in csv_reader:
            # print(row)
            print("Car {vendor} {name} ({year} y) ${price}".format(
                vendor=row['vendor'],
                name=row['name'],
                year=row['year'],
                price=row['price'],
            ))

    # f = open('file.csv')
    # f.readline()
    # f.close()


def write_csv_dict():
    FIELD_NAME = "name"
    FIELD_DEPARTMENT = "department"
    FIELD_MONTH = "month"

    fieldnames = [
        FIELD_NAME,
        FIELD_DEPARTMENT,
        FIELD_MONTH,
    ]
    with open("employees_birth_months.csv", "w") as f:
        csv_writer = csv.DictWriter(
            f,
            fieldnames=fieldnames,
        )
        csv_writer.writeheader()
        csv_writer.writerow({
            FIELD_NAME: "John",
            FIELD_DEPARTMENT: "Helpdesk",
            FIELD_MONTH: "November",
        })
        csv_writer.writerow({
            FIELD_NAME: "Henry",
            FIELD_DEPARTMENT: "IT",
            FIELD_MONTH: "August",
        })
        csv_writer.writerow({
            FIELD_NAME: "Ann",
            FIELD_DEPARTMENT: "Accounting",
            FIELD_MONTH: "May",
        })


def read_by_line():
    with open_with_close('file.csv') as f:
        # len(f.readlines())  - no
        for line in f:
            print(repr(line))
            if 'Chevy' in line:
                print('stop processing')
                break


if __name__ == '__main__':
    # read_csv_cars()
    # read_csv_cars_as_dict()
    # write_csv_dict()
    read_by_line()
