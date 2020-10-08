from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, filters, generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import Task, History
from api.permissions import IsAuthor
from api.serializers import TaskSerializer, UsersSerializer

User = get_user_model()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthor]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=status', '=finished']

    def get_queryset(self):
        queryset = Task.objects.filter(author=self.request.user).all()
        return queryset

    def create_history(self, data, request):
        task_title = data.get('title')
        task = get_object_or_404(Task, title=task_title)
        status = task.status
        History.objects.create(task=task, author=request.user, status=status)

    def change_new_status(self, data, request):
        task_title = data.get('title')
        task = get_object_or_404(Task, title=task_title)
        status = data.get('status')
        History.objects.create(task=task, author=request.user, status=status)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.create_history(serializer.validated_data, request)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(generics.CreateAPIView):
    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if serializer.is_valid():
            username = self.request.data.get('username')
            password = self.request.data.get('password')
            new_user = User.objects.create(username=username, is_active=True)
            new_user.set_password(password)
            new_user.save()
