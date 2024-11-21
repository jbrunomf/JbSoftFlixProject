from datetime import datetime

from django.db.models import Avg
from rest_framework import serializers

from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        return round(obj.reviews.aggregate(average=Avg('rating'))['average'], 1) if obj.reviews.exists() else None

    def validate_release_date(self, value: datetime):
        if not value.year >= 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990')


class MovieListDetailSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'synopsis', 'rate']

    def get_rate(self, obj):
        return round(obj.reviews.aggregate(average=Avg('rating'))['average'], 1) if obj.reviews.exists() else None
