"""
Create
Read
Update
Delete
"""
from pydantic import BaseModel

from .schema import Movie, MovieCreate


class MoviesStorage(BaseModel):
    last_id: int = 0
    movies: dict[int, Movie] = {}

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def get(self) -> list[Movie]:
        return list(self.movies.values())

    def get_by_id(self, movie_id: int) -> Movie | None:
        return self.movies.get(movie_id)

    def add(self, movie_in: MovieCreate) -> Movie:
        movie = Movie(
            id=self.next_id,
            **movie_in.model_dump(),
        )
        self.movies[movie.id] = movie
        return movie

    def delete(self, movie_id: int) -> None:
        self.movies.pop(movie_id, None)


storage = MoviesStorage()

storage.add(
    MovieCreate(
        title="The Shawshank Redemption",
        year=1994,
    ),
)
storage.add(
    MovieCreate(
        title="Pulp Fiction",
        year=1994,
    ),
)
storage.add(
    MovieCreate(
        title="The Game",
        year=1997,
    ),
)