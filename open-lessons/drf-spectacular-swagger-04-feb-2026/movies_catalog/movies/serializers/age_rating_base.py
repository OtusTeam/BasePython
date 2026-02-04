from rest_framework import serializers

from movies.models import AgeRating


class AgeRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeRating
        fields = (
            "name",
            "description",
        )
