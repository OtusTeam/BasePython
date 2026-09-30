from typing import Self


class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_iso(cls, date_str: str) -> Self:
        return cls(*map(int, date_str.split("-")))

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.year}, {self.month}, {self.day})"


class CalendarDate(Date):
    def book_time(self):
        return f"бронируем время на {self}.."


d1 = Date(2000, 10, 30)
print(d1)
print(d1.year, d1.month, d1.day)

d2 = Date.from_iso("2020-12-31")
print(d2)
print(d2.year, d2.month, d2.day)
cd = CalendarDate.from_iso("2020-12-31")
print(cd, type(cd))
print(cd.year, cd.month, cd.day)
print(cd.book_time())
