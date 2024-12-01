from typing import Optional, TypedDict
from categories.models import Category
from tasker.base.service_base import ServiceBase
from django.contrib.auth.models import User


class UserBody(TypedDict):
    id: Optional[int]
    name: str
    email: str
    username: str
    password: Optional[str]


class UpsertUser(ServiceBase):
    def __init__(self, body: UserBody) -> None:
        super().__init__()

        self.__body = body

    def _perform(self):
        user = None
        if self.__body.get("id", None):
            user = User.objects.filter(id=self.__body["id"], deleted=False).first()

            if user is None:
                return False, "User not found", None
        else:
            password = self.__body.get("password", None)

            if password is None:
                return False, "Password is required", None

            user = User.objects.create_user(
                first_name=self.__body["name"],
                username=self.__body["username"],
                password=self.__body["password"],
                email=self.__body.get("email", ""),
            )

            return True, "User created successfully", user

        user.name = self.__body.get("name", user.name)
        user.email = self.__body.get("email", user.email)
        user.username = self.__body.get("username", user.username)
        user.password = self.__body.get("password", user.password)

        user.save()

        return True, "User updated successfully", None
