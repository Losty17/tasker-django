from tasker.base.service_base import ServiceBase
from tasks.models import Task
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models.functions import JSONObject, Coalesce
from django.db.models import Case, When, Value, Subquery, OuterRef, Q


class GetTask(ServiceBase):
    def __init__(self, id: int) -> None:
        super().__init__()
        self.__id = id

    def _perform(self):
        tasks = list(
            Task.objects.filter(deleted=False, id=self.__id)
            .annotate(
                categories_list=Coalesce(
                    ArrayAgg(
                        JSONObject(
                            id="categories__id",
                            name="categories__name",
                            description="categories__description",
                        ),
                        filter=~Q(
                            categories__id__isnull=True
                        ),  # Filter out null categories
                        distinct=True,
                    ),
                    Value([]),  # Default to empty list when no categories
                )
            )
            .annotate(
                responsible_list=Coalesce(
                    ArrayAgg(
                        JSONObject(
                            id="responsibles__id",
                            name="responsibles__first_name",
                        ),
                        filter=~Q(
                            responsibles__id__isnull=True
                        ),  # Filter out null users
                        distinct=True,
                    ),
                    Value([]),  # Default to empty list when no users
                )
            )
            .values(
                "id",
                "title",
                "description",
                "created_at",
                "updated_at",
                "priority",
                "status",
                "categories_list",
            )
        )

        task = tasks[0] if tasks else None

        if not task:
            return False, "Task not found", None

        return True, "Tasks retrieved successfully", task
