from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel


app = FastAPI()


class Movie(BaseModel):
    title: str
    year: int
    description: str


movie_list = [
    Movie(
        title='Movie1',
        year=1999,
        description='Movie description',
    ),
    Movie(
        title='Movie2',
        year=1992,
        description='Movie description2',
    ),
    Movie(
        title='Movie3',
        year=1949,
        description='Movie description3',
    ),
    Movie(
        title='Movie4',
        year=1999,
        description='Movie description4',
    ),
    Movie(
        title='Movie5',
        year=1939,
        description='Movie description5',
    ),
]

@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/movies/", response_model=list[Movie])
async def movies_list(
    year: int = Query(None, description="Year of release"),
    title: str = Query(None, description="The title of movies")
):
    result = movie_list
    if year is not None:
        result = [movie for movie in result if movie.year == year]
    if title is not None:
        result = [movie for movie in result if movie.title == title]
    return result


@app.get("/movies/{movie_id}/", response_model=Movie)  # это маршрут для разных путей /movies/1 ,  /movies/2
async def movie_details(movie_id: int):
    """Получить детальную информацию по списку."""
    movie_id -= 1
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie_list[movie_id]


@app.post("/movies/", response_model=Movie, status_code=201)
async def movie_create(movie: Movie):
    """Добавить новый фильм."""
    for m in movie_list:
        if m.title == movie.title and m.year == movie.year:
            raise HTTPException(status_code=409, detail="Movie already exists")
    movie_list.append(movie)
    return movie


@app.put("/movies/{movie_id}/", response_model=Movie)
async def movie_update(movie_id: int, movie: Movie):
    """Обновить фильм."""
    movie_id -= 1
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=404, detail="Movie not found")
    movie_list[movie_id].title = movie.title
    movie_list[movie_id].year = movie.year

    return movie_list[movie_id]


@app.delete("/movies/{movie_id}/")
async def movie_update(movie_id: int):
    """Удалить фильм."""
    movie_id -= 1
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=404, detail="Movie not found")

    result = movie_list.pop(movie_id)

    return {'message': f'Movie  {result.title} deleted'}