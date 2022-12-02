from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from task_manager.models import TaskType, Task, Position, Worker


class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(TaskType, TaskTypeAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ["is_completed", "priority", "task_type", "deadline"]


admin.site.register(Task, TaskAdmin)


class PositionAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Position, PositionAdmin)

admin.site.register(Worker, UserAdmin)
