from categories.models import Category
from tasker.base.service_base import ServiceBase


class DeleteCategory(ServiceBase):
    def __init__(self, category_id):
        self.__category_id = category_id

    def _perform(self):
        category = Category.objects.filter(id=self.__category_id).first()

        if category is None:
            return False, "Category not found", None

        category.delete()

        return True, "Category deleted successfully", None
