from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import csv

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Настраиваем шаблонизатор Jinja2, указывая директорию для шаблонов
templates = Jinja2Templates(directory="templates")

# Определяем файл данных CSV
DATA_FILE = "data.csv"


# Определяем маршрут корневого пути
@app.get("/")
def read_root():
    return "Hello, World!"


# Определяем маршрут, возвращающий JSON ответ
@app.get("/json")
def read_json():
    return {"message": "Hello, World in JSON!"}


# Определяем маршрут, возвращающий HTML ответ
@app.get("/html", response_class=HTMLResponse)
def read_html():
    return """
    <html>
        <head>
            <title>Hello, World!</title>
        </head>
        <body>
            <h1>Hello, World in HTML!</h1>
        </body>
    </html>
    """


# Определяем маршрут, использующий шаблон Jinja2 для формирования ответа
@app.get("/template", response_class=HTMLResponse)
def read_templated_html(request: Request):
    context = {
        "request": request,
        "title": "Hello, Templated World!",
        "message": "Hello, World in HTML with Templating!",
    }
    return templates.TemplateResponse("step_1.html", context)


# Функция для чтения данных из CSV файла
def read_csv():
    with open(DATA_FILE, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]


# Определяем маршрут для получения всех записей из CSV файла
@app.get("/records", response_class=HTMLResponse)
def get_records(request: Request):
    records = read_csv()
    context = {"request": request, "records": records}
    return templates.TemplateResponse("step_2.html", context)


# Определяем маршрут для получения записи по ID
@app.get("/record/{record_id}", response_class=HTMLResponse)
def get_record(request: Request, record_id: int):
    records = read_csv()
    record = next(
        (record for record in records if int(record["id"]) == record_id), None
    )
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    context = {"request": request, "record": record}
    return templates.TemplateResponse("step_2.html", context)


# Функция для записи данных в CSV файл
def write_csv(data):
    fieldnames = ["id", "name", "age", "city"]
    with open(DATA_FILE, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# Определяем маршрут для добавления новой записи в CSV файл
@app.post("/add-record-query")
def add_record_query(name: str, age: int, city: str):
    records = read_csv()
    new_id = max(int(record["id"]) for record in records) + 1
    new_record = {"id": new_id, "name": name, "age": age, "city": city}
    records.append(new_record)
    write_csv(records)
    return {"message": "Запись успешно добавлена!", "record": new_record}


# Определяем маршрут для удаления записи в CSV файле
@app.delete("/delete-record-query")
def delete_record_query(record_id: int):
    records = read_csv()
    record = next(
        (record for record in records if int(record["id"]) == record_id), None
    )
    if not record:
        raise HTTPException(status_code=404, detail="Запись не найдена")
    records = [record for record in records if int(record["id"]) != record_id]
    write_csv(records)
    return {"message": "Запись успешно удалена", "record_id": record_id}


# Определяем маршрут для редактирования записи в CSV файле
@app.patch("/edit-record-query")
def edit_record_query(
    record_id: int, name: str = None, age: int = None, city: str = None
):
    records = read_csv()
    record = next(
        (record for record in records if int(record["id"]) == record_id), None
    )

    if not record:
        raise HTTPException(status_code=404, detail="Запись не найдена")

    if name:
        record["name"] = name
    if age:
        record["age"] = age
    if city:
        record["city"] = city

    write_csv(records)
    return {"message": "Запись успешно отредактирована", "record": record}


# Определяем маршрут для добавления новой записи в CSV файл через форму html
@app.post("/add-record", response_class=HTMLResponse)
def add_record(
    request: Request, name: str = Form(...), age: int = Form(...), city: str = Form(...)
):
    records = read_csv()
    new_id = max(int(record["id"]) for record in records) + 1
    new_record = {"id": new_id, "name": name, "age": age, "city": city}
    records.append(new_record)
    write_csv(records)
    context = {
        "request": request,
        "records": records,
        "message": "Record added successfully!",
    }
    return templates.TemplateResponse("step_2.html", context)
