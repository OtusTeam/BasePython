import csv


def read_csv_cars():
    with open("cars.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for line, row in enumerate(csv_reader):
            if line == 0:
                print("Columns:", " | ".join(row))
            else:
                print("Car by {vendor} name {name!r} for {price}".format(
                    vendor=row[1],
                    name=row[2],
                    price=row[4],
                ))


def read_csv_cars_as_dict():
    print("Read CSV as dict")
    with open("cars.csv") as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        print("Columns:", " | ".join(csv_reader.fieldnames))
        for row in csv_reader:
            print("Car by {vendor} name {name!r} for {price}".format(
                vendor=row["Make"],
                name=row["Model"],
                price=row["Price"],
            ))


class FieldNames:
    NAME = "name"
    DEPARTMENT = "department"
    MONTH = "month"

    @classmethod
    def get_fields(cls):
        return [
            cls.NAME,
            cls.DEPARTMENT,
            cls.MONTH,
        ]

    # def smth(self):
    #     return self.DEPARTMENT


def write_csv_dict():

    fieldnames = FieldNames.get_fields()

    with open("employees_birth_months.csv", "w") as f:
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()

        csv_writer.writerow({
            FieldNames.NAME: "John",
            FieldNames.MONTH: "May",
            FieldNames.DEPARTMENT: "IT",
        })

        csv_writer.writerow({
            FieldNames.NAME: "Adam",
            FieldNames.MONTH: "June",
            FieldNames.DEPARTMENT: "HelpDesk",
        })


def main():
    # read_csv_cars()
    # read_csv_cars_as_dict()
    write_csv_dict()


if __name__ == '__main__':
    main()
