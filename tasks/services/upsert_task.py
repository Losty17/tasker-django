from typing import Optional, TypedDict
from tasker.base.service_base import ServiceBase
from tasks.models import Task, TaskCategories


class TaskBody(TypedDict):
    id: Optional[int]
    title: str
    description: str
    priority: int
    status: int
    categories: list[int]


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

        task.save()

        task.categories.clear()
        task_categories = [
            TaskCategories(task=task, category_id=category_id)
            for category_id in self.__body.get("categories", [])
        ]
        TaskCategories.objects.bulk_create(task_categories)

        return True, "Task updated successfully", None
