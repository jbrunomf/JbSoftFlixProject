from movies.views import MovieListCreateView, MovieRetrieveUpdateDestroyApiView
from django.urls import path

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>', MovieRetrieveUpdateDestroyApiView.as_view(), name='movie-retrieve-update-destroy'),
]
