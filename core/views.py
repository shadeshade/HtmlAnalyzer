from rest_framework import viewsets

from .models import Task
from .serializers import TaskCreateSerializer, TaskRetrieveSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    lookup_field = 'identifier'

    def get_serializer_class(self):
        if self.action == 'create':
            return TaskCreateSerializer
        else:
            return TaskRetrieveSerializer
