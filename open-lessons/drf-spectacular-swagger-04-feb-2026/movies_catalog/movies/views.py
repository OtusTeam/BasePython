from django.db.models import QuerySet
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiExample,
    OpenApiResponse,
)

EXAMPLE_REPONSE_MOVIE_WITH_INCLUDES = OpenApiExample(
    name="Response with included relations",
    value={
        "id": 21,
        "title": "Example Title",
        "description": "Hello description",
        "release_date": "1996-01-12",
        "duration": 89,
        "age_rating": {
            "name": "R",
            "description": "R – Restricted\r\n\r\nUnder 17",
        },
        "genres": [
            {
                "id": 1,
                "name": "comedy",
                "description": "Movies to laugh at",
            },
            {
                "id": 2,
                "name": "criminal",
                "description": "Movies about criminals",
            },
        ],
    },
    response_only=True,
)

EXAMPLE_REPONSE_MOVIE_WITHOUT_INCLUDES = OpenApiExample(
    name="Response without includes",
    value={
        "id": 16,
        "title": "Django Unchained",
        "description": "Movie starts with..",
        "release_date": "2010-01-20",
        "duration": 95,
        "age_rating": "R",
    },
    response_only=True,
)
from rest_framework import viewsets, status
from rest_framework.serializers import Serializer

from movies.models import AgeRating, Movie
from movies.serializers import (
    AgeRatingDetailSerializer,
    AgeRatingSerializer,
    MovieDetailSerializerExtended,
    MovieSerializer,
)


INCLUDE_MOVIE_RELATIONS_PARAMETER = OpenApiParameter(
    name="include",
    description="Join age rating and genres",
    type=OpenApiTypes.STR,
    location=OpenApiParameter.QUERY,
    default="1",
    examples=[
        OpenApiExample(
            "Example 1",
            summary="join related (1)",
            description="joins age rating and genres",
            value="1",
        ),
        OpenApiExample(
            "Example 2",
            summary="join related (7)",
            description="same as 1, but lucky",
            value="7",
        ),
    ],
)
list_view_description = """\
### List available movies

Technologies used:

- Django
- DRF
- drf-spectacular

Example API call:

```bash
curl -X 'GET' 'http://127.0.0.1:8000/api/movies/'
```
"""


@extend_schema_view(
    list=extend_schema(
        description=list_view_description,
        responses={
            # status.HTTP_200_OK: MovieSerializer,
            status.HTTP_200_OK: OpenApiResponse(
                response="application/json",
                description="Movie details list",
                examples=[
                    EXAMPLE_REPONSE_MOVIE_WITHOUT_INCLUDES,
                    EXAMPLE_REPONSE_MOVIE_WITH_INCLUDES,
                ],
            ),
        },
        parameters=[
            INCLUDE_MOVIE_RELATIONS_PARAMETER,
        ],
    ),
    retrieve=extend_schema(
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                response="application/json",
                description="Movie details",
                examples=[
                    EXAMPLE_REPONSE_MOVIE_WITHOUT_INCLUDES,
                    EXAMPLE_REPONSE_MOVIE_WITH_INCLUDES,
                ],
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                response="application/json",
                examples=[
                    OpenApiExample(
                        name="Movie not found",
                        value={
                            "detail": "No Movie matches the given query.",
                        },
                    ),
                ],
            ),
        },
        parameters=[
            INCLUDE_MOVIE_RELATIONS_PARAMETER,
        ],
    ),
    create=extend_schema(
        responses={
            status.HTTP_201_CREATED: MovieSerializer,
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response="application/json",
                examples=[
                    OpenApiExample(
                        name="Invalid request parameters / body",
                        value={
                            "age_rating": [
                                'Invalid pk "qwerty" - object does not exist.'
                            ]
                        },
                    ),
                    OpenApiExample(
                        name="Missing required field",
                        value={
                            "title": ["This field is required."],
                        },
                    ),
                ],
            ),
        },
    ),
)
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self) -> QuerySet:
        qs = self.queryset
        # if self.action == "retrieve":
        if self.request.GET.get("include"):
            # if self.action == "retrieve":
            qs = qs.select_related("age_rating").prefetch_related("genres")
        return qs

    def get_serializer_class(self) -> type[Serializer]:
        if self.request.GET.get("include"):
            # if self.action == "retrieve":
            #     return MovieDetailSerializerExtended
            return MovieDetailSerializerExtended
        return MovieSerializer


class AgeRatingViewSet(viewsets.ModelViewSet):
    queryset = AgeRating.objects.all()

    def get_queryset(self) -> QuerySet:
        qs = self.queryset
        if self.action == "retrieve":
            qs = qs.prefetch_related("movies")
        return qs

    def get_serializer_class(self) -> type[Serializer]:
        if self.action == "retrieve":
            return AgeRatingDetailSerializer
        return AgeRatingSerializer
