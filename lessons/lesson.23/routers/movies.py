from fastapi import APIRouter, Query, HTTPException, status

from schemas.movies import Movie, MovieCreate, movie_list


router = APIRouter()


@router.get("/", response_model=list[Movie])
async def movies(
    year: int = Query(None, description="Year of the movie"),
    title: str = Query(None, description="Title of the movie")
):
    """Получить список фильмов."""
    result = movie_list
    if year is not None:
        result = [movie for movie in result if movie.year >= year]
    if title is not None:
        result = [movie for movie in result if title in movie.title]
    return result


@router.get("/{movie_id}/", response_model=Movie)
async def movie_detail(movie_id: int):
    """Получить детали фильма по его ID."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {movie_id + 1} not found")

    return movie_list[movie_id]


@router.post("/", response_model=Movie, status_code=status.HTTP_201_CREATED)
async def movie_create(movie: MovieCreate):
    """Создать новый фильм."""
    for m in movie_list:
        if m.title == movie.title and m.year == movie.year:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Такой фильм уже существует")
    new_id = max((ex_movie.id for ex_movie in movie_list), default=0) + 1
    new_movie = Movie(
        id=new_id,
        **movie.model_dump(),
    )
    movie_list.append(new_movie)
    return new_movie


@router.put("/{movie_id}/", response_model=Movie)
async def movie_update(movie_id: int, movie: Movie):
    """Обновить фильм."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {movie_id + 1} not found")

    movie_list[movie_id].title = movie.title
    movie_list[movie_id].year = movie.year

    return movie_list[movie_id]


@router.delete("/{movie_id}/")
async def movie_delete(movie_id: int):
    """Удалить фильм."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {movie_id + 1} not found")

    result = movie_list.pop(movie_id)

    return {'message': f'Movie {result.title} deleted'}
