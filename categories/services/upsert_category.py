from typing import Optional, TypedDict
from categories.models import Category
from tasker.base.service_base import ServiceBase
from tasks.models import Task, TaskCategories


class CategoryBody(TypedDict):
    id: Optional[int]
    name: str
    description: str


class UpsertCategory(ServiceBase):
    def __init__(self, body: CategoryBody) -> None:
        super().__init__()

        self.__body = body

    def _perform(self):
        category = None
        if self.__body.get("id", None):
            category = Category.objects.filter(
                id=self.__body["id"], deleted=False
            ).first()

            if category is None:
                return False, "Task not found", None
        else:
            category = Category()

        category.name = self.__body.get("title", category.title)
        category.description = self.__body.get("description", category.description)

        category.save()

        return True, "Task updated successfully", None
