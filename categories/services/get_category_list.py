from categories.models import Category
from tasker.base.service_base import ServiceBase
from tasks.models import Task
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models.functions import JSONObject, Coalesce
from django.db.models import Case, When, Value, Subquery, OuterRef, Q


class GetCategoryList(ServiceBase):
    def __init__(self) -> None:
        super().__init__()

    def _perform(self):
        categories = list(
            Category.objects.filter(deleted=False).values(
                "id",
                "name",
                "description",
            )
        )

        return True, "Categories retrieved successfully", categories
