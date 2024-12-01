import abc
from typing import Any
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class BaseView(APIView, abc.ABC):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def build_response(self, success: bool, detail: str, data: Any) -> JsonResponse:
        return JsonResponse({"success": success, "detail": detail, "data": data})
