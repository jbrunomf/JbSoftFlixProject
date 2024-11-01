from django.urls import path
from actors.views import ActorCreateList, ActorRetrieveUpdateDestroy

urlpatterns = [
    path('actors/', ActorCreateList.as_view(), name='actor-create-list'),
    path('actors/<int:pk>', ActorRetrieveUpdateDestroy.as_view(), name='actor-retrieve-update-destroy'),
]
