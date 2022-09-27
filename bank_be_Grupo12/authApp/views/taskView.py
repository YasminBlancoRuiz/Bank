from rest_framework import viewsets
from authApp.serializers import TaskSerializer
from authApp.models import Task

#from rest_framework.permissions import IsAuthenticated

#crud
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    #permission_classes = (IsAuthenticated,)