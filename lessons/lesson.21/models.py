from pydantic import BaseModel, validator


class Movie(BaseModel):
    title: str
    year: int
    description: str | None = None

    @validator("year")
    def chech_year(cls, value):
        if value < 1900:
            raise ValueError("Year must be greater than 1900")
        return value



# class MovieEmail(Movie):
#     email: EmailStr
