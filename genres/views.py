from rest_framework import generics

from genres.models import Genre

from genres.serializers import GenreSerializer


class GenreCreateList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
