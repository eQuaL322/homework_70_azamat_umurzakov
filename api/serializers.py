from rest_framework import serializers
from django.contrib.auth.models import User

from issue_tracker.models import Project, Status, Type, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'start_date', 'end_date', 'name', 'description', 'users']
        read_only_fields = ['id', 'start_date', 'end_date']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class TaskSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)
    types = TypeSerializer(many=True, read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'summary', 'description', 'status', 'types', 'created_at', 'updated_at', 'project']
        read_only_fields = ['id', 'created_at', 'updated_at']
