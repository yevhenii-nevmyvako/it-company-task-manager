from django.urls import path
from . import views

from task_manager.views import (
    index,
    TaskTypeListView,
    TaskListView,
    WorkerListView,
    PositionListView,
    TaskTypeDetailView,
    TaskDetailView,
    WorkerDetailView,
    PositionDetailView,
    TaskTypeCreateViews,
    TaskCreateViews,
    WorkerCreateViews
)

urlpatterns = [
    path("", index, name="index"),
    path("task-types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("task-types/<int:pk>/", TaskTypeDetailView.as_view(), name="task-type-detail"),
    path("task-types/create/", TaskTypeCreateViews.as_view(), name="task-type-create"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateViews.as_view(), name="task-create"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", WorkerCreateViews.as_view(), name="worker-create"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("position/<int:pk>", PositionDetailView.as_view(), name="position-detail")


]

app_name = "task_manager"
