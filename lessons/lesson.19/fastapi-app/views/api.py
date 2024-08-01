from fastapi import APIRouter
from views.users.crud import UsersStorage


"""В этом модуле теперь только маршруты для взаимодействия напрямую с csv 
файлом, без html страницы"""

# Создаем роутер
router = APIRouter()


@router.post(
    "/add-record-query",
    summary="Добавление новой записи через Query String",
    description="Добавляет новую запись в CSV файл через Query String.",
)
def add_record_query(name: str, age: int, city: str):
    new_record = UsersStorage.add_record(name, age, city)
    if "error" in new_record:
        return {"message": "Данные не прошли валидацию!", "record": new_record}
    return {"message": "Запись успешно добавлена!", "record": new_record}


@router.delete(
    "/delete-record-query",
    summary="Удаление записи через Query String",
    description="Удаляет запись из CSV файла через Query String.",
)
def delete_record_query(record_id: int):
    message = UsersStorage.delete_record(id=record_id)
    return message


@router.post(
    "/edit-record-query",
    summary="Редактирование записи через Query String",
    description="Редактирует запись в CSV файле через Query String.",
)
def edit_record_query(
    record_id: int, name: str = None, age: int = None, city: str = None
):
    message = UsersStorage.edit_record(record_id, name, age, city)
    return message
