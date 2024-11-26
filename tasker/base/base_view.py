import abc
from typing import Any
from django.http import JsonResponse
from django.views import View


class BaseView(View, abc.ABC):
    def build_response(self, success: bool, detail: str, data: Any) -> JsonResponse:
        return JsonResponse({"success": success, "detail": detail, "data": data})
