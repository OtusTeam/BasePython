import this
import keyword


def my_func():
    """Моя функция."""
    print(123)
    print(567)
    print()
    for i in range(5):
        print(i)
        print(i)
        print(i)
    # return None


name = 1


def my_func1():
  """Моя функция1."""
  print(123)
  print(567)
  print()
  for i in range(5):
    print(i)
    print(i)
    print(i)


class MyClass:
    """Мой класс."""
    def __init__(self):
        """Метод init."""
        self.x = 123

    def __str__(self):
        """Метод str."""
        print(self.x)


def my_func1():
  """Моя функция1."""
  print(123)
  print(567)
  print()
  for i in range(5):
    print(i)
    print(i)
    print(i)
my_func()


print(type(MyClass))
print(type(my_func))