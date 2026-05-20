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
        title="Movie1",
        year=2009,
        description="My Movie 1 description",
    ),
    Movie(
        title="Movie2",
        year=2020,
        description="My Movie 2 description",
    ),
    Movie(
        title="Movie3",
        year=2009,
        description="My Movie 3 description",
    ),
    Movie(
        title="Movie4",
        year=2021,
        description="My Movie 4 description",
    ),
    Movie(
        title="Movie5",
        year=2019,
        description="My Movie 15description",
    ),
]

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/about/{about_id}/author/{author_id}/")
async def about(about_id: str, author_id: int):
    print(about_id)
    print(type(about_id))
    print(author_id)
    print(type(author_id))
    return {"message": f"About us  {about_id}, {author_id}"}


@app.get("/contact/")
async def contact(
    name: str = Query(None, description="Name of contact"),
    age: int = Query(None, description="Age of contact"),
):
    print(name)
    print(type(name))
    print(age)
    print(type(age))
    return {"message": f"Contact {name} {age}"}


@app.get("/movies/", response_model=list[Movie])
async def movies(
    year: int = Query(None, description="Год фильма"),
    title: str = Query(None, description="Заголовок фильма"),
):
    """Получить список фильмов."""
    result = movie_list

    if title is not None:
        result = [movie for movie in result if movie.title == title]
    if year is not None:
        result = [movie for movie in result if movie.year == year]

    return result


@app.get("/movies/{movie_id}/", response_model=Movie)
async def movie_details(movie_id: int):
    """Получить детальную информацию о фильме."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    return movie_list[movie_id]


@app.post("/movies/", response_model=Movie, status_code=status.HTTP_201_CREATED)
async def movie_create(movie: Movie):
    """Добавить фильм."""
    for m in movie_list:
        if m.title == movie.title and m.year == movie.year:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Такой фильм уже есть")

    movie_list.append(movie)

    return movie


@app.put("/movies/{movie_id}/", response_model=Movie)
async def movie_update(movie_id: int, movie: Movie):
    """Обновить фильм."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    movie_list[movie_id].title = movie.title
    movie_list[movie_id].year = movie.year

    return movie_list[movie_id]


@app.delete("/movies/{movie_id}/")
async def movie_update(movie_id: int):
    """Удалить фильм."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    result = movie_list.pop(movie_id)

    return {'message': f'Фильм {result.title} был удалеен'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)