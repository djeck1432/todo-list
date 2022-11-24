from django.contrib.auth.models import User
from django.db import models


class ToDoList(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ToDoItem(models.Model):
    order = models.IntegerField(
        default=0,
        unique=True,
        verbose_name="Order",
    )
    description = models.TextField(verbose_name="Item description")
    is_done = models.BooleanField(default=False, verbose_name="Is item done")
    todo_list = models.ForeignKey(
        ToDoList,
        related_name="todo_items",
        verbose_name="To Do List",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["order"]
