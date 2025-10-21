from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from schemas.movie import Movie


router = APIRouter()
templates = Jinja2Templates(directory="templates")

movie_list = [
    Movie(
        title='Movie1',
        year=1999,
        description='Movie description',
    ),
    Movie(
        title='Movie2',
        year=1992,
        description='Movie description2',
    ),
    Movie(
        title='Movie3',
        year=1949,
        description='Movie description3',
    ),
    Movie(
        title='Movie4',
        year=1999,
        description='Movie description4',
    ),
    Movie(
        title='Movie5',
        year=1939,
        description='Movie description5',
    ),
    Movie(
        title='Movie1',
        year=1999,
        description='Movie description',
    ),
    Movie(
        title='Movie2',
        year=1992,
        description='Movie description2',
    ),
    Movie(
        title='Movie3',
        year=1949,
        description='Movie description3',
    ),
    Movie(
        title='Movie4',
        year=1999,
        description='Movie description4',
    ),
    Movie(
        title='Movie5',
        year=1939,
        description='Movie description5',
    ),
]


@router.get("/", response_class=HTMLResponse)
async def movies_list(request: Request):
    context = {
        "request": request,
        "title": "Список наших фильмов ",
        "text": "Описание страницы",
        "movies": movie_list,
    }

    return templates.TemplateResponse("movies_list.html", context=context)


@router.get("/{movie_id}/", response_class=HTMLResponse)
async def movie_details(request: Request, movie_id: int):
    """Получить детальную информацию по списку."""
    movie_id -= 1
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=404, detail="Movie not found")

    context = {
        "request": request,
        "text": "Описание страницы",
        "movie": movie_list[movie_id],
    }

    return templates.TemplateResponse("movies_detail.html", context=context)

