from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import Movie


router = APIRouter()
templates = Jinja2Templates(directory="templates")


movie_list = [
    Movie(
        title="Film1",
        year=1993,
        description="The film of film 1",
    ),
    Movie(
        title="Film2",
        year=1992,
        description="The film of film 2",
    ),
    Movie(
        title="Film3",
        year=1993,
        description="The film of film 3",
    ),
    Movie(
        title="Film5",
        year=1994,
        description="The film of film 4",
    ),
    Movie(
        title="Film5",
        year=1995,
        description="The film of film 5",
    )
]


@router.get("/movies/",response_model=list[Movie])
def get_movies(
    year: int = Query(None, description="The year of movies"),
    title: str = Query(None, description="The title of movies"),
):
    result = movie_list
    if year is not None:
        result = [movie for movie in result if movie.year == year]
    if title is not None:
        result = [movie for movie in result if movie.title == title]

    return result


@router.get("/movs/", response_class=HTMLResponse)
def get_movs(
    request: Request,
    year: int = Query(None, description="The year of movies"),
    title: str = Query(None, description="The title of movies"),
):
    result = movie_list
    if year is not None:
        result = [movie for movie in result if movie.year == year]
    if title is not None:
        result = [movie for movie in result if movie.title == title]

    title1 = 'Все фильмы'
    text = "Страница с фильмами"
    context = {"request": request,
               "title": title1,
               "text": text,
               "movies": result}
    return templates.TemplateResponse("movies.html", context=context)


@router.get("/movies/{movie_id}/", response_model=Movie)
def get_movie_by_id(movie_id: int):
    """Получить информацию по фильму."""
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie_list[movie_id]


@router.post("/movies/", response_model=Movie, status_code=201)
def create_movie(movie: Movie):
    """Добавить новый фильм."""
    for m in movie_list:
        if m.title == movie.title and m.year == movie.year:
            raise HTTPException(status_code=409, detail="Такой фильм есть")

    movie_list.append(movie)
    return movie


@router.put("/movies/{movie_id}/")
def edit_movie(movie_id: int, movie: Movie):
    """Добавить новый фильм."""
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=404, detail="Movie not found")
    movie_list[movie_id].title = movie.title
    movie_list[movie_id].year = movie.year
    movie_list[movie_id].description = movie.description

    return movie_list[movie_id]


@router.delete("/movies/{movie_id}/")
def delete_movie(movie_id: int):
    """Добавить новый фильм."""
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=404, detail="Movie not found")
    result = movie_list.pop(movie_id)

    return {'message': f'Movie {result.title} deleted'}
