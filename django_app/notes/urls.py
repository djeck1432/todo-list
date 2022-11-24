from django.urls import include, path
from notes.views import TodoItemsViewSet, TodoListViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"todo-list", TodoListViewSet, basename="todo")
router.register(r"todo-item", TodoItemsViewSet, basename="todo-item")

urlpatterns = [
    path("", include(router.urls)),
]
