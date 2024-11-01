from django.urls import path
from actors.views import ActorCreateList, ActorRetrieveUpdateDestroy

urlpatterns = [
    path('', ActorCreateList.as_view(), name='actor-create-list'),
    path('<int:pk>', ActorRetrieveUpdateDestroy.as_view(), name='actor-retrieve-update-destroy'),
]
