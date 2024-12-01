from categories.models import Category
from tasker.base.service_base import ServiceBase


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
