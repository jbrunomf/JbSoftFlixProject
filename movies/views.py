from rest_framework import generics

from movies.models import Movie

from movies.serializers import MovieSerializer

from rest_framework import permissions

class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


