from rest_framework import generics

from djangoDrfLearningProject import defaultPermission
from genres.models import Genre

from genres.serializers import GenreSerializer

from rest_framework import permissions

from genres.permissions import GenrePermission

from djangoDrfLearningProject.defaultPermission import DefaultPermission


class GenreCreateList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, DefaultPermission]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, DefaultPermission]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
