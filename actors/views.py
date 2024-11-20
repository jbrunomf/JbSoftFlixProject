from rest_framework import generics
from rest_framework import permissions
from actors.models import Actor
from actors.serializers import ActorSerializer
from djangoDrfLearningProject.defaultPermission import DefaultPermission


class ActorCreateList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, DefaultPermission]
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, DefaultPermission]
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
