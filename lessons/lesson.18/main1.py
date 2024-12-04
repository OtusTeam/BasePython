from typing import Optional
from xml.dom.xmlbuilder import Options

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

movies = []

class Movie(BaseModel):
    id_: int
    title: str
    description: str
    genre: str
    year: Optional[int] = None

movies.append(Movie(id_=1, title="Movie 1", description="Description 1", genre="Genre 1", year=2022))
movies.append(Movie(id_=2, title="Movie 2", description="Description 2", genre="Genre 2", year=2023))
movies.append(Movie(id_=3, title="Movie 3", description="Description 3", genre="Genre 3", year=2024))
movies.append(Movie(id_=4, title="Movie 4", description="Description 4", genre="Genre 4", year=2025))
movies.append(Movie(id_=5, title="Movie 5", description="Description 5", genre="Genre 3", year=2026))


@app.get("/movies/")
async def all_movies():
    return {"movies": movies}


@app.post("/movie/add")
async def add_movie(movie: Movie):
    movies.append(movie)
    return {"movie": movie, "status": "added"}


@app.get("/movies/{genre}")
async def get_movies_genre(genre: str):
    tmp = []
    for m in movies:
        if m.genre == genre:
            tmp.append(m)
    return {"movies": tmp}


@app.put("/movies/update/{movie_id}")
async def update_movies(movie_id: int, movie: Movie):
    for m in movies:
        if m.id_ == movie_id:
            m.title = movie.title
            m.description = movie.description
            m.genre = movie.genre
            return {"movie": movie, "status": "updated"}


if __name__ == '__main__':
    uvicorn.run("main1:app", host='127.0.0.1', port=8000)