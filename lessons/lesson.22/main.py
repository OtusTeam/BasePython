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
        title="The Shawshank Redemption",
        year=1994,
        description="Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
    ),
    Movie(
        title="The Godfather",
        year=1972,
        description="The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."
    ),
    Movie(
        title="The Dark Knight",
        year=2008,
        description="When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."
    ),
    Movie(
        title="The Godfather: Part II",
        year=1974,
        description="The early life and career of Vito Corleone in 1920s New York is portrayed while his son, Michael, expands and tightens his grip on his crime syndicate stretching from Lake Tahoe, Nevada to pre-revolution 1958 Cuba."
    ),
    Movie(
        title="The Godfather: Part III",
        year=1990,
        description="After the death of his father, Michael Corleone must decide whether to follow in his footsteps and take over the family business."
    ),
    Movie(
        title="The Shawshank Redemption 2",
        year=1990,
        description="Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
    )
]


@app.get("/")
async def main_page():
    return {"Hello": "World2"}


@app.get("/about/{about_id}/author/{author_id}/")
async def about_page(about_id: int, author_id: str):
    print(about_id)
    print(type(about_id))
    print(author_id)
    print(type(author_id))
    return {"Hello": f"World {about_id} - Имя {author_id}"}


@app.get("/contact/")
async def contact_page(
    name: str = Query(None, description="Name of the contact"),
    age: int = Query(None, description="Age of the contact")
):
    print(name)
    print(type(name))
    print(age)
    print(type(age))
    return {"message": f"Contact: Name - {name}, Age - {age}"}


@app.get("/movies/", response_model=list[Movie])
async def movies(
    year: int = Query(None, description="Year of the movie"),
    title: str = Query(None, description="Title of the movie")
):
    """Получить список фильмов."""
    result = movie_list
    if year is not None:
        result = [movie for movie in result if movie.year >= year]
    if title is not None:
        result = [movie for movie in result if title in movie.title]
    return result


@app.get("/movies/{movie_id}/", response_model=Movie)
async def movie_detail(movie_id: int):
    """Получить детали фильма по его ID."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {movie_id + 1} not found")

    return movie_list[movie_id]


@app.post("/movies/", response_model=Movie, status_code=status.HTTP_201_CREATED)
async def movie_create(movie: Movie):
    """Создать новый фильм."""
    for m in movie_list:
        if m.title == movie.title and m.year == movie.year:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Такой фильм уже существует")
    movie_list.append(movie)
    return movie


@app.put("/movies/{movie_id}/", response_model=Movie)
async def movie_update(movie_id: int, movie: Movie):
    """Обновить фильм."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {movie_id + 1} not found")

    movie_list[movie_id].title = movie.title
    movie_list[movie_id].year = movie.year

    return movie_list[movie_id]


@app.delete("/movies/{movie_id}/")
async def movie_delete(movie_id: int):
    """Удалить фильм."""
    movie_id -= 1

    if movie_id < 0 or movie_id >= len(movie_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {movie_id + 1} not found")

    result = movie_list.pop(movie_id)

    return {'message': f'Movie {result.title} deleted'}


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)