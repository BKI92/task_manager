from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import TaskViewSet, UserViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', UserViewSet.as_view()),

]

