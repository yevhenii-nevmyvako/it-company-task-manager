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
    TaskTypeCreateView,
    TaskCreateView,
    WorkerCreateView,
    PositionCreateView,
    TaskTypeUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("task-types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("task-types/<int:pk>/", TaskTypeDetailView.as_view(), name="task-type-detail"),
    path("task-types/create/", TaskTypeCreateView.as_view(), name="task-type-create"),
    path("task-types/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task-type-update"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/<int:pk>", PositionDetailView.as_view(), name="position-detail"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),


]

app_name = "task_manager"
