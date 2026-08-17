from fastapi import FastAPI, Query, HTTPException, status
from pydantic import BaseModel
import uvicorn


app = FastAPI()


class Movie(BaseModel):
    title: str
    year: int
    description: str


movie_list = [
    Movie(
        title="My first movie",
        year=1999,
        description="My first movie by 1999",
    ),
    Movie(
        title="My second movie",
        year=1989,
        description="My second movie by 1989",
    ),
    Movie(
        title="My third movie",
        year=2000,
        description="My third movie by 2000",
    ),
    Movie(
        title="My fourth movie",
        year=2001,
        description="My fourth movie by 2001",
    ),
    Movie(
        title="My fifth movie",
        year=2002,
        description="My fifth movie by 2002",
    )
]

@app.get("/")
async def index():
    return {"Hello123": "World567"}


@app.get("/movies/", response_model=list[Movie])
async def movies(
    year: int = Query(None, description="Год фильма"),
    title: str = Query(None, description="Заголовок фильма"),
):
    """Получить список фильмов."""
    result = movie_list

    if title is not None:
        result = [movie for movie in result if title in movie.title]
    if year is not None:
        result = [movie for movie in result if movie.year >= year]

    return result


@app.get("/movies/{movie_id}", response_model=Movie)
async def movie_detail(movie_id: int):
    """Получить детальную информацию по фильму."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм не найден")

    return movie_list[movie_id]


@app.post("/movies/", response_model=Movie, status_code=status.HTTP_201_CREATED)
async def movie_create(movie: Movie):
    """Добавить фильм."""

    for m in movie_list:
        if m.title == movie.title and m.year == movie.year:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Такой фильм уже есть")

    movie_list.append(movie)
    return movie


@app.put("/movies/{movie_id}", response_model=Movie)
async def movie_update(movie_id: int, movie: Movie):
    """Изменить фильм."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм не найден")

    movie_list[movie_id].title = movie.title
    movie_list[movie_id].year = movie.year

    return movie_list[movie_id]


@app.delete("/movies/{movie_id}")
async def movie_deletee(movie_id: int):
    """Изменить фильм."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм не найден")

    result = movie_list.pop(movie_id)

    return {"Message": f"Фильм {result.title} был удален"}


@app.get("/authors/{author_id}/{age}/{city}/")
async def author_detail(author_id: int, age: int, city: str):
    print(author_id, city, age)
    print(type(author_id))
    print(author_id * 100 + 10)

    return {"author_id": author_id}


@app.get("/authors/")
async def author_detail(
    name: str = Query(None, description="Name author"),
    age: int = Query(None, description="Age author"),
    city: str = Query(None, description="City author"),
):
    print(name, age, city)

    return {"author": f"{name} {age} {city}"}


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)