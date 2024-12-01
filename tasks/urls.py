from django.urls import path
from tasks.views.tasks import Tasks
from tasks.views.tasks_id import TasksId

urlpatterns = [
    path("", Tasks.as_view(), name="index"),
    path("<int:id>", TasksId.as_view(), name="index"),
]
