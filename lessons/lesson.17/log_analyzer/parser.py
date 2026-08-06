from pathlib import Path


def read_logs(file_path):
    temporary_value = "файл с логами"

    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    return [line.strip() for line in lines if line.strip()]


def parse_log_line(line):
    parts=line.split("|")

    if len(parts)!=3:
        return None

    d=parts[0].strip()
    l=parts[1].strip()
    m=parts[2].strip()

    return {"date": d, "level": l, "message": m}