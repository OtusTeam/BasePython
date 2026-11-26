from fastapi import APIRouter, Query, HTTPException, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from schemas.movies import Movie, MovieCreate, movie_list


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse, name="html_movies_list")
async def movies(
    request: Request,
    year: int = Query(None, description="Year of the movie"),
    title: str = Query(None, description="Title of the movie")
):
    """Получить список фильмов."""
    result = movie_list
    if year is not None:
        result = [movie for movie in result if movie.year >= year]
    if title is not None:
        result = [movie for movie in result if title in movie.title]

    context = {
        "movies": result,
        "title": "Список фильмов"
    }
    # return templates.TemplateResponse("movies.html", {"request": request, "movies": result})
    return templates.TemplateResponse(request=request, name="movies/movie_list.html", context=context)


@router.get("/{movie_id}/", response_class=HTMLResponse, name="html_movies_detail")
async def movie_detail(request: Request, movie_id: int):
    """Получить детали фильма по его ID."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {movie_id + 1} not found")

    context = {
        "movie": movie_list[movie_id],
        "title": movie_list[movie_id].title
    }

    return templates.TemplateResponse(request=request, name="movies/movie_detail.html", context=context)

