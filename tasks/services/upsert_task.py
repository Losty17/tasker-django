from typing import Optional, TypedDict
from tasker.base.service_base import ServiceBase
from tasks.models import Task, TaskCategories, TaskResponsibles
from django.contrib.auth.models import User


class TaskBody(TypedDict):
    id: Optional[int]
    title: str
    description: str
    priority: int
    status: int
    user_id: int
    categories: list[int]
    responsibles: list[int]


class UpsertTask(ServiceBase):
    def __init__(self, body: TaskBody) -> None:
        super().__init__()

        self.__body = body

    def _perform(self):
        task = None
        if self.__body.get("id", None):
            task = Task.objects.filter(id=self.__body["id"], deleted=False).first()

            if task is None:
                return False, "Task not found", None
        else:
            task = Task()

        task.title = self.__body.get("title", task.title)
        task.description = self.__body.get("description", task.description)
        task.priority = self.__body.get("priority", task.priority)
        task.status = self.__body.get("status", task.status)

        user = User.objects.filter(id=self.__body.get("user_id", task.user_id)).first()

        if user is None:
            return False, "User not found", None

        task.user = user

        task.save()

        task.categories.clear()
        task_categories = [
            TaskCategories(task=task, category_id=category_id)
            for category_id in self.__body.get("categories", [])
        ]
        TaskCategories.objects.bulk_create(task_categories)

        task.responsibles.clear()
        task_responsibles = [
            TaskResponsibles(task=task, responsible_id=user_id)
            for user_id in self.__body.get("responsibles", [])
        ]
        TaskResponsibles.objects.bulk_create(task_responsibles)

        return True, "Task updated successfully", None
