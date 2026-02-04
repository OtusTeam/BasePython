from movies.serializers.age_rating_base import AgeRatingSerializer
from movies.serializers.movie_base import MovieSerializer


class AgeRatingDetailSerializer(AgeRatingSerializer):
    movies = MovieSerializer(
        many=True,
        read_only=True,
    )

    class Meta(AgeRatingSerializer.Meta):
        fields = (
            *AgeRatingSerializer.Meta.fields,
            "movies",
        )
