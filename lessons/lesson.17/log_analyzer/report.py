import json
from collections import Counter


def count_levels(entries):
    x = {"INFO": 0, "WARNING": 0,"ERROR":0}

    for item in entries:
        level=item["level"]

        if level in x:
            x[level] += 1

    return x


def build_report(statistics):
    report_text = f"Результат анализа логов: INFO - {statistics['INFO']}, WARNING - {statistics['WARNING']}, ERROR - {statistics['ERROR']}"

    return report_text
