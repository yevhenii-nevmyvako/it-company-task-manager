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
    WorkerDeleteView,
    WorkerPositionUpdateView,
    assign_worker_to_task,
    delete_worker_from_task,
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    TeamListView,
    TeamDetailView,
    TeamCreateView,

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
    path("workers/<int:pk>/delete/",
         WorkerDeleteView.as_view(), name="worker-delete"),
    path("workers/<int:pk>/update/",
         WorkerPositionUpdateView.as_view(), name="worker-position-update"),
    path("workers/<int:pk>/assign_worker_to_task",
         assign_worker_to_task, name="worker-assign-to-task"),
    path("workers/<int:pk>/delete_worker_from_task",
         delete_worker_from_task, name="worker-delete-from-task"),


    path("positions/",
         PositionListView.as_view(), name="position-list"),
    path("positions/<int:pk>/",
         PositionDetailView.as_view(), name="position-detail"),
    path("positions/create/",
         PositionCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/update/",
         PositionUpdateView.as_view(), name="position-update"),
    path("positions/<int:pk>/delete/",
         PositionDeleteView.as_view(), name="position-delete"),


    path("projects/",
         ProjectListView.as_view(), name="project-list"),
    path("projects/<int:pk>/",
         ProjectDetailView.as_view(), name="project-detail"),
    path("projects/create/",
         ProjectCreateView.as_view(), name="project-create"),
    path("projects/<int:pk>/update/",
         ProjectUpdateView.as_view(), name="project-update"),
    path("projects/<int:pk>/delete/",
         ProjectDeleteView.as_view(), name="project-delete"),


    path("teams/",
         TeamListView.as_view(), name="team-list"),
    path("teams/<int:pk>/",
         TeamDetailView.as_view(), name="team-detail"),
    path("teams/create/",
         TeamCreateView.as_view(), name="team-create")
]

app_name = "task_manager"
