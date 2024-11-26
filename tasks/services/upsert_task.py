from typing import Optional, TypedDict
from tasker.base.service_base import ServiceBase
from tasks.models import Task


class TaskBody(TypedDict):
    id: Optional[int]
    title: str
    description: str


class UpsertTask(ServiceBase):
    def __init__(self, body: TaskBody) -> None:
        super().__init__()

        self.__body = body

    def _perform(self):
        task = None
        if self.__body.get("id", None):
            task = Task.objects.filter(id=self.__body["id"], deleted=False).first()
        else:
            task = Task()

        if task is None:
            return False, "Task not found", None

        task.title = self.__body["title"]
        task.description = self.__body["description"]
        task.save()

        return True, "Task updated successfully", None
