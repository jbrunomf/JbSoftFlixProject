from datetime import datetime

from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    # Validaçoes básicas apenas para validar o funcionamento
    def validate_title(self, value: str):
        if not value.lower().startswith('a'):
            raise serializers.ValidationError('O título deve iniciar com a letra A')

    def validate_release_date(self, value: datetime):
        if not value.year >= 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990')
