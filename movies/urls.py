from movies.views import MovieListCreateView, MovieRetrieveUpdateDestroyApiView, MovieStatisticsView
from django.urls import path

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>', MovieRetrieveUpdateDestroyApiView.as_view(), name='movie-retrieve-update-destroy'),
    path('movies/statistics/', MovieStatisticsView.as_view(), name='movie-statistics')
]
