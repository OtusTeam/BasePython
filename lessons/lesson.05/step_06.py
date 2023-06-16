# перегрузка (overload) - не существует

class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_date_string(cls, date_string: str):
        year, month, day = map(int, date_string.split("-"))
        return cls(
            year=year,
            month=month,
            day=day,
        )

    @staticmethod
    def is_date_string(date_string: str):
        return date_string.count("-") == 2

    def copy(self):
        return self.__class__(
            year=self.year,
            month=self.month,
            day=self.day,
        )

    def __eq__(self, other: "Date"):
        return (
            isinstance(other, Date)
            and
            self.year == other.year
            and
            self.month == other.month
            and
            self.day == other.day
        )

    def greater_than(self, other: "Date"):
        if self.year > other.year:
            return True
        if self.year < other.year:
            return False

        if self.month > other.month:
            return True
        if self.month < other.month:
            return False

        return self.day > other.day

    def __gt__(self, other):
        # print("self", self)
        # print("other", other)
        return self.greater_than(other)

    # def __ge__(self, other):
    #     pass
    #
    # def __lt__(self, other):
    #     pass
    #
    # def __le__(self, other):
    #     pass

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"year={self.year}, "
            f"month={self.month}, "
            f"day={self.day}"
            f")"
        )


# Date("2023-06-16")
# Date(2023, 6, 16)
# Date(164756464364)

d1 = Date(2023, 6, 16)
print(d1)

d2 = Date(2002, 2, 2)
print(d2)

d3 = Date.from_date_string("1968-12-31")
print(d3)

d4 = d3

print("is:", d3 is d4)
print("eq:", d3 == d4)
print(d4)

d4.day = 20
d3.month = 3
print(d3)
print(d4)

print(d4 is d3)

d5 = Date(year=d3.year, month=d3.month, day=d3.day)
print(d5)
print(d3)

d3.year = 2000
d5.month = 5
print(d3)
print(d5)
print(d5 is d3)

d6 = d5.copy()
print("is:", d5 is d6)
print("eq:", d5 == d6)
# print("gr or eq:", d5 >= d6)
print(d5)
print(d6)

d5.day = 10
d6.month = 7
print("d5", d5)
print("d6", d6)
print("d6 > d5", d6.greater_than(d5))
print()
print("d6 > d5", d6 > d5)
print()
print("d6 < d5", d6 < d5)

print(Date.is_date_string("abc"))
print(Date.is_date_string("2000-01-20"))
print(type(d5))
