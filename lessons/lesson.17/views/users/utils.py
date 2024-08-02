import csv
from typing import List, Dict

"""В этом модуле утилитарные функции для работы с CSV файлом."""

DATA_FILE = "data.csv"


def read_csv() -> List[Dict[str, str]]:
    """Функция для чтения данных из CSV файла"""
    with open(DATA_FILE, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]


def write_csv(data: List[Dict[str, str]]):
    """Функция для записи данных в CSV файл"""
    fieldnames = ["id", "name", "age", "city"]
    with open(DATA_FILE, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def add_csv(data: Dict[str, str]):
    """Функция для добавления строки в CSV файл"""
    fieldnames = ["id", "name", "age", "city"]
    with open(DATA_FILE, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)
