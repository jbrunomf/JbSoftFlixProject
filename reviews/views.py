from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewModelSerializer
from rest_framework import permissions
from djangoDrfLearningProject.defaultPermission import DefaultPermission


class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, DefaultPermission]
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, DefaultPermission]
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer
