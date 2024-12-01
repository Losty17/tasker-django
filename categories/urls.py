from django.urls import path
from categories.views.categories import Categories

urlpatterns = [path("", Categories.as_view(), name="index")]
