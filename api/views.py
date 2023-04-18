from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from issue_tracker.models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer


class ProjectView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                project = Project.objects.get(pk=pk)
            except Project.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = ProjectSerializer(instance=project)
            return Response(serializer.data)
        else:
            projects = Project.objects.all()
            serializer = ProjectSerializer(instance=projects, many=True)
            return Response(serializer.data)

    def put(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectSerializer(instance=project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        project.delete()
        return Response(pk, status=status.HTTP_204_NO_CONTENT)


class TaskView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                task = Task.objects.get(pk=pk)
            except Task.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = TaskSerializer(instance=task)
            return Response(serializer.data)
        else:
            tasks = Task.objects.all()
            serializer = TaskSerializer(instance=tasks, many=True)
            return Response(serializer.data)

    def put(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response(pk, status=status.HTTP_204_NO_CONTENT)
