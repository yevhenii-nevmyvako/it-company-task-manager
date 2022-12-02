from django.http import HttpResponse
from django.shortcuts import render

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
