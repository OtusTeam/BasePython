from django.db import models
from django.shortcuts import reverse


class AgeRating(models.Model):
    name = models.CharField(
        max_length=10,
        primary_key=True,
    )
    description = models.TextField(
        null=False,
        blank=True,
    )

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse(
            "movies:agerating-detail",
            kwargs={"pk": self.name},
        )
