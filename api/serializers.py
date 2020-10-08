from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Task
User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.username')
    finished = serializers.DateField(format="%d-%m-%Y ", input_formats=['%d-%m-%Y',])

    class Meta:
        fields = ('id', 'title', 'description', 'created', 'status', 'finished')
        model = Task


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
        write_only_fields = ('password',)

    def validate_username(self, data):
        username = self.context.get('request').data.get('username')
        if User.objects.filter(username=username):
            raise serializers.ValidationError(
                f"User with this username already exist.")
        return data

