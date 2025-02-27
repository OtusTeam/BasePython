from fastapi import APIRouter, HTTPException, status
from pydantic import PositiveInt

from .crud import storage
from .schema import MovieRead, MovieCreate

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)

@router.get(
    "/",
    response_model=list[MovieRead],
)
def get_movies():
    return storage.get()


@router.post(
    "/",
    response_model=MovieRead,
)
def create_movie(
    movie_in: MovieCreate,
):
    return storage.add(movie_in=movie_in)


@router.get(
    "/{movie_id}/",
    response_model=MovieRead,
)
def get_movie(
    movie_id: PositiveInt,
):
    movie = storage.get_by_id(movie_id=movie_id)
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie #{movie_id} not found!",
    )

@router.delete(
    "/{movie_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def get_movie(
    movie_id: PositiveInt,
) -> None:
    storage.delete(movie_id=movie_id)
