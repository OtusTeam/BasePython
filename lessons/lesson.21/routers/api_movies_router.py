from fastapi import HTTPException, Query, APIRouter
from models import Movie


router = APIRouter()


movie_list = [
    Movie(
        title = "Movie0",
        year = 1999,
        description = "Movie Description",
    ),
    Movie(
        title="Movie1",
        year=1990,
        description="Movie Description 1",
    ),
    Movie(
        title="Movie2",
        year=1999,
        description="Movie Description 2",
    ),
    Movie(
        title="Movie3",
        year=1989,
        description="Movie Description 3",
    ),
    Movie(
        title="Movie4",
        year=2009,
        description="Movie Description 4",
    ),
]



@router.get("/", response_model=list[Movie])
async def get_movies(
    year: int = Query(None, description="Year of release"),
    title: str = Query(None, description="The title of movies")
):
    """Получить список фильмов."""
    result = movie_list
    if  year is not None:
        result = [movie for movie in result if movie.year == year]
    if  title is not None:
        result = [movie for movie in result if movie.title == title]
    return result


@router.get("/{movie_id}/", response_model=Movie)
async def get_movie_id(movie_id: int):
    """Получить информациб по фильму."""
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie_list[movie_id]


@router.post("/", response_model=Movie, status_code=201)
async def create_movie(movie: Movie):
    """Добавить новый фильм."""
    for m in movie_list:
        if m.title == movie.title and m.year == movie.year:
            raise HTTPException(status_code=409, detail="Movie already exists")

    movie_list.append(movie)
    return movie


@router.put("/{movie_id}/", response_model=Movie)
async def edit_movie(movie_id: int, movie: Movie):
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=404, detail="Movie not found")
    movie_list[movie_id].title = movie.title
    movie_list[movie_id].year = movie.year
    return movie_list[movie_id]


@router.delete("/{movie_id}/")
async def delete_movie(movie_id: int):
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=404, detail="Movie not found")
    result = movie_list.pop(movie_id)
    return {'message': f'Фильм {result.title} удален.'}