from pydantic import BaseModel


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