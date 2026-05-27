from fastapi import APIRouter, Query, HTTPException, status, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from schemas.movies import Movie, movie_list


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def html_movies(
    request: Request,
    year: int = Query(None, description="Год фильма"),
    title: str = Query(None, description="Заголовок фильма"),
):
    """Получить список фильмов."""
    result = movie_list

    if title is not None:
        result = [movie for movie in result if movie.title == title]
    if year is not None:
        result = [movie for movie in result if movie.year == year]

    context = {
        "movies": result,
        "title": "Список фильмов"
    }

    return templates.TemplateResponse(request, "movies/movie_list.html", context=context)


@router.get("/{movie_id}/", response_class=HTMLResponse, name="html_movie_det")
async def html_movie_details(request: Request, movie_id: int):
    """Получить детальную информацию о фильме."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    context = {
       "movie": movie_list[movie_id]
    }

    return templates.TemplateResponse(request, 'movies/movie_detail.html', context=context)

