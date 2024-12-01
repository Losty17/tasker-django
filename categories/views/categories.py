import json
from django.http import HttpRequest, JsonResponse

from tasker.base.base_view import BaseView


class Categories(BaseView):
    def get(self, request: HttpRequest) -> JsonResponse:

        return self.build_response(True, "", None)

    def post(self, request: HttpRequest) -> JsonResponse:

        return self.build_response(True, "", None)
