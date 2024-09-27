import csv
from typing import List, Dict
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field, PositiveInt, ValidationError
from typing import Annotated

app = FastAPI()

# Инициализируем шаблонизатор Jinja2
templates = Jinja2Templates(directory="templates")

# Утилитарные функции для работы с CSV файлом
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

# Определяем Pydantic-модель для валидации данных
class User(BaseModel):
    id: PositiveInt
    name: Annotated[str, Field(min_length=3, max_length=15)]
    age: Annotated[int, Field(ge=14, le=100)]
    city: Annotated[str, Field(default="default city", min_length=2, max_length=12)]

# Класс для CRUD операций
class UsersStorage:

    @staticmethod
    def validation(record):
        User(**record)

    @staticmethod
    def get_all_records():
        return read_csv()

    @staticmethod
    def get_record_by_id(id):
        records = read_csv()
        return next((record for record in records if int(record["id"]) == id), None)

    @staticmethod
    def add_record(name: str, age: int, city: str):
        records = UsersStorage.get_all_records()
        id = max([int(record["id"]) for record in records] + [0]) + 1
        # Валидация данных
        try:
            new_record = User(id=id, name=name, age=age, city=city)
            add_csv(new_record.model_dump())
            return new_record
        except ValidationError as e:
            return {"error": e.errors()}

    @staticmethod
    def delete_record(id: PositiveInt):
        records = read_csv()
        record = next((record for record in records if int(record["id"]) == id), None)
        if not record:
            return {"message": "Запись не найдена", "record_id": id}
        records = [record for record in records if int(record["id"]) != id]
        write_csv(records)
        return {"message": "Запись успешно удалена", "record_id": id}

    @staticmethod
    def edit_record(id: int, name: str = None, age: int = None, city: str = None):
        records = read_csv()
        record = next((record for record in records if int(record["id"]) == id), None)

        if not record:
            return {"message": "Запись не найдена", "record_id": id}

        if name:
            record["name"] = name
        if age:
            record["age"] = age
        if city:
            record["city"] = city

        try:
            UsersStorage.validation(record)
            write_csv(records)
            return {"message": "Запись успешно отредактирована", "record": record}
        except ValidationError as e:
            return {"error": e.errors()}

# Маршруты для HTML-шаблонов

@app.get(
    "/template",
    response_class=HTMLResponse,
    summary="Маршрут с шаблоном",
    description="Возвращает сообщение в формате HTML, используя шаблон Jinja2.",
)
def read_templated_html(request: Request):
    context = {
        "request": request,
        "title": "Hello, Templated World!",
        "message": "Hello, World in HTML with Templating!",
    }
    return templates.TemplateResponse("step_1.html", context)

@app.get(
    "/record/{record_id}",
    response_class=HTMLResponse,
    summary="Получение записи по ID",
    description="Возвращает запись из CSV файла по указанному ID в формате HTML.",
)
def get_record(request: Request, record_id: int):
    record = UsersStorage.get_record_by_id(record_id)
    context = {"request": request, "record": record}
    return templates.TemplateResponse("step_2.html", context)

@app.get(
    "/records",
    response_class=HTMLResponse,
    summary="Получение всех записей",
    description="Возвращает все записи из CSV файла в формате HTML.",
)
def get_records(request: Request):
    records = UsersStorage.get_all_records()
    context = {"request": request, "records": records}
    return templates.TemplateResponse("step_2.html", context)

@app.post(
    "/add-record",
    response_class=HTMLResponse,
    summary="Добавление новой записи",
    description="""
    Добавляет новую запись в CSV файл и возвращает обновленный
    список записей в формате HTML.""",
)
def add_record(
    request: Request, name: str = Form(...), age: int = Form(...), city: str = Form(...)
):
    record = UsersStorage.add_record(name, age, city)
    records = UsersStorage.get_all_records()
    if "error" in record:
        target = record["error"][0]["loc"][0]
        error = record["error"][0]["msg"]
        message = f"Ошибка! Валидация не пройдена, {target} - {error}"
    else:
        message = "Запись успешно добавлена!"
    context = {
        "request": request,
        "records": records,
        "message": message,
    }
    return templates.TemplateResponse("step_2.html", context)

# API-маршруты без использования роутеров

@app.post(
    "/add-record-query",
    summary="Добавление новой записи через Query String",
    description="Добавляет новую запись в CSV файл через Query String.",
)
def add_record_query(name: str, age: int, city: str):
    new_record = UsersStorage.add_record(name, age, city)
    if "error" in new_record:
        return {"message": "Данные не прошли валидацию!", "record": new_record}
    return {"message": "Запись успешно добавлена!", "record": new_record}

@app.delete(
    "/delete-record-query",
    summary="Удаление записи через Query String",
    description="Удаляет запись из CSV файла через Query String.",
)
def delete_record_query(record_id: int):
    message = UsersStorage.delete_record(id=record_id)
    return message

@app.post(
    "/edit-record-query",
    summary="Редактирование записи через Query String",
    description="Редактирует запись в CSV файле через Query String.",
)
def edit_record_query(
    record_id: int, name: str = None, age: int = None, city: str = None
):
    message = UsersStorage.edit_record(record_id, name, age, city)
    return message
