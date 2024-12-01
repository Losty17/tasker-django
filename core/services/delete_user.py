from tasker.base.service_base import ServiceBase
from django.contrib.auth.models import User


class DeleteUser(ServiceBase):
    def __init__(self, user_id):
        self.__user_id = user_id

    def _perform(self):
        category = User.objects.filter(id=self.__user_id).first()

        if category is None:
            return False, "User not found", None

        category.delete()

        return True, "User deleted successfully", None
