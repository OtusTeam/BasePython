from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    year: int
    description: str


class Movie(MovieBase):
    id: int


movie_list = [
    Movie(
        id = 1,
        title = "First",
        year = 2020,
        description = "My first movie description",
    ),
    Movie(
        id = 2,
        title = "My second movie",
        year = 2021,
        description = "My second movie description",
    ),
    Movie(
        id=3,
        title = "My third movie",
        year = 2020,
        description = "My third movie description",
    ),
    Movie(
        id=4,
        title = "My fourth movie",
        year = 2021,
        description = "My fourth movie description",
    ),
    Movie(
        id=5,
        title="Five",
        year = 2022,
        description = "My five movie description",
    )
]