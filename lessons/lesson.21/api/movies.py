from typing import Annotated

from fastapi import status, Form, Query, HTTPException, APIRouter
from pydantic import PositiveInt

router = APIRouter()

MOVIES_DATABASE = {}


def init_movies():
    MOVIES_DATABASE.update(
        movies=[
            {"title": "Django Unchained"},
            {"title": "Chain Reaction"},
            {"title": "Pulp Fiction"},
        ],
    )

    for idx, movie_obj in enumerate(MOVIES_DATABASE["movies"], start=1):
        movie_obj["id"] = idx


init_movies()


@router.get(
    "/movies",
    tags=["Movies"],
    responses={
        status.HTTP_200_OK: {
            "description": "Movies List",
            "content": {
                "application/json": {
                    "example": {
                        "data": {
                            "movies": [
                                {"title": "Django Unchained"},
                                {"title": "Chain Reaction"},
                            ],
                        },
                    },
                },
            },
        },
    },
)
def get_movies(
    filter_name: Annotated[str, Query(alias="filter")] = "",
):
    # get data from db
    movies = MOVIES_DATABASE["movies"]
    # send data to client
    filtered_movies = movies[:]
    if filter_name:
        filtered_movies = [
            movie
            for movie in filtered_movies
            if filter_name.lower() in movie["title"].lower()
        ]
    return {
        "data": filtered_movies,
    }


@router.post(
    "/movies",
    tags=["Movies"],
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "description": "Movie Created",
            "content": {
                "application/json": {
                    "example": {
                        "data": {
                            "title": "The Shawshank Redemption"
                        },
                    },
                },
            },
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "Movie already exists",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Movie 'Name' already exists",
                    },
                },
            },
        },
    },
)
def add_movie(
    title: Annotated[str, Form()],
):
    movies = MOVIES_DATABASE["movies"]
    if any(title.lower() == movie["title"].lower() for movie in movies):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Movie {title!r} already exists",
        )

    # create new item
    new_movie = {"title": title.title()}
    # save to db
    movies.append(new_movie)
    new_movie["id"] = len(movies)
    # respond with new item
    return {
        "data": new_movie,
    }


@router.get(
    "/movies/{movie_id}",
    tags=["Movies"],
    responses={
        status.HTTP_200_OK: {
            "description": "Movie Found",
            "content": {
                "application/json": {
                    "example": {
                        "data": {
                            "title": "The Shawshank Redemption"
                        },
                    },
                },
            },
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Movie not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Movie #1 does not exist",
                    },
                },
            },
        },
    },
)
def get_movie(movie_id: PositiveInt):
    movies = MOVIES_DATABASE["movies"]
    if movie_id > len(movies):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Movie #{movie_id} does not exist",
        )
    movie = movies[movie_id - 1]
    return {
        "data": movie,
    }
