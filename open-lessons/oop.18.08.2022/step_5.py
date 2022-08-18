class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        # self.__demo_hidden = "super secret!!"

    def copy(self):
        return Date(year=self.year, month=self.month, day=self.day)

    @classmethod
    def from_date_string(cls, date_string: str):
        """
        Parse date from string '2022-08-18'

        :param date_string:
        :return:
        """
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
        return (
            f"{self.__class__.__name__}(year={self.year}, "
            f"month={self.month}, day={self.day})"
        )


# Date.is_date_string_valid()


print(Date)
print(Date.__name__)


date1 = Date(2022, 8, 18)
date2 = Date(1934, 3, 24)

print(date1)
print(date2)

date3 = date1
print(date3)
print(date1)
date3.month = 1
date1.year = 2000

print(date3)
print(date1)

date4 = date1.copy()
print("---")
print(date1)
print(date4)

date1.year = 2002
date4.day = 22
date4.month = 2
print(date1)
print(date4)

print('***')

# date5 = date4.from_date_string("")
date5 = Date.from_date_string("2048-11-22")
print(date5)

print(Date.is_date_string_valid("200"))
print(Date.is_date_string_valid("2048-11-22"))
print(Date.is_date_string_valid("4048-11-22"))
print(Date.is_date_string_valid("2048-11-31"))

# Date.copy(date4)
# date4.copy()


# print(date1.__dict__)
# # print(date1.__demo_hidden)
# print(date2._Date__demo_hidden)
# date2._Date__demo_hidden = "not secret!"
# print(date2._Date__demo_hidden)
# print(date2.__dict__)
