"""
URL configuration for djangoDrfLearningProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateList, GenreRetrieveUpdateDestroy

from actors.views import ActorCreateList, ActorRetrieveUpdateDestroy

from movies.views import MovieListCreateApiView, MovieRetrieveUpdateDestroyApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateList.as_view(), name='genre-create-list'),
    path('genres/<int:pk>', GenreRetrieveUpdateDestroy.as_view(), name='genre-retrieve-update-destroy'),
    path('actors/', ActorCreateList.as_view(), name='actor-create-list'),
    path('actors/<int:pk>', ActorRetrieveUpdateDestroy.as_view(), name='actor-retrieve-update-destroy'),
    path('movies/', MovieListCreateApiView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>', MovieRetrieveUpdateDestroyApiView.as_view(), name='movie-retrieve-update-destroy'),
]
