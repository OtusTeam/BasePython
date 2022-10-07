import csv


def read_csv_cars():
    with open("employees_bd_months.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for line_number, row in enumerate(csv_reader):
            print(" | ".join(row))
            # if line_number == 0:
            #     print(" | ".join(row))
            # else:
            #     print("{} | {} | {}".format(*row))


def read_csv_cars_as_dict():
    with open("employees_bd_months.csv") as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        print("Columns:", " | ".join(csv_reader.fieldnames))
        for row in csv_reader:
            # print(row)
            # print("Employer {name}, department: {department} - {month}".format(
            #     name=row["name"],
            #     department=row["department"],
            #     month=row["month"],
            # ))
            print("Employer {name}, department: "
                  "{department} - {month}".format(**row))


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
    with open("employees_bd_months.csv", "w") as f:
        csv_writer = csv.DictWriter(f, fieldnames)
        csv_writer.writeheader()

        row = {
            FieldNames.NAME: "John",
            FieldNames.DEPARTMENT: "HelpDesk",
            FieldNames.MONTH: "February",
        }
        csv_writer.writerow(row)

        row2 = {
            FieldNames.NAME: "Jack",
            FieldNames.DEPARTMENT: "IT",
            FieldNames.MONTH: "March",
        }
        row3 = {
            FieldNames.NAME: "Ann",
            FieldNames.DEPARTMENT: "Accounting",
            FieldNames.MONTH: "May",
        }
        csv_writer.writerows([row2, row3])


def main():
    read_csv_cars()
    # read_csv_cars_as_dict()
    # write_csv_dict()


if __name__ == "__main__":
    main()
