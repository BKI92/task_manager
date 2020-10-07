from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'title', 'description', 'created', 'status', 'finished')
        model = Task
