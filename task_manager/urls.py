from django.urls import path

from task_manager.views import index

urlpatterns = [
    path("", index)
]

app_name = "task_manager"