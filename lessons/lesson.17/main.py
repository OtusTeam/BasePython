from fastapi import FastAPI
from views.api import router
from views.views import view_router

"""Основное приложение"""
app = FastAPI(
    title="Приложение для работы с записями",
    description="Приложение для добавления, просмотра и управления записями в CSV файле",
    version="1.0.0",
)

app.include_router(router, prefix="/api")
app.include_router(view_router, prefix="")


@app.get(
    "/", summary="Корневой маршрут", description="Возвращает приветственное сообщение."
)
def read_root():
    return "Hello, World!"
