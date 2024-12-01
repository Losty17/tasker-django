import json
from django.http import HttpRequest, JsonResponse

from tasker.base.base_view import BaseView
from tasks.services.delete_task import DeleteTask
from tasks.services.get_task_list import GetTaskList
from tasks.services.upsert_task import UpsertTask


class Tasks(BaseView):
    def get(self, request: HttpRequest) -> JsonResponse:
        success, detail, data = GetTaskList().perform()

        return self.build_response(success, detail, data)

    def post(self, request: HttpRequest) -> JsonResponse:
        body = json.loads(request.body)

        if body is None or not isinstance(body, dict):
            return self.build_response(False, "Invalid request body", None)

        if not "id" in body:
            required_fields = ["title", "description"]

            for field in required_fields:
                if field not in body:
                    return self.build_response(
                        False, f"Missing required field: {field}", None
                    )

        success, detail, data = UpsertTask(body).perform()

        return self.build_response(success, detail, data)

    def delete(self, request: HttpRequest) -> JsonResponse:
        body = json.loads(request.body)

        if body is None or not isinstance(body, dict):
            return self.build_response(False, "Invalid request body", None)

        if "id" not in body:
            return self.build_response(False, "Missing required field: id", None)

        success, detail, data = DeleteTask(body["id"]).perform()

        return self.build_response(success, detail, data)
