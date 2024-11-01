from django.urls import path

from genres.views import GenreCreateList, GenreRetrieveUpdateDestroy

urlpatterns = [
    path('', GenreCreateList.as_view(), name='genre-create-list'),
    path('<int:pk>', GenreRetrieveUpdateDestroy.as_view(), name='genre-retrieve-update-destroy'),
]
