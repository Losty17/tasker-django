import json
from django.http import HttpRequest, JsonResponse

from core.services.delete_user import DeleteUser
from core.services.get_user_list import GetUserList
from core.services.upsert_user import UpsertUser
from tasker.base.base_view import BaseView


class Users(BaseView):
    def get(self, request: HttpRequest) -> JsonResponse:
        success, detail, data = GetUserList().perform()

        return self.build_response(success, detail, data)

    def post(self, request: HttpRequest) -> JsonResponse:
        body = json.loads(request.body)

        if body is None or not isinstance(body, dict):
            return self.build_response(False, "Invalid request body", None)

        if not "id" in body:
            required_fields = ["name", "username"]

            for field in required_fields:
                if field not in body:
                    return self.build_response(False, f"{field} is required", None, 400)

        success, detail, data = UpsertUser(body).perform()
        return self.build_response(success, detail, data)

    def delete(self, request: HttpRequest) -> JsonResponse:
        body = json.loads(request.body)

        if body is None or not isinstance(body, dict):
            return self.build_response(False, "Invalid request body", None)

        if "id" not in body:
            return self.build_response(False, "Missing required field: id", None)

        success, detail, data = DeleteUser(body["id"]).perform()

        return self.build_response(success, detail, data)
