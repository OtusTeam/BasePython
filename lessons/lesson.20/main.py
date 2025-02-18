import random
from typing import Annotated

import uvicorn

from fastapi import FastAPI, Header, status, Form, Query, HTTPException
from pydantic import PositiveInt

app = FastAPI()


@app.get("/")
def get_root():
    """
    Получение корня сайта.
    """
    return {
        "message": "Hello World",
        "docs": "http://127.0.0.1:8000/docs",
    }


@app.get("/hello")
def reply_hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/add", tags=["Numbers"])
def count_add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "sum": a + b,
    }


@app.get("/random-numbers", tags=["Numbers", "Random"])
def generate_random_numbers(
    count: PositiveInt,
):
    return {
        "numbers": [
            random.randint(1, 10000)
            for _ in range(count)
        ]
    }


@app.get("/items", tags=["Items"])
def get_items():
    return {
        "data": [
            {"item_id": 1, "name": "item-1"},
            {"item_id": 2, "name": "item-2"},
            {"item_id": 3, "name": "item-3"},
        ],
    }


@app.post(
    "/items",
    tags=["Items"],
    status_code=status.HTTP_201_CREATED,
)
def create_item(
    name: Annotated[str, Form()],
):
    return {
        "data": {"item_id": 0, "name": name},
    }


@app.get("/items/{item_id}", tags=["Items"])
def get_item(item_id: PositiveInt):
    return {
        "data": {
            "item_id": item_id,
            "name": f"item-{item_id}",
        },
    }


@app.get("/me")
def get_me(
    # username: str = Header(),
    username: Annotated[str, Header()],
):
    return {"username": username}

#
#
#
#
#
#
#
#
#
#


MOVIES_DATABASE = {
    "movies": [
        {"title": "Django Unchained"},
        {"title": "Chain Reaction"},
        {"title": "Pulp Fiction"},
    ],
}

for idx, movie_obj in enumerate(MOVIES_DATABASE["movies"], start=1):
    movie_obj["id"] = idx



@app.get(
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


@app.post(
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


@app.get(
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


if __name__ == "__main__":
    # uvicorn.run(app)
    uvicorn.run("main:app", reload=True)
