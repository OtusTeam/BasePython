from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Настраиваем шаблонизатор Jinja2, указывая директорию для шаблонов
templates = Jinja2Templates(directory="templates")


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
def read_templated_html(request: Request):  # pylint: disable=missing-function-docstring
    context = {
        "request": request,
        "title": "Hello, Templated World!",
        "message": "Hello, World in HTML with Templating!",
    }
    return templates.TemplateResponse("step_1.html", context)


# Запуск приложения uvicorn step_1:app --reload
