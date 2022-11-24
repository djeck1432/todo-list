from django.urls import include, path
from rest_framework import routers

from notes.views import TodoItemsViewSet, TodoListViewSet

router = routers.DefaultRouter()
router.register(r"todo-list", TodoListViewSet, basename="todo")
router.register(r"todo-item", TodoItemsViewSet, basename="todo-item")

urlpatterns = [
    path("", include(router.urls)),
]
