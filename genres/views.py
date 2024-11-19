from rest_framework import generics

from genres.models import Genre

from genres.serializers import GenreSerializer

from rest_framework import permissions

from genres.permissions import GenrePermission


class GenreCreateList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, GenrePermission]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, GenrePermission]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
