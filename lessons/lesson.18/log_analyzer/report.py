"""Подготовка отчета."""

import json
from collections import Counter


def coun_levels(enteries):
    x = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    for item in enteries:
        level = item["level"]

        if level in x:
            x[level] += 1

    return x


def build_report(statistics):
    report = f"Результат анализа логов: INFO - {statistics['INFO']}, WARNING - {statistics['WARNING']}, ERROR - {statistics['ERROR']}. Отчет успешно сформирован на основе журнала приложения."

    return report
