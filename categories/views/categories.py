import json
from django.http import HttpRequest, JsonResponse

from categories.services.delete_category import DeleteCategory
from categories.services.get_category_list import GetCategoryList
from categories.services.upsert_category import UpsertCategory
from tasker.base.base_view import BaseView


class Categories(BaseView):
    def get(self, request: HttpRequest) -> JsonResponse:
        success, detail, data = GetCategoryList().perform()

        return self.build_response(success, detail, data)

    def post(self, request: HttpRequest) -> JsonResponse:
        body = json.loads(request.body)

        if body is None or not isinstance(body, dict):
            return self.build_response(False, "Invalid request body", None)

        if not "id" in body:
            required_fields = ["name", "description"]

            for field in required_fields:
                if field not in body:
                    return self.build_response(False, f"{field} is required", None, 400)

        success, detail, data = UpsertCategory(body).perform()
        return self.build_response(success, detail, data)

    def delete(self, request: HttpRequest) -> JsonResponse:
        body = json.loads(request.body)

        if body is None or not isinstance(body, dict):
            return self.build_response(False, "Invalid request body", None)

        if "id" not in body:
            return self.build_response(False, "Missing required field: id", None)

        success, detail, data = DeleteCategory(body["id"]).perform()

        return self.build_response(success, detail, data)
