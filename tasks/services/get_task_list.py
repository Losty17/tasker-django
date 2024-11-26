from tasker.base.service_base import ServiceBase
from tasks.models import Task


class GetTaskList(ServiceBase):
    def __init__(self) -> None:
        super().__init__()

    def _perform(self):
        tasks = list(
            Task.objects.select_related("categories")
            .filter(deleted=False)
            .values(
                "id",
                "title",
                "description",
                "created_at",
                "updated_at",
                "priority",
                "status",
                "categories__category__name",
            )
        )

        return True, "Tasks retrieved successfully", tasks
