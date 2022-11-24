from notes.models import ToDoItem, ToDoList
from rest_framework import serializers


class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ["order", "is_done", "description", "id"]


class ToDoListSerializer(serializers.ModelSerializer):
    todo_items = ToDoItemSerializer(many=True)

    class Meta:
        model = ToDoList
        fields = ["title", "user", "id", "todo_items"]
