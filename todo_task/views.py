from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.utils import timezone


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def overdue(self, request):
        overdue_tasks = self.queryset.filter(user=self.request.user, due_date__lt=timezone.now(), completed=False)
        serializer = self.get_serializer(overdue_tasks, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def status(self, request, pk=None):
        task = self.get_object()
        task.completed = request.data.get('completed', task.completed)
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def filter(self, request):
        created_at = request.query_params.get('created_at')
        updated_at = request.query_params.get('updated_at')
        queryset = self.queryset.filter(user=self.request.user)
        if created_at:
            queryset = queryset.filter(created_at__date=created_at)
        if updated_at:
            queryset = queryset.filter(updated_at__date=updated_at)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
