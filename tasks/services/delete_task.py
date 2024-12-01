from tasker.base.service_base import ServiceBase
from tasks.models import Task


class DeleteTask(ServiceBase):
    def __init__(self, task_id):
        self.__task_id = task_id

    def _perform(self):
        task = Task.objects.filter(id=self.__task_id).first()

        if task is None:
            return False, "Task not found", None

        task.delete()

        return True, "Task deleted successfully", None
