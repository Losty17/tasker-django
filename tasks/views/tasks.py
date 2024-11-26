import json
from django.http import HttpRequest, JsonResponse

from tasker.base.base_view import BaseView
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

        required_fields = ["title", "description"]

        for field in required_fields:
            if field not in body:
                return self.build_response(
                    False, f"Missing required field: {field}", None
                )

        success, detail, data = UpsertTask(body).perform()

        return self.build_response(success, detail, data)
