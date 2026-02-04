"""
- `title` - str, CI (если PG), not null, index - для поиска
- `description` - описание фильма - not null, default `""`
- `release_date` - старт проката - `date`, nullable
- `duration` - продолжительность фильма в минутах - uint, nullable
- `age_rating` - возрастной рейтинг, ссылка на сущность, nullable

"""

from django.db import models


class Movie(models.Model):

    title = models.CharField(max_length=120, db_index=True)
    description = models.TextField(blank=True, null=False)
    release_date = models.DateField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    age_rating = models.ForeignKey(
        to="AgeRating",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="movies",
    )
    genres = models.ManyToManyField(
        to="Genre",
        blank=True,
        related_name="movies",
    )

    class Meta:
        ordering = ("id",)

    def __str__(self) -> str:
        return self.title
