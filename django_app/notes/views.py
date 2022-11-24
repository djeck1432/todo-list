from notes.models import ToDoItem, ToDoList
from notes.serializers import ToDoItemSerializer, ToDoListSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class CustomAuthToken(ObtainAuthToken):
    """
    Endpoint for getting token to run further api endpoints
    """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})


class TodoItemsViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    """
    ViewSet for managing with TodoItems models
    """

    serializer_class = ToDoItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list__user=self.request.user)


class TodoListViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    """
    ViewSet for managing with ToDoList models
    """

    serializer_class = ToDoListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ToDoList.objects.filter(user=self.request.user)
