from rest_framework import generics
from rest_framework import permissions
from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorCreateList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
