from django.urls import path


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
    TaskUpdateView,
    PositionUpdateView,
    TaskTypeDeleteView,
    TaskDeleteView,
    PositionDeleteView,

)

urlpatterns = [
    path("", index, name="index"),
    path("task-types/",
         TaskTypeListView.as_view(), name="task-type-list"),
    path("task-types/<int:pk>/",
         TaskTypeDetailView.as_view(), name="task-type-detail"),
    path("task-types/create/",
         TaskTypeCreateView.as_view(), name="task-type-create"),
    path("task-types/<int:pk>/update/",
         TaskTypeUpdateView.as_view(), name="task-type-update"),
    path("task-types/<int:pk>/delete/",
         TaskTypeDeleteView.as_view(), name="task-type-delete"),


    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/",
         TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/",
         TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/",
         TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/",
         TaskDeleteView.as_view(), name="task-delete"),


    path("workers/",
         WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/",
         WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/",
         WorkerCreateView.as_view(), name="worker-create"),
    # path("workers<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),


    path("positions/",
         PositionListView.as_view(), name="position-list"),
    path("positions/<int:pk>",
         PositionDetailView.as_view(), name="position-detail"),
    path("positions/create/",
         PositionCreateView.as_view(), name="position-create"),
    path("position/<int:pk>/update/",
         PositionUpdateView.as_view(), name="position-update"),
    path("position/<int:pk>/delete/",
         PositionDeleteView.as_view(), name="position-delete")
]

app_name = "task_manager"
