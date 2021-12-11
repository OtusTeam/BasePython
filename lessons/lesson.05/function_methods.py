# подскажите что за методы могут быть у функции?


def work():
    print("I can work")


# Можно распечатать все методы, доступные для данной функции
# Все они наследуются любой функцией/методом из класса object.
for method_name in dir(work):
    if callable(getattr(work, method_name)):
        print(method_name)


# Создаем функцию для замены __str__ метода для функции из класса object
def str_for_function():
    print("test")


# Проверяем, что у объекта-функции work есть метод __str__
# У функции есть все методы из класса object, так как он от object наследуется
print(work.__str__())
print(work)
print(type(work))
print(type(work.__str__))
