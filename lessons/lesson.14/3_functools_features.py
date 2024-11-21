import time
from functools import partial, wraps, lru_cache, reduce, total_ordering
from termcolor import colored
import os
import logging

os.system("clear")

"""
Для работы с кодом необходимо установить все зависимости, указанные в файле requirements.txt

Пример команды:
pip install -r requirements.txt
"""

# Настройка логгера
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Стартовое время для измерения текущего времени
start_time = time.time()


def current_time():
    """
    Возвращает текущее время в секундах с момента запуска программы.
    """
    return round(time.time() - start_time, 2)


def log_message(message, color, level):
    """
    Логирует сообщение с указанным цветом и уровнем.

    Args:
        message (str): Сообщение для логирования.
        color (str): Цвет сообщения (используется библиотека termcolor).
        level (str): Уровень логирования ('info', 'warning', 'error').
    """
    formatted_message = colored(f"[{current_time()}s] {message}", color)
    if level == "info":
        logger.info(formatted_message)
    elif level == "warning":
        logger.warning(formatted_message)
    elif level == "error":
        logger.error(formatted_message)


# Создаем частичные функции для упрощения логирования
log_info = partial(log_message, color="green", level="info")
log_warning = partial(log_message, color="yellow", level="warning")
log_error = partial(log_message, color="red", level="error")


def multiply_by(x):
    """
    Возвращает замыкание для умножения заданного числа на переданное значение.

    Args:
        x (int): Число для умножения.

    Returns:
        function: Функция, умножающая переданное значение на x.
    """

    def multiplier(y):
        return x * y

    return multiplier


def multiply(x, y):
    """
    Умножает два числа.

    Args:
        x (int): Первый множитель.
        y (int): Второй множитель.

    Returns:
        int: Произведение x и y.
    """
    return x * y


def timing_decorator(func):
    """
    Декоратор для измерения времени выполнения функции.

    Args:
        func (function): Функция, время выполнения которой нужно измерить.

    Returns:
        function: Обернутая функция с измерением времени.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        log_warning(f"Executed {func.__name__} in {end - start:.4f} seconds")
        return result

    return wrapper


@timing_decorator
def slow_function():
    """
    Пример функции, которая выполняется медленно для демонстрации декоратора.
    """
    time.sleep(1)
    return "Done"


@timing_decorator
@lru_cache(maxsize=2)
def multiply_thousand(n):
    """
    Вычисляет n в степени 1 000 000 для демонстрации мемоизации.

    Args:
        n (int): Число для возведения в степень.

    Returns:
        int: Возвращает то же число (результат опущен для скорости).
    """
    n**1000000
    return n


@total_ordering
class Person:
    """
    Класс, представляющий человека с упрощенным сравнением по возрасту.

    Args:
        name (str): Имя человека.
        age (int): Возраст человека.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


# Если вы захотите активировать примеры, просто раскомментируйте нужные блоки
if __name__ == "__main__":
    pass
    """
    # Примеры логирования
    log_info("This is an info message.")
    log_warning("This is a warning message.")
    log_error("This is an error message.")

    # Примеры использования замыкания
    triple_with_closure = multiply_by(3)
    log_info(f"Using closure: 3 * 5 = {triple_with_closure(5)}")

    # Примеры использования partial
    triple_with_partial = partial(multiply, 3)
    log_info(f"Using partial: 3 * 5 = {triple_with_partial(5)}")

    # Пример декоратора
    log_info(slow_function())

    # Пример мемоизации
    log_info(f"multiply_thousand: {multiply_thousand(100)}")

    # Пример работы reduce
    numbers = [1, 2, 3, 4, 5]
    sum_result = reduce(lambda x, y: x + y, numbers)
    log_info(f"Sum of {numbers}: {sum_result}")

    # Пример использования total_ordering
    alice = Person("Alice", 30)
    bob = Person("Bob", 25)
    log_info(f"Alice > Bob: {alice > bob}")
    """
