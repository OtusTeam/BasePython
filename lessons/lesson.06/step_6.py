class Date:
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def copy(self):
        # date = self.__class__(...)
        date = Date(year=self.year, month=self.month, day=self.day)
        return date

    @classmethod
    def from_date_string(cls, date_string: str):
        """
        Accepts date string like 2022-06-15
        :param date_string:
        :return:
        """
        # year, month, day = date_string.split("-")
        # year = int(year)
        # month = int(month)
        # day = int(day)
        year, month, day = map(int, date_string.split("-"))
        date = cls(year=year, month=month, day=day)
        return date

    @staticmethod
    def is_date_string_valid(date_string: str):
        if date_string.count("-") != 2:
            return False

        year, month, day = map(int, date_string.split("-"))
        return day <= 31 and month <= 12 and year <= 3999

    def __str__(self):
        return f"Date(year={self.year}, month={self.month}, day={self.day})"


# copy example

date1 = Date(2022, 6, 22)
print("date1:", date1)


date2 = date1
print("date2:", date2)

date2.day = 13
date1.month = 1
print("date1:", date1)
print("date2:", date2)

print("date1 is date2:", date1 is date2)

date3 = date1.copy()
print("date3", date3)

date3.year = 2021
date1.month = 3
print("date1:", date1)
print("date2:", date2)
print("date3", date3)

# from str example


date1 = Date.from_date_string("2022-06-22")
print(date1)

print("valid 1:", Date.is_date_string_valid("2022-06-22"))
print("valid 2:", Date.is_date_string_valid("2022-15-22"))
print("valid 3:", Date.is_date_string_valid("2022-1-32"))

# date1.from_date_string("...")
# date1.copy()

# date4 = Date.copy(date1)
date4 = date1.copy()
# date1.Date = Date
# date1.Date()
