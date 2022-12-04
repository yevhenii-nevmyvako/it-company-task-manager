
from django.shortcuts import render
from django.views import generic

from task_manager.models import TaskType, Task, Position, Worker


def index(request):
    num_tusk_types = TaskType.objects.count()
    num_tusks = Task.objects.count()
    num_positions = Position.objects.count()
    num_workers = Worker.objects.count()

    context = {
        "num_tusk_types": num_tusk_types,
        "num_tusks": num_tusks,
        "num_positions": num_positions,
        "num_workers": num_workers
    }

    return render(request, "task_manager/index.html", context=context)


class TaskTypeListView(generic.ListView):
    model = TaskType
    template_name = "task_manager/task_type_list.html"
    context_object_name = "task_type_list"
    queryset = TaskType.objects.all()


class TaskTypeDetailView(generic.DetailView):
    model = TaskType
    template_name = "task_manager/task_type_detail.html"
    context_object_name = "task_type_detail"


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().select_related("task_type")
    context_object_name = "task_list"


class TaskDetailView(generic.DetailView):
    model = Task


class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    queryset = Worker.objects.all().select_related("position")


class WorkerDetailView(generic.DetailView):
    model = Worker


class PositionListView(generic.ListView):
    model = Position
    queryset = Position.objects.all()
    context_object_name = "position_list"


class PositionDetailView(generic.DetailView):
    model = Position
