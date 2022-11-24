from rest_framework import serializers

from notes.models import ToDoItem, ToDoList


class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ["order", "is_done", "description", "id"]


class ToDoListSerializer(serializers.ModelSerializer):
    todo_items = ToDoItemSerializer(many=True)

    class Meta:
        model = ToDoList
        fields = ["title", "user", "id", "todo_items"]
