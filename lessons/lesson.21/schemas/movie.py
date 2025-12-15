from pydantic import BaseModel


class MovieBase(BaseModel):

    title: str
    year: int
    description: str


class Movie(BaseModel):
    id: int
    title: str
    year: int
    description: str


# class MovieCreate(Movie):
#     id: int
#



movie_list = [
    Movie(
        id=1,
        title='Movie1',
        year=1999,
        description='Movie description 1',
    ),
    Movie(
        id=2,
        title='Movie2',
        year=2005,
        description='Movie description 2',
    ),
    Movie(
        id=3,
        title='Movie3',
        year=2005,
        description='Movie description 3',
    ),
    Movie(
        id=4,
        title='Movie4',
        year=2009,
        description='Movie description 4',
    ),
    Movie(
        id=5,
        title='Movie5',
        year=1999,
        description='Movie description 5',
    ),
]