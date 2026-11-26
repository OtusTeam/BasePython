from pydantic import BaseModel, Field, field_validator


class MovieBase(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=50,
        description="Название фильма."
    )
    year: int = Field(
        ge=1900,
        le=2050,
        description="Год выпуска фильма."
    )

    # description: str = Field(
    description: str = Field(
        default="Стандартное Описание",
        min_length=10,
        max_length=500,
        description="Описание фильма."
    )
    # genre: str | None = None

    @field_validator("title", mode="before")
    @classmethod
    def clean_title(cls, value) -> str:
        if isinstance(value, str):
            value = value.strip()

            if not value:
                raise ValueError("Название фильма не может состоять из пробелов.")

        return value


class MovieCreate(MovieBase):
    pass


class Movie(MovieBase):
    id: int = Field(
        ge=1,
        description="Идентификатор фильма."
    )


movie_list = [
    Movie(
        id=1,
        title="The Shawshank Redemption",
        year=1994,
        description="Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."

    ),
    Movie(
        id=2,
        title="The Godfather",
        year=1972,
        description="The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."
    ),
    Movie(
        id=3,
        title="The Dark Knight",
        year=2008,
        description="When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."
    ),
    Movie(
        id=4,
        title="The Godfather: Part II",
        year=1974,
        description="The early life and career of Vito Corleone in 1920s New York is portrayed while his son, Michael, expands and tightens his grip on his crime syndicate stretching from Lake Tahoe, Nevada to pre-revolution 1958 Cuba."
    ),
    Movie(
        id=5,
        title="The Godfather: Part III",
        year=1990,
        description="After the death of his father, Michael Corleone must decide whether to follow in his footsteps and take over the family business."
    ),
    Movie(
        id=6,
        title="The Shawshank Redemption 2",
        year=1990,
        description="Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
    )
]