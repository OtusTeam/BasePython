# from datetime import datetime, date !!!!!!!

class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    # def __init__(self, date_string):
    #     year, month, day = date_string(...)
    #     self.year = year
    #     self.month = month
    #     self.day = day

    @classmethod
    def from_date_string(cls, date_string: str):
        """
        accepts strings like '2022-11-25'
        :param date_string:
        :return:
        """

        year, month, day = map(int, date_string.split("-"))
        return cls(year=year, month=month, day=day)
        # return cls(*map(int, date_string.split("-")))

    @staticmethod
    def is_date_string_valid(date_string: str) -> bool:
        if date_string.count("-") != 2:
            return False
        # return ""
        year, month, day = map(int, date_string.split("-"))
        return day <= 31 and month <= 12 and year <= 3999

    def copy(self):
        # return Date()
        return self.__class__(
            year=self.year,
            month=self.month,
            day=self.day,
        )

    def __str__(self):
        return (
            f"{self.__class__.__name__}(year={self.year}, "
            f"month={self.month}, day={self.day})"
        )


d1 = Date(2001, 4, 30)
print("d1:", d1)

d2 = Date(2002, 2, 22)
print("d2:", d2)

d3 = d2

print("d2:", d2)
print("d3:", d3)

d1.month = 6
d2.year = 2004
d3.day = 5

print("d1:", d1)
print("d2:", d2)
print("d3:", d3)
print("d2 is d3:", d2 is d3)
print(id(d2))
print(id(d3))

d4 = d3.copy()
print("d4:", d4)
print("d3:", d3)
print("d4 is d3:", d4 is d3)

d4.day = 15
d3.year = 2010

print("d4:", d4)
print("d3:", d3)

# d5 = Date.copy(d3)
d5 = d3.copy()

# method = Date.copy
# method(d3)

# a = 1
# b = 2
# a = b
# b = 3

# print(Date.from_date_string(True))
# print(Date.from_date_string(None))
# print(Date.from_date_string(123))
# print(Date.from_date_string({"foo": "bar"}))
# print(Date.from_date_string("foo-bar"))

# print(Date("foo", None, []))

print(Date.from_date_string('2022-11-25'))
print(Date.from_date_string('2000-11-25'))
print(Date.from_date_string('2000-20-42'))
print("Check '2000-20-42'", Date.is_date_string_valid('2000-20-42'))
print("Check '2022-11-25'", Date.is_date_string_valid('2022-11-25'))
print("Check '2022-02-31'", Date.is_date_string_valid('2022-02-31'))
