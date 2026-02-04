import textwrap

from django.contrib import admin

from movies.models import AgeRating, Genre, Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "release_date",
        "duration",
        "age_rating",
    )
    list_display_links = (
        "id",
        "title",
    )
    list_filter = (
        "title",
        "release_date",
        "age_rating",
    )
    search_fields = (
        "title",
        "description",
    )


@admin.register(AgeRating, Genre)
class AgeRatingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "short_description",
    )
    list_display_links = ("name",)
    list_filter = ("name",)
    search_fields = (
        "name",
        "description",
    )

    def short_description(self, obj: AgeRating) -> str:
        description = obj.description.replace("\r\n", "\n")
        if "\n\n" in description:
            description = description.split("\n\n")[0]
        return textwrap.wrap(description, width=50)[0]
