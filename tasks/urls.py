from django.urls import path
from tasks.views.tasks import Tasks

urlpatterns = [path("", Tasks.as_view(), name="index")]
