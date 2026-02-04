from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from movies.models import Movie


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Movie Details",
            summary="Movie Details example",
            # description="Movie Details example",
            value={
                "id": 16,
                "title": "Django Unchained",
                "description": "Movie starts with..",
                "release_date": "2010-01-20",
                "duration": 95,
                "age_rating": "R",
            },
            response_only=True,
        ),
        OpenApiExample(
            "Movie Creation",
            summary="Create Movie Details",
            description="Body to send to create a new Movie",
            value={
                "title": "SomeTitle",
                "description": "SomeDescription",
                "release_date": "2010-01-20",
                "duration": 90,
                "age_rating": "PG",
            },
            request_only=True,
        ),
    ],
)
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "release_date",
            "duration",
            "age_rating",
        )
