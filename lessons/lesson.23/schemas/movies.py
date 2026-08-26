from pydantic import BaseModel, Field


class MovieBase(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=50,
    )
    year: int = Field(
        ge=1900,
        le=2100,
    )
    # description: str | None = None
    description: str = Field(
        min_length=10,
        max_length=500,
    )
    genre: str | None = None


class MovieCreate(MovieBase):
    pass


class Movie(MovieBase):
    pk: int | None = None


movie_list = [
    Movie(
        pk=1,
        title="My first movie",
        year=1999,
        description="My first movie by 1999",
    ),
    Movie(
        pk=2,
        title="My second movie",
        year=1989,
        description="My second movie by 1989",
    ),
    Movie(
        pk=3,
        title="My third movie",
        year=2000,
        description="My third movie by 2000",
    ),
    Movie(
        pk=4,
        title="My fourth movie",
        year=2001,
        description="My fourth movie by 2001",
    ),
    Movie(
        pk=5,
        title="My fifth movie",
        year=2002,
        description="My fifth movie by 2002",
    )
]