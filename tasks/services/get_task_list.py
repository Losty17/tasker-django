from tasker.base.service_base import ServiceBase
from tasks.models import Task
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models.functions import JSONObject, Coalesce
from django.db.models import Case, When, Value, Subquery, OuterRef, Q


class GetTaskList(ServiceBase):
    def __init__(self) -> None:
        super().__init__()

    def _perform(self):
        tasks = list(
            Task.objects.filter(deleted=False)
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
        return True, "Tasks retrieved successfully", tasks
