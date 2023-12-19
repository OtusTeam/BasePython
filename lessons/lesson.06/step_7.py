def date_from_str(cls, date_str: str):
    year, month, day = (
        int(elem)
        for elem in date_str.split("-")
    )

    assert cls.validate_month(month)
    return cls(
        year=year,
        month=month,
        day=day,
    )


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def copy(self):
        # return Date(...)
        return self.__class__(
            year=self.year,
            month=self.month,
            day=self.day,
        )

    @classmethod
    def from_str(cls, date_str: str):
        year, month, day = (
            int(elem)
            for elem in date_str.split("-")
        )
        # my_class = Date
        # class_ = Date
        # klass = Date

        assert cls.validate_month(month)
        return cls(
            year=year,
            month=month,
            day=day,
        )

    @staticmethod
    def validate_month(month):
        return 1 <= month <= 12

    def __str__(self):
        return f"{self.__class__.__name__}(year={self.year}, month={self.month}, day={self.day})"


def main():
    d1 = Date(2023, 12, 19)
    d2 = d1
    d3 = d1.copy()
    print(d1)
    print(d2)
    print(d3)
    d2.year = 2022
    print(d1)
    print(d2)
    print(d3)

    d4 = Date.from_str("2023-11-14")
    print(d4)
    d5 = d4.from_str("2021-10-18")
    print(d5)
    # d6 = d5.copy()
    d6 = Date.copy(d5)
    print(d6)

    print("13 is month?", Date.validate_month(13))
    print("12 is month?", Date.validate_month(12))
    print("7 is month?", d5.validate_month(7))


main()
