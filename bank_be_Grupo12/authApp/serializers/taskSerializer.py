from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from authApp.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'owner']