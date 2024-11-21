from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie

from movies.serializers import MovieSerializer, MovieListDetailSerializer

from rest_framework import permissions

from djangoDrfLearningProject.defaultPermission import DefaultPermission

from reviews.models import Review


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, DefaultPermission]
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MovieSerializer
        return MovieListDetailSerializer


class MovieRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, DefaultPermission]
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MovieSerializer
        return MovieListDetailSerializer

class MovieStatisticsView(views.APIView):
    permission_classes = (IsAuthenticated, DefaultPermission,)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values("genre__name").annotate(count=Count("id"))
        total_reviews = Review.objects.count()
        average_reviews = Review.objects.aggregate(avg_reviews=Avg("rating"))['avg_reviews']

        return response.Response(data={
            "total_movies": total_movies,
            "total_movies by genre": movies_by_genre,
            "total reviews": total_reviews,
            "average reviews": round(average_reviews, 1) if average_reviews else 0,
        }, status=status.HTTP_200_OK)
