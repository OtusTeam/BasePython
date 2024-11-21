import itertools
import time
import os
import logging

os.system("clear")

# Настройка стандартного логгера
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()


def generate_ids():
    """
    Генерирует последовательные идентификаторы, начиная с 1, с шагом 1.
    """
    logger.info("Генерация последовательных идентификаторов:")
    id_generator = itertools.count(start=1, step=1)
    for _ in range(5):
        logger.info(f"ID: {next(id_generator)}")


def cycle_tasks():
    """
    Циклически выполняет заданные задачи.

    Задачи определены как функции, которые выполняются по очереди.
    """

    def task_1():
        logger.info("task1")

    def task_2():
        logger.info("task2")

    def task_3():
        logger.info("task3")

    logger.info("Циклическое выполнение задач:")
    tasks = itertools.cycle([task_1, task_2, task_3])
    for _ in range(6):
        next(tasks)()


def repeat_messages(iterations):
    """
    Повторяет указанное сообщение заданное количество раз.

    Args:
        iterations (int): Количество повторений.
    """
    logger.info("Повторяющиеся сообщения:")
    repeater = itertools.repeat("Повторяйте это сообщение", iterations)
    for item in repeater:
        logger.info(f"Сообщение: {item}")


def generate_test_cases():
    """
    Генерирует тестовые случаи в виде всех возможных комбинаций из двух полей.
    """
    logger.info("Тестовые случаи с комбинациями полей:")
    fields = ["username", "password", "email"]
    required_fields = itertools.combinations(fields, 2)
    for combination in required_fields:
        logger.info(f"Комбинация: {combination}")


def filter_data():
    """
    Демонстрирует фильтрацию данных с использованием dropwhile и takewhile.
    """
    logger.info("Фильтрация данных с использованием dropwhile и takewhile:")
    data = [1, 2, 3, 4, 5, 6]

    logger.info("Данные после dropwhile (x < 4):")
    dropped_data = itertools.dropwhile(lambda x: x < 4, data)
    for item in dropped_data:
        logger.info(f"Элемент: {item}")

    logger.info("Данные после takewhile (x < 4):")
    taken_data = itertools.takewhile(lambda x: x < 4, data)
    for item in taken_data:
        logger.info(f"Элемент: {item}")


def combine_iterators():
    """
    Объединяет несколько итераторов в один с использованием itertools.chain.
    """
    logger.info("Объединение нескольких итераторов:")
    iter1 = [1, 2, 3]
    iter2 = ["A", "B", "C"]
    iter3 = "string"
    combined = itertools.chain(iter1, iter2, iter3)
    logger.info(list(combined))


def demonstrate_product():
    """
    Демонстрирует картезианское произведение двух итераторов.
    """
    logger.info("Картезианское произведение итераторов:")
    iter1 = [1, 2]
    iter2 = ["A", "B"]
    product_result = itertools.product(iter1, iter2)
    for item in product_result:
        logger.info(f"Комбинация: {item}")


def demonstrate_permutations():
    """
    Генерирует перестановки элементов.
    """
    logger.info("Перестановки элементов:")
    elements = ["A", "B", "C"]
    permutation_result = itertools.permutations(elements, 2)
    logger.info(f"Перестановки: {list(permutation_result)}")


def demonstrate_accumulate():
    """
    Демонстрирует накопление значений с использованием accumulate.

    Проводится как накопительная сумма, так и накопительное произведение.
    """
    logger.info("Пример accumulate (накопительная сумма):")
    numbers = [1, 2, 3, 4, 5]
    accumulate_result = itertools.accumulate(numbers)
    for item in accumulate_result:
        logger.info(f"Накопленная сумма: {item}")

    logger.info("Пример accumulate (накопительное произведение):")
    accumulate_result = itertools.accumulate(numbers, lambda x, y: x * y)
    for item in accumulate_result:
        logger.info(f"Накопленное произведение: {item}")


def demonstrate_zip_longest():
    """
    Объединяет итераторы разной длины с использованием zip_longest.

    Элементы, для которых нет пары, заполняются значением по умолчанию.
    """
    logger.info("Пример zip_longest:")
    iter1 = [1, 2, 3]
    iter2 = ["A", "B"]
    zip_longest_result = itertools.zip_longest(iter1, iter2, fillvalue="?")
    logger.info(f"Комбинации: {list(zip_longest_result)}")


def demonstrate_groupby():
    """
    Демонстрирует группировку данных с использованием groupby.
    """
    logger.info("Пример groupby:")
    group_data = sorted(
        [
            ("Russia", "Moscow"),
            ("Russia", "Saint-Petersburg"),
            ("Russia", "Krasnoyarsk"),
            ("Turkey", "Istanbul"),
            ("Turkey", "Alanya"),
            ("Great Britain", "London"),
            ("Great Britain", "Manchester"),
        ]
    )
    for key, group in itertools.groupby(group_data, lambda x: x[0]):
        group_items = [item[1] for item in group]
        logger.info(f"{key}: {group_items}")


def demonstrate_islice():
    """
    Создает срез из итератора с помощью islice.

    Пример: числа от 5 до 15 с шагом 2.
    """
    logger.info("Пример islice:")
    count_numbers = itertools.count(1)
    islice_result = itertools.islice(count_numbers, 5, 15, 2)
    for item in islice_result:
        logger.info(f"Элемент: {item}")


def demonstrate_tee():
    """
    Дублирует итераторы с использованием tee.
    """
    logger.info("Пример tee:")
    numbers = [1, 2, 3, 4]
    iter1, iter2 = itertools.tee(numbers, 2)

    logger.info("Первый итератор:")
    for item in iter1:
        logger.info(f"Элемент: {item}")

    logger.info("Второй итератор:")
    for item in iter2:
        logger.info(f"Элемент: {item}")


def demonstrate_combinations_with_replacement():
    """
    Генерирует комбинации с повторением.
    """
    logger.info("Комбинации с повторением:")
    elements = ["A", "B"]
    combinations_with_replacement_result = itertools.combinations_with_replacement(
        elements, 2
    )
    for item in combinations_with_replacement_result:
        logger.info(f"Комбинация: {item}")


if __name__ == "__main__":
    # Вызывайте нужные функции, чтобы посмотреть примеры их работы.
    generate_ids()
    # cycle_tasks()
    # repeat_messages(5)
    # generate_test_cases()
    # filter_data()
    # combine_iterators()
    # demonstrate_product()
    # demonstrate_permutations()
    # demonstrate_accumulate()
    # demonstrate_zip_longest()
    # demonstrate_groupby()
    # demonstrate_islice()
    # demonstrate_tee()
    # demonstrate_combinations_with_replacement()
