import json
from tasker.base.base_view import BaseView
from tasks.services.delete_task import DeleteTask
from tasks.services.get_task import GetTask
from tasks.services.upsert_task import UpsertTask


class TasksId(BaseView):
    def get(self, request, id: int):
        success, detail, data = GetTask(id).perform()

        return self.build_response(success, detail, data)

    def post(self, request, id: int):
        if not id:
            return self.build_response(False, "Invalid task id", None)

        body = json.loads(request.body)
        body["id"] = id

        success, detail, data = UpsertTask(body).perform()

        return self.build_response(success, detail, data)

    def delete(self, request, id: int):
        if not id:
            return self.build_response(False, "Invalid task id", None)

        success, detail, data = DeleteTask(id).perform()

        return self.build_response(success, detail, data)
