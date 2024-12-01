from django.urls import path

from core.views.users import Users


urlpatterns = [
    path("users/", Users.as_view()),
]
