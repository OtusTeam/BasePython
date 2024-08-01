from fastapi import APIRouter
from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from views.users.crud import UsersStorage


"""Модуль с маршрутами для HTML шаблонов"""
view_router = APIRouter()

# Настраиваем шаблонизатор Jinja2, указывая директорию для шаблонов
templates = Jinja2Templates(directory="templates")


@view_router.get(
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


@view_router.get(
    "/record/{record_id}",
    response_class=HTMLResponse,
    summary="Получение записи по ID",
    description="Возвращает запись из CSV файла по указанному ID в формате HTML.",
)
def get_record(request: Request, record_id: int):
    record = UsersStorage.get_record_by_id(record_id)
    context = {"request": request, "record": record}
    return templates.TemplateResponse("step_2.html", context)


@view_router.get(
    "/records",
    response_class=HTMLResponse,
    summary="Получение всех записей",
    description="Возвращает все записи из CSV файла в формате HTML.",
)
def get_records(request: Request):
    records = UsersStorage.get_all_records()
    context = {"request": request, "records": records}
    return templates.TemplateResponse("step_2.html", context)


@view_router.post(
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
        target = record["error"][0]["input"]
        error = record["error"][0]["msg"]
        message = f"Error! Validation error, {target} - {error}"
    else:
        message = "Запись успешно добавлена!"
    context = {
        "request": request,
        "records": records,
        "message": message,
    }
    return templates.TemplateResponse("step_2.html", context)
