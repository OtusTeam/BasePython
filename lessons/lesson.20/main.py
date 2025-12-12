from fastapi import FastAPI, Query, HTTPException, status
import uvicorn
from pydantic import BaseModel


app = FastAPI()

class MovieBase(BaseModel):
    title: str
    year: int
    description: str


class Movie(BaseModel):
    title: str
    year: int
    description: str


class MovieCreate(Movie):
    id: int




movie_list = [
    Movie(
        title='Movie1',
        year=1999,
        description='Movie description 1',
    ),
    Movie(
        title='Movie2',
        year=2005,
        description='Movie description 2',
    ),
    Movie(
        title='Movie3',
        year=2005,
        description='Movie description 3',
    ),
    Movie(
        title='Movie4',
        year=2009,
        description='Movie description 4',
    ),
    Movie(
        title='Movie5',
        year=1999,
        description='Movie description 5',
    ),
]


@app.get("/")
async def index():
    """Главная страница."""
    return {"message": "Hello World"}


@app.get("/about/{about_id}/")
async def about(about_id: int):
    """Страница о нас."""
    print(type(about_id))
    print(about_id * 10)
    return {"message": f"About us - {about_id}"}


@app.get("/movies/", response_model=list[Movie])
async def movies(
    year: int = Query(None, description="Год релиза"),
    title: str = Query(None, description="Заголовок фильма"),
):
    result = movie_list
    if year is not None:
        result = [movie for movie in result if movie.year == year]
    if title is not None:
        result = [movie for movie in result if title in movie.title]
    return result


@app.get("/movies/{movie_id}/", response_model=Movie)
async def movie_details(movie_id: int):
    """Получить детальную информацию по фильму."""
    movie_id -= 1
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм с таким id не найден")
    return movie_list[movie_id]


@app.post("/movies/", response_model=Movie, status_code=status.HTTP_201_CREATED)
async def create_movie(movie: Movie):
    """Добавить фильм."""
    for m in movie_list:
        if m.title == movie.title and m.year == movie.year:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Такой фильм уже есть")
    movie_list.append(movie)
    return movie


@app.put("/movies/{movie_id}/", response_model=Movie)
async def update_movie(movie_id: int, movie: Movie):
    """Обновить фильм."""
    movie_id -= 1
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм с таким id не найден")
    movie_list[movie_id].title = movie.title
    movie_list[movie_id].year = movie.year
    return movie_list[movie_id]


@app.delete("/movies/{movie_id}/")
async def delete_movie(movie_id: int):
    """Удалить фильм."""
    movie_id -= 1
    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Фильм с таким id не найден")

    result = movie_list.pop(movie_id)
    return {'message': f'Фильм {result.title} был удален'}


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)