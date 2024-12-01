from tasker.base.service_base import ServiceBase
from django.contrib.auth.models import User
from django.db.models import F


class GetUserList(ServiceBase):
    def __init__(self) -> None:
        super().__init__()

    def _perform(self):
        users = list(
            User.objects.filter()
            .annotate(
                name=F("first_name"),
            )
            .values(
                "id",
                "name",
                "username",
            )
        )

        return True, "Users retrieved successfully", users
