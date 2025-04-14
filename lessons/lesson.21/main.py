from http.client import responses

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from routers.user_routers import router as user_router
from routers.items_routers import router as item_router


app = FastAPI()

templates = Jinja2Templates(directory='templates')

# Список фильмов
movies = [
    {'id': 1, 'title': 'Film1', 'genre': 'Fantastic1', 'rating': 9.0},
    {'id': 2, 'title': 'Film2', 'genre': 'Fantastic2', 'rating': 5.77},
    {'id': 3, 'title': 'Film3', 'genre': 'Fantastic3', 'rating': 7.0},
    {'id': 4, 'title': 'Film4', 'genre': 'Fantastic4', 'rating': 8.0},
]


# Главная страница
@app.get("/index/")
async def main_page(request: Request):
    context = {
        'request': request,
        'title': 'Главная страница',
        'movies': movies,
    }
    return templates.TemplateResponse('index.html', context=context)
    # return templates.TemplateResponse('index.html', {'request': request, 'title': 'Главная страница', })


app.include_router(item_router, prefix='/api', tags=['items_routers'])
app.include_router(user_router, prefix='/main', tags=['user_routers'])

