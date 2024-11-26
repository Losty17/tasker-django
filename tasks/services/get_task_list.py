from tasker.base.service_base import ServiceBase
from tasks.models import Task


class GetTaskList(ServiceBase):
    def __init__(self) -> None:
        super().__init__()

    def _perform(self):
        tasks = Task.objects.filter(deleted=False).all()

        return True, "Tasks retrieved successfully", []
