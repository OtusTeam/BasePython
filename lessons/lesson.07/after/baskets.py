DIRECTORY = "/Users/nigar/GitHub/BasePython/lessons/lesson.07/after/baskets.py"
RELATIVE_PATH = "lessons/lesson.07/after/baskets.py"


def test_function():
    print('I am a test function')


class Basket:

    def __init__(self, max_size=100):
        self.max_size = max_size

    def __str__(self):
        return f"{self.__class__.__name__} : max_size = {self.max_size}"


class IncorrectValueNumber(BaseException):
    pass


# print('testing imports')


# if __name__ == '__main__':
#     print('testing imports')
