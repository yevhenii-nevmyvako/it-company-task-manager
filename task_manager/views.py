from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task_manager.forms import WorkerCreationFrom, TaskForm, PositionForm
from task_manager.models import TaskType, Task, Position, Worker


@login_required
def index(request):
    num_tusk_types = TaskType.objects.count()
    num_tusks = Task.objects.count()
    num_positions = Position.objects.count()
    num_workers = Worker.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_tusk_types": num_tusk_types,
        "num_tusks": num_tusks,
        "num_positions": num_positions,
        "num_workers": num_workers,
        "num_visits": num_visits + 1
    }

    return render(request, "task_manager/index.html", context=context)


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "task_manager/task_type_list.html"
    context_object_name = "task_type_list"
    queryset = TaskType.objects.all()
    paginate_by = 5


class TaskTypeDetailView(generic.DetailView):
    model = TaskType
    template_name = "task_manager/task_type_detail.html"
    context_object_name = "task_type"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    template_name = "task_manager/task_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    template_name = "task_manager/task_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "task_manager/task_type_delete_confirm.html"
    context_object_name = "task_type_to_delete"
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    queryset = Task.objects.all().select_related("task_type")
    context_object_name = "task_list"
    paginate_by = 5


class TaskDetailView(generic.DetailView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("task_manager:task-list")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "task_manager/task_delete_confirm.html"
    context_object_name = "task_to_delete"
    success_url = reverse_lazy("task_manager:task-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    queryset = Worker.objects.all().select_related("position")
    paginate_by = 5


class WorkerDetailView(generic.DetailView):
    model = Worker
    queryset = Worker.objects.all().prefetch_related("tasks")


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationFrom
    success_url = reverse_lazy("task_manager:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    template_name = "task_manager/worker_delete_confirm.html"
    success_url = reverse_lazy("task_manager:worker-list")


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    queryset = Position.objects.all()
    context_object_name = "position_list"
    paginate_by = 5


class PositionDetailView(generic.DetailView):
    model = Position


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("task_manager:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("task_manager:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    template_name = "task_manager/position_delete_confirm.html"
    context_object_name = "position_to_delete"
    success_url = reverse_lazy("task_manager:position-list")
