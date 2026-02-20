import uvicorn
from fastapi import FastAPI, Query, HTTPException, status
from pydantic import BaseModel


app = FastAPI()


class Movie(BaseModel):
    title: str
    year: int
    description: str


movie_list = [
    Movie(
        title = "First",
        year = 2020,
        description = "My first movie description",
    ),
    Movie(
        title = "My second movie",
        year = 2021,
        description = "My second movie description",
    ),
    Movie(
        title = "My third movie",
        year = 2020,
        description = "My third movie description",
    ),
    Movie(
        title = "My fourth movie",
        year = 2021,
        description = "My fourth movie description",
    ),
    Movie(
        title="Five",
        year = 2022,
        description = "My five movie description",
    )
]


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/about/{about_id}/{my_id}/")
async def about(about_id: int, my_id: int):
    print(type(about_id))
    print(type(my_id))
    print(about_id * my_id)

    return {"message": f"About us {about_id}"}


@app.get("/contact/")
async def contact(
    name: str = Query(None, description="Name of contact"),
    age: int = Query(None, description="Age of contact"),
):
    print(type(name))
    print(type(age))
    print(f"Contact  {name} {age}")

    return {"message": f"Contact  {name} {age}"}


@app.get("/movies/", response_model=list[Movie])
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
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Movie already exists")
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
async def movie_details(movie_id: int):
    """Удалить фильм."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

    result = movie_list.pop(movie_id)

    return {'message': f'Фильм {result.title} был удален'}


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
