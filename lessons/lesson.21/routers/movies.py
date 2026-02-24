from fastapi import APIRouter, Query, HTTPException, status
from schemas.movie import Movie, movie_list


router = APIRouter()


@router.get("/", response_model=list[Movie])
async def movies(
    year: int = Query(None, description="Year of movie"),
    title: str = Query(None, description="Title of movie"),
):
    """Получить список фильмов."""
    result = movie_list

    if year is not None:
        result = [movie for movie in result if movie.year == year]
    if title is not None:
        result = [movie for movie in result if movie.title == title]

    return result


@router.get("/{movie_id}/", response_model=Movie)
async def movie_details(movie_id: int):
    """Получить детальную информацию о фильме."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    return movie_list[movie_id]


@router.post("/", response_model=Movie, status_code=status.HTTP_201_CREATED)
async def movie_create(movie: Movie):
    """Добавить фильм."""
    for m in movie_list:
        if m.title == movie.title and m.year == movie.year:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Movie already exists")
    movie_list.append(movie)
    return movie


@router.put("/{movie_id}/", response_model=Movie)
async def movie_update(movie_id: int, movie: Movie):
    """Обновить фильм."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    movie_list[movie_id].title = movie.title
    movie_list[movie_id].year = movie.year

    return movie_list[movie_id]


@router.delete("/{movie_id}/")
async def movie_details(movie_id: int):
    """Удалить фильм."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    result = movie_list.pop(movie_id)

    return {'message': f'Фильм {result.title} был удален'}
