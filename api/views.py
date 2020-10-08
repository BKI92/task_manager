from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from rest_framework.permissions import AllowAny

from api.models import Task
from api.permissions import IsAuthorOrReadOnly
from api.serializers import TaskSerializer, UsersSerializer

User = get_user_model()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=status', '=finished']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(generics.ListCreateAPIView):
    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if serializer.is_valid():
            username = self.request.data.get('username')
            password = self.request.data.get('password')
            new_user = User.objects.create(username=username,  is_active=True)
            new_user.set_password(password)
            new_user.save()

